#!/usr/bin/env python3
"""
Check that each committed SCXML model is the same model as the ASAM Enterprise Architect
project it was exported from.

The export from ``standards/<std>/uml/source/*.qeax`` to ``standards/<std>/uml/<std>.scxml``
is the only pipeline step that needs an Enterprise Architect licence, so it is run once and
its output committed, and everything downstream trusts that output. This check reads both
files - the ``.qeax`` as the SQLite database it is, the SCXML as XML - and compares them fact
by fact with ``model_equivalence.py``. No EA, no ShapeChange, no JDK: it runs in a pull-request
workflow.

Gating is by baseline, as for the content-model check in ``check_xsd_structural_parity.py``:
each standard has ``pipeline/<artifact>-model-equivalence-baseline.json`` recording the
findings accepted today. A finding outside it fails the run. A baseline entry that no longer
occurs is reported, and with ``--strict-baseline`` fails the run too, so a fix that makes the
export more faithful has to record that in the same change. The baseline is not a tolerance:
every entry is a known difference between ASAM's model and the model this repository builds
on, and the target for every rule is zero.

Usage
-----
::

    python scripts/check_model_equivalence.py                      # both standards
    python scripts/check_model_equivalence.py --standard asam-opendrive
    python scripts/check_model_equivalence.py --write-baseline     # after reviewing

Exit status
-----------
Non-zero if a finding is not in the baseline, if a baseline is missing, if either side of a
comparison is empty or the two share no element (``VacuousComparison``), if a ``.qeax`` is not
an SQLite database (typically a Git LFS pointer), or - with ``--strict-baseline`` - if a
baseline entry no longer occurs.
"""

from __future__ import annotations

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from generate_semantic_artifacts import REPO_ROOT, STANDARDS
from model_equivalence import (
    VERDICTS,
    NotAnEaProject,
    VacuousComparison,
    compare,
    group,
    read_qeax,
    read_scxml,
    summarize,
)


def baseline_problem(baseline) -> str | None:
    """Why a baseline file cannot be gated on, or None when it can."""
    if not isinstance(baseline, dict):
        return "is not an object of verdicts"
    unknown = sorted(set(baseline) - set(VERDICTS))
    if unknown:
        return f"records verdicts this check does not produce: {unknown}"
    for verdict, keys in baseline.items():
        if not isinstance(keys, list) or not all(isinstance(k, str) for k in keys):
            return f"records {verdict} as something other than a list of finding keys"
        repeated = sorted({k for k in keys if keys.count(k) > 1})
        if repeated:
            return f"records {len(repeated)} {verdict} finding(s) twice, e.g. {repeated[0]!r}"
    return None


def check_standard(name: str, spec: dict, write_baseline: bool, strict_baseline: bool,
                   limit: int) -> tuple[bool, dict | None]:
    """Compare one standard's EA project with its SCXML and gate on the baseline."""
    qeax = REPO_ROOT / spec["ea_project"]
    scxml = REPO_ROOT / spec["model"]
    baseline_path = REPO_ROOT / spec["model_equivalence_baseline"]

    try:
        model = read_qeax(qeax)
        export = read_scxml(scxml)
        findings = compare(model, export)
    except (NotAnEaProject, VacuousComparison, ET.ParseError, OSError) as error:
        print(f"\n=== {name}\nFAIL: {error}")
        return False, None
    current = group(findings)
    counts = {verdict: len(keys) for verdict, keys in current.items()}

    print(f"\n=== {name}: {qeax.relative_to(REPO_ROOT)}  vs  {scxml.relative_to(REPO_ROOT)}")
    print(f"model  : {len(model.packages)} packages, {len(model.classifiers)} classifiers, "
          f"{len(model.attributes)} attributes, {len(model.associations)} associations, "
          f"{len(model.generalizations)} generalizations, {len(model.realizations)} "
          f"realizations, {sum(len(c) for c in model.constraints.values())} constraints")
    print(f"export : {len(export.packages)} packages, {len(export.classifiers)} classes, "
          f"{len(export.attributes)} attributes, {len(export.associations)} associations")
    print("\nfindings by rule:")
    for (verdict, rule), count in sorted(summarize(findings).items()):
        print(f"  {verdict:<9} {rule:<34} {count:>5}")
    print(f"  {'total':<44} {len(findings):>5}")

    if model.out_of_scope:
        print("\nread but out of scope (not UML model content):")
        for category, count in sorted(model.out_of_scope.items()):
            print(f"  {category:<44} {count:>5}")
        for oid, text in model.diagram_texts:
            print(f"    diagram text {oid}: {text!r}")
    if model.normalized:
        print("\nnormalizations applied (see the module docstring):")
        for category, count in sorted(model.normalized.items()):
            print(f"  {category:<66} {count:>5}")
    if model.empty_tags:
        print("\ntagged values declared without a value (equal to absent; counted per owner):")
        for (kind, tag), count in sorted(model.empty_tags.items()):
            print(f"  {kind + ' ' + tag:<44} {count:>5}")

    if write_baseline:
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        baseline_path.write_text(json.dumps(current, indent=1, sort_keys=True) + "\n")
        print(f"\nwrote baseline {baseline_path.relative_to(REPO_ROOT)} ({len(findings)} findings)")
        return True, counts

    if not baseline_path.exists():
        print(f"\nFAIL: no baseline at {baseline_path.relative_to(REPO_ROOT)}. Create it with "
              "--write-baseline after reviewing the findings above.")
        return False, counts

    baseline = json.loads(baseline_path.read_text())
    problem = baseline_problem(baseline)
    if problem:
        print(f"\nFAIL: {baseline_path.relative_to(REPO_ROOT)} {problem}")
        return False, counts
    ok = True
    for verdict in VERDICTS:
        recorded = set(baseline.get(verdict, []))
        found = set(current[verdict])
        appeared = sorted(found - recorded)
        resolved = sorted(recorded - found)
        if appeared:
            ok = False
            print(f"\nFAIL: {len(appeared)} new {verdict} finding(s) not in the baseline:")
            for key in appeared[:limit]:
                print(f"  {key}")
            if len(appeared) > limit:
                print(f"  ... and {len(appeared) - limit} more")
        if resolved:
            if strict_baseline:
                ok = False
                print(f"\nFAIL: {len(resolved)} baseline {verdict} finding(s) no longer occur. "
                      "The export is closer to the model, but the baseline still records "
                      "them; re-record it with --write-baseline:")
            else:
                print(f"\n{len(resolved)} baseline {verdict} finding(s) no longer occur - "
                      "tighten the baseline in this change (--write-baseline):")
            for key in resolved[:limit]:
                print(f"  {key}")
            if len(resolved) > limit:
                print(f"  ... and {len(resolved) - limit} more")
    if ok:
        print(f"\nPASS: every difference between the SCXML and the EA model ({len(findings)}) "
              "is recorded in the baseline.")
    return ok, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    checkable = sorted(name for name, spec in STANDARDS.items() if "ea_project" in spec)
    parser.add_argument("--standard", choices=checkable, action="append",
                        help="standard to check (repeatable; default: every standard)")
    parser.add_argument("--write-baseline", action="store_true",
                        help="record the current findings as the accepted baseline instead of "
                             "checking against it")
    parser.add_argument("--strict-baseline", action="store_true",
                        help="also fail when a baseline finding no longer occurs, so that an "
                             "improvement must re-record the baseline in the same change "
                             "(intended for CI)")
    parser.add_argument("--limit", type=int, default=40,
                        help="findings printed per verdict when gating fails (default: 40)")
    parser.add_argument("--summary-json", type=Path,
                        help="write the per-verdict finding counts here")
    args = parser.parse_args()

    results = {}
    all_ok = True
    compared = True
    for name in args.standard or checkable:
        ok, counts = check_standard(name, STANDARDS[name], args.write_baseline,
                                    args.strict_baseline, args.limit)
        all_ok = all_ok and ok
        if counts is None:
            compared = False  # nothing was compared, so there is no size to report
            continue
        results[name] = {"findings": counts, "total": sum(counts.values()),
                         "within_baseline": ok}

    if args.summary_json and compared:
        args.summary_json.parent.mkdir(parents=True, exist_ok=True)
        args.summary_json.write_text(json.dumps(results, indent=1, sort_keys=True) + "\n")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
