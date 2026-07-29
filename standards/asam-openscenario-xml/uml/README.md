# OpenSCENARIO (XML) — open UML model (SCXML)

This directory holds the **open, tool-neutral UML model** for ASAM OpenSCENARIO
(the XML / `.xosc` format), so the ontology/SHACL/XSD pipeline can run **without
Enterprise Architect (EA)**.

## Files

| File | What it is |
|------|------------|
| `openscenario.scxml` | The model in ShapeChange SCXML (plain XML, diff-friendly). **Source of truth** for all downstream generation. |
| `openscenario.scxml.zip` | The exact `ModelExport` artifact (`zipOutput=true`); same content as `openscenario.scxml`, directly consumable as a ShapeChange `inputFile`. |
| `export-model-to-scxml.config.xml` | The ShapeChange `ModelExport` configuration that produced the two files above **from EA**. |

## Provenance

- **Origin:** `OpenSCENARIO.qeax` (Enterprise Architect project).
- **Exported by:** ShapeChange 4.0.0, `ModelExport` target, `inputModelType=EA7`,
  `zipOutput=true`, `sortedSchemaOutput=true`.
- `scxmlProducer="ShapeChange"`, `scxmlProducerVersion="4.0.0"` (see the file header).

## Reproducing the export (requires EA once)

Only this export step needs EA. Everything downstream consumes the committed
`*.scxml`:

```bash
java -jar ShapeChange-4.0.0.jar -c export-model-to-scxml.config.xml \
     -x "$inputFile$" "C:/path/to/OpenSCENARIO.qeax"
```

This writes `scxml-out/model_export.zip`; unzip to obtain the SCXML. Adjust the
`xi:include` path in the config to your local ShapeChange installation.

## Using the model without EA (the normal case)

Point a ShapeChange OWL (or XSD) configuration's `inputFile` at
`openscenario.scxml` (or `openscenario.scxml.zip`) and set `inputModelType=SCXML`.
No EA is required. See the OMB pipeline docs (`docs/future/asam-openx/`) for the
OWL→SHACL steps.
