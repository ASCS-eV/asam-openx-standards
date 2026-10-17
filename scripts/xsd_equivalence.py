#!/usr/bin/env python3
"""Whether two XML Schemas say the same thing, component by component.

``xsd_content_model.py`` compares a ShapeChange-generated schema with ASAM's across an
encoding-style gap, so it normalizes that gap away. This module compares two schemas written in
the *same* style, a regenerated one and the normative one, and normalizes nothing that carries
meaning. It separates three things a byte comparison cannot tell apart:

**Content.** Whether each top-level component (every child of ``xs:schema``) declares the same
thing: the same particles, attributes, facets, identity constraints, assertions and type
alternatives, with the same values. The order of a construct matters exactly where XML Schema
gives it meaning:

- the children of ``xs:sequence``;
- the ``xs:alternative`` list of an element, where the first matching test wins;
- the ``xs:field`` list of an identity constraint.

Elsewhere it does not, and is not compared: the attributes of a component, the alternatives of
``xs:choice`` and ``xs:all``, the facets of a restriction, identity constraints, assertions, and
the components of a schema.

**Particle order.** A sequence whose particles are the same but in another order. A sequence
fixes element order in a conforming document, so this is a difference of content. It is
reported under its own rule because its cause differs: the order must be *recorded* somewhere to
be reproduced.

**Alternative order.** The same type alternatives in another order. The first alternative whose
test holds assigns the type, so the order matters wherever two tests can hold at once.

**Documentation.** ``xs:annotation`` compared on its own, since it describes the language
without changing it.

**The schema element.** The attributes of ``xs:schema`` itself, such as ``targetNamespace``,
``elementFormDefault`` and XSD 1.1's ``vc:minVersion``.

Comments, whitespace-only text and the lexical form of the document (attribute order,
indentation, line ends, character references) are not schema content and are not compared.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass

XS = "http://www.w3.org/2001/XMLSchema"
VC = "http://www.w3.org/2007/XMLSchema-versioning"

#: Elements whose children are ordered by XML Schema's semantics.
ORDERED = frozenset({"sequence", "element", "key", "keyref", "unique", "annotation"})
#: Of the children of an element, only these are ordered among themselves: the
#: ``xs:alternative`` list. Its other children (the anonymous type, identity constraints) are not.
ORDERED_CHILDREN = {"element": frozenset({"alternative"})}

VERDICTS = ("MISSING", "EXTRA", "DIFFERENT")
RULES = ("schema", "component", "particle-order", "alternative-order", "documentation")


@dataclass(frozen=True, order=True)
class Finding:
    verdict: str
    rule: str
    component: str
    detail: str

    @property
    def key(self) -> str:
        return f"{self.rule}: {self.component}"


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _canon(node: ET.Element, documentation: bool, order: bool,
           alternatives: bool = True) -> tuple:
    """A hashable form of a schema element; see the module docstring for what is ordered.

    ``order`` keeps sequences in order, ``alternatives`` the ``xs:alternative`` lists.
    """
    tag = _local(node.tag)
    text = (node.text or "") if tag in ("documentation", "appinfo") else ""
    attributes = tuple(sorted((_local(k), v) for k, v in node.attrib.items()))
    children = [c for c in node if isinstance(c.tag, str)]
    if not documentation:
        children = [c for c in children if _local(c.tag) != "annotation"]
    forms = [(_local(c.tag), _canon(c, documentation, order, alternatives)) for c in children]
    if tag in ORDERED and (order or tag != "sequence"):
        ordered_kinds = ORDERED_CHILDREN.get(tag)
        if ordered_kinds is not None and not alternatives:
            ordered_kinds = frozenset()
        if ordered_kinds is None:
            content = tuple(form for _, form in forms)
        else:
            content = (tuple(sorted(form for kind, form in forms if kind not in ordered_kinds))
                       + tuple(form for kind, form in forms if kind in ordered_kinds))
    else:
        content = tuple(sorted(form for _, form in forms))
    return (tag, attributes, text, content)


def component_key(node: ET.Element) -> str:
    name = node.get("name") or node.get("ref") or node.get("schemaLocation") or ""
    return f"{_local(node.tag)} {name}".strip()


def components(root: ET.Element) -> dict[str, list[ET.Element]]:
    """The children of ``xs:schema`` by kind and name. A repeated key keeps every occurrence."""
    found: dict[str, list[ET.Element]] = {}
    for child in root:
        if isinstance(child.tag, str):
            found.setdefault(component_key(child), []).append(child)
    return found


def _first_difference(ours: tuple, theirs: tuple, path: str = "") -> str:
    """A short description of where two canonical forms part."""
    tag, attributes, text, content = ours
    other_tag, other_attributes, other_text, other_content = theirs
    here = f"{path}/{tag}" if path else tag
    if tag != other_tag:
        return f"{here}: {tag} vs {other_tag}"
    if attributes != other_attributes:
        mine, other = dict(attributes), dict(other_attributes)
        keys = sorted(set(mine) | set(other))
        diffs = [f"@{k}={mine.get(k)!r} vs {other.get(k)!r}" for k in keys
                 if mine.get(k) != other.get(k)]
        return f"{here}: " + ", ".join(diffs)
    if text != other_text:
        return f"{here}: text {text[:60]!r} vs {other_text[:60]!r}"
    for mine, other in zip(content, other_content):
        if mine != other:
            return _first_difference(mine, other, here)
    return f"{here}: {len(content)} vs {len(other_content)} children"


def compare_schemas(generated: ET.Element, normative: ET.Element) -> list[Finding]:
    """Findings, from the normative schema's point of view: MISSING is absent from ``generated``."""
    ours, theirs = components(generated), components(normative)
    findings = []
    mine, other = dict(generated.attrib), dict(normative.attrib)
    for name in sorted(set(mine) | set(other)):
        shown = name.replace(f"{{{VC}}}", "vc:")
        if name not in mine:
            findings.append(Finding("MISSING", "schema", f"schema @{shown}", repr(other[name])))
        elif name not in other:
            findings.append(Finding("EXTRA", "schema", f"schema @{shown}", repr(mine[name])))
        elif mine[name] != other[name]:
            findings.append(Finding("DIFFERENT", "schema", f"schema @{shown}",
                                    f"{mine[name]!r} vs {other[name]!r}"))
    for key in sorted(set(theirs) - set(ours)):
        findings.append(Finding("MISSING", "component", key, "not generated"))
    for key in sorted(set(ours) - set(theirs)):
        findings.append(Finding("EXTRA", "component", key, "not in the normative schema"))
    for key in sorted(set(ours) & set(theirs)):
        mine, other = ours[key], theirs[key]
        if len(mine) != len(other):
            findings.append(Finding("DIFFERENT", "component", key,
                                    f"{len(mine)} vs {len(other)} declarations"))
            continue
        for a, b in zip(sorted(mine, key=lambda n: _canon(n, True, True)),
                        sorted(other, key=lambda n: _canon(n, True, True))):
            content = (_canon(a, False, False, False), _canon(b, False, False, False))
            if content[0] != content[1]:
                findings.append(Finding("DIFFERENT", "component", key,
                                        _first_difference(*content)))
                continue
            # With the content equal, each remaining aspect is compared on its own.
            for rule, forms in (
                    ("particle-order", (_canon(a, False, True, False),
                                        _canon(b, False, True, False))),
                    ("alternative-order", (_canon(a, False, False, True),
                                           _canon(b, False, False, True))),
                    ("documentation", (_canon(a, True, False, False),
                                       _canon(b, True, False, False)))):
                if forms[0] != forms[1]:
                    findings.append(Finding("DIFFERENT", rule, key, _first_difference(*forms)))
    return findings
