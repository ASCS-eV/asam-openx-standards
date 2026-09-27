#!/usr/bin/env python3
"""
Check that the generated SHACL shapes say what the model's schema says.

``check_xsd_transformation.py`` establishes what each model means in XML Schema terms: the
schema derived from ASAM's EA project is the normative one, up to the differences it records.
This check takes the same derivation, with the record of which UML property each schema
declaration stands for, and compares the committed SHACL shapes with it, class by class, in
terms of the graph a conforming document becomes: which properties a node may carry, how many
values each takes, of what type, and which of them exclude each other. See
``shacl_equivalence.py`` for the reading of both sides.

A finding is a difference in what a conforming instance may be. The shapes can be stricter than
the schema (a closed shape without a property the schema declares, a lower bound the schema does
not have, a choice encoded as a conjunction), which makes them reject conforming documents; or
looser (a property or choice the schema does not have), which makes them accept documents the
schema rejects. Gating is by baseline, as for the other model checks:
``pipeline/<artifact>-shacl-equivalence-baseline.json`` records the findings accepted today,
and the target is zero.

Usage
-----
::

    python scripts/check_shacl_equivalence.py                      # both standards
    python scripts/check_shacl_equivalence.py --shacl other.ttl --standard asam-opendrive
    python scripts/check_shacl_equivalence.py --write-baseline     # after reviewing
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from collections import Counter
from pathlib import Path

import rdflib

from ea_api import NotAnEaProject, open_qeax
from generate_semantic_artifacts import REPO_ROOT, STANDARDS
from shacl_equivalence import ValueTypes, compare, expected_content, load_map_entries, shapes

MAP_ENTRIES = REPO_ROOT / "pipeline" / "mapentries-asam.xml"


def namespace_of(shacl: rdflib.Graph, artifact: str) -> str:
    """The namespace the OWL target wrote the standard's classes in."""
    for _, uri in shacl.namespaces():
        if str(uri).rstrip("#/").endswith(f"/{artifact}"):
            return str(uri)
    raise SystemExit(f"no namespace for {artifact} in the shapes")


def findings_for(spec: dict, shacl_path: Path, project: Path | None = None) -> list[str]:
    """``project`` is the EA project the shapes were built from; ASAM's by default."""
    module = importlib.import_module(spec["xsd_transformation"])
    bindings: dict = {}
    repository = open_qeax(project or REPO_ROOT / spec["ea_project"])
    documents = [d[2] for d in module.documents(repository, None, bindings)]
    graph = rdflib.Graph().parse(shacl_path)
    namespace = namespace_of(graph, spec["artifact"])
    value_types = ValueTypes(documents, namespace, load_map_entries(MAP_ENTRIES))
    expected = expected_content(documents, bindings, namespace, value_types)
    return sorted({f.key for f in compare(expected, shapes(graph), namespace)})


def check_standard(name: str, spec: dict, shacl_path: Path, write_baseline: bool,
                   strict_baseline: bool, limit: int, project: Path | None = None) -> bool:
    baseline_path = REPO_ROOT / spec["shacl_equivalence_baseline"]
    inside = shacl_path.is_relative_to(REPO_ROOT)
    shown = shacl_path.relative_to(REPO_ROOT) if inside else shacl_path
    print(f"\n=== {name}: {shown}")
    try:
        current = findings_for(spec, shacl_path, project)
    except NotAnEaProject as error:
        print(f"FAIL: {error}")
        return False
    for rule, count in sorted(Counter(k.split(":")[0] for k in current).items()):
        print(f"  {rule:<24} {count:>5}")
    print(f"  {'total':<24} {len(current):>5}")
    if write_baseline:
        baseline_path.write_text(json.dumps(current, indent=1) + "\n")
        print(f"wrote baseline {baseline_path.relative_to(REPO_ROOT)}")
        return True
    if not baseline_path.exists():
        print(f"FAIL: no baseline at {baseline_path.relative_to(REPO_ROOT)}")
        return False
    recorded = json.loads(baseline_path.read_text())
    if not isinstance(recorded, list) or not all(isinstance(k, str) for k in recorded):
        print(f"FAIL: {baseline_path.relative_to(REPO_ROOT)} is not a list of finding keys")
        return False
    appeared = sorted(set(current) - set(recorded))
    resolved = sorted(set(recorded) - set(current))
    ok = not appeared and not (strict_baseline and resolved)
    for label, keys in (("new finding(s) not in the baseline", appeared),
                        ("baseline finding(s) no longer occur; re-record with --write-baseline",
                         resolved)):
        if keys:
            print(f"\n{len(keys)} {label}:")
            for key in keys[:limit]:
                print(f"  {key}")
    print("\nPASS" if ok else "\nFAIL", f"({len(current)} finding(s))")
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    checkable = sorted(n for n, spec in STANDARDS.items() if "shacl_equivalence_baseline" in spec)
    parser.add_argument("--standard", choices=checkable, action="append")
    parser.add_argument("--shacl", type=Path,
                        help="shapes to check instead of the committed ones (one standard)")
    parser.add_argument("--project", type=Path,
                        help="the EA project the shapes were built from (with --shacl)")
    parser.add_argument("--write-baseline", action="store_true")
    parser.add_argument("--strict-baseline", action="store_true")
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args()
    names = args.standard or checkable
    if args.shacl and len(names) != 1:
        parser.error("--shacl needs exactly one --standard")
    ok = True
    for name in names:
        spec = STANDARDS[name]
        shacl = args.shacl or REPO_ROOT / "standards" / name / "generated" / \
            f"{spec['artifact']}.shacl.ttl"
        ok = check_standard(name, spec, shacl, args.write_baseline, args.strict_baseline,
                            args.limit, args.project) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
