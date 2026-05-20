# ASAM OSI (Open Simulation Interface) — Overview

> **Source**: https://github.com/OpenSimulationInterface/open-simulation-interface
> **Documentation**: https://opensimulationinterface.github.io/osi-antora-generator/asamosi/latest/specification/index.html
> **License**: MPL-2.0
> **Downloaded**: 2025-05-19

---

## Overview

The Open Simulation Interface (OSI) is a generic interface based on Google's protocol buffers for the environmental perception of automated driving functions in virtual scenarios.

As the complexity of automated driving functions rapidly increases, the requirements for test and development methods are growing. Testing in virtual environments offers the advantage of completely controlled and reproducible environment conditions.

## Key Characteristics

- **Format**: Protocol Buffers (`.proto` files defining message types)
- **Purpose**: Standardized interface between simulation environment and ADS functions
- **Layer**: Sits between the simulation environment (OpenDRIVE road, OpenSCENARIO scenarios) and the function under test
- **Main Messages**:
  - `SensorView` — Raw sensor data (lidar, camera, radar)
  - `SensorData` — Processed sensor outputs (object lists)
  - `GroundTruth` — Complete environment state (all objects, lanes, signals)
  - `TrafficCommand` — Traffic participant control
  - `TrafficUpdate` — Position updates for traffic participants
  - `HostVehicleData` — Ego vehicle state

## Relationship to ENVITED-X `ositrace` Domain

The ENVITED-X `ositrace` domain ontology describes **credentials** for OSI trace file data assets.

| OSI Concept | ositrace Ontology Mapping |
|-------------|--------------------------|
| OSI trace file (`.osi`) | The asset described by `OsiTraceCredential` |
| GroundTruth messages | `ositrace:containsGroundTruth` |
| SensorView messages | `ositrace:containsSensorView` |
| Protobuf version | `ositrace:osiVersion` |
| Sensor model type | `ositrace:sensorModelType` |
| Recording duration | `ositrace:duration` |

## Proto File Structure

```
osi3/
├── osi_common.proto           — Common types (Identifier, Timestamp, Vector3d, etc.)
├── osi_groundtruth.proto      — Complete environment state
├── osi_sensorview.proto       — Raw sensor data
├── osi_sensordata.proto       — Processed sensor data
├── osi_detectedobject.proto   — Detected moving objects
├── osi_lane.proto             — Lane boundaries and center lines
├── osi_object.proto           — Static and moving objects
├── osi_occupant.proto         — Vehicle occupants
├── osi_hostvehicledata.proto  — Ego vehicle state
├── osi_trafficcommand.proto   — Traffic participant commands
├── osi_trafficupdate.proto    — Traffic position updates
├── osi_trafficsign.proto      — Traffic signs
├── osi_trafficlight.proto     — Traffic lights
└── osi_environment.proto      — Environmental conditions (weather, lighting)
```

## Connection to Other ASAM Standards

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  OpenSCENARIO   │────▶│       OSI        │────▶│    ADS under    │
│  (Scenarios)    │     │  (Interface)     │     │    test         │
└─────────────────┘     └──────────────────┘     └─────────────────┘
         │                       ▲
         ▼                       │
┌─────────────────┐     ┌──────────────────┐
│   OpenDRIVE     │────▶│   Simulation     │
│ (Road Network)  │     │   Environment    │
└─────────────────┘     └──────────────────┘
```

## Citation

Hanke, T., Hirsenkorn, N., van-Driesten, C., Garcia-Ramos, P., Schiementz, M., Schneider, S. & Biebl, E. (2017). *A generic interface for the environment perception of automated driving functions in virtual scenarios.*
