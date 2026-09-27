#!/usr/bin/env python3
"""Regression tests for ``model_equivalence.py``.

The comparison is the proof that the committed SCXML is ASAM's model, so it has to be right in
both directions: it must report every way the export can lose or invent information, and it
must report nothing for a faithful export. Each case below builds a small EA project - an
SQLite database with the columns of EA's own tables - and the SCXML ShapeChange writes for it,
changes one fact, and states the complete list of findings that change produces, verdict and
rule. A case passes only when the findings are exactly that list.

Two kinds of case keep the comparison honest:

- **Negative cases**, one or more for every rule in ``RULES``. The run fails if a rule has
  none, so a rule cannot be added without a case that shows it firing.
- **Faithful cases**, which must produce no finding at all: the base pair, which follows the
  structure of the committed exports, and one per value ShapeChange derives rather than
  copies - a constructed association name, a role name for an unnamed end, the
  ``enumeration`` stereotype, composition on attributes, lower-cased containment, a type bound
  by name, a constraint's rendered text, an end matched by id rather than by position.

The losses the committed exports actually have are all reproduced: a connector stereotype EA
stores only in ``t_connector.Stereotype``, a classifier owned by another classifier, a
realization, a stereotype on a generalization, a generalization EA records by name in
``GenLinks``, a valued tag outside the export's allow-list, ``isID``, a constraint,
visibility, and a navigability EA states and the export contradicts.

No JDK, no ShapeChange, no EA: this runs in a pull-request workflow.

Run:  python scripts/test_model_equivalence.py
"""

from __future__ import annotations

import sqlite3
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from model_equivalence import (
    RULES,
    SC,
    NotAnEaProject,
    VacuousComparison,
    compare,
    ea_txt,
    java_trim,
    read_qeax,
    read_scxml,
)

FAILURES: list[str] = []
EXERCISED: set[str] = set()


def check(condition: bool, what: str) -> None:
    if condition:
        print(f"  ok   {what}")
    else:
        print(f"  FAIL {what}")
        FAILURES.append(what)


# ---------------------------------------------------------------------------------------
# A minimal EA project. Only the columns the reader uses exist; EA's real tables have more.

SCHEMA = {
    "t_package": "Package_ID, Name, Parent_ID, Notes, ea_guid",
    "t_object": "Object_ID, Object_Type, Name, Alias, Note, Package_ID, Stereotype, Abstract, "
                "IsLeaf, Scope, ea_guid, ParentID, GenLinks, IsRoot, IsSpec, IsActive, "
                "Multiplicity, Persistence, NType, Classifier",
    "t_attribute": "Object_ID, Name, Scope, Stereotype, Containment, IsStatic, IsCollection, "
                   "IsOrdered, AllowDuplicates, LowerBound, UpperBound, Container, Notes, "
                   "Derived, ID, Pos, Length, Precision, Scale, Const, Style, Classifier, "
                   "[Default], Type, ea_guid, StyleEx",
    "t_connector": "Connector_ID, Name, Direction, Notes, Connector_Type, SubType, SourceCard, "
                   "DestCard, SourceRole, SourceRoleNote, SourceContainment, SourceIsAggregate, "
                   "SourceIsOrdered, SourceQualifier, DestRole, DestRoleNote, DestContainment, "
                   "DestIsAggregate, DestIsOrdered, DestQualifier, Start_Object_ID, "
                   "End_Object_ID, Stereotype, ea_guid, SourceConstraint, DestConstraint, "
                   "SourceChangeable, DestChangeable, StyleEx, SourceStereotype, "
                   "DestStereotype, SourceStyle, DestStyle, SourceAccess, DestAccess, "
                   "SourceTS, DestTS, IsLeaf, IsRoot, IsSpec",
    "t_xref": "Name, Type, Description, Client",
    "t_objectproperties": "PropertyID, Object_ID, Property, Value, Notes",
    "t_attributetag": "PropertyID, ElementID, Property, VALUE, NOTES",
    "t_connectortag": "PropertyID, ElementID, Property, VALUE, NOTES",
    "t_taggedvalue": "PropertyID, ElementID, BaseClass, TagValue, Notes",
    "t_objectconstraint": "Object_ID, [Constraint], ConstraintType, Notes, Status",
    "t_attributeconstraints": "Object_ID, [Constraint], Type, Notes, ID",
    "t_operation": "OperationID, Object_ID, Name",
    "t_diagram": "Diagram_ID",
    "t_document": "DocID, DocType",
    "t_genopt": "AppliesTo, Option",
}


def base_rows() -> dict[str, list[dict]]:
    """A faithful model: one schema package, classes A and B, enumeration E, one association
    A -> B (A composes B), and B specializing A."""
    return {
        "t_package": [
            {"Package_ID": 1, "Name": "Model", "Parent_ID": 0, "ea_guid": "{P1}"},
            {"Package_ID": 2, "Name": "Schema", "Parent_ID": 1, "Notes": "The schema.",
             "ea_guid": "{P2}"},
        ],
        "t_object": [
            {"Object_ID": 1, "Object_Type": "Package", "Name": "Schema", "Package_ID": 1,
             "Stereotype": "XSDschema", "Scope": "Public", "ea_guid": "{P2}"},
            {"Object_ID": 10, "Object_Type": "Class", "Name": "A", "Package_ID": 2,
             "Note": "The <b>A</b> class.", "Abstract": "0", "Scope": "Public",
             "ea_guid": "{A}", "ParentID": 0},
            {"Object_ID": 11, "Object_Type": "Class", "Name": "B", "Package_ID": 2,
             "Abstract": "0", "Scope": "Public", "ea_guid": "{B}", "ParentID": 0},
            {"Object_ID": 12, "Object_Type": "Enumeration", "Name": "E", "Package_ID": 2,
             "Abstract": "0", "Scope": "Public", "ea_guid": "{E}", "ParentID": 0},
        ],
        "t_attribute": [
            {"Object_ID": 10, "ID": 100, "Name": "x", "Scope": "Public", "LowerBound": "0",
             "UpperBound": "1", "Classifier": "11", "Type": "B", "Pos": 0, "ea_guid": "{A.x}",
             "Containment": "Not Specified", "StyleEx": "IsLiteral=0;"},
            {"Object_ID": 10, "ID": 101, "Name": "y", "Scope": "Public", "Classifier": "0",
             "Type": "string", "Pos": 1, "Default": '"hello"', "ea_guid": "{A.y}"},
            {"Object_ID": 12, "ID": 102, "Name": "red", "Scope": "Public", "Pos": 0,
             "ea_guid": "{E.red}", "StyleEx": "IsLiteral=1;"},
        ],
        "t_connector": [
            {"Connector_ID": 500, "Connector_Type": "Association",
             "Direction": "Source -> Destination", "Start_Object_ID": 10, "End_Object_ID": 11,
             "SourceCard": "0..*", "DestRole": "b", "DestCard": "1", "SourceIsAggregate": 2,
             "SourceStyle": "Union=0;Derived=0;AllowDuplicates=0;Navigable=Unspecified;Owned=0;",
             "DestStyle": "Union=0;Derived=0;AllowDuplicates=0;Navigable=Navigable;Owned=0;",
             "SourceAccess": "Public", "DestAccess": "Public", "SourceTS": "instance",
             "DestTS": "instance", "SourceChangeable": "none", "DestChangeable": "none",
             "SourceContainment": "Unspecified", "ea_guid": "{C500}"},
            {"Connector_ID": 501, "Connector_Type": "Generalization", "Start_Object_ID": 11,
             "End_Object_ID": 10, "ea_guid": "{C501}"},
        ],
        "t_xref": [
            {"Name": "Stereotypes", "Type": "element property", "Client": "{P2}",
             "Description": "@STEREO;Name=XSDschema;GUID={S1};FQName=osc::XSDschema;@ENDSTEREO;"},
        ],
        "t_objectproperties": [
            {"PropertyID": 1, "Object_ID": 10, "Property": "modelGroup", "Value": "sequence",
             "Notes": "Help text from the XML Schema profile, not a value."},
        ],
        "t_attributetag": [], "t_connectortag": [], "t_taggedvalue": [],
        "t_objectconstraint": [], "t_attributeconstraints": [], "t_operation": [],
        "t_diagram": [{"Diagram_ID": 1}],
        "t_document": [{"DocID": "{D1}", "DocType": "Baseline"}],
        "t_genopt": [{"AppliesTo": "Java", "Option": "x"}],
    }


def write_qeax(rows: dict, path: Path) -> None:
    db = sqlite3.connect(path)
    for table, columns in SCHEMA.items():
        db.execute(f"CREATE TABLE {table} ({columns})")
        names = [c.strip().strip("[]") for c in columns.split(",")]
        for row in rows.get(table, []):
            unknown = set(row) - set(names)
            assert not unknown, f"{table} has no column {unknown}"
            db.execute(f"INSERT INTO {table} ({columns}) VALUES ({', '.join('?' * len(names))})",
                       [row.get(n) for n in names])
    db.commit()
    db.close()


def doc(text: str) -> str:
    """A documentation and definition descriptor pair, as ShapeChange writes them."""
    value = f"<sc:descriptorValues><sc:DescriptorValue>{text}</sc:DescriptorValue>" \
            "</sc:descriptorValues>"
    return f"<sc:documentation>{value}</sc:documentation><sc:definition>{value}</sc:definition>"


# The SCXML ShapeChange writes for base_rows(), including every value it derives.
BASE_SCXML = f"""<?xml version="1.0" encoding="UTF-8"?>
<sc:Model xmlns:sc="{SC}">
  <sc:packages>
    <sc:Package editable="false">
      <sc:name>Model</sc:name>
      <sc:id>P1</sc:id>
      <sc:packages>
        <sc:Package>
          <sc:name>Schema</sc:name>
          <sc:id>P2</sc:id>
          <sc:stereotypes><sc:Stereotype>XSDschema</sc:Stereotype></sc:stereotypes>
          <sc:descriptors>{doc("The schema.")}</sc:descriptors>
          <sc:classes>
            <sc:Class>
              <sc:name>A</sc:name>
              <sc:id>10</sc:id>
              <sc:descriptors>{doc("The A class.")}</sc:descriptors>
              <sc:taggedValues>
                <sc:TaggedValue><sc:name>modelGroup</sc:name>
                  <sc:values><sc:Value>sequence</sc:Value></sc:values></sc:TaggedValue>
              </sc:taggedValues>
              <sc:subtypes><sc:SubtypeId>11</sc:SubtypeId></sc:subtypes>
              <sc:properties>
                <sc:Property>
                  <sc:name>x</sc:name><sc:id>10_100</sc:id><sc:cardinality>0..1</sc:cardinality>
                  <sc:sequenceNumber>-1073741824</sc:sequenceNumber>
                  <sc:typeId>11</sc:typeId><sc:typeName>B</sc:typeName>
                  <sc:isComposition>true</sc:isComposition>
                </sc:Property>
                <sc:Property>
                  <sc:name>y</sc:name><sc:id>10_101</sc:id>
                  <sc:sequenceNumber>-1073741823</sc:sequenceNumber>
                  <sc:typeName>string</sc:typeName><sc:initialValue>hello</sc:initialValue>
                  <sc:isComposition>true</sc:isComposition>
                </sc:Property>
                <sc:Property>
                  <sc:name>b</sc:name><sc:id>Tas500</sc:id>
                  <sc:sequenceNumber>-536870911</sc:sequenceNumber>
                  <sc:isAttribute>false</sc:isAttribute>
                  <sc:typeId>11</sc:typeId><sc:typeName>B</sc:typeName>
                  <sc:isComposition>true</sc:isComposition>
                  <sc:associationId>as500</sc:associationId>
                </sc:Property>
              </sc:properties>
            </sc:Class>
            <sc:Class>
              <sc:name>B</sc:name>
              <sc:id>11</sc:id>
              <sc:supertypes><sc:SupertypeId>10</sc:SupertypeId></sc:supertypes>
            </sc:Class>
            <sc:Class>
              <sc:name>E</sc:name>
              <sc:id>12</sc:id>
              <sc:stereotypes><sc:Stereotype>enumeration</sc:Stereotype></sc:stereotypes>
              <sc:properties>
                <sc:Property>
                  <sc:name>red</sc:name><sc:id>12_102</sc:id>
                  <sc:sequenceNumber>-1073741822</sc:sequenceNumber>
                </sc:Property>
              </sc:properties>
            </sc:Class>
          </sc:classes>
        </sc:Package>
      </sc:packages>
    </sc:Package>
  </sc:packages>
  <sc:associations>
    <sc:Association>
      <sc:name>A_B</sc:name>
      <sc:id>as500</sc:id>
      <sc:end1>
        <sc:Property>
          <sc:name>role_Sas500</sc:name><sc:id>Sas500</sc:id><sc:cardinality>0..*</sc:cardinality>
          <sc:isNavigable>false</sc:isNavigable>
          <sc:sequenceNumber>-536870912</sc:sequenceNumber>
          <sc:isAttribute>false</sc:isAttribute>
          <sc:typeId>10</sc:typeId><sc:typeName>A</sc:typeName>
          <sc:inClassId>11</sc:inClassId><sc:associationId>as500</sc:associationId>
        </sc:Property>
      </sc:end1>
      <sc:end2 ref="Tas500"/>
    </sc:Association>
  </sc:associations>
</sc:Model>
"""

ET.register_namespace("sc", SC)


def q(tag: str) -> str:
    return f"{{{SC}}}{tag}"


def by_id(root: ET.Element, element_id: str) -> ET.Element:
    """The element (Package, Class, Property, Association) whose ``sc:id`` is ``element_id``."""
    for element in root.iter():
        child = element.find(q("id"))
        if child is not None and child.text == element_id:
            return element
    raise KeyError(element_id)


def parent_of(root: ET.Element, element: ET.Element) -> ET.Element:
    return next(p for p in root.iter() if element in list(p))


def set_child(element: ET.Element, tag: str, text: str | None) -> None:
    child = element.find(q(tag))
    if text is None:
        if child is not None:
            element.remove(child)
        return
    if child is None:
        child = ET.SubElement(element, q(tag))
    child.text = text


def add(element: ET.Element, tag: str, text: str | None = None, **attributes) -> ET.Element:
    child = ET.SubElement(element, q(tag), attributes)
    child.text = text
    return child


def holder(element: ET.Element, tag: str) -> ET.Element:
    found = element.find(q(tag))
    return found if found is not None else add(element, tag)


def add_stereotype(element: ET.Element, name: str) -> None:
    add(holder(element, "stereotypes"), "Stereotype", name)


def add_tag(element: ET.Element, name: str, *values: str) -> None:
    """One tagged value, with all its values, as ShapeChange writes it."""
    tag = add(holder(element, "taggedValues"), "TaggedValue")
    add(tag, "name", name)
    holder_ = add(tag, "values")
    for value in values:
        add(holder_, "Value", value)


def add_descriptor(element: ET.Element, kind: str, text: str, lang: str | None = None) -> None:
    values = add(add(holder(element, "descriptors"), kind), "descriptorValues")
    value = add(values, "DescriptorValue", text)
    if lang:
        value.set("lang", lang)


def set_documentation(element: ET.Element, text: str) -> None:
    for kind in ("documentation", "definition"):
        found = element.find(f"{q('descriptors')}/{q(kind)}")
        if found is not None:
            found.find(f"{q('descriptorValues')}/{q('DescriptorValue')}").text = text
        else:
            add_descriptor(element, kind, text)


def row(rows: dict, table: str, **match) -> dict:
    return next(r for r in rows[table] if all(r.get(k) == v for k, v in match.items()))


def obj(rows: dict, oid: int) -> dict:
    return row(rows, "t_object", Object_ID=oid)


def attr(rows: dict, aid: int) -> dict:
    return row(rows, "t_attribute", ID=aid)


def conn(rows: dict, cid: int) -> dict:
    return row(rows, "t_connector", Connector_ID=cid)


def run(rows: dict, root: ET.Element):
    """Compare a (possibly edited) model and export; returns (findings, model)."""
    with tempfile.TemporaryDirectory() as tmp:
        qeax, export = Path(tmp) / "m.qeax", Path(tmp) / "m.scxml"
        write_qeax(rows, qeax)
        ET.ElementTree(root).write(export, encoding="UTF-8", xml_declaration=True)
        model = read_qeax(qeax)
        return compare(model, read_scxml(export)), model


def case(what: str, edit=None, expect=(), contains: str | None = None):
    """Apply ``edit(rows, root)`` to the faithful pair; the findings must be exactly
    ``expect``, a list of (verdict, rule), and one of them must contain ``contains``."""
    rows, root = base_rows(), ET.fromstring(BASE_SCXML)
    if edit is not None:
        edit(rows, root)
    findings, model = run(rows, root)
    got = sorted((f.verdict, f.rule) for f in findings)
    ok = got == sorted(expect) and (contains is None or any(contains in f.key for f in findings))
    if ok:
        EXERCISED.update(rule for _, rule in expect)
    check(ok, what if ok else f"{what}\n         got {[(f.verdict, f.key) for f in findings]}")
    return findings, model


def M(rule: str) -> tuple:
    return ("MISSING", rule)


def X(rule: str) -> tuple:
    return ("EXTRA", rule)


def D(rule: str) -> tuple:
    return ("DIFFERENT", rule)


# ---------------------------------------------------------------------------------------
print("The faithful pair produces no finding")
findings, model = case("zero findings, derived values included")
check(model.empty_tags == {}, "no empty tags in the faithful model")
check(model.out_of_scope["t_diagram rows"] == 1 and model.out_of_scope["t_document Baseline"]
      == 1, "diagrams and EA documents are counted as out of scope")
check(model.out_of_scope["EA configuration table t_genopt"] == 1,
      "every other EA table is counted as configuration")

# ---------------------------------------------------------------------------------------
print("\nThe SCXML file is read totally")
case("a child element the check does not compare", expect=[X("export-element")],
     contains="linkedDocument",
     edit=lambda r, x: add(by_id(x, "10"), "linkedDocument", "doc.docx"))
case("an XML attribute the check does not compare", expect=[X("export-element")],
     contains="'color'", edit=lambda r, x: by_id(x, "10").set("color", "red"))
case("a repeated single child: reported, and the last one wins, as in ShapeChange",
     expect=[X("export-element"), D("attribute-type")],
     edit=lambda r, x: add(by_id(x, "10_100"), "typeId", "12"))
case("a list item under a non-canonical tag is reported and still read",
     expect=[X("export-element")],
     edit=lambda r, x: (conn(r, 500).update(Stereotype="transient"),
                        add(holder(by_id(x, "as500"), "stereotypes"), "Stereo", "transient")))
def class_in_packages(rows, root):
    cls = add(holder(by_id(root, "P2"), "packages"), "Class")
    add(cls, "name", "Stray")
    add(cls, "id", "99")


case("a class inside <packages> is reported and read as a class of the package",
     expect=[X("export-element"), X("classifier")], edit=class_in_packages)
case("an element without an id", expect=[D("export-id"), M("attribute"), X("attribute")],
     edit=lambda r, x: set_child(by_id(x, "10_101"), "id", None))
case("a value that is not an xs:boolean; ShapeChange reads 'yes' as false",
     expect=[D("export-value")], edit=lambda r, x: set_child(by_id(x, "10"), "isAbstract", "yes"))
case("'True' is read as true, as ShapeChange reads it, and reported",
     expect=[D("export-value"), D("classifier-abstract")],
     edit=lambda r, x: set_child(by_id(x, "10"), "isAbstract", "True"))
case("'1' is an xs:boolean true",
     edit=lambda r, x: set_child(by_id(x, "10_100"), "isComposition", "1"))
case("a descriptor value in a language", expect=[X("export-descriptor")], contains="'de'",
     edit=lambda r, x: by_id(x, "10").find(f"{q('descriptors')}/{q('documentation')}/"
                                           f"{q('descriptorValues')}/{q('DescriptorValue')}")
     .set("lang", "de"))
case("a repeated id", expect=[X("duplicate-id")],
     edit=lambda r, x: by_id(x, "P2").find(q("classes")).append(
         ET.fromstring(ET.tostring(by_id(x, "11")))))
case("a role property no association end uses", expect=[X("property")],
     edit=lambda r, x: [add(p, t, v) for p in [add(holder(by_id(x, "11"), "properties"),
                                                   "Property")]
                        for t, v in (("name", "ghost"), ("id", "Tas999"),
                                     ("sequenceNumber", "-536870000"), ("isAttribute", "false"),
                                     ("typeId", "10"))])
case("a property without a sequenceNumber", expect=[D("property-sequence-number")],
     edit=lambda r, x: set_child(by_id(x, "10_101"), "sequenceNumber", None))
case("two properties of one class sharing a sequenceNumber (a tie, not an inversion)",
     expect=[D("property-sequence-number")],
     edit=lambda r, x: set_child(by_id(x, "10_101"), "sequenceNumber", "-1073741824"))
case("a structured sequence number is a sequence number",
     edit=lambda r, x: set_child(by_id(x, "10_101"), "sequenceNumber", "-1073741823.1"))
case("an end referring to no property", expect=[M("end"), D("association-endpoint"),
                                                X("property")],
     edit=lambda r, x: x.find(f".//{q('end2')}").set("ref", "Tas999"))
case("a non-navigable end inside its class, which ShapeChange's reader removes",
     expect=[D("end-placement"), D("end-navigability")],
     edit=lambda r, x: set_child(by_id(x, "Tas500"), "isNavigable", "false"))


def navigable_end_inline(rows, root):
    tas = by_id(root, "Tas500")
    parent_of(root, tas).remove(tas)
    end2 = root.find(f".//{q('end2')}")
    del end2.attrib["ref"]
    end2.append(tas)
    add(tas, "inClassId", "10")


case("a navigable end written inline, which ShapeChange's reader keeps out of its class",
     expect=[D("end-placement")], edit=navigable_end_inline)


def swap_ends(rows, root):
    association = by_id(root, "as500")
    end1, end2 = association.find(q("end1")), association.find(q("end2"))
    end1.tag, end2.tag = q("end2"), q("end1")


case("ends are matched by id; swapped positions are reported", edit=swap_ends,
     expect=[D("end-placement"), D("end-placement")])

case("a child in a foreign namespace", expect=[X("export-element")],
     edit=lambda r, x: ET.SubElement(by_id(x, "10"), "{urn:other}isAbstract").__setattr__(
         "text", "true"))
case("a value holding a child element", expect=[X("export-element")],
     edit=lambda r, x: add(by_id(x, "10").find(q("name")), "x", "B"))
case("text between elements", expect=[X("export-element")],
     edit=lambda r, x: by_id(x, "10").find(q("name")).__setattr__("tail", "stray"))
case("a tagged value without a name", expect=[M("export-element"), X("classifier-tag")],
     edit=lambda r, x: add(add(holder(by_id(x, "10"), "taggedValues"), "TaggedValue"),
                           "values").append(ET.fromstring(f'<sc:Value xmlns:sc="{SC}">v'
                                                          '</sc:Value>')))
case("a descriptor without values, which ShapeChange's reader cannot load",
     expect=[M("export-element")],
     edit=lambda r, x: add(holder(by_id(x, "10"), "descriptors"), "example"))
case("a tagged value name repeated", expect=[X("export-element"), D("classifier-tag")],
     edit=lambda r, x: add_tag(by_id(x, "10"), "modelGroup", "sequence"))
case("a sequence number with surrounding whitespace", expect=[D("property-sequence-number")],
     edit=lambda r, x: set_child(by_id(x, "10_101"), "sequenceNumber", " -1073741823"))
case("a boolean Java's trim() cannot clean is read as ShapeChange reads it",
     expect=[D("export-value")],
     edit=lambda r, x: set_child(by_id(x, "10"), "isAbstract", "\u00a0true"))
case("a non-canonical item in <properties> is reported, not read as a property",
     expect=[X("export-element")],
     edit=lambda r, x: add(by_id(x, "10").find(q("properties")), "Operation"))


def two_property_lists(rows, root):
    cls = by_id(root, "10")
    prop = by_id(root, "10_101")
    cls.find(q("properties")).remove(prop)
    add(cls, "properties").append(prop)


case("a second <properties>: reported, and every property still read",
     expect=[X("export-element")], edit=two_property_lists)
case("a repeated subtype is reported, and read as the set ShapeChange reads",
     expect=[X("export-element")],
     edit=lambda r, x: add(by_id(x, "10").find(q("subtypes")), "SubtypeId", "11"))
case("two documentation values: the first is ShapeChange's", expect=[X("export-descriptor")],
     edit=lambda r, x: add(by_id(x, "10").find(f"{q('descriptors')}/{q('documentation')}/"
                                               f"{q('descriptorValues')}"),
                           "DescriptorValue", "Another."))

# ---------------------------------------------------------------------------------------
print("\nPackages")
case("a package the export lacks", expect=[M("package")],
     edit=lambda r, x: r["t_package"].append({"Package_ID": 3, "Name": "Extra", "Parent_ID": 1,
                                              "ea_guid": "{P3}"}))
case("a package name", expect=[D("package-name")],
     edit=lambda r, x: set_child(by_id(x, "P2"), "name", "Other"))
case("a package parent", expect=[X("package-parent")],
     edit=lambda r, x: row(r, "t_package", Package_ID=2).update(Parent_ID=0))
case("a package stereotype", expect=[M("package-stereotype")],
     edit=lambda r, x: by_id(x, "P2").remove(by_id(x, "P2").find(q("stereotypes"))))
case("a package tag", expect=[M("package-tag")],
     edit=lambda r, x: r["t_objectproperties"].append(
         {"PropertyID": 2, "Object_ID": 1, "Property": "xmlns", "Value": "osc"}))
case("package documentation", expect=[M("package-documentation")],
     edit=lambda r, x: by_id(x, "P2").remove(by_id(x, "P2").find(q("descriptors"))))
case("a package definition", expect=[D("package-definition")],
     edit=lambda r, x: by_id(x, "P2").find(f"{q('descriptors')}/{q('definition')}/"
                                           f"{q('descriptorValues')}/{q('DescriptorValue')}")
     .__setattr__("text", "Other."))
case("a package alias", expect=[M("package-alias")],
     edit=lambda r, x: obj(r, 1).update(Alias="S"))
case("a hyperlink in a package note", expect=[M("package-documentation-link")],
     edit=lambda r, x: (row(r, "t_package", Package_ID=2).update(
         Notes='See <a href="$inet://https://example.org/p">it</a>.'),
         set_documentation(by_id(x, "P2"), "See it.")))
case("a descriptor ShapeChange fills from a same-named tag", expect=[M("package-descriptor")],
     edit=lambda r, x: (r["t_objectproperties"].append(
         {"PropertyID": 2, "Object_ID": 1, "Property": "example", "Value": "e"}),
         add_tag(by_id(x, "P2"), "example", "e")))
case("the same descriptor, exported", edit=lambda r, x: (r["t_objectproperties"].append(
    {"PropertyID": 2, "Object_ID": 1, "Property": "example", "Value": "e"}),
    add_tag(by_id(x, "P2"), "example", "e"), add_descriptor(by_id(x, "P2"), "example", "e")))
case("a private package", expect=[M("package-visibility")],
     edit=lambda r, x: obj(r, 1).update(Scope="Private"))
case("a package flag the SCXML cannot carry", expect=[M("package-unrepresentable")],
     edit=lambda r, x: obj(r, 1).update(IsActive=1))
case("EA's second copy of a package note, when it differs", expect=[M("package-element-note")],
     edit=lambda r, x: obj(r, 1).update(Note="Another text."))

# ---------------------------------------------------------------------------------------
print("\nClassifiers and elements")
case("a classifier the export lacks", expect=[M("classifier")],
     edit=lambda r, x: r["t_object"].append({"Object_ID": 13, "Object_Type": "Class",
                                             "Name": "C", "Package_ID": 2, "ea_guid": "{C}"}))
case("a classifier owned by a classifier, and its association",
     expect=[M("nested-classifier"), M("association")],
     contains="end classifier 13 Root is not exported",
     edit=lambda r, x: (r["t_object"].append({"Object_ID": 13, "Object_Type": "Class",
                                              "Name": "Root", "Package_ID": 2,
                                              "ea_guid": "{R}", "ParentID": 10}),
                        r["t_connector"].append({"Connector_ID": 502, "Start_Object_ID": 13,
                                                 "Connector_Type": "Association",
                                                 "End_Object_ID": 11, "ea_guid": "{C502}"})))
case("an exported classifier the model nests in another", expect=[D("classifier-owner")],
     edit=lambda r, x: obj(r, 11).update(ParentID=10))
case("a PrimitiveType; the attribute typed by it keeps only the type name",
     expect=[M("element-type")],
     edit=lambda r, x: (r["t_object"].append({"Object_ID": 14, "Object_Type": "PrimitiveType",
                                              "Name": "double", "Package_ID": 2,
                                              "ea_guid": "{D}"}),
                        attr(r, 101).update(Classifier="14", Type="double"),
                        set_child(by_id(x, "10_101"), "typeName", "double")))
case("a classifier name", expect=[D("classifier-name")],
     edit=lambda r, x: set_child(by_id(x, "10"), "name", "A2"))
case("a classifier's package", expect=[D("classifier-package")],
     edit=lambda r, x: obj(r, 11).update(Package_ID=1))
case("an abstract flag", expect=[D("classifier-abstract")],
     edit=lambda r, x: set_child(by_id(x, "10"), "isAbstract", "true"))
case("a leaf flag", expect=[D("classifier-leaf")],
     edit=lambda r, x: set_child(by_id(x, "10"), "isLeaf", "true"))
case("an Interface's kind", expect=[M("classifier-kind")],
     edit=lambda r, x: obj(r, 10).update(Object_Type="Interface"))
case("a private classifier", expect=[M("classifier-visibility")],
     edit=lambda r, x: obj(r, 10).update(Scope="Private"))
case("an active class", expect=[M("classifier-unrepresentable")], contains="IsActive=1",
     edit=lambda r, x: obj(r, 10).update(IsActive=1))
case("an exported stereotype the model lacks", expect=[X("classifier-stereotype")],
     edit=lambda r, x: add_stereotype(by_id(x, "10"), "invented"))
case("the enumeration stereotype ShapeChange derives must be there",
     expect=[M("classifier-stereotype")],
     edit=lambda r, x: by_id(x, "12").remove(by_id(x, "12").find(q("stereotypes"))))
case("a changed tag value", expect=[D("classifier-tag")],
     edit=lambda r, x: row(r, "t_objectproperties", PropertyID=1).update(Value="choice"))
case("classifier documentation", expect=[D("classifier-documentation")],
     edit=lambda r, x: set_documentation(by_id(x, "10"), "Another class."))
case("a classifier definition", expect=[D("classifier-definition")],
     edit=lambda r, x: by_id(x, "10").find(f"{q('descriptors')}/{q('definition')}/"
                                           f"{q('descriptorValues')}/{q('DescriptorValue')}")
     .__setattr__("text", "Other."))
case("a classifier alias", expect=[M("classifier-alias")],
     edit=lambda r, x: obj(r, 10).update(Alias="AA"))
case("a hyperlink in a classifier note", expect=[M("classifier-documentation-link")],
     contains="https://example.org/spec",
     edit=lambda r, x: (obj(r, 10).update(Note='See <a href="$inet://https://example.org/spec">'
                                               '<font color="#0000ff"><u>it</u></font></a>.'),
                        set_documentation(by_id(x, "10"), "See it.")))
case("a descriptor whose source is none", expect=[X("classifier-descriptor")],
     edit=lambda r, x: add_descriptor(by_id(x, "10"), "description", "A description."))
case("a whitespace-only note is no documentation",
     edit=lambda r, x: obj(r, 11).update(Note="  \r\n "))
case("Java's trim() keeps a no-break space",
     edit=lambda r, x: (obj(r, 11).update(Note="B "),
                        set_documentation(by_id(x, "11"), "B ")))

# ---------------------------------------------------------------------------------------
print("\nGeneralizations, realizations, other connectors")
case("a dropped generalization", expect=[M("generalization")],
     edit=lambda r, x: (by_id(x, "11").remove(by_id(x, "11").find(q("supertypes"))),
                        by_id(x, "10").remove(by_id(x, "10").find(q("subtypes")))))
case("a second generalization between the same classes is counted, not merged",
     expect=[M("generalization")], contains="connector 504",
     edit=lambda r, x: r["t_connector"].append({"Connector_ID": 504, "Start_Object_ID": 11,
                                                "Connector_Type": "Generalization",
                                                "End_Object_ID": 10, "ea_guid": "{C504}"}))
case("a supertype the model lacks", expect=[X("generalization"), D("subtypes")],
     edit=lambda r, x: add(holder(by_id(x, "12"), "supertypes"), "SupertypeId", "10"))
case("a generalization stereotype", expect=[M("generalization-stereotype")],
     edit=lambda r, x: conn(r, 501).update(Stereotype="XSDextension"))
case("a generalization tag", expect=[M("generalization-tag")],
     edit=lambda r, x: r["t_connectortag"].append({"PropertyID": 1, "ElementID": 501,
                                                   "Property": "k", "VALUE": "v"}))
case("generalization notes", expect=[M("generalization-documentation")],
     edit=lambda r, x: conn(r, 501).update(Notes="Why."))
case("a generalization custom property", expect=[M("generalization-unrepresentable")],
     edit=lambda r, x: r["t_xref"].append({"Name": "CustomProperties", "Type": "connector property",
                                           "Client": "{C501}", "Description":
                                           "@PROP=@NAME=p@ENDNAME;@VALU=1@ENDVALU;@ENDPROP;"}))
case("a generalization EA records by name", expect=[M("generalization-by-name")],
     contains="Parent=double", edit=lambda r, x: obj(r, 10).update(GenLinks="Parent=double;"))
case("two identical GenLinks entries are two findings",
     expect=[M("generalization-by-name"), M("generalization-by-name")],
     edit=lambda r, x: obj(r, 10).update(GenLinks="Parent=double;Parent=double;"))
case("a GenLinks parent the export carries as a supertype",
     edit=lambda r, x: (obj(r, 12).update(GenLinks="Parent=B;"),
                        add(holder(by_id(x, "12"), "supertypes"), "SupertypeId", "11"),
                        add(holder(by_id(x, "11"), "subtypes"), "SubtypeId", "12")))
case("a realization EA records by name", expect=[M("realization-by-name")],
     edit=lambda r, x: obj(r, 10).update(GenLinks="Implements=E;"))
case("a GenLinks realization the export carries as a supertype",
     expect=[D("realization-by-name")],
     edit=lambda r, x: (obj(r, 10).update(GenLinks="Implements=E;"),
                        add(holder(by_id(x, "10"), "supertypes"), "SupertypeId", "12"),
                        add(holder(by_id(x, "12"), "subtypes"), "SubtypeId", "10")))
case("a realization's custom property is named in its finding", expect=[M("realization")],
     contains="custom property p=1",
     edit=lambda r, x: (r["t_connector"].append({"Connector_ID": 503, "Start_Object_ID": 10,
                                                 "Connector_Type": "Realisation",
                                                 "End_Object_ID": 12, "ea_guid": "{C503}"}),
                        r["t_xref"].append({"Name": "CustomProperties", "Client": "{C503}",
                                            "Type": "connector property", "Description":
                                            "@PROP=@NAME=p@ENDNAME;@VALU=1@ENDVALU;@ENDPROP;"})))
case("a custom property on a generalization end", expect=[M("generalization-unrepresentable")],
     contains="S end",
     edit=lambda r, x: r["t_xref"].append({"Name": "CustomProperties", "Client": "{C501}",
                                           "Type": "connectorSrcEnd property", "Description":
                                           "@PROP=@NAME=p@ENDNAME;@VALU=1@ENDVALU;@ENDPROP;"}))
_, model = case("a t_xref row about a part its owner does not have is counted",
                edit=lambda r, x: r["t_xref"].append(
                    {"Name": "Stereotypes", "Client": "{A}", "Type": "connectorSrcEnd property",
                     "Description": "@STEREO;Name=s;@ENDSTEREO;"}))
check(model.out_of_scope["t_xref rows describing a part their owner does not have"] == 1,
      "... as out of scope")
_, model = case("an empty association-end tag on a generalization is counted",
                edit=lambda r, x: r["t_taggedvalue"].append(
                    {"PropertyID": 1, "ElementID": "{C501}", "BaseClass": "ASSOCIATION_SOURCE",
                     "TagValue": "position", "Notes": ""}))
check(model.empty_tags[("connector end", "position")] == 1, "... as an empty tag")
case("a realization", expect=[M("realization")],
     edit=lambda r, x: r["t_connector"].append({"Connector_ID": 503, "Start_Object_ID": 10,
                                                "Connector_Type": "Realisation",
                                                "End_Object_ID": 12, "ea_guid": "{C503}"}))
case("subtypes that do not mirror the supertypes", expect=[D("subtypes")],
     edit=lambda r, x: by_id(x, "10").remove(by_id(x, "10").find(q("subtypes"))))
case("a connector of another UML type", expect=[M("connector-type")],
     edit=lambda r, x: r["t_connector"].append({"Connector_ID": 505, "Start_Object_ID": 10,
                                                "Connector_Type": "Dependency",
                                                "End_Object_ID": 11, "ea_guid": "{C505}"}))
case("an association-end tag on a generalization", expect=[M("connector-end-tag")],
     edit=lambda r, x: r["t_taggedvalue"].append({"PropertyID": 1, "ElementID": "{C501}",
                                                  "BaseClass": "ASSOCIATION_SOURCE",
                                                  "TagValue": "position", "Notes": "1"}))

# ---------------------------------------------------------------------------------------
print("\nTagged values")
case("a valued tag outside the export's allow-list", expect=[M("attribute-tag")],
     contains="key = 'k_id'",
     edit=lambda r, x: r["t_attributetag"].append({"PropertyID": 1, "ElementID": 100,
                                                   "Property": "key", "VALUE": "k_id"}))
_, model = case("a tag declared without a value equals absence",
                edit=lambda r, x: r["t_attributetag"].append(
                    {"PropertyID": 1, "ElementID": 100, "Property": "use", "VALUE": ""}))
check(model.empty_tags[("attribute", "use")] == 1, "... and is counted")
case("a <memo> value is read from Notes",
     edit=lambda r, x: row(r, "t_objectproperties", PropertyID=1).update(Value="<memo>",
                                                                          Notes="sequence"))
case("an association tag", expect=[M("association-tag")],
     edit=lambda r, x: r["t_connectortag"].append({"PropertyID": 1, "ElementID": 500,
                                                   "Property": "position", "VALUE": "1"}))
case("a role tag belongs to the end its BaseClass names", expect=[M("end-tag")],
     contains="[Sas500]",
     edit=lambda r, x: r["t_taggedvalue"].append({"PropertyID": 1, "ElementID": "{C500}",
                                                  "BaseClass": "ASSOCIATION_SOURCE",
                                                  "TagValue": "position", "Notes": "2"}))

# ---------------------------------------------------------------------------------------
print("\nStereotypes are the union of the column and t_xref, keyed by what they describe")
case("a connector stereotype held only in t_connector.Stereotype",
     expect=[M("association-stereotype")], contains="transient",
     edit=lambda r, x: conn(r, 500).update(Stereotype="transient"))
case("the same stereotype, exported",
     edit=lambda r, x: (conn(r, 500).update(Stereotype="transient"),
                        add_stereotype(by_id(x, "as500"), "transient")))
case("an attribute stereotype held only in the column", expect=[M("attribute-stereotype")],
     edit=lambda r, x: attr(r, 100).update(Stereotype="XSDattribute"))
case("a t_xref row about a connector end belongs to that end", expect=[M("end-stereotype")],
     contains="[Sas500]",
     edit=lambda r, x: r["t_xref"].append({"Name": "Stereotypes", "Client": "{C500}",
                                           "Type": "connectorSrcEnd property",
                                           "Description": "@STEREO;Name=role;@ENDSTEREO;"}))

# ---------------------------------------------------------------------------------------
print("\nAttributes")
case("an attribute the export lacks", expect=[M("attribute")],
     edit=lambda r, x: r["t_attribute"].append({"Object_ID": 10, "ID": 105, "Name": "z",
                                                "Pos": 5, "ea_guid": "{A.z}"}))
case("an attribute name", expect=[D("attribute-name")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "name", "xx"))
case("an attribute carrying an end's inClassId", expect=[D("attribute-owner")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "inClassId", "11"))
case("a type bound by name when the classifier id is empty",
     edit=lambda r, x: (attr(r, 101).update(Classifier="0", Type="B"),
                        set_child(by_id(x, "10_101"), "typeName", "B"),
                        set_child(by_id(x, "10_101"), "typeId", "11")))
case("the derived by-name binding must be present", expect=[M("attribute-type")],
     edit=lambda r, x: (attr(r, 101).update(Classifier="0", Type="B"),
                        set_child(by_id(x, "10_101"), "typeName", "B")))
case("a typeId whose class does not carry the type's name", expect=[X("attribute-type")],
     edit=lambda r, x: set_child(by_id(x, "10_101"), "typeId", "11"))
case("a bound type's typeName is its class's name, not EA's cached Type",
     edit=lambda r, x: attr(r, 100).update(Type="Bee"))
case("an attribute type name", expect=[D("attribute-type-name")],
     edit=lambda r, x: set_child(by_id(x, "10_101"), "typeName", "str"))
case("0..1 exported as 1..1", expect=[D("attribute-multiplicity")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "cardinality", None))
case("empty bounds are UML's default 1..1",
     edit=lambda r, x: (attr(r, 100).update(LowerBound="", UpperBound=""),
                        set_child(by_id(x, "10_100"), "cardinality", None)))
case("an initial value", expect=[D("attribute-initial-value")],
     edit=lambda r, x: set_child(by_id(x, "10_101"), "initialValue", "bye"))
case("a read-only attribute", expect=[D("attribute-read-only")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "isReadOnly", "true"))
case("a derived attribute", expect=[D("attribute-derived")],
     edit=lambda r, x: attr(r, 100).update(Derived="1"))
case("an ordered enumeration literal is not silently made unordered",
     expect=[D("attribute-ordered")], edit=lambda r, x: attr(r, 102).update(IsOrdered=1))
case("an attribute that allows duplicates", expect=[D("attribute-unique")],
     edit=lambda r, x: attr(r, 100).update(AllowDuplicates=1))
case("containment by reference must be exported", expect=[M("attribute-containment")],
     edit=lambda r, x: attr(r, 100).update(Containment="By Reference"))
case("containment by reference exported lower-case, as ShapeChange writes it",
     edit=lambda r, x: (attr(r, 100).update(Containment="By Reference"),
                        set_child(by_id(x, "10_100"), "inlineOrByReference", "byreference")))
case("containment compared exactly, as ShapeChange's targets compare it",
     expect=[D("attribute-containment")],
     edit=lambda r, x: (attr(r, 100).update(Containment="By Reference"),
                        set_child(by_id(x, "10_100"), "inlineOrByReference", "byReference")))
case("the first inlineOrByReference tag value in EA's row order is the one used",
     edit=lambda r, x: (r["t_attributetag"].extend([
         {"PropertyID": 1, "ElementID": 100, "Property": "inlineOrByReference",
          "VALUE": "inline"},
         {"PropertyID": 2, "ElementID": 100, "Property": "inlineOrByReference",
          "VALUE": "byreference"}]),
         add_tag(by_id(x, "10_100"), "inlineOrByReference", "inline", "byreference"),
         set_child(by_id(x, "10_100"), "inlineOrByReference", "inline")))
case("the inlineOrByReference tag comes before EA's containment",
     edit=lambda r, x: (r["t_attributetag"].append({"PropertyID": 1, "ElementID": 100,
                                                    "Property": "inlineOrByReference",
                                                    "VALUE": "byReference"}),
                        add_tag(by_id(x, "10_100"), "inlineOrByReference", "byReference"),
                        set_child(by_id(x, "10_100"), "inlineOrByReference", "byreference")))
case("an attribute without the derived composition", expect=[D("attribute-composition")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "isComposition", None))
case("an attribute marked shared aggregation", expect=[D("attribute-aggregation")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "isAggregation", "true"))
case("an attribute marked owned", expect=[D("attribute-owned")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "isOwned", "true"))
case("a non-navigable attribute, which ShapeChange's reader drops",
     expect=[D("attribute-navigable")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "isNavigable", "false"))
case("attribute qualifiers", expect=[X("attribute-qualifiers")],
     edit=lambda r, x: [add(add(holder(by_id(x, "10_100"), "qualifiers"), "Qualifier"), t, v)
                        for t, v in (("name", "k"),)])
case("an enumeration literal outside an enumeration", expect=[D("attribute-literal")],
     edit=lambda r, x: attr(r, 100).update(StyleEx="IsLiteral=1;"))
_, model = case("a member of an enumeration without EA's IsLiteral is a literal, and counted",
                edit=lambda r, x: attr(r, 102).update(StyleEx=None))
check(sum(model.normalized.values()) == 1, "... the normalization is counted")
case("a private attribute", expect=[M("attribute-visibility")],
     edit=lambda r, x: attr(r, 100).update(Scope="Private"))
case("isID=1", expect=[M("attribute-unrepresentable")], contains="isID=1",
     edit=lambda r, x: r["t_xref"].append({"Name": "CustomProperties", "Client": "{A.x}",
                                           "Type": "attribute property", "Description":
                                           "@PROP=@NAME=isID@ENDNAME;@VALU=1@ENDVALU;@ENDPROP;"}))
case("isID=0 is unset",
     edit=lambda r, x: r["t_xref"].append({"Name": "CustomProperties", "Client": "{A.x}",
                                           "Type": "attribute property", "Description":
                                           "@PROP=@NAME=isID@ENDNAME;@VALU=0@ENDVALU;@ENDPROP;"}))
case("EA's union style on an attribute", expect=[M("attribute-unrepresentable")],
     contains="union=1", edit=lambda r, x: attr(r, 100).update(StyleEx="IsLiteral=0;union=1;"))
case("attribute documentation", expect=[M("attribute-documentation")],
     edit=lambda r, x: attr(r, 100).update(Notes="An x."))
case("an attribute definition without documentation", expect=[D("attribute-definition")],
     edit=lambda r, x: add_descriptor(by_id(x, "10_100"), "definition", "X."))
case("an attribute alias", expect=[M("attribute-alias")],
     edit=lambda r, x: attr(r, 100).update(Style="ax"))
case("a hyperlink in an attribute note", expect=[M("attribute-documentation-link")],
     edit=lambda r, x: (attr(r, 100).update(Notes='Per <a href="$inet://https://iso.org/x">x'
                                                  '</a>.'),
                        set_documentation(by_id(x, "10_100"), "Per x.")))
case("an attribute descriptor the model has no tag for", expect=[X("attribute-descriptor")],
     edit=lambda r, x: add_descriptor(by_id(x, "10_100"), "example", "3"))

# ---------------------------------------------------------------------------------------
print("\nAttribute order")
case("attributes exported against EA's Pos order", expect=[D("attribute-order")],
     edit=lambda r, x: set_child(by_id(x, "10_100"), "sequenceNumber", "-1073741800"))
case("attributes tied on Pos follow their names, as EA orders them",
     edit=lambda r, x: attr(r, 101).update(Pos=0))
case("attributes tied on Pos exported against name order", expect=[D("attribute-order")],
     edit=lambda r, x: (attr(r, 101).update(Pos=0),
                        set_child(by_id(x, "10_100"), "sequenceNumber", "-1073741800")))
case("a numeric sequenceNumber tag orders its attribute after the untagged ones",
     edit=lambda r, x: (r["t_attributetag"].append({"PropertyID": 1, "ElementID": 100,
                                                    "Property": "sequenceNumber",
                                                    "VALUE": "99"}),
                        add_tag(by_id(x, "10_100"), "sequenceNumber", "99"),
                        set_child(by_id(x, "10_100"), "sequenceNumber", "99")))
case("... and an export that orders it first is DIFFERENT", expect=[D("attribute-order")],
     edit=lambda r, x: (r["t_attributetag"].append({"PropertyID": 1, "ElementID": 100,
                                                    "Property": "sequenceNumber",
                                                    "VALUE": "99"}),
                        add_tag(by_id(x, "10_100"), "sequenceNumber", "99")))


def four_attributes(rows, root, numbers):
    rows["t_attribute"] += [
        {"Object_ID": 10, "ID": 103, "Name": "z", "Scope": "Public", "Pos": 2,
         "ea_guid": "{A.z}"},
        {"Object_ID": 10, "ID": 104, "Name": "w", "Scope": "Public", "Pos": 3,
         "ea_guid": "{A.w}"}]
    properties = by_id(root, "10").find(q("properties"))
    for name, pid in (("z", "10_103"), ("w", "10_104")):
        prop = add(properties, "Property")
        for tag, value in (("name", name), ("id", pid), ("sequenceNumber", "0"),
                           ("isComposition", "true")):
            add(prop, tag, value)
    for pid, number in zip(("10_100", "10_101", "10_103", "10_104"), numbers):
        set_child(by_id(root, pid), "sequenceNumber", str(number))


order_a, _ = case("every inverted pair is its own finding",
                  expect=[D("attribute-order")] * 3,
                  edit=lambda r, x: four_attributes(r, x, (4, 1, 2, 3)))
order_b, _ = case("... so a different wrong order has a different key set",
                  expect=[D("attribute-order")] * 3,
                  edit=lambda r, x: four_attributes(r, x, (2, 3, 4, 1)))
check({f.key for f in order_a} != {f.key for f in order_b},
      "two wrong orders never share one baseline key set")

# ---------------------------------------------------------------------------------------
print("\nAssociations")
case("an association the export lacks", expect=[M("association")],
     edit=lambda r, x: r["t_connector"].append({"Connector_ID": 506, "Start_Object_ID": 10,
                                                "Connector_Type": "Association",
                                                "End_Object_ID": 12, "ea_guid": "{C506}"}))
case("an association end that is no model element", expect=[D("association-endpoint"),
                                                           M("association")],
     edit=lambda r, x: r["t_connector"].append({"Connector_ID": 507, "Start_Object_ID": 999,
                                                "Connector_Type": "Association",
                                                "End_Object_ID": 11, "ea_guid": "{C507}"}))
case("an association name that is not the derived <source>_<target>",
     expect=[D("association-name")], edit=lambda r, x: set_child(by_id(x, "as500"), "name", "X"))
case("association notes", expect=[M("association-documentation")],
     edit=lambda r, x: conn(r, 500).update(Notes="An association."))
case("an association definition without documentation", expect=[D("association-definition")],
     edit=lambda r, x: add_descriptor(by_id(x, "as500"), "definition", "D."))
case("an association alias", expect=[M("association-alias")],
     edit=lambda r, x: conn(r, 500).update(StyleEx="alias=Link;"))
case("a hyperlink in association notes", expect=[M("association-documentation-link")],
     edit=lambda r, x: (conn(r, 500).update(Notes='See <a href="$inet://https://a.org">a</a>.'),
                        set_documentation(by_id(x, "as500"), "See a.")))
case("an association descriptor the model has no tag for",
     expect=[X("association-descriptor")],
     edit=lambda r, x: add_descriptor(by_id(x, "as500"), "example", "e"))
case("an association flag the SCXML cannot carry", expect=[M("association-unrepresentable")],
     edit=lambda r, x: conn(r, 500).update(IsSpec=1))

# ---------------------------------------------------------------------------------------
print("\nAssociation ends")


def move_role_to_b(rows, root):
    tas = by_id(root, "Tas500")
    parent_of(root, tas).remove(tas)
    holder(by_id(root, "11"), "properties").append(tas)


case("a role moved to another class", expect=[D("end-owner")], edit=move_role_to_b)
case("an inline end in the wrong class", expect=[D("end-owner")],
     edit=lambda r, x: set_child(by_id(x, "Sas500"), "inClassId", "10"))
case("an end whose id is not its association's", expect=[D("end-id")],
     edit=lambda r, x: set_child(by_id(x, "Sas500"), "id", "Xas500"))
case("an end naming another association", expect=[D("end-association-id")],
     edit=lambda r, x: set_child(by_id(x, "Sas500"), "associationId", "as501"))
case("an end whose type name is not its type's", expect=[D("end-type-name")],
     edit=lambda r, x: set_child(by_id(x, "Sas500"), "typeName", "B"))
case("a wrong synthesized role name", expect=[D("end-role")],
     edit=lambda r, x: set_child(by_id(x, "Sas500"), "name", "role_Tas500"))
case("an end multiplicity", expect=[D("end-multiplicity")],
     edit=lambda r, x: set_child(by_id(x, "Tas500"), "cardinality", "0..*"))
case("EA's diamond at the source end is the target property's composition",
     expect=[D("end-aggregation")],
     edit=lambda r, x: set_child(by_id(x, "Tas500"), "isComposition", None))
case("an end marked both composition and aggregation", expect=[D("end-aggregation")],
     contains="both",
     edit=lambda r, x: set_child(by_id(x, "Tas500"), "isAggregation", "true"))
case("an ordered end", expect=[D("end-ordered")],
     edit=lambda r, x: conn(r, 500).update(DestIsOrdered=1))
case("an end that allows duplicates", expect=[D("end-unique")],
     edit=lambda r, x: conn(r, 500).update(DestStyle="AllowDuplicates=1;Navigable=Navigable;"))
case("a derived end", expect=[D("end-derived")],
     edit=lambda r, x: conn(r, 500).update(DestStyle="Derived=1;Navigable=Navigable;"))
case("an owned end", expect=[D("end-owned")],
     edit=lambda r, x: conn(r, 500).update(DestStyle="Owned=1;Navigable=Navigable;"))
case("an owned end exported as owned",
     edit=lambda r, x: (conn(r, 500).update(DestStyle="Owned=1;Navigable=Navigable;"),
                        set_child(by_id(x, "Tas500"), "isOwned", "true")))
case("a frozen end", expect=[D("end-read-only")],
     edit=lambda r, x: conn(r, 500).update(DestChangeable="frozen"))
case("an end qualifier", expect=[M("end-qualifiers")],
     edit=lambda r, x: conn(r, 500).update(DestQualifier="key:string"))
case("an end contained by value (EA's end spelling)", expect=[M("end-containment")],
     edit=lambda r, x: conn(r, 500).update(DestContainment="Value"))
case("the same end, exported inline",
     edit=lambda r, x: (conn(r, 500).update(DestContainment="Value"),
                        set_child(by_id(x, "Tas500"), "inlineOrByReference", "inline")))
case("an end initial value", expect=[X("end-initial-value")],
     edit=lambda r, x: set_child(by_id(x, "Tas500"), "initialValue", "42"))
case("a private end", expect=[M("end-visibility")],
     edit=lambda r, x: conn(r, 500).update(DestAccess="Private"))
case("end notes", expect=[M("end-documentation")],
     edit=lambda r, x: conn(r, 500).update(DestRoleNote="The b."))
case("an end definition without documentation", expect=[D("end-definition")],
     edit=lambda r, x: add_descriptor(by_id(x, "Tas500"), "definition", "D."))
case("an end alias the model lacks", expect=[X("end-alias")],
     edit=lambda r, x: add_descriptor(by_id(x, "Tas500"), "alias", "bee"))
case("a hyperlink in an end note", expect=[M("end-documentation-link")],
     edit=lambda r, x: (conn(r, 500).update(DestRoleNote='Per <a href="$inet://https://r.org">'
                                                         'r</a>.'),
                        set_documentation(by_id(x, "Tas500"), "Per r.")))
case("an end descriptor the model has no tag for", expect=[X("end-descriptor")],
     edit=lambda r, x: add_descriptor(by_id(x, "Tas500"), "example", "e"))
case("a static end", expect=[M("end-unrepresentable")], contains="TS=static",
     edit=lambda r, x: conn(r, 500).update(DestTS="static"))
case("an add-only end", expect=[M("end-unrepresentable")], contains="Changeable=addOnly",
     edit=lambda r, x: conn(r, 500).update(DestChangeable="addOnly"))

# ---------------------------------------------------------------------------------------
print("\nNavigability: stated values survive, unstated ones follow ShapeChange's rule")
case("an unnamed end EA marks navigable, exported not navigable",
     expect=[D("end-navigability")], contains="unnamed",
     edit=lambda r, x: conn(r, 500).update(SourceStyle="Navigable=Navigable;"))
case("an end EA marks not navigable, exported navigable", expect=[D("end-navigability")],
     edit=lambda r, x: conn(r, 500).update(DestStyle="Navigable=Non-Navigable;"))
case("a bi-directional connector states both ends navigable",
     expect=[D("end-navigability")], contains="[Sas500]",
     edit=lambda r, x: conn(r, 500).update(Direction="Bi-Directional"))
case("an unspecified arrow end of a directed connector is navigable",
     edit=lambda r, x: conn(r, 500).update(DestStyle="Navigable=Unspecified;"))
case("an unspecified named end of an undirected connector derives navigable",
     edit=lambda r, x: conn(r, 500).update(Direction="Unspecified",
                                           DestStyle="Navigable=Unspecified;"))


def role_prefixed(rows, root):
    conn(rows, 500).update(Direction="Unspecified", DestRole="role_b",
                           DestStyle="Navigable=Unspecified;")
    navigable_end_inline(rows, root)
    tas = by_id(root, "Tas500")
    set_child(tas, "name", "role_b")
    set_child(tas, "isNavigable", "false")


case("a role named role_… is unnamed to ShapeChange, so not navigable", edit=role_prefixed)

# ---------------------------------------------------------------------------------------
print("\nConstraints and operations")
case("a constraint", expect=[M("constraint")],
     edit=lambda r, x: r["t_objectconstraint"].append(
         {"Object_ID": 10, "Constraint": "count(x) = 1", "ConstraintType": "Invariant",
          "Status": "Approved"}))
case("two constraints of one name on one owner are two findings",
     expect=[M("constraint"), M("constraint")],
     edit=lambda r, x: r["t_objectconstraint"].extend(
         [{"Object_ID": 10, "Constraint": "c", "ConstraintType": "Invariant"}] * 2))


def exported_constraint(root, owner, kind, **children):
    constraint = add(holder(by_id(root, owner), "constraints"), kind)
    for tag, value in children.items():
        add(constraint, tag, value)


case("a constraint's text is EA's rendering of its notes",
     edit=lambda r, x: (r["t_objectconstraint"].append(
         {"Object_ID": 10, "Constraint": "c", "Notes": "<b>Must</b> hold.",
          "ConstraintType": "Invariant", "Status": "Approved"}),
         exported_constraint(x, "10", "TextConstraint", name="c", status="Approved",
                             text="Must hold.", type="Invariant")))
case("a constraint's status is compared", expect=[D("constraint")], contains="status",
     edit=lambda r, x: (r["t_objectconstraint"].append(
         {"Object_ID": 10, "Constraint": "c", "Notes": "t", "ConstraintType": "Invariant",
          "Status": "Approved"}),
         exported_constraint(x, "10", "TextConstraint", name="c", status="Proposed", text="t",
                             type="Invariant")))
case("a constraint exported as the wrong kind", expect=[D("constraint-kind")],
     edit=lambda r, x: (r["t_objectconstraint"].append(
         {"Object_ID": 10, "Constraint": "c", "Notes": "t", "ConstraintType": "Invariant"}),
         exported_constraint(x, "10", "FolConstraint", name="c", text="t")))
case("an attribute constraint's status is written into its name",
     edit=lambda r, x: (r["t_attributeconstraints"].append(
         {"Object_ID": 10, "ID": 100, "Constraint": "type=virtual [Approved]", "Type": "OCL"}),
         exported_constraint(x, "10_100", "TextConstraint", name="type=virtual ",
                             status="Approved", type="OCL")))
case("constraint text is compared as written, a leading tab included",
     edit=lambda r, x: (r["t_objectconstraint"].append(
         {"Object_ID": 10, "Constraint": "c", "Notes": "<ul>\r\n\t<li>a</li>\r\n</ul>",
          "ConstraintType": "Invariant"}),
         exported_constraint(x, "10", "TextConstraint", name="c", text="\t- a",
                             type="Invariant")))
case("... so a trimmed text is DIFFERENT", expect=[D("constraint")],
     edit=lambda r, x: (r["t_objectconstraint"].append(
         {"Object_ID": 10, "Constraint": "c", "Notes": "<ul>\r\n\t<li>a</li>\r\n</ul>",
          "ConstraintType": "Invariant"}),
         exported_constraint(x, "10", "TextConstraint", name="c", text="- a",
                             type="Invariant")))
case("an attribute constraint's name is split as ShapeChange splits it",
     edit=lambda r, x: (r["t_attributeconstraints"].append(
         {"Object_ID": 10, "ID": 100, "Constraint": "type=virtual[Approved]x", "Type": "OCL"}),
         exported_constraint(x, "10_100", "TextConstraint", name="type=virtual",
                             status="Approved", type="OCL")))
case("an attribute constraint of type sbvr, in any case, is a FolConstraint",
     edit=lambda r, x: (r["t_attributeconstraints"].append(
         {"Object_ID": 10, "ID": 100, "Constraint": "c", "Type": "sbvr"}),
         exported_constraint(x, "10_100", "FolConstraint", name="c", sourceType="sbvr")))
case("a FolConstraint's sourceType is its EA type", expect=[D("constraint-kind")],
     edit=lambda r, x: (r["t_objectconstraint"].append(
         {"Object_ID": 10, "Constraint": "c", "ConstraintType": "SBVR"}),
         exported_constraint(x, "10", "FolConstraint", name="c", sourceType="OCL")))
case("an OclConstraint carries no type", expect=[D("constraint-kind")],
     edit=lambda r, x: (r["t_objectconstraint"].append(
         {"Object_ID": 10, "Constraint": "c", "ConstraintType": "OCL"}),
         exported_constraint(x, "10", "OclConstraint", name="c", type="OCL")))
case("a constraint the model lacks", expect=[X("constraint")], contains="text 'v'",
     edit=lambda r, x: exported_constraint(x, "10", "TextConstraint", name="c", text="v"))
case("an end constraint is a constraint", expect=[M("constraint")],
     edit=lambda r, x: conn(r, 500).update(DestConstraint="{ordered}"))
case("an operation", expect=[M("operation")],
     edit=lambda r, x: r["t_operation"].append({"OperationID": 1, "Object_ID": 10, "Name": "f"}))

# ---------------------------------------------------------------------------------------
print("\nNotation")
check(ea_txt("<ol>\r\n<li>one</li>\r\n<li>two</li>\r\n</ol>") == "\r\n1. one\r\n2. two",
      "an ordered list is numbered")
check(ea_txt("<ul>\r\n<li>a</li>\r\n</ul>\r\n") == "- a", "a CRLF after <ul>/</ul> is dropped")
check(ea_txt("a&nbsp;&lt;b&gt;&#178;\r\n\r\n") == "a<b>²",
      "entities decoded, nbsp removed, trailing CRLF stripped")
check(ea_txt("") is None and ea_txt(None) is None and ea_txt(" \t ") is None,
      "an empty or blank note has no rendering")
check(java_trim("  x  ") == " x ", "java_trim strips only up to U+0020")

# ---------------------------------------------------------------------------------------
print("\nGuards")
try:
    run(base_rows(), ET.fromstring(f'<sc:Model xmlns:sc="{SC}"><sc:packages/></sc:Model>'))
    check(False, "an export with no classes raises VacuousComparison")
except VacuousComparison:
    check(True, "an export with no classes raises VacuousComparison")

root = ET.fromstring(BASE_SCXML)
for element in root.iter():
    child = element.find(q("id"))
    if child is not None and child.text.isdigit():
        child.text = str(int(child.text) + 1000)
try:
    run(base_rows(), root)
    check(False, "two models that share no classifier id raise VacuousComparison")
except VacuousComparison:
    check(True, "two models that share no classifier id raise VacuousComparison")

with tempfile.TemporaryDirectory() as tmp:
    pointer = Path(tmp) / "m.qeax"
    pointer.write_text("version https://git-lfs.github.com/spec/v1\noid sha256:0\nsize 1\n")
    try:
        read_qeax(pointer)
        check(False, "a Git LFS pointer is rejected")
    except NotAnEaProject as error:
        check("git lfs pull" in str(error), "a Git LFS pointer is rejected with the fix named")

# ---------------------------------------------------------------------------------------
print("\nEvery rule has a negative case")
untested = sorted(RULES - EXERCISED)
check(not untested, f"every rule in RULES fired in a case (untested: {untested})")
check(not EXERCISED - RULES, "no case names a rule that RULES does not declare")

print()
if FAILURES:
    print(f"{len(FAILURES)} check(s) FAILED")
    sys.exit(1)
print(f"all checks passed ({len(RULES)} rules)")
