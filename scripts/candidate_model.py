#!/usr/bin/env python3
"""A candidate model: ASAM's released model plus a declared list of changes.

The SCXML of a released version is the export of ASAM's EA project and stays exactly that
(AGENTS.md, rule 7). A change to the *modelling* is published separately, as a candidate for a
future version, in ``standards/<std>/candidates/<version>/``:

``changes.json``
    The candidate's name, the release it is based on, and its changes. Each change has an id,
    a title, the reason for it, what it does to the normative schema, and the operations that
    carry it out. It is the only file a person edits.
``<artifact>.scxml``
    The candidate model: the release SCXML with every operation applied, written as
    ShapeChange's ``ModelExport`` writes a model, so that its diff against the release shows
    the changes and nothing else.
``CHANGELOG.md``
    The changes, rendered from ``changes.json`` with the names of the elements they touch.

Both written files are produced by this module and checked to be up to date, so the candidate
differs from the release by exactly its changelog.

Every operation addresses the model by EA id, which the export carries over (``as<n>`` for
connector *n*, ``<class>_<n>`` for attribute *n*), and every operation is applied twice: to the
SCXML, and to a copy of ASAM's ``.qeax``. An operation marked ``"export": false`` addresses an
element the release export does not carry, such as a classifier nested in another, and is
applied to the project only; the SCXML is checked to lack the element. The copy is never
committed. It exists so that the candidate can be checked the way the release is:

- ``check_model_equivalence.py``'s comparison of the two must find nothing the release does not
  already have, which shows that each operation changes both representations alike;
- ``check_xsd_transformation.py``'s derivation, run on it, shows what the candidate does to
  the normative schema.

Operations
----------
``set-multiplicity``  ``attribute``, ``lower``, ``upper``
``set-tag``           ``package`` | ``class`` | ``attribute`` | ``connector``, ``name``,
                      ``value``
``remove-tag``        ``package`` | ``class`` | ``attribute`` | ``connector``, ``name``
``set-stereotypes``   ``class`` | ``attribute`` | ``connector``, ``stereotypes``
``set-end-tag``       ``connector``, ``name``, ``value``: a tag of the connector's target end
``set-role``          ``connector``, ``role``: the role of the connector's target end, which is
                      then navigable
``set-classifier``    ``attribute``, ``classifier``: the class the attribute's type refers to
``remove-connector``  ``connector``
"""

from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import sys
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

SC = "http://shapechange.net/model"
OPERATIONS = ("set-multiplicity", "set-tag", "remove-tag", "set-stereotypes", "set-end-tag",
              "set-role", "set-classifier", "remove-connector")
ELEMENT_KINDS = ("package", "class", "attribute", "connector")

#: Stereotypes ShapeChange writes in lower case, as it normalizes its well-known ones.
WELL_KNOWN = frozenset({"union", "enumeration", "datatype", "codelist", "featuretype", "type",
                        "interface", "basictype", "adeelement", "application schema", "schema"})

#: The order in which ShapeChange's ModelWriter writes the children of a class and a property.
CLASS_ORDER = ("name", "id", "stereotypes", "descriptors", "taggedValues", "profiles",
               "constraints", "isAbstract", "isLeaf", "associationId", "linkedDocument",
               "supertypes", "subtypes", "properties")
PROPERTY_ORDER = ("name", "id", "stereotypes", "descriptors", "taggedValues", "profiles",
                  "constraints", "cardinality", "isNavigable", "sequenceNumber", "typeId",
                  "typeName", "isDerived", "isReadOnly", "isAttribute", "isOrdered", "isUnique",
                  "isComposition", "isAggregation", "isOwned", "initialValue",
                  "inlineOrByReference", "qualifiers", "inClassId", "associationId")
PACKAGE_ORDER = ("name", "id", "stereotypes", "descriptors", "taggedValues", "profiles",
                 "supplierIds", "classes", "packages")
ASSOCIATION_ORDER = ("name", "id", "stereotypes", "descriptors", "taggedValues", "profiles",
                     "constraints", "assocClassId", "end1", "end2")


class CandidateError(ValueError):
    """A change set that cannot be applied as written."""


def q(tag: str) -> str:
    return f"{{{SC}}}{tag}"


def _local(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


# ---------------------------------------------------------------------------------------
# Writing SCXML as ShapeChange does


def _escape(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace("\r", "&#xD;").replace("\n", "&#xA;"))


def _name(tag: str) -> str:
    namespace, local = tag[1:].split("}")
    return ("sc:" if namespace == SC else "xsi:") + local


def serialize(root: ET.Element, header: str, root_start: str) -> str:
    """ShapeChange's ModelExport layout: two-space indentation, a leaf on one line, CR and LF
    in text as character references, and no line break after the root."""
    out = [header]

    def write(element: ET.Element, level: int, start: str | None = None) -> None:
        pad = "  " * level
        if start is None:
            attributes = "".join(f' {_name(k) if k.startswith("{") else k}="'
                                 f'{_escape(v).replace(chr(34), "&quot;")}"'
                                 for k, v in element.attrib.items())
            start = f"<{_name(element.tag)}{attributes}>"
        children = list(element)
        if children:
            out.append(f"{pad}{start}\n")
            for child in children:
                write(child, level + 1)
            out.append(f"{pad}</{_name(element.tag)}>\n")
        else:
            out.append(f"{pad}{start}{_escape(element.text or '')}</{_name(element.tag)}>\n")

    write(root, 0, root_start)
    return "".join(out).rstrip("\n")


def read_scxml(path: Path) -> tuple[ET.Element, str, str]:
    raw = path.read_text(encoding="utf-8")
    header = raw[: raw.index("\n") + 1]
    start = raw.index("<sc:Model")
    root_start = raw[start: raw.index(">", start) + 1]
    return ET.fromstring(raw.encode("utf-8")), header, root_start


# ---------------------------------------------------------------------------------------
# The change set


def load_changes(path: Path) -> dict:
    changes = json.loads(path.read_text())
    for key in ("name", "based_on", "changes"):
        if key not in changes:
            raise CandidateError(f"{path} has no {key!r}")
    seen = set()
    for change in changes["changes"]:
        for key in ("id", "title", "why", "schema", "operations"):
            if key not in change:
                raise CandidateError(f"change {change.get('id')!r} has no {key!r}")
        if change["id"] in seen:
            raise CandidateError(f"change id {change['id']!r} is used twice")
        seen.add(change["id"])
        for operation in change["operations"]:
            if operation.get("op") not in OPERATIONS:
                raise CandidateError(f"change {change['id']}: unknown operation "
                                     f"{operation.get('op')!r}")
    return changes


def target_of(operation: dict) -> tuple[str, int]:
    kinds = [k for k in ELEMENT_KINDS if k in operation]
    if len(kinds) != 1:
        raise CandidateError(f"operation {operation} must name exactly one of {ELEMENT_KINDS}")
    return kinds[0], int(operation[kinds[0]])


# ---------------------------------------------------------------------------------------
# Applying it to the SCXML


class _Scxml:
    def __init__(self, root: ET.Element) -> None:
        self.root = root
        self.classes = {c.findtext(q("id")): c for c in root.iter(q("Class"))}
        self.packages = {p.findtext(q("id")): p for p in root.iter(q("Package"))}
        self.associations = {a.findtext(q("id")): a for a in root.iter(q("Association"))}
        self.properties: dict[str, ET.Element] = {}
        self.parent: dict[ET.Element, ET.Element] = {}
        for element in root.iter():
            for child in element:
                self.parent[child] = element
            if element.tag == q("Property"):
                self.properties[element.findtext(q("id"))] = element

    def element(self, kind: str, eid: int) -> ET.Element:
        if kind == "class":
            found = self.classes.get(str(eid))
        elif kind == "package":
            found = self.packages.get(f"P{eid}")
        elif kind == "connector":
            found = self.associations.get(f"as{eid}")
        else:
            found = next((p for pid, p in self.properties.items()
                          if pid.endswith(f"_{eid}") and "_" in pid), None)
        if found is None:
            raise CandidateError(f"the SCXML has no {kind} {eid}")
        return found

    @staticmethod
    def place(element: ET.Element, child: ET.Element, order: tuple) -> None:
        """Insert ``child`` where ShapeChange's writer puts an element of its kind."""
        rank = order.index(_local(child))
        for index, existing in enumerate(list(element)):
            if order.index(_local(existing)) > rank:
                element.insert(index, child)
                return
        element.append(child)

    @staticmethod
    def order_of(element: ET.Element) -> tuple:
        return {"Class": CLASS_ORDER, "Property": PROPERTY_ORDER, "Package": PACKAGE_ORDER,
                "Association": ASSOCIATION_ORDER}[_local(element)]

    def set_text(self, element: ET.Element, tag: str, text: str | None) -> None:
        existing = element.find(q(tag))
        if text is None:
            if existing is not None:
                element.remove(existing)
            return
        if existing is None:
            existing = ET.Element(q(tag))
            self.place(element, existing, self.order_of(element))
        existing.text = text

    def set_tag(self, element: ET.Element, name: str, value: str | None) -> None:
        holder = element.find(q("taggedValues"))
        if holder is None:
            if value is None:
                return
            holder = ET.Element(q("taggedValues"))
            self.place(element, holder, self.order_of(element))
        for tag in list(holder):
            if tag.findtext(q("name")) == name:
                holder.remove(tag)
        if value is not None:
            tag = ET.Element(q("TaggedValue"))
            ET.SubElement(tag, q("name")).text = name
            ET.SubElement(ET.SubElement(tag, q("values")), q("Value")).text = value
            names = [t.findtext(q("name")) for t in holder]
            index = sum(1 for n in names if n < name)
            holder.insert(index, tag)
        if not len(holder):
            element.remove(holder)

    def set_stereotypes(self, element: ET.Element, stereotypes: list[str]) -> None:
        holder = element.find(q("stereotypes"))
        if holder is not None:
            element.remove(holder)
        if stereotypes:
            holder = ET.Element(q("stereotypes"))
            for name in stereotypes:
                ET.SubElement(holder, q("Stereotype")).text = (
                    name.lower() if name.lower() in WELL_KNOWN else name)
            self.place(element, holder, self.order_of(element))

    def target_end(self, cid: int) -> ET.Element:
        end = self.properties.get(f"Tas{cid}")
        if end is None:
            raise CandidateError(f"the SCXML has no target end of connector {cid}")
        return end

    def set_role(self, cid: int, role: str) -> None:
        """Name the target end. A named end is navigable, and ShapeChange writes a navigable end
        as a property of its class, ordered by sequence number, rather than inline."""
        end = self.target_end(cid)
        association = self.element("connector", cid)
        end.find(q("name")).text = role
        if end.findtext(q("isNavigable")) != "false":
            return
        self.set_text(end, "isNavigable", None)
        owner_id = end.findtext(q("inClassId"))
        self.set_text(end, "inClassId", None)
        holder = self.parent[end]
        holder.remove(end)
        holder.attrib["ref"] = f"Tas{cid}"
        owner = self.classes[owner_id]
        properties = owner.find(q("properties"))
        if properties is None:
            properties = ET.Element(q("properties"))
            self.place(owner, properties, CLASS_ORDER)
        number = _sequence(end)
        index = sum(1 for p in properties if _sequence(p) < number)
        properties.insert(index, end)
        self.parent[end] = properties
        del association  # the association keeps its end by reference

    def remove_connector(self, cid: int) -> None:
        association = self.element("connector", cid)
        for end_id in (f"Sas{cid}", f"Tas{cid}"):
            end = self.properties.pop(end_id, None)
            if end is not None and self.parent.get(end) is not None:
                holder = self.parent[end]
                holder.remove(end)
                if _local(holder) == "properties" and not len(holder):
                    self.parent[holder].remove(holder)
        self.parent[association].remove(association)
        del self.associations[f"as{cid}"]


def _sequence(prop: ET.Element) -> tuple:
    return tuple(int(p) for p in (prop.findtext(q("sequenceNumber")) or "0").split("."))


def _cardinality(lower: str, upper: str) -> str | None:
    """ShapeChange's ``Multiplicity.toString``, which is not written for 1..1."""
    if lower == upper == "1":
        return None
    return lower if lower == upper else f"{lower}..{upper}"


def apply_to_scxml(root: ET.Element, changes: dict) -> None:
    model = _Scxml(root)
    for change in changes["changes"]:
        for operation in change["operations"]:
            op = operation["op"]
            if operation.get("export") is False:
                # The target is an element the release export does not carry, such as a
                # classifier nested in another; the operation changes the EA project only,
                # and the SCXML must indeed lack it.
                kind, eid = target_of(operation)
                try:
                    model.element(kind, eid)
                except CandidateError:
                    continue
                raise CandidateError(f"operation {operation} is marked export: false, but the "
                                     f"SCXML has {kind} {eid}")
            if op == "set-multiplicity":
                prop = model.element("attribute", int(operation["attribute"]))
                model.set_text(prop, "cardinality",
                               _cardinality(str(operation["lower"]), str(operation["upper"])))
            elif op in ("set-tag", "remove-tag"):
                kind, eid = target_of(operation)
                model.set_tag(model.element(kind, eid), operation["name"],
                              operation.get("value") if op == "set-tag" else None)
            elif op == "set-stereotypes":
                kind, eid = target_of(operation)
                model.set_stereotypes(model.element(kind, eid), operation["stereotypes"])
            elif op == "set-end-tag":
                model.set_tag(model.target_end(int(operation["connector"])), operation["name"],
                              operation["value"])
            elif op == "set-role":
                model.set_role(int(operation["connector"]), operation["role"])
            elif op == "set-classifier":
                prop = model.element("attribute", int(operation["attribute"]))
                classifier = str(operation["classifier"])
                if classifier not in model.classes:
                    raise CandidateError(f"no class {classifier} for attribute "
                                         f"{operation['attribute']}")
                model.set_text(prop, "typeId", classifier)
                model.set_text(prop, "typeName", model.classes[classifier].findtext(q("name")))
            elif op == "remove-connector":
                model.remove_connector(int(operation["connector"]))


# ---------------------------------------------------------------------------------------
# Applying it to a copy of the EA project

_XREF_TYPE = {"class": "element property", "attribute": "attribute property",
              "connector": "connector property", "package": "element property"}
_TAG_TABLE = {"package": ("t_objectproperties", "Object_ID", "Value", "Notes"),
              "class": ("t_objectproperties", "Object_ID", "Value", "Notes"),
              "attribute": ("t_attributetag", "ElementID", "VALUE", "NOTES"),
              "connector": ("t_connectortag", "ElementID", "VALUE", "NOTES")}
_ELEMENT_TABLE = {"class": ("t_object", "Object_ID"), "attribute": ("t_attribute", "ID"),
                  "connector": ("t_connector", "Connector_ID")}


def _package_object(db: sqlite3.Connection, package_id: int) -> int:
    """The ``t_object`` row of a package, which holds its tags and stereotypes."""
    row = db.execute("SELECT o.Object_ID FROM t_package p JOIN t_object o ON o.ea_guid = p.ea_guid"
                     " WHERE p.Package_ID = ?", (package_id,)).fetchone()
    if row is None:
        raise CandidateError(f"the EA project has no package {package_id}")
    return row[0]


def _guid(db: sqlite3.Connection, kind: str, eid: int) -> str:
    if kind == "package":
        kind, eid = "class", _package_object(db, eid)
    table, key = _ELEMENT_TABLE[kind]
    row = db.execute(f"SELECT ea_guid FROM {table} WHERE {key} = ?", (eid,)).fetchone()
    if row is None:
        raise CandidateError(f"the EA project has no {kind} {eid}")
    return row[0]


def _new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


def apply_to_qeax(source: Path, target: Path, changes: dict) -> None:
    shutil.copyfile(source, target)
    db = sqlite3.connect(target)
    try:
        for change in changes["changes"]:
            for operation in change["operations"]:
                _apply_qeax(db, operation)
        db.commit()
    finally:
        db.close()


def _apply_qeax(db: sqlite3.Connection, operation: dict) -> None:
    op = operation["op"]
    if op == "set-multiplicity":
        eid = int(operation["attribute"])
        _guid(db, "attribute", eid)
        db.execute("UPDATE t_attribute SET LowerBound = ?, UpperBound = ? WHERE ID = ?",
                   (str(operation["lower"]), str(operation["upper"]), eid))
    elif op in ("set-tag", "remove-tag"):
        kind, eid = target_of(operation)
        _guid(db, kind, eid)
        if kind == "package":
            eid = _package_object(db, eid)
        table, owner, value_column, notes_column = _TAG_TABLE[kind]
        db.execute(f"DELETE FROM {table} WHERE {owner} = ? AND Property = ?",
                   (eid, operation["name"]))
        if op == "set-tag":
            next_id = db.execute(f"SELECT COALESCE(MAX(PropertyID), 0) + 1 FROM {table}"
                                 ).fetchone()[0]
            db.execute(f"INSERT INTO {table} (PropertyID, {owner}, Property, {value_column}, "
                       f"{notes_column}, ea_guid) VALUES (?, ?, ?, ?, NULL, ?)",
                       (next_id, eid, operation["name"], operation["value"], _new_guid()))
    elif op == "set-stereotypes":
        kind, eid = target_of(operation)
        guid = _guid(db, kind, eid)
        if kind == "package":
            kind, eid = "class", _package_object(db, eid)
        table, key = _ELEMENT_TABLE[kind]
        names = operation["stereotypes"]
        db.execute(f"UPDATE {table} SET Stereotype = ? WHERE {key} = ?",
                   (names[0] if names else None, eid))
        db.execute("DELETE FROM t_xref WHERE Client = ? AND Name = 'Stereotypes'", (guid,))
        if names:
            description = "".join(f"@STEREO;Name={n};@ENDSTEREO;" for n in names)
            db.execute("INSERT INTO t_xref (XrefID, Name, Type, Visibility, Partition, "
                       "Description, Client, Supplier) VALUES (?, 'Stereotypes', ?, 'Public', "
                       "'0', ?, ?, '<none>')", (_new_guid(), _XREF_TYPE[kind], description, guid))
    elif op == "set-end-tag":
        # A role tag: EA keys it by the connector's GUID and the end, with the value in Notes.
        guid = _guid(db, "connector", int(operation["connector"]))
        db.execute("DELETE FROM t_taggedvalue WHERE ElementID = ? AND BaseClass = "
                   "'ASSOCIATION_TARGET' AND TagValue = ?", (guid, operation["name"]))
        db.execute("INSERT INTO t_taggedvalue (PropertyID, ElementID, BaseClass, TagValue, Notes) "
                   "VALUES (?, ?, 'ASSOCIATION_TARGET', ?, ?)",
                   (_new_guid(), guid, operation["name"], operation["value"]))
    elif op == "set-role":
        # A named end is a property of the class at the other end, so it is navigable: the
        # style says so explicitly, whatever it said before.
        eid = int(operation["connector"])
        _guid(db, "connector", eid)
        style = db.execute("SELECT DestStyle FROM t_connector WHERE Connector_ID = ?",
                           (eid,)).fetchone()[0] or ""
        parts = [p for p in style.split(";") if p and not p.startswith("Navigable=")]
        style = ";".join(parts + ["Navigable=Navigable"]) + ";"
        db.execute("UPDATE t_connector SET DestRole = ?, DestStyle = ? WHERE Connector_ID = ?",
                   (operation["role"], style, eid))
    elif op == "set-classifier":
        eid = int(operation["attribute"])
        _guid(db, "attribute", eid)
        _guid(db, "class", int(operation["classifier"]))
        db.execute("UPDATE t_attribute SET Classifier = ? WHERE ID = ?",
                   (str(operation["classifier"]), eid))
    elif op == "remove-connector":
        eid = int(operation["connector"])
        guid = _guid(db, "connector", eid)
        db.execute("DELETE FROM t_connectortag WHERE ElementID = ?", (eid,))
        db.execute("DELETE FROM t_xref WHERE Client = ?", (guid,))
        db.execute("DELETE FROM t_taggedvalue WHERE ElementID = ?", (guid,))
        db.execute("DELETE FROM t_diagramlinks WHERE ConnectorID = ?", (eid,))
        db.execute("DELETE FROM t_connector WHERE Connector_ID = ?", (eid,))


# ---------------------------------------------------------------------------------------
# The changelog


def describe(operation: dict, names: dict) -> str:
    """One line naming what an operation does, with the names of the elements it touches."""
    text = _describe(operation, names)
    return text + " (not in the export)" if operation.get("export") is False else text


def _describe(operation: dict, names: dict) -> str:
    op = operation["op"]

    def label(kind: str, eid) -> str:
        return f"{names.get((kind, int(eid)), '?')} ({kind} {eid})"

    if op == "set-multiplicity":
        return (f"multiplicity of {label('attribute', operation['attribute'])} := "
                f"{operation['lower']}..{operation['upper']}")
    if op == "set-tag":
        kind, eid = target_of(operation)
        return f"tag {operation['name']} = {operation['value']!r} on {label(kind, eid)}"
    if op == "remove-tag":
        kind, eid = target_of(operation)
        return f"tag {operation['name']} removed from {label(kind, eid)}"
    if op == "set-stereotypes":
        kind, eid = target_of(operation)
        shown = ", ".join(f"«{s}»" for s in operation["stereotypes"]) or "none"
        return f"stereotypes of {label(kind, eid)} := {shown}"
    if op == "set-end-tag":
        return (f"tag {operation['name']} = {operation['value']!r} on the target end of "
                f"{label('connector', operation['connector'])}")
    if op == "set-role":
        return (f"target role of {label('connector', operation['connector'])} := "
                f"{operation['role']!r}, navigable")
    if op == "set-classifier":
        return (f"type of {label('attribute', operation['attribute'])} refers to "
                f"{label('class', operation['classifier'])}")
    return f"{label('connector', operation['connector'])} removed"


def element_names(root: ET.Element) -> dict:
    """``(kind, EA id) -> readable name`` for the release model."""
    names = {}
    for package in root.iter(q("Package")):
        names[("package", int(package.findtext(q("id"))[1:]))] = package.findtext(q("name"))
    for cls in root.iter(q("Class")):
        class_name = cls.findtext(q("name"))
        names[("class", int(cls.findtext(q("id"))))] = class_name
        for prop in cls.iter(q("Property")):
            pid = prop.findtext(q("id")) or ""
            if "_" in pid and pid.split("_")[-1].isdigit() and not pid.startswith(("S", "T")):
                names[("attribute", int(pid.split("_")[-1]))] = \
                    f"{class_name}.{prop.findtext(q('name'))}"
    classes = {c.findtext(q("id")): c.findtext(q("name")) for c in root.iter(q("Class"))}
    for association in root.iter(q("Association")):
        cid = int((association.findtext(q("id")) or "as0")[2:])
        ends = {}
        for prop in association.iter(q("Property")):
            ends[prop.findtext(q("id"))[:1]] = prop
        target = next((p for p in root.iter(q("Property")) if p.findtext(q("id")) == f"Tas{cid}"),
                      None)
        source = next((p for p in root.iter(q("Property")) if p.findtext(q("id")) == f"Sas{cid}"),
                      None)
        source_class = classes.get(source.findtext(q("typeId"))) if source is not None else "?"
        target_class = classes.get(target.findtext(q("typeId"))) if target is not None else "?"
        role = target.findtext(q("name")) if target is not None else None
        role = "" if role in (None, f"role_Tas{cid}") else f".{role}"
        names[("connector", cid)] = f"{source_class}{role} → {target_class}"
    return names


def render_changelog(changes: dict, names: dict) -> str:
    lines = [f"# {changes['name']}", "",
             f"Based on {changes['based_on']['version']}, the model in "
             f"`{changes['based_on']['model']}`. This file is generated from `changes.json` by "
             "`scripts/candidate_model.py`; edit that file instead.", ""]
    if changes.get("summary"):
        lines += [changes["summary"], ""]
    for change in changes["changes"]:
        lines += [f"## {change['id']}: {change['title']}", "", change["why"], "",
                  f"**Normative schema:** {change['schema']}", ""]
        described = [describe(o, names) for o in change["operations"]]
        lines += [f"- {text}" for text in described]
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------------------
# Building a candidate


def build(candidate_dir: Path, release_scxml: Path, artifact: str) -> tuple[str, str]:
    """The candidate SCXML and changelog, as text."""
    changes = load_changes(candidate_dir / "changes.json")
    root, header, root_start = read_scxml(release_scxml)
    names = element_names(root)
    apply_to_scxml(root, changes)
    return serialize(root, header, root_start), render_changelog(changes, names)


def main() -> int:
    from generate_semantic_artifacts import REPO_ROOT, STANDARDS

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true",
                        help="write the candidate SCXML and changelog instead of checking them")
    args = parser.parse_args()
    ok = True
    for name, spec in sorted(STANDARDS.items()):
        for candidate in sorted((REPO_ROOT / "standards" / name / "candidates").glob("*/")):
            if not (candidate / "changes.json").exists():
                continue
            scxml, changelog = build(candidate, REPO_ROOT / spec["model"], spec["artifact"])
            outputs = {candidate / f"{spec['artifact']}.scxml": scxml,
                       candidate / "CHANGELOG.md": changelog}
            for path, text in outputs.items():
                if args.write:
                    path.write_text(text, encoding="utf-8")
                    print(f"wrote {path.relative_to(REPO_ROOT)}")
                elif not path.exists() or path.read_text(encoding="utf-8") != text:
                    ok = False
                    print(f"FAIL: {path.relative_to(REPO_ROOT)} is not what changes.json "
                          "produces; run scripts/candidate_model.py --write")
                else:
                    print(f"ok: {path.relative_to(REPO_ROOT)} is up to date")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
