#!/usr/bin/env python3
"""The OpenDRIVE XML Schema, derived from ASAM's EA project by EA's XML Schema profile.

ASAM states that the OpenDRIVE XSD schemas "are derived from the UML model" (OpenDRIVE V1.9.0,
clause 1). Unlike OpenSCENARIO, the project does not contain the generator that derives them.
It does apply Enterprise Architect's *UML profile for XML Schema*: ``XSDschema`` packages,
``XSDcomplexType``, ``XSDsimpleType``, ``XSDunion``, ``XSDgroup``, ``XSDchoice``, ``XSDany`` and
``XSDtopLevelElement`` classes, ``XSDattribute`` attributes, and the profile's tagged values.
It adds ASAM's own for what XSD 1.1 offers and the profile does not: identity constraints, type
alternatives, and assertions.

This module derives the schema from those constructs, one rule per construct, with no knowledge
of any particular class. The rules are reconstructed, not ported: where the normative schema
and a rule disagree, ``check_xsd_transformation.py`` reports the component, so a rule that is
wrong cannot pass unnoticed and a fact the model does not record cannot be supplied from
elsewhere. The counts below are those of the V1.9.0 project.

**Schemas.** Each ``XSDschema`` package is one schema document, named by the last path segment
of its ``schemaLocation`` tag, with the package's ``targetNamespace`` and ``elementFormDefault``
tags. It includes each other document one of its components refers to. When any document uses
an XSD 1.1 construct, an assertion or a type alternative, every document declares
``vc:minVersion="1.1"``, since the set is processed as one.

**Components**, in ``Package.Elements`` order:

- ``XSDtopLevelElement``: a global element of the class's name, whose anonymous complex type is
  the class nested in it, with every identity constraint that names no ``targetElement``;
- ``XSDcomplexType``: a complex type, ``abstract`` when the class is abstract and ``mixed``
  from the ``mixed`` tag. A generalization makes it a ``complexContent`` extension of the
  general class. Its content is the ``modelGroup`` tag's compositor over its particles, then its
  attributes, then one assertion per invariant, whose name is the test. A ``modelGroup`` that is
  not one of the profile's ``sequence``, ``choice`` or ``all`` is a sequence; 34 classes carry
  ``group``;
- ``XSDsimpleType``: a restriction of the general type by every facet tag with a value, or a
  list of it when ``derivation`` is ``list``;
- ``XSDunion``: a union of the general types;
- an EA ``Enumeration``, or a class stereotyped ``enumeration``: a restriction of
  ``xs:string`` to its literals;
- ``XSDgroup``: a named group whose content is built like a complex type's.

A general type is the target of a generalization, then each ``GenLinks`` ``Parent``, which is
how EA records a generalization to a type it has no element for (``double``).

**Particles**, in order: the class's attributes that are not ``XSDattribute``s, as elements
with their multiplicity as occurrence; then its outgoing associations, ordered by their
``position`` tag, an untagged one counting as -1, and otherwise in connector order. An
association is:

- a reference to an ``XSDgroup`` target;
- a nested compositor for an ``XSDchoice`` target: its ``modelGroup``, ``choice`` when unset,
  over the target's own particles;
- a wildcard for an ``XSDany`` target, with its ``processContents`` and ``namespace`` tags;
- otherwise an element named by the target role, or by the target class when the role is
  unnamed, and typed by the target class. Associations of one class that share a role are one
  element: ``t_junction_virtual`` draws ``connection`` once per type alternative.

Its occurrence is the target cardinality, 1..1 when unset. An element's type alternatives are
the classes tagged ``XSDAlternative_element`` with its name, and ``XSDAlternative_type`` with the
type it is declared in (none for the global element's content), ordered by
``XSDAlternative_nr``. ``XSDAlternative_test`` is the test, and an alternative without one is
the default. Such an element is declared with the alternatives' common general type.

**Attributes.** An ``XSDattribute`` is an ``xs:attribute`` with its ``default`` and ``fixed``
tags when they have a value, and its ``use`` tag, which is ``optional`` when unset. Its UML
multiplicity is not read: 76 attributes are 1..1 in the model and optional in the schema, and 4
are 0..1 and required. Its type is the class EA's classifier reference names; the XSD built-in
type of its type name when there is no reference; and ``xs:string`` when the name is a class's
but the reference is missing, as for 8 attributes.

**Identity constraints.** An attribute tagged ``key`` declares a key of that name, with the
attribute's ``selector`` tag and the attribute as its field; one tagged ``keyref`` declares a
reference to the key its ``refer`` tag names. Each is declared in the element its
``targetElement`` tag names, and in the global element otherwise.

**Documentation.** A class's, attribute's or literal's notes, as EA renders them as plain text,
are its ``xs:documentation``.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET

from ea_api import Connector, Element, Package, Repository, has_stereotype, tagged_value

XS = "http://www.w3.org/2001/XMLSchema"
VC = "http://www.w3.org/2007/XMLSchema-versioning"

#: The facets of a restriction, as the profile names its tags.
FACETS = ("length", "minLength", "maxLength", "pattern", "whiteSpace", "maxInclusive",
          "maxExclusive", "minExclusive", "minInclusive", "totalDigits", "fractionDigits")


#: The compositors the profile's ``modelGroup`` tag offers. Any other value, including
#: ``group`` (34 classes) and an unset tag, is a sequence.
COMPOSITORS = ("sequence", "choice", "all")


def compositor(element: Element, default: str = "sequence") -> str:
    value = tagged_value(element, "modelGroup")
    return value if value in COMPOSITORS else default


UNTAGGED = -1


def position_key(connector: Connector) -> int:
    value = tagged_value(connector, "position")
    try:
        return int(value) if value is not None else UNTAGGED
    except ValueError:
        return UNTAGGED


def q(name: str) -> str:
    return f"{{{XS}}}{name}"


class _Schema:
    """The model-wide lookups the rules need."""

    def __init__(self, repository: Repository, bindings: dict | None = None) -> None:
        self.repository = repository
        self.bindings = bindings
        self.by_name: dict[str, Element] = {}
        for element in repository.elements.values():
            if element.type in ("Class", "Enumeration", "DataType", "Interface") and element.name:
                self.by_name.setdefault(element.name, element)
        self.alternatives: dict[tuple[str, str | None], list[Element]] = {}
        for element in repository.elements.values():
            name = tagged_value(element, "XSDAlternative_element")
            if name:
                context = tagged_value(element, "XSDAlternative_type") or None
                self.alternatives.setdefault((name, context), []).append(element)
        #: Identity constraints by the element they are declared in; None is the global element.
        self.identity_constraints: dict[str | None, list[tuple]] = {}
        for owner in repository.elements.values():
            for attribute in owner.attributes:
                for kind in ("key", "keyref"):
                    name = tagged_value(attribute, kind)
                    if name:
                        target = tagged_value(attribute, "targetElement") or None
                        self.identity_constraints.setdefault(target, []).append(
                            (kind, name, tagged_value(attribute, "refer"),
                             tagged_value(attribute, "selector"), attribute.name))
        #: The package each class belongs to, to find cross-document references.
        self.package_of: dict[str, int] = {e.name: e.package_id for e in self.by_name.values()
                                           if e.package_id is not None}

    def bind(self, xsd_owner: str | None, name: str, *binding) -> None:
        """Record which UML property an emitted particle or attribute stands for."""
        if self.bindings is not None:
            self.bindings[(xsd_owner, name)] = binding

    def outgoing(self, element: Element, kind: str) -> list[Connector]:
        found = [c for c in element.connectors
                 if c.type == kind and c.client_id == element.element_id]
        if kind == "Association":
            found.sort(key=position_key)
        return found

    def target(self, connector: Connector) -> Element:
        return self.repository.get_element_by_id(connector.supplier_id)

    def type_name(self, name: str | None) -> str:
        """A model class by name, or else the XSD built-in type of that name."""
        if name and name in self.by_name:
            return name
        return f"xs:{name}"

    def attribute_type(self, attribute) -> str:
        """The class the attribute's type refers to; EA's built-in type of that name when it
        refers to none; and ``xs:string`` when the name is a class's but the reference is
        missing, since EA then resolves nothing."""
        if attribute.classifier_id in self.repository.elements:
            return self.repository.elements[attribute.classifier_id].name or ""
        if attribute.type in self.by_name:
            return "xs:string"
        return f"xs:{attribute.type}"

    def general_types(self, element: Element) -> list[str]:
        names = [self.target(c).name or "" for c in self.outgoing(element, "Generalization")]
        for entry in (element.gen_links or "").split(";"):
            key, _, value = entry.partition("=")
            if key.strip() == "Parent" and value.strip():
                names.append(value.strip())
        return [self.type_name(n) for n in names]


def _occurs(node: ET.Element, cardinality: str | None) -> None:
    text = (cardinality or "").strip()
    low, high = ("1", "1") if not text else (text.split("..", 1) if ".." in text
                                             else (text, text))
    node.set("minOccurs", low.strip())
    node.set("maxOccurs", "unbounded" if high.strip() == "*" else high.strip())


def _documentation(parent: ET.Element, text: str | None) -> None:
    if text is None:
        return
    annotation = ET.SubElement(parent, q("annotation"))
    ET.SubElement(annotation, q("documentation")).text = text


def _particles(schema: _Schema, owner: Element, group: ET.Element,
               context: str | None, xsd_owner: str | None) -> None:
    for attribute in owner.attributes:
        if not has_stereotype(attribute, "XSDattribute"):
            node = ET.SubElement(group, q("element"), name=attribute.name,
                                 type=schema.attribute_type(attribute))
            schema.bind(xsd_owner, attribute.name, "element", owner.name, attribute.name,
                        node.get("type"))
            node.set("minOccurs", attribute.lower_bound or "1")
            upper = attribute.upper_bound or "1"
            node.set("maxOccurs", "unbounded" if upper == "*" else upper)
            _documentation(node, attribute.notes_text)
    declared: set[str] = set()
    for connector in schema.outgoing(owner, "Association"):
        target = schema.target(connector)
        role = connector.supplier_end.role
        if role and role in declared:
            # A second association with the same role is the same element declaration.
            continue
        if role:
            declared.add(role)
        if has_stereotype(target, "XSDgroup"):
            node = ET.SubElement(group, q("group"), ref=target.name or "")
            _occurs(node, connector.supplier_end.cardinality)
            schema.bind(xsd_owner, f"group {target.name}", "group", owner.name, role,
                        target.name)
        elif has_stereotype(target, "XSDchoice"):
            node = ET.SubElement(group, q(compositor(target, "choice")))
            _occurs(node, connector.supplier_end.cardinality)
            schema.bind(xsd_owner, f"compositor {target.name}", "compositor", owner.name, role,
                        target.name)
            _particles(schema, target, node, context, xsd_owner)
        elif has_stereotype(target, "XSDany"):
            node = ET.SubElement(group, q("any"))
            _occurs(node, connector.supplier_end.cardinality)
            for tag in ("processContents", "namespace"):
                value = tagged_value(target, tag)
                if value:
                    node.set(tag, value)
        else:
            name = connector.supplier_end.role or target.name or ""
            node = ET.SubElement(group, q("element"), name=name, type=target.name or "")
            _occurs(node, connector.supplier_end.cardinality)
            schema.bind(xsd_owner, name, "element", owner.name, role, target.name)
            _alternatives(schema, node, name, context)
            for constraint in schema.identity_constraints.get(name, ()):
                _identity_constraint(node, *constraint)


def _alternatives(schema: _Schema, node: ET.Element, name: str, context: str | None) -> None:
    candidates = schema.alternatives.get((name, context), [])
    generals = {general for element in candidates for general in schema.general_types(element)}
    if len(generals) == 1:
        # An element with type alternatives is declared with their common general type.
        node.set("type", generals.pop())
    for element in sorted(candidates, key=lambda e: int(tagged_value(e, "XSDAlternative_nr")
                                                        or 0)):
        alternative = ET.SubElement(node, q("alternative"))
        test = tagged_value(element, "XSDAlternative_test")
        if test:
            alternative.set("test", test)
        alternative.set("type", element.name or "")


def _attributes(schema: _Schema, owner: Element, parent: ET.Element) -> None:
    for attribute in owner.attributes:
        if not has_stereotype(attribute, "XSDattribute"):
            continue
        node = ET.SubElement(parent, q("attribute"), name=attribute.name,
                             type=schema.attribute_type(attribute))
        schema.bind(owner.name, attribute.name, "attribute", owner.name, attribute.name,
                    node.get("type"))
        # The profile's default for an unset use is optional; the multiplicity is not read.
        node.set("use", tagged_value(attribute, "use") or "optional")
        for tag in ("default", "fixed"):
            value = tagged_value(attribute, tag)
            if value:
                node.set(tag, value)
        _documentation(node, attribute.notes_text)


def _content(schema: _Schema, element: Element, parent: ET.Element,
             context: str | None, xsd_owner: str | None) -> None:
    group = ET.SubElement(parent, q(compositor(element)))
    _particles(schema, element, group, context, xsd_owner)
    _attributes(schema, element, parent)
    for constraint in element.constraints:
        ET.SubElement(parent, q("assert"), test=constraint.name)


def complex_type(schema: _Schema, element: Element, parent: ET.Element,
                 named: bool = True) -> ET.Element:
    """A named complex type; or, with ``named`` false, the anonymous type of the global element,
    whose elements are the global context of ``XSDAlternative_type``."""
    context = element.name if named else None
    xsd_owner = element.name if named else parent.get("name")
    node = ET.SubElement(parent, q("complexType"))
    if named:
        node.set("name", element.name or "")
    if element.abstract:
        node.set("abstract", "true")
    if tagged_value(element, "mixed") == "true":
        node.set("mixed", "true")
    _documentation(node, element.notes_text)
    generals = schema.outgoing(element, "Generalization")
    if generals:
        extension = ET.SubElement(ET.SubElement(node, q("complexContent")), q("extension"),
                                  base=schema.target(generals[0]).name or "")
        _content(schema, element, extension, context, xsd_owner)
    else:
        _content(schema, element, node, context, xsd_owner)
    return node


def simple_type(schema: _Schema, element: Element, parent: ET.Element) -> None:
    node = ET.SubElement(parent, q("simpleType"), name=element.name or "")
    _documentation(node, element.notes_text)
    bases = schema.general_types(element)
    if tagged_value(element, "derivation") == "list":
        ET.SubElement(node, q("list"), itemType=bases[0] if bases else "")
        return
    restriction = ET.SubElement(node, q("restriction"), base=bases[0] if bases else "")
    for facet in FACETS:
        value = tagged_value(element, facet)
        if value:
            ET.SubElement(restriction, q(facet), value=value)


def union_type(schema: _Schema, element: Element, parent: ET.Element) -> None:
    node = ET.SubElement(parent, q("simpleType"), name=element.name or "")
    _documentation(node, element.notes_text)
    ET.SubElement(node, q("union"), memberTypes=" ".join(schema.general_types(element)))


def enumeration(element: Element, parent: ET.Element) -> None:
    node = ET.SubElement(parent, q("simpleType"), name=element.name or "")
    _documentation(node, element.notes_text)
    restriction = ET.SubElement(node, q("restriction"), base="xs:string")
    for literal in element.attributes:
        value = ET.SubElement(restriction, q("enumeration"), value=literal.name)
        _documentation(value, literal.notes_text)


def group(schema: _Schema, element: Element, parent: ET.Element) -> None:
    node = ET.SubElement(parent, q("group"), name=element.name or "")
    _documentation(node, element.notes_text)
    content = ET.SubElement(node, q(compositor(element)))
    _particles(schema, element, content, element.name, element.name)


def _identity_constraint(node: ET.Element, kind: str, name: str, refer: str | None,
                         selector: str | None, field: str) -> None:
    constraint = ET.SubElement(node, q(kind), name=name)
    if kind == "keyref":
        constraint.set("refer", refer or "")
    ET.SubElement(constraint, q("selector"), xpath=selector or "")
    ET.SubElement(constraint, q("field"), xpath=f"@{field}")


def top_level_element(schema: _Schema, element: Element, parent: ET.Element) -> None:
    node = ET.SubElement(parent, q("element"), name=element.name or "")
    for nested in element.elements:
        if has_stereotype(nested, "XSDcomplexType"):
            complex_type(schema, nested, node, named=False)
    for constraint in schema.identity_constraints.get(None, ()):
        _identity_constraint(node, *constraint)


def schema_packages(repository: Repository) -> list[Package]:
    found = []

    def walk(package: Package) -> None:
        if package.element is not None and has_stereotype(package.element, "XSDschema"):
            found.append(package)
        for sub in package.packages:
            walk(sub)

    for model in repository.models:
        walk(model)
    return found


def document_name(package: Package) -> str:
    location = tagged_value(package.element, "schemaLocation") or f"{package.name}.xsd"
    return location.rsplit("/", 1)[-1]


def _references(root: ET.Element) -> set[str]:
    """Every type, group and base name a schema document refers to."""
    names = set()
    for node in root.iter():
        for attribute in ("type", "base", "ref", "itemType"):
            if node.get(attribute):
                names.add(node.get(attribute))
        for member in (node.get("memberTypes") or "").split():
            names.add(member)
    return names


def documents(repository: Repository, errors: list | None = None,
              bindings: dict | None = None) -> list[tuple]:
    """Every schema document, as ``(package, file name, parsed schema, text)``. The rules raise
    nothing, so ``errors`` is accepted for the common interface and left empty."""
    names = {document_name(p): p.name for p in schema_packages(repository)}
    return [(names[file_name], file_name, root, None)
            for file_name, root in transform(repository, bindings).items()]


def transform(repository: Repository, bindings: dict | None = None) -> dict[str, ET.Element]:
    """Every schema document, by file name.

    With ``bindings`` given, it is filled with what each declaration stands for in the model,
    keyed by ``(declaring type or group, XML name)``: ``(kind, UML class, UML property,
    target)``, where kind is ``element``, ``attribute``, ``group`` or ``compositor``. Nothing
    written depends on it.
    """
    schema = _Schema(repository, bindings)
    documents = {}
    packages = schema_packages(repository)
    document_of = {p.package_id: document_name(p) for p in packages}
    for package in packages:
        root = ET.Element(q("schema"))
        for tag in ("targetNamespace", "elementFormDefault"):
            value = tagged_value(package.element, tag)
            if value:
                root.set(tag, value)
        for element in package.elements:
            if element.type == "Enumeration" or has_stereotype(element, "enumeration"):
                enumeration(element, root)
            elif has_stereotype(element, "XSDtopLevelElement"):
                top_level_element(schema, element, root)
            elif has_stereotype(element, "XSDcomplexType"):
                complex_type(schema, element, root)
            elif has_stereotype(element, "XSDsimpleType") or has_stereotype(element,
                                                                            "XSDSimpleType"):
                simple_type(schema, element, root)
            elif has_stereotype(element, "XSDunion"):
                union_type(schema, element, root)
            elif has_stereotype(element, "XSDgroup"):
                group(schema, element, root)
        included = sorted({document_of[schema.package_of[name]] for name in _references(root)
                           if schema.package_of.get(name) in document_of
                           and schema.package_of[name] != package.package_id})
        for position, location in enumerate(included):
            root.insert(position, ET.Element(q("include"), schemaLocation=location))
        documents[document_name(package)] = root
    # A schema set that uses an XSD 1.1 construct is processed as XSD 1.1 throughout, so each of
    # its documents says so.
    if any(node.tag in (q("assert"), q("alternative")) for root in documents.values()
           for node in root.iter()):
        for root in documents.values():
            root.set(f"{{{VC}}}minVersion", "1.1")
    return documents
