# ASAM OpenLABEL v1.0.0 — Normative Deliverables

Version: 1.0.0 | Date: November 9, 2021

## Tracked Normative Files

The following normative deliverables are included in this repository under the
ASAM Unrestricted Distribution Clause:

### Ontologies

- [`ontologies/openlabel_ontology_scenario_tags.ttl`](ontologies/openlabel_ontology_scenario_tags.ttl)
  — OWL ontology defining scenario tag vocabulary (151 classes)

### Schema

- [`schema/openlabel_json_schema.json`](schema/openlabel_json_schema.json)
  — JSON Schema for the complete OpenLABEL file format (46 definitions)
- [`schema/openlabel_json_schema-v1.0.0.json`](schema/openlabel_json_schema-v1.0.0.json)
  — Versioned copy of the JSON Schema

### Examples

10 example JSON files demonstrating labeling and annotation use cases:

- `examples/openlabel100_test_bbox_simple.json` — Simple bounding box
- `examples/openlabel100_test_bbox_simple_attributes.json` — Bounding box with attributes
- `examples/openlabel100_example_cuboids.json` — 3D cuboid annotations
- `examples/openlabel100_point_cloud_labels_rle.json` — Point cloud with RLE encoding
- `examples/openlabel-3-*` — Multi-sensor labeling examples (class/instance modes)

## Restricted Deliverables (not tracked)

The following are in `Source/` (gitignored) and require ASAM membership:

- `specification/ASAM_OpenLABEL_BS_V1-0-0.html` — Full HTML specification
- `release_presentation/Release_Presentation_ASAM_OpenLABEL_V1-0-0.pdf` — Release slides

The specification content has been extracted to markdown chapters (see [INDEX.md](INDEX.md)).
