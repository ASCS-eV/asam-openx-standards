# Agent Instructions for ASAM OpenX Standards

This repository contains version-pinned markdown copies of ASAM OpenX simulation
standards. It serves as a reference library for AI agents working on the
[ontology-management-base](https://github.com/ASCS-eV/ontology-management-base)
ontologies.

## Purpose

The ENVITED-X ontologies describe **searchable metadata** for simulation assets.
They align with, summarize, and extend the ASAM standards documented here.
When adding or modifying ontology properties, agents should cite the normative
source from these references.

## Quick Reference: Concept → File → Section

### Enumerations (most commonly needed)

| Concept | File | Section |
|---------|------|---------|
| Road types | `asam-opendrive/map-uml-enumerations.md` | A.6.2 `e_roadType` |
| Lane types | `asam-opendrive/map-uml-enumerations.md` | A.3.7 `e_laneType` |
| Object types | `asam-opendrive/map-uml-enumerations.md` | A.4.5 `e_objectType` |
| Junction types | `asam-opendrive/map-uml-enumerations.md` | A.2.1 `e_junction_type` |
| Signal semantics | `asam-opendrive/map-uml-enumerations.md` | A.7.5 `e_signals_semantics_lane` |
| Road mark types | `asam-opendrive/map-uml-enumerations.md` | A.3.4 `e_roadMarkType` |
| Road mark colors | `asam-opendrive/map-uml-enumerations.md` | A.3.10 `e_roadMarkColor` |
| CRG mode/purpose | `asam-opendrive/map-uml-enumerations.md` | A.2.2–A.2.3 |
| Junction group types | `asam-opendrive/map-uml-enumerations.md` | A.2.5 `e_junctionGroup_type` |

### Definitions & Core Concepts

| Concept | File | What You'll Find |
|---------|------|-----------------|
| Road network terms | `asam-opendrive/03-terms-and-definitions.md` | Normative definitions (road, lane, junction, signal, etc.) |
| OpenDRIVE scope | `asam-opendrive/01-scope.md` | What the standard covers |
| Header/metadata | `asam-opendrive/06-04-header.md` | File metadata structure |
| Georeferencing | `asam-opendrive/08-*` chapters | Coordinate systems |
| Lane model | `asam-opendrive/11-*` chapters | Lane structure, widths, sections |
| Junctions | `asam-opendrive/12-*` chapters | Junction connections, types |
| Signals | `asam-opendrive/14-*` chapters | Traffic signs, signals, markings |
| Objects | `asam-opendrive/13-*` chapters | Roadside objects, tunnels, bridges |

### ODD / Scenario Concepts

| Concept | File | What You'll Find |
|---------|------|-----------------|
| ODD taxonomy | `asam-openodd/06-02-*` through `06-08-*` | Full ODD module breakdown |
| ODD scenery | `asam-openodd/06-*` chapters | Road, environment, weather |
| Scenario structure | `asam-openscenario-dsl/02-*` through `05-*` | Domain model, actions, triggers |
| Label taxonomy | `asam-openlabel/INDEX.md` | JSON schema reference for labels |

### Material / Environment

| Concept | File | What You'll Find |
|---------|------|-----------------|
| Material properties | `asam-openmaterial-3d/` chapters | 3D material/geometry schemas |
| Sensor simulation | `asam-osi/INDEX.md` | Overview of OSI interface |
| Road surfaces | `asam-opencrg/INDEX.md` | OpenCRG road profile format |

## Search Strategies

### Find an enumeration's valid values
```bash
grep -A 50 "e_laneType" standards/asam-opendrive/map-uml-enumerations.md
```

### Find a concept definition
```bash
grep -i "junction" standards/asam-opendrive/03-terms-and-definitions.md
```

### Check version history (introduced/deprecated)
Look for "Introduced" and "Deprecated" columns in enumeration tables in
`map-uml-enumerations.md`. Values show the version where they were added/removed.

### Find cross-standard relationships
See `CROSS_REFERENCES.md` for concept equivalences across standards.

### Find machine-readable enum data
See `ENUMERATIONS.yaml` for structured enum definitions with deprecation metadata.

## Citation Pattern

When modifying ontologies in ontology-management-base, cite sources as:

**In SHACL comments:**
```turtle
sh:description "Road types per OpenDRIVE v1.9.0, Annex A.6.2 (e_roadType)"@en ;
```

**In OWL annotations:**
```turtle
dcterms:source "ASAM OpenDRIVE v1.9.0, Annex A.6.2, Table 194" ;
```

**In LinkML slots:**
```yaml
comments:
  - "[OpenDRIVE] Annex A.3.7, Table 176 (e_laneType)"
see_also:
  - https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/...
```

## Directory Layout

```
standards/
├── asam-opendrive/          # 95 chapters — road network format (v1.9.0)
├── asam-openscenario-dsl/   # 59 chapters — scenario language (v2.2.0)
├── asam-openodd/            # 62 chapters — operational design domain (v1.0.0)
├── asam-openmaterial-3d/    # 27 chapters — material/geometry (BS 1.0.0)
├── asam-openlabel/          # 2 files — labeling standard (v1.0.0)
├── asam-osi/                # 1 file — open simulation interface
├── asam-opencrg/            # 1 file — road surface profiles
├── asam-traffic-participants/ # 1 file — road user types
└── iso-345xx/               # 1 file — ISO 34503 (paraphrased summary)
submodules/
├── open-simulation-interface/ # Full OSI source (MPL-2.0)
└── OpenCRG/                  # Full OpenCRG source (Apache-2.0)
```

## Ontology ↔ Standard Mapping

| ENVITED-X Domain | Primary Standard | Key Reference Files |
|-----------------|-----------------|-------------------|
| `hdmap` | OpenDRIVE | `map-uml-enumerations.md`, `03-terms-and-definitions.md` |
| `scenario` | OpenSCENARIO DSL | `02-*` through `05-*` (domain model) |
| `openlabel-v2` | OpenLABEL + OpenODD + ISO 34503 | `asam-openodd/06-*`, `iso-345xx/` |
| `ositrace` | OSI | `asam-osi/INDEX.md`, submodule source |
| `surface-model` | OpenCRG + OpenDRIVE | `asam-opencrg/`, CRG sections in OpenDRIVE |
| `environment-model` | OpenMATERIAL 3D | `asam-openmaterial-3d/` chapters |
