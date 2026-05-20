# ASAM OpenLABEL® v1.0.0 — Overview

- **Source**: https://www.asam.net/standards/detail/openlabel/
- **Schema**: https://openlabel.asam.net/V1-0-0/schema/openlabel_json_schema.json
- **Version**: v1.0.0
- **License**: Unrestricted distribution (ASAM e.V.)
- **Date retrieved**: 2025-05-19
- **Access**: Full spec requires ASAM account; JSON schema is public

## Summary

ASAM OpenLABEL is a standard for the annotation and labeling of objects,
actions, events, contexts, and relations in sensor data recordings used in
automotive applications. It defines a JSON-based format for storing labels
applied to images, point clouds, and other sensor modalities.

## Key Concepts (from JSON Schema)

### Core Elements

| Element | Description |
|---------|-------------|
| **Objects** | Physical entities (vehicles, pedestrians, signs) with spatial data |
| **Actions** | Temporal activities (crossing, turning, braking) with frame intervals |
| **Events** | Instantaneous occurrences at specific frames |
| **Contexts** | Environmental/situational descriptors (weather, road type, time of day) |
| **Relations** | Semantic relationships between elements |

### Data Types

OpenLABEL supports these geometric/attribute data types:

- `bbox` — 2D bounding box [x, y, w, h]
- `cuboid` — 3D cuboid with position and rotation
- `poly2d` / `poly3d` — 2D/3D polygons
- `point2d` / `point3d` — Point annotations
- `num` — Numeric values
- `text` — String values
- `boolean` — Boolean values
- `vec` — Vector values (arrays of numbers)
- `binary` — Binary payload (e.g., segmentation masks)
- `line_reference` / `area_reference` — References to other geometric data
- `mesh` — 3D mesh data

### Structure

```json
{
  "openlabel": {
    "metadata": { ... },
    "coordinate_systems": { ... },
    "streams": { ... },
    "objects": { ... },
    "actions": { ... },
    "events": { ... },
    "contexts": { ... },
    "relations": { ... },
    "frames": { ... },
    "frame_intervals": [ ... ],
    "ontologies": { ... },
    "resources": { ... },
    "tags": { ... }
  }
}
```

### Ontology Support

OpenLABEL has built-in ontology referencing:
- `ontologies` section maps UIDs to external ontology definitions
- Each element (object, action, context) can reference an `ontology_uid`
- The `type` field of each element corresponds to a class in the referenced ontology

### Frame-based Annotation

- `frames` contains per-frame data (time-series annotations)
- `frame_intervals` defines ranges where elements exist
- Supports both sparse and dense annotation patterns

## Relationship to ENVITED-X openlabel-v2

The ENVITED-X `openlabel-v2` ontology domain directly models the OpenLABEL
standard's data structures, particularly:

| OpenLABEL Concept | openlabel-v2 Class/Slot |
|-------------------|------------------------|
| `contexts` → weather | `Odd.weather_*` slots |
| `contexts` → road | `Odd.drivable_area_type` |
| `contexts` → time_of_day | `Odd.time_of_day` |
| `objects` → vehicle | Object type taxonomy |
| `tags` | Classification metadata |

### ODD (Operational Design Domain) in OpenLABEL

The `contexts` section of OpenLABEL is specifically designed to capture ODD
information as defined by ISO 34503. The openlabel-v2 `Odd` class maps these
context fields to a credential-based representation.

## JSON Schema Location

The complete JSON schema is saved separately:
- `01-json-schema-core.md` — Core definitions (actions, objects, frames)
- `02-json-schema-geometry.md` — Geometric data types
- `03-json-schema-metadata.md` — Metadata and ontology references

## Relevance to ENVITED-X

| ENVITED-X Domain | Relationship |
|-----------------|--------------|
| `openlabel` | Direct — v1 ontology based on this standard |
| `openlabel-v2` | Direct — v2 ontology, especially ODD/contexts |
| `scenario` | Complementary — labels on scenario recordings |
| `ositrace` | Complementary — labels on OSI trace data |
