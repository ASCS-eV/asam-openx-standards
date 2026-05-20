# ASAM OpenSCENARIO DSL v2.2.0 — §1 Scope & Structure

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/
> **Standard**: ASAM OpenSCENARIO DSL BS 2.2.0 Specification, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2025-05-19

---

## §1 Scope

ASAM OpenSCENARIO comprises the specification of a _domain-specific language_ and a _domain model_. The standard is intended for the description of dynamic behaviors and environments for driving simulation applications or any application that utilizes scenario descriptions.

The primary use of ASAM OpenSCENARIO is the description and construction of complex scenarios.

These scenarios include maneuvers that involve:

- Multiple vehicles
- Other participants
- Complex environmental interactions
- Complex variations of testing parameters
- Evaluation and analysis of complex or compound measurement criteria

### Applications

ASAM OpenSCENARIO is used in:

- Virtual development
- Testing
- Validation of functions for:
  - Driver assistance
  - Automated driving
  - Autonomous driving

Also suitable for:
- Testing on test tracks or proving grounds
- Testing in a mixed environment (HiL)
- Decoding real-world driving data

ASAM OpenSCENARIO may be used in conjunction with **ASAM OpenDRIVE** and **ASAM OpenCRG**. These standards describe detailed information of the road network and surface in driving simulations.

ASAM OpenSCENARIO introduces the concept of a _domain-specific language_ into scenario description. The language has the properties of a software language.

## Table of Contents (Full Spec)

| Chapter | Title | Key Content |
|---------|-------|-------------|
| 6 | Conceptual Overview | Scenario writing, key terminology, abstraction |
| 7 | Language Reference Manual | Syntax, types, expressions, coverage, semantics, libraries |
| 8 | Domain Model Reference | Core layout, coordinate systems, actions, road network, actors, environment |
| 9 | User Guide | Reusable scenarios, style guide, extending domain model |
| Annex A | Scenario Examples | Reference implementations |
| Annex B | Use Cases & Workflows | Auditor, AV/ADAS developer, scenario author workflows |

## Domain Model Structure (Chapter 8)

The domain model defines the semantic building blocks:

| Section | Topic | Description |
|---------|-------|-------------|
| 8.1 | Introduction | Overall domain model architecture |
| 8.2 | Core Layout | Base structure of scenario descriptions |
| 8.3 | Coordinate Systems | Spatial reference frames |
| 8.4 | Actions & Modifiers | Behavioral primitives |
| 8.5 | Abstract Road Network | Road/junction abstractions |
| 8.6 | Behavioral Model | Actor behavior specification |
| 8.7 | Physical Object Actors | Vehicles, pedestrians, objects |
| 8.8 | Movement Actions | Speed, lane change, path following |
| 8.9 | Movement Modifiers | Constraints on movement actions |
| 8.10 | Environment Actors | Weather, time, lighting entities |
| 8.11 | Environment Actions | Weather changes, time progression |
| 8.12 | Road Abstraction Classes | Lane, road, junction types |
| 8.13 | Primitive Types | int, float, string, bool, etc. |
| 8.14 | Physical Types | speed, acceleration, distance, etc. |
| 8.15 | Traffic Lights | Signal state definitions |
| 8.16 | Standard Library | Built-in types and functions |

## Deliverables

- Domain model library (`.zip`)
- Consolidated EBNF grammar

## Relationship to ENVITED-X `scenario` Domain

The ENVITED-X `scenario` domain ontology describes **credentials** for scenario data assets. ASAM OpenSCENARIO DSL defines the **language** those scenarios are written in.

| OpenSCENARIO Concept | scenario Ontology Mapping |
|---------------------|--------------------------|
| Scenario file (`.osc`) | The asset described by `ScenarioCredential` |
| Domain model actors | `scenario:actorTypes` |
| Environment settings | `scenario:environmentConditions` (connects to OpenODD taxonomy) |
| Road network reference | `scenario:roadNetworkFormat` (links to OpenDRIVE) |
| Abstraction level | `scenario:abstractionLevel` (concrete vs. abstract) |
| Coverage metrics | `scenario:coverageMetrics` |

## Relationship to ASAM OpenODD

OpenSCENARIO DSL v2.2.0 is one of the three **mapping references** for ASAM OpenODD:
- OpenODD §9 specifies how to express ODD taxonomy, COD/OD, and modules in the OpenSCENARIO DSL
- The ASAM OpenODD model's `TaxonomyConcept` instances can be used directly in OpenSCENARIO scenario conditions
- This enables scenarios to be linked to specific ODD boundary conditions
