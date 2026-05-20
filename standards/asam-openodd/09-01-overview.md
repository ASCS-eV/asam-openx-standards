# ASAM OpenODD® v1.0.0 — 9.1 Overview

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/09_openscenario_dsl/09_01_overview.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.1 Overview

## 9.1.1 Introduction

This mapping reference consists of [Section 9.1, "Overview"](09_01_overview.html),  [Section 9.2, "Modeling taxonomy"](09_02_modeling_taxonomy.html#top-openscenario-modeling-taxonomy),  [Section 9.3, "Modeling COD/OD"](09_03_modeling_cod_od.html#top-openscenario-modeling-cod-od),  [Section 9.4, "Modeling ODD"](09_04_modeling_odd.html#top-openscenario-modeling-odd),  [Section 9.5, "Mapping ASAM OpenODD® to ASAM OpenSCENARIO® DSL"](09_05_mapping_model_to_osc_dsl.html#top-openscenario-mapping), and the annexes  [Section 9.6, "(informative) Usage Guide for model to ASAM OpenSCENARIO® DSL mapping reference"](../11_annexes/11_f_usage_guide_openscenario_dsl.html#top-annexes-usage-guide-dsl), and  [Annex B.2, *ASAM OpenSCENARIO® DSL ISO 34503*](../11_annexes/11_e_iso34503_02_openscenario_dsl.html#top-openscenario-example-iso34503).

## 9.1.2 General information

The model to ASAM OpenSCENARIO® DSL mapping reference describes how to model ODDs, TODs, CODs, and ODs using ASAM OpenSCENARIO® DSL.
The section specifies the mapping between the ASAM OpenODD® model and the representation in ASAM OpenSCENARIO® DSL.
This specification is the foundation for exporting ASAM OpenSCENARIO® DSL representations from the ASAM OpenODD® model and the foundation for importing.

This section describes ASAM OpenSCENARIO® DSL, and its syntax.
ODD modelling uses existing language constructs and syntax, with no addition.
In order to process and utilize the modelled data, an application using these models may need to implement additional methods and external functions.
For example, there is no construct built into the language that makes it possible to compare a set of COD values with the ODD definition.
Such a comparison, which answers the question “Is this COD fully inside the ODD?”, is assumed to be implemented as an external function by the application.

**Scope and limitation**

This mapping reference describes overall capabilities and methodology of using ASAM OpenSCENARIO® DSL for modeling.
It also describes the "forward" mapping from the ASAM OpenODD® model to ASAM OpenSCENARIO® DSL.
The "backward" mapping from ASAM OpenSCENARIO® DSL to the ASAM OpenODD® model is not covered by this version of ASAM OpenODD®.

Several key differences and limitations affect the "backward" mapping process:

* Inheritance support:  
  ASAM OpenSCENARIO® DSL supports inheritance, while the ASAM OpenODD® model supports loose inheritance via delegation (see [Code 54](../06_model_concept/06_02_openodd_taxonomy.html#code-example-concept-taxonomy-inheritance)).
  As a result, models utilizing inheritance in ASAM OpenSCENARIO® DSL cannot be mapped back to the ASAM OpenODD® model, in a one-to-one fashion.
* Subset expressions:  
  ASAM OpenSCENARIO® DSL allows for subset expressions over many-valued attributes, which can also be expressed in the ASAM OpenODD® model, but are again not easily translatable to the ASAM OpenODD® model.

Limitations of the "forward" mapping are:

* Modules and reusability:  
  The ASAM OpenODD® model supports reusable modules and sub-expressions.
  However, ASAM OpenSCENARIO® DSL does not inherently support this feature.
  As a result, reusable modules are flattened into individual expressions during the forward mapping to ASAM OpenSCENARIO® DSL.
* Module titles and labels:  
  In this mapping process, module titles and labels from the ASAM OpenODD® model are mapped as comments in ASAM OpenSCENARIO® DSL, which may result in a loss of structural information when importing back.

## 9.1.3 ASAM OpenSCENARIO® DSL

ASAM OpenSCENARIO® DSL is an ASAM standard that defines the following:

* A domain-specific language (DSL) with the characteristics of a human and machine-readable software programming language.
* An extendable domain model, which represents the central concepts of the on-road driving domain.

The standard is specifically designed for large-scale verification and validation (V&V), to support this it comes with extensive reusability features.
Its purpose is to test the safety and functionality of autonomous vehicles (AV) and advanced driver-assistance systems (ADAS).
ASAM OpenSCENARIO® DSL may be used in conjunction with many other ASAM standards to enable fully-fledged V&V workflows.
It emphasizes composition and the reuse of scenario descriptions, that allow simple scenarios to serve as building blocks for more complex ones.
It enables both location-specific as well as map or ODD-agnostic scenario descriptions, that enable wide applicability.
The language supports various concrete, logical, and abstract scenario descriptions.
These scenarios include maneuvers that involve multiple vehicles, other traffic participants, complex environmental interactions, complex variations of testing parameters, and the evaluation and analysis of complex or compound measurement criteria.
The standard is used in virtual development, testing, as well as validation of functions for driver assistance, automated driving, and autonomous driving.
However, it is also suitable for testing on test tracks or proving grounds, for testing in a mixed environment (HiL), and for decoding real-world driving data.
It enables exploration of scenario and functionality space to identify potential unknowns.
The built-in abstract road descriptions enable many-to-many reuse of scenarios and ODD specifications.
Once modelled, the ODD, COD, or TOD model can be imported into any test scenario expressed in ASAM OpenSCENARIO® DSL, referenced by the test scenario, and used for KPI measurements and coverage measurements.

ASAM OpenSCENARIO® DSL supports the following language features that are ideally suited also for the purpose of modeling ODD definitions:

* Definition of structured types and enumeration types to represent ODD domain concepts and data types (Taxonomy)
* Adding constraints to types to specify ODD constraints
* Extension of types to refine existing types by adding additional constraints
* Specialization (inheritance) of types for modularization and reuse
* Modularization of the type definitions into files and file-based imports for modularization and reuse
* Specifying external functions for additional functionality, for example to realize the mapping of real world or simulation states to COD models

## 9.1.4 Syntax and EBNF

The model to ASAM OpenSCENARIO® DSL mapping reference uses the exact same syntax as ASAM OpenSCENARIO® DSL.
The syntax specification can be found in Section 7, "Language Reference Manual" of ASAM OpenSCENARIO® DSL [[2](../bibliography.html#bib-oscdsl)].

ASAM supplies an informative representation of an EBNF that represents the syntax.
This EBNF description can be used to accelerate the development of applications that would like to compile ASAM OpenSCENARIO® DSL for any purpose.
Among them the compilation and parsing of ODD models is represented in model to ASAM OpenSCENARIO® DSL mapping reference.
The EBNF file is a deliverable of ASAM OpenSCENARIO® DSL [[2](../bibliography.html#bib-oscdsl)].

|  |  |
| --- | --- |
|  | Deliverables  Deliverables' menu can be found on the top right corner of the ASAM OpenSCENARIO® DSL web page. |

## 9.1.5 Illustrative overview

### 9.1.5.1 General information

This section illustrates a possible scenario for the use of ASAM OpenSCENARIO® DSL-based ODD definitions in a scenario-based V&V process using a simplified example.
The ASAM OpenSCENARIO® DSL code is intentionally omitted from this illustration.

[Figure 21](#fig-overview-files-and-models-in-scenario-based-v-v) shows how the scenario- and ODD-related aspects that form the basis for a scenario-based V&V process could be organized in different ASAM OpenSCENARIO® DSL files.
The simplified ODD definition for an autonomous airport shuttle serves as an example.

An ASAM OpenSCENARIO® DSL simulation engine loads a scenario model, which imports a specific ODD definition file (`ODD_Shuttle_Service_Barcelona_Airport.osc`).
The ODD definition in this file can be an extension, refinement, or both of another, more general ODD definition (`ODD_Spain.osc`), which in turn defines constraints based on a common definition of ODD concepts.
For example, this is the case according to the taxonomy defined in the ISO 34503 [[4](../bibliography.html#bib-iso34503)] standard (`Domain_Concepts_Definition_ISO_34503.osc`).

For certain regions or application contexts, ODD definitions could be based on additional domain concept definitions, which means taxonomies or taxonomy extensions, for example specific road signs or road types (`Domain_Concepts_Definition_Roadsigns_Spain.osc`).

During the execution of the ASAM OpenSCENARIO® DSL scenario to perform the scenario-based V&V, a possible use case is to check whether the execution state satisfies the ODD definition.
For example, verify whether a scenario execution is within the bounds of the ODD at all times, or, if not, whether the vehicle under test (VUT) correctly responds to the violated ODD constraints (ODD-exit maneuver).

![Files and models in a scenario-based V&V process](../_images/OpenSCENARIO_DSL/overview-files-and-models-in-scenario-based-v-v.png)

Figure 21. Files and models in a scenario-based V&V process

[Figure 21](#fig-overview-files-and-models-in-scenario-based-v-v) shows files and models in a scenario-based V&V process.

To check whether a world state, which is a state of a simulation, recorded trace, or a measured real-world state, satisfies the ODD constraints, the current world state must be mapped to the abstraction level of the concepts that appear in the ODD definition, so that the ODD constraints can be checked.
This is achieved by creating an instance model of the ODD domain concepts that are based on the world state.

The resulting instance model of the ODD domain concepts that reflects the current world state is called the Current Operational Domain (COD).
To check whether the current world state satisfies the ODD constraints, it must be checked whether the COD model satisfies the constraints that are specified in the ODD specification.

[Figure 22](#fig-overview-type-and-instance-models-in-a-scenario-based-v-v-process) illustrates this approach by a simplified example.
The top left shows some of the types defined in a domain concept definition file that is based on the ISO 34503 [[4](../bibliography.html#bib-iso34503)] taxonomy.
It shows the types `odd`, which is the root element in the ISO 34503 taxonomy [[4](../bibliography.html#bib-iso34503)], `environmental_conditions`, and `weather`.
The weather type defines two properties, `wind` and `rainfall`, that are typed over the enum data types `wind_kind` and `rain_kind`.

|  |  |
| --- | --- |
|  | Enum or categorical?  ASAM OpenSCENARIO® DSL uses *enumerated types* (`enum`) to model a finite number of named values, for example wind or rain strengths. In ASAM OpenODD®, these are called `categoricals`. These are the same concepts. |

The ISO 34503 taxonomy hierarchy is modeled as a hierarchy of structured types, which means a containment hierarchy, between the ASAM OpenSCENARIO® DSL types.
The COD model at the bottom left always consists of an instance of the ODD root type, which contains, directly or indirectly, instances of other types as defined by the structured types` hierarchy.
In a use case where an ASAM OpenSCENARIO® DSL engine executes a driving scenario, the simulation state must be mapped to the COD model.
The simulated world state typically has some more detailed representation of the current weather.
For example, the current wind speed is represented by some numeric value like 5.23 m/s, which must be mapped to the corresponding wind kind, which is gentle\_breeze.
The same holds for other properties of the weather, road types, road features, traffic properties, and so on , that are of interest at the ODD level.
For example, [Figure 22](#fig-overview-type-and-instance-models-in-a-scenario-based-v-v-process) illustrates that a coordinate location might be mapped to a geographical zone defined on the ODD level, for which certain constraints hold conditionally.

It may happen that certain world- or simulation-state concepts are mapped to enum values like wind kind, but that the same phenomenon is additionally represented by a numerical value on the ODD-level, for example a numerical representation of the wind speed.
In this case, it is the responsibility of the world- and simulation-state-to-COD-mapping to ensure that the values are mapped to the COD model consistently.

Based on this COD model, which reflects the world state properties, the constraint-checking capabilities of an ASAM OpenSCENARIO® DSL engine can be used to check whether the COD satisfies the ODD constraints.
This information can be used to control the scenario, for example to check that the simulation satisfies the ODD constraints, to verify whether the VUT triggers appropriate ODD exit maneuvers when ODD constraints are violated, or to formulate ODD-based coverage goals.

![Overview type and instance models in a scenario based v-v process](../_images/OpenSCENARIO_DSL/overview-type-and-instance-models-in-a-scenario-based-v-v-process.png)

Figure 22. Overview of type and instance models in a scenario-based V&V process

[Figure 22](#fig-overview-type-and-instance-models-in-a-scenario-based-v-v-process) shows an overview type and instance models in a scenario based V&V process.

The containment relationships between the types in the definition models of the ODD domain concepts, which are similar to the taxonomy hierarchy, have a cardinality of one.
For example, an instance of the `EnvironmentalConditions` type always has exactly one contained instance of the `Weather` type.
Properties can be single-valued or many-valued.
For example, a vehicle may encounter multiple road features at the same time, like speed bumps, cracks, or potholes (see ISO 34503 [[4](../bibliography.html#bib-iso34503)], Section 9.3.7, "Drivable area surface") (many-valued attribute), while there can only be one current wind speed (single-valued attribute).

### 9.1.5.2 Working with geographical zones

ODD definitions might formulate specific conditions for specific geographical zones.
In some cases, the operation of vehicles may only be allowed in certain zones, or special constraints could be applied in a certain area.

Within the ODD domain concepts definition, the taxonomy, the zones are represented with an enum type that may be called `zone`.
The current zone of the subject vehicle is then modeled by a field typed over that enum.
An ODD can extend this enum type and add additional zones as simple named enum literals, for example `airport_zone1` or `airport_zone2`.
The specific geographical boundary of each zone is modeled outside the ASAM OpenSCENARIO® DSL representation of the ODD.
They could be modeled as a list of GPS coordinates or by using shapefiles.
An external method must then be implemented to determine the current zone based on the position of the subject vehicle, as part of the mapping from the world state to the ODD abstraction level.

[Figure 23](#fig-overview-geo-zones-in-a-scenario-based-v-v-process) shows on the top left how a base ODD model defines a `scenery` class with a `current_zone` attribute that is typed over an enum type `zone`.
This enum type initially only has one value `undefined` that represents an undefined zone.
A specific ODD extension would extend this enum type and add one or more specific zones as additional enum values.
These may be relevant to the ODD.
For example, the ODD disallows pedestrians in certain areas and not in others or the traffic speed must be different in different zones.
[Figure 23](#fig-overview-geo-zones-in-a-scenario-based-v-v-process) shows two example constraints:

* (1) Pedestrians are disallowed in zones 102 and 103.
* (2) The traffic speed must be at most 80 km/h in zones 101 and 102.

On the bottom right [Figure 23](#fig-overview-geo-zones-in-a-scenario-based-v-v-process) shows how a geographical zone could be specified in an external file, for example an existing format like OpenDRIVE or a shape file.
The task of mapping to the COD model is to determine whether the current position of the ego vehicle is within one of the specified zones.
The mapping then sets the `current_zone` attribute to the corresponding value.
Constraint checking can now evaluate whether the current state is within the ODD or not.
In this case, the constraint is not violated, since the vehicle is currently not in a zone where pedestrians are disallowed and the traffic speed is below 80 km/h.

![Process of deriving the current geographical zone from the world/simulation-state-level to the ODD-level](../_images/OpenSCENARIO_DSL/overview-geo-zones-in-a-scenario-based-v-v-process.png)

Figure 23. Process of deriving the current geographical zone from the world/simulation-state-level to the ODD-level

[Figure 23](#fig-overview-geo-zones-in-a-scenario-based-v-v-process) shows an process of deriving the current geographical zone from the world/simulation-state-level to the ODD-level.