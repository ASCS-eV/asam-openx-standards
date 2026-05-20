# ASAM OpenLABEL v1.0.0 — JSON Schema Reference

- **Source**: https://openlabel.asam.net/V1-0-0/schema/openlabel_json_schema.json
- **Schema ID**: `https://openlabel.asam.net/V1-0-0/schema#`
- **JSON Schema Draft**: draft-07
- **Date retrieved**: 2025-05-19

## Top-Level Structure

The root object has a single property `openlabel` which contains:

| Property | Type | Description |
|----------|------|-------------|
| `metadata` | object | Version, schema version, name, comment, tagged file |
| `coordinate_systems` | map<string, coordinate_system> | 3D reference frames |
| `streams` | map<string, stream> | Data streams (cameras, lidars, etc.) |
| `objects` | map<uid, object> | Physical entities with spatial data |
| `actions` | map<uid, action> | Temporal activities |
| `events` | map<uid, event> | Instantaneous occurrences |
| `contexts` | map<uid, context> | Non-spatial/temporal annotations (weather, ODD) |
| `relations` | map<uid, relation> | Semantic relationships |
| `frames` | map<frame_num, frame> | Per-frame dynamic data |
| `frame_intervals` | array<frame_interval> | Frame ranges |
| `ontologies` | map<uid, ontology> | External ontology references |
| `resources` | map<uid, resource> | External resource references |
| `tags` | map<uid, tag> | Classification tags |

## Core Element Definitions

### action

```json
{
  "name": "string (friendly name)",
  "type": "string (class from ontology)",
  "ontology_uid": "string (reference to ontologies section)",
  "resource_uid": "string",
  "frame_intervals": [{"frame_start": int, "frame_end": int}],
  "action_data": { "boolean": [], "num": [], "text": [], "vec": [] },
  "action_data_pointers": {}
}
```

### object

```json
{
  "name": "string",
  "type": "string (class from ontology)",
  "ontology_uid": "string",
  "resource_uid": "string",
  "frame_intervals": [{"frame_start": int, "frame_end": int}],
  "object_data": {
    "bbox": [], "cuboid": [], "poly2d": [], "poly3d": [],
    "point2d": [], "point3d": [], "num": [], "text": [],
    "boolean": [], "vec": [], "binary": [],
    "line_reference": [], "area_reference": [], "mesh": [],
    "image": [], "mat": [], "rbbox": []
  },
  "object_data_pointers": {}
}
```

### context

```json
{
  "name": "string",
  "type": "string (class from ontology)",
  "ontology_uid": "string",
  "resource_uid": "string",
  "frame_intervals": [{"frame_start": int, "frame_end": int}],
  "context_data": { "boolean": [], "num": [], "text": [], "vec": [] },
  "context_data_pointers": {}
}
```

### event

```json
{
  "name": "string",
  "type": "string (class from ontology)",
  "ontology_uid": "string",
  "resource_uid": "string",
  "frame_intervals": [{"frame_start": int, "frame_end": int}],
  "event_data": { "boolean": [], "num": [], "text": [], "vec": [] },
  "event_data_pointers": {}
}
```

### relation

```json
{
  "name": "string",
  "type": "string",
  "ontology_uid": "string",
  "rdf_objects": [{"uid": "string", "type": "object|action|event|context"}],
  "rdf_subjects": [{"uid": "string", "type": "object|action|event|context"}],
  "frame_intervals": [{"frame_start": int, "frame_end": int}]
}
```

### tag

```json
{
  "name": "string",
  "type": "string",
  "ontology_uid": "string",
  "tag_data": { "boolean": [], "num": [], "text": [], "vec": [] },
  "tag_data_pointers": {}
}
```

## Geometric Data Types

### bbox (2D bounding box)
- Format: `[x, y, w, h]` — center + width/height
- Required: `name`, `val`

### cuboid (3D bounding box)
- Format (9 values): `[x, y, z, rx, ry, rz, sx, sy, sz]` — position, Euler rotation, dimensions
- Format (10 values): `[x, y, z, qx, qy, qz, qw, sx, sy, sz]` — position, quaternion, dimensions
- Required: `name`, `val`

### poly2d (2D polygon)
- `val`: flat array of 2D points `[x1, y1, x2, y2, ...]`
- `mode`: `MODE_POLY2D_ABSOLUTE` | `MODE_POLY2D_SRF6DCC` | `MODE_POLY2D_RS6FCC`
- `closed`: boolean

### poly3d (3D polygon)
- `val`: flat array of 3D points `[x1, y1, z1, x2, y2, z2, ...]`
- `closed`: boolean

### mesh (3D mesh)
- `point3d`: array of 3D vertices
- `area_reference`: array of face definitions (referencing point indices)
- `line_reference`: array of edge definitions

## Coordinate Systems

```json
{
  "type": "string (e.g., 'local', 'geo')",
  "parent": "string (UID of parent coordinate system)",
  "children": ["string"],
  "pose_wrt_parent": { "translation": [x,y,z], "quaternion": [qx,qy,qz,qw] }
}
```

## Frame Structure

Each frame can contain per-frame updates for:
- `objects` → per-object `object_data`
- `actions` → per-action `action_data`
- `events` → per-event `event_data`
- `contexts` → per-context `context_data`
- `relations` → presence indicates relation exists in frame
- `frame_properties` → timestamp, per-frame transforms, streams

## Ontology References

```json
{
  "ontologies": {
    "uid-1": { "uri": "https://example.org/ontology/v1" }
  }
}
```

Elements reference ontologies via `ontology_uid` field, and their `type` field
maps to a class in the referenced ontology.

## Key Design Patterns

1. **Static vs Dynamic**: Top-level elements define static properties; `frames`
   section overrides/extends with per-frame dynamic data.

2. **Ontology-agnostic**: The format itself is generic; semantics come from
   external ontologies referenced in the `ontologies` section.

3. **Frame intervals**: Elements exist only within their declared frame intervals.
   This enables sparse annotation.

4. **Nested attributes**: Geometric data (bbox, cuboid, etc.) can contain nested
   `attributes` for per-geometry metadata (e.g., visibility score, occlusion level).

5. **UID patterns**: Element UIDs can be numeric strings or UUIDs
   (`^(-?[0-9]+|[0-9a-fA-F]{8}-...-[0-9a-fA-F]{12})$`).
