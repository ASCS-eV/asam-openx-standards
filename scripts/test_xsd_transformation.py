#!/usr/bin/env python3
"""Regression tests for the XSD derivation: ``ea_api.py``, ``osc_xsd_transformation.py``,
``odr_xsd_transformation.py`` and ``xsd_equivalence.py``.

``check_xsd_transformation.py`` asserts, on the real projects, that the OpenSCENARIO port
reproduces the normative schema byte for byte and that the OpenDRIVE derivation leaves only the
recorded differences. Those runs exercise only the constructs the two models use. The cases here
exercise each rule directly, on small models built in memory, including the behaviour of
ASAM's script that neither model reaches. Each rule is stated in the module it tests; a case
fails when the rule's output changes.

The comparison is tested the other way round: a difference that carries meaning must be
reported, under the right rule, and one that does not must not be.

No JDK, no EA: this runs in a pull-request workflow.

Run:  python scripts/test_xsd_transformation.py
"""

from __future__ import annotations

import sqlite3
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import odr_xsd_transformation as odr
import osc_xsd_transformation as osc
from ea_api import (
    SC,
    Attribute,
    Connector,
    ConnectorEnd,
    Constraint,
    Element,
    NotAnEaProject,
    Package,
    Repository,
    TaggedValue,
    open_qeax,
    open_scxml,
)
from xsd_equivalence import compare_schemas

FAILURES: list[str] = []
XS = "http://www.w3.org/2001/XMLSchema"


def check(condition: bool, what: str) -> None:
    print(f"  {'ok  ' if condition else 'FAIL'} {what}")
    if not condition:
        FAILURES.append(what)


# ---------------------------------------------------------------------------------------
# Building EA object models in memory


def tags(**values) -> tuple:
    return tuple(TaggedValue(k, v) for k, v in values.items())


def attribute(name: str, type_: str = "double", lower: str = "1", upper: str = "1",
              stereotypes: tuple = (), attr_tags: tuple = (), notes: str | None = None,
              classifier: int | None = None, aid: int = 0) -> Attribute:
    return Attribute(aid, name, type_, lower, upper, stereotypes[0] if stereotypes else None,
                     stereotypes, attr_tags, notes_text=notes, classifier_id=classifier)


def element(eid: int, name: str, stereotypes: tuple = (), el_tags: tuple = (),
            attributes: tuple = (), type_: str = "Class", notes: str | None = None,
            abstract: bool = False, gen_links: str | None = None,
            constraints: tuple = (), package: int = 1) -> Element:
    return Element(eid, type_, name, stereotypes[0] if stereotypes else None, stereotypes,
                   el_tags, attributes, package_id=package, notes_text=notes, abstract=abstract,
                   gen_links=gen_links, constraints=constraints)


def connector(cid: int, client: int, supplier: int, role: str | None = None,
              card: str | None = None, type_: str = "Association", stereotypes: tuple = (),
              con_tags: tuple = (), column: str | None = None) -> Connector:
    return Connector(cid, type_, client, supplier,
                     column if column is not None else (stereotypes[0] if stereotypes else None),
                     stereotypes, con_tags, ConnectorEnd(None, None), ConnectorEnd(role, card))


def repository(packages: list[Package], connectors: list[Connector] = ()) -> Repository:
    elements = {}

    def walk(package: Package) -> None:
        for item in package.elements:
            elements[item.element_id] = item
            for nested in item.elements:
                elements[nested.element_id] = nested
        for sub in package.packages:
            walk(sub)

    for package in packages:
        walk(package)
    for item in elements.values():
        item.connectors = tuple(sorted(
            (c for c in connectors if item.element_id in (c.client_id, c.supplier_id)),
            key=lambda c: c.connector_id))
    return Repository(models=tuple(packages), elements=elements)


def osc_repository(classes: list[Element], connectors: list[Connector] = (),
                   extra_packages: list[Package] = ()) -> Repository:
    classes_package = Package(10, "Classes", elements=tuple(classes))
    root = Package(3, "OpenSCENARIO", packages=(classes_package, *extra_packages))
    return repository([Package(2, "ASAM", packages=(root,))], connectors)


def lines_of(text: str, start: str) -> list[str]:
    """The lines of the top-level component that begins with ``start``."""
    lines = text.splitlines()
    first = next(i for i, line in enumerate(lines) if line.startswith(start))
    end = next(i for i in range(first + 1, len(lines))
               if lines[i].startswith("\t<xsd:") or lines[i] == "</xsd:schema>")
    return lines[first:end]


# ---------------------------------------------------------------------------------------
# osc_xsd_transformation: ASAM's script, rule by rule


def test_osc() -> None:
    print("osc_xsd_transformation")
    a = element(1, "A", ("XSDcomplexType",), tags(modelGroup="sequence"),
                (attribute("speed", "double", "1"), attribute("name", "string", "0"),
                 attribute("gone", "double", "0", stereotypes=("deprecated",))))
    b = element(2, "B", ("XSDcomplexType",))
    wrapped = element(3, "W", ("XSDcomplexType",),
                      tags(xsdWrapperType="Ws", xsdWrapperElementName="W"))
    group = element(4, "G", ("XSDgroup",))
    conns = [
        connector(10, 1, 2, "second", "0..*", stereotypes=("XSDelement",),
                  con_tags=tags(position="2")),
        connector(11, 1, 2, "first", "1..1", con_tags=tags(position="1",
                                                            xsdElementName="First")),
        connector(12, 1, 3, "ws", "0..1", stereotypes=("XSDwrapped",)),
        connector(13, 1, 4, "g", "0..1"),
        connector(14, 1, 2, "ref", "1..1", stereotypes=("nameRef",),
                  con_tags=tags(xsdType="string")),
        connector(15, 1, 2, "optionalRef", "0..1", stereotypes=("nameRef",),
                  con_tags=tags(xsdType="string")),
        connector(16, 1, 2, "hidden", "1..1", column="transient"),
        connector(17, 1, 2, "notHidden", "1..1", stereotypes=("transient",),
                  column="XSDelement"),
        connector(18, 1, 2, "few", "0..2", con_tags=tags(position="9")),
    ]
    text = osc.transform(osc_repository([a, b, wrapped, group], conns))
    body = lines_of(text, '\t<xsd:complexType name="A">')
    particles = [line.strip().split('"')[1] for line in body
                 if line.startswith("\t\t\t<xsd:element") or line.startswith("\t\t\t<xsd:group")]
    check(particles == ["Ws", "G", "NotHidden", "First", "Second", "Few"],
          "untagged particles (position -1) first, in connector order, then by position; a "
          "transient only in StereotypeEx is not excluded")
    check('\t\t\t<xsd:element name="First" type="B"/>' in body,
          "xsdElementName names the element; lower 1 writes no minOccurs")
    check('\t\t\t<xsd:element name="Second" type="B" minOccurs="0" maxOccurs="unbounded"/>'
          in body, "a role becomes ToFirstUpper(role); 0..* is minOccurs 0, unbounded")
    check(body.index('\t\t\t<xsd:element name="First" type="B"/>')
          < body.index('\t\t\t<xsd:element name="Second" type="B" minOccurs="0" '
                       'maxOccurs="unbounded"/>'), "elements are ordered by position")
    check(not any('name="Hidden"' in line for line in body),
          "a connector whose Stereotype column is transient is excluded")
    check('\t\t\t<xsd:element name="Ws" type="Ws" minOccurs="0"/>' in body,
          "an XSDwrapped connector to a wrapped class is typed by the wrapper, without "
          "maxOccurs")
    check('\t\t\t<xsd:group ref="G" minOccurs="0"/>' in body, "an XSDgroup target is a group ref")
    check('\t\t\t<xsd:element name="Few" type="B" maxOccurs="0"/>' in body,
          "as ASAM's script: 0..2 writes maxOccurs with the lower bound, replacing minOccurs")
    check('\t\t<xsd:attribute name="ref" type="String" use="required"/>' in body
          and '\t\t<xsd:attribute name="optionalRef" type="String"/>' in body,
          "a nameRef is an attribute of its xsdType, required unless its lower bound is 0")
    check(body.index('\t\t<xsd:attribute name="ref" type="String" use="required"/>')
          < body.index('\t\t<xsd:attribute name="speed" type="Double" use="required"/>'),
          "name references come before attributes")
    check('\t\t<xsd:attribute name="name" type="String"/>' in body,
          "an attribute is optional unless its LowerBound is 1; its type is ToFirstUpper")
    check(body[-4:-1] == ['\t\t<xsd:attribute name="gone" type="Double">',
                        '\t\t\t' + osc.DEPRECATED, '\t\t</xsd:attribute>'],
          "a deprecated attribute carries the deprecated annotation")
    wrapper = [line for line in text.splitlines() if 'complexType name="Ws"' in line]
    check(wrapper == ['\t\t<xsd:complexType name="Ws">'],
          "as ASAM's script: a complexType's wrapper type is one level deeper")

    choice = element(1, "C", ("XSDcomplexType",), tags(modelGroup="choice", minOccurs="0"))
    text = osc.transform(osc_repository([choice, b], [connector(10, 1, 2, "x", "1..1")]))
    check('\t\t<xsd:choice minOccurs="0">' in text, "modelGroup and a minOccurs tag")
    both = element(1, "C", ("XSDcomplexType",), tags(modelGroup="choice", minOccurs="0",
                                                      maxOccurs="*"))
    text = osc.transform(osc_repository([both, b], [connector(10, 1, 2, "x", "1..1")]))
    check('\t\t<xsd:choice maxOccurs="unbound">' in text,
          'as ASAM\'s script: "*" is "unbound", and maxOccurs drops minOccurs')
    one = element(1, "C", ("XSDcomplexType",), tags(minOccurs="1.0"))
    text = osc.transform(osc_repository([one, b], [connector(10, 1, 2, "x", "1..1")]))
    check("\t\t<xsd:sequence>" in text, 'JavaScript\'s "1.0" == 1: no minOccurs is written')

    enum = element(5, "E", ("enumeration",), attributes=(
        attribute("on"), attribute("off", stereotypes=("deprecated",))))
    text = osc.transform(osc_repository([enum]))
    body = lines_of(text, '\t<xsd:simpleType name="E">')
    check(body[1:4] == ["\t\t<xsd:union>", "\t\t\t<xsd:simpleType>",
                        '\t\t\t\t<xsd:restriction base="xsd:string">']
          and '\t\t\t\t\t<xsd:enumeration value="on"/>' in body
          and '\t\t\t\t\t<xsd:enumeration value="off">' in body
          and '\t\t\t\t<xsd:restriction base="parameter"/>' in body,
          "an enumeration is a union of its literals and a parameter; a deprecated literal is "
          "annotated")

    primitives = Package(11, "PrimitiveTypes", elements=(
        element(6, "double", type_="PrimitiveType"), element(7, "string", type_="PrimitiveType"),
        element(8, "float", type_="PrimitiveType")))
    enums = Package(12, "Enums", elements=(enum,))
    text = osc.transform(osc_repository([a, b], [], [enums, primitives]))
    order = [line for line in text.splitlines() if line.startswith("\t<xsd:simpleType name=")
             or line.startswith("\t<xsd:complexType name=")]
    check(order[2:6] == ['\t<xsd:simpleType name="Double">', '\t<xsd:simpleType name="String">',
                         '\t<xsd:simpleType name="E">', '\t<xsd:complexType name="A">'],
          "PrimitiveTypes, then Enums, then Classes; an unknown primitive is skipped")
    check('\t\t<xsd:union memberTypes="expression parameter xsd:double"/>' in text
          and '\t\t<xsd:union memberTypes="parameter xsd:string"/>' in text,
          "a numeric primitive admits an expression, a string one a parameter")

    top = element(9, "Root", ("XSDcomplexType", "XSDtopLevelElement"), tags(elementName="R"))
    text = osc.transform(osc_repository([top]))
    check('\t<xsd:element name="R" type="Root"/>' in text,
          "XSDtopLevelElement adds a global element named by elementName")

    simple = element(9, "Text", ("XSDsimpleContent",), tags(umlPropertyName="content",
                                                             xsdType="string"),
                     (attribute("content", "string"), attribute("lang", "string", "0")))
    body = lines_of(osc.transform(osc_repository([simple])), '\t<xsd:complexType name="Text">')
    check(body == ['\t<xsd:complexType name="Text">', "\t\t<xsd:simpleContent>",
                   '\t\t\t<xsd:extension base="xsd:string">',
                   '\t\t<xsd:attribute name="lang" type="String"/>', "\t\t\t</xsd:extension>",
                   "\t\t</xsd:simpleContent>", "\t</xsd:complexType>"],
          "XSDsimpleContent extends xsdType, without the umlPropertyName attribute, which the "
          "script writes one level out")

    unnamed = osc_repository([a, b], [connector(10, 1, 2, None, "1..1")])
    try:
        osc.transform(unnamed)
        check(False, "an unnamed element role is refused")
    except osc.TransformationError:
        check(True, "an unnamed element role is refused")
    errors: list[str] = []
    osc.transform(unnamed, errors)
    check(len(errors) == 1, "the measuring mode records the refusal and carries on")
    no_type = osc_repository([a, b], [connector(10, 1, 2, "r", "1..1",
                                                stereotypes=("nameRef",))])
    errors = []
    text = osc.transform(no_type, errors)
    check(errors and '<xsd:attribute name="r" type="?" use="required"/>' in text,
          "a nameRef without xsdType stands in '?' when measuring")


# ---------------------------------------------------------------------------------------
# odr_xsd_transformation: EA's XML Schema profile


def odr_repository(elements: list[Element], connectors: list[Connector] = (),
                   packages: list[tuple] = ()) -> Repository:
    """One XSDschema package ``Core`` with ``elements``, plus ``packages``: (name, elements)."""
    def schema(pid: int, name: str, members: list[Element]) -> Package:
        own = element(-pid, name, ("XSDschema",),
                      tags(schemaLocation=f"https://example.org/x/{name}.xsd",
                           elementFormDefault="qualified"), type_="Package")
        for member in members:
            member.package_id = pid
        return Package(pid, name, elements=tuple(members), element=own)

    subs = [schema(4, "Core", elements)]
    subs += [schema(5 + i, name, members) for i, (name, members) in enumerate(packages)]
    return repository([Package(2, "Model", packages=(Package(3, "OpenDRIVE",
                                                               packages=tuple(subs)),))],
                      connectors)


def generated(repo: Repository, name: str = "Core.xsd") -> ET.Element:
    return odr.transform(repo)[name]


def find(root: ET.Element, kind: str, name: str) -> ET.Element:
    return next(n for n in root.iter(f"{{{XS}}}{kind}") if n.get("name") == name)


def local(node: ET.Element) -> str:
    return node.tag.rsplit("}", 1)[-1]


def test_odr() -> None:
    print("odr_xsd_transformation")
    base = element(1, "_Base", ("XSDcomplexType",), abstract=True)
    t = element(2, "t_a", ("XSDcomplexType",), tags(modelGroup="group", mixed="true"),
                (attribute("s", "double", "1", stereotypes=("XSDattribute",)),
                 attribute("x", "double", "0", stereotypes=("XSDattribute",),
                           attr_tags=tags(use="required", fixed="1"), notes="The x."),
                 attribute("e", "e_kind", "1", "1"),
                 attribute("r", "t_grEqZero", stereotypes=("XSDattribute",), classifier=6),
                 attribute("u", "t_grEqZero", stereotypes=("XSDattribute",))),
                notes="A type.")
    b = element(3, "t_b", ("XSDcomplexType",))
    g = element(4, "g_data", ("XSDgroup",))
    choice = element(5, "C", ("XSDchoice",), tags(maxOccurs="unbounded"), abstract=True)
    ge = element(6, "t_grEqZero", ("XSDsimpleType",), tags(minInclusive="0.0"),
                 gen_links="Parent=double;")
    kind = element(7, "e_kind", type_="Enumeration",
                   attributes=(attribute("on", notes="On."), attribute("off")))
    conns = [
        connector(20, 2, 1, type_="Generalization"),
        connector(21, 2, 3, "late", "0..*", con_tags=tags(position="2")),
        connector(22, 2, 4, None, "0..*"),
        connector(23, 2, 5, None, "0..1"),
        connector(24, 5, 3, "one", "1..*"),
        connector(25, 5, 3, "two", "2..*"),
        connector(26, 2, 3, None, None),
    ]
    root = generated(odr_repository([base, t, b, g, choice, ge, kind], conns))
    ct = find(root, "complexType", "t_a")
    check(ct.get("mixed") == "true" and find(root, "complexType", "_Base").get("abstract")
          == "true", "mixed from the tag; abstract from the class")
    check(ct.find(f"{{{XS}}}annotation/{{{XS}}}documentation").text == "A type.",
          "a class's notes are its documentation")
    extension = ct.find(f"{{{XS}}}complexContent/{{{XS}}}extension")
    check(extension is not None and extension.get("base") == "_Base",
          "a generalization is a complexContent extension")
    group = extension.find(f"{{{XS}}}sequence")
    check(group is not None, 'a modelGroup of "group" is a sequence')
    particles = [(local(n), n.get("name") or n.get("ref") or "") for n in group]
    check(particles[0] == ("element", "e"),
          "an attribute without XSDattribute is an element, before the associations")
    check(particles[1] == ("group", "g_data") and particles[2] == ("choice", "")
          and particles[3] == ("element", "t_b") and particles[4] == ("element", "late"),
          "untagged associations in connector order before a positioned one; a group ref; "
          "an unnamed role is named after its target")
    nested = group[2]
    check((nested.get("minOccurs"), nested.get("maxOccurs")) == ("0", "1")
          and [n.get("name") for n in nested] == ["one", "two"],
          "an XSDchoice target is a nested choice by default, with the association's "
          "occurrence, not the class tag's")
    check((group[3].get("minOccurs"), group[3].get("maxOccurs")) == ("1", "1"),
          "an unset cardinality is 1..1")
    attrs = {n.get("name"): n for n in extension.findall(f"{{{XS}}}attribute")}
    check(attrs["s"].get("use") == "optional", "an unset use is optional, whatever the "
                                               "multiplicity")
    check(attrs["x"].get("use") == "required" and attrs["x"].get("fixed") == "1"
          and attrs["x"].find(f"{{{XS}}}annotation/{{{XS}}}documentation").text == "The x.",
          "use and fixed from the tags; the attribute's notes are its documentation")
    check(attrs["s"].get("type") == "xs:double" and attrs["r"].get("type") == "t_grEqZero"
          and attrs["u"].get("type") == "xs:string",
          "a built-in type; a resolved classifier; a class name without a reference is "
          "xs:string")
    simple = find(root, "simpleType", "t_grEqZero").find(f"{{{XS}}}restriction")
    check(simple.get("base") == "xs:double" and simple.find(f"{{{XS}}}minInclusive")
          .get("value") == "0.0", "a simple type restricts its GenLinks parent by its facets")
    enum = find(root, "simpleType", "e_kind").find(f"{{{XS}}}restriction")
    check(enum.get("base") == "xs:string" and [e.get("value") for e in enum] == ["on", "off"]
          and enum[0].find(f"{{{XS}}}annotation") is not None,
          "an Enumeration restricts xs:string to its literals, documented")

    union = element(8, "u", ("XSDunion",), gen_links="Parent=elsewhere;")
    listed = element(9, "l", ("XSDSimpleType",), tags(derivation="list"),
                     gen_links="Parent=double;")
    stereotyped = element(10, "e_s", ("enumeration",), attributes=(attribute("a"),))
    wildcard = element(11, "any", ("XSDany",), tags(processContents="skip"))
    holder = element(12, "t_h", ("XSDcomplexType",))
    root = generated(odr_repository([union, listed, stereotyped, wildcard, holder, b, ge], [
        connector(30, 8, 3, type_="Generalization"),
        connector(31, 8, 6, type_="Generalization"),
        connector(32, 12, 11, None, "0..*"),
    ]))
    check(find(root, "simpleType", "u").find(f"{{{XS}}}union").get("memberTypes")
          == "t_b t_grEqZero xs:elsewhere",
          "a union's members are its generalizations, then its GenLinks parents")
    check(find(root, "simpleType", "l").find(f"{{{XS}}}list").get("itemType") == "xs:double",
          "derivation=list is a list of the general type")
    check(find(root, "simpleType", "e_s") is not None,
          "a class stereotyped enumeration is an enumeration")
    wild = find(root, "complexType", "t_h").find(f"{{{XS}}}sequence/{{{XS}}}any")
    check(wild is not None and wild.get("processContents") == "skip"
          and wild.get("maxOccurs") == "unbounded", "an XSDany target is a wildcard")

    context = element(13, "t_ctx", ("XSDcomplexType",))
    general = element(14, "t_item", ("XSDcomplexType",))
    first = element(15, "t_item_one", ("XSDcomplexType",), tags(
        XSDAlternative_element="item", XSDAlternative_nr="2", XSDAlternative_type="t_ctx",
        XSDAlternative_test="@k='1'"))
    default = element(16, "t_item_default", ("XSDcomplexType",), tags(
        XSDAlternative_element="item", XSDAlternative_nr="3", XSDAlternative_type="t_ctx"))
    elsewhere = element(17, "t_item_two", ("XSDcomplexType",), tags(
        XSDAlternative_element="item", XSDAlternative_nr="1", XSDAlternative_type="t_ctx",
        XSDAlternative_test="@k='2'"))
    keyed = element(18, "t_keyed", ("XSDcomplexType",), attributes=(
        attribute("id", "string", stereotypes=("XSDattribute",), attr_tags=tags(
            key="k_id", selector="keyed")),
        attribute("ref", "string", stereotypes=("XSDattribute",), attr_tags=tags(
            keyref="r_ref", refer="k_id", selector="keyed/ref", targetElement="item"))),
        constraints=(Constraint("count(x) = 1", "Invariant", "Approved", None),))
    top = element(19, "OpenDRIVE", ("XSDtopLevelElement",))
    top.elements = (element(20, "t_Root", ("XSDcomplexType",)),)
    root = generated(odr_repository([context, general, first, default, elsewhere, keyed, top], [
        connector(40, 15, 14, type_="Generalization"),
        connector(41, 16, 14, type_="Generalization"),
        connector(42, 17, 14, type_="Generalization"),
        connector(43, 13, 15, "item", "0..*"),
        connector(44, 13, 16, "item", "0..*"),
        connector(45, 20, 18, "keyed", "0..*"),
    ]))
    items = find(root, "complexType", "t_ctx").findall(f".//{{{XS}}}element")
    check(len(items) == 1 and items[0].get("type") == "t_item",
          "associations sharing a role are one element, typed by the alternatives' common "
          "general type")
    alternatives = items[0].findall(f"{{{XS}}}alternative")
    check([(a.get("test"), a.get("type")) for a in alternatives] == [
        ("@k='2'", "t_item_two"), ("@k='1'", "t_item_one"), (None, "t_item_default")],
        "alternatives in XSDAlternative_nr order; one without a test is the default")
    check([c.get("name") for c in items[0] if local(c) == "keyref"] == ["r_ref"],
          "targetElement places an identity constraint in the element of that name")
    global_element = find(root, "element", "OpenDRIVE")
    keys = global_element.findall(f"{{{XS}}}key")
    check(len(keys) == 1 and keys[0].find(f"{{{XS}}}selector").get("xpath") == "keyed"
          and keys[0].find(f"{{{XS}}}field").get("xpath") == "@id"
          and global_element.find(f"{{{XS}}}complexType") is not None,
          "a global element with its nested class as anonymous type, holding every key "
          "without a targetElement")
    check([a.get("test") for a in find(root, "complexType", "t_keyed").iter(f"{{{XS}}}assert")]
          == ["count(x) = 1"], "an invariant's name is an assertion")

    road = element(21, "t_road", ("XSDcomplexType",))
    lane = element(22, "t_lane", ("XSDcomplexType",))
    documents = odr.transform(odr_repository([road], [connector(50, 21, 22, "lane", "0..*")],
                                             [("Lane", [lane])]))
    includes = [n.get("schemaLocation") for n in documents["Core.xsd"]
                if local(n) == "include"]
    check(includes == ["Lane.xsd"] and not [n for n in documents["Lane.xsd"]
                                            if local(n) == "include"],
          "a document includes each document it refers to, by its schemaLocation's last "
          "segment")
    check(documents["Core.xsd"].get("elementFormDefault") == "qualified",
          "elementFormDefault from the XSDschema package")


# ---------------------------------------------------------------------------------------
# xsd_equivalence


def schema(body: str, attrs: str = "") -> ET.Element:
    return ET.fromstring(f'<xs:schema xmlns:xs="{XS}" {attrs}>{body}</xs:schema>')


def rules(generated_body: str, normative_body: str, g_attrs: str = "",
          n_attrs: str = "") -> list[tuple]:
    return [(f.verdict, f.rule) for f in compare_schemas(schema(generated_body, g_attrs),
                                                         schema(normative_body, n_attrs))]


def test_equivalence() -> None:
    print("xsd_equivalence")
    seq = ('<xs:complexType name="T"><xs:sequence><xs:element name="a" type="A"/>'
           '<xs:element name="b" type="B"/></xs:sequence>'
           '<xs:attribute name="x" type="X" use="optional"/>'
           '<xs:attribute name="y" type="Y"/></xs:complexType>')
    check(rules(seq, seq) == [], "a schema is equivalent to itself")
    reordered = seq.replace('<xs:attribute name="x" type="X" use="optional"/>'
                            '<xs:attribute name="y" type="Y"/>',
                            '<xs:attribute name="y" type="Y"/>'
                            '<xs:attribute use="optional" type="X" name="x"/><!-- note -->')
    check(rules(reordered, seq) == [], "attribute order and comments are not content")
    swapped = seq.replace('<xs:element name="a" type="A"/><xs:element name="b" type="B"/>',
                          '<xs:element name="b" type="B"/><xs:element name="a" type="A"/>')
    check(rules(swapped, seq) == [("DIFFERENT", "particle-order")],
          "sequence order is its own rule")
    choice = swapped.replace("sequence", "choice")
    check(rules(choice, seq.replace("sequence", "choice")) == [],
          "the order of choice alternatives is not compared")
    optional = seq.replace('name="a" type="A"', 'name="a" type="A" minOccurs="0"')
    check(rules(optional, seq) == [("DIFFERENT", "component")], "an occurrence is content")
    facets = ('<xs:simpleType name="S"><xs:restriction base="xs:double">'
              '<xs:minInclusive value="0"/><xs:maxInclusive value="1"/>'
              '</xs:restriction></xs:simpleType>')
    check(rules(facets.replace('<xs:minInclusive value="0"/><xs:maxInclusive value="1"/>',
                               '<xs:maxInclusive value="1"/><xs:minInclusive value="0"/>'),
                facets) == [], "facet order is not compared")
    alternatives = ('<xs:element name="E" type="T"><xs:alternative test="@a" type="A"/>'
                    '<xs:alternative type="B"/></xs:element>')
    check(rules(alternatives.replace('<xs:alternative test="@a" type="A"/>'
                                     '<xs:alternative type="B"/>',
                                     '<xs:alternative type="B"/>'
                                     '<xs:alternative test="@a" type="A"/>'), alternatives)
          == [("DIFFERENT", "alternative-order")], "type alternative order is its own rule")
    documented = ('<xs:simpleType name="S"><xs:annotation><xs:documentation>One&#13;\n'
                  'two</xs:documentation></xs:annotation><xs:restriction base="xs:string"/>'
                  '</xs:simpleType>')
    check(rules(documented.replace("&#13;\n", "&#13;&#10;"), documented) == [],
          "a character reference is the character it denotes")
    check(rules(documented.replace("&#13;\n", "\r\n"), documented)
          == [("DIFFERENT", "documentation")],
          "a literal CR is not: XML normalizes a line end to LF, and &#13; keeps it")
    check(rules(documented.replace("two", "three"), documented)
          == [("DIFFERENT", "documentation")], "documentation is its own rule")
    check(rules(seq + facets, facets + '<xs:group name="G"><xs:sequence/></xs:group>')
          == [("MISSING", "component"), ("EXTRA", "component")],
          "a component on one side only is MISSING or EXTRA")
    check(sorted(rules(seq, seq, 'targetNamespace="urn:x"',
                       f'xmlns:vc="{odr.VC}" vc:minVersion="1.1"'))
          == [("EXTRA", "schema"), ("MISSING", "schema")],
          "the attributes of xs:schema are compared")
    both = swapped.replace('type="A"', 'type="A2"')
    check(rules(both, seq) == [("DIFFERENT", "component")],
          "content is compared order-free first, so a changed and moved particle is content")


# ---------------------------------------------------------------------------------------
# ea_api: the two loaders


TABLES = {
    "t_package": "Package_ID INTEGER, Name TEXT, Parent_ID INTEGER, TPos INTEGER, ea_guid TEXT",
    "t_object": "Object_ID INTEGER, Object_Type TEXT, Name TEXT, Stereotype TEXT, ea_guid TEXT, "
                "Package_ID INTEGER, Note TEXT, Abstract TEXT, GenLinks TEXT, ParentID INTEGER, "
                "TPos INTEGER",
    "t_attribute": "ID INTEGER, Object_ID INTEGER, Name TEXT, Type TEXT, LowerBound TEXT, "
                   "UpperBound TEXT, Stereotype TEXT, ea_guid TEXT, [Default] TEXT, Notes TEXT, "
                   "Classifier TEXT, Pos INTEGER",
    "t_connector": "Connector_ID INTEGER, Connector_Type TEXT, Start_Object_ID INTEGER, "
                   "End_Object_ID INTEGER, Stereotype TEXT, ea_guid TEXT, SourceRole TEXT, "
                   "SourceCard TEXT, DestRole TEXT, DestCard TEXT, Notes TEXT",
    "t_xref": "XrefID TEXT, Name TEXT, Client TEXT, Description TEXT",
    "t_objectproperties": "PropertyID INTEGER, Object_ID INTEGER, Property TEXT, Value TEXT, "
                          "Notes TEXT",
    "t_attributetag": "PropertyID INTEGER, ElementID INTEGER, Property TEXT, VALUE TEXT, "
                      "NOTES TEXT",
    "t_connectortag": "PropertyID INTEGER, ElementID INTEGER, Property TEXT, VALUE TEXT, "
                      "NOTES TEXT",
    "t_objectconstraint": 'Object_ID INTEGER, "Constraint" TEXT, ConstraintType TEXT, '
                          "Status TEXT, Notes TEXT",
}


def write_project(path: Path) -> None:
    db = sqlite3.connect(path)
    for table, columns in TABLES.items():
        db.execute(f"CREATE TABLE {table} ({columns})")
    rows = {
        "t_package": [(1, "Root", 0, 0, "{P1}"), (2, "B", 1, 0, "{P2}"), (3, "a", 1, 0, "{P3}")],
        "t_object": [
            (10, "Class", "ControlPoint", None, "{O10}", 2, "<b>Bold</b> &amp; plain", "0",
             None, 0, 0),
            (11, "Class", "Controller", "XSDcomplexType", "{O11}", 2, None, "1",
             "Parent=double;", 0, None),
            (12, "Class", "Nested", None, "{O12}", 2, None, "0", None, 11, 0),
            (13, "Package", "B", None, "{P2}", 1, None, "0", None, 0, 0),
        ],
        "t_attribute": [
            (100, 11, "zeta", "double", "1", "1", None, "{A100}", None, None, "0", 1),
            (101, 11, "Alpha", "t_x", "0", "1", "XSDattribute", "{A101}", None, None, "10", 1),
            (102, 11, "first", "int", "1", "1", None, "{A102}", None, None, None, None),
        ],
        "t_connector": [
            (201, "Association", 11, 10, "transient", "{C201}", None, None, "cp", "0..1", None),
            (200, "Association", 10, 11, None, "{C200}", None, None, "back", None, None),
        ],
        "t_xref": [("{X1}", "Stereotypes", "{O11}",
                    "@STEREO;Name=XSDcomplexType;@ENDSTEREO;@STEREO;Name=deprecated;@ENDSTEREO;"),
                   ("{X2}", "Stereotypes", "{A101}", "@STEREO;Name=XSDattribute;@ENDSTEREO;")],
        "t_objectproperties": [(2, 11, "modelGroup", "choice", None),
                               (1, 11, "modelGroup", "sequence", None)],
        "t_attributetag": [],
        "t_connectortag": [(1, 201, "position", "3", None)],
        "t_objectconstraint": [(11, "count(a) = 1", "Invariant", "Approved", None)],
    }
    for table, values in rows.items():
        for value in values:
            db.execute(f"INSERT INTO {table} VALUES ({', '.join('?' * len(value))})", value)
    db.commit()
    db.close()


SCXML_FIXTURE = f"""<sc:Model xmlns:sc="{SC}"><sc:packages><sc:Package>
<sc:name>Root</sc:name><sc:id>P1</sc:id><sc:packages><sc:Package>
<sc:name>B</sc:name><sc:id>P2</sc:id>
<sc:stereotypes><sc:Stereotype>XSDschema</sc:Stereotype></sc:stereotypes>
<sc:taggedValues><sc:TaggedValue><sc:name>elementFormDefault</sc:name>
<sc:values><sc:Value>qualified</sc:Value></sc:values></sc:TaggedValue></sc:taggedValues>
<sc:classes>
<sc:Class><sc:name>ControlPoint</sc:name><sc:id>10</sc:id></sc:Class>
<sc:Class><sc:name>Controller</sc:name><sc:id>11</sc:id>
<sc:descriptors><sc:documentation><sc:descriptorValues><sc:DescriptorValue>A &lt;b&gt;
</sc:DescriptorValue></sc:descriptorValues></sc:documentation></sc:descriptors>
<sc:supertypes><sc:SupertypeId>10</sc:SupertypeId></sc:supertypes>
<sc:properties><sc:Property><sc:name>speed</sc:name><sc:id>11_5</sc:id>
<sc:cardinality>1</sc:cardinality><sc:sequenceNumber>1</sc:sequenceNumber>
<sc:typeId>10</sc:typeId><sc:typeName>ControlPoint</sc:typeName></sc:Property>
<sc:Property><sc:name>cp</sc:name><sc:id>Tas7</sc:id><sc:cardinality>*</sc:cardinality>
<sc:sequenceNumber>2</sc:sequenceNumber><sc:typeId>10</sc:typeId>
<sc:isAttribute>false</sc:isAttribute><sc:associationId>as7</sc:associationId></sc:Property>
</sc:properties></sc:Class>
</sc:classes></sc:Package></sc:packages></sc:Package></sc:packages>
<sc:associations><sc:Association><sc:id>as7</sc:id>
<sc:stereotypes><sc:Stereotype>XSDelement</sc:Stereotype></sc:stereotypes>
<sc:end1><sc:Property><sc:name>role_Sas7</sc:name><sc:id>Sas7</sc:id>
<sc:cardinality>1</sc:cardinality><sc:isNavigable>false</sc:isNavigable>
<sc:sequenceNumber>1</sc:sequenceNumber><sc:typeId>11</sc:typeId>
<sc:isAttribute>false</sc:isAttribute><sc:inClassId>10</sc:inClassId></sc:Property></sc:end1>
<sc:end2 ref="Tas7"></sc:end2></sc:Association></sc:associations></sc:Model>"""


def test_loaders() -> None:
    print("ea_api")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "fixture.qeax"
        write_project(path)
        repo = open_qeax(path)
        root = repo.models[0]
        check([p.name for p in root.packages] == ["a", "B"],
              "packages in (TPos, Name) order, Name without regard to case")
        package = root.packages[1]
        check([e.name for e in package.elements] == ["Controller", "ControlPoint"],
              "Package.Elements: NOCASE name order, an unset TPos read as 0, nested elements "
              "left out, and the package's own element no member")
        controller = repo.elements[11]
        check(package.element is not None and package.element.element_id == 13,
              "Package.Element is the package's t_object row")
        check([e.name for e in controller.elements] == ["Nested"], "Element.Elements")
        check(controller.stereotype == "XSDcomplexType"
              and controller.stereotype_ex == ("XSDcomplexType", "deprecated"),
              "Stereotype is the column, StereotypeEx the t_xref entries")
        check([t.value for t in controller.tagged_values] == ["sequence", "choice"],
              "tagged values by PropertyID")
        check([a.name for a in controller.attributes] == ["first", "Alpha", "zeta"],
              "attributes by (Pos, Name): an unset Pos first, names without regard to case")
        check(controller.attributes[1].classifier_id == 10
              and controller.attributes[2].classifier_id is None,
              "a Classifier of 0 is no reference")
        check([c.connector_id for c in controller.connectors] == [200, 201]
              and repo.elements[10].connectors == controller.connectors,
              "Element.Connectors: every connector at either end, by id")
        transient = controller.connectors[1]
        check(transient.stereotype == "transient" and transient.stereotype_ex == (),
              "a stereotype only in the column is in Stereotype, not StereotypeEx")
        check(controller.gen_links == "Parent=double;" and controller.abstract
              and controller.constraints[0].name == "count(a) = 1",
              "GenLinks, Abstract and constraints are read")
        check(repo.elements[10].notes_text == "Bold & plain",
              "notes_text is EA's plain-text rendering")
        pointer = Path(tmp) / "pointer.qeax"
        pointer.write_text("version https://git-lfs.github.com/spec/v1\n")
        try:
            open_qeax(pointer)
            check(False, "a Git LFS pointer is refused")
        except NotAnEaProject:
            check(True, "a Git LFS pointer is refused")

        scxml = Path(tmp) / "fixture.scxml"
        scxml.write_text(SCXML_FIXTURE)
        repo = open_scxml(scxml)
        package = repo.models[0].packages[0]
        check(package.element.stereotype_ex == ("XSDschema",)
              and package.element.tagged_values == (TaggedValue("elementFormDefault",
                                                                "qualified"),),
              "a package's stereotypes and tags are its Package.Element's")
        check([e.name for e in package.elements] == ["Controller", "ControlPoint"],
              "classes in NOCASE name order")
        controller = repo.elements[11]
        check([a.name for a in controller.attributes] == ["speed"]
              and controller.attributes[0].lower_bound == "1"
              and controller.attributes[0].classifier_id == 10,
              "attributes only, bounds from the cardinality, typeId as the classifier")
        association = next(c for c in controller.connectors if c.type == "Association")
        check(association.client_id == 11 and association.supplier_id == 10
              and association.supplier_end.role == "cp"
              and association.supplier_end.cardinality == "0..*"
              and association.client_end.role is None
              and association.client_end.cardinality == "1..1",
              "an association: S end is the client, T end the supplier, role_ names are "
              "unnamed, and a cardinality is written lower..upper")
        general = [c for c in controller.connectors if c.type == "Generalization"]
        check(len(general) == 1 and general[0].supplier_id == 10
              and general[0].connector_id > 7, "a supertype is a generalization, numbered "
                                               "after every association")
        check(controller.notes_text == "A <b>\n" and controller.notes is None,
              "the exported documentation is notes_text, taken as written")


def main() -> int:
    test_osc()
    test_odr()
    test_equivalence()
    test_loaders()
    if FAILURES:
        print(f"\n{len(FAILURES)} check(s) failed")
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
