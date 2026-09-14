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
export — this list has already had one request withdrawn after such a check.

| # | Standard | Kind | Summary |
|---|---|---|---|
| [1](#1-union-alternatives-are-encoded-as-supertypes) | OpenDRIVE | Defect | Union alternatives encoded as supertypes, not properties |
| [2](#2-the-root-element-has-no-content-model) | OpenDRIVE | Defect | Root element has no content model |
| [3](#3-xsdsimpletype-is-spelled-two-ways) | OpenDRIVE | Defect | `XSDSimpleType` vs `XSDsimpleType` casing |
| [4](#4-membernames-is-declared-everywhere-and-never-populated) | Both | Defect | `memberNames` declared on 170 classes, always empty |
| [5](#5-activatecontrolleractionobjectcontrollerref-is-an-association-where-the-schema-says-attribute) | OpenSCENARIO | Defect | Reference modelled as an association |
| [6](#6-use-is-present-on-every-attribute-and-populated-on-none) | OpenSCENARIO | Defect | `use` present on 165 attributes, blank on all |
| [7](#7-the-two-standards-use-different-names-for-the-same-concepts) | Both | Harmonisation | Divergent tag and stereotype names |
| [8](#8-do-all-seven-sub-packages-need-the-same-targetnamespace) | OpenDRIVE | Question | Seven packages share one `targetNamespace` |
| [9](#9-does-the-model-carry-ocl-constraints) | Both | Question | No constraints reach the export |

---

## 1. Union alternatives are encoded as supertypes

**Source: the export.** All four OpenDRIVE union classes carry the `XSDunion` stereotype and
**no properties at all**. Three of the four attach their alternatives as *supertypes*, which is
the inverse of a union — a union is a choice among its members, a supertype is a generalisation
of them.

| Class | Supertypes in the model | Properties |
|---|---|---:|
| `e_unit` | *(none)* | **0** |
| `t_maxSpeed` | `t_grEqZero` | **0** |
| `e_countryCode` | `e_countryCode_iso3166alpha2`, `e_countryCode_iso3166alpha3_deprecated` | **0** |
| `t_grEqZeroOrContactPoint` | `e_contactPoint`, `t_grZero` | **0** |

`e_unit` is empty in both directions: the normative schema declares it a union of
`e_unitDistance`, `e_unitSpeed`, `e_unitMass` and `e_unitSlope`, and the model relates it to
none of them.

ShapeChange reports the supertype encoding itself:

> The class 'e_countryCode' is modelled as a feature type, object type, data type, mixin, or
> union, but has more than one supertype of the same kind.

**Why it matters.** Seven OpenDRIVE attributes are typed by these four classes, including
`t_road_signals_signal.unit`, `t_road_type.country` and `t_road_type_speed.max`. Nothing derived
from the model can constrain those values the way the schema does. In the generated OWL,
`odr:E_unit` is a bare class and `odr:E_countryCode` is asserted to be a subclass of two of its
own alternatives.

**The strongest argument is ASAM's own sibling standard.** OpenSCENARIO XML encodes the same
concept correctly, 48 times: `«union»` classes with **zero supertypes** and one property per
alternative — `Action`, `AnimationType` and `AppearanceAction` all have 4, 4 and 2 properties and
no supertypes. That is exactly the shape ShapeChange's `rule-owl-cls-union` consumes, and it is
why OpenSCENARIO produces 48 `owl:unionOf` axioms while OpenDRIVE produces none.

**Requested change.** Encode the four OpenDRIVE unions the way OpenSCENARIO already encodes
its 48: apply `«union»`, remove the generalisations, and add one attribute per member type at
multiplicity 1.

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

**Requested change.** Add the seven compositions with the multiplicities from
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

## 6. `use` is present on every attribute and populated on none

**Source: the `.qeax`.** OpenSCENARIO declares the tagged value `use` on **165 attributes and
connectors** and leaves **all 165 blank**. OpenDRIVE declares it on 465 and populates **366**
with `required` or `optional`.

**Why it matters.** `use` is how the model states whether an XML attribute is required.
OpenSCENARIO therefore cannot express requiredness at all, so nothing derived from it can
distinguish a mandatory attribute from an optional one. As in request 1, the same organisation
does this correctly in the sibling standard.

**Requested change.** Populate `use` in OpenSCENARIO, or remove it and state that requiredness
is carried only by the schema.

## 7. The two standards use different names for the same concepts

**Source: the `.qeax` and the export.** Identical concepts carry different names in the two
models:

| Concept | OpenDRIVE | OpenSCENARIO XML |
|---|---|---|
| Per-element version provenance | `introducedAtVersion` (242 values) | `withVersion` (41 values) |
| Union | `XSDunion` stereotype (4) | `«union»`, UML standard (48) |

**Why it matters.** Every tool that consumes both standards needs per-standard special cases for
no modelling reason. This repository maintains two export configurations that differ only in
these names.

**Requested change.** Harmonise on one spelling of each. For unions the UML standard `«union»`
is the better target, since it is what tooling already recognises — and it is what OpenSCENARIO
already does.

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

## 9. Does the model carry OCL constraints?

**A question, not a defect. Source: the export.** Neither export contains a single constraint —
zero `<sc:constraints>` elements and zero `OclConstraint`s in both. ShapeChange's
`checkingConstraints=disabled` only skips *analysis*, and `includeConstraintDescriptions` only
affects `<description>` children, so absence here suggests absence in the model rather than an
export setting.

If that is intended, then SHACL derived from these models is structural-only by construction,
and consumers should be told so. If it is not intended, the constraints are being lost somewhere
before the export.

---

## Withdrawn

Kept for the record, because the reasoning matters more than the conclusion.

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

**The lesson generalises:** a difference between our artifacts and ASAM's schema is evidence of
a defect *somewhere*, and the export is the first place to look. Everything on the active list
above has been re-checked against the current export for exactly this reason.
