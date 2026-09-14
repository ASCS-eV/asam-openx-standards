# ASAM OpenDRIVE® UML Model (SCXML) — V1.9.0

The **open, tool-neutral UML model** of ASAM OpenDRIVE® V1.9.0, exported once from
Enterprise Architect and committed here so that every downstream generation step —
OWL, SHACL, XSD — runs **without an Enterprise Architect licence**.

**These files are not original works of this project.** They are derived from ASAM's
`ASAM_OpenDRIVE.qeax` Enterprise Architect project. Copyright © ASAM e.V., 2026.
Redistributed under the ASAM Unrestricted Distribution Clause; see the repository
[LICENSE](../../../LICENSE).

## Provenance

| Field | Value |
|---|---|
| Standard | ASAM OpenDRIVE® |
| Version | **V1.9.0** — matches the normative schema in [`../schema/`](../schema/README.md) |
| Origin | [`source/ASAM_OpenDRIVE.qeax`](source/README.md) (Enterprise Architect project, committed) |
| Exported by | ShapeChange built from source at commit [`f4ee27b5`](https://github.com/ASCS-eV/ShapeChange/commit/f4ee27b5) (`ASCS-eV/ShapeChange`, branch `feature/asam-pipeline` = upstream `next` `7a44ce20` plus one carried commit that touches only the OWL target), `ModelExport` target, `inputModelType=EA7`, `zipOutput=true` |
| Producer header | `scxmlProducer="ShapeChange"`, `scxmlProducerVersion="4.1.0-SNAPSHOT"` |
| Classes | 238 |
| Stereotypes | 775 — the EA XML Schema profile, carried via `addStereotypes` |
| Tagged values | 1,711 — a curated set, carried via `representTaggedValues` |

### Why a commit, not a numbered ShapeChange release

The `4.0.0` release cannot build the EA/`eaapi` module from source at all — that only
became possible once the EA module upstream became an optional Maven profile (`ea`,
active unless `-DskipEa` is passed). That change is on `next` but not yet in a numbered
release, so we cite the exact commit above instead. We verified
it changes nothing in this export except the producer-version string in the header — see
[`export-model-to-scxml.config.xml`](export-model-to-scxml.config.xml) and
[Reproducing the export](#reproducing-the-export-requires-ea-once) below for the full
from-source build. The maintainer has indicated a `4.1.0` release is planned; we intend to
switch this citation to that release once it ships.

### How the version is established

The export carries no ASAM version stamp of its own — the producer version in the file
header identifies ShapeChange, not the standard. The revision is therefore determined
against the normative schema in `../schema/`, which is the version-pinned artifact:

- All **231** named types of the V1.9.0 XSD are present in the model; none is missing.
- That set includes all **10** types V1.9.0 added over V1.8.0 — `e_layerType`,
  `e_personCategory`, `e_vehicleCategory`, the `t_road_objects_object_outlines_outline_curveLocal*`
  family and the `t_signals_semantics_{animal,person,vehicle}` family — so the model is
  V1.9.0 and not the previous revision.
- All **56** enumerations of the V1.9.0 XSD are present with literals that match the schema
  exactly — same names, same counts, no discrepancy in any of them. `e_laneType` carries all
  31 values.

The model additionally declares 7 classes that have no named XSD counterpart. These are
UML-level constructs that XML Schema expresses differently, not model/schema drift:

| Class | Why it has no named XSD type |
|---|---|
| `OpenDRIVE` | the root **element**; its type is anonymous in the XSD |
| `g_additionalData` | an XSD **group**, not a type |
| `userDataContent` | the free/mixed content of `userData`, which the XSD expresses as `xs:any` rather than a named type |
| `LaneGeometry`, `t_outline_geometry`, `t_physicalPosition`, `t_polyline_geometry` | abstractions the schema inlines |

### Known encoding gaps

Things the XSD expresses and the generated artifacts do not yet reflect. The first two
originate in the Enterprise Architect model, so the export reproduces them faithfully and no
ShapeChange configuration repairs them. The third is different in kind and was previously
misfiled here: the model **does** express it and the export now carries it, but nothing
downstream consumes it yet.

**XSD union types carry no union semantics.** The schema declares four unions. The export now
carries their `XSDunion` stereotype, but the member types — where they appear at all — appear
as *supertypes*, which is the inverse of a union:

| XSD union | Members in the XSD | In the model |
|---|---|---|
| `e_unit` | `e_unitDistance`, `e_unitSpeed`, `e_unitMass`, `e_unitSlope` | empty class, no members |
| `t_maxSpeed` | `t_grEqZero`, `e_maxSpeedString` | one supertype; `e_maxSpeedString` absent |
| `e_countryCode` | 3 member types | two supertypes; `e_countryCode_deprecated` absent |
| `t_grEqZeroOrContactPoint` | `t_grZero`, `e_contactPoint` | two supertypes |

ShapeChange reports this itself when the model is processed — *"is modelled as a feature
type, object type, data type, mixin, or union, but has more than one supertype of the same
kind"*. Seven attributes are typed by these four classes, including
`t_road_signals_signal.unit`, `t_road_type.country` and `t_road_type_speed.max`, so anything
generated from the model cannot constrain those values the way the XSD does.

This looks like an oversight in the OpenDRIVE model rather than an ASAM-wide convention,
because **the sibling OpenSCENARIO XML model does it correctly**: it carries 48 `«union»`
classes, each with one property per alternative, which is exactly the shape ShapeChange's
`rule-owl-cls-union` consumes. OpenDRIVE carries none. Encoding these four the same way
would fix it at the source, and is a request to ASAM rather than something a downstream
configuration can repair.

**The root element has no content model.** `OpenDRIVE` appears in no association and is the
type of no property. The XSD root element composes `header`, `road`, `controller`,
`junction`, `junctionGroup`, `station`, `g_additionalData` and `vmsGroup`; none of that
composition exists in the UML, so a model-derived artifact has no document entry point.

**Exclusive choice is carried but not yet honoured.** The model marks four classes
`modelGroup = choice`, including `t_road_planView_geometry`, whose XSD content model is an
`xs:choice` of five geometry primitives. The export now carries this, but the OWL, SHACL and
XSD targets still generate a sequence requiring **all** members, so a generated artifact
rejects documents the normative schema accepts. This was previously recorded — here and in the
issue tracker — as an ASAM modelling defect; it is not. The information is in ASAM's model and
was being discarded by the export. Tracked in
[#37](https://github.com/ASCS-eV/asam-openx-standards/issues/37).

## Files

| File | What it is |
|------|------------|
| `opendrive.scxml` | The model in ShapeChange SCXML (plain XML, diff-friendly). **Source of truth** for all downstream generation. |
| `opendrive.scxml.zip` | The `ModelExport` artifact exactly as ShapeChange wrote it (`zipOutput=true`), directly consumable as a ShapeChange `inputFile`. |
| `export-model-to-scxml.config.xml` | The ShapeChange `ModelExport` configuration that produced both files **from EA**. |

### `.scxml` and `.scxml.zip` hold identical bytes

The zip's `opendrive.xml` entry is **byte-identical** to `opendrive.scxml`. Earlier exports
differed by line endings — the export ran on Windows and produced CRLF, which had to be
normalised before committing — but the exporter now writes LF on every platform, so the two
agree without conversion:

| Artifact | Bytes | CR bytes | SHA-256 (truncated) |
|---|---:|---:|---|
| `opendrive.scxml` | 1,900,834 | 0 | `be10c8d8c25bb8e8…` |
| `opendrive.xml` inside the zip | 1,900,834 | 0 | `be10c8d8c25bb8e8…` |
| `opendrive.scxml.zip` | 88,899 | — | `6ce4295b166d760b…` |

Use `opendrive.scxml` unless a tool requires the zip. The zip entry is named for the standard
rather than the exporter because the configuration sets `outputFilename`; it used to be
`ModelExport.xml`, which said nothing about what it contained.

### Why the export is diff-friendly

Two properties, both of which the exporter now provides by default.

**Element order is a function of the model's names, not of Enterprise Architect's ids.**
Packages and classes are emitted in name order. This matters because EA's internal element ids
shift whenever the project is edited, and an id-ordered file would reshuffle for reasons that
have nothing to do with the model. Earlier exports were id-ordered — hence sequences like
`132, 133, 134, 135, 82, 83` — so a diff against an export made before ShapeChange `7a44ce20`
shows a wholesale reordering that carries no meaning.

The `sortedOutput` parameter is deliberately **not** set: it was verified byte-for-byte inert
against this model, because the order it requests is the order already produced.

**`ModelExport` is deterministic.** The committed `.scxml` is a fixed point of the exporter:
re-running `ModelExport` over it, using the committed `export-model-to-scxml.config.xml` with
only `inputModelType` switched from `EA7` to `SCXML`, reproduces the committed bytes. Any diff
here therefore reflects a real change in the Enterprise Architect project or in the exporter,
and the project itself is now committed under [`source/`](source/README.md) so the two can be
told apart.

## Using the model without EA (the normal case)

Point a ShapeChange OWL (or XSD) configuration's `inputFile` at `opendrive.scxml` (or
`opendrive.scxml.zip`) and set `inputModelType=SCXML`. No EA is required. See the
pipeline runbook ([`pipeline/README.md`](../../../pipeline/README.md)) for the OWL→SHACL steps.

## Reproducing the export (requires EA once)

Only this step needs EA. Everything downstream consumes the committed `*.scxml`.

`eaapi.jar` (the EA Java API) is not published to Maven Central — it ships with your EA
installation and must be installed into your local Maven repository once, using the exact
coordinates the ShapeChange `ea` module expects:

```bash
mvn install:install-file \
    -Dfile="C:/Program Files/Sparx Systems/EA/Java API/eaapi.jar" \
    -DgroupId=org.sparx -DartifactId=eaapi -Dversion=17.0.1704 -Dpackaging=jar
```

Build ShapeChange from source at the commit in the provenance table above (the `ea`
Maven profile is active by default and bundles the EA module using the `eaapi` installed
above):

```bash
git clone https://github.com/ASCS-eV/ShapeChange.git
cd ShapeChange
git checkout f4ee27b5dfac3f58d6534fb31b943cbef0269d34
mvn install
```

This produces `shapechange-app/target/ShapeChange-4.1.0-SNAPSHOT.zip`; unzip it, then run
the export. The native EA↔Java bridge DLL (`SSJavaCOM64.dll`) lives in the EA installation,
not in ShapeChange's own distribution, so `-Djava.library.path` must point there:

```bash
java -Djava.library.path="C:/Program Files/Sparx Systems/EA/Java API" \
     -jar ShapeChange-4.1.0-SNAPSHOT.jar -c export-model-to-scxml.config.xml \
     -x "$inputFile$" "C:/path/to/ASAM_OpenDRIVE.qeax"
```

This writes `scxml-out/INPUT/opendrive.zip`; unzip to obtain the SCXML. The exporter writes LF
on every platform, so no line-ending normalisation is needed before committing. The
configuration needs no editing: it runs as committed, and carries no absolute paths.

### What the export carries, and what it deliberately does not

The configuration sets `addStereotypes="*"` and a named `representTaggedValues` list. Both are
required: without them the export drops 691 of 775 stereotypes and every tagged value that is
not in ShapeChange's well-known set.

Carried because the model populates them:

| | Count with a value | What it is |
|---|---:|---|
| `XSDattribute` (stereotype) | 468 | which properties are XML attributes — matches the 468 `xs:attribute` declarations in the normative schema exactly |
| `use` | 365 | `required` / `optional` |
| `position` | 244 | element order within a content model |
| `introducedAtVersion` | 242 | per-element version provenance, `1.6.0`–`1.9.0` |
| `modelGroup` | 161 | XSD content-model kind: `sequence`, `group`, `choice` |
| `mixed` | 100 | mixed content |
| `deprecatedWithVersion` | 41 | when an element was deprecated |
| `unit` | 224 | physical units — well-known, carried without configuration |

Left out of `representTaggedValues` because the model declares them and never fills them in —
naming them would only add value-less elements. Note that `representTaggedValues` takes a list
of tag names and has **no wildcard form**; a named list is the only way to use it. The
comparison worth recording is against `addTaggedValues="*"`, which does carry everything:
measured, that produces an export 93,675 bytes larger than this list.

`memberNames` (98 occurrences, none with a value), `minOccurs` (56, none), and
`fractionDigits`, `totalDigits`, `whiteSpace` (15 each, none).

Some tags are in ShapeChange's well-known set and are exported whether or not the parameter
names them, so this configuration cannot suppress them. That is how `unit` and the populated
facets arrive — but it also means four empty facets (`length`, `minLength`, `maxLength`,
`maxExclusive`: 15 occurrences each, **none with a value**) and `maxOccurs` (56 occurrences,
one value) are in the committed model regardless. In total the model carries 1,711 tagged
values, 1,448 of which have a value; the 263 empty ones occupy 27,814 bytes.

Note there are only **six** populated facet values in the entire model — `minInclusive` ×2,
`pattern` ×2, `maxInclusive` ×1, `minExclusive` ×1 — matching the six restriction facets in
the normative schema exactly.
