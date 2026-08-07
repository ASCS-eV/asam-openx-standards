#!/usr/bin/env python3
"""Content-model comparison between two XML Schemas.

``check_xsd_structural_parity.py`` counts constructs per file. A count cannot see a
compositor or a multiplicity, so a generated schema can match every count and still
accept a *different language* than the schema it is compared against. This module adds
the comparison that can see it, as pure functions over parsed schemas — no ShapeChange,
no Maven, no JDK, and stdlib-only — so it is testable on its own (``test_xsd_content_model.py``) and cheap
enough for a pull-request workflow.

For every named ``complexType`` present in both schemas, with ``xs:extension`` bases and
``xs:group`` references resolved first, three things are compared:

**The particle set** — child elements and attributes taken *together*. The two schemas
differ by design in whether a property is an XML element or an XML attribute (ASAM's
schema encodes 468 OpenDRIVE properties as attributes; the generated one encodes none,
because no model property carries an ``xsdEncodingRule`` tagged value selecting attribute
encoding). That difference is a known encoding style, so it is normalized away here
rather than measured — measuring it is what the count-based check already does.

**The compositor** — whether a particle is an alternative of an ``xs:choice``.

**The multiplicity** — ``minOccurs``, with an XML attribute's ``use="required"`` read as 1
and anything else as 0, since an attribute has no ``minOccurs`` of its own.

Four verdicts, kept apart because they mean different things and have different fixes:

``MISSING``
    The reference schema declares a particle the compared schema has no way to express.
    Content a conforming document may carry and the derived artifacts cannot represent.

``EXTRA``
    The compared schema declares a particle the reference schema does not. Content the
    derived artifacts invent.

``CONTRADICTS``
    The compared schema *demands* something the reference schema makes optional, or makes
    mandatory something the reference schema offers as one alternative among several. A
    document valid against the reference schema is **invalid** against the compared one.
    This is the only verdict that is unsound rather than incomplete.

``TYPE_MISMATCH``
    Same particle, different declared type, after the target's own ``XsdMapEntry``
    substitutions are applied to the reference side (those substitutions are configuration,
    so reporting them would be reporting the configuration as a defect).

Type names are normalized **asymmetrically**, which is easy to get wrong: see :func:`degen`.
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

XS = "http://www.w3.org/2001/XMLSchema"

#: The verdicts, in the order a report reads best: what is absent, what is invented, what
#: is unsound, what is mistyped.
VERDICTS = ("MISSING", "EXTRA", "CONTRADICTS", "TYPE_MISMATCH")

#: ``xs:`` tags this module walks. Anything else in a content model is ignored, which is
#: safe for the two ASAM schemas (neither uses ``xs:any`` in a content model, and
#: substitution groups are not used) but is the first thing to revisit for a new standard.
_CONTAINERS = ("complexContent", "simpleContent", "sequence", "all")


def _q(name: str) -> str:
    return f"{{{XS}}}{name}"


def unqualify(name: str | None) -> str:
    """Drop a namespace prefix, leaving the local name untouched."""
    return "" if not name else re.sub(r"^[A-Za-z_][\w.-]*:", "", name)


def degen(name: str) -> str:
    """Undo ShapeChange's ISO 19136 type-name suffix. **Generated side only.**

    ShapeChange emits two XSD types per UML class: ``<name>Type`` carries the content
    model and ``<name>PropertyType`` is the by-reference wrapper. Undoing that suffix is
    how a generated type is paired with the ASAM type it came from.

    Two traps, both of which produced confident wrong answers while this was being
    written, and both of which a test in ``test_xsd_content_model.py`` now pins:

    1. **Never apply this to the reference side.** ASAM has many legitimate type names
       ending in ``Type`` — ``e_roadType``, ``e_laneType``, ``e_layerType``,
       ``e_roadMarkType``. Stripping those invents type mismatches everywhere.
    2. **Strip exactly one suffix.** ShapeChange appends one, so ``e_roadTypeType``
       reduces to ``e_roadType``, not to ``e_road``.
    """
    for suffix in ("PropertyType", "Type"):
        if name.endswith(suffix) and len(name) > len(suffix):
            return name[: -len(suffix)]
    return name


def load_map_entries(path: Path) -> dict[str, str]:
    """``XsdMapEntry`` substitutions from the XSD target's own configuration.

    The four ASAM base types (``t_grEqZero``, ``t_grZero``, ``t_zeroOne``, ``t_bool``)
    carry no UML stereotype, so the target is told what to render them as. Those
    substitutions are part of the encoding, and a comparison that did not apply them
    would report each use of them as a defect in the configuration that declares them.
    """
    if not path.exists():
        return {}
    root = ET.parse(path).getroot()
    entries: dict[str, str] = {}
    for node in root.iter():
        if isinstance(node.tag, str) and node.tag.endswith("XsdMapEntry"):
            source, target = node.get("type"), node.get("xmlType")
            if source and target:
                entries[source] = target
    return entries


class Particle:
    """One thing a document may carry at a given level: an element or an attribute.

    ``min``/``max`` are normalized across both encodings, because an XML attribute has no
    ``minOccurs``: ``use="required"`` reads as ``min="1"``, anything else as ``min="0"``,
    and ``max`` is always ``"1"``. Without that, every required attribute in the reference
    schema reads as a multiplicity contradiction against the same property encoded as an
    element — which is the encoding difference this comparison exists to look past.
    """

    __slots__ = ("name", "type", "min", "max", "choice", "kind")

    def __init__(self, name: str, type_: str, min_: str, max_: str,
                 choice: int | None, kind: str) -> None:
        self.name, self.type, self.min, self.max = name, type_, min_, max_
        self.choice, self.kind = choice, kind

    def __repr__(self) -> str:  # pragma: no cover - diagnostic only
        alt = " (choice alternative)" if self.choice is not None else ""
        return f"{self.kind} {self.name}: {self.type} [{self.min}..{self.max}]{alt}"


class Schema:
    """Named ``complexType`` definitions with their content models resolved.

    ``generated`` selects the asymmetric normalization: the generated side has its
    ShapeChange suffix removed, the reference side has the target's ``XsdMapEntry``
    substitutions applied. Both end up in one shared vocabulary so names can be compared.
    """

    def __init__(self, paths: list[Path], *, generated: bool,
                 map_entries: dict[str, str] | None = None) -> None:
        self.generated = generated
        self.map_entries = map_entries or {}
        self.complex_types: dict[str, ET.Element] = {}
        self.groups: dict[str, ET.Element] = {}
        self._roots: list[ET.Element] = []
        for path in paths:
            root = ET.parse(path).getroot()
            self._roots.append(root)
            # Any depth: a property's inline anonymous type is a complexType too, and the
            # named ones are what get paired, so an unnamed one is simply skipped.
            for node in root.iter():
                if not isinstance(node.tag, str):
                    continue
                name = node.get("name")
                if not name:
                    continue
                if node.tag == _q("complexType"):
                    self.complex_types.setdefault(name, node)
                elif node.tag == _q("group"):
                    self.groups.setdefault(name, node)
        self.by_key = self._index()
        self.union_bases = {} if generated else self._union_bases()

    def _union_bases(self) -> dict[str, str]:
        """Named ``xs:simpleType`` union -> its XSD built-in member. Reference side only.

        OpenSCENARIO's schema declares every value type as a union that also admits a
        parameter reference or an expression::

            <xs:simpleType name="Double">
              <xs:union memberTypes="expression parameter xsd:double"/>

        The UML model carries the underlying type (``double``), because the parameter
        mechanism is an XML-serialization concern rather than a modelled one. So ``Double``
        against ``double`` is the schema being *more permissive at the wire level*, not a
        divergence - 366 of them on OpenSCENARIO. Derived from the reference schema itself,
        so no type name is written here and a new union type is picked up automatically.
        """
        bases: dict[str, str] = {}
        for path_root in self._roots:
            for node in path_root.iter(_q("simpleType")):
                name = node.get("name")
                if not name:
                    continue
                for union in node.findall(_q("union")):
                    members = (union.get("memberTypes") or "").split()
                    builtin = [unqualify(m) for m in members if m.startswith("xs:") or m.startswith("xsd:")]
                    if len(builtin) == 1:
                        bases[name] = builtin[0]
        return bases

    def _index(self) -> dict[str, str]:
        """Pairing key -> the type name to read the content model from.

        ``<name>Type`` and ``<name>PropertyType`` reduce to the same key, and only the
        first carries content: the ``PropertyType`` wrapper is empty by design. Pairing
        against the wrapper makes every particle of every type report as ``MISSING``, so
        the content type is chosen explicitly rather than by iteration order.
        """
        index: dict[str, str] = {}
        for name in self.complex_types:
            key = self.key(name)
            incumbent = index.get(key)
            if incumbent is None:
                index[key] = name
            elif incumbent.endswith("PropertyType") and not name.endswith("PropertyType"):
                index[key] = name
        return index

    def key(self, name: str) -> str:
        """The name under which this schema's types pair with the other schema's."""
        return degen(name) if self.generated else name

    def normalize_type(self, name: str | None) -> str:
        local = unqualify(name)
        if not local:
            return ""
        if self.generated:
            return degen(local)
        # Configuration substitutions first, then the schema's own parameter/expression
        # unions, so a mapped type is not re-resolved by a coincidentally-named union.
        substituted = self.map_entries.get(local)
        if substituted is not None:
            return substituted
        return self.union_bases.get(local, local)

    def particles(self, type_name: str) -> dict[str, Particle]:
        """Every particle a document may carry inside ``type_name``, inherited included."""
        found: dict[str, Particle] = {}
        self._walk_type(type_name, found, set(), [0])
        return found

    def _walk_type(self, type_name: str, found: dict[str, Particle],
                   seen: set[str], counter: list[int]) -> None:
        node = self.complex_types.get(type_name)
        if node is None or type_name in seen:
            return
        seen.add(type_name)
        self._walk(node, found, seen, counter, None)

    def _walk(self, node: ET.Element, found: dict[str, Particle], seen: set[str],
              counter: list[int], choice_id: int | None) -> None:
        """Collect particles. ``counter`` numbers choice groups so two alternatives of the
        same choice are distinguishable from two particles in unrelated choices."""
        for child in node:
            if not isinstance(child.tag, str):
                continue
            tag = child.tag
            if tag == _q("extension"):
                # Inherited content is content a document carries here, so it is compared
                # here. Both schemas encode the hierarchy, so both resolve the same way.
                self._walk_type(unqualify(child.get("base")), found, seen, counter)
                self._walk(child, found, seen, counter, choice_id)
            elif tag in tuple(_q(t) for t in _CONTAINERS):
                self._walk(child, found, seen, counter, choice_id)
            elif tag == _q("choice"):
                counter[0] += 1
                self._walk(child, found, seen, counter, counter[0])
            elif tag == _q("group"):
                ref = unqualify(child.get("ref"))
                if ref in self.groups:
                    self._walk(self.groups[ref], found, seen, counter, choice_id)
                else:
                    # An unresolvable group reference is recorded rather than dropped: a
                    # silently ignored group is content that vanishes from the comparison.
                    marker = f"<group:{ref}>"
                    found.setdefault(marker, Particle(
                        marker, ref, child.get("minOccurs", "1"),
                        child.get("maxOccurs", "1"), choice_id, "group"))
            elif tag == _q("element"):
                name = child.get("name")
                if not name:
                    continue  # a ref= element; neither ASAM schema uses one in a content model
                declared = self.normalize_type(child.get("type"))
                if not declared:
                    declared = "<inline>" if child.find(_q("complexType")) is not None else ""
                found.setdefault(name, Particle(
                    name, declared, child.get("minOccurs", "1"),
                    child.get("maxOccurs", "1"), choice_id, "element"))
            elif tag == _q("attribute"):
                name = child.get("name")
                if not name:
                    continue
                found.setdefault(name, Particle(
                    name, self.normalize_type(child.get("type")),
                    "1" if child.get("use") == "required" else "0", "1",
                    choice_id, "attribute"))


def _plural_forms(name: str) -> tuple[str, ...]:
    """Candidate plural spellings of a UML role name for a multi-valued property."""
    return (name, name + "s", name + "es", re.sub(r"y$", "ies", name))


def pair_names(reference: dict[str, Particle],
               generated: dict[str, Particle]) -> dict[str, str]:
    """Reference particle name -> generated particle name, for names that differ.

    ASAM's schemas name an XML element; ShapeChange names it after the UML **role**. In
    OpenDRIVE the two coincide, so this does nothing. In OpenSCENARIO they systematically
    differ: the element is UpperCamelCase and singular (``<ManeuverGroup>``) while the role
    is lowerCamelCase and, for a multi-valued property, plural (``maneuverGroups``).
    Without pairing them, one particle reports as both ``MISSING`` and ``EXTRA`` - 412 and
    388 such pairs on OpenSCENARIO, which buries any real finding.

    Pairing is deliberately conservative: a candidate must be **unique**, and a generated
    name already matching a reference name exactly is never re-paired. Anything not paired
    stays reported, because a wrong pairing hides a real difference and is worse than a
    duplicated report.
    """
    pairs: dict[str, str] = {}
    unmatched_gen = set(generated) - set(reference)
    for ref_name in sorted(set(reference) - set(generated)):
        candidates = {c for c in _plural_forms(ref_name[:1].lower() + ref_name[1:])
                      if c in unmatched_gen}
        # A type-compatible candidate is preferred, which disambiguates two roles of the
        # same target type (StartTrigger/StopTrigger both typed Trigger).
        if len(candidates) != 1:
            typed = {c for c in candidates if generated[c].type == reference[ref_name].type}
            candidates = typed if len(typed) == 1 else candidates
        if len(candidates) == 1:
            chosen = candidates.pop()
            pairs[ref_name] = chosen
            unmatched_gen.discard(chosen)
    return pairs


def compare(generated: Schema, reference: Schema) -> dict[str, list[tuple]]:
    """Compare every complexType present in both schemas. See the module docstring."""
    findings: dict[str, list[tuple]] = {verdict: [] for verdict in VERDICTS}
    shared = sorted(n for n in reference.complex_types if reference.key(n) in generated.by_key)
    findings["shared_types"] = shared  # type: ignore[assignment]

    for type_name in shared:
        ref = reference.particles(type_name)
        gen_raw = generated.particles(generated.by_key[reference.key(type_name)])
        # Re-key the generated particles under the reference's names where the two
        # conventions differ, so a single particle is compared once rather than reported
        # twice under two spellings.
        inverse = {generated_name: reference_name
                   for reference_name, generated_name in pair_names(ref, gen_raw).items()}
        gen = {inverse.get(name, name): particle for name, particle in gen_raw.items()}

        for name in sorted(set(ref) - set(gen)):
            findings["MISSING"].append((type_name, name, ref[name].type, ref[name].kind))
        for name in sorted(set(gen) - set(ref)):
            findings["EXTRA"].append((type_name, name, gen[name].type, gen[name].kind))

        for name in sorted(set(ref) & set(gen)):
            r, g = ref[name], gen[name]
            if r.type != g.type and not r.type.startswith("<") and not g.type.startswith("<"):
                findings["TYPE_MISMATCH"].append((type_name, name, r.type, g.type))

            # Only a generated schema that demands MORE than the reference schema can
            # reject a conforming document. The reverse — generated is laxer — is
            # incompleteness, already reported as MISSING or visible in the counts, and
            # is deliberately not called a contradiction.
            if r.choice is not None and g.choice is None and g.min != "0":
                findings["CONTRADICTS"].append((
                    type_name, name, "reference: xs:choice alternative",
                    f"generated: mandatory (minOccurs={g.min})"))
            elif g.choice is not None and r.choice is None and r.min != "0":
                findings["CONTRADICTS"].append((
                    type_name, name, f"reference: mandatory (minOccurs={r.min})",
                    "generated: xs:choice alternative"))
            elif r.choice is None and g.choice is None and r.min == "0" and g.min != "0":
                findings["CONTRADICTS"].append((
                    type_name, name, "reference: optional",
                    f"generated: mandatory (minOccurs={g.min})"))
    return findings


def finding_key(finding: tuple) -> str:
    """A stable one-line identity for a finding, for baselining."""
    return " :: ".join(str(part) for part in finding)


class VacuousComparison(RuntimeError):
    """Raised when there is nothing to compare.

    An oracle that reports "no findings" because it found no input is worse than no
    oracle: it passes, and it passes loudest exactly when it has been mis-wired. This was
    not hypothetical - the first wiring of this module into the parity check globbed
    ``*.xsd`` non-recursively while ShapeChange nests its output one directory deeper, so
    the comparison loaded zero schemas, reported zero findings for all four verdicts, wrote
    an empty baseline and printed PASS.
    """


def load(generated_dir: Path, reference_dir: Path,
         map_entries_path: Path | None = None) -> dict[str, list[tuple]]:
    """Parse both schema directories and compare them.

    Recursive: ShapeChange nests its output under a subdirectory named after the
    pseudo-package wrapping the input model, and that name is not a documented contract.
    """
    entries = load_map_entries(map_entries_path) if map_entries_path else {}
    generated_files = sorted(generated_dir.rglob("*.xsd"))
    reference_files = sorted(reference_dir.rglob("*.xsd"))
    if not generated_files:
        raise VacuousComparison(f"no .xsd files under {generated_dir}")
    if not reference_files:
        raise VacuousComparison(f"no .xsd files under {reference_dir}")

    generated = Schema(generated_files, generated=True)
    reference = Schema(reference_files, generated=False, map_entries=entries)
    findings = compare(generated, reference)
    if not findings["shared_types"]:
        raise VacuousComparison(
            f"{len(generated_files)} generated and {len(reference_files)} reference schema "
            f"file(s) parsed ({len(generated.complex_types)} and "
            f"{len(reference.complex_types)} named complexTypes), but not one type name "
            "pairs between them. Either the pairing key is wrong or the wrong directories "
            "were passed; reporting zero findings here would be a false pass.")
    return findings
