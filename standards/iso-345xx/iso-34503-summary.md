# ISO 34503:2023 — Road vehicles — Taxonomy for Operational Design Domain

> **Standard**: ISO 34503:2023 "Road vehicles — Test scenarios for automated driving systems — Taxonomy for operational design domain"
> **Organization**: ISO (International Organization for Standardization)
> **License**: Copyright ISO — ONLY paraphrased summaries permitted here
> **Note**: Full text requires purchase from ISO. This document summarizes the structure for cross-referencing purposes.

---

## Purpose

ISO 34503 provides a taxonomy (hierarchical classification) of attributes and concepts for describing an Operational Design Domain (ODD) for automated driving systems. It provides the vocabulary backbone used by both:
- **ASAM OpenODD®** (which formalizes it into a rule-based model)
- **ASAM OpenLABEL / openlabel-v2** (which uses it for scenario annotation)

## Relationship to ASAM OpenODD®

ASAM OpenODD® Annex B provides the complete ISO 34503 taxonomy in machine-readable CSV format. See: [`../asam-openodd/annex-b-iso34503-taxonomy.md`](../asam-openodd/annex-b-iso34503-taxonomy.md)

## Taxonomy Structure (Clauses 8–11)

### Clause 8: General Framework

Defines the overall ODD description framework. An ODD is described by specifying values/ranges for taxonomy attributes organized in a hierarchy.

### Clause 9: Scenery Elements

Static infrastructure and geographic features:

| Category | Sub-categories |
|----------|---------------|
| **Zone** | Fixed zones (school, environmental, industrial, parking), dynamic zones, interference zones, geofenced areas |
| **Region/States** | Geographic regions, countries |
| **Drivable Area** | Type (motorway, primary, radial, distributor, local, slip road, parking, shared), geometry (horizontal/transverse/longitudinal planes), lane spec (dimensions, marking, type, direction), speed limit, signs, edge, shoulder, surface (type, features, condition) |
| **Junctions** | Roundabouts (mini/compact/normal/large), intersections (T/Y/cross/staggered/grade-separated), classification (signalized/non-signalized) |
| **Road Furniture** | Barriers, guardrails, bollards, posts |
| **Structures** | Bridges, tunnels, overpasses |

### Clause 10: Environmental Conditions

Dynamic environmental factors:

| Category | Sub-categories |
|----------|---------------|
| **Weather** | Precipitation (rain, snow, hail — with intensity levels), wind (speed, direction), fog (visibility ranges), temperature |
| **Lighting** | Natural (sun position, time of day, cloud cover), artificial (street lighting intensity, type) |
| **Connectivity** | V2X availability, cellular coverage, GNSS quality |

### Clause 11: Dynamic Elements

Moving entities and traffic characteristics:

| Category | Sub-categories |
|----------|---------------|
| **Traffic Participants** | Vehicles (car, truck, bus, motorcycle), pedestrians, cyclists, animals, special vehicles (emergency, construction) |
| **Traffic Flow** | Density levels, speed characteristics, congestion states |
| **Temporary Road Structures** | Construction zones, detours, temporary signals |

## Mapping to openlabel-v2 Ontology

The `Odd` class in the openlabel-v2 LinkML schema maps directly to ISO 34503 clauses:

| ISO 34503 Clause | openlabel-v2 Slot Prefix | Example Slots |
|------------------|-------------------------|---------------|
| Clause 9 (Scenery) | `odd_scenery_*`, `odd_road_*` | `odd_road_type`, `odd_scenery_junction_type` |
| Clause 10 (Environment) | `odd_weather_*`, `odd_light_*` | `odd_weather_rain`, `odd_light_time_of_day` |
| Clause 11 (Dynamic) | `odd_dynamic_*` | `odd_dynamic_traffic_density` |

## Related ISO Standards

| Standard | Title | Relationship |
|----------|-------|-------------|
| ISO 34501:2022 | Vocabulary | Defines fundamental terms (ODD, COD, OD, etc.) |
| ISO 34503:2023 | Taxonomy for ODD | **This document** — the classification backbone |
| ISO 34504:2024 | Scenario categorization | How to organize and classify scenarios |
| ISO/PAS 21448 (SOTIF) | Safety of the Intended Functionality | Uses ODD concept for safety analysis |
| SAE J3016 | Levels of Driving Automation | Defines ODD as part of automation level definitions |

## Key Definitions (from ISO 34501:2022)

- **Operational Design Domain (ODD)**: Operating conditions under which a given driving automation system is specifically designed to function (Source: SAE J3016)
- **Current Operational Domain (COD)**: Set of operating conditions which exists presently in the immediate vicinity of an ADS
- **Operational Domain (OD)**: Set of operating conditions (aggregated view)
- **Target Operational Domain (TOD)**: Set of operating conditions in which an ADS is expected to operate

## Citation Format

When referencing ISO 34503 in LinkML schemas:

```yaml
comments:
  - "[ISO-34503] Clause 9.2 Drivable Area; [OpenODD] Annex B row 'drivable_area_type'"
```
