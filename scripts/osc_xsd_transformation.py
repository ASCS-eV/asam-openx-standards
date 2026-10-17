#!/usr/bin/env python3
"""ASAM's "OSC 2 XSD Transformation", ported from the script ASAM keeps in its EA project.

ASAM generates the normative OpenSCENARIO XML schema from its Enterprise Architect project with
a JScript that the project itself contains, in ``t_script``. It is extracted byte for byte to
``standards/asam-openscenario-xml/uml/source/osc-2-xsd-transformation.js``. This module is that
script, function by function and in the same order, over the object model in ``ea_api.py``, so
that it runs on the ``.qeax`` or on the SCXML export without EA.

The port reproduces the script's behaviour, including where that differs from what the code
seems to intend. Each such place is marked ``As ASAM's script:``. None of them is reached by
the V1.4.0 model, but a port that "fixed" them would stop being evidence about what ASAM
generates.

Two things differ from running the script inside EA, both outside the schema's content:

- EA's ``TextStream.WriteLine`` ends a line with CRLF; the published schema has LF, so the
  port writes LF;
- the script reports a modelling error with ``Session.Output`` or by throwing; the port raises
  :class:`TransformationError`, or, given an ``errors`` list, records the message there and
  carries on with ``?`` in place of the value it could not read. That mode exists to measure
  an incomplete model - the SCXML export - in full rather than up to its first gap.

Run on ASAM's project, the output is byte-identical to the published
``OpenSCENARIO.xsd``. ``check_xsd_transformation.py`` asserts that on every run.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET

from ea_api import Connector, Element, Package, Repository, has_stereotype, tagged_value

DEPRECATED = "<xsd:annotation><xsd:appinfo>deprecated</xsd:appinfo></xsd:annotation>"

HEADER_COMMENT = (
    "<!--",
    "ASAM OpenSCENARIO XML V1.4.0",
    "",
    "__(c)__ by ASAM e.V., 2026",
    "",
    "Description of dynamic content in driving simulations",
    "",
    "Any use is limited to the scope described in the ASAM license terms. ",
    "In alteration to the regular license terms, ASAM allows unrestricted distribution of "
    "this standard.",
    "Paragraph 2 (1) of ASAM's regular license terms is therefore substituted by the following "
    "clause:",
    "\"The licensor grants everyone a basic, non-exclusive and unlimited license to use the "
    "standard ASAM OpenSCENARIO XML\".",
    "See www.asam.net/license.html for further details.",
    "-->",
)


class TransformationError(RuntimeError):
    """A model the script rejects, with the script's own message."""


class _Writer:
    def __init__(self, errors: list | None, bindings: dict | None = None) -> None:
        self.lines: list[str] = []
        self.errors = errors
        self.bindings = bindings
        self.target_names: dict = {}

    def bind(self, owner: str | None, name: str, *binding) -> None:
        """Record which UML property an emitted particle or attribute stands for."""
        if self.bindings is not None:
            self.bindings[(owner, name)] = binding

    def fail(self, message: str) -> str:
        """Raise, or record the message and stand in for the unreadable value."""
        if self.errors is None:
            raise TransformationError(message)
        self.errors.append(message)
        return "?"

    def line(self, text: str) -> None:
        self.lines.append(text)

    def text(self) -> str:
        return "\n".join(self.lines) + "\n"


def indent(counter: int) -> str:
    """``MakeIndent``."""
    return "\t" * counter


def to_first_upper(name: str) -> str:
    """``ToFirstUpper``."""
    return name[:1].upper() + name[1:]


def transform(repository: Repository, errors: list | None = None,
              bindings: dict | None = None) -> str:
    """``Main``: the schema of the package named ``OpenSCENARIO`` under the first model.

    With ``errors`` given, a model the script would reject is measured instead; see the module
    docstring. With ``bindings`` given, it is filled with what each declaration stands for in
    the model, keyed by ``(declaring type or group, XML name)``:
    ``(kind, UML class, UML property, target)``, where kind is ``element``, ``attribute``,
    ``name-reference``, ``wrapper`` or ``content``. Nothing written depends on it.
    """
    root = repository.models[0]
    current = next((p for p in root.packages if p.name == "OpenSCENARIO"), None)
    if current is None:
        raise TransformationError("Select a <XSDschema> Package to create the Schema")
    out = _Writer(errors, bindings)
    out.target_names = {eid: e.name for eid, e in repository.elements.items()}
    write_header(out, 1)
    process_package(out, repository, current)
    out.line("</xsd:schema>")
    return out.text()


def documents(repository: Repository, errors: list | None = None,
              bindings: dict | None = None) -> list[tuple]:
    """The one schema document, as ``(package, file name, parsed schema, text)``."""
    text = transform(repository, errors, bindings)
    return [("OpenSCENARIO", "OpenSCENARIO.xsd", ET.fromstring(text.encode("utf-8")), text)]


def process_package(out: _Writer, repository: Repository, package: Package) -> None:
    for element in package.elements:
        if element.type == "Class":
            if has_stereotype(element, "XSDcomplexType"):
                process_complex_type(out, repository, element, 1)
            elif has_stereotype(element, "XSDgroup"):
                process_group(out, repository, element, 1)
            elif has_stereotype(element, "enumeration"):
                process_enumeration(out, element, 1)
            elif has_stereotype(element, "XSDsimpleContent"):
                process_simple_content(out, element, 1)
            if has_stereotype(element, "XSDtopLevelElement"):
                process_top_level_element(out, element, 1)
        elif element.type == "PrimitiveType":
            process_primitive_type(out, element, 1)
    for sub in sorted(package.packages, key=package_sort_key):
        process_package(out, repository, sub)


#: ``PackageSort``'s order list. The script's comparator returns -1 whenever its first argument
#: is in the list, so it is not a consistent ordering; for the three names it lists and any
#: packages that follow, it places them in list order, which is what this key does.
PACKAGE_ORDER = ("PrimitiveTypes", "Enums", "Classes")


def package_sort_key(package: Package) -> int:
    """``PackageSort``, as an ordering key; see :data:`PACKAGE_ORDER`."""
    if package.name in PACKAGE_ORDER:
        return PACKAGE_ORDER.index(package.name)
    return len(PACKAGE_ORDER)


def process_top_level_element(out: _Writer, element: Element, level: int) -> None:
    name = tagged_value(element, "elementName")
    out.line(f'{indent(level)}<xsd:element name="{name}" type="{element.name}"/>')


def write_header(out: _Writer, level: int) -> None:
    out.line('<?xml version="1.0" encoding="utf-8"?>')
    out.line('<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">')
    for text in HEADER_COMMENT:
        out.line(text)
    out.line(f'{indent(level)}<xsd:element name="OpenSCENARIO" type="OpenScenario"/>')
    out.line(f'{indent(level)}<xsd:simpleType name="parameter">')
    out.line(f'{indent(level + 1)}<xsd:restriction base="xsd:string">')
    out.line(f'{indent(level + 2)}<xsd:pattern value="[$][A-Za-z_][A-Za-z0-9_]*"/>')
    out.line(f"{indent(level + 1)}</xsd:restriction>")
    out.line(f"{indent(level)}</xsd:simpleType>")
    out.line(f'{indent(level)}<xsd:simpleType name="expression">')
    out.line(f'{indent(level + 1)}<xsd:restriction base="xsd:string">')
    out.line(f'{indent(level + 2)}<xsd:pattern value="[$][{{][ A-Za-z0-9_\\+\\-\\*/%$\\(\\)\\.,]*'
             f'[\\}}]"/>')
    out.line(f"{indent(level + 1)}</xsd:restriction>")
    out.line(f"{indent(level)}</xsd:simpleType>")


def process_primitive_type(out: _Writer, element: Element, level: int) -> None:
    name = element.name or ""
    if name in ("int", "unsignedInt", "boolean", "double", "unsignedShort"):
        out.line(f'{indent(level)}<xsd:simpleType name="{to_first_upper(name)}">')
        out.line(f'{indent(level + 1)}<xsd:union memberTypes="expression parameter xsd:{name}"/>')
        out.line(f"{indent(level)}</xsd:simpleType>")
    elif name in ("string", "dateTime"):
        out.line(f'{indent(level)}<xsd:simpleType name="{to_first_upper(name)}">')
        out.line(f'{indent(level + 1)}<xsd:union memberTypes="parameter xsd:{name}"/>')
        out.line(f"{indent(level)}</xsd:simpleType>")
    elif name == "id":
        out.line(f'{indent(level)}<xsd:attributeGroup name="Identifier">')
        out.line(f'{indent(level + 1)}<xsd:attribute name="name" type="xsd:string"/>')
        out.line(f"{indent(level)}</xsd:attributeGroup>")
    else:
        # As ASAM's script: reported to the output window, and generation carries on.
        pass


def process_complex_type(out: _Writer, repository: Repository, element: Element,
                         level: int) -> None:
    out.line(f'{indent(level)}<xsd:complexType name="{element.name}">')
    if has_stereotype(element, "deprecated"):
        out.line(indent(level + 1) + DEPRECATED)
    process_type(out, repository, element, level + 1)
    out.line(f"{indent(level)}</xsd:complexType>")
    wrapper = tagged_value(element, "xsdWrapperType")
    if wrapper is not None:
        out.bind(wrapper, tagged_value(element, "xsdWrapperElementName") or "", "wrapped",
                 None, None, element.name)
        # As ASAM's script: one level deeper than the complexType it follows.
        process_wrapper_type(out, wrapper, element.name or "",
                             tagged_value(element, "xsdWrapperElementName"), level + 1)


def process_simple_content(out: _Writer, element: Element, level: int) -> None:
    uml_property_name = tagged_value(element, "umlPropertyName")
    xsd_type = tagged_value(element, "xsdType")
    out.line(f'{indent(level)}<xsd:complexType name="{element.name}">')
    if has_stereotype(element, "deprecated"):
        out.line(indent(level + 1) + DEPRECATED)
    out.line(f"{indent(level + 1)}<xsd:simpleContent>")
    out.line(f'{indent(level + 2)}<xsd:extension base="xsd:{xsd_type}">')
    for attribute in element.attributes:
        if attribute.name != uml_property_name:
            # As ASAM's script: at the level of <xsd:simpleContent>, not inside the extension.
            process_attribute(out, attribute, level + 1, element)
        else:
            out.bind(element.name, "", "content", element.name, attribute.name, xsd_type)
    out.line(f"{indent(level + 2)}</xsd:extension>")
    out.line(f"{indent(level + 1)}</xsd:simpleContent>")
    out.line(f"{indent(level)}</xsd:complexType>")
    wrapper = tagged_value(element, "xsdWrapperType")
    if wrapper is not None:
        process_wrapper_type(out, wrapper, element.name or "",
                             tagged_value(element, "xsdWrapperElementName"), level)


def process_enumeration(out: _Writer, element: Element, level: int) -> None:
    out.line(f'{indent(level)}<xsd:simpleType name="{element.name}">')
    if has_stereotype(element, "deprecated"):
        out.line(indent(level + 1) + DEPRECATED)
    out.line(f"{indent(level + 1)}<xsd:union>")
    out.line(f"{indent(level + 2)}<xsd:simpleType>")
    out.line(f'{indent(level + 3)}<xsd:restriction base="xsd:string">')
    for literal in element.attributes:
        if not has_stereotype(literal, "deprecated"):
            out.line(f'{indent(level + 4)}<xsd:enumeration value="{literal.name}"/>')
        else:
            out.line(f'{indent(level + 4)}<xsd:enumeration value="{literal.name}">')
            out.line(indent(level + 5) + DEPRECATED)
            out.line(f"{indent(level + 4)}</xsd:enumeration>")
    out.line(f"{indent(level + 3)}</xsd:restriction>")
    out.line(f"{indent(level + 2)}</xsd:simpleType>")
    out.line(f"{indent(level + 2)}<xsd:simpleType>")
    out.line(f'{indent(level + 3)}<xsd:restriction base="parameter"/>')
    out.line(f"{indent(level + 2)}</xsd:simpleType>")
    out.line(f"{indent(level + 1)}</xsd:union>")
    out.line(f"{indent(level)}</xsd:simpleType>")


def process_group(out: _Writer, repository: Repository, element: Element, level: int) -> None:
    out.line(f'{indent(level)}<xsd:group name="{element.name}">')
    if has_stereotype(element, "deprecated"):
        # As ASAM's script: a fixed indentation of 2.
        out.line(indent(2) + DEPRECATED)
    process_type(out, repository, element, level + 1)
    out.line(f"{indent(level)}</xsd:group>")


def process_type(out: _Writer, repository: Repository, element: Element, level: int) -> None:
    elements, name_refs = get_connectors(out, element)
    model_group, full_result = get_model_group(element)
    if elements:
        out.line(f"{indent(level)}<xsd:{full_result}>")
        for connector in elements:
            process_element(out, repository, connector, element, level + 1)
        out.line(f"{indent(level)}</xsd:{model_group}>")
    for connector in name_refs:
        process_name_ref(out, connector, level, element.name)
    for attribute in element.attributes:
        process_attribute(out, attribute, level, element)


def process_element(out: _Writer, repository: Repository, connector: Connector, owner: Element,
                    level: int) -> None:
    lower_upper = get_lower_upper(connector.supplier_end.cardinality)
    supplier = repository.get_element_by_id(connector.supplier_id)
    if lower_upper is None:
        lower_upper = (out.fail(
            f"Cardinality of property '{connector.supplier_end.role}' of '{owner.name}' must "
            "be in the format '0..1', '1..*', '0..2', '1..1'"),) * 2
    lower, upper = lower_upper
    min_occurs = max_occurs = ""
    if lower != "1":
        min_occurs = f' minOccurs="{lower}"'
    wrapper = tagged_value(supplier, "xsdWrapperType")
    type_name = supplier.name
    if wrapper is not None and has_stereotype(connector, "XSDwrapped"):
        type_name = wrapper
    elif upper != "1":
        if upper == "*":
            max_occurs = ' maxOccurs="unbounded"'
        else:
            # As ASAM's script: a finite upper bound replaces minOccurs, written as
            # maxOccurs with the *lower* bound's value.
            min_occurs = f' maxOccurs="{lower}"'
    deprecated = has_stereotype(connector, "deprecated")
    if has_stereotype(supplier, "XSDgroup"):
        out.bind(owner.name, f"group {supplier.name}", "group", owner.name,
                 connector.supplier_end.role, supplier.name)
        out.line(f'{indent(level)}<xsd:group ref="{supplier.name}"{min_occurs}{max_occurs}/>')
        if deprecated:
            # As ASAM's script: after a self-closed <xsd:group/>, which is not well formed.
            out.line(indent(level + 1) + DEPRECATED)
            out.line(f"{indent(level)}</xsd:group>")
    else:
        name = get_element_name(connector.supplier_end.role or "", connector)
        out.bind(owner.name, name, "wrapper" if type_name != supplier.name else "element",
                 owner.name, connector.supplier_end.role, supplier.name)
        if not deprecated:
            out.line(f'{indent(level)}<xsd:element name="{name}" type="{type_name}"'
                     f"{min_occurs}{max_occurs}/>")
        else:
            out.line(f'{indent(level)}<xsd:element name="{name}" type="{type_name}"'
                     f"{min_occurs}{max_occurs}>")
            out.line(indent(level + 1) + DEPRECATED)
            out.line(f"{indent(level)}</xsd:element>")


def process_wrapper_type(out: _Writer, wrapper: str, wrapped: str, element_name: str | None,
                         level: int) -> None:
    out.line(f'{indent(level)}<xsd:complexType name="{wrapper}">')
    out.line(f"{indent(level + 1)}<xsd:sequence>")
    out.line(f'{indent(level + 2)}<xsd:element name="{element_name}" type="{wrapped}" '
             'minOccurs="0" maxOccurs="unbounded"/>')
    out.line(f"{indent(level + 1)}</xsd:sequence>")
    out.line(f"{indent(level)}</xsd:complexType>")


def process_attribute(out: _Writer, attribute, level: int, owner: Element | None = None) -> None:
    if owner is not None:
        out.bind(owner.name, attribute.name, "attribute", owner.name, attribute.name,
                 attribute.type)
    deprecated = has_stereotype(attribute, "deprecated")
    use = ' use="required"' if attribute.lower_bound == "1" else ""
    if attribute.type != "id":
        head = (f'{indent(level)}<xsd:attribute name="{attribute.name}" '
                f'type="{to_first_upper(attribute.type or "")}"{use}')
        if not deprecated:
            out.line(head + "/>")
        else:
            out.line(head + ">")
            out.line(indent(level + 1) + DEPRECATED)
            out.line(f"{indent(level)}</xsd:attribute>")
    elif not deprecated:
        out.line(f'{indent(level)}<xsd:attributeGroup ref="Identifier"/>')
    else:
        out.line(f'{indent(level)}<xsd:attributeGroup ref="Identifier">')
        out.line(indent(level + 1) + DEPRECATED)
        # As ASAM's script: closed as an attribute, which is not well formed.
        out.line(f"{indent(level)}</xsd:attribute>")


def process_name_ref(out: _Writer, connector: Connector, level: int,
                     owner_name: str | None = None) -> None:
    lower_upper = get_lower_upper(connector.supplier_end.cardinality)
    if lower_upper is None:
        # As ASAM's script: it indexes the null result, which throws.
        lower_upper = (out.fail(
            f"nameRef '{connector.supplier_end.role}' has no cardinality in the format "
            "'n..m'"),) * 2
    name = connector.supplier_end.role
    use = ' use="required"' if lower_upper[0] != "0" else ""
    xsd_type = tagged_value(connector, "xsdType")
    if xsd_type is None:
        # As ASAM's script: ToFirstUpper(null) throws.
        xsd_type = out.fail(f"nameRef '{name}' of connector {connector.connector_id} has no "
                            "xsdType tagged value")
    head = f'{indent(level)}<xsd:attribute name="{name}" type="{to_first_upper(xsd_type)}"{use}'
    out.bind(owner_name, name or "", "name-reference", owner_name, name,
             out.target_names.get(connector.supplier_id))
    if not has_stereotype(connector, "deprecated"):
        out.line(head + "/>")
    else:
        out.line(head + ">")
        out.line(indent(level + 1) + DEPRECATED)
        out.line(f"{indent(level)}</xsd:attribute>")


def get_connectors(out: _Writer, element: Element) -> tuple[list[Connector], list[Connector]]:
    """``GetConnectors``: the element-producing and the name-reference connectors, in order."""
    elements: list[tuple[int, Connector]] = []
    name_refs: list[Connector] = []
    for connector in element.connectors:
        outgoing = connector.client_id == element.element_id
        if outgoing and connector.type == "Association" and not connector.supplier_end.role:
            out.fail(f"Every property of class '{element.name}' must define a name at "
                     "association end role")
        name_ref = has_stereotype(connector, "nameRef")
        # As ASAM's script: "transient" is tested on the Stereotype property alone.
        if (outgoing and connector.type == "Association" and not name_ref
                and connector.stereotype != "transient"):
            elements.append((get_position(out, connector), connector))
        elif name_ref and outgoing:
            name_refs.append(connector)
    # Array.prototype.sort; a stable sort, like Python's, keeps connectors with the same
    # position in collection order.
    elements.sort(key=lambda pair: pair[0])
    return [connector for _, connector in elements], name_refs


def get_position(out: _Writer, connector: Connector) -> int:
    value = tagged_value(connector, "position")
    if value is None:
        return -1
    match = re.match(r"\s*([+-]?\d+)", value)
    # As ASAM's script: parseInt of a value with no leading digits is NaN, which compares
    # neither less nor greater; this port refuses the model instead of guessing an order.
    if match is None:
        out.fail(f"position {value!r} of connector {connector.connector_id} is not a number")
        return -1
    return int(match.group(1))


#: ``GetLowerUpper``'s pattern. As ASAM's script: the upper bound is one character from the
#: class ``[\d+|*]``, so "0..10" reads as 0..1.
_LOWER_UPPER = re.compile(r"(\d+)\.\.([\d+|*])")


def get_lower_upper(cardinality: str | None) -> tuple[str, str] | None:
    match = _LOWER_UPPER.search(cardinality or "")
    return (match.group(1), match.group(2)) if match else None


def get_occurrence(element: Element) -> tuple[str | int, str | int]:
    """``GetOccurrence``: the class's minOccurs/maxOccurs tags, 1 when absent or empty."""
    return (tagged_value(element, "minOccurs") or 1, tagged_value(element, "maxOccurs") or 1)


def get_model_group(element: Element) -> tuple[str, str]:
    """``GetModelGroup``: the compositor, and the compositor with its occurrence."""
    value = tagged_value(element, "modelGroup")
    min_occurs, max_occurs = get_occurrence(element)
    model_group = "sequence" if value is None or value == "" else value
    full_result = model_group
    if min_occurs and not _loosely_equals_one(min_occurs):
        full_result = f'{model_group} minOccurs="{min_occurs}"'
    if max_occurs and not _loosely_equals_one(max_occurs):
        # As ASAM's script: "unbound", and minOccurs is dropped when both are set.
        max_occurs = "unbound" if max_occurs == "*" else max_occurs
        full_result = f'{model_group} maxOccurs="{max_occurs}"'
    return model_group, full_result


def _loosely_equals_one(value: str | int) -> bool:
    """JavaScript's ``value == 1``: a string is converted to a number first."""
    if isinstance(value, int):
        return value == 1
    text = value.strip()
    try:
        return text != "" and float(text) == 1
    except ValueError:
        return False


def get_element_name(property_name: str, connector: Connector) -> str:
    name = tagged_value(connector, "xsdElementName")
    return to_first_upper(property_name) if name is None else name
