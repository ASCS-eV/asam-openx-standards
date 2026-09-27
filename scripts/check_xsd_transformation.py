#!/usr/bin/env python3
"""
Check that each normative XML Schema is what ASAM's model says it is.

ASAM derives the XSD of OpenDRIVE and OpenSCENARIO XML from the UML model in its Enterprise
Architect project. This check derives it again, without EA, and compares the result with the
published schema, twice per standard:

**From the EA project** (``standards/<std>/uml/source/*.qeax``), the normative source. The
derivation is ASAM's own where ASAM ships it: the OpenSCENARIO project contains the JScript that
writes its schema, and ``osc_xsd_transformation.py`` ports it. That script is committed next to
the project, and this check fails unless its bytes are the project's ``t_script``. Run on the
project, the port must reproduce ``OpenSCENARIO.xsd`` **byte for byte**. OpenDRIVE's project
contains no generator, so ``odr_xsd_transformation.py`` derives the schema from EA's XML Schema
profile, which the project applies. Its output is compared with the seven published documents
by ``xsd_equivalence.py``, component by component.

**From the committed SCXML** (``standards/<std>/uml/<std>.scxml``), which every generated
artifact in this repository is built from. The same derivation run on the export instead of the
project shows which of the facts the schema depends on the export does not carry.

Every difference is a finding named by document, rule and component. Gating is by baseline, as
for the repository's other model checks: ``pipeline/<artifact>-xsd-transformation-baseline.json``
records the findings accepted today, per source. A finding outside it fails the run; with
``--strict-baseline`` so does a baseline entry that no longer occurs. The target for the EA
project is zero: a finding there is a difference between ASAM's model and ASAM's schema. The
target for the SCXML is the EA project's own findings.

Usage
-----
::

    python scripts/check_xsd_transformation.py                     # both standards
    python scripts/check_xsd_transformation.py --standard asam-opendrive
    python scripts/check_xsd_transformation.py --write-baseline    # after reviewing

Exit status
-----------
Non-zero if a finding is not in the baseline, if the OpenSCENARIO port does not reproduce the
normative schema byte for byte from the EA project, if the committed generator script is not the
project's, if a document is not produced at all, if a ``.qeax`` is not an SQLite database, or,
with ``--strict-baseline``, if a baseline entry no longer occurs.
"""

from __future__ import annotations

import argparse
import importlib
import json
import sqlite3
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

from ea_api import NotAnEaProject, open_qeax, open_scxml
from generate_semantic_artifacts import REPO_ROOT, STANDARDS
from xsd_equivalence import compare_schemas

SOURCES = ("qeax", "scxml")


def ea_script(qeax: Path, name: str) -> bytes | None:
    """The body of the project's ``t_script`` entry named ``name``, as EA stores it."""
    db = sqlite3.connect(f"file:{qeax}?mode=ro", uri=True)
    try:
        for notes, script in db.execute("SELECT Notes, Script FROM t_script"):
            if f'Name="{name}"' in (notes or ""):
                return (script or "").encode("utf-8")
    finally:
        db.close()
    return None


def findings_for(documents: list[tuple], normative: dict[str, ET.Element],
                 pairing: dict[str, str], errors: list[str]) -> list[str]:
    """Finding keys for one run. ``pairing`` maps a package to the normative file it writes."""
    keys = [f"model error: {message}" for message in errors]
    produced = {}
    for package, file_name, root, _ in documents:
        produced[pairing.get(package, file_name)] = root
    for file_name, reference in sorted(normative.items()):
        root = produced.get(file_name)
        if root is None:
            keys.append(f"{file_name}: MISSING document")
            continue
        keys.extend(f"{file_name}: {f.verdict} {f.key}" for f in compare_schemas(root, reference))
    for file_name in sorted(set(produced) - set(normative)):
        keys.append(f"{file_name}: EXTRA document")
    return sorted(set(keys))


def check_standard(name: str, spec: dict, write_baseline: bool, strict_baseline: bool,
                   limit: int) -> bool:
    qeax = REPO_ROOT / spec["ea_project"]
    scxml = REPO_ROOT / spec["model"]
    schema_dir = REPO_ROOT / spec["xsd_schema_dir"]
    baseline_path = REPO_ROOT / spec["xsd_transformation_baseline"]
    module = importlib.import_module(spec["xsd_transformation"])
    ok = True
    print(f"\n=== {name}: {spec['xsd_transformation']}.py against "
          f"{schema_dir.relative_to(REPO_ROOT)}/")

    normative_bytes = {p.name: p.read_bytes() for p in sorted(schema_dir.glob("*.xsd"))}
    normative = {n: ET.fromstring(b) for n, b in normative_bytes.items()}
    try:
        repository = open_qeax(qeax)
    except NotAnEaProject as error:
        print(f"FAIL: {error}")
        return False

    script = spec.get("xsd_transformation_script")
    if script:
        committed = (REPO_ROOT / script).read_bytes()
        stored = ea_script(qeax, spec["xsd_transformation_script_name"])
        if stored != committed:
            ok = False
            print(f"FAIL: {script} is not the script "
                  f"{spec['xsd_transformation_script_name']!r} in {qeax.name}")
        else:
            print(f"generator: {script} is the project's t_script entry "
                  f"{spec['xsd_transformation_script_name']!r} ({len(committed):,} bytes)")

    current: dict[str, list[str]] = {}
    ea_documents = module.documents(repository)
    pairing = {package: file_name for package, file_name, _, _ in ea_documents}
    for package, file_name, _, text in ea_documents:
        if text is None:
            continue
        identical = text.encode("utf-8") == normative_bytes.get(file_name)
        print(f"from the EA project: {file_name} byte-identical: {identical}")
        if not identical:
            ok = False
            print(f"FAIL: the port of ASAM's generator no longer reproduces {file_name}")
    current["qeax"] = findings_for(ea_documents, normative, pairing, [])

    errors: list[str] = []
    current["scxml"] = findings_for(module.documents(open_scxml(scxml), errors), normative,
                                    pairing, errors)

    for source in SOURCES:
        tally = Counter("model error" if key.startswith("model error: ")
                        else key.split(": ", 1)[1].split(":")[0] for key in current[source])
        print(f"\nfrom the {'EA project' if source == 'qeax' else 'SCXML export'}: "
              f"{len(current[source])} finding(s)")
        for rule, count in sorted(tally.items()):
            print(f"  {rule:<44} {count:>5}")

    if write_baseline:
        baseline_path.write_text(json.dumps(current, indent=1, sort_keys=True) + "\n")
        print(f"\nwrote baseline {baseline_path.relative_to(REPO_ROOT)}")
        return ok
    if not baseline_path.exists():
        print(f"\nFAIL: no baseline at {baseline_path.relative_to(REPO_ROOT)}; create it with "
              "--write-baseline after reviewing the findings above.")
        return False
    baseline = json.loads(baseline_path.read_text())
    if not isinstance(baseline, dict) or set(baseline) - set(SOURCES) or not all(
            isinstance(v, list) and all(isinstance(k, str) for k in v) for v in baseline.values()):
        print(f"\nFAIL: {baseline_path.relative_to(REPO_ROOT)} is not a list of finding keys "
              f"per source {SOURCES}")
        return False
    for source in SOURCES:
        recorded, found = set(baseline.get(source, [])), set(current[source])
        appeared, resolved = sorted(found - recorded), sorted(recorded - found)
        if appeared:
            ok = False
            print(f"\nFAIL: {len(appeared)} new finding(s) from the {source} not in the baseline:")
            for key in appeared[:limit]:
                print(f"  {key}")
            if len(appeared) > limit:
                print(f"  ... and {len(appeared) - limit} more")
        if resolved:
            if strict_baseline:
                ok = False
            print(f"\n{'FAIL: ' if strict_baseline else ''}{len(resolved)} baseline finding(s) "
                  f"from the {source} no longer occur; re-record with --write-baseline:")
            for key in resolved[:limit]:
                print(f"  {key}")
    if ok:
        print(f"\nPASS: every difference from the normative schema is recorded in the baseline "
              f"(EA project {len(current['qeax'])}, SCXML {len(current['scxml'])}).")
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    checkable = sorted(n for n, spec in STANDARDS.items() if "xsd_transformation" in spec)
    parser.add_argument("--standard", choices=checkable, action="append",
                        help="standard to check (repeatable; default: every standard)")
    parser.add_argument("--write-baseline", action="store_true",
                        help="record the current findings as the accepted baseline")
    parser.add_argument("--strict-baseline", action="store_true",
                        help="also fail when a baseline finding no longer occurs (for CI)")
    parser.add_argument("--limit", type=int, default=40,
                        help="findings printed per source when gating fails (default: 40)")
    args = parser.parse_args()
    ok = True
    for name in args.standard or checkable:
        ok = check_standard(name, STANDARDS[name], args.write_baseline, args.strict_baseline,
                            args.limit) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
