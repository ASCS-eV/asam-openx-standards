# ASAM OpenDRIVE v1.9.0 — §1 Scope & §6 General Architecture

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/
> **Standard**: ASAM OpenDRIVE BS 1.9.0 Specification, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2025-05-19

---

## §1 Scope

ASAM OpenDRIVE specifies the modeling approach of how to describe static road networks for driving simulation applications using the Extensible Markup Language (XML).

The ASAM OpenDRIVE standard has the following scope:

- Specify the schema for ASAM OpenDRIVE in a UML model and XSD schemas. The UML model and the XSD schemas define the structure, sequence, elements, and values of ASAM OpenDRIVE. The XSD schemas are derived from the UML model.
- Provide the XSD schemas to which valid ASAM OpenDRIVE files shall conform.
- Explain how the ASAM OpenDRIVE elements are used and relationships between elements in the ASAM OpenDRIVE UML model and XSD schemas, for example, roads, lanes, junctions, objects, signals, and railroads.
- Give additional guidelines and rules, that cannot be represented in the UML model and XSD schemas for using ASAM OpenDRIVE.

## §6 General Architecture

### 6.1 Introduction

ASAM OpenDRIVE data is stored in XML files with the extension `.xodr`. Compressed files have the extension `.xodrz` (compression format: `gzip`).

Elements are organized into levels. Elements with a level greater than zero (0) are children of the preceding level. Elements with a level of one (1) are called primary elements.

All floating-point numbers are IEEE 754 double precision.

### 6.5 Overview of Elements

The ASAM OpenDRIVE element hierarchy (primary elements under `<OpenDRIVE>` root):

```
<OpenDRIVE>
  ├── <header>          — File metadata, geo-reference, offset
  ├── <road>            — Road definition (the core element)
  │   ├── <planView>    — Road reference line geometry
  │   ├── <elevationProfile>  — Height profile along road
  │   ├── <lateralProfile>    — Superelevation and shape
  │   ├── <lanes>       — Lane definitions and properties
  │   ├── <objects>     — Road-side objects (barriers, signs, etc.)
  │   ├── <signals>     — Traffic signals and controllers
  │   ├── <surface>     — CRG surface data reference
  │   └── <railroad>    — Railroad track overlays
  ├── <junction>        — Junction connectivity
  ├── <junctionGroup>   — Junction groupings
  ├── <controller>      — Signal controller definitions
  └── <station>         — Railroad station definitions
```

## Table of Contents (Full Spec)

| Chapter | Title | Domain Relevance |
|---------|-------|-----------------|
| 6 | General Architecture | File structure, root element, header |
| 7 | Additional Data | User data extensions |
| 8 | Coordinate Systems | Inertial, reference line, local, georeferencing |
| 9 | Geometries | Reference line types: line, spiral, arc, poly3 |
| 10 | Roads | Road properties, linkage, type, elevation, surface |
| 11 | Lanes | Layers, groups, sections, offset, link, geometry, markings |
| 12 | Junctions | Common, direct, virtual junctions; connections |
| 13 | Objects | Outline, skeleton, repeating, material, tunnels, bridges |
| 14 | Signals | Types, dependency, reference, controllers, boards |
| 15 | Railroads | Tracks, switches, stations |
| Annex A | Enumerations | All enumeration values (normative) |
| Annex B | Data Types | UML data type definitions (normative) |
| Annex C | Dynamic Signal Terms | Signal state terminology (normative) |
| Annex F | Checker Rules | Validation rules (normative) |

## Deliverables

- Enterprise Architect UML model (`.zip`)
- XSD schema files (`.zip`)
- Examples and use cases (`.zip`)
- Implementation examples (`.zip`)

## Relationship to ENVITED-X `hdmap` Domain

The ENVITED-X `hdmap` domain ontology describes **credentials** for HD map data assets. ASAM OpenDRIVE defines the **data format** those assets contain. Key alignment:

| OpenDRIVE Concept | hdmap Ontology Mapping |
|-------------------|-----------------------|
| Road network file (`.xodr`) | The asset described by `HdMapCredential` |
| Coordinate system / geo-reference | `hdmap:coordinateSystem`, `hdmap:georeference` |
| Road types (motorway, rural, etc.) | `hdmap:roadTypes` (aligns with ISO 34503 drivable_area_type) |
| Lane configuration | `hdmap:laneCount`, `hdmap:laneTypes` |
| Junction complexity | `hdmap:junctionTypes` |
| Signal catalog | `hdmap:signalTypes` |
| XSD version | `hdmap:formatVersion` |
