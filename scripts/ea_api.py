#!/usr/bin/env python3
"""The part of Enterprise Architect's automation interface that ASAM's schema generators read.

ASAM derives the normative XML Schema of a standard from its Enterprise Architect project with
a script that walks EA's object model: ``Repository.Models``, ``Package.Elements``,
``Element.Attributes``, ``Element.Connectors``, ``TaggedValues``, ``Stereotype`` and
``StereotypeEx``. This module offers that object model, read-only, over the two files this
repository holds. A generator ported to it can therefore run on either one, without Enterprise
Architect:

:func:`open_qeax`
    ASAM's project itself. A ``.qeax`` is an SQLite database, so each collection is the table
    EA reads it from, in the order EA returns it:

    - ``Package.Elements``: ``(TPos, Name)``, with an unset ``TPos`` read as 0. Only elements
      placed directly in the package are included; a nested element is not;
    - ``Package.Packages``: ``(TPos, Name)``;
    - ``Element.Attributes``: ``(Pos, Name)``;

    where ``Name`` compares as EA's schema declares the column, ``COLLATE NOCASE``: ASCII
    letters without regard to case, so ``Controller`` precedes ``ControlPoint``;
    - ``Element.Connectors``: every connector with the element at either end, by
      ``Connector_ID``;
    - ``TaggedValues``: by ``PropertyID``.

    ``Stereotype`` is the element's own column. ``StereotypeEx`` lists the element's
    ``t_xref`` ``Stereotypes`` entries, which is what EA's ``StereotypeEx`` returns. A stereotype
    held only by the column is therefore in ``Stereotype`` alone. EA's API behaves the same way,
    so a generator that tests both properties, as ASAM's does, sees what it sees in EA.

:func:`open_scxml`
    The committed SCXML export. The SCXML records a model, not an EA project, so the facade
    states what it assumes where the export has no counterpart:

    - every classifier is an EA ``Class``, since the export does not say which EA element type
      it came from;
    - the order within a package is by name, compared as EA compares it, since ``TPos`` is not
      exported;
    - ``Stereotype`` is the first of the exported stereotypes, and ``StereotypeEx`` is all of
      them, in export order;
    - an association end's cardinality is written ``lower..upper``, the form in which EA writes
      a range;
    - an end the exporter named ``role_<end id>`` is unnamed, as it is in EA;
    - a connector's tagged values are the association's own. Role tags, which the exporter
      writes on the end, are EA's ``ConnectorEnd.TaggedValues`` and not part of this subset;
    - a supertype is a generalization connector, numbered after every association in the order
      the export lists supertypes, since the export records no connector id for it;
    - a note is the exported documentation, which is already EA's plain-text rendering, so it
      is ``notes_text`` and ``notes`` is unset;
    - a package's stereotypes and tags are its ``Package.Element``'s.

    It reads the SCXML as written and validates nothing: ``check_model_equivalence.py`` is
    what decides that the file is well formed and the same model as the project.

What a generator run on the SCXML produces differently from the same generator run on the
``.qeax`` is exactly what the export lost of the information that generator reads. That is
the measurement this module exists for.
"""

from __future__ import annotations

import re
import sqlite3
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

from model_equivalence import ea_txt

SC = "http://shapechange.net/model"


@dataclass(frozen=True)
class TaggedValue:
    name: str
    value: str | None
    notes: str | None = None


@dataclass
class ConnectorEnd:
    role: str | None
    cardinality: str | None


@dataclass
class Connector:
    connector_id: int
    type: str
    client_id: int
    supplier_id: int
    stereotype: str | None
    stereotype_ex: tuple
    tagged_values: tuple
    client_end: ConnectorEnd
    supplier_end: ConnectorEnd
    notes: str | None = None


@dataclass
class Attribute:
    attribute_id: int
    name: str
    type: str | None
    lower_bound: str | None
    upper_bound: str | None
    stereotype: str | None
    stereotype_ex: tuple
    tagged_values: tuple
    default: str | None = None
    notes: str | None = None
    #: The notes as EA renders them as plain text (``GetFormatFromField("TXT", Notes)``).
    notes_text: str | None = None
    #: ``ClassifierID``: the element the type name refers to, or None when EA holds only the
    #: name.
    classifier_id: int | None = None


@dataclass(frozen=True)
class Constraint:
    """``Element.Constraints``: the name, type, status and notes of a constraint."""

    name: str
    type: str | None
    status: str | None
    notes: str | None


@dataclass
class Element:
    element_id: int
    type: str
    name: str | None
    stereotype: str | None
    stereotype_ex: tuple
    tagged_values: tuple
    attributes: tuple = ()
    connectors: tuple = ()
    package_id: int | None = None
    notes: str | None = None
    #: The notes as EA renders them as plain text (``GetFormatFromField("TXT", Notes)``).
    notes_text: str | None = None
    abstract: bool = False
    #: ``GenLinks``: EA's record of generalizations to classifiers it has no element for,
    #: e.g. ``Parent=double;``.
    gen_links: str | None = None
    constraints: tuple = ()
    #: ``Element.Elements``: elements nested in this one, ordered as ``Package.Elements``.
    elements: tuple = ()
    parent_id: int | None = None


@dataclass
class Package:
    package_id: int
    name: str
    elements: tuple = ()
    packages: tuple = ()
    #: ``Package.Element``: the package's own element, which holds its stereotypes and tags.
    element: Element | None = None


@dataclass
class Repository:
    """``Repository.Models`` and ``Repository.GetElementByID``."""

    models: tuple
    elements: dict = field(default_factory=dict)
    source: str = ""

    def get_element_by_id(self, element_id: int) -> Element:
        return self.elements[element_id]


_ASCII_UPPER = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")


def nocase(text: str | None) -> str:
    """SQLite's ``NOCASE`` collation, which folds ASCII letters only."""
    return (text or "").translate(_ASCII_UPPER)


def has_stereotype(item, name: str) -> bool:
    """ASAM's ``HasStereotype``: the ``Stereotype`` property, or an entry of ``StereotypeEx``."""
    if item.stereotype == name:
        return True
    return any(entry.strip() == name for entry in item.stereotype_ex)


def tagged_value(item, key: str) -> str | None:
    """ASAM's ``GetTaggedValue``: the value of the first tagged value named ``key``."""
    for tag in item.tagged_values:
        if tag.name == key:
            return tag.value
    return None


# ---------------------------------------------------------------------------------------
# The EA project


class NotAnEaProject(RuntimeError):
    """Raised when the ``.qeax`` is not an SQLite database, usually a Git LFS pointer."""


def _stereotype_names(description: str | None) -> list[str]:
    return re.findall(r"@STEREO;Name=([^;]*);", description or "")


def open_qeax(path: Path) -> Repository:
    """The EA object model of a ``.qeax``, as ASAM's generators see it through EA's API."""
    with open(path, "rb") as handle:
        if handle.read(16) != b"SQLite format 3\x00":
            raise NotAnEaProject(f"{path} is not an SQLite database; is it a Git LFS "
                                 "pointer? Run `git lfs pull`.")
    db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    try:
        return _read_qeax(db)
    finally:
        db.close()


def _read_qeax(db: sqlite3.Connection) -> Repository:
    xref: dict[str, list[str]] = {}
    for row in db.execute("SELECT Client, Description FROM t_xref WHERE Name = 'Stereotypes' "
                          "ORDER BY XrefID"):
        xref.setdefault(row["Client"], []).extend(_stereotype_names(row["Description"]))

    def tags(sql: str) -> dict[int, list[TaggedValue]]:
        found: dict[int, list[TaggedValue]] = {}
        for owner, name, value, notes in db.execute(sql):
            found.setdefault(owner, []).append(TaggedValue(name, value, notes))
        return found

    object_tags = tags("SELECT Object_ID, Property, Value, Notes FROM t_objectproperties "
                       "ORDER BY PropertyID")
    attribute_tags = tags("SELECT ElementID, Property, VALUE, NOTES FROM t_attributetag "
                          "ORDER BY PropertyID")
    connector_tags = tags("SELECT ElementID, Property, VALUE, NOTES FROM t_connectortag "
                          "ORDER BY PropertyID")

    attributes: dict[int, list[Attribute]] = {}
    rows = db.execute("SELECT * FROM t_attribute").fetchall()
    # (Pos, Name), with an unset Pos first as SQLite sorts NULL, and Name as NOCASE.
    rows.sort(key=lambda r: (r["Pos"] is not None, r["Pos"] or 0, nocase(r["Name"]), r["ID"]))
    for row in rows:
        attributes.setdefault(row["Object_ID"], []).append(Attribute(
            attribute_id=row["ID"],
            name=row["Name"],
            type=row["Type"],
            lower_bound=row["LowerBound"],
            upper_bound=row["UpperBound"],
            stereotype=row["Stereotype"],
            stereotype_ex=tuple(xref.get(row["ea_guid"], ())),
            tagged_values=tuple(attribute_tags.get(row["ID"], ())),
            default=row["Default"],
            notes=row["Notes"],
            notes_text=ea_txt(row["Notes"]),
            classifier_id=int(row["Classifier"]) if str(row["Classifier"] or "0") != "0" else None,
        ))

    connectors: dict[int, list[Connector]] = {}
    for row in db.execute("SELECT * FROM t_connector ORDER BY Connector_ID"):
        connector = Connector(
            connector_id=row["Connector_ID"],
            type=row["Connector_Type"],
            client_id=row["Start_Object_ID"],
            supplier_id=row["End_Object_ID"],
            stereotype=row["Stereotype"],
            stereotype_ex=tuple(xref.get(row["ea_guid"], ())),
            tagged_values=tuple(connector_tags.get(row["Connector_ID"], ())),
            client_end=ConnectorEnd(row["SourceRole"], row["SourceCard"]),
            supplier_end=ConnectorEnd(row["DestRole"], row["DestCard"]),
            notes=row["Notes"],
        )
        connectors.setdefault(connector.client_id, []).append(connector)
        if connector.supplier_id != connector.client_id:
            connectors.setdefault(connector.supplier_id, []).append(connector)
    for listed in connectors.values():
        listed.sort(key=lambda connector: connector.connector_id)

    constraints: dict[int, list[Constraint]] = {}
    for row in db.execute('SELECT Object_ID, "Constraint", ConstraintType, Status, Notes '
                          "FROM t_objectconstraint ORDER BY Object_ID, rowid"):
        constraints.setdefault(row[0], []).append(Constraint(row[1], row[2], row[3], row[4]))

    elements: dict[int, Element] = {}
    in_package: dict[int, list[tuple]] = {}
    nested: dict[int, list[tuple]] = {}
    by_guid: dict[str, Element] = {}
    for row in db.execute("SELECT * FROM t_object"):
        element = Element(
            element_id=row["Object_ID"],
            type=row["Object_Type"],
            name=row["Name"],
            stereotype=row["Stereotype"],
            stereotype_ex=tuple(xref.get(row["ea_guid"], ())),
            tagged_values=tuple(object_tags.get(row["Object_ID"], ())),
            attributes=tuple(attributes.get(row["Object_ID"], ())),
            connectors=tuple(connectors.get(row["Object_ID"], ())),
            package_id=row["Package_ID"],
            notes=row["Note"],
            notes_text=ea_txt(row["Note"]),
            abstract=str(row["Abstract"]) == "1",
            gen_links=row["GenLinks"],
            constraints=tuple(constraints.get(row["Object_ID"], ())),
            parent_id=row["ParentID"] or None,
        )
        elements[element.element_id] = element
        by_guid[row["ea_guid"]] = element
        order = ((row["TPos"] or 0, nocase(row["Name"]), row["Object_ID"]), element)
        if row["Object_Type"] == "Package":
            continue
        if row["ParentID"]:
            nested.setdefault(row["ParentID"], []).append(order)
        else:
            in_package.setdefault(row["Package_ID"], []).append(order)
    for parent_id, children in nested.items():
        if parent_id in elements:
            elements[parent_id].elements = tuple(e for _, e in sorted(children,
                                                                      key=lambda pair: pair[0]))

    package_rows = db.execute("SELECT * FROM t_package").fetchall()

    def package(row) -> Package:
        children = sorted((r for r in package_rows if r["Parent_ID"] == row["Package_ID"]),
                          key=lambda r: (r["TPos"] or 0, nocase(r["Name"]), r["Package_ID"]))
        return Package(
            package_id=row["Package_ID"],
            name=row["Name"],
            elements=tuple(e for _, e in sorted(in_package.get(row["Package_ID"], ()),
                                                key=lambda pair: pair[0])),
            packages=tuple(package(child) for child in children),
            element=by_guid.get(row["ea_guid"]),
        )

    roots = sorted((r for r in package_rows if not r["Parent_ID"]),
                   key=lambda r: (r["TPos"] or 0, nocase(r["Name"]), r["Package_ID"]))
    return Repository(models=tuple(package(r) for r in roots), elements=elements, source="qeax")


# ---------------------------------------------------------------------------------------
# The SCXML export


def _q(tag: str) -> str:
    return f"{{{SC}}}{tag}"


def _text(element: ET.Element, tag: str) -> str | None:
    child = element.find(_q(tag))
    return None if child is None else (child.text or "")


def _strings(element: ET.Element, container: str) -> tuple:
    holder = element.find(_q(container))
    return () if holder is None else tuple((item.text or "") for item in holder)


def _documentation(element: ET.Element) -> str | None:
    """The exported documentation descriptor: EA's plain-text rendering of the notes."""
    holder = element.find(f"{_q('descriptors')}/{_q('documentation')}/{_q('descriptorValues')}")
    values = [] if holder is None else [(v.text or "") for v in holder]
    return values[0] if values else None


def _scxml_tags(element: ET.Element) -> tuple:
    found = []
    holder = element.find(_q("taggedValues"))
    for tag in holder if holder is not None else ():
        name = _text(tag, "name") or ""
        for value in _strings(tag, "values") or ("",):
            found.append(TaggedValue(name, value))
    return tuple(found)


def _bounds(cardinality: str | None) -> tuple[str, str]:
    """ShapeChange's cardinality text as EA's two bounds; an empty one is UML's 1..1."""
    text = (cardinality or "").strip()
    if not text:
        return "1", "1"
    if text == "*":
        return "0", "*"
    if ".." in text:
        low, high = text.split("..", 1)
        return low.strip(), high.strip()
    return text, text


def _numeric_id(text: str | None, prefix: str = "") -> int:
    value = (text or "")[len(prefix):] if (text or "").startswith(prefix) else (text or "")
    return int(value)


def open_scxml(path: Path) -> Repository:
    """The EA object model as the SCXML export records it. See the module docstring."""
    root = ET.parse(path).getroot()
    elements: dict[int, Element] = {}
    attributes: dict[int, list[tuple]] = {}
    properties: dict[str, ET.Element] = {}
    supertypes: dict[int, list[int]] = {}

    def read_package(element: ET.Element) -> Package:
        pid = _numeric_id(_text(element, "id"), "P")
        members = [read_class(cls, pid) for cls in _direct_classes(element)]
        subs = [read_package(p) for p in _direct_packages(element)]
        stereotypes = _strings(element, "stereotypes")
        own = Element(
            element_id=-pid,
            type="Package",
            name=_text(element, "name"),
            stereotype=stereotypes[0] if stereotypes else None,
            stereotype_ex=stereotypes,
            tagged_values=_scxml_tags(element),
            package_id=pid,
            notes_text=_documentation(element),
        )
        return Package(
            package_id=pid,
            name=_text(element, "name") or "",
            elements=tuple(sorted(members, key=lambda e: (nocase(e.name), e.element_id))),
            packages=tuple(sorted(subs, key=lambda p: (nocase(p.name), p.package_id))),
            element=own,
        )

    def read_class(cls: ET.Element, pid: int) -> Element:
        cid = _numeric_id(_text(cls, "id"))
        stereotypes = _strings(cls, "stereotypes")
        holder = cls.find(_q("properties"))
        for prop in holder if holder is not None else ():
            properties[_text(prop, "id") or ""] = prop
            if (_text(prop, "isAttribute") or "true").strip().lower() in ("true", "1"):
                low, high = _bounds(_text(prop, "cardinality"))
                prop_stereotypes = _strings(prop, "stereotypes")
                attributes.setdefault(cid, []).append((
                    tuple(int(p) for p in (_text(prop, "sequenceNumber") or "0").split(".")),
                    Attribute(
                        attribute_id=_numeric_id((_text(prop, "id") or "").split("_")[-1]),
                        name=_text(prop, "name") or "",
                        type=_text(prop, "typeName"),
                        lower_bound=low,
                        upper_bound=high,
                        stereotype=prop_stereotypes[0] if prop_stereotypes else None,
                        stereotype_ex=prop_stereotypes,
                        tagged_values=_scxml_tags(prop),
                        default=_text(prop, "initialValue"),
                        notes_text=_documentation(prop),
                        classifier_id=int(_text(prop, "typeId")) if (_text(prop, "typeId") or "")
                        .isdigit() else None,
                    ),
                ))
        supertypes[cid] = [_numeric_id(t) for t in _strings(cls, "supertypes")]
        element = Element(
            element_id=cid,
            type="Class",
            name=_text(cls, "name"),
            stereotype=stereotypes[0] if stereotypes else None,
            stereotype_ex=stereotypes,
            tagged_values=_scxml_tags(cls),
            package_id=pid,
            notes_text=_documentation(cls),
            abstract=(_text(cls, "isAbstract") or "").strip().lower() in ("true", "1"),
        )
        elements[cid] = element
        return element

    packages_holder = root.find(_q("packages"))
    top = tuple(read_package(p) for p in (packages_holder if packages_holder is not None else ()))

    connectors: dict[int, list[Connector]] = {}
    holder = root.find(_q("associations"))
    for association in holder if holder is not None else ():
        aid = _text(association, "id") or ""
        ends = {}
        for tag in ("end1", "end2"):
            end = association.find(_q(tag))
            if end is None:
                continue
            ref = end.get("ref")
            prop = properties.get(ref) if ref else end.find(_q("Property"))
            if prop is not None:
                ends[(_text(prop, "id") or "")[:1]] = prop
        client, supplier = ends.get("S"), ends.get("T")
        if client is None or supplier is None:
            continue
        stereotypes = _strings(association, "stereotypes")
        low, high = _bounds(_text(supplier, "cardinality"))
        source_low, source_high = _bounds(_text(client, "cardinality"))
        connector = Connector(
            connector_id=_numeric_id(aid, "as"),
            type="Association",
            client_id=_numeric_id(_text(client, "typeId")),
            supplier_id=_numeric_id(_text(supplier, "typeId")),
            stereotype=stereotypes[0] if stereotypes else None,
            stereotype_ex=stereotypes,
            tagged_values=_scxml_tags(association),
            client_end=ConnectorEnd(_role(client), f"{source_low}..{source_high}"),
            supplier_end=ConnectorEnd(_role(supplier), f"{low}..{high}"),
        )
        connectors.setdefault(connector.client_id, []).append(connector)
        if connector.supplier_id != connector.client_id:
            connectors.setdefault(connector.supplier_id, []).append(connector)

    # A supertype is a generalization. The export records no connector for it, so it is
    # numbered after every association, in the order the supertypes are listed.
    next_id = max((c.connector_id for listed in connectors.values() for c in listed), default=0)
    for cid, supers in supertypes.items():
        for super_id in supers:
            next_id += 1
            connector = Connector(
                connector_id=next_id,
                type="Generalization",
                client_id=cid,
                supplier_id=super_id,
                stereotype=None,
                stereotype_ex=(),
                tagged_values=(),
                client_end=ConnectorEnd(None, None),
                supplier_end=ConnectorEnd(None, None),
            )
            connectors.setdefault(cid, []).append(connector)
            connectors.setdefault(super_id, []).append(connector)

    for cid, element in elements.items():
        element.attributes = tuple(a for _, a in sorted(attributes.get(cid, ()),
                                                        key=lambda pair: pair[0]))
        element.connectors = tuple(sorted(connectors.get(cid, ()),
                                          key=lambda connector: connector.connector_id))
    return Repository(models=top, elements=elements, source="scxml")


def _role(end: ET.Element) -> str | None:
    """An end's role name; the exporter names an unnamed end ``role_<end id>``."""
    name = _text(end, "name") or ""
    return None if name in ("", f"role_{_text(end, 'id')}") else name


def _direct_classes(package: ET.Element) -> list[ET.Element]:
    holder = package.find(_q("classes"))
    return [] if holder is None else [c for c in holder if c.tag == _q("Class")]


def _direct_packages(package: ET.Element) -> list[ET.Element]:
    holder = package.find(_q("packages"))
    return [] if holder is None else [p for p in holder if p.tag == _q("Package")]
