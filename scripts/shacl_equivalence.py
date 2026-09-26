#!/usr/bin/env python3
"""Whether the SHACL shapes constrain an instance graph as the model's schema constrains a file.

``check_xsd_transformation.py`` establishes what the model says in XML Schema terms: the schema
derived from the model is ASAM's normative one, up to the differences it records. This module
compares the SHACL shapes generated from the same model with that schema, class by class, in
terms of the RDF graph an instance document becomes. For every complex type it computes what a
node of that class must and may carry:

- each **property** with the least and greatest number of values a conforming document can give
  it, and its value type. A property is the UML property the schema's element or attribute was
  derived from; the derivation records which, per declaration (its ``bindings``);
- each **choice**: a set of properties of which a conforming document gives exactly one (or at
  most one, when the choice is optional), each with its own count.

The schema's structure is resolved on the way. An extension inherits its base's content, a
group reference and a nested compositor contribute their particles, occurrences multiply
through repeated groups, and a choice that can repeat is no choice at all, only a set of
optional properties. An XML list wrapper, such as OpenSCENARIO's ``ParameterDeclarations``,
stands for no class: its items are the values of the property it was derived from. Simple
content is the value of the property it was derived from, exactly one. A reference by name
(OpenSCENARIO's ``nameRef``) is the association it was derived from: its value is the node of
the class it names, which a document identifies by its name. The order of a sequence does not
survive into a graph and is not compared;
``xsd_equivalence.py`` compares it.

From the SHACL it reads, per node shape, the property shapes (``sh:path``, ``sh:minCount``,
``sh:maxCount``, ``sh:class``, ``sh:datatype``, ``sh:in``), ``sh:closed`` with
``sh:ignoredProperties``, and each ``sh:or``. A path a closed shape ignores is admitted, and
constrained by the shape of the class that declares it: SHACL targets that shape at the
instances of its subclasses too, when the data graph holds the ontology's ``rdfs:subClassOf``.
An ``sh:or`` whose
alternatives each admit one property and exclude the others (``sh:maxCount 0``) is a choice;
this is how the OWL union encoding reaches SHACL.

A property is identified as the OWL target names it: ``<namespace><Class>.<property>``, the
class being the one that declares the property, with its first letter upper-cased. A property
contributed by a group or a nested compositor is **inlined**: it is identified as a property of
the class whose content includes it, because in a document its elements are that class's
children.

A difference is a finding with a verdict and a rule:

``MISSING``
    The schema lets a document carry it; the shapes do not: no node shape for a class, no
    property shape on a closed shape, a choice the shapes do not encode as one.
``EXTRA``
    The shapes demand or admit what the schema does not: a property the schema has no
    declaration for, a choice the schema does not have.
``DIFFERENT``
    Both state it, differently: a count bound, a value type.

The rule says which: ``shape``, ``property``, ``choice``, ``min``, ``max``, ``value``, or
``unbound`` for a declaration with no UML property to be (an unnamed association end).
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

XS = "http://www.w3.org/2001/XMLSchema"
XSD_NS = "http://www.w3.org/2001/XMLSchema#"
SH = "http://www.w3.org/ns/shacl#"
RDF_FIRST = "http://www.w3.org/1999/02/22-rdf-syntax-ns#first"
RDF_REST = "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest"
RDF_NIL = "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"
RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"

UNBOUNDED = None
VERDICTS = ("MISSING", "EXTRA", "DIFFERENT")
RULES = ("shape", "property", "choice", "min", "max", "value", "unbound")


def _q(name: str) -> str:
    return f"{{{XS}}}{name}"


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def capitalized(name: str) -> str:
    """The OWL target's class name: the UML name with its first letter upper-cased."""
    return name[:1].upper() + name[1:]


def uncapitalized(name: str) -> str:
    """The OWL target's property name: the UML name with its first letter lower-cased."""
    return name[:1].lower() + name[1:]


def _times(a: int | None, b: int | None) -> int | None:
    return UNBOUNDED if a is UNBOUNDED or b is UNBOUNDED else a * b


def _plus(a: int | None, b: int | None) -> int | None:
    return UNBOUNDED if a is UNBOUNDED or b is UNBOUNDED else a + b


def _occurs(node: ET.Element) -> tuple[int, int | None]:
    low = int(node.get("minOccurs", "1"))
    high = node.get("maxOccurs", "1")
    return low, UNBOUNDED if high == "unbounded" else int(high)


@dataclass
class Prop:
    min: int
    max: int | None
    value: str


@dataclass
class Choice:
    """Alternatives that exclude each other; each is the properties it gives values to."""

    optional: bool
    alternatives: list = field(default_factory=list)

    @property
    def members(self) -> dict:
        return {path: prop for alternative in self.alternatives
                for path, prop in alternative.items()}

    def signature(self) -> frozenset:
        return frozenset(frozenset(alternative) for alternative in self.alternatives)

    def normalized(self) -> "Choice":
        """The same language with each single-property alternative optional when the choice is.

        When no alternative need be given, one that requires its property at least once admits
        the same documents as one that does not: the empty case is admitted either way. This is
        how a flattened optional choice reaches the shapes.
        """
        if not self.optional:
            return self
        alternatives = [{path: Prop(0, prop.max, prop.value) for path, prop in alt.items()}
                        if len(alt) == 1 else alt for alt in self.alternatives]
        return Choice(True, alternatives)


@dataclass
class Expected:
    abstract: bool = False
    properties: dict = field(default_factory=dict)
    choices: list = field(default_factory=list)
    unbound: list = field(default_factory=list)
    #: Declarations of one class that become the same property: an attribute and an element of
    #: the same name, which XML keeps apart and a graph cannot.
    clashes: set = field(default_factory=set)
    wildcard: bool = False


@dataclass(frozen=True, order=True)
class Finding:
    verdict: str
    rule: str
    subject: str
    detail: str

    @property
    def key(self) -> str:
        return f"{self.verdict} {self.rule}: {self.subject}"


# ---------------------------------------------------------------------------------------
# What the schema lets an instance node carry


class _Content:
    def __init__(self, documents: list[ET.Element], bindings: dict, namespace: str,
                 value_type) -> None:
        self.namespace = namespace
        self.bindings = bindings
        self.value_type = value_type
        self.complex: dict[str, ET.Element] = {}
        self.groups: dict[str, ET.Element] = {}
        self.roots: dict[str, ET.Element] = {}
        for root in documents:
            for node in root:
                if not isinstance(node.tag, str) or not node.get("name"):
                    continue
                kind = _local(node.tag)
                if kind == "complexType":
                    self.complex[node.get("name")] = node
                elif kind == "group":
                    self.groups[node.get("name")] = node
                elif kind == "element" and node.find(_q("complexType")) is not None:
                    self.roots[node.get("name")] = node.find(_q("complexType"))

    def is_wrapper(self, type_name: str) -> bool:
        """An XML list wrapper type, which no UML class stands for."""
        return any(key[0] == type_name and binding[0] == "wrapped"
                   for key, binding in self.bindings.items())

    def path(self, uml_class: str | None, prop: str | None) -> str | None:
        if not uml_class or not prop:
            return None
        return f"{self.namespace}{capitalized(uml_class)}.{uncapitalized(prop)}"

    def expected(self, type_name: str, node: ET.Element, uml_class: str) -> Expected:
        """What a node of ``uml_class``, whose schema type is ``node``, may carry."""
        found = Expected(abstract=node.get("abstract") == "true")
        self.walk_type(node, type_name, uml_class, found, (1, 1), set())
        return found

    def walk_type(self, node: ET.Element, owner: str, declaring: str, found: Expected,
                  multiplier: tuple, seen: set) -> None:
        """``owner`` keys the bindings of the declarations in ``node``; ``declaring`` is the
        UML class whose properties they are."""
        for child in node:
            if not isinstance(child.tag, str):
                continue
            kind = _local(child.tag)
            if kind == "simpleContent":
                binding = self.bindings.get((owner, ""))
                path = self.path(binding[1], binding[2]) if binding else None
                if path is None:
                    found.unbound.append(f"the text content of {owner}")
                else:
                    extension = child.find(_q("extension"))
                    base = extension.get("base") if extension is not None else None
                    self.add(found.properties, path, Prop(1, 1, self.value_type(base)), found)
                self.walk_type(child, owner, declaring, found, multiplier, seen)
            elif kind == "complexContent":
                self.walk_type(child, owner, declaring, found, multiplier, seen)
            elif kind == "extension":
                base = child.get("base")
                if base in self.complex and base not in seen and not self.is_wrapper(base):
                    self.walk_type(self.complex[base], base, base, found, multiplier,
                                   seen | {base})
                self.walk_type(child, owner, declaring, found, multiplier, seen)
            elif kind in ("sequence", "all", "choice", "element", "group", "any"):
                self.particle(child, owner, declaring, found, multiplier, seen, None)
            elif kind == "attribute":
                self.attribute(child, owner, found)

    def attribute(self, node: ET.Element, owner: str, found: Expected) -> None:
        binding = self.bindings.get((owner, node.get("name")))
        path = self.path(binding[1], binding[2]) if binding else None
        if path is None:
            found.unbound.append(f"attribute {node.get('name')} of {owner}")
            return
        low = 1 if node.get("use") == "required" else 0
        # A reference by name is, in the model, an association to the class it names: its
        # value in a graph is that node, of which the document gives only the name.
        value = (self.value_type(binding[3]) if binding[0] == "name-reference"
                 else self.value_type(node.get("type")))
        self.add(found.properties, path, Prop(low, 1, value), found)

    @staticmethod
    def add(into: dict, path: str, prop: Prop, found: Expected) -> None:
        """The same property declared twice holds the values of both declarations; declared
        with two value types, it is a clash."""
        if path in into:
            old = into[path]
            if old.value != prop.value:
                found.clashes.add(path)
            into[path] = Prop(old.min + prop.min, _plus(old.max, prop.max), old.value)
        else:
            into[path] = prop

    def particle(self, node: ET.Element, owner: str, declaring: str, found: Expected,
                 multiplier: tuple, seen: set, into: dict | None) -> None:
        """``into`` collects the properties of one choice alternative, else ``found``'s."""
        kind = _local(node.tag)
        low, high = _occurs(node)
        m_low, m_high = _times(multiplier[0], low), _times(multiplier[1], high)
        target = into if into is not None else found.properties
        if kind in ("sequence", "all"):
            for child in node:
                if isinstance(child.tag, str):
                    self.particle(child, owner, declaring, found, (m_low, m_high), seen, into)
        elif kind == "choice":
            alternatives = [c for c in node if isinstance(c.tag, str)]
            if m_high == 1 and into is None and len(alternatives) > 1:
                group = Choice(optional=m_low == 0)
                for child in alternatives:
                    alternative: dict = {}
                    self.particle(child, owner, declaring, found, (1, 1), seen, alternative)
                    group.alternatives.append(alternative)
                    if all(prop.min == 0 for prop in alternative.values()):
                        group.optional = True
                found.choices.append(group)
            else:
                # A choice that can repeat, has one alternative, or sits in an alternative of
                # another choice excludes nothing here: each alternative is optional and can
                # recur as often as the choice can.
                for child in alternatives:
                    self.particle(child, owner, declaring, found, (0, m_high), seen, into)
        elif kind == "group":
            name = node.get("ref")
            if name in self.groups and name not in seen:
                for child in self.groups[name]:
                    if isinstance(child.tag, str) and _local(child.tag) != "annotation":
                        self.particle(child, name, declaring, found, (m_low, m_high),
                                      seen | {name}, into)
        elif kind == "any":
            found.wildcard = True
        elif kind == "element":
            binding = self.bindings.get((owner, node.get("name")))
            if binding is None or not binding[2]:
                found.unbound.append(f"element {node.get('name')} of {owner}")
                return
            if binding[0] == "wrapper":
                # An XML list wrapper: its items are the property's values, and the wrapper
                # type admits any number of them, none included.
                self.add(target, self.path(declaring, binding[2]),
                         Prop(0, UNBOUNDED, self.value_type(binding[3])), found)
                return
            # A property of the class whose content model declares it, which for a group's
            # or a nested compositor's element is the class that includes them (inlined).
            self.add(target, self.path(declaring, binding[2]),
                     Prop(m_low, m_high, self.value_type(node.get("type"))), found)


class ValueTypes:
    """The value constraint each schema type stands for, as the shapes would state it.

    - a built-in type is its XSD datatype;
    - a type the OWL target's map entries replace is the datatype they name;
    - an enumeration is ``sh:in`` over its literals, and so is a union of enumerations;
    - a union of one built-in type with pattern restrictions of ``xs:string`` is that built-in
      type: OpenSCENARIO's ``Double`` admits a parameter reference or an expression in place of
      a number, which is how a template is written and not a different value type;
    - a complex type is ``sh:class`` of its class.

    Anything else is reported as ``simple <name>`` and compared as such.
    """

    def __init__(self, documents: list[ET.Element], namespace: str,
                 map_entries: dict[str, str]) -> None:
        self.namespace = namespace
        self.map_entries = map_entries
        self.simple: dict[str, ET.Element] = {}
        self.complex: set[str] = set()
        for root in documents:
            for node in root:
                if isinstance(node.tag, str) and node.get("name"):
                    if _local(node.tag) == "simpleType":
                        self.simple[node.get("name")] = node
                    elif _local(node.tag) == "complexType":
                        self.complex.add(node.get("name"))

    @staticmethod
    def builtin(name: str) -> str | None:
        prefix, _, local = name.rpartition(":")
        return local if prefix in ("xs", "xsd") else None

    def literals(self, name: str, seen: frozenset = frozenset()) -> list[str] | None:
        """The literals of an enumeration or a union of enumerations, else None."""
        node = self.simple.get(name)
        if node is None or name in seen:
            return None
        values = [e.get("value") for e in node.iter(_q("enumeration"))]
        union = node.find(_q("union"))
        members = (union.get("memberTypes") or "").split() if union is not None else []
        for member in members:
            if self.builtin(member) or member in ("parameter", "expression"):
                continue
            more = self.literals(member, seen | {name})
            if more is None:
                return None
            values.extend(more)
        return values or None

    def __call__(self, name: str | None) -> str:
        if not name:
            return "any"
        builtin = self.builtin(name)
        if builtin:
            return f"datatype {XSD_NS}{builtin}"
        if name in self.map_entries:
            return f"datatype {XSD_NS}{self.map_entries[name]}"
        if name in self.complex:
            return f"class {self.namespace}{capitalized(name)}"
        literals = self.literals(name)
        if literals:
            return "in " + " ".join(sorted(set(literals)))
        node = self.simple.get(name)
        union = node.find(_q("union")) if node is not None else None
        if union is not None:
            members = (union.get("memberTypes") or "").split()
            builtins = [m for m in members if self.builtin(m)]
            patterns = [m for m in members if not self.builtin(m) and self.is_pattern(m)]
            if len(builtins) == 1 and len(builtins) + len(patterns) == len(members):
                return f"datatype {XSD_NS}{self.builtin(builtins[0])}"
        return f"simple {name}"

    def is_pattern(self, name: str) -> bool:
        node = self.simple.get(name)
        restriction = node.find(_q("restriction")) if node is not None else None
        return (restriction is not None and self.builtin(restriction.get("base") or "")
                == "string" and restriction.find(_q("pattern")) is not None)


def load_map_entries(path) -> dict[str, str]:
    """The OWL target's ``RdfTypeMapEntry`` substitutions: UML type -> XSD datatype local name."""
    root = ET.parse(path).getroot()
    entries = {}
    for node in root.iter():
        if isinstance(node.tag, str) and node.tag.endswith("RdfTypeMapEntry"):
            target = node.get("target") or ""
            if target.startswith("xsd:"):
                entries[node.get("type")] = target[4:]
    return entries


def expected_content(documents: list[ET.Element], bindings: dict, namespace: str,
                     value_type) -> dict[str, Expected]:
    """What a node of each class may carry, by UML class name.

    A global element with an anonymous type stands for the UML class its declarations are bound
    to, such as OpenDRIVE's ``t_OpenDRIVE`` nested in the element class ``OpenDRIVE``.
    """
    content = _Content(documents, bindings, namespace, value_type)
    found = {name: content.expected(name, node, name) for name, node in content.complex.items()
             if not content.is_wrapper(name)}
    for element_name, node in content.roots.items():
        classes = {b[1] for key, b in bindings.items() if key[0] == element_name and b[1]}
        if len(classes) == 1:
            uml = classes.pop()
            found[uml] = content.expected(element_name, node, uml)
    return found


# ---------------------------------------------------------------------------------------
# What the SHACL shapes let a node carry


@dataclass
class Shape:
    closed: bool = False
    properties: dict = field(default_factory=dict)
    choices: list = field(default_factory=list)
    #: ``sh:ignoredProperties``: paths a closed shape admits without constraining them.
    ignored: set = field(default_factory=set)


def _list(graph, head) -> list:
    from rdflib import URIRef
    items = []
    while head is not None and head != URIRef(RDF_NIL):
        items.append(graph.value(head, URIRef(RDF_FIRST)))
        head = graph.value(head, URIRef(RDF_REST))
    return items


def _value(graph, shape) -> str:
    from rdflib import URIRef
    for predicate in ("class", "datatype"):
        found = graph.value(shape, URIRef(SH + predicate))
        if found is not None:
            return f"{predicate} {found}"
    listed = graph.value(shape, URIRef(SH + "in"))
    if listed is not None:
        return "in " + " ".join(sorted(str(v) for v in _list(graph, listed)))
    return "any"


def _bounds(graph, shape) -> tuple[int, int | None]:
    from rdflib import URIRef
    low = graph.value(shape, URIRef(SH + "minCount"))
    high = graph.value(shape, URIRef(SH + "maxCount"))
    return (int(low) if low is not None else 0, int(high) if high is not None else UNBOUNDED)


def shapes(graph) -> dict[str, Shape]:
    """Node shapes by IRI, with their property shapes and the choices their ``sh:or`` encode."""
    from rdflib import URIRef
    found: dict[str, Shape] = {}
    for node in graph.subjects(URIRef(RDF_TYPE), URIRef(SH + "NodeShape")):
        shape = Shape(closed=str(graph.value(node, URIRef(SH + "closed"))).lower() == "true")
        for head in graph.objects(node, URIRef(SH + "ignoredProperties")):
            shape.ignored.update(str(p) for p in _list(graph, head))
        for prop in graph.objects(node, URIRef(SH + "property")):
            path = graph.value(prop, URIRef(SH + "path"))
            if path is not None:
                low, high = _bounds(graph, prop)
                shape.properties[str(path)] = Prop(low, high, _value(graph, prop))
        for head in graph.objects(node, URIRef(SH + "or")):
            choice = Choice(optional=False)
            for alternative in _list(graph, head):
                chosen = {}
                for prop in graph.objects(alternative, URIRef(SH + "property")):
                    low, high = _bounds(graph, prop)
                    if high != 0:
                        chosen[str(graph.value(prop, URIRef(SH + "path")))] = Prop(low, high,
                                                                                    "any")
                choice.alternatives.append(chosen)
                if all(prop.min == 0 for prop in chosen.values()):
                    choice.optional = True
            shape.choices.append(choice)
        found[str(node)] = shape
    return found


# ---------------------------------------------------------------------------------------
# The comparison


def _show(value: int | None) -> str:
    return "*" if value is UNBOUNDED else str(value)


def compare(expected: dict[str, Expected], found: dict[str, Shape],
            namespace: str) -> list[Finding]:
    findings: list[Finding] = []
    for uml_class, want in sorted(expected.items()):
        iri = f"{namespace}{capitalized(uml_class)}"
        subject = capitalized(uml_class)
        shape = found.get(iri)
        for item in want.unbound:
            findings.append(Finding("MISSING", "unbound", f"{subject}: {item}",
                                    "declared in the schema, but no named UML property is it"))
        if shape is None:
            if want.abstract and not want.properties and not want.choices:
                continue  # an abstract type with no content has no instance to constrain
            findings.append(Finding("MISSING", "shape", subject, "no node shape"))
            continue
        choice_paths = {p for c in shape.choices for p in c.members}
        wanted_choice_paths = {p for c in want.choices for p in c.members}
        for path, prop in sorted(want.properties.items()):
            name = path[len(namespace):]
            if path in choice_paths:
                findings.append(Finding("EXTRA", "choice", f"{subject}: {name}",
                                        "the shapes make it an alternative; the schema does not"))
            have = shape.properties.get(path)
            if have is None and path in shape.ignored:
                # Admitted here and constrained by the shape of the class that declares it,
                # which applies to this class's instances too.
                owner = found.get(path.rsplit(".", 1)[0])
                have = owner.properties.get(path) if owner is not None else None
                if have is None:
                    continue
            if have is None:
                if shape.closed:
                    findings.append(Finding("MISSING", "property", f"{subject}: {name}",
                                            "the closed shape rejects it"))
                continue
            findings.extend(_bounds_differ(subject, name, prop, have))
            if have.value != "any" and prop.value != have.value:
                findings.append(Finding("DIFFERENT", "value", f"{subject}: {name}",
                                        f"{prop.value} vs {have.value}"))
        for path in sorted(want.clashes):
            findings.append(Finding("DIFFERENT", "value", f"{subject}: {path[len(namespace):]}",
                                    "an attribute and an element of this name are one property"))
        for choice in want.choices:
            choice = choice.normalized()
            members = set(choice.members)
            match = next((c for c in shape.choices if c.signature() == choice.signature()), None)
            if match is None:
                # A choice inherited from a base class is enforced by the base class's shape,
                # which SHACL applies to instances of its subclasses.
                for owner_iri in {path.rsplit(".", 1)[0] for path in members}:
                    owner = found.get(owner_iri)
                    if owner is not None and owner is not shape:
                        match = next((c for c in owner.choices
                                      if c.signature() == choice.signature()), None)
                        if match is not None:
                            break
            if match is not None:
                match = match.normalized()
            label = " | ".join(" & ".join(sorted(p[len(namespace):] for p in alternative))
                               for alternative in sorted(choice.alternatives, key=sorted))
            if match is None:
                findings.append(Finding("MISSING", "choice", f"{subject}: {label}",
                                        "the shapes do not encode this choice"))
                for path in sorted(members):
                    have = shape.properties.get(path)
                    if have is None and shape.closed and path not in shape.ignored:
                        findings.append(Finding("MISSING", "property",
                                                f"{subject}: {path[len(namespace):]}",
                                                "the closed shape rejects it"))
                    elif have is not None and have.min > 0:
                        findings.append(Finding(
                            "DIFFERENT", "min", f"{subject}: {path[len(namespace):]}",
                            f"one alternative of a choice, but the shapes require {have.min}"))
                continue
            if match.optional != choice.optional:
                findings.append(Finding("DIFFERENT", "choice", f"{subject}: {label}",
                                        f"optional {choice.optional} vs {match.optional}"))
            for path, prop in sorted(choice.members.items()):
                findings.extend(_bounds_differ(subject, path[len(namespace):], prop,
                                               match.members[path]))
        known = set(want.properties) | wanted_choice_paths
        for path in sorted(set(shape.properties) - known):
            findings.append(Finding("EXTRA", "property", f"{subject}: {path[len(namespace):]}",
                                    "no declaration in the schema"))
        for choice in shape.choices:
            if not any(choice.signature() == c.signature() for c in want.choices):
                label = " | ".join(sorted(p[len(namespace):] for p in choice.members))
                findings.append(Finding("EXTRA", "choice", f"{subject}: {label}",
                                        "the schema has no such choice"))
    for iri in sorted(set(found) - {f"{namespace}{capitalized(c)}" for c in expected}):
        if iri.startswith(namespace):
            findings.append(Finding("EXTRA", "shape", iri[len(namespace):],
                                    "no complex type in the schema"))
    return sorted(set(findings))


def _bounds_differ(subject: str, name: str, want: Prop, have: Prop) -> list[Finding]:
    found = []
    if want.min != have.min:
        found.append(Finding("DIFFERENT", "min", f"{subject}: {name}",
                             f"the schema requires {want.min}, the shapes {have.min}"))
    if want.max != have.max:
        found.append(Finding("DIFFERENT", "max", f"{subject}: {name}",
                             f"the schema admits {_show(want.max)}, the shapes {_show(have.max)}"))
    return found
