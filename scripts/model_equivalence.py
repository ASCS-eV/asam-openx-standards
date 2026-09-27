#!/usr/bin/env python3
"""Model equivalence between ASAM's Enterprise Architect project and the committed SCXML.

Every generated artifact in this repository derives from ``standards/<std>/uml/<std>.scxml``,
which derives from ASAM's ``standards/<std>/uml/source/*.qeax`` through the one pipeline step
that needs an Enterprise Architect licence. This module decides whether the SCXML is the *same
model* as the EA project, and names every way in which it is not. It needs neither EA nor
ShapeChange: a ``.qeax`` is an SQLite database, so both sides are read with the standard
library alone.

Both sides are read into one normalized model and compared fact by fact. The two readers are
deliberately not symmetric:

**The EA side is read with UML semantics, not with ShapeChange's.** Where EA records a fact in
two places, both are read. A stereotype is the union of the element's ``Stereotype`` column
and its ``t_xref`` ``Stereotypes`` rows; ShapeChange's ``Connector.GetStereotypeEx()`` returns
only the second for connectors. A classifier owned by another classifier (``ParentID``) is
part of the model, although ShapeChange visits only the elements of packages. A connector's
``Direction`` states navigability when an end's own ``Navigable`` style does not. A package's
notes are in ``t_package`` and again in its element in ``t_object``. Reading the model the way
the exporter reads it would prove only that the exporter agrees with itself.

**The SCXML side is read as ShapeChange's own SCXML reader reads it, and totally.** Every
element and attribute of the file is checked against a table of what each element may contain
(:data:`SCXML_CONTENT`), with :data:`SCXML_REQUIRED` naming the children that must be there. Each
of the following is a finding in its own right:

- an unknown or foreign-namespace child, and child elements or stray text inside a value;
- a repeated single-valued child (ShapeChange keeps the last, and so does this reader);
- a list item under a non-canonical tag. ShapeChange reads it as an item in a string list, and
  so does this reader; elsewhere it is ignored, except that a class or package is loaded
  wherever it appears in a package;
- a repeated id or tagged-value name;
- a role property no association end uses;
- an end placed or ordered other than ShapeChange writes it.

It is not read through ShapeChange's reader itself, which re-normalizes stereotypes and tags on
the way in and would hide exactly the differences this check exists to find.

Elements are joined by identifier, never by name. ShapeChange carries EA's ids over: package
``P<Package_ID>``, classifier ``<Object_ID>``, attribute ``<Object_ID>_<ID>``, association
``as<Connector_ID>``, association ends ``S`` / ``T`` + the association id. The ``S`` end
belongs to the target class and is typed by the source; the ``T`` end the reverse.

Three verdicts, kept apart because they have different fixes:

``MISSING``
    The model states it; the SCXML does not carry it. Information the export lost.

``EXTRA``
    The SCXML states it; the model does not. Information the export invented, or content
    this module does not compare.

``DIFFERENT``
    Both state it, and the values contradict each other.

Each finding names the rule that produced it, one of :data:`RULES`, so a baseline of accepted
findings reads as a list of known export defects by cause.

Three kinds of difference are not findings. Each is declared here, and verified or counted.
Line references are to ShapeChange ``62c30807``, the commit pinned in
``pipeline/toolchain-lock.json``.

*Derived values.* ShapeChange fills fields the model leaves blank, or writes a value computed
from it. The check computes the value the export must then hold, and reports anything else:

- the association name ``<source>_<target>`` when ``t_connector.Name`` is blank
  (``AssociationInfoImpl.java:97-113``);
- the role name ``role_<S|T>as<id>`` when the role is blank (``EAConnectorEndUtil.java:591-597``);
- the ``enumeration`` / ``datatype`` stereotype on an EA ``Enumeration`` / ``DataType`` without
  one (``ClassInfoEA.java:538-552``);
- ``isComposition`` on every attribute outside an enumeration (``PropertyInfoEA.java:565-570``);
- the navigability of an end the model does not state: navigable when the connector's direction
  is ``Unspecified`` or ``Bi-Directional``, but never for a role that is unnamed or named
  ``role_…`` (``EAConnectorEndUtil.java:611-630``, ``EAConnectorUtil.java:547-557``);
- ``definition`` as the documentation with Java's ``trim()`` applied (``InfoImpl.java:317-343``);
- an attribute's type bound by name when its classifier id is empty or names no exported class,
  and ``typeName`` as the bound class's name (``PropertyInfoEA.java:175-186``). When several
  exported classes share the name, any of them is accepted;
- the ``inlineOrByReference`` value: the ``inlineOrByReference`` tag, else EA's containment
  ``By Reference`` / ``By Value``, lower-cased (``PropertyInfoEA.java:536-560``);
- the descriptors ``example``, ``primaryCode``, ``language``, ``legalBasis`` and
  ``dataCaptureStatement`` as the values of the same-named tags (``EADocument.java:830-846``);
- a constraint's kind: ``OclConstraint`` or, when OCL parsing fails, ``TextConstraint`` for EA
  types matching ``(OCL|Invariant)``; ``FolConstraint`` for ``(SBVR)``; ``TextConstraint``
  carrying the EA type otherwise. Its text is EA's plain-text rendering of its notes, and an
  attribute constraint's status is written into its name as ``name[status]``
  (``ClassInfoEA.java:886-934``, ``TextConstraintEA.java:60-110``).

*Normalizations* of notation that carries no information:

- UML's default multiplicity 1 for an empty bound or cardinality;
- EA names trimmed of surrounding whitespace, as ShapeChange trims them when it reads EA. The
  SCXML side is read raw: ShapeChange's SCXML reader trims nothing but booleans;
- documentation compared in EA's plain-text rendering of its rich-text notes
  (``EADocument.java:804-806``, reproduced by :func:`ea_txt`). A hyperlink target inside a
  note is information that rendering discards, so it is reported. A value Java's ``trim()``
  leaves empty is not written (``ModelWriter.java:667-706``), so it equals no value;
- an initial value trimmed, with one leading and one trailing ``"`` and the case of
  ``true``/``false`` removed (``PropertyInfoEA.java:484-508``);
- the case of ShapeChange's well-known stereotypes (``StereotypeNormalizer.java:89-91``; the
  union of the per-kind sets in ``Options.java:109-122``);
- the tag-name aliases ShapeChange applies (``TaggedValueNormalizer.java:185-221``);
- booleans read as ShapeChange reads them, ``true`` in any case or ``1``
  (``AbstractContentHandler.java:140-144``). A value outside ``xs:boolean`` is still reported;
- a tagged value declared with no value, which equals no tagged value. These are counted per
  tag, so a claim such as "declared 106 times, never given a value" is measured;
- a custom property (``t_xref`` ``CustomProperties``) whose value is empty, ``0`` or ``false``,
  which is unset;
- a member of an enumeration for which EA records no ``IsLiteral`` style, which is a literal;
  these are counted.

*Order.* EA returns a class's attributes ordered by ``Pos``, then by name, and ShapeChange numbers
them in that order; the export must follow it. An attribute carrying a numeric
``sequenceNumber`` tag is numbered by the tag instead (``PropertyInfoEA.java:389-391``), after
the untagged ones.

*Out of scope*, because it is not UML model content. It is counted where EA stores it as
rows, and printed as such; the counts are reported, not gated, because the ``.qeax`` bytes are
pinned by checksum (``verify-models.yml``):

- diagrams (``t_diagram``, ``t_diagramobjects``, ``t_diagramlinks``) and their furniture
  elements (``Boundary``, ``Text``, ``Note``);
- ``NoteLink`` connectors and ``t_xref`` ``diagram properties``;
- ``t_document``: document styles, stereotype backups, forum entries, baselines;
- ``t_stereotypes``, the profile definitions, and ``t_script``;
- ``t_xref`` rows and ``t_taggedvalue`` rows that belong to no model element;
- ``t_taggedvalue`` rows that describe a package (``LastImportFileDate``);
- EA's bookkeeping and presentation columns: GUIDs, authors, dates, ``Status``, ``Version``,
  ``Phase``, ``Complexity``, ``Effort``, ``GenType``, ``GenFile``, ``GenOption``,
  ``PDATA*``, ``TPos``, ``Tagged``, colours, borders, ``Diagram_ID``, connector geometry,
  label caches and ``SeqNo``, ``HeadStyle``, ``LineStyle``, ``RouteStyle``, ``IsBold``,
  ``Target2``, ``VirtualInheritance``, ``IsSignal``, ``IsStimulus``, constraint ``Weight``,
  the ``t_package`` flags (``IsControlled``, ``Protected``, ``UseDTD``, ``LogXML``,
  ``PackageFlags``, ``BatchSave``, ``BatchLoad``), the ``MDoc`` linked-document flag in
  ``t_object.Style`` (neither project holds a linked document), and ``t_xref`` ``Visibility``,
  ``Namespace``, ``Requirement``, ``Partition``, ``Supplier``, ``Link``;
- ``SourceIsNavigable`` / ``DestIsNavigable``. EA's own API reports navigability from the
  ``Navigable`` style key; these columns are a cache that disagrees with it on 18 of the ends
  whose style states navigability explicitly (14 OpenSCENARIO, 4 OpenDRIVE);
- ``t_object.Classifier_guid`` (the classifier of an ``Object`` is read from ``Classifier``),
  ``t_connector.DiagramID``, and every other EA reference or configuration table
  (``t_datatypes``, ``t_genopt``, ``t_template``, ``usys*``, ...), counted by name;
- ``Package@editable``, which records the packages ShapeChange selected, and the SCXML header
  attributes;
- the ``sequenceNumber`` of an association role, a counter ShapeChange assigns
  (``PropertyInfoEA.java:417-421``), except that two properties of one class may not share one.

Run it through ``check_model_equivalence.py``; this module holds only pure functions and is
tested on its own by ``test_model_equivalence.py``, which requires a negative case for every
rule.
"""

from __future__ import annotations

import hashlib
import html
import re
import sqlite3
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

#: The SCXML namespace, as written by ShapeChange's ModelExport target.
SC = "http://shapechange.net/model"

#: The verdicts, in the order a report reads best.
VERDICTS = ("MISSING", "EXTRA", "DIFFERENT")

#: Every rule a finding can carry. The self-test fails unless each has a negative case.
RULES = frozenset({
    # Structure of the SCXML file itself.
    "export-element", "export-id", "export-value", "export-descriptor", "duplicate-id",
    "property", "property-sequence-number", "end", "end-placement",
    # Packages.
    "package", "package-name", "package-parent", "package-stereotype", "package-tag",
    "package-documentation", "package-definition", "package-alias",
    "package-documentation-link", "package-descriptor", "package-visibility",
    "package-unrepresentable", "package-element-note",
    # Classifiers and elements.
    "classifier", "nested-classifier", "element-type", "classifier-name", "classifier-package",
    "classifier-owner", "classifier-abstract", "classifier-leaf", "classifier-kind",
    "classifier-visibility", "classifier-unrepresentable", "classifier-stereotype",
    "classifier-tag", "classifier-documentation", "classifier-definition", "classifier-alias",
    "classifier-documentation-link", "classifier-descriptor",
    # Generalizations, realizations, other connectors.
    "generalization", "generalization-stereotype", "generalization-tag",
    "generalization-documentation", "generalization-unrepresentable", "generalization-by-name",
    "realization", "realization-by-name", "subtypes", "connector-type", "connector-end-tag",
    # Attributes.
    "attribute", "attribute-name", "attribute-owner", "attribute-type", "attribute-type-name",
    "attribute-multiplicity", "attribute-initial-value", "attribute-read-only",
    "attribute-derived", "attribute-ordered", "attribute-unique", "attribute-containment",
    "attribute-composition", "attribute-aggregation", "attribute-owned", "attribute-navigable",
    "attribute-qualifiers", "attribute-literal", "attribute-visibility",
    "attribute-unrepresentable", "attribute-stereotype", "attribute-tag",
    "attribute-documentation", "attribute-definition", "attribute-alias",
    "attribute-documentation-link", "attribute-descriptor", "attribute-order",
    # Associations and their ends.
    "association", "association-endpoint", "association-name", "association-stereotype",
    "association-tag", "association-documentation", "association-definition",
    "association-alias", "association-documentation-link", "association-descriptor",
    "association-unrepresentable",
    "end-id", "end-association-id", "end-owner", "end-type-name", "end-role", "end-multiplicity",
    "end-navigability", "end-aggregation", "end-ordered", "end-unique", "end-derived",
    "end-owned", "end-read-only", "end-qualifiers", "end-containment", "end-initial-value",
    "end-visibility", "end-stereotype", "end-tag", "end-documentation", "end-definition",
    "end-alias", "end-documentation-link", "end-descriptor", "end-unrepresentable",
    # Constraints and operations.
    "constraint", "constraint-kind", "operation",
})

#: EA element types that are classifiers ShapeChange can export.
EXPORTABLE_KINDS = frozenset({"Class", "Interface", "DataType", "Enumeration"})

#: EA element types that belong to diagrams, not to the UML model.
DIAGRAM_ELEMENT_TYPES = frozenset({"Boundary", "Text", "Note"})

#: EA connector types compared as associations, and the ones that attach diagram notes.
ASSOCIATION_TYPES = frozenset({"Association", "Aggregation"})
DIAGRAM_CONNECTOR_TYPES = frozenset({"NoteLink"})

#: ShapeChange lower-cases these stereotypes when it reads them (``StereotypeNormalizer``,
#: the union of the per-kind well-known sets in ``Options.java:109-122``).
WELL_KNOWN_STEREOTYPES = frozenset({
    "codelist", "enumeration", "datatype", "featuretype", "type", "basictype", "interface",
    "union", "abstract", "fachid", "schluesseltabelle", "adeelement", "featureconcept",
    "attributeconcept", "valueconcept", "roleconcept", "aixmextension", "retired",
    "featurecollection", "voidable", "identifier", "version", "property", "estimated", "enum",
    "propertymetadata", "application schema", "schema", "bundle", "leaf", "disjoint",
})

#: Tag names ShapeChange renames on read (``TaggedValueNormalizer.java:203-222``).
TAG_RENAMES = {
    "xmlNamespace": "targetNamespace",
    "xmlNamespaceAbbreviation": "xmlns",
    "xsdName": "xsdDocument",
    "asGroup": "gmlAsGroup",
    "implementedByNilReason": "gmlImplementedByNilReason",
}

#: Descriptors: the three ShapeChange fills from EA itself, the five it fills from same-named
#: tags, and the two whose source is ``none`` in the export configuration.
NOTE_DESCRIPTORS = ("documentation", "definition", "alias")
TAG_DESCRIPTORS = ("example", "primaryCode", "language", "legalBasis", "dataCaptureStatement")
UNSOURCED_DESCRIPTORS = ("description", "globalIdentifier")

#: What each SCXML element may contain (``ShapeChangeExportedModel.xsd``). ``1`` is a single
#: child, ``"*"`` a repeatable one, and a tuple a list container with its canonical item tag.
#: The item kind, when it is itself described here, is validated in turn.
SCXML_CONTENT = {
    "Model": {"packages": ("Package",), "associations": ("Association",)},
    "Package": {"name": 1, "id": 1, "stereotypes": ("Stereotype",), "descriptors": 1,
                "taggedValues": ("TaggedValue",), "classes": ("Class",),
                "packages": ("Package",)},
    "Class": {"name": 1, "id": 1, "stereotypes": ("Stereotype",), "descriptors": 1,
              "taggedValues": ("TaggedValue",), "isAbstract": 1, "isLeaf": 1,
              "supertypes": ("SupertypeId",), "subtypes": ("SubtypeId",),
              "properties": ("Property",), "constraints": ("Constraint",)},
    "Property": {"name": 1, "id": 1, "stereotypes": ("Stereotype",), "descriptors": 1,
                 "taggedValues": ("TaggedValue",), "cardinality": 1, "isNavigable": 1,
                 "sequenceNumber": 1, "typeId": 1, "typeName": 1, "isDerived": 1,
                 "isReadOnly": 1, "isAttribute": 1, "isOrdered": 1, "isUnique": 1,
                 "isComposition": 1, "isAggregation": 1, "isOwned": 1, "initialValue": 1,
                 "inlineOrByReference": 1, "qualifiers": ("Qualifier",), "inClassId": 1,
                 "associationId": 1, "constraints": ("Constraint",)},
    "Association": {"name": 1, "id": 1, "stereotypes": ("Stereotype",), "descriptors": 1,
                    "taggedValues": ("TaggedValue",), "end1": 1, "end2": 1},
    "end": {"Property": 1},
    "TaggedValue": {"name": 1, "values": ("Value",)},
    "Qualifier": {"name": 1, "type": 1},
    "Constraint": {"name": 1, "status": 1, "text": 1, "type": 1, "sourceType": 1,
                   "description": "*"},
    "descriptors": {kind: 1 for kind in NOTE_DESCRIPTORS + TAG_DESCRIPTORS
                    + UNSOURCED_DESCRIPTORS},
    "descriptor": {"descriptorValues": ("DescriptorValue",)},
}

#: Children each element must have (``ShapeChangeExportedModel.xsd``). A missing id, end or
#: sequence number has its own rule and is not repeated here.
SCXML_REQUIRED = {
    "Package": ("name",), "Class": ("name",), "Property": ("name",),
    "TaggedValue": ("name",), "Qualifier": ("name",), "descriptor": ("descriptorValues",),
    "Constraint": ("name",),
}

#: List containers whose items ShapeChange reads as strings, under any tag, taking the last
#: container (``StringListContentHandler``). Other lists keep only their canonical items, from
#: every container.
STRING_LISTS = frozenset({"stereotypes", "supertypes", "subtypes", "values"})

#: Children that hold a single value: they may contain text only.
SCXML_VALUES = frozenset({
    "name", "id", "cardinality", "isNavigable", "sequenceNumber", "typeId", "typeName",
    "isDerived", "isReadOnly", "isAttribute", "isOrdered", "isUnique", "isComposition",
    "isAggregation", "isOwned", "initialValue", "inlineOrByReference", "inClassId",
    "associationId", "isAbstract", "isLeaf", "status", "text", "type", "sourceType",
    "description", "Stereotype", "SupertypeId", "SubtypeId", "Value", "DescriptorValue",
})

#: The constraint elements ShapeChange writes, all validated as ``Constraint``.
CONSTRAINT_KINDS = frozenset({"OclConstraint", "FolConstraint", "TextConstraint"})

#: XML attributes each element may carry; any other is reported.
SCXML_ATTRIBUTES = {
    "Model": {"encoding", "scxmlProducer", "scxmlProducerVersion",
              "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"},
    "Package": {"editable"},
    "end": {"ref"},
    "DescriptorValue": {"lang"},
}

#: EA containment and the ``inlineOrByReference`` value ShapeChange derives from it. EA spells
#: an attribute's containment ``By Reference``/``By Value``, and a connector end's
#: ``Reference``/``Value``; ShapeChange maps only the attribute spelling.
ATTRIBUTE_CONTAINMENT = {"By Reference": "byreference", "By Value": "inline"}
END_CONTAINMENT = {"Reference": "byreference", "Value": "inline"}
CONTAINMENT_UNSET = frozenset({"", "Not Specified", "Unspecified"})

#: EA tables this reader reads, and those it only counts as out of scope. Every other
#: non-empty table is counted as EA configuration.
READ_TABLES = frozenset({
    "t_package", "t_object", "t_attribute", "t_connector", "t_xref", "t_objectproperties",
    "t_attributetag", "t_connectortag", "t_taggedvalue", "t_objectconstraint",
    "t_attributeconstraints", "t_operation", "t_document", "t_diagram", "t_diagramobjects",
    "t_diagramlinks", "t_stereotypes", "t_script",
})
COUNTED_TABLES = ("t_diagram", "t_diagramobjects", "t_diagramlinks", "t_stereotypes", "t_script")

#: ShapeChange's default constraint-type patterns (``Options.java:2287-2288``).
OCL_TYPES = re.compile(r"(OCL|Invariant)")
FOL_TYPES = re.compile(r"(SBVR)")


class VacuousComparison(RuntimeError):
    """Raised when one side holds nothing, or the two sides share no element.

    A comparison of an empty model reports no findings and passes; so would a comparison
    whose inputs were mis-wired, if nothing noticed that the two sides never meet.
    """


class NotAnEaProject(RuntimeError):
    """Raised when the ``.qeax`` is not an SQLite database, usually a Git LFS pointer."""


# ---------------------------------------------------------------------------------------
# The normalized model


@dataclass
class End:
    """One association end. Fields the SCXML has and EA has not are export-only."""

    role: str | None = None
    multiplicity: tuple | str = (1, 1)
    #: True, False, or None when the model does not state it.
    navigable: bool | None = None
    #: Model: the aggregation kind of the *whole* at this end (``none``/``shared``/``composite``).
    aggregation: str = "none"
    ordered: bool = False
    unique: bool = True
    derived: bool = False
    owned: bool = False
    read_only: bool = False
    qualifiers: tuple = ()
    containment: str | None = None
    visibility: str | None = None
    initial_value: str | None = None
    stereotypes: frozenset = frozenset()
    tags: dict = field(default_factory=dict)
    documentation: str | None = None
    definition: str | None = None
    alias: str | None = None
    descriptors: dict = field(default_factory=dict)
    #: Model facts the SCXML has no place for, as ``name=value``.
    unrepresentable: tuple = ()
    links: tuple = ()
    # Export only.
    id: str | None = None
    association_id: str | None = None
    composition: bool = False
    shared: bool = False
    owner: str | None = None
    type_id: str | None = None
    type_name: str | None = None


@dataclass
class Association:
    id: str
    source: str | None
    target: str | None
    name: str | None
    stereotypes: frozenset = frozenset()
    tags: dict = field(default_factory=dict)
    documentation: str | None = None
    definition: str | None = None
    alias: str | None = None
    descriptors: dict = field(default_factory=dict)
    direction: str | None = None
    ends: dict = field(default_factory=dict)
    unrepresentable: tuple = ()
    links: tuple = ()


@dataclass
class Attribute:
    id: str
    owner: str
    name: str
    type_id: str | None = None
    type_name: str | None = None
    multiplicity: tuple | str = (1, 1)
    initial_value: str | None = None
    stereotypes: frozenset = frozenset()
    tags: dict = field(default_factory=dict)
    documentation: str | None = None
    definition: str | None = None
    alias: str | None = None
    descriptors: dict = field(default_factory=dict)
    #: Model: ``(Pos,)``. Export: ``sequenceNumber`` as a tuple. Only the order is compared.
    position: tuple | None = None
    visibility: str | None = None
    read_only: bool = False
    ordered: bool = False
    unique: bool = True
    derived: bool = False
    containment: str | None = None
    #: Model: EA's ``IsLiteral`` style, True/False, or None when EA does not record it.
    literal: bool | None = None
    unrepresentable: tuple = ()
    links: tuple = ()
    # Export only.
    composition: bool = False
    shared: bool = False
    owned: bool = False
    navigable: bool = True
    qualifiers: tuple = ()
    in_class: str | None = None
    association_id: str | None = None


@dataclass
class Classifier:
    id: str
    name: str
    kind: str | None
    package: str | None
    parent: str | None = None
    abstract: bool = False
    leaf: bool = False
    visibility: str | None = None
    stereotypes: frozenset = frozenset()
    tags: dict = field(default_factory=dict)
    documentation: str | None = None
    definition: str | None = None
    alias: str | None = None
    descriptors: dict = field(default_factory=dict)
    #: Model: ``t_object.GenLinks`` ``Parent=`` / ``Implements=`` names.
    parents_by_name: tuple = ()
    implements_by_name: tuple = ()
    unrepresentable: tuple = ()
    links: tuple = ()
    # Export only.
    supertypes: tuple = ()
    subtypes: tuple = ()


@dataclass
class Package:
    id: str
    name: str
    parent: str | None
    stereotypes: frozenset = frozenset()
    tags: dict = field(default_factory=dict)
    documentation: str | None = None
    definition: str | None = None
    alias: str | None = None
    descriptors: dict = field(default_factory=dict)
    visibility: str | None = None
    #: Model: the note of the package's element in ``t_object``, EA's second copy.
    element_note: str | None = None
    unrepresentable: tuple = ()
    links: tuple = ()


@dataclass
class Model:
    """Either side of the comparison. ``source`` is ``"qeax"`` or ``"scxml"``."""

    source: str
    packages: dict = field(default_factory=dict)
    classifiers: dict = field(default_factory=dict)
    attributes: dict = field(default_factory=dict)
    associations: dict = field(default_factory=dict)
    #: Model: connector id -> {"sub", "super", "stereotypes", "tags", "documentation",
    #: "unrepresentable"}.
    generalizations: dict = field(default_factory=dict)
    #: Model: connector id -> {"client", "supplier", "facts"}.
    realizations: dict = field(default_factory=dict)
    #: owner id -> list of {"name", "type", "status", "text"}.
    constraints: dict = field(default_factory=lambda: defaultdict(list))
    #: Model: connectors of other UML types, id -> (type, source, target).
    other_connectors: dict = field(default_factory=dict)
    #: Model: association-end tags on connectors that are not associations, as
    #: (connector id, connector type, side, tag, value).
    other_connector_end_tags: list = field(default_factory=list)
    #: Model: operations, id -> (owner, name).
    operations: dict = field(default_factory=dict)
    #: Model: elements that are not exportable classifiers, id -> (kind, name, detail).
    other_elements: dict = field(default_factory=dict)
    #: What was read but is out of scope, by category, with a count.
    out_of_scope: Counter = field(default_factory=Counter)
    #: Model: normalizations the reader applied, by kind, with a count.
    normalized: Counter = field(default_factory=Counter)
    #: Model: out-of-scope diagram texts, e.g. OpenDRIVE's ``{XOR}`` notes.
    diagram_texts: list = field(default_factory=list)
    #: Model: (owner kind, tag name) -> number of owners declaring the tag with no value.
    empty_tags: Counter = field(default_factory=Counter)
    #: Export: structural findings the reader makes on its own, as
    #: (verdict, rule, subject, detail).
    issues: list = field(default_factory=list)


# ---------------------------------------------------------------------------------------
# Notation shared by both readers


def java_trim(text: str) -> str:
    """Java's ``String.trim()``: strips characters up to U+0020, nothing else."""
    start, end = 0, len(text)
    while start < end and text[start] <= " ":
        start += 1
    while end > start and text[end - 1] <= " ":
        end -= 1
    return text[start:end]


def ea_txt(raw: str | None) -> str | None:
    """EA's plain-text rendering of a rich-text note (``GetFormatFromField("TXT", …)``).

    ShapeChange asks EA for this rendering, so the SCXML documentation is in it. The rules are
    reverse-engineered from the two ASAM models, where they reproduce all 2,195 non-empty
    documentation values; the EA version that ran the export is not recorded. Tags are
    removed and their text kept; an ordered list item becomes ``N. `` and an unordered one
    ``- ``; a line break directly after ``<ul>`` or ``</ul>`` is dropped; ``&nbsp;`` is removed
    and other entities are decoded; trailing line breaks are removed. A rendering Java's
    ``trim()`` leaves empty is no rendering, because ShapeChange does not write it.
    """
    if raw is None or raw == "":
        return None
    tokens = re.split(r"(<[^>]+>)", raw)
    out: list[str] = []
    lists: list[list] = []
    for i, token in enumerate(tokens):
        if token.startswith("<") and token.endswith(">"):
            tag = token[1:-1].strip().lower()
            closing = tag.startswith("/")
            bare = tag.lstrip("/")
            name = bare.split()[0] if bare else ""
            if name in ("ol", "ul"):
                if closing:
                    if lists:
                        lists.pop()
                else:
                    lists.append([name, 0])
                if name == "ul" and i + 1 < len(tokens) and tokens[i + 1].startswith("\r\n"):
                    tokens[i + 1] = tokens[i + 1][2:]
            elif name == "li" and not closing:
                if lists and lists[-1][0] == "ol":
                    lists[-1][1] += 1
                    out.append(f"{lists[-1][1]}. ")
                else:
                    out.append("- ")
        else:
            out.append(token)
    text = html.unescape("".join(out).replace("&nbsp;", "")).rstrip("\r\n")
    return text if java_trim(text) else None


def link_targets(raw: str | None) -> tuple:
    """Hyperlink targets in a rich-text note, which the plain-text rendering discards."""
    if not raw:
        return ()
    return tuple(href.removeprefix("$inet://") for href in
                 re.findall(r"""<a\s[^>]*href\s*=\s*["']([^"']+)["']""", raw, flags=re.I))


def parse_multiplicity(lower: str | None, upper: str | None) -> tuple | str:
    """A UML multiplicity from two bounds. An empty bound is UML's default, 1."""
    def bound(value: str | None, is_upper: bool):
        text = (value or "").strip()
        if text == "":
            return 1
        if text == "*":
            return None if is_upper else 0
        return int(text)
    try:
        return (bound(lower, False), bound(upper, True))
    except ValueError:
        return f"{lower!r}..{upper!r}"


def parse_cardinality(text: str | None) -> tuple | str:
    """A UML multiplicity from a cardinality string (``0..*``, ``1``, ``*``).

    An empty cardinality is UML's default, 1..1. A form one range cannot represent - a
    comma-separated list, or anything unparsable - is returned as the original string, so that
    it compares unequal to whatever the export made of it.
    """
    value = (text or "").strip()
    if value == "":
        return (1, 1)
    if value == "*":
        return (0, None)
    try:
        if ".." in value:
            low, high = value.split("..", 1)
            return (int(low), None if high.strip() == "*" else int(high))
        return (int(value), int(value))
    except ValueError:
        return value


def show_multiplicity(multiplicity: tuple | str) -> str:
    if isinstance(multiplicity, str):
        return multiplicity
    low, high = multiplicity
    return f"{low}..{'*' if high is None else high}"


def parse_sequence(text: str | None) -> tuple | None:
    """A ShapeChange ``sequenceNumber`` (a ``StructuredNumber``: ``n`` or ``n.n.n``)."""
    try:
        return tuple(int(part) for part in (text or "").strip().split("."))
    except ValueError:
        return None


def normalize_stereotype(name: str) -> str:
    return name.lower() if name.lower() in WELL_KNOWN_STEREOTYPES else name


def normalize_tag_name(name: str) -> str:
    name = name.strip()
    if "::" in name:
        name = name.rsplit("::", 1)[1]
    return TAG_RENAMES.get(name, name)


def add_tag(tags: dict, name: str, value: str | None) -> None:
    """Record one tagged-value row. Empty values are kept apart from real ones."""
    tags.setdefault(normalize_tag_name(name), []).append(value or "")


def split_tags(raw: dict) -> tuple[dict, set]:
    """Split raw tags into ``{name: Counter(values)}`` with values, and the names without."""
    valued, empty = {}, set()
    for name, values in raw.items():
        real = Counter(v for v in values if v != "")
        if real:
            valued[name] = real
        else:
            empty.add(name)
    return valued, empty


def parse_style(style: str | None) -> dict:
    """EA's ``key=value;`` style strings (``SourceStyle``, ``StyleEx``, ``GenLinks``, ...)."""
    result = {}
    for part in (style or "").split(";"):
        if "=" in part:
            key, value = part.split("=", 1)
            result[key.strip()] = value.strip()
    return result


def parse_pairs(style: str | None) -> list[tuple[str, str]]:
    """EA's ``key=value;`` strings as a list, where a key may repeat (``GenLinks``)."""
    pairs = []
    for part in (style or "").split(";"):
        if "=" in part:
            key, value = part.split("=", 1)
            pairs.append((key.strip(), value.strip()))
    return pairs


def normalize_initial_value(raw: str | None) -> str | None:
    """EA's attribute default as ShapeChange carries it (see the module docstring)."""
    value = (raw or "").strip()
    if value == "":
        return None
    if value.startswith('"'):
        value = value[1:]
    if value.endswith('"'):
        value = value[:-1]
    if value.lower() in ("true", "false"):
        value = value.lower()
    return value or None


def parse_qualifiers(raw: str | None) -> tuple:
    """EA's ``name:type;name:type`` end qualifiers, in order, as (name, type) pairs."""
    pairs = []
    for part in (raw or "").split(";"):
        if part.strip():
            name, _, kind = part.partition(":")
            pairs.append((name.strip(), kind.strip()))
    return tuple(pairs)


def containment(raw_tags: dict, value: str | None,
                vocabulary: dict) -> tuple[str | None, str | None]:
    """The ``inlineOrByReference`` a property must be exported with, and an unmappable value.

    ShapeChange takes the first value of the ``inlineOrByReference`` tag, in EA's row order,
    then EA's containment, and writes the result lower-cased.
    """
    tag = next((v for v in raw_tags.get("inlineOrByReference", ()) if v), None)
    if tag:
        return tag.lower(), None
    text = (value or "").strip()
    if text in CONTAINMENT_UNSET:
        return None, None
    if text in vocabulary:
        return vocabulary[text], None
    return None, text


def expected_constraint_kinds(ea_type: str | None, attribute: bool = False) -> frozenset:
    """The constraint elements ShapeChange may write for an EA constraint type.

    A class constraint's type is matched against the configured patterns
    (``ClassInfoEA.java:905-926``); an attribute constraint's against ``SBVR`` ignoring case
    (``PropertyInfoEA.java:953``).
    """
    kind = ea_type or ""
    if OCL_TYPES.fullmatch(kind):
        return frozenset({"OclConstraint", "TextConstraint"})
    if (kind.lower() == "sbvr") if attribute else FOL_TYPES.fullmatch(kind):
        return frozenset({"FolConstraint"})
    return frozenset({"TextConstraint"})


def split_constraint_name(raw: str) -> tuple[str, str | None]:
    """An attribute constraint's name and status, as ShapeChange splits ``name[status]``.

    The name is trimmed; the status is between the first ``[`` and the next ``]``, and the
    name is what precedes the ``[`` (``TextConstraintEA.java:92-101``).
    """
    name = raw.strip()
    start = name.find("[")
    end = name.find("]", start) if start != -1 else -1
    if start != -1 and end != -1:
        return name[:start], name[start + 1:end].strip() or None
    return name, None


# ---------------------------------------------------------------------------------------
# The EA side


def _stereotype_blocks(description: str | None) -> list[str]:
    """Stereotype names in a ``t_xref`` ``Stereotypes`` row (``@STEREO;Name=…;@ENDSTEREO;``)."""
    names = []
    for block in re.findall(r"@STEREO;(.*?)@ENDSTEREO;", description or ""):
        for part in block.split(";"):
            if part.startswith("Name="):
                names.append(part[len("Name="):].strip())
    return [n for n in names if n]


def _custom_properties(description: str | None) -> list[tuple[str, str]]:
    """``(name, value)`` pairs in a ``t_xref`` ``CustomProperties`` row (``@PROP=…@ENDPROP;``)."""
    pairs = []
    for block in re.findall(r"@PROP=(.*?)@ENDPROP;", description or ""):
        name = re.search(r"@NAME=(.*?)@ENDNAME;", block)
        value = re.search(r"@VALU=(.*?)@ENDVALU;", block)
        if name:
            pairs.append((name.group(1), value.group(1) if value else ""))
    return pairs


def _xref_target(xref_type: str | None) -> str:
    """Which part of its owner a ``t_xref`` row describes: the element, or a connector end."""
    kind = (xref_type or "").lower()
    if "srcend" in kind or "sourceend" in kind:
        return "S"
    if "destend" in kind or "targetend" in kind:
        return "T"
    return "owner"


def _role_tag_value(notes: str | None) -> str:
    """A role tag's value from ``t_taggedvalue.Notes``: EA's ``<memo>`` / ``$ea_notes=`` forms."""
    value = notes or ""
    if value.startswith("<memo>$ea_notes="):
        return value[len("<memo>$ea_notes="):]
    if value.startswith("<memo>"):
        return ""
    if "$ea_notes=" in value:
        return value[: value.index("$ea_notes=")]
    return value


def _tag_value(value: str | None, notes: str | None) -> str:
    """An object, attribute or connector tag's value: ``<memo>`` means "look in Notes".

    Otherwise ``Notes`` holds the profile's help text for the tag, not a value.
    """
    return (notes or "") if value == "<memo>" else (value or "")


def _flag(value) -> bool:
    return str(value or 0).strip() == "1"


def _tag_descriptors(tags: dict) -> dict:
    """The descriptors ShapeChange fills from same-named tags, as sorted value lists."""
    return {kind: sorted(tags[kind].elements()) for kind in TAG_DESCRIPTORS if kind in tags}


def read_qeax(path: Path) -> Model:
    """Read an EA project (``.qeax``, SQLite) with UML semantics."""
    head = Path(path).read_bytes()[:64]
    if not head.startswith(b"SQLite format 3\x00"):
        hint = " It is a Git LFS pointer: run `git lfs pull`." if b"git-lfs" in head else ""
        raise NotAnEaProject(f"{path} is not an SQLite database.{hint}")
    connection = sqlite3.connect(f"file:{Path(path).resolve()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        return _EaReader(connection).read()
    finally:
        connection.close()


class _EaReader:
    """Reads the tables of an EA project into the normalized model."""

    def __init__(self, db: sqlite3.Connection) -> None:
        self.db = db
        self.model = Model(source="qeax")
        self.xref_stereotypes: dict[tuple, set] = defaultdict(set)
        self.custom_properties: dict[tuple, list] = defaultdict(list)
        self.xref_owners: Counter = Counter()
        self.consumed: set = set()

    def rows(self, sql: str, *args) -> list:
        return self.db.execute(sql, args).fetchall()

    def count(self, table: str) -> int:
        exists = self.rows("SELECT name FROM sqlite_master WHERE type='table' AND name=?", table)
        return self.rows(f"SELECT COUNT(*) FROM {table}")[0][0] if exists else 0

    def stereotypes(self, guid: str | None, column: str | None, part: str = "owner") -> frozenset:
        self.consumed.add((guid, part))
        found = set(self.xref_stereotypes.get((guid, part), ()))
        for name in (column or "").split(","):
            if name.strip():
                found.add(name.strip())
        return frozenset(normalize_stereotype(s) for s in found)

    def custom(self, guid: str | None, part: str = "owner") -> list[str]:
        self.consumed.add((guid, part))
        return [f"{name}={value}" for name, value in self.custom_properties.get((guid, part), ())
                if value not in ("", "0", "false")]

    def record_empty(self, kind: str, empty: set) -> None:
        for name in empty:
            self.model.empty_tags[(kind, name)] += 1

    def read(self) -> Model:
        model = self.model
        for row in self.rows("SELECT Name, Type, Description, Client FROM t_xref"):
            key = (row["Client"], _xref_target(row["Type"]))
            if row["Name"] == "Stereotypes":
                self.xref_stereotypes[key].update(_stereotype_blocks(row["Description"]))
                self.xref_owners[row["Client"]] += 1
            elif row["Name"] == "CustomProperties" and row["Type"] == "diagram properties":
                model.out_of_scope["t_xref diagram properties"] += 1
            elif row["Name"] == "CustomProperties":
                self.custom_properties[key].extend(_custom_properties(row["Description"]))
                self.xref_owners[row["Client"]] += 1
            else:
                model.out_of_scope[f"t_xref {row['Name']}"] += 1
        for table in COUNTED_TABLES:
            if self.count(table):
                model.out_of_scope[f"{table} rows"] = self.count(table)
        if self.count("t_document"):
            for row in self.rows("SELECT DocType, COUNT(*) AS n FROM t_document GROUP BY 1"):
                model.out_of_scope[f"t_document {row['DocType']}"] = row["n"]

        objects = {str(r["Object_ID"]): r for r in self.rows("SELECT * FROM t_object")}
        object_tags: dict[str, dict] = defaultdict(dict)
        for row in self.rows("SELECT * FROM t_objectproperties ORDER BY PropertyID"):
            add_tag(object_tags[str(row["Object_ID"])], row["Property"],
                    _tag_value(row["Value"], row["Notes"]))
        self.read_packages(objects, object_tags)
        self.read_objects(objects, object_tags)
        self.read_attributes()
        self.read_connectors()
        self.read_constraints_and_operations()

        known = ({r["ea_guid"] for r in objects.values()}
                 | {r["ea_guid"] for r in self.rows("SELECT ea_guid FROM t_attribute")}
                 | {r["ea_guid"] for r in self.rows("SELECT ea_guid FROM t_connector")}
                 | {r["ea_guid"] for r in self.rows("SELECT ea_guid FROM t_package")})
        orphans = sum(n for guid, n in self.xref_owners.items() if guid not in known)
        if orphans:
            model.out_of_scope["t_xref rows without an owner"] = orphans
        misplaced = sum(1 for key in set(self.xref_stereotypes) | set(self.custom_properties)
                        if key[0] in known and key not in self.consumed)
        if misplaced:
            model.out_of_scope["t_xref rows describing a part their owner does not have"] = \
                misplaced
        for (table,) in self.rows("SELECT name FROM sqlite_master WHERE type='table'"):
            if table.startswith("sqlite_"):
                continue  # SQLite's own bookkeeping, not part of the EA project
            if table not in READ_TABLES and self.count(table):
                model.out_of_scope[f"EA configuration table {table}"] = self.count(table)
        return model

    def read_packages(self, objects: dict, object_tags: dict) -> None:
        by_guid = {r["ea_guid"]: r for r in objects.values()}
        for row in self.rows("SELECT * FROM t_package ORDER BY Package_ID"):
            pid = f"P{row['Package_ID']}"
            element = by_guid.get(row["ea_guid"])
            raw = object_tags.get(str(element["Object_ID"]), {}) if element else {}
            tags, empty = split_tags(raw)
            self.record_empty("package", empty)
            documentation = ea_txt(row["Notes"])
            unrepresentable = []
            if element is not None:
                unrepresentable = [f"{column}=1" for column in ("IsRoot", "IsSpec", "IsActive")
                                   if _flag(element[column])]
                if (element["Multiplicity"] or "").strip():
                    unrepresentable.append(f"Multiplicity={element['Multiplicity']}")
                unrepresentable += self.custom(element["ea_guid"])
            self.model.packages[pid] = Package(
                id=pid,
                name=(row["Name"] or "").strip(),
                parent=f"P{row['Parent_ID']}" if row["Parent_ID"] else None,
                stereotypes=self.stereotypes(row["ea_guid"],
                                             element["Stereotype"] if element else None),
                tags=tags,
                documentation=documentation,
                definition=java_trim(documentation) if documentation else None,
                alias=(element["Alias"] or None) if element else None,
                descriptors=_tag_descriptors(tags),
                visibility=element["Scope"] if element else None,
                element_note=ea_txt(element["Note"]) if element else None,
                unrepresentable=tuple(unrepresentable),
                links=link_targets(row["Notes"]),
            )

    def read_objects(self, objects: dict, object_tags: dict) -> None:
        model = self.model
        for oid, row in objects.items():
            kind = row["Object_Type"]
            if kind == "Package":
                continue
            if kind in DIAGRAM_ELEMENT_TYPES:
                model.out_of_scope[f"diagram element {kind}"] += 1
                if kind == "Text" and row["Note"]:
                    model.diagram_texts.append((oid, ea_txt(row["Note"])))
                continue
            if kind not in EXPORTABLE_KINDS:
                instance = str(row["Classifier"] or 0)
                detail = f", an instance of {instance}" if instance != "0" else ""
                model.other_elements[oid] = (kind, (row["Name"] or "").strip(), detail)
                continue
            tags, empty = split_tags(object_tags.get(oid, {}))
            self.record_empty("classifier", empty)
            unrepresentable = [f"{column}=1" for column in ("IsRoot", "IsSpec", "IsActive")
                               if _flag(row[column])]
            for column in ("Multiplicity", "Persistence"):
                if (row[column] or "").strip():
                    unrepresentable.append(f"{column}={row[column]}")
            if str(row["NType"] or 0) == "17":
                unrepresentable.append("association class (NType=17)")
            unrepresentable += self.custom(row["ea_guid"])
            parents, implements = [], []
            for key, value in parse_pairs(row["GenLinks"]):
                if key == "Parent":
                    parents.append(value)
                elif key == "Implements":
                    implements.append(value)
                else:
                    unrepresentable.append(f"GenLinks {key}={value}")
            documentation = ea_txt(row["Note"])
            model.classifiers[oid] = Classifier(
                id=oid,
                name=(row["Name"] or "").strip(),
                kind=kind,
                package=f"P{row['Package_ID']}",
                parent=str(row["ParentID"]) if row["ParentID"] else None,
                abstract=_flag(row["Abstract"]),
                leaf=_flag(row["IsLeaf"]),
                visibility=row["Scope"],
                stereotypes=self.stereotypes(row["ea_guid"], row["Stereotype"]),
                tags=tags,
                documentation=documentation,
                definition=java_trim(documentation) if documentation else None,
                alias=(row["Alias"] or None),
                descriptors=_tag_descriptors(tags),
                parents_by_name=tuple(parents),
                implements_by_name=tuple(implements),
                unrepresentable=tuple(unrepresentable),
                links=link_targets(row["Note"]),
            )

    def read_attributes(self) -> None:
        model = self.model
        attribute_tags: dict[str, dict] = defaultdict(dict)
        for row in self.rows("SELECT * FROM t_attributetag ORDER BY PropertyID"):
            add_tag(attribute_tags[str(row["ElementID"])], row["Property"],
                    _tag_value(row["VALUE"], row["NOTES"]))
        for row in self.rows("SELECT * FROM t_attribute"):
            owner = str(row["Object_ID"])
            aid = f"{owner}_{row['ID']}"
            raw_tags = attribute_tags.get(str(row["ID"]), {})
            tags, empty = split_tags(raw_tags)
            self.record_empty("attribute", empty)
            unrepresentable = [f"{column}={row[column]}"
                               for column in ("IsStatic", "IsCollection", "Length", "Precision",
                                              "Scale")
                               if str(row[column] or 0).strip() not in ("0", "")]
            if (row["Container"] or "").strip():
                unrepresentable.append(f"Container={row['Container']}")
            style = parse_style(row["StyleEx"])
            for key in ("union", "volatile"):
                if style.get(key, "0") not in ("0", ""):
                    unrepresentable.append(f"{key}={style[key]}")
            unrepresentable += self.custom(row["ea_guid"])
            expected, unmapped = containment(raw_tags, row["Containment"], ATTRIBUTE_CONTAINMENT)
            if unmapped:
                unrepresentable.append(f"Containment={unmapped}")
            literal = style.get("IsLiteral")
            if literal is None and _is_enumeration(model.classifiers.get(owner)):
                model.normalized["enumeration members without EA's IsLiteral "
                                 "(read as literals)"] += 1
            # EA's collection order is Pos, then name; a numeric sequenceNumber tag overrides
            # it in ShapeChange, after the untagged attributes.
            number = next((v for v in raw_tags.get("sequenceNumber", ())
                           if re.fullmatch(r"[0-9.]+", v)), None)
            name = (row["Name"] or "").strip()
            order = (1, parse_sequence(number)) if number else (0, float(row["Pos"] or 0), name)
            classifier_ref = (row["Classifier"] or "").strip()
            documentation = ea_txt(row["Notes"])
            model.attributes[aid] = Attribute(
                id=aid,
                owner=owner,
                name=name,
                type_id=classifier_ref if classifier_ref not in ("", "0") else None,
                type_name=(row["Type"] or "").strip() or None,
                multiplicity=parse_multiplicity(row["LowerBound"], row["UpperBound"]),
                initial_value=normalize_initial_value(row["Default"]),
                stereotypes=self.stereotypes(row["ea_guid"], row["Stereotype"]),
                tags=tags,
                documentation=documentation,
                definition=java_trim(documentation) if documentation else None,
                alias=(row["Style"] or None),
                descriptors=_tag_descriptors(tags),
                position=order,
                visibility=row["Scope"],
                read_only=_flag(row["Const"]),
                ordered=_flag(row["IsOrdered"]),
                unique=not _flag(row["AllowDuplicates"]),
                derived=_flag(row["Derived"]),
                containment=expected,
                literal=None if literal is None else literal == "1",
                unrepresentable=tuple(unrepresentable),
                links=link_targets(row["Notes"]),
            )

    def read_connectors(self) -> None:
        model = self.model
        connector_tags: dict[str, dict] = defaultdict(dict)
        for row in self.rows("SELECT * FROM t_connectortag ORDER BY PropertyID"):
            add_tag(connector_tags[str(row["ElementID"])], row["Property"],
                    _tag_value(row["VALUE"], row["NOTES"]))
        role_tags: dict[tuple, dict] = defaultdict(dict)
        for row in self.rows("SELECT * FROM t_taggedvalue ORDER BY PropertyID"):
            side = {"ASSOCIATION_SOURCE": "S", "ASSOCIATION_TARGET": "T"}.get(row["BaseClass"])
            if side is None:
                model.out_of_scope[f"t_taggedvalue {row['BaseClass']}"] += 1
                continue
            add_tag(role_tags[(row["ElementID"], side)], row["TagValue"] or "",
                    _role_tag_value(row["Notes"]))
        consumed = set()

        aggregation_kind = {"0": "none", "1": "shared", "2": "composite"}
        for row in self.rows("SELECT * FROM t_connector"):
            cid = str(row["Connector_ID"])
            kind = row["Connector_Type"]
            guid = row["ea_guid"]
            source, target = str(row["Start_Object_ID"]), str(row["End_Object_ID"])
            tags, empty = split_tags(connector_tags.get(cid, {}))
            documentation = ea_txt(row["Notes"])
            stereotypes = self.stereotypes(guid, row["Stereotype"])
            if kind not in ASSOCIATION_TYPES:
                for side in ("S", "T"):
                    end_tags, end_empty = split_tags(role_tags.get((guid, side), {}))
                    self.record_empty("connector end", end_empty)
                    consumed.add((guid, side))
                    for name, values in sorted(end_tags.items()):
                        model.other_connector_end_tags.append(
                            (cid, kind, side, name, sorted(values.elements())))
            if kind in DIAGRAM_CONNECTOR_TYPES:
                model.out_of_scope[f"diagram connector {kind}"] += 1
                continue
            if kind == "Generalization":
                model.generalizations[cid] = {
                    "sub": source, "super": target, "tags": tags,
                    "documentation": documentation, "stereotypes": stereotypes,
                    "unrepresentable": tuple(self.custom(guid) + [
                        f"{side} end {fact}" for side in ("S", "T")
                        for fact in self.custom(guid, side)]),
                }
                continue
            if kind == "Realisation":
                facts = [f"stereotype {s}" for s in sorted(stereotypes)] + [
                    f"tag {n}" for n in sorted(tags)] + (["notes"] if documentation else []) + [
                    f"custom property {c}" for c in self.custom(guid)]
                model.realizations[cid] = {"client": source, "supplier": target,
                                           "facts": tuple(facts)}
                continue
            if kind not in ASSOCIATION_TYPES:
                model.other_connectors[cid] = (kind, source, target)
                continue
            self.record_empty("association", empty)
            direction = (row["Direction"] or "Unspecified").strip()
            ends = {}
            for side, prefix in (("S", "Source"), ("T", "Dest")):
                consumed.add((guid, side))
                ends[side] = self.read_end(row, cid, side, prefix, direction, role_tags,
                                           aggregation_kind)
            unrepresentable = [f"{column}=1" for column in ("IsLeaf", "IsRoot", "IsSpec")
                               if _flag(row[column])]
            if (row["SubType"] or "").strip().lower() == "class":
                unrepresentable.append("association class (SubType=Class)")
            unrepresentable += self.custom(guid)
            model.associations[f"as{cid}"] = Association(
                id=f"as{cid}",
                source=source,
                target=target,
                name=row["Name"] if (row["Name"] or "").strip() else None,
                stereotypes=stereotypes,
                tags=tags,
                documentation=documentation,
                definition=java_trim(documentation) if documentation else None,
                alias=parse_style(row["StyleEx"]).get("alias") or None,
                descriptors=_tag_descriptors(tags),
                direction=direction,
                ends=ends,
                unrepresentable=tuple(unrepresentable),
                links=link_targets(row["Notes"]),
            )
        stray = sum(1 for key in role_tags if key not in consumed)
        if stray:
            model.out_of_scope["t_taggedvalue association-end rows without a connector"] = stray

    def read_end(self, row, cid: str, side: str, prefix: str, direction: str, role_tags: dict,
                 aggregation_kind: dict) -> End:
        guid = row["ea_guid"]
        end_tags, end_empty = split_tags(role_tags.get((guid, side), {}))
        self.record_empty("association end", end_empty)
        style = parse_style(row[f"{prefix}Style"])
        navigable = {"Navigable": True, "Non-Navigable": False}.get(style.get("Navigable"))
        if navigable is None:
            # EA states navigability on the connector when the end leaves it unspecified.
            arrow = {"S": "Destination -> Source", "T": "Source -> Destination"}[side]
            if direction in ("Bi-Directional", arrow):
                navigable = True
        unrepresentable = []
        if style.get("Union", "0") not in ("0", ""):
            unrepresentable.append(f"Union={style['Union']}")
        if (row[f"{prefix}TS"] or "instance").strip() not in ("instance", ""):
            unrepresentable.append(f"TS={row[f'{prefix}TS']}")
        changeable = (row[f"{prefix}Changeable"] or "none").strip()
        if changeable not in ("none", "frozen", ""):
            unrepresentable.append(f"Changeable={changeable}")
        expected, unmapped = containment(role_tags.get((guid, side), {}),
                                         row[f"{prefix}Containment"], END_CONTAINMENT)
        if unmapped:
            unrepresentable.append(f"Containment={unmapped}")
        unrepresentable += self.custom(guid, side)
        constraint = (row[f"{prefix}Constraint"] or "").strip()
        if constraint:
            self.model.constraints[f"{side}as{cid}"].append(
                {"name": constraint, "type": "Constraint", "status": None, "text": "",
                 "attribute": False})
        documentation = ea_txt(row[f"{prefix}RoleNote"])
        return End(
            role=(row[f"{prefix}Role"] or "").strip() or None,
            multiplicity=parse_cardinality(row[f"{prefix}Card"]),
            navigable=navigable,
            aggregation=aggregation_kind.get(str(row[f"{prefix}IsAggregate"] or 0), "none"),
            ordered=_flag(row[f"{prefix}IsOrdered"]),
            unique=style.get("AllowDuplicates", "0") in ("0", ""),
            derived=style.get("Derived", "0") not in ("0", ""),
            owned=style.get("Owned", "0") not in ("0", ""),
            read_only=changeable == "frozen",
            qualifiers=parse_qualifiers(row[f"{prefix}Qualifier"]),
            containment=expected,
            visibility=row[f"{prefix}Access"],
            stereotypes=self.stereotypes(guid, row[f"{prefix}Stereotype"], side),
            tags=end_tags,
            documentation=documentation,
            definition=java_trim(documentation) if documentation else None,
            descriptors=_tag_descriptors(end_tags),
            unrepresentable=tuple(unrepresentable),
            links=link_targets(row[f"{prefix}RoleNote"]),
        )

    def read_constraints_and_operations(self) -> None:
        model = self.model
        # ShapeChange writes a constraint's name as EA holds it and its text as EA's rendering
        # of the notes, neither trimmed (TextConstraintEA.java:60-110).
        for row in self.rows("SELECT * FROM t_objectconstraint"):
            model.constraints[str(row["Object_ID"])].append({
                "name": row["Constraint"] or "", "type": row["ConstraintType"],
                "status": (row["Status"] or "").strip() or None, "attribute": False,
                "text": ea_txt(row["Notes"]) or ""})
        for row in self.rows("SELECT * FROM t_attributeconstraints"):
            # EA has no status column for attribute constraints; ShapeChange reads it from the
            # name, written as name[status].
            name, status = split_constraint_name(row["Constraint"] or "")
            model.constraints[f"{row['Object_ID']}_{row['ID']}"].append({
                "name": name, "type": row["Type"], "status": status, "attribute": True,
                "text": ea_txt(row["Notes"]) or ""})
        for row in self.rows("SELECT * FROM t_operation"):
            model.operations[f"{row['Object_ID']}_M{row['OperationID']}"] = (
                str(row["Object_ID"]), (row["Name"] or "").strip())


# ---------------------------------------------------------------------------------------
# The SCXML side


def _q(tag: str) -> str:
    return f"{{{SC}}}{tag}"


def _local(element: ET.Element) -> str:
    return element.tag.split("}", 1)[1] if "}" in element.tag else element.tag


class _ScxmlReader:
    """Reads an SCXML file the way ShapeChange's reader does, reporting what it cannot place."""

    def __init__(self) -> None:
        self.model = Model(source="scxml")
        self.ids: dict[str, Counter] = defaultdict(Counter)
        self.properties: dict[str, dict] = {}
        self.references: Counter = Counter()
        self.anonymous = 0

    def issue(self, verdict: str, rule: str, subject: str, detail: str) -> None:
        self.model.issues.append((verdict, rule, subject, detail))

    # -- structure ---------------------------------------------------------------------

    def element_detail(self, element: ET.Element, message: str) -> str:
        """A finding detail naming the content, so two different contents never share a key."""
        digest = hashlib.sha1(ET.tostring(element)).hexdigest()[:8]
        return f"{message} [content {digest}]"

    def validate(self, element: ET.Element, kind: str, subject: str) -> None:
        """Check ``element`` against :data:`SCXML_CONTENT`, recursing into value kinds."""
        allowed_attributes = SCXML_ATTRIBUTES.get(kind, set())
        for name in element.attrib:
            if name not in allowed_attributes:
                self.issue("EXTRA", "export-element", subject,
                           f"attribute {name!r}={element.get(name)!r} on a {kind} is content "
                           "this check does not compare")
        content = SCXML_CONTENT[kind]
        for required in SCXML_REQUIRED.get(kind, ()):
            if element.find(_q(required)) is None:
                self.issue("MISSING", "export-element", subject,
                           f"a {kind} without <{required}>")
        counts = Counter(_local(child) for child in element if child.tag.startswith(f"{{{SC}}}"))
        for tag, count in sorted(counts.items()):
            spec = content.get(tag)
            if spec is not None and spec != "*" and count > 1:
                self.issue("EXTRA", "export-element", subject,
                           f"<{tag}> appears {count} times in a {kind}; ShapeChange's reader "
                           "keeps the last")
        for child in element:
            tag = _local(child)
            if (child.tail or "").strip():
                self.issue("EXTRA", "export-element", subject,
                           f"text {child.tail.strip()!r} after <{tag}> in a {kind}")
            if not child.tag.startswith(f"{{{SC}}}"):
                self.issue("EXTRA", "export-element", subject, self.element_detail(
                    child, f"<{child.tag}> in a {kind} is not in the SCXML namespace"))
                continue
            spec = content.get(tag)
            if spec is None:
                self.issue("EXTRA", "export-element", subject, self.element_detail(
                    child, f"<{tag}> in a {kind} is content this check does not compare"))
                continue
            if tag in SCXML_VALUES and kind != "descriptors":
                self.value_only(child, f"<{tag}> in a {kind}", subject)
            if isinstance(spec, tuple):
                self.validate_list(child, tag, spec[0], subject)
            elif tag == "descriptors":
                self.validate(child, "descriptors", subject)
            elif kind == "descriptors":
                self.validate(child, "descriptor", subject)

    def value_only(self, element: ET.Element, where: str, subject: str) -> None:
        """A value element holds text only; ShapeChange would read nested text into it."""
        if len(element):
            self.issue("EXTRA", "export-element", subject, self.element_detail(
                element, f"{where} contains child elements"))

    def validate_list(self, container: ET.Element, tag: str, canonical: str,
                      subject: str) -> None:
        for item in container:
            item_tag = _local(item)
            if (item.tail or "").strip():
                self.issue("EXTRA", "export-element", subject,
                           f"text {item.tail.strip()!r} in <{tag}>")
            if canonical == "Constraint":
                if item_tag in CONSTRAINT_KINDS and item.tag.startswith(f"{{{SC}}}"):
                    self.validate(item, "Constraint", f"{subject} constraint")
                else:
                    self.issue("EXTRA", "export-element", subject, self.element_detail(
                        item, f"<{item_tag}> in <{tag}> is not a constraint; ShapeChange's "
                        "reader ignores it"))
                continue
            if item_tag != canonical or not item.tag.startswith(f"{{{SC}}}"):
                if tag in STRING_LISTS:
                    message = f"<{item_tag}> in <{tag}> is read as a <{canonical}>"
                elif tag in ("classes", "packages") and item_tag in ("Class", "Package"):
                    message = (f"a <{item_tag}> in <{tag}>, which ShapeChange's reader loads "
                               "as part of the package")
                else:
                    message = f"<{item_tag}> in <{tag}> is not a <{canonical}>; ShapeChange's " \
                              "reader ignores it"
                self.issue("EXTRA", "export-element", subject, self.element_detail(item, message))
            if canonical in SCXML_VALUES or tag in STRING_LISTS:
                self.value_only(item, f"<{item_tag}> in <{tag}>", subject)
            if canonical in ("TaggedValue", "Qualifier") and item_tag == canonical:
                self.validate(item, canonical, subject)
            if canonical == "DescriptorValue":
                pass

    def last(self, element: ET.Element, tag: str) -> ET.Element | None:
        """The last child with this tag: ShapeChange's reader overwrites on each one."""
        children = element.findall(_q(tag))
        return children[-1] if children else None

    def text(self, element: ET.Element, tag: str) -> str | None:
        child = self.last(element, tag)
        return child.text if child is not None and child.text is not None else None

    def items(self, element: ET.Element, container: str,
              canonical: str | tuple | None = None) -> list[ET.Element]:
        """The canonical items of a list, from every container, as ShapeChange reads them."""
        wanted = (canonical,) if isinstance(canonical, str) else canonical
        return [item for holder in element.findall(_q(container)) for item in holder
                if item.tag.startswith(f"{{{SC}}}")
                and (wanted is None or _local(item) in wanted)]

    def strings(self, element: ET.Element, container: str, subject: str) -> tuple:
        """A string list: every item of the last container, under any tag, text as written."""
        holder = self.last(element, container)
        values = tuple(item.text for item in holder if item.text) if holder is not None else ()
        for value, count in Counter(values).items():
            if count > 1:
                self.issue("EXTRA", "export-element", subject,
                           f"{value!r} appears {count} times in <{container}>")
        return values

    def flag(self, element: ET.Element, tag: str, default: bool, subject: str) -> bool:
        """A boolean child, read as ShapeChange reads it: Java-trimmed, ``true`` in any case,
        or ``1``. A value outside ``xs:boolean`` is reported."""
        raw = self.text(element, tag)
        if raw is None:
            return default
        value = java_trim(raw)
        if value not in ("true", "false", "1", "0"):
            self.issue("DIFFERENT", "export-value", subject,
                       f"<{tag}> {raw!r} is not an xs:boolean")
        return value.lower() == "true" or value == "1"

    def register(self, kind: str, element_id: str | None, subject: str) -> str:
        if not element_id:
            self.anonymous += 1
            self.issue("DIFFERENT", "export-id", subject, f"a {kind} without an id")
            return f"<{kind} without an id #{self.anonymous}>"
        self.ids[kind][element_id] += 1
        return element_id

    # -- content -----------------------------------------------------------------------

    def stereotypes(self, element: ET.Element, subject: str) -> frozenset:
        return frozenset(normalize_stereotype(s)
                         for s in self.strings(element, "stereotypes", subject))

    def tags(self, element: ET.Element, subject: str) -> dict:
        raw: dict = {}
        names: Counter = Counter()
        for tag in self.items(element, "taggedValues", "TaggedValue"):
            name = self.text(tag, "name") or ""
            names[name] += 1
            holder = self.last(tag, "values")
            values = [v.text or "" for v in holder] if holder is not None else []
            for value in values or [""]:
                add_tag(raw, name, value)
        for name, count in sorted(names.items()):
            if count > 1:
                self.issue("EXTRA", "export-element", subject,
                           f"tagged value {name!r} appears {count} times")
        return split_tags(raw)[0]

    def descriptors(self, element: ET.Element, subject: str) -> dict:
        """Every descriptor kind present, as value lists; languages and repeats reported."""
        found = {}
        holder = self.last(element, "descriptors")
        if holder is None:
            return found
        for descriptor in holder:
            kind = _local(descriptor)
            values = self.items(descriptor, "descriptorValues", "DescriptorValue")
            for value in values:
                if value.get("lang"):
                    self.issue("EXTRA", "export-descriptor", subject,
                               f"{kind} value in language {value.get('lang')!r}")
            texts = [value.text for value in values if value.text is not None]
            if kind in NOTE_DESCRIPTORS and len(texts) > 1:
                self.issue("EXTRA", "export-descriptor", subject,
                           f"{kind} has {len(texts)} values {texts!r}; the model has one, and "
                           "ShapeChange uses the first")
            found[kind] = texts
        return found

    def constraints(self, element: ET.Element, owner: str) -> None:
        for constraint in self.items(element, "constraints", tuple(CONSTRAINT_KINDS)):
            self.model.constraints[owner].append({
                "name": self.text(constraint, "name") or "",
                "kind": _local(constraint),
                "type": self.text(constraint, "type"),
                "source_type": self.text(constraint, "sourceType"),
                "descriptions": len(constraint.findall(_q("description"))),
                "status": self.text(constraint, "status") or None,
                "text": self.text(constraint, "text") or ""})

    def property(self, element: ET.Element, owner: str | None) -> dict:
        pid = self.register("Property", self.text(element, "id"), "property")
        subject = f"property {pid}"
        self.validate(element, "Property", subject)
        sequence = self.text(element, "sequenceNumber")
        position = parse_sequence(sequence)
        if sequence is None:
            self.issue("DIFFERENT", "property-sequence-number", subject,
                       "no sequenceNumber (the SCXML schema requires one)")
        elif position is None or sequence != sequence.strip():
            self.issue("DIFFERENT", "property-sequence-number", subject,
                       f"{sequence!r} is not a sequence number as ShapeChange parses one")
        qualifiers = tuple((self.text(q, "name") or "", self.text(q, "type") or "")
                           for q in self.items(element, "qualifiers", "Qualifier"))
        inline_or_ref = self.text(element, "inlineOrByReference")
        descriptors = self.descriptors(element, subject)
        fields = {
            "id": pid,
            "name": self.text(element, "name") or "",
            "stereotypes": self.stereotypes(element, subject),
            "tags": self.tags(element, subject),
            "descriptors": descriptors,
            "multiplicity": parse_cardinality(self.text(element, "cardinality")),
            "navigable": self.flag(element, "isNavigable", True, subject),
            "is_attribute": self.flag(element, "isAttribute", True, subject),
            "composition": self.flag(element, "isComposition", False, subject),
            "shared": self.flag(element, "isAggregation", False, subject),
            "ordered": self.flag(element, "isOrdered", False, subject),
            "unique": self.flag(element, "isUnique", True, subject),
            "read_only": self.flag(element, "isReadOnly", False, subject),
            "derived": self.flag(element, "isDerived", False, subject),
            "owned": self.flag(element, "isOwned", False, subject),
            "initial_value": self.text(element, "initialValue"),
            "position": position,
            "type_id": self.text(element, "typeId"),
            "type_name": self.text(element, "typeName") or None,
            "in_class": self.text(element, "inClassId"),
            "association_id": self.text(element, "associationId"),
            "qualifiers": qualifiers,
            # ShapeChange never writes the default; its targets compare the value exactly.
            "containment": None if inline_or_ref in (None, "inlineOrByReference")
            else inline_or_ref,
            "owner": owner,
        }
        self.constraints(element, pid)
        return fields

    def package(self, element: ET.Element, parent: str | None) -> None:
        pid = self.register("Package", self.text(element, "id"), "package")
        subject = f"package {pid}"
        self.validate(element, "Package", subject)
        descriptors = self.descriptors(element, subject)
        self.model.packages[pid] = Package(
            id=pid,
            name=self.text(element, "name") or "",
            parent=parent,
            stereotypes=self.stereotypes(element, subject),
            tags=self.tags(element, subject),
            descriptors=descriptors,
        )
        # ShapeChange's package reader loads a Class and a Package wherever they appear in
        # the package's lists; validate() has reported any that is not in its canonical list.
        for container in ("classes", "packages"):
            for child in self.items(element, container, ("Class", "Package")):
                if _local(child) == "Class":
                    self.classifier(child, pid)
                else:
                    self.package(child, pid)

    def classifier(self, element: ET.Element, package: str) -> None:
        cid = self.register("Class", self.text(element, "id"), "class")
        subject = f"class {cid}"
        self.validate(element, "Class", subject)
        self.model.classifiers[cid] = Classifier(
            id=cid,
            name=self.text(element, "name") or "",
            kind=None,
            package=package,
            abstract=self.flag(element, "isAbstract", False, subject),
            leaf=self.flag(element, "isLeaf", False, subject),
            stereotypes=self.stereotypes(element, subject),
            tags=self.tags(element, subject),
            descriptors=self.descriptors(element, subject),
            supertypes=self.strings(element, "supertypes", subject),
            subtypes=self.strings(element, "subtypes", subject),
        )
        self.constraints(element, cid)
        for prop in self.items(element, "properties", "Property"):
            fields = self.property(prop, cid)
            self.properties[fields["id"]] = fields

    def association(self, element: ET.Element) -> None:
        aid = self.register("Association", self.text(element, "id"), "association")
        subject = f"association {aid}"
        self.validate(element, "Association", subject)
        ends = {}
        for position, tag in (("S", "end1"), ("T", "end2")):
            end_element = self.last(element, tag)
            end_subject = f"{subject} <{tag}>"
            if end_element is None:
                self.issue("MISSING", "end", end_subject, f"no <{tag}>")
                continue
            self.validate(end_element, "end", end_subject)
            ref = end_element.get("ref")
            inline = self.last(end_element, "Property")
            if ref and inline is not None:
                self.issue("DIFFERENT", "end", end_subject,
                           f"<{tag}> has both a ref and an inline property")
            if ref:
                fields = self.properties.get(ref)
                if fields is None:
                    self.issue("MISSING", "end", end_subject,
                               f"<{tag} ref={ref!r}> names no class property")
                    continue
                owner = fields["owner"]
                if fields["in_class"] is not None:
                    self.issue("DIFFERENT", "end-owner", end_subject,
                               f"property {ref} is in class {owner} and also names inClassId "
                               f"{fields['in_class']}")
                if not fields["navigable"]:
                    self.issue("DIFFERENT", "end-placement", end_subject,
                               f"non-navigable end {ref} is a property of class {owner}; "
                               "ShapeChange's reader removes it from the class")
            elif inline is not None:
                fields = self.property(inline, None)
                owner = fields["in_class"]
                if owner is None:
                    self.issue("MISSING", "end-owner", end_subject,
                               "an inline end without inClassId")
                if fields["navigable"]:
                    self.issue("DIFFERENT", "end-placement", end_subject,
                               f"navigable end {fields['id']} is written inline; ShapeChange's "
                               "reader does not add it to its class")
            else:
                self.issue("MISSING", "end", end_subject, f"<{tag}> is empty")
                continue
            self.references[fields["id"]] += 1
            if fields["is_attribute"]:
                self.issue("DIFFERENT", "end", end_subject,
                           f"property {fields['id']} is an attribute, not an association end")
            # The end's side is stated by its id; the position only when the id does not.
            side = next((s for s in ("S", "T") if fields["id"] == f"{s}{aid}"), position)
            if side in ends:
                self.issue("DIFFERENT", "end", end_subject, f"a second {side} end")
                continue
            if side != position:
                self.issue("DIFFERENT", "end-placement", end_subject,
                           f"<{tag}> holds the {side} end; ShapeChange writes the S end as "
                           "end1 and the T end as end2")
            ends[side] = End(
                id=fields["id"],
                association_id=fields["association_id"],
                role=fields["name"] or None,
                multiplicity=fields["multiplicity"],
                navigable=fields["navigable"],
                ordered=fields["ordered"],
                unique=fields["unique"],
                derived=fields["derived"],
                owned=fields["owned"],
                read_only=fields["read_only"],
                qualifiers=fields["qualifiers"],
                containment=fields["containment"],
                initial_value=fields["initial_value"],
                stereotypes=fields["stereotypes"],
                tags=fields["tags"],
                descriptors=fields["descriptors"],
                composition=fields["composition"],
                shared=fields["shared"],
                owner=owner,
                type_id=fields["type_id"],
                type_name=fields["type_name"],
            )
        self.model.associations[aid] = Association(
            id=aid,
            source=ends["S"].type_id if "S" in ends else None,
            target=ends["T"].type_id if "T" in ends else None,
            name=self.text(element, "name"),
            stereotypes=self.stereotypes(element, subject),
            tags=self.tags(element, subject),
            descriptors=self.descriptors(element, subject),
            ends=ends,
        )

    def finish(self) -> Model:
        model = self.model
        for kind, counts in self.ids.items():
            for element_id, count in sorted(counts.items()):
                if count > 1:
                    self.issue("EXTRA", "duplicate-id", f"{kind.lower()} {element_id}",
                               f"{count} elements share this id; the SCXML schema requires "
                               "unique ids")
        for pid, fields in self.properties.items():
            if fields["is_attribute"]:
                if self.references[pid]:
                    continue  # reported as an end that is an attribute
                model.attributes[pid] = Attribute(
                    id=pid,
                    owner=fields["owner"],
                    name=fields["name"],
                    type_id=fields["type_id"],
                    type_name=fields["type_name"],
                    multiplicity=fields["multiplicity"],
                    initial_value=fields["initial_value"],
                    stereotypes=fields["stereotypes"],
                    tags=fields["tags"],
                    descriptors=fields["descriptors"],
                    position=fields["position"],
                    read_only=fields["read_only"],
                    ordered=fields["ordered"],
                    unique=fields["unique"],
                    derived=fields["derived"],
                    containment=fields["containment"],
                    composition=fields["composition"],
                    shared=fields["shared"],
                    owned=fields["owned"],
                    navigable=fields["navigable"],
                    qualifiers=fields["qualifiers"],
                    in_class=fields["in_class"],
                    association_id=fields["association_id"],
                )
            elif self.references[pid] == 0:
                self.issue("EXTRA", "property", f"property {pid} in class {fields['owner']}",
                           "a role property no association end uses")
        for pid, count in sorted(self.references.items()):
            if count > 1:
                self.issue("DIFFERENT", "property", f"property {pid}",
                           f"used by {count} association ends")
        # Two properties of one class with the same number collapse into one when ShapeChange
        # reads this file back, which keys a class's properties by sequence number.
        numbers = Counter((f["owner"], f["position"]) for f in self.properties.values()
                          if f["position"] is not None)
        for (owner, number), count in sorted(numbers.items(), key=str):
            if count > 1:
                self.issue("DIFFERENT", "property-sequence-number", f"class {owner}",
                           f"{count} properties share sequenceNumber "
                           f"{'.'.join(map(str, number))}")
        return model


def _note_descriptors(model_item) -> None:
    """Copy documentation/definition/alias out of an export item's descriptor lists: the first
    value, as ShapeChange takes it (``InfoImpl.java:507-531``)."""
    for kind in NOTE_DESCRIPTORS:
        values = model_item.descriptors.get(kind) or []
        setattr(model_item, kind, values[0] if values else None)


def read_scxml(path: Path) -> Model:
    """Read a ShapeChange SCXML export, accounting for everything it contains."""
    root = ET.parse(path).getroot()
    reader = _ScxmlReader()
    reader.validate(root, "Model", "model")
    for package in reader.items(root, "packages", "Package"):
        reader.package(package, None)
    for association in reader.items(root, "associations", "Association"):
        reader.association(association)
    model = reader.finish()
    for collection in (model.packages, model.classifiers, model.attributes):
        for item in collection.values():
            _note_descriptors(item)
    for association in model.associations.values():
        _note_descriptors(association)
        for end in association.ends.values():
            _note_descriptors(end)
    return model


# ---------------------------------------------------------------------------------------
# The comparison


@dataclass(frozen=True, order=True)
class Finding:
    verdict: str
    rule: str
    subject: str
    detail: str

    @property
    def key(self) -> str:
        return f"{self.rule} :: {self.subject} :: {self.detail}"


def _show(value) -> str:
    if value is None:
        return "(none)"
    if isinstance(value, (set, frozenset)):
        return "{" + ", ".join(sorted(value)) + "}" if value else "{}"
    return repr(value) if isinstance(value, str) else str(value)


class _Report:
    def __init__(self) -> None:
        self.findings: list[Finding] = []

    def add(self, verdict: str, rule: str, subject: str, detail: str) -> None:
        if rule not in RULES:
            raise AssertionError(f"rule {rule!r} is not declared in RULES")
        self.findings.append(Finding(verdict, rule, subject, detail))

    def value(self, rule: str, subject: str, model_value, export_value) -> None:
        """Compare one value; ``None`` on one side is absence, not a value."""
        if model_value == export_value:
            return
        if export_value is None:
            self.add("MISSING", rule, subject, _show(model_value))
        elif model_value is None:
            self.add("EXTRA", rule, subject, _show(export_value))
        else:
            self.add("DIFFERENT", rule, subject,
                     f"model {_show(model_value)} | export {_show(export_value)}")

    def stereotypes(self, rule: str, subject: str, model: frozenset, export: frozenset) -> None:
        for name in sorted(model - export):
            self.add("MISSING", rule, subject, name)
        for name in sorted(export - model):
            self.add("EXTRA", rule, subject, name)

    def tags(self, rule: str, subject: str, model: dict, export: dict) -> None:
        def show(values: Counter) -> str:
            return ", ".join(f"{v!r}" + (f" x{n}" if n > 1 else "")
                             for v, n in sorted(values.items()))
        for name in sorted(set(model) | set(export)):
            ours, theirs = model.get(name), export.get(name)
            if ours == theirs:
                continue
            if theirs is None:
                self.add("MISSING", rule, subject, f"{name} = {show(ours)}")
            elif ours is None:
                self.add("EXTRA", rule, subject, f"{name} = {show(theirs)}")
            else:
                self.add("DIFFERENT", rule, subject,
                         f"{name}: model {show(ours)} | export {show(theirs)}")

    def documentation(self, prefix: str, subject: str, ours, theirs) -> None:
        self.value(f"{prefix}-documentation", subject, ours.documentation, theirs.documentation)
        self.value(f"{prefix}-alias", subject, ours.alias, theirs.alias)
        # The definition is derived from the export's own documentation; checking it against
        # the model's would report one documentation difference twice.
        expected = java_trim(theirs.documentation) if theirs.documentation else None
        if theirs.definition != expected:
            self.add("DIFFERENT", f"{prefix}-definition", subject,
                     f"definition {_show(theirs.definition)} is not the trimmed "
                     f"documentation {_show(expected)}")
        for target in ours.links:
            if not theirs.documentation or target not in theirs.documentation:
                self.add("MISSING", f"{prefix}-documentation-link", subject, target)
        for kind in TAG_DESCRIPTORS + UNSOURCED_DESCRIPTORS:
            exported = sorted(theirs.descriptors.get(kind) or []) or None
            self.value(f"{prefix}-descriptor", f"{subject} {kind}",
                       ours.descriptors.get(kind), exported)


def _is_enumeration(classifier: Classifier | None) -> bool:
    if classifier is None:
        return False
    return classifier.kind == "Enumeration" or bool(
        {"enumeration", "codelist"} & classifier.stereotypes)


def _derived_classifier_stereotypes(classifier: Classifier) -> frozenset:
    """The stereotype ShapeChange adds for EA's ``Enumeration`` and ``DataType`` kinds."""
    added = set()
    stated = classifier.stereotypes
    if classifier.kind == "Enumeration" and not {"enumeration", "codelist"} & stated:
        added.add("enumeration")
    if classifier.kind == "DataType" and not {"datatype", "union", "enumeration"} & stated:
        added.add("datatype")
    return stated | added


def _unnamed(role: str | None) -> bool:
    """ShapeChange treats a blank role, and one named ``role_…``, as unnamed."""
    return role is None or role.startswith("role_")


def compare(model: Model, export: Model) -> list[Finding]:
    """Every difference between an EA model and its SCXML export, sorted.

    Raises :class:`VacuousComparison` when there is nothing to compare.
    """
    if not model.classifiers or not export.classifiers:
        raise VacuousComparison(
            f"nothing to compare: the EA model has {len(model.classifiers)} classifiers and the "
            f"export has {len(export.classifiers)}")
    if not set(model.classifiers) & set(export.classifiers):
        raise VacuousComparison("the EA model and the export share no classifier id; "
                                "they are not the same model")

    report = _Report()
    for verdict, rule, subject, detail in export.issues:
        report.add(verdict, rule, subject, detail)

    names = {cid: c.name for cid, c in model.classifiers.items()}
    names.update({oid: name for oid, (_, name, _) in model.other_elements.items()})
    by_name: dict[str, list] = defaultdict(list)
    for cid, classifier in model.classifiers.items():
        by_name[classifier.name].append(cid)
    owned = Counter(a.owner for a in model.attributes.values())

    def label(cid: str | None) -> str:
        return names.get(cid, "?") if cid else "?"

    def with_attributes(oid: str) -> str:
        return f", with {owned[oid]} attributes" if owned[oid] else ""

    _compare_packages(report, model, export)
    _compare_classifiers(report, model, export, label, with_attributes)
    _compare_generalizations(report, model, export, label, by_name)
    _compare_attributes(report, model, export, label, by_name)
    _compare_associations(report, model, export, label)
    _compare_constraints(report, model, export, label)
    for oid, (owner, name) in sorted(model.operations.items()):
        report.add("MISSING", "operation", f"{owner} {label(owner)} [{oid}]",
                   f"{name} (the SCXML has no operations)")
    return sorted(set(report.findings))


def _compare_packages(report: _Report, model: Model, export: Model) -> None:
    for pid, ours in model.packages.items():
        subject = f"{pid} {ours.name}"
        theirs = export.packages.get(pid)
        if theirs is None:
            report.add("MISSING", "package", subject, "not exported")
            continue
        report.value("package-name", subject, ours.name, theirs.name)
        report.value("package-parent", subject, ours.parent, theirs.parent)
        report.stereotypes("package-stereotype", subject, ours.stereotypes, theirs.stereotypes)
        report.tags("package-tag", subject, ours.tags, theirs.tags)
        report.documentation("package", subject, ours, theirs)
        if (ours.visibility or "Public") != "Public":
            report.add("MISSING", "package-visibility", subject,
                       f"{ours.visibility} (the SCXML has no visibility)")
        for fact in ours.unrepresentable:
            report.add("MISSING", "package-unrepresentable", subject, fact)
        if ours.element_note and ours.element_note != ours.documentation:
            report.add("MISSING", "package-element-note", subject,
                       f"the package element's own note {ours.element_note!r} (ShapeChange "
                       "reads only t_package.Notes)")
    for pid in sorted(set(export.packages) - set(model.packages)):
        report.add("EXTRA", "package", f"{pid} {export.packages[pid].name}", "not in the model")


def _compare_classifiers(report: _Report, model: Model, export: Model, label,
                         with_attributes) -> None:
    for cid, ours in model.classifiers.items():
        subject = f"{cid} {ours.name}"
        theirs = export.classifiers.get(cid)
        if theirs is None:
            if ours.parent:
                report.add("MISSING", "nested-classifier", subject,
                           f"owned by classifier {ours.parent} {label(ours.parent)}"
                           f"{with_attributes(cid)}")
            else:
                report.add("MISSING", "classifier", subject,
                           f"{ours.kind} not exported{with_attributes(cid)}")
            continue
        report.value("classifier-name", subject, ours.name, theirs.name)
        report.value("classifier-package", subject, ours.package, theirs.package)
        if ours.parent:
            report.add("DIFFERENT", "classifier-owner", subject,
                       f"model: owned by classifier {ours.parent} {label(ours.parent)} | "
                       f"export: owned by package {theirs.package}")
        report.value("classifier-abstract", subject, ours.abstract, theirs.abstract)
        report.value("classifier-leaf", subject, ours.leaf, theirs.leaf)
        if ours.kind == "Interface":
            report.add("MISSING", "classifier-kind", subject,
                       "Interface (the SCXML has no classifier kind)")
        if (ours.visibility or "Public") != "Public":
            report.add("MISSING", "classifier-visibility", subject,
                       f"{ours.visibility} (the SCXML has no visibility)")
        for fact in ours.unrepresentable:
            report.add("MISSING", "classifier-unrepresentable", subject, fact)
        report.stereotypes("classifier-stereotype", subject,
                           _derived_classifier_stereotypes(ours), theirs.stereotypes)
        report.tags("classifier-tag", subject, ours.tags, theirs.tags)
        report.documentation("classifier", subject, ours, theirs)
    for oid, (kind, name, detail) in sorted(model.other_elements.items()):
        report.add("MISSING", "element-type", f"{oid} {name}",
                   f"{kind}{detail}{with_attributes(oid)} (ShapeChange exports only "
                   f"{', '.join(sorted(EXPORTABLE_KINDS))})")
    for cid in sorted(set(export.classifiers) - set(model.classifiers)):
        report.add("EXTRA", "classifier", f"{cid} {export.classifiers[cid].name}",
                   "not in the model")


def _compare_generalizations(report: _Report, model: Model, export: Model, label,
                             by_name) -> None:
    exported = Counter((cid, sup) for cid, c in export.classifiers.items() for sup in c.supertypes)
    used: Counter = Counter()

    def take(pair: tuple) -> bool:
        if exported.get(pair, 0) > used[pair]:
            used[pair] += 1
            return True
        return False

    for cid, gen in sorted(model.generalizations.items()):
        pair = (gen["sub"], gen["super"])
        subject = f"{pair[0]} {label(pair[0])} -> {pair[1]} {label(pair[1])} [connector {cid}]"
        if not take(pair):
            report.add("MISSING", "generalization", subject, "not exported")
        for name in sorted(gen["stereotypes"]):
            report.add("MISSING", "generalization-stereotype", subject,
                       f"{name} (the SCXML has no generalization stereotypes)")
        for name, values in sorted(gen["tags"].items()):
            report.add("MISSING", "generalization-tag", subject,
                       f"{name} = {sorted(values.elements())}")
        if gen["documentation"]:
            report.add("MISSING", "generalization-documentation", subject, gen["documentation"])
        for fact in gen["unrepresentable"]:
            report.add("MISSING", "generalization-unrepresentable", subject, fact)

    # EA's generalizations by name (t_object.GenLinks). One that names a model classifier is
    # satisfied by a supertype in the export; the export reads none today.
    for cid, classifier in sorted(model.classifiers.items()):
        if cid not in export.classifiers:
            continue
        for rule, names_ in (("generalization-by-name", classifier.parents_by_name),
                             ("realization-by-name", classifier.implements_by_name)):
            occurrences = Counter(names_)
            seen: Counter = Counter()
            for name in names_:
                seen[name] += 1
                targets = by_name.get(name, [])
                nth = f" [{seen[name]} of {occurrences[name]}]" if occurrences[name] > 1 else ""
                key = "Parent" if rule == "generalization-by-name" else "Implements"
                if len(targets) == 1 and take((cid, targets[0])):
                    if rule == "realization-by-name":
                        report.add("DIFFERENT", rule, f"{cid} {classifier.name}",
                                   f"{key}={name} is exported as a generalization{nth}")
                    continue
                where = (f"classifier {', '.join(targets)}" if targets
                         else "no model classifier of that name")
                report.add("MISSING", rule, f"{cid} {classifier.name}",
                           f"{key}={name} ({where}; EA's t_object.GenLinks, which the export "
                           f"does not read){nth}")

    for cid, real in sorted(model.realizations.items()):
        pair = (real["client"], real["supplier"])
        subject = f"{pair[0]} {label(pair[0])} -> {pair[1]} {label(pair[1])} [connector {cid}]"
        facts = f", with {', '.join(real['facts'])}" if real["facts"] else ""
        if take(pair):
            report.add("DIFFERENT", "realization", subject,
                       f"exported as a generalization{facts}")
        else:
            report.add("MISSING", "realization", subject,
                       f"the SCXML has no realizations{facts}")
    for pair, count in sorted(exported.items()):
        for _ in range(count - used[pair]):
            report.add("EXTRA", "generalization", f"{pair[0]} -> {pair[1]}", "not in the model")
    # ShapeChange writes each generalization twice, as a supertype and as a subtype, and reads
    # both as sets (GenericClassContentHandler.java:228-235).
    for cid, classifier in sorted(export.classifiers.items()):
        inverse = sorted({sub for sub, c in export.classifiers.items() if cid in c.supertypes})
        if sorted(set(classifier.subtypes)) != inverse:
            report.add("DIFFERENT", "subtypes", f"{cid} {label(cid)}",
                       f"subtypes {sorted(set(classifier.subtypes))} do not mirror the "
                       f"supertypes that name it {inverse}")
    for cid, (kind, source, target) in sorted(model.other_connectors.items()):
        report.add("MISSING", "connector-type", f"{cid} {label(source)} -> {label(target)}",
                   f"{kind} connector")
    for cid, kind, side, name, values in model.other_connector_end_tags:
        report.add("MISSING", "connector-end-tag", f"{kind} connector {cid} [{side}]",
                   f"{name} = {values}")


def _compare_attributes(report: _Report, model: Model, export: Model, label, by_name) -> None:
    for aid, ours in model.attributes.items():
        owner = model.classifiers.get(ours.owner)
        subject = f"{label(ours.owner)}.{ours.name} [{aid}]"
        theirs = export.attributes.get(aid)
        if theirs is None:
            if ours.owner in export.classifiers:
                report.add("MISSING", "attribute", subject, "not exported")
            elif ours.owner not in model.classifiers and ours.owner not in model.other_elements:
                report.add("MISSING", "attribute", subject,
                           f"owner {ours.owner} is not a model element")
            continue  # otherwise the owner's own finding counts it
        enumeration = _is_enumeration(owner)
        report.value("attribute-name", subject, ours.name, theirs.name)
        report.value("attribute-owner", subject, ours.owner, theirs.owner)
        if theirs.in_class is not None or theirs.association_id is not None:
            report.add("DIFFERENT", "attribute-owner", subject,
                       f"an attribute with inClassId {theirs.in_class} / associationId "
                       f"{theirs.association_id}")
        _compare_attribute_type(report, subject, ours, theirs, export, by_name)
        report.value("attribute-multiplicity", subject, show_multiplicity(ours.multiplicity),
                     show_multiplicity(theirs.multiplicity))
        report.value("attribute-initial-value", subject, ours.initial_value,
                     theirs.initial_value)
        report.value("attribute-read-only", subject, ours.read_only, theirs.read_only)
        report.value("attribute-derived", subject, ours.derived, theirs.derived)
        report.value("attribute-ordered", subject, ours.ordered, theirs.ordered)
        report.value("attribute-unique", subject, ours.unique, theirs.unique)
        report.value("attribute-containment", subject, ours.containment, theirs.containment)
        report.value("attribute-composition", subject, not enumeration, theirs.composition)
        report.value("attribute-aggregation", subject, False, theirs.shared)
        report.value("attribute-owned", subject, False, theirs.owned)
        report.value("attribute-navigable", subject, True, theirs.navigable)
        report.value("attribute-qualifiers", subject, None, theirs.qualifiers or None)
        if ours.literal is not None and ours.literal != enumeration:
            report.add("DIFFERENT", "attribute-literal", subject,
                       f"model: {'an' if ours.literal else 'not an'} enumeration literal "
                       f"(IsLiteral={int(ours.literal)}) | export: "
                       + ("a literal, as a member of an enumeration" if enumeration
                          else "an attribute"))
        if (ours.visibility or "Public") != "Public":
            report.add("MISSING", "attribute-visibility", subject,
                       f"{ours.visibility} (the SCXML has no visibility)")
        for fact in ours.unrepresentable:
            report.add("MISSING", "attribute-unrepresentable", subject, fact)
        report.stereotypes("attribute-stereotype", subject, ours.stereotypes,
                           theirs.stereotypes)
        report.tags("attribute-tag", subject, ours.tags, theirs.tags)
        report.documentation("attribute", subject, ours, theirs)
    for aid in sorted(set(export.attributes) - set(model.attributes)):
        theirs = export.attributes[aid]
        report.add("EXTRA", "attribute", f"{label(theirs.owner)}.{theirs.name} [{aid}]",
                   "not in the model")

    # Attribute order: within a class, the export must follow EA's order (Pos, then name, or a
    # sequenceNumber tag). Every inverted pair is its own finding, so two different wrong
    # orders never share a key set.
    def place(key: tuple) -> str:
        if key[0] == 1:
            return f"sequenceNumber tag {'.'.join(map(str, key[1]))}"
        return f"Pos {key[1]:g}"

    by_owner: dict[str, list] = defaultdict(list)
    for aid, theirs in export.attributes.items():
        ours = model.attributes.get(aid)
        if ours is not None and theirs.position is not None:
            by_owner[theirs.owner].append((theirs.position, ours.position, ours.name))
    for owner, entries in sorted(by_owner.items()):
        entries.sort()
        for i, (_, earlier_key, earlier) in enumerate(entries):
            for _, later_key, later in entries[i + 1:]:
                if later_key < earlier_key:
                    report.add("DIFFERENT", "attribute-order", f"{owner} {label(owner)}",
                               f"{later} ({place(later_key)}) is exported after {earlier} "
                               f"({place(earlier_key)})")


def _compare_attribute_type(report: _Report, subject: str, ours: Attribute, theirs: Attribute,
                            export: Model, by_name) -> None:
    """An attribute's type, where EA and ShapeChange each have their own fallbacks.

    EA binds the type by classifier id. When that id names no exported class, ShapeChange
    binds it by name, to the class of that name; when there is none, only the name survives.
    The ``typeName`` of a bound type is the class's name.
    """
    if ours.type_id is not None and ours.type_id in export.classifiers:
        candidates = [ours.type_id]
    else:
        candidates = [cid for cid in by_name.get(ours.type_name or "", ())
                      if cid in export.classifiers]
    if len(candidates) > 1 and theirs.type_id in candidates:
        expected = theirs.type_id
    else:
        expected = candidates[0] if len(candidates) == 1 else None
    report.value("attribute-type", subject, expected, theirs.type_id)
    bound = export.classifiers.get(expected) if expected else None
    report.value("attribute-type-name", subject, bound.name if bound else ours.type_name,
                 theirs.type_name)


def _compare_associations(report: _Report, model: Model, export: Model, label) -> None:
    for aid, ours in model.associations.items():
        subject = f"{aid} {label(ours.source)} -> {label(ours.target)}"
        theirs = export.associations.get(aid)
        foreign = [c for c in (ours.source, ours.target)
                   if c not in model.classifiers and c not in model.other_elements]
        if foreign:
            report.add("DIFFERENT", "association-endpoint", subject,
                       f"end {', '.join(foreign)} is not a model element")
        if theirs is None:
            missing_ends = [f"{c} {label(c)}" for c in (ours.source, ours.target)
                            if c not in export.classifiers]
            cause = (f"end classifier {', '.join(missing_ends)} is not exported"
                     if missing_ends else "not exported")
            report.add("MISSING", "association", subject, cause)
            continue
        report.value("association-endpoint", subject, (ours.source, ours.target),
                     (theirs.source, theirs.target))
        expected_name = ours.name if ours.name is not None else \
            f"{label(ours.source)}_{label(ours.target)}"
        report.value("association-name", subject, expected_name, theirs.name)
        report.stereotypes("association-stereotype", subject, ours.stereotypes,
                           theirs.stereotypes)
        report.tags("association-tag", subject, ours.tags, theirs.tags)
        report.documentation("association", subject, ours, theirs)
        for fact in ours.unrepresentable:
            report.add("MISSING", "association-unrepresentable", subject, fact)
        for side in ("S", "T"):
            _compare_end(report, subject, aid, side, ours, theirs, model, label)
    for aid in sorted(set(export.associations) - set(model.associations)):
        report.add("EXTRA", "association", aid, "not in the model")


def _compare_end(report: _Report, subject: str, aid: str, side: str, ours: Association,
                 theirs: Association, model: Model, label) -> None:
    mine, exported = ours.ends.get(side), theirs.ends.get(side)
    end_subject = f"{subject} [{side}{aid}]"
    if exported is None:
        return  # the reader reported the missing end
    # The S end belongs to the target class and is typed by the source; the T end the reverse.
    owner, typed = (ours.target, ours.source) if side == "S" else (ours.source, ours.target)
    report.value("end-id", end_subject, f"{side}{aid}", exported.id)
    report.value("end-association-id", end_subject, aid, exported.association_id)
    report.value("end-owner", end_subject, owner, exported.owner)
    report.value("end-type-name", end_subject,
                 label(typed) if typed in model.classifiers else None, exported.type_name)
    expected_role = mine.role if mine.role else f"role_{side}{aid}"
    report.value("end-role", end_subject, expected_role, exported.role)
    report.value("end-multiplicity", end_subject, show_multiplicity(mine.multiplicity),
                 show_multiplicity(exported.multiplicity))

    # Navigability: an end the model states navigable or not must be exported as such. An end
    # it does not state gets ShapeChange's derived value.
    unnamed = _unnamed(mine.role)
    if mine.navigable is None:
        expected = not unnamed and (ours.direction or "Unspecified") in (
            "Unspecified", "Bi-Directional")
        if exported.navigable != expected:
            report.add("DIFFERENT", "end-navigability", end_subject,
                       f"unspecified in the model, derived {expected} | export "
                       f"{exported.navigable}")
    elif mine.navigable != exported.navigable:
        cause = " (the end is unnamed)" if unnamed else ""
        report.add("DIFFERENT", "end-navigability", end_subject,
                   f"model {'navigable' if mine.navigable else 'not navigable'} | export "
                   f"{'navigable' if exported.navigable else 'not navigable'}{cause}")

    # Aggregation: EA marks the whole at one end; the SCXML marks the opposite property - the
    # part - as composition or aggregation.
    whole = ours.ends.get("T" if side == "S" else "S")
    if exported.composition and exported.shared:
        report.add("DIFFERENT", "end-aggregation", end_subject,
                   "exported as both composition and shared aggregation")
    exported_kind = "composite" if exported.composition else (
        "shared" if exported.shared else "none")
    report.value("end-aggregation", end_subject, whole.aggregation if whole else "none",
                 exported_kind)
    report.value("end-ordered", end_subject, mine.ordered, exported.ordered)
    report.value("end-unique", end_subject, mine.unique, exported.unique)
    report.value("end-derived", end_subject, mine.derived, exported.derived)
    report.value("end-owned", end_subject, mine.owned, exported.owned)
    report.value("end-read-only", end_subject, mine.read_only, exported.read_only)
    report.value("end-qualifiers", end_subject, mine.qualifiers or None,
                 exported.qualifiers or None)
    report.value("end-containment", end_subject, mine.containment, exported.containment)
    report.value("end-initial-value", end_subject, None, exported.initial_value)
    if (mine.visibility or "Public") != "Public":
        report.add("MISSING", "end-visibility", end_subject,
                   f"{mine.visibility} (the SCXML has no visibility)")
    report.stereotypes("end-stereotype", end_subject, mine.stereotypes, exported.stereotypes)
    report.tags("end-tag", end_subject, mine.tags, exported.tags)
    report.documentation("end", end_subject, mine, exported)
    for fact in mine.unrepresentable:
        report.add("MISSING", "end-unrepresentable", end_subject, fact)


def _compare_constraints(report: _Report, model: Model, export: Model, label) -> None:
    for owner in sorted(set(model.constraints) | set(export.constraints)):
        subject = f"{owner} {label(owner.split('_')[0])}"
        remaining = list(export.constraints.get(owner, ()))
        ours_list = model.constraints.get(owner, [])
        occurrences = Counter(c["name"] for c in ours_list)
        seen: Counter = Counter()
        for ours in ours_list:
            seen[ours["name"]] += 1
            # Two constraints of one name on one owner are two model facts, not one.
            nth = (f" [{seen[ours['name']]} of {occurrences[ours['name']]}]"
                   if occurrences[ours["name"]] > 1 else "")
            same_name = [c for c in remaining if c["name"] == ours["name"]]
            match = next((c for c in same_name if c["text"] == ours["text"]),
                         same_name[0] if same_name else None)
            text = f" ({ours['text']!r})" if ours["text"] else ""
            if match is None:
                report.add("MISSING", "constraint", subject,
                           f"{ours['type']} {ours['name']!r}{text}{nth}")
                continue
            remaining.remove(match)
            named = f"{ours['name']!r}{nth}"
            if match["text"] != ours["text"]:
                report.add("DIFFERENT", "constraint", subject,
                           f"{named}: text model {ours['text']!r} | export {match['text']!r}")
            if match["status"] != ours["status"]:
                report.add("DIFFERENT", "constraint", subject,
                           f"{named}: status model {ours['status']!r} | export "
                           f"{match['status']!r}")
            kinds = expected_constraint_kinds(ours["type"], ours.get("attribute", False))
            if match["kind"] not in kinds:
                report.add("DIFFERENT", "constraint-kind", subject,
                           f"{named}: an EA {ours['type']!r} constraint is exported as "
                           f"{match['kind']}, not {' or '.join(sorted(kinds))}")
                continue
            # ShapeChange writes the EA type as a TextConstraint's type and as a FolConstraint's
            # sourceType, and neither on an OclConstraint (ModelWriter.java:446-496).
            expected_type = ours["type"] if match["kind"] == "TextConstraint" else None
            expected_source = ours["type"] if match["kind"] == "FolConstraint" else None
            if match["type"] != expected_type:
                report.add("DIFFERENT", "constraint-kind", subject,
                           f"{named}: type model {expected_type!r} | export {match['type']!r}")
            if match["source_type"] != expected_source:
                report.add("DIFFERENT", "constraint-kind", subject,
                           f"{named}: sourceType model {expected_source!r} | export "
                           f"{match['source_type']!r}")
            if match["descriptions"]:
                report.add("EXTRA", "constraint", subject,
                           f"{named}: {match['descriptions']} description(s)")
        for extra in remaining:
            report.add("EXTRA", "constraint", subject,
                       f"{extra['kind']} {extra['name']!r} status {extra['status']!r} text "
                       f"{extra['text']!r}")


def group(findings: list[Finding]) -> dict[str, list[str]]:
    """Finding keys by verdict, the shape a baseline is stored in."""
    grouped: dict[str, list[str]] = {verdict: [] for verdict in VERDICTS}
    for finding in findings:
        grouped[finding.verdict].append(finding.key)
    return {verdict: sorted(keys) for verdict, keys in grouped.items()}


def summarize(findings: list[Finding]) -> Counter:
    """Finding counts by (verdict, rule)."""
    return Counter((f.verdict, f.rule) for f in findings)
