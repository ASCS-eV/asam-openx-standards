# ASAM OpenSCENARIO® XML UML Model (SCXML) — V1.4.0

The **open, tool-neutral UML model** of ASAM OpenSCENARIO® XML V1.4.0 (the `.xosc`
format), exported once from Enterprise Architect and committed here so that every
downstream generation step — OWL, SHACL, XSD — runs **without an Enterprise Architect
licence**.

This is the **XML** standard, not OpenSCENARIO® **DSL** (see `../../asam-openscenario-dsl/`).

**These files are not original works of this project.** They are derived from ASAM's
`OpenSCENARIO.qeax` Enterprise Architect project. Copyright © ASAM e.V., 2026.
Redistributed under the ASAM Unrestricted Distribution Clause; see the repository
[LICENSE](../../../LICENSE).

## Provenance

| Field | Value |
|---|---|
| Standard | ASAM OpenSCENARIO® XML |
| Version | **V1.4.0** — matches the normative schema in [`../schema/`](../README.md) |
| Origin | `OpenSCENARIO.qeax` (Enterprise Architect project) |
| Exported by | ShapeChange 4.0.0, `ModelExport` target, `inputModelType=EA7`, `zipOutput=true`, `sortedSchemaOutput=true` |
| Producer header | `scxmlProducer="ShapeChange"`, `scxmlProducerVersion="4.0.0"` |
| Classes | 343 |

### How the version is established

The export carries no ASAM version stamp of its own — the producer version in the file
header identifies ShapeChange, not the standard. The revision is therefore determined
against the normative schema in `../schema/`, which is the version-pinned artifact:

- All **6** types V1.4.0 added over V1.3.1 are present in the model: `Interpolation`,
  `LaneLayerType`, `Motion`, `PreferredLaneLayerAction`,
  `TrafficDistributionEntryCatalogLocation` and `TrafficSignalSemantics`. The model is
  therefore V1.4.0 and not the previous revision.

Model and schema do not enumerate the same names, because UML and XML Schema encode the
same information differently. Neither direction indicates drift:

- **14 XSD types have no model class.** Nine are `xs:simpleType` primitives and
  parameterisable value types (`Boolean`, `Double`, `Int`, `String`, `UnsignedInt`,
  `UnsignedShort`, `DateTime`, `expression`, `parameter`), which map to UML primitives
  rather than classes. The other five — `MonitorDeclarations`, `ParameterDeclarations`,
  `VariableDeclarations`, `ParameterAssignments`, `TrafficSignals` — are XML list
  wrappers, each holding exactly one `maxOccurs="unbounded"` child; UML expresses that as
  a multiplicity on the owning class, so no wrapper class exists.
- **18 model classes have no named XSD type.** These are UML abstractions the schema
  flattens into choices and substitution groups — `Entity`, `EntityObject`,
  `StoryboardElement`, `ScenarioDefinition`, `CatalogElement`, `MotionControlAction`,
  the `*DistributionType` family, and similar.

## Files

| File | What it is |
|------|------------|
| `openscenario.scxml` | The model in ShapeChange SCXML (plain XML, diff-friendly). **Source of truth** for all downstream generation. |
| `openscenario.scxml.zip` | The `ModelExport` artifact exactly as ShapeChange wrote it (`zipOutput=true`), directly consumable as a ShapeChange `inputFile`. |
| `export-model-to-scxml.config.xml` | The ShapeChange `ModelExport` configuration that produced both files **from EA**. |

### `.scxml` and `.scxml.zip` are the same model, in different line endings

The zip's `ModelExport.xml` entry is byte-identical to `openscenario.scxml` **after
converting CRLF to LF** — the export ran on Windows, and the committed `.scxml` is
normalised to LF for the repository. The two therefore have different checksums by
design, and comparing them byte-for-byte will report a difference that is not one:

| Artifact | Bytes | CRLF line endings | SHA-256 (truncated) |
|---|---:|---:|---|
| `openscenario.scxml` | 1,925,499 | 0 | `fd1eeb32c8da4e3d…` |
| `ModelExport.xml` inside the zip | 1,962,824 | 37,325 | `4e928434a2806582…` |
| `openscenario.scxml.zip` | — | — | `b8f9c111345fe32b…` |

The 37,325-byte difference is exactly one `\r` per line. Use `openscenario.scxml` unless
a tool requires the zip.

## Using the model without EA (the normal case)

Point a ShapeChange OWL (or XSD) configuration's `inputFile` at `openscenario.scxml` (or
`openscenario.scxml.zip`) and set `inputModelType=SCXML`. No EA is required. See the
`ontology-management-base` pipeline documentation (`docs/future/asam-openx/`) for the
OWL→SHACL steps.

## Reproducing the export (requires EA once)

Only this step needs EA. Everything downstream consumes the committed `*.scxml`:

```bash
java -jar ShapeChange-4.0.0.jar -c export-model-to-scxml.config.xml \
     -x "$inputFile$" "C:/path/to/OpenSCENARIO.qeax"
```

This writes `scxml-out/model_export.zip`; unzip to obtain the SCXML, and normalise its
line endings to LF before committing. Adjust the `xi:include` path in the config to your
local ShapeChange installation.
