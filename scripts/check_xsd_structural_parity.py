#!/usr/bin/env python3
"""
Check that the committed ASAM UML model produces the same schema content as ASAM's
independently published, normative XSD.

Regenerates an XSD from ``standards/<standard>/uml/<standard>.scxml`` with a dedicated
ShapeChange XML Schema target configuration, then compares its structural inventory -
elements, attributes, complexTypes, simpleTypes and enumeration values, counted at any
nesting depth - against the corresponding files in ``standards/<standard>/schema/``. This
is not a byte diff: the two schemas use different naming and structuring conventions by
design (see ``pipeline/opendrive-xsd.config.xml``), so the comparison counts constructs,
not text.

This is the "XSD equivalence oracle" named as future work in ``pipeline/README.md``, in
its narrower, currently built form: a structural check between two independently produced
schemas, rather than validating shared instance data against both. Enumeration values are
the strongest signal it produces, because a missing enumeration - the exact regression
``pipeline/README.md`` describes for the OWL stage - would show up here as a per-file
enumeration-value count that stops matching the official schema.

Usage
-----
::

    python scripts/check_xsd_structural_parity.py \\
        --standard asam-opendrive \\
        --shapechange ../ShapeChange

Run ``--help`` for the full argument list. See ``pipeline/README.md`` for how to obtain
ShapeChange and how this check relates to the OWL/SHACL generation stages.

Exit status
-----------
Non-zero if ShapeChange fails to build or run, if its log contains an error or
union-encoding warning outside the set ``check_shapechange_log()`` already tolerates (see
``generate_semantic_artifacts.py``), or if any file's enumeration-value count does not
match the official schema exactly - that count is the one invariant this check exists to
guarantee. Differences in element, attribute, complexType or simpleType counts are
reported but do not fail the run: they reflect a known, documented style difference
(ASAM's XSD favours XML attributes; the UML model carries no ``xsdEncodingRule`` tagged
value selecting attribute encoding for any property, so ShapeChange renders them as
elements instead), not a correctness regression.
"""

from __future__ import annotations

import argparse
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from generate_semantic_artifacts import (
    REPO_ROOT,
    STANDARDS,
    build_shapechange,
    check_shapechange_log,
    run,
    shapechange_classpath,
    shapechange_log,
)

XS = "{http://www.w3.org/2001/XMLSchema}"

#: Structural counts taken across the whole document (any nesting depth), so a
#: property's inline anonymous type is counted along with top-level declarations.
METRICS = ("all_elements", "all_attributes", "all_enumeration_values", "all_complexTypes", "all_simpleTypes")


def inventory(path: Path) -> dict[str, int]:
    """Count XSD constructs in a schema file, at any nesting depth."""
    root = ET.parse(path).getroot()
    return {
        "all_elements": len(root.findall(f".//{XS}element")),
        "all_attributes": len(root.findall(f".//{XS}attribute")),
        "all_enumeration_values": len(root.findall(f".//{XS}enumeration")),
        "all_complexTypes": len(root.findall(f".//{XS}complexType")),
        "all_simpleTypes": len(root.findall(f".//{XS}simpleType")),
    }


def generate_xsd(spec: dict, classpath: str, resources: Path, work: Path) -> Path:
    """Regenerate the XSD from the committed SCXML with the dedicated XSD target config.

    This is a verification artifact, not a pipeline deliverable: it is written under
    ``work``, never under ``standards/<standard>/generated/``, and is not committed.
    """
    print("• generating XSD from the committed SCXML model (structural check only, not committed)")
    template = (REPO_ROOT / spec["xsd_config"]).read_text()
    out_dir = work / "xsd"
    out_dir.mkdir(parents=True, exist_ok=True)
    config = work / "shapechange-xsd.config.xml"
    config.write_text(
        template.replace("{SHAPECHANGE_RESOURCES}", str(resources))
        .replace("{PIPELINE}", str(REPO_ROOT / "pipeline"))
        .replace("{OUT}", str(out_dir))
    )
    run(["java", "-cp", classpath,
         "de.interactive_instruments.shapechange.app.Main", "-c", str(config)],
        cwd=REPO_ROOT, what="ShapeChange XSD generation")
    # Same reasoning as the OWL stage: a 0 exit code does not mean the run was clean, so the
    # log is parsed and any error or union-encoding warning outside the already-documented set
    # fails the build rather than shipping a silently incomplete comparison.
    check_shapechange_log(shapechange_log(config), spec, stage="xsd")

    # ShapeChange nests output under a subdirectory named after the pseudo-package that
    # wraps the input model (observed as "INPUT"); searched recursively rather than
    # relying on that name, since it is not a documented, stable contract.
    if not sorted(out_dir.rglob("*.xsd")):
        raise SystemExit("ShapeChange produced no XSD output; see the log in the work directory")
    return out_dir


def compare(generated_dir: Path, official_dir: Path, prefix: str) -> bool:
    """Print the structural comparison and report whether enumeration values match exactly."""
    pairs = []
    for generated in sorted(generated_dir.rglob("*.xsd")):
        # Two naming conventions are in use among ASAM's published schemas: a multi-document
        # standard prefixes each file with the standard's name (OpenDRIVE_Core.xsd), while a
        # single-document standard publishes one file named after the standard itself
        # (OpenSCENARIO.xsd). Both are tried rather than configured per standard, because the
        # generated document is named by the configuration in either case and a mismatch is
        # reported below with both candidates.
        candidates = [official_dir / f"{prefix}_{generated.stem}.xsd", official_dir / f"{generated.stem}.xsd"]
        official = next((c for c in candidates if c.exists()), None)
        if official is None:
            raise SystemExit(
                f"no official counterpart for {generated.name}: tried "
                + ", ".join(str(c) for c in candidates)
            )
        pairs.append((generated, official))
    if not pairs:
        raise SystemExit(f"no generated .xsd files found under {generated_dir}")

    totals_gen: dict[str, int] = defaultdict(int)
    totals_off: dict[str, int] = defaultdict(int)
    enumerations_match = True

    print(f"{'File':<10} {'Metric':<24} {'Generated':>10} {'Official':>10} {'Diff':>8}")
    print("-" * 66)
    for generated, official in pairs:
        gen_counts = inventory(generated)
        off_counts = inventory(official)
        if gen_counts["all_enumeration_values"] != off_counts["all_enumeration_values"]:
            enumerations_match = False
        for metric in METRICS:
            totals_gen[metric] += gen_counts[metric]
            totals_off[metric] += off_counts[metric]
            print(f"{generated.stem:<10} {metric:<24} {gen_counts[metric]:>10} "
                  f"{off_counts[metric]:>10} {gen_counts[metric] - off_counts[metric]:>8}")
        print()

    print("=" * 66)
    print(f"TOTALS across all {len(pairs)} files:")
    for metric in METRICS:
        print(f"{'TOTAL':<10} {metric:<24} {totals_gen[metric]:>10} "
              f"{totals_off[metric]:>10} {totals_gen[metric] - totals_off[metric]:>8}")

    return enumerations_match


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    checkable = sorted(name for name, spec in STANDARDS.items() if "xsd_config" in spec)
    parser.add_argument("--standard", choices=checkable, default=checkable[0] if checkable else None)
    parser.add_argument("--shapechange", type=Path, required=True,
                        help="ShapeChange checkout, built here with -DskipEa")
    parser.add_argument("--mvn", default="mvn", help="Maven executable (default: mvn)")
    parser.add_argument("--work", type=Path, default=Path(".pipeline-work"),
                        help="scratch directory for build output (default: .pipeline-work)")
    args = parser.parse_args()

    if not args.shapechange.exists():
        raise SystemExit(f"--shapechange does not exist: {args.shapechange}")

    spec = STANDARDS[args.standard]
    work = (REPO_ROOT / args.work).resolve()
    work.mkdir(parents=True, exist_ok=True)

    resources = build_shapechange(args.shapechange.resolve(), args.mvn)
    classpath = shapechange_classpath(args.shapechange.resolve(), args.mvn, work)
    generated_dir = generate_xsd(spec, classpath, resources, work)

    official_dir = REPO_ROOT / spec["xsd_schema_dir"]
    enumerations_match = compare(generated_dir, official_dir, spec["xsd_prefix"])

    if not enumerations_match:
        print("\nFAIL: enumeration-value counts do not match the official schema exactly.")
        return 1
    print("\nPASS: enumeration-value counts match the official schema exactly, file by file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
