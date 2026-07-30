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
| Exported by | ShapeChange 4.0.0, `ModelExport` target, `inputModelType=EA7`, `zipOutput=true`, `sortedSchemaOutput=true` |
| Producer header | `scxmlProducer="ShapeChange"`, `scxmlProducerVersion="4.0.0"` |
| Classes | 238 |

### How the version is established

The export carries no ASAM version stamp of its own — the producer version in the file
header identifies ShapeChange, not the standard. The revision is therefore determined
against the normative schema in `../schema/`, which is the version-pinned artifact:

- All **231** named types of the V1.9.0 XSD are present in the model; none is missing.
- That set includes all **10** types V1.9.0 added over V1.8.0 — `e_layerType`,
  `e_personCategory`, `e_vehicleCategory`, the `t_road_objects_object_outlines_outline_curveLocal*`
  family and the `t_signals_semantics_{animal,person,vehicle}` family — so the model is
  V1.9.0 and not the previous revision.
- `e_laneType` carries all 31 values of the V1.9.0 schema.

The model additionally declares 7 classes that have no named XSD counterpart. These are
UML-level constructs that XML Schema expresses differently, not model/schema drift:
`OpenDRIVE` is the root **element** (its type is anonymous in the XSD),
`g_additionalData` is an XSD **group**, and `LaneGeometry`, `t_outline_geometry`,
`t_physicalPosition` and `t_polyline_geometry` are abstractions the schema inlines.

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
| `opendrive.scxml` | 1,451,724 | 0 | `f67d96b93cd2e807…` |
| `ModelExport.xml` inside the zip | 1,481,256 | 29,532 | `8bf5554424621bc0…` |
| `opendrive.scxml.zip` | — | — | `ca2b9c33e245e8e7…` |

The 29,532-byte difference is exactly one `\r` per line. Use `opendrive.scxml` unless a
tool requires the zip.

## Using the model without EA (the normal case)

Point a ShapeChange OWL (or XSD) configuration's `inputFile` at `opendrive.scxml` (or
`opendrive.scxml.zip`) and set `inputModelType=SCXML`. No EA is required. See the
`ontology-management-base` pipeline documentation (`docs/future/asam-openx/`) for the
OWL→SHACL steps.

## Reproducing the export (requires EA once)

Only this step needs EA. Everything downstream consumes the committed `*.scxml`:

```bash
java -jar ShapeChange-4.0.0.jar -c export-model-to-scxml.config.xml \
     -x "$inputFile$" "C:/path/to/ASAM_OpenDRIVE.qeax"
```

This writes `scxml-out/model_export.zip`; unzip to obtain the SCXML, and normalise its
line endings to LF before committing. Adjust the `xi:include` path in the config to your
local ShapeChange installation.
