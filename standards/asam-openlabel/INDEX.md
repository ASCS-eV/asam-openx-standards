# ASAM OpenLABEL® v1.0.0 — Chapter Index

> **Version**: v1.0.0 (November 9, 2021)
> **License**: Restricted distribution (ASAM e.V.)
> **Files**: 13 chapters (extracted from HTML specification)

## Chapters

| # | File | Title |
|---|------|-------|
| 1 | [00-preamble.md](00-preamble.md) | Preamble (0.6 KB) |
| 2 | [01-foreword.md](01-foreword.md) | 1. Foreword (1.1 KB) |
| 3 | [02-introduction.md](02-introduction.md) | 2. Introduction (11.9 KB) |
| 4 | [03-scope.md](03-scope.md) | 3. Scope (2.6 KB) |
| 5 | [04-normative-references.md](04-normative-references.md) | 4. Normative references (0.7 KB) |
| 6 | [05-terms-and-definitions.md](05-terms-and-definitions.md) | 5. Terms and definitions (4.2 KB) |
| 7 | [06-conceptual-overview.md](06-conceptual-overview.md) | 6. Conceptual overview (27.9 KB) |
| 8 | [07-multi-sensor-data-labeling.md](07-multi-sensor-data-labeling.md) | 7. Multi-sensor data labeling (124.7 KB) |
| 9 | [08-scenario-tagging.md](08-scenario-tagging.md) | 8. Scenario tagging (57.1 KB) |
| 10 | [09-references.md](09-references.md) | 9. References (46.8 KB) |
| 11 | [10-list-of-figures.md](10-list-of-figures.md) | 10. List of figures (6.3 KB) |
| 12 | [11-list-of-tables.md](11-list-of-tables.md) | 11. List of tables (3.4 KB) |
| 13 | [12-bibliography.md](12-bibliography.md) | Bibliography (1.9 KB) |

## Source Material

### Tracked Normative Deliverables

Machine-readable normative deliverables are tracked in this repository:

| Path | Description |
|------|-------------|
| [`ontologies/openlabel_ontology_scenario_tags.ttl`](ontologies/openlabel_ontology_scenario_tags.ttl) | Scenario tagging ontology (1357 lines, RDF Turtle) |
| [`schema/openlabel_json_schema.json`](schema/openlabel_json_schema.json) | Complete JSON Schema (draft-07, 88 KB) |
| [`schema/openlabel_json_schema-v1.0.0.json`](schema/openlabel_json_schema-v1.0.0.json) | Versioned JSON Schema copy |
| [`examples/`](examples/) | 10 annotation examples (bbox, cuboid, poly2d, point cloud) |
| [`DELIVERABLES.md`](DELIVERABLES.md) | Deliverables manifest |

### Restricted Source Material (gitignored)

The `Source/` directory contains the original ASAM deliverables (not tracked):

| Path | Description |
|------|-------------|
| `Source/specification/ASAM_OpenLABEL_BS_V1-0-0.html` | Full HTML specification (12.6 MB, self-contained) |
| `Source/release_presentation/` | Release presentation (PDF) |

## Key Sections for ENVITED-X Ontology Work

| Task | Chapter | What You'll Find |
|------|---------|------------------|
| Understand tagging model | `08-scenario-tagging.md` | Tagging semantics, ontology structure, use cases |
| Tag value rules | `08-scenario-tagging.md` §8.2 | Subsets, extensions, multiple values, inference |
| JSON schema structure | `07-multi-sensor-data-labeling.md` | Full annotation schema details |
| Ontology format | `08-scenario-tagging.md` §8.6 | How ontologies are referenced |
| Terms/definitions | `05-terms-and-definitions.md` | Normative definitions |
| Class reference | `09-references.md` | Complete ontology class listing |
