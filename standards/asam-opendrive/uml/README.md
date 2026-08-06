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
| Origin | `ASAM_OpenDRIVE.qeax` (Enterprise Architect project) |
| Exported by | ShapeChange built from source at commit [`1a16d4af3336`](https://github.com/ShapeChange/ShapeChange/commit/1a16d4af333627059d12d271f588e903e6ecb172) (`next` branch, 2026-07-30), `ModelExport` target, `inputModelType=EA7`, `zipOutput=true` |
| Producer header | `scxmlProducer="ShapeChange"`, `scxmlProducerVersion="4.1.0-SNAPSHOT"` |
| Classes | 238 |

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

Two things the XSD expresses and this UML model does not. Both originate in the Enterprise
Architect model, so the export reproduces them faithfully; neither can be repaired by
configuring ShapeChange differently, and neither is repaired downstream. They are recorded
here so a consumer is not surprised by them.

**XSD union types carry no union semantics.** The schema declares four unions. In the model
they are plain classes, and the member types — where they appear at all — appear as
*supertypes*, which is the inverse of a union:

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

## Files

| File | What it is |
|------|------------|
| `opendrive.scxml` | The model in ShapeChange SCXML (plain XML, diff-friendly). **Source of truth** for all downstream generation. |
| `opendrive.scxml.zip` | The `ModelExport` artifact exactly as ShapeChange wrote it (`zipOutput=true`), directly consumable as a ShapeChange `inputFile`. |
| `export-model-to-scxml.config.xml` | The ShapeChange `ModelExport` configuration that produced both files **from EA**. |

### `.scxml` and `.scxml.zip` are the same model, in different line endings

The zip's `ModelExport.xml` entry is byte-identical to `opendrive.scxml` **after
converting CRLF to LF** — the export ran on Windows, and the committed `.scxml` is
normalised to LF for the repository. The two therefore have different checksums by
design, and comparing them byte-for-byte will report a difference that is not one:

| Artifact | Bytes | CRLF line endings | SHA-256 (truncated) |
|---|---:|---:|---|
| `opendrive.scxml` | 1,451,750 | 0 | `02648f53ab50e34a…` |
| `ModelExport.xml` inside the zip | 1,481,282 | 29,532 | `3c377b7b20346703…` |
| `opendrive.scxml.zip` | 77,472 | — | `bb2f8d6769dd4843…` |

The 29,532-byte difference is exactly one `\r` per line. Use `opendrive.scxml` unless a
tool requires the zip.

### Why the export is diff-friendly

Not because of a sort parameter. ShapeChange's `sortedSchemaOutput` orders the *schemas* it
processes, not the classes within one; class order is `sortedOutput`, and `ModelExport` ignores
that parameter — verified against this model, as both an input and a target parameter, with the
output unchanged either way. Element order therefore follows the source model, and no package
in this export is alphabetical.

What makes the file reviewable is that `ModelExport` is **deterministic**: the committed
`.scxml` is a fixed point of the exporter. Re-running `ModelExport` over it, using the
committed `export-model-to-scxml.config.xml` with only `inputModelType` switched from `EA7` to
`SCXML`, reproduces the committed bytes exactly. Element order is a function of the model, not
of the run, so re-exporting an unchanged model yields an unchanged file and any diff here
reflects a real change in the Enterprise Architect project.

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
git clone https://github.com/ShapeChange/ShapeChange.git
cd ShapeChange
git checkout 1a16d4af333627059d12d271f588e903e6ecb172
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

This writes `scxml-out/INPUT/ModelExport.zip`; unzip to obtain the SCXML, and normalise its
line endings to LF before committing. The configuration needs no editing: it runs as
committed, and carries no absolute paths.

Two things to settle at the next re-export, deliberately left alone here because changing
them would mean the committed artifacts were no longer what this configuration produces:

- **`outputFilename`.** Unset, so `ModelExport` uses its default and the zip entry is called
  `ModelExport.xml` rather than something that identifies the standard. Setting it changes
  the zip's contents, so it belongs with a real re-export.
- **`representTaggedValues`.** Unset, so only tagged values ShapeChange already knows are
  carried; this export contains just `targetNamespace` and `xmlns`. Whether ASAM annotates
  the Enterprise Architect model further — deprecation, version-added — cannot be
  determined from the export itself. Run the export once with and once without the
  parameter and diff, then either set it or record that there was nothing to carry.
