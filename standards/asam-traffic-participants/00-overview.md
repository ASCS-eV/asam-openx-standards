# ASAM Traffic Participants — Overview

- **Source**: https://www.asam.net/standards/detail/traffic-participants/
- **Version**: v1.0.2
- **License**: Unrestricted distribution (ASAM e.V.)
- **Date retrieved**: 2025-05-19
- **Access**: Requires ASAM account (not publicly accessible via web)

## Summary

ASAM Traffic Participants defines a standardized classification and description
system for all types of road users and traffic participants in simulation
environments. It provides a common taxonomy for vehicles, pedestrians, cyclists,
and other entities that interact in traffic scenarios.

## Key Concepts (from public documentation)

### Traffic Participant Categories

Based on publicly available ASAM documentation, the standard covers:

- **Vehicles**: Cars, trucks, buses, motorcycles, with detailed sub-classifications
- **Vulnerable Road Users (VRU)**: Pedestrians, cyclists, e-scooter riders
- **Other participants**: Animals, debris, unknown objects
- **Special vehicles**: Emergency vehicles, construction vehicles, agricultural vehicles

### Properties

Each traffic participant type is characterized by:

- Physical dimensions (length, width, height)
- Dynamic capabilities (max speed, acceleration)
- Visual appearance classification
- Behavioral models references

### Relationship to Other Standards

- **OpenSCENARIO**: Uses traffic participant definitions for entity declarations
- **OpenLABEL**: References traffic participant types for annotation
- **OSI**: Ground truth objects reference traffic participant classifications

## Access Note

The full specification text is available only through the ASAM member portal or
direct download after registration. The JSON schema and detailed classification
tables are not publicly hosted.

For ontology development, the relevant type hierarchies can be reconstructed from:
1. OpenSCENARIO DSL entity type definitions (see `asam-openscenario-dsl/`)
2. OpenLABEL object type taxonomy
3. ASAM OSI `MovingObject` classification enums

## Relevance to ENVITED-X

| ENVITED-X Domain | Relationship |
|-----------------|--------------|
| `openlabel-v2` | Direct — object type classifications |
| `scenario` | Direct — entity definitions in scenarios |
| `ositrace` | Direct — moving object types in ground truth |
