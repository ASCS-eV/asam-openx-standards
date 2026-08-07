#!/usr/bin/env python3
"""Regression tests for ``xsd_content_model.py``.

Every test here exists because an earlier version of the comparison produced a confident
wrong answer. That is the point: this comparison is the oracle the model, configuration and
tool changes are judged against, so a plausible-looking number it reports has to be
trustworthy. Three of the cases below each produced hundreds of phantom findings.

No JDK, no Maven, no ShapeChange: the schemas are written inline, so this runs in a cheap
workflow on every pull request.

Run:  python scripts/test_xsd_content_model.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

from xsd_content_model import (
    Schema,
    VacuousComparison,
    compare,
    degen,
    load,
    load_map_entries,
)

HEAD = ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">\n')
TAIL = "</xs:schema>\n"

FAILURES: list[str] = []


def check(condition: bool, what: str) -> None:
    if condition:
        print(f"  ok   {what}")
    else:
        print(f"  FAIL {what}")
        FAILURES.append(what)


def run(reference_body: str, generated_body: str,
        map_entries_body: str | None = None) -> dict[str, list[tuple]]:
    """Compare two inline schemas and return the findings."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "ref").mkdir()
        (root / "gen").mkdir()
        (root / "ref" / "S.xsd").write_text(HEAD + reference_body + TAIL)
        (root / "gen" / "S.xsd").write_text(HEAD + generated_body + TAIL)
        entries = {}
        if map_entries_body is not None:
            path = root / "map.xml"
            path.write_text(f'<xsdMapEntries>{map_entries_body}</xsdMapEntries>')
            entries = load_map_entries(path)
        return compare(
            Schema(sorted((root / "gen").glob("*.xsd")), generated=True),
            Schema(sorted((root / "ref").glob("*.xsd")), generated=False, map_entries=entries),
        )


def counts(findings: dict) -> dict[str, int]:
    return {k: len(v) for k, v in findings.items() if k != "shared_types"}


# ---------------------------------------------------------------------------------------
print("degen() strips exactly one ShapeChange suffix and nothing else")
check(degen("t_roadType") == "t_road", "t_roadType -> t_road")
check(degen("t_roadPropertyType") == "t_road", "t_roadPropertyType -> t_road")
check(degen("e_roadTypeType") == "e_roadType", "e_roadTypeType -> e_roadType (one suffix only)")
check(degen("e_roadType") == "e_road", "degen is unconditional; callers must not apply it "
                                       "to the reference side")

# ---------------------------------------------------------------------------------------
print("\nan ASAM type name that genuinely ends in 'Type' is not a mismatch")
# Was: 141 phantom TYPE_MISMATCH findings, from stripping the suffix on both sides.
findings = run(
    reference_body='<xs:complexType name="t_x">'
                   '<xs:attribute name="type" type="e_roadType" use="required"/>'
                   "</xs:complexType>",
    generated_body='<xs:complexType name="t_xType">'
                   '<xs:sequence><xs:element name="type" type="e_roadTypeType"/></xs:sequence>'
                   "</xs:complexType>",
)
check(counts(findings)["TYPE_MISMATCH"] == 0,
      f"e_roadType vs e_roadTypeType is not a mismatch (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\nthe empty PropertyType wrapper does not win the pairing")
# Was: every particle of every type reported MISSING, because the wrapper carries none.
findings = run(
    reference_body='<xs:complexType name="t_x">'
                   '<xs:sequence><xs:element name="child" type="t_y"/></xs:sequence>'
                   "</xs:complexType>",
    generated_body='<xs:complexType name="t_xPropertyType"/>'
                   '<xs:complexType name="t_xType">'
                   '<xs:sequence><xs:element name="child" type="t_yPropertyType"/></xs:sequence>'
                   "</xs:complexType>",
)
check(counts(findings)["MISSING"] == 0,
      f"content type wins over the wrapper (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\na required attribute equals a mandatory element; an optional one does not")
# Was: 174 phantom CONTRADICTS, from defaulting an attribute's minOccurs to 1.
findings = run(
    reference_body='<xs:complexType name="t_x">'
                   '<xs:attribute name="a" type="xs:string" use="required"/>'
                   "</xs:complexType>",
    generated_body='<xs:complexType name="t_xType">'
                   '<xs:sequence><xs:element name="a" type="xs:string"/></xs:sequence>'
                   "</xs:complexType>",
)
check(counts(findings)["CONTRADICTS"] == 0,
      f"use=required vs mandatory element is not a contradiction (got {counts(findings)})")

findings = run(
    reference_body='<xs:complexType name="t_x">'
                   '<xs:attribute name="a" type="xs:string"/>'  # no use= -> optional
                   "</xs:complexType>",
    generated_body='<xs:complexType name="t_xType">'
                   '<xs:sequence><xs:element name="a" type="xs:string"/></xs:sequence>'
                   "</xs:complexType>",
)
check(counts(findings)["CONTRADICTS"] == 1,
      f"an optional attribute made mandatory IS a contradiction (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\na choice alternative made mandatory is a contradiction")
# This is the real OpenDRIVE t_road_planView_geometry defect, in miniature.
findings = run(
    reference_body='<xs:complexType name="t_g">'
                   "<xs:choice>"
                   '<xs:element name="line" type="t_l"/>'
                   '<xs:element name="arc" type="t_a"/>'
                   "</xs:choice></xs:complexType>",
    generated_body='<xs:complexType name="t_gType"><xs:sequence>'
                   '<xs:element name="line" type="t_lPropertyType"/>'
                   '<xs:element name="arc" type="t_aPropertyType"/>'
                   "</xs:sequence></xs:complexType>",
)
check(counts(findings)["CONTRADICTS"] == 2,
      f"both alternatives contradict (got {counts(findings)})")

# and the fixed form must be clean
findings = run(
    reference_body='<xs:complexType name="t_g">'
                   "<xs:choice>"
                   '<xs:element name="line" type="t_l"/>'
                   '<xs:element name="arc" type="t_a"/>'
                   "</xs:choice></xs:complexType>",
    generated_body='<xs:complexType name="t_gType"><xs:choice>'
                   '<xs:element name="line" type="t_lPropertyType"/>'
                   '<xs:element name="arc" type="t_aPropertyType"/>'
                   "</xs:choice></xs:complexType>",
)
check(counts(findings)["CONTRADICTS"] == 0,
      f"an xs:choice on both sides is clean (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\na generated schema that is LAXER is incomplete, not contradictory")
findings = run(
    reference_body='<xs:complexType name="t_x">'
                   '<xs:sequence><xs:element name="a" type="xs:string"/></xs:sequence>'
                   "</xs:complexType>",
    generated_body='<xs:complexType name="t_xType">'
                   '<xs:sequence><xs:element minOccurs="0" name="a" type="xs:string"/></xs:sequence>'
                   "</xs:complexType>",
)
check(counts(findings)["CONTRADICTS"] == 0,
      f"mandatory -> optional is laxity, not a contradiction (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\nan xs:group reference is resolved, so spliced content is compared where it lands")
# The real OpenDRIVE g_additionalData case: 141 group references, 3 elements each.
findings = run(
    reference_body='<xs:group name="g_extra"><xs:sequence>'
                   '<xs:element name="userData" type="t_u"/>'
                   "</xs:sequence></xs:group>"
                   '<xs:complexType name="t_x"><xs:sequence>'
                   '<xs:element name="kept" type="t_k"/>'
                   '<xs:group ref="g_extra"/>'
                   "</xs:sequence></xs:complexType>",
    generated_body='<xs:complexType name="t_xType"><xs:sequence>'
                   '<xs:element name="kept" type="t_kPropertyType"/>'
                   "</xs:sequence></xs:complexType>",
)
missing = [f for f in findings["MISSING"] if f[1] == "userData"]
check(len(missing) == 1,
      f"the group's member is reported MISSING where the reference splices it (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\ninherited content is compared at the type that carries it")
findings = run(
    reference_body='<xs:complexType name="t_base">'
                   '<xs:attribute name="id" type="xs:string" use="required"/>'
                   "</xs:complexType>"
                   '<xs:complexType name="t_x"><xs:complexContent>'
                   '<xs:extension base="t_base">'
                   '<xs:sequence><xs:element name="a" type="t_a"/></xs:sequence>'
                   "</xs:extension></xs:complexContent></xs:complexType>",
    generated_body='<xs:complexType name="t_baseType">'
                   '<xs:sequence><xs:element name="id" type="xs:string"/></xs:sequence>'
                   "</xs:complexType>"
                   '<xs:complexType name="t_xType"><xs:complexContent>'
                   '<xs:extension base="t_baseType">'
                   '<xs:sequence><xs:element name="a" type="t_aPropertyType"/></xs:sequence>'
                   "</xs:extension></xs:complexContent></xs:complexType>",
)
check(counts(findings) == {"MISSING": 0, "EXTRA": 0, "CONTRADICTS": 0, "TYPE_MISMATCH": 0},
      f"an inherited required attribute is matched through the extension (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\nXsdMapEntry substitutions are applied to the reference side")
findings = run(
    reference_body='<xs:complexType name="t_x">'
                   '<xs:attribute name="s" type="t_grEqZero" use="required"/>'
                   "</xs:complexType>",
    generated_body='<xs:complexType name="t_xType">'
                   '<xs:sequence><xs:element name="s" type="xs:double"/></xs:sequence>'
                   "</xs:complexType>",
    map_entries_body='<XsdMapEntry type="t_grEqZero" xmlType="double"/>',
)
check(counts(findings)["TYPE_MISMATCH"] == 0,
      f"t_grEqZero -> double is configuration, not a mismatch (got {counts(findings)})")

# without the map entries the same pair IS a mismatch, so the substitution is doing work
findings = run(
    reference_body='<xs:complexType name="t_x">'
                   '<xs:attribute name="s" type="t_grEqZero" use="required"/>'
                   "</xs:complexType>",
    generated_body='<xs:complexType name="t_xType">'
                   '<xs:sequence><xs:element name="s" type="xs:double"/></xs:sequence>'
                   "</xs:complexType>",
)
check(counts(findings)["TYPE_MISMATCH"] == 1,
      f"and it is a mismatch without them (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\ncontent the generated schema invents is EXTRA")
findings = run(
    reference_body='<xs:complexType name="t_x"><xs:sequence/></xs:complexType>',
    generated_body='<xs:complexType name="t_xType">'
                   '<xs:sequence><xs:element name="invented" type="t_iPropertyType"/></xs:sequence>'
                   "</xs:complexType>",
)
check(counts(findings)["EXTRA"] == 1, f"invented content is EXTRA (got {counts(findings)})")

# ---------------------------------------------------------------------------------------
print("\na comparison with nothing to compare FAILS instead of passing")
# Was: the first wiring globbed *.xsd non-recursively while ShapeChange nests its output
# one directory deeper. Zero schemas loaded -> zero findings -> empty baseline -> PASS.
with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    (root / "ref").mkdir()
    (root / "gen" / "INPUT").mkdir(parents=True)
    (root / "ref" / "S.xsd").write_text(
        HEAD + '<xs:complexType name="t_x"><xs:sequence/></xs:complexType>' + TAIL)
    (root / "gen" / "INPUT" / "S.xsd").write_text(
        HEAD + '<xs:complexType name="t_xType"><xs:sequence/></xs:complexType>' + TAIL)

    raised = False
    try:
        load(root / "empty-does-not-exist", root / "ref")
    except VacuousComparison:
        raised = True
    except Exception:
        pass
    check(raised, "an empty generated directory raises VacuousComparison")

    raised = False
    try:
        load(root / "gen", root / "ref-with-no-shared-names") if False else None
        (root / "other").mkdir()
        (root / "other" / "S.xsd").write_text(
            HEAD + '<xs:complexType name="totally_unrelated"><xs:sequence/></xs:complexType>' + TAIL)
        load(root / "gen", root / "other")
    except VacuousComparison:
        raised = True
    check(raised, "zero paired type names raises VacuousComparison")

    # and the nested layout ShapeChange actually produces must be found
    findings = load(root / "gen", root / "ref")
    check(len(findings["shared_types"]) == 1,
          f"output nested one directory deeper is found (got {len(findings['shared_types'])})")

# ---------------------------------------------------------------------------------------
print()
if FAILURES:
    print(f"{len(FAILURES)} FAILED:")
    for name in FAILURES:
        print(f"  - {name}")
    sys.exit(1)
print("all content-model comparison tests pass")
