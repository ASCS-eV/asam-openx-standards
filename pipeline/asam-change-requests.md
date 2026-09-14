# Change requests to ASAM

Defects and questions about ASAM's normative Enterprise Architect models, found by generating
open artifacts from them. This file is the authoritative list: it is version-controlled,
reviewable, and every claim in it is reproducible from files committed in this repository.

Tracked in [#6](https://github.com/ASCS-eV/asam-openx-standards/issues/6).

## How to verify any claim here

The Enterprise Architect projects are committed under `standards/*/uml/source/`, and a `.qeax`
is a SQLite database, so **no Enterprise Architect licence is needed** — only the file:

```bash
git lfs pull
sqlite3 standards/asam-opendrive/uml/source/ASAM_OpenDRIVE.qeax \
  "SELECT Client, Description FROM t_xref WHERE Name = 'Stereotypes';"
```

Claims about the *export* are reproducible from the committed `standards/*/uml/*.scxml`, which
is plain XML. Each entry below states which of the two it rests on.

## Status

Nothing here has been sent to ASAM yet. Before sending, re-check each entry against the current
export — this list has already had **two** requests withdrawn after such a check, both of which
turned out to describe defects in our own pipeline.

| # | Standard | Kind | Summary |
|---|---|---|---|
| [1](#1-union-alternatives-are-encoded-as-supertypes) | OpenDRIVE | Defect | Union member types attached as supertypes, and never all of them |
| [2](#2-the-root-element-has-no-content-model) | OpenDRIVE | Defect | Root element has no content model |
| [3](#3-xsdsimpletype-is-spelled-two-ways) | OpenDRIVE | Defect | `XSDSimpleType` vs `XSDsimpleType` casing |
| [4](#4-membernames-is-declared-everywhere-and-never-populated) | Both | Defect | `memberNames` declared on 170 classes, populated on none |
| [5](#5-activatecontrolleractionobjectcontrollerref-is-an-association-where-the-schema-says-attribute) | OpenSCENARIO | Defect | Reference modelled as an association |
| [6](#6-use-is-declared-throughout-openscenario-and-populated-nowhere) | OpenSCENARIO | Defect | `use` declared on 165 elements, populated on none |
| [7](#7-the-two-standards-use-different-names-for-the-same-concepts) | Both | Harmonisation | Divergent tag and stereotype names |
| [8](#8-do-all-seven-sub-packages-need-the-same-targetnamespace) | OpenDRIVE | Question | Seven packages share one `targetNamespace` |
| [9](#9-does-openscenario-xml-intend-to-carry-no-constraints) | OpenSCENARIO | Question | No constraints, where OpenDRIVE has 24 |

Two further requests have been **withdrawn** after they turned out to describe defects in our own
pipeline rather than in ASAM's models — see [Withdrawn](#withdrawn). Read that section before
adding anything here.

---

## 1. Union alternatives are encoded as supertypes

**Source: the export and the normative schema.** All four OpenDRIVE union classes carry the
`XSDunion` stereotype and **no properties at all**. All four attach their member types — where
they attach them at all — as *supertypes*, which is the inverse of a union: a union is a choice
among its members, a supertype is a generalisation of them. Three of the four also attach only
part of their member list.

| Class | Members in the schema | Attached as supertypes in the model | Properties |
|---|---|---|---:|
| `e_unit` | `e_unitDistance`, `e_unitSpeed`, `e_unitMass`, `e_unitSlope` | *(none)* | **0** |
| `t_maxSpeed` | `t_grEqZero`, `e_maxSpeedString` | `t_grEqZero` only | **0** |
| `e_countryCode` | `e_countryCode_iso3166alpha2`, `e_countryCode_iso3166alpha3_deprecated`, `e_countryCode_deprecated` | the first two only | **0** |
| `t_grEqZeroOrContactPoint` | `t_grZero`, `e_contactPoint` | both | **0** |

So only `t_grEqZeroOrContactPoint` states its full member list, and `e_unit` states nothing at
all: the schema declares it a union of four types and the model relates it to none of them.
`e_maxSpeedString` and `e_countryCode_deprecated` exist as classes in the model but are attached
to nothing. Even where the list is complete the relationship is still wrong way round.

ShapeChange reports the supertype encoding itself:

> The class 'e_countryCode' is modelled as a feature type, object type, data type, mixin, or
> union, but has more than one supertype of the same kind.

**Why it matters.** Seven OpenDRIVE attributes are typed by these four classes, including
`t_road_signals_signal.unit`, `t_road_type.country` and `t_road_type_speed.max`. Nothing derived
from the model can constrain those values the way the schema does. In the generated OWL,
`odr:E_unit` is a bare class and `odr:E_countryCode` is asserted to be a subclass of two of its
own alternatives.

**Requested change.** State the member list. In schema terms these are
`<xs:simpleType><xs:union memberTypes="…"/></xs:simpleType>` — unions of *datatypes*, used as
the types of XML **attributes** — so the fix is to relate each union class to all of its member
types with a relationship that means "is one of", not "is a generalisation of". Either a UML
union with one attribute per member type, or an EA-level union construct that survives export,
would do; what matters is that the alternatives are members rather than supertypes.

**Note on the sibling standard.** OpenSCENARIO XML applies the UML standard `«union»` stereotype
to 48 classes, each with zero supertypes and one property per alternative, and those do reach
the ontology as `owl:unionOf`. It is tempting to cite that as the model to copy, and this
document previously did — but the two are **not the same construct**: OpenSCENARIO's unions are
`xsd:complexType`/`xsd:group` with an `xs:choice` of *elements*, whereas OpenDRIVE's are simple-type
unions of *datatypes* used as attribute types. Re-encoding `e_unit` as a complex type would make
it unusable as the type of `<xs:attribute name="unit">`. The OpenSCENARIO encoding is also not
defect-free: `pipeline/openscenario-owl.config.xml` records seven classes that carry XML
attributes outside the choice, and in four of them — `Action`, `Color`, `Condition` and
`ControllerDistributionEntry` — that attribute is `use="required"`, so the choice is
unsatisfiable. Those four are the source of 6 of the 20 accepted `CONTRADICTS` in
`openscenario-xsd-content-baseline.json`; three more come from `EntityAction`,
`ParameterAction` and `VariableAction`, where the schema's required attribute is modelled as an
association end instead — the pattern of [request 5](#5-activatecontrolleractionobjectcontrollerref-is-an-association-where-the-schema-says-attribute).

## 2. The root element has no content model

**Source: the export.** The `OpenDRIVE` class exists but has **no properties**, appears in no
association, and is **the type of no property** (0 occurrences as a `typeId`). For contrast
`t_road` is the type of 11 properties in the same model.

The normative schema's root element composes `header`, `road`, `controller`, `junction`,
`junctionGroup`, `station`, `g_additionalData` and `vmsGroup`. None of that composition exists
in the UML.

**Why it matters.** Every other level of the document *is* modelled, so the gap is specifically
at the root — which means an artifact derived from the model has no document entry point. A
consumer cannot express "this file is an OpenDRIVE file" in terms of the model.

**Requested change.** Add the eight compositions with the multiplicities from
`OpenDRIVE_Core.xsd`.

## 3. `XSDSimpleType` is spelled two ways

**Source: the `.qeax` and the export.** The OpenDRIVE model applies `XSDsimpleType` to five
classes and `XSDSimpleType` — capital S — to one: `t_junction_grid_position_list`.

**Why it matters.** Any consumer selecting classes by stereotype name silently misses one. It
is invisible in Enterprise Architect's UI and costs nothing to fix.

**Requested change.** Normalise to `XSDsimpleType`.

## 4. `memberNames` is declared everywhere and never populated

**Source: the `.qeax`.** The tagged value `memberNames` is declared on **98 OpenDRIVE classes**
and **72 OpenSCENARIO classes**, and carries a value on **none** of them.

```sql
SELECT COUNT(*) FROM t_objectproperties WHERE Property = 'memberNames';
SELECT COUNT(*) FROM t_objectproperties
 WHERE Property = 'memberNames' AND TRIM(COALESCE(Value,'')) <> '';
```

**Why it matters.** It is dead metadata that every consumer must decide how to treat. This
repository excludes it from the export for that reason.

**Requested change.** Populate it or remove it.

## 5. `ActivateControllerAction.objectControllerRef` is an association where the schema says attribute

**Source: the export and the normative schema.** The model encodes `objectControllerRef` as an
**association** to the `ObjectController` class. The normative schema declares:

```xml
<xsd:complexType name="ActivateControllerAction">
    <xsd:attribute name="objectControllerRef" type="String"/>
```

— a plain string name reference, not a containment or an association.

**Why it matters.** The two say different things about the document. An association implies a
structural relationship a validator can traverse; the schema describes an unresolved name. A
model-derived artifact will require an object where the document carries a string.

**Requested change.** Model it as an attribute of type `String`, matching the schema, or
confirm that the association is intended and the schema is the thing to change.

## 6. `use` is declared throughout OpenSCENARIO and populated nowhere

**Source: the `.qeax`.** OpenSCENARIO declares the tagged value `use` on **165 elements** — 133
attributes and 32 connectors — and leaves **all 165 blank** (132 `NULL`, one empty string, 32
`NULL`). OpenDRIVE declares it on 465 and populates **366**: 228 `required` and 138 `optional`.

**Why it matters.** It is dead metadata in one standard and load-bearing in the other, so a tool
reading both must know to ignore it for one of them. Either it was intended to carry something
here and does not, or it should be removed.

**Not an argument for this request.** OpenSCENARIO does *not* lose the ability to express
requiredness: it carries it in UML multiplicity instead, completely and correctly. Every one of
the **443** attribute declarations inside a `complexType` in `OpenSCENARIO.xsd` was compared
against the model's multiplicity for the same property, and **443 of 443 agree** — absent
multiplicity corresponds to `use="required"`, `0..1` to optional. The generated SHACL reflects
it: 588 `sh:minCount` constraints, with `AngleCondition.angleType` carrying `sh:minCount 1` and
`AngleCondition.coordinateSystem` carrying none.

**Requested change.** Populate `use`, or remove it.

## 7. The two standards use different names for the same concepts

**Source: the `.qeax` and the export.** Identical concepts carry different names in the two
models:

| Concept | OpenDRIVE | OpenSCENARIO XML |
|---|---|---|
| Per-element version provenance | `introducedAtVersion` — 242 declared, 242 populated | `withVersion` — 41 declared, **39** populated |
| Union | `XSDunion` stereotype, 4 classes | `«union»`, UML standard, 48 classes |

**Why it matters.** Every tool that consumes both standards needs per-standard special cases for
no modelling reason. This repository's two export configurations differ in exactly these names,
among other things.

**Requested change.** Harmonise the version-provenance tag on one spelling. The union spelling
is a harder question than it looks and is discussed in request 1 — the two standards' unions are
different XSD constructs, so a common stereotype name would still not make them the same thing.

## 8. Do all seven sub-packages need the same `targetNamespace`?

**A question, not a defect. Source: the export.** Seven OpenDRIVE packages carry the `XSDschema`
stereotype and the same `targetNamespace`. That is reasonable for a seven-file schema split, but
ShapeChange treats every `targetNamespace`-tagged package as a distinct schema, so it finds eight
schemas resolving to one namespace and reports 227 of 238 classes as "no schema package was
found". The generated ontology is complete regardless; the errors are tolerated by an allowlist.

Would carrying `targetNamespace` only on the parent package still produce the intended seven-file
schema? If ASAM's structure must stay as it is, this becomes a ShapeChange feature request
instead — treating packages that share a target namespace as one schema.

OpenSCENARIO is the opposite case: it declares no `targetNamespace` anywhere, so exactly one
schema resolves and the run is clean.

## 9. Does OpenSCENARIO XML intend to carry no constraints?

**A question, not a defect. Source: the `.qeax`.** OpenSCENARIO's constraint tables are empty —
`t_objectconstraint`, `t_attributeconstraints`, `t_connectorconstraint` and `t_operationpres`
all have zero rows.

OpenDRIVE, by contrast, carries **24 approved invariants on 11 classes**, expressing mutual
exclusivity, conditional applicability and identifier uniqueness — the semantics that neither
the schema's structure nor a UML multiplicity can state.

Is the absence in OpenSCENARIO intended? If it is, SHACL derived from that standard is
structural-only by construction and consumers should be told so. If it is not, the same class of
constraint is presumably being enforced somewhere outside the model.

*Note: an earlier version of this request asked ASAM whether either model carried constraints at
all. That was our own configuration discarding OpenDRIVE's — see the withdrawn section below.*

---

## Withdrawn

Kept for the record, because the reasoning matters more than the conclusion. **Both withdrawn
entries were our own defects mistaken for ASAM's**, which is why every active request above
states the file it rests on and has been re-checked against the current export.

### `t_road_planView_geometry` requires all five geometry primitives — **withdrawn**

This was the largest entry on the list: the generated schema and SHACL required all five
geometry primitives where the normative schema declares an `xs:choice`, so every conforming
`.xodr` was rejected — `CONTRADICTS` = 91 for OpenDRIVE and 20 for OpenSCENARIO.

**It was not an ASAM defect.** The EA models carry a `modelGroup` tagged value holding the XSD
content-model kind, and `t_road_planView_geometry` carries `modelGroup = choice`. Our export was
dropping the tagged value, because it is not in ShapeChange's well-known set. Four OpenDRIVE
classes and 55 OpenSCENARIO classes are `choice`, plus 56 OpenSCENARIO `all`, and all of them
were affected.

The export now carries `modelGroup`; honouring it in the OWL, SHACL and XSD targets is
[#37](https://github.com/ASCS-eV/asam-openx-standards/issues/37).

### Does the OpenDRIVE model carry constraints? — **withdrawn**

This asked ASAM whether their model carried any constraints, reasoning that because none reach
the export, none exist. **Both halves were wrong.**

OpenDRIVE carries **24 approved `Invariant` constraints on 11 classes**, including twelve
`@type`-conditional invariants on `t_road_objects_object` alone, plus this mutual-exclusivity
rule on the same class:

```
not(@radius or @width or @length)
  or (@radius and not(@width or @length))
  or (@width and @length and not(@radius))
```

Our export sets `checkingConstraints="disabled"`, and in ShapeChange that disables constraint
**loading**, not checking — the accessor is named `constraintLoadingEnabled()`, and
`ClassInfoEA.validateConstraintsCache()` returns before ever calling `GetConstraints()`. So the
constraints could not have reached the export under any circumstances.

Recovering them is [#44](https://github.com/ASCS-eV/asam-openx-standards/issues/44). What
remains ASAM-facing is only the cross-standard question in request 9 above.

**The lesson generalises:** a difference between our artifacts and ASAM's schema is evidence of
a defect *somewhere*, and the export is the first place to look. Twice now the answer has been
our own configuration.
