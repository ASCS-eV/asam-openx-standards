#!/usr/bin/env python3
"""Regression tests for ``shacl_equivalence.py``.

The comparison decides whether generated shapes constrain an instance graph as the model's
schema constrains a document, so each case pairs a small schema, the bindings the derivation
records for it, and a small set of shapes, and states the complete list of findings. The
schema side is tested for each construct whose reading into graph terms is a rule of its own:
inheritance, group inlining, occurrence multiplication, single and repeated choices, list
wrappers, simple content, attribute use and name clashes. The shape side is tested for the
union encoding the OWL target produces and for closed shapes.

Run:  python scripts/test_shacl_equivalence.py
"""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET

import rdflib

from shacl_equivalence import ValueTypes, compare, expected_content, shapes

FAILURES: list[str] = []
NS = "http://example.org/m#"
XS = "http://www.w3.org/2001/XMLSchema"


def check(condition: bool, what: str) -> None:
    print(f"  {'ok  ' if condition else 'FAIL'} {what}")
    if not condition:
        FAILURES.append(what)


def schema(body: str) -> ET.Element:
    return ET.fromstring(f'<xs:schema xmlns:xs="{XS}">{body}</xs:schema>')


def run(body: str, bindings: dict, turtle: str) -> list[tuple]:
    documents = [schema(body)]
    values = ValueTypes(documents, NS, {"t_pos": "double"})
    expected = expected_content(documents, bindings, NS, values)
    graph = rdflib.Graph().parse(data=PREFIXES + turtle, format="turtle")
    return sorted((f.verdict, f.rule, f.subject) for f in compare(expected, shapes(graph), NS))


PREFIXES = f"""@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix m: <{NS}> .
"""

BASE = """<xs:complexType name="t_base"><xs:sequence/>
  <xs:attribute name="id" type="xs:string" use="required"/></xs:complexType>
<xs:complexType name="t_a"><xs:complexContent><xs:extension base="t_base"><xs:sequence>
  <xs:element name="b" type="t_b" minOccurs="0" maxOccurs="unbounded"/>
  <xs:group ref="g_extra" minOccurs="0" maxOccurs="unbounded"/>
</xs:sequence><xs:attribute name="x" type="t_pos" use="optional"/></xs:extension>
</xs:complexContent></xs:complexType>
<xs:complexType name="t_b"><xs:sequence/></xs:complexType>
<xs:group name="g_extra"><xs:sequence>
  <xs:element name="note" type="xs:string" minOccurs="0" maxOccurs="1"/></xs:sequence></xs:group>"""

BASE_BINDINGS = {
    ("t_base", "id"): ("attribute", "t_base", "id", "xs:string"),
    ("t_a", "b"): ("element", "t_a", "b", "t_b"),
    ("t_a", "group g_extra"): ("group", "t_a", None, "g_extra"),
    ("g_extra", "note"): ("element", "g_extra", "note", "xs:string"),
    ("t_a", "x"): ("attribute", "t_a", "x", "t_pos"),
}

FAITHFUL = """
m:T_base a sh:NodeShape ; sh:closed true ; sh:property [ sh:path m:T_base.id ;
  sh:datatype xsd:string ; sh:minCount 1 ; sh:maxCount 1 ] .
m:T_b a sh:NodeShape ; sh:closed true .
m:T_a a sh:NodeShape ; sh:closed true ;
  sh:property [ sh:path m:T_base.id ; sh:datatype xsd:string ; sh:minCount 1 ; sh:maxCount 1 ] ,
    [ sh:path m:T_a.b ; sh:class m:T_b ] ,
    [ sh:path m:T_a.note ; sh:datatype xsd:string ] ,
    [ sh:path m:T_a.x ; sh:datatype xsd:double ; sh:maxCount 1 ] .
"""


def main() -> int:
    print("shacl_equivalence")
    check(run(BASE, BASE_BINDINGS, FAITHFUL) == [],
          "inherited, own and group-inlined properties, a repeated group multiplying its "
          "member's count, and a mapped type: no finding")
    check(run(BASE, BASE_BINDINGS, FAITHFUL.replace(
        "[ sh:path m:T_base.id ; sh:datatype xsd:string ; sh:minCount 1 ; sh:maxCount 1 ] ,\n",
        "")) == [("MISSING", "property", "T_a: T_base.id")],
        "a closed shape without an inherited property rejects it")
    ignoring = FAITHFUL.replace(
        "[ sh:path m:T_base.id ; sh:datatype xsd:string ; sh:minCount 1 ; sh:maxCount 1 ] ,\n",
        "").replace("m:T_a a sh:NodeShape ; sh:closed true ;",
                    "m:T_a a sh:NodeShape ; sh:closed true ; "
                    "sh:ignoredProperties ( m:T_base.id ) ;")
    check(run(BASE, BASE_BINDINGS, ignoring) == [],
          "an inherited property a closed shape ignores is admitted, and constrained by its "
          "declaring class's shape")
    check(run(BASE, BASE_BINDINGS, ignoring.replace("sh:minCount 1 ; sh:maxCount 1 ] .",
                                                    "sh:maxCount 1 ] ."))
          == [("DIFFERENT", "min", "T_a: T_base.id"), ("DIFFERENT", "min", "T_base: T_base.id")],
          "the declaring class's bound is the one an inherited property is held to")
    check(run(BASE, BASE_BINDINGS, FAITHFUL.replace("sh:path m:T_a.note ; sh:datatype "
                                                    "xsd:string ]",
                                                    "sh:path m:T_a.note ; sh:datatype "
                                                    "xsd:string ; sh:maxCount 1 ]"))
          == [("DIFFERENT", "max", "T_a: T_a.note")],
          "a group that repeats lets its member repeat")
    check(run(BASE, BASE_BINDINGS, FAITHFUL.replace("sh:path m:T_a.x ; sh:datatype xsd:double ;",
                                                    "sh:path m:T_a.x ; sh:datatype xsd:double ; "
                                                    "sh:minCount 1 ;"))
          == [("DIFFERENT", "min", "T_a: T_a.x")], "an optional attribute has no lower bound")
    check(run(BASE, BASE_BINDINGS, FAITHFUL.replace("sh:class m:T_b", "sh:class m:T_base"))
          == [("DIFFERENT", "value", "T_a: T_a.b")], "the value type is compared")
    check(run(BASE, BASE_BINDINGS, FAITHFUL + "m:T_a sh:property [ sh:path m:T_a.y ] .")
          == [("EXTRA", "property", "T_a: T_a.y")], "a property the schema lacks is EXTRA")
    check(run(BASE, BASE_BINDINGS, FAITHFUL.replace("m:T_b a sh:NodeShape ; sh:closed true .",
                                                    ""))
          == [("MISSING", "shape", "T_b")], "a complex type without a node shape")

    choice = """<xs:complexType name="t_c"><xs:sequence>
      <xs:choice><xs:element name="p" type="t_b"/><xs:element name="q" type="t_b"/>
        <xs:group ref="g_extra" minOccurs="0" maxOccurs="unbounded"/></xs:choice>
      <xs:choice maxOccurs="unbounded"><xs:element name="r" type="t_b"/>
        <xs:element name="s" type="t_b"/></xs:choice>
    </xs:sequence><xs:attribute name="name" type="xs:string" use="required"/></xs:complexType>
    <xs:complexType name="t_b"><xs:sequence/></xs:complexType>
    <xs:group name="g_extra"><xs:sequence>
      <xs:element name="note" type="xs:string" minOccurs="0"/>
      <xs:element name="more" type="xs:string" minOccurs="0"/></xs:sequence></xs:group>"""
    bindings = {("t_c", n): ("element", "t_c", n, "t_b") for n in "pqrs"}
    bindings.update({("g_extra", "note"): ("element", "g_extra", "note", "xs:string"),
                     ("g_extra", "more"): ("element", "g_extra", "more", "xs:string"),
                     ("t_c", "name"): ("attribute", "t_c", "name", "xs:string")})

    def alternative(own: str, others: list[str]) -> str:
        zeros = " , ".join(f"[ sh:path m:T_c.{o} ; sh:maxCount 0 ]" for o in others)
        return f"[ sh:property {own} , {zeros} ]"

    union = ("m:T_c a sh:NodeShape ; sh:closed true ; sh:or ( "
             + alternative("[ sh:path m:T_c.p ; sh:minCount 1 ; sh:maxCount 1 ]",
                           ["q", "note", "more"])
             + alternative("[ sh:path m:T_c.q ; sh:minCount 1 ; sh:maxCount 1 ]",
                           ["p", "note", "more"])
             + "[ sh:property [ sh:path m:T_c.note ] , "
               "[ sh:path m:T_c.more ] , [ sh:path m:T_c.p ; sh:maxCount 0 ] , "
               "[ sh:path m:T_c.q ; sh:maxCount 0 ] ] ) ;"
             + " sh:property [ sh:path m:T_c.p ; sh:class m:T_b ] , [ sh:path m:T_c.q ; sh:class "
               "m:T_b ] , [ sh:path m:T_c.note ; sh:datatype xsd:string ] , [ sh:path m:T_c.more ;"
               " sh:datatype xsd:string ] , [ sh:path m:T_c.r ; sh:class m:T_b ] , [ sh:path "
               "m:T_c.s ; sh:class m:T_b ] , [ sh:path m:T_c.name ; sh:datatype xsd:string ; "
               "sh:minCount 1 ; sh:maxCount 1 ] .\nm:T_b a sh:NodeShape ; sh:closed true .")
    found = run(choice, bindings, union)
    check(found == [], "a single choice is exactly-one-of its alternatives, a group alternative "
                       f"is one alternative of several properties, and a repeated choice excludes "
                       f"nothing {found or ''}")
    conjunction = union.split(" sh:or ( ")[0] + " ;" + union.split(") ;", 1)[1]
    found = run(choice, bindings, conjunction)
    check(("MISSING", "choice", "T_c: T_c.more & T_c.note | T_c.p | T_c.q") in found
          and len(found) == 1, "a choice the shapes do not encode")
    folded = union.replace("m:T_c.more ; sh:maxCount 0 ]", "m:T_c.more ; sh:maxCount 0 ] , "
                                                         "[ sh:path m:T_c.name ; sh:maxCount 0 ]")
    found = run(choice, bindings, folded.replace(
        "[ sh:path m:T_c.note ] , ",
        "[ sh:path m:T_c.note ] , [ sh:path m:T_c.name ; sh:maxCount 1 ] , "))
    check(("EXTRA", "choice", "T_c: T_c.name") in found,
          "a property the shapes make an alternative, which the schema does not")

    wrapped = """<xs:complexType name="t_d"><xs:sequence>
      <xs:element name="Items" type="Items" minOccurs="0"/></xs:sequence></xs:complexType>
    <xs:complexType name="Items"><xs:sequence>
      <xs:element name="Item" type="t_b" minOccurs="0" maxOccurs="unbounded"/></xs:sequence>
    </xs:complexType><xs:complexType name="t_b"><xs:sequence/></xs:complexType>
    <xs:complexType name="t_text"><xs:simpleContent><xs:extension base="xs:string">
      <xs:attribute name="lang" type="xs:string"/></xs:extension></xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="t_clash"><xs:sequence>
      <xs:element name="type" type="t_b"/></xs:sequence>
      <xs:attribute name="type" type="xs:string"/></xs:complexType>"""
    bindings = {("t_d", "Items"): ("wrapper", "t_d", "items", "t_b"),
                ("Items", "Item"): ("wrapped", None, None, "t_b"),
                ("t_text", ""): ("content", "t_text", "content", "string"),
                ("t_text", "lang"): ("attribute", "t_text", "lang", "xs:string"),
                ("t_clash", "type"): ("element", "t_clash", "type", "t_b")}
    shapes_ = """m:T_d a sh:NodeShape ; sh:closed true ; sh:property [ sh:path m:T_d.items ;
      sh:class m:T_b ] . m:T_b a sh:NodeShape ; sh:closed true .
    m:T_text a sh:NodeShape ; sh:closed true ; sh:property [ sh:path m:T_text.content ;
      sh:datatype xsd:string ; sh:minCount 1 ; sh:maxCount 1 ] , [ sh:path m:T_text.lang ;
      sh:datatype xsd:string ; sh:maxCount 1 ] .
    m:T_clash a sh:NodeShape ; sh:property [ sh:path m:T_clash.type ; sh:class m:T_b ] ."""
    found = run(wrapped, bindings, shapes_)
    check(("MISSING", "shape", "Items") not in found and not any(s.startswith("T_d") or
                                                                  s.startswith("T_text")
                                                                  for _, _, s in found),
          "a list wrapper stands for no class, its items are the property's values; simple "
          "content is the value of its property")
    check(("DIFFERENT", "value", "T_clash: T_clash.type") in found,
          "an attribute and an element of one name are reported as a clash")

    print("\nall checks passed" if not FAILURES else f"\n{len(FAILURES)} check(s) failed")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
