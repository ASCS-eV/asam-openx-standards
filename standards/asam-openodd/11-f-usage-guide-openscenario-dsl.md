# ASAM Openodd v1.0.0 — 9.6 (informative) Usage Guide for model to ASAM OpenSCENARIO DSL mapping reference

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_f_usage_guide_openscenario_dsl.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.6 (informative) Usage Guide for model to ASAM OpenSCENARIO DSL mapping reference

## 9.6.1 General information

This section is a guide for using ASAM OpenSCENARIO DSL to model taxonomies, ODDs, and to integrate these models into scenario based V&V activities.
ASAM OpenSCENARIO DSL is ASAM’s standard Scenario Description Language intended for large scale V&V of Automated Driving Systems (ADS) and Advanced Driver Assistance Systems (ADAS), that support Test Scenarios which may include coverage measurement, checks, and KPI analysis in the scenario description.
For more details, see the ASAM OpenScenario DSL specification [[2](../bibliography.html#bib-oscdsl)].

ODD definitions play a key part in the process of verifying and validating ADS and ADAS.
Therefore, ODD definitions must be modeled and incorporated into a scenario-based V&V process in a way that enables a productive workflow.

|  |  |
| --- | --- |
|  | As this usage guide is focusing usage of ASAM OpenODD models within a V&V flow, the relevant models are the taxonomy, the ODD and the COD. OD (Operational Domain) data is not used within a V&V flow. The OD data and models may be used to design the test and validation plan and prioritize different scenarios and conditions. Details on OD modelling in ASAM OpenSCENARIO DSL can be found in [Section 9.3.3, "Modeling OD"](../09_openscenario_dsl/09_03_modeling_cod_od.html#sec-openscenario-modeling-ods-in-openscenario). |

## 9.6.2 Basic principles

The basic principles for ODD modeling using model to ASAM OpenSCENARIO DSL mapping reference are as follows:

* The taxonomy is represented as ASAM OpenSCENARIO DSL type, where all attributes and concepts are represented as enumerated types or other types within this type.
   [Annex B.2, *ASAM OpenSCENARIO DSL ISO 34503*](11_e_iso34503_02_openscenario_dsl.html#top-openscenario-example-iso34503) presents a full modeling of ISO 34503 [[4](../bibliography.html#bib-iso34503)] taxonomy using ASAM OpenSCENARIO DSL.
* The ODD is modeled by applying constraints on the taxonomy types.
  The constraints are specifying the ODD boundaries, out of the full range described by the type.
* Each COD is an instance of the ODD type.
  It is assumed that a mechanism to create the instance and fill it with sampled value is implemented within the application.
* A TOD can be described the same way an ODD through constraints on the taxonomy.

Once this modeling is applied, ODD models can immediately be incorporated into test scenarios, be subject to coverage measurements, event handling, and so on.
Different examples are supplied within the document.
It should be noted that while ASAM OpenODD provides an export mechanism from the ASAM OpenODD model to this mapping reference representation, a user can actually model ODDs directly with the ASAM OpenSCENARIO DSL in text form without using the ASAM OpenODD database of the ASAM OpenODD model.

## 9.6.3 Overview

This section overviews how this mapping reference uses ASAM OpenSCENARIO DSL-based ODD definitions in a scenario-based V&V process.
However, the test design methodology and the mechanism on how to integrate the ODD definitions with scenario definitions on the tool level are outside the scope of this document.
Assuming [Figure 25](#fig-overview-files-and-models-in-scenario-based-v-v-process) represents the full V&V flow, this document focuses on merging scenarios with ODDs and on specific aspects related to V&V.
It does not cover implementation details of the test platform.

[Figure 25](#fig-overview-files-and-models-in-scenario-based-v-v-process) shows how the scenario- and ODD-related aspects that form the basis for a scenario-based V&V-process could possibly be organized in different ASAM OpenSCENARIO DSL files.
As an example serves the simplified ODD definition for an autonomous airport shuttle.
An ASAM OpenSCENARIO DSL simulation engine loads a scenario model, that imports a specific ODD definition file like `ODD_Shuttle_Service_Barcelona_Airport`.
The ODD definition in this file can be an extension, refinement or both of another, that in turn defines constraints based on a common definition of ODD concepts, for example according to the taxonomy defined in the ISO 34503 [[4](../bibliography.html#bib-iso34503)] standard like `Domain_Concepts_Definition_ISO_34503`.

For certain regions or application contexts, ODD definitions could be based on additional domain concept definitions (taxonomies), for example specific road signs or road types like `Domain_Concepts_Definition_Roadsigns_Spain`.
The example stated above demonstrates one possible methodology of maintaining a set of ODD related data with the ability to use ASAM OpenSCENARIO DSL “import” statements in order to combine the files according to the specific needs of the use case.
This is the basic paradigm for a reuse methodology.

![Files and models in a scenario-based V&V process](../_images/OpenSCENARIO_DSL/overview-files-and-models-in-scenario-based-v-v.png)

Figure 25. Files and models in a scenario-based V&V process

[Figure 21](../09_openscenario_dsl/09_01_overview.html#fig-overview-files-and-models-in-scenario-based-v-v) shows files and models in a scenario-based V&V process.

As part of the V&V flow, the ODD definition should be imported to a scenario definition.
This is pointed out at the top left corner of [Figure 25](#fig-overview-files-and-models-in-scenario-based-v-v-process), where “ODD Shuttle…” is imported into the scenario file to form a coherent input to the scenario engine.
Another possible usage is to analyze actual logs of simulations and real world tests.
When the amount of data available in these logs is given, an usage is also to perform ODD correctness checks in a “post processing” mode.
For example, one possible use case is to check whether the execution state satisfies the ODD definition.
Another use case could be to verify, whether a scenario execution is within the bounds of the ODD at all times, or, if not, whether the vehicle under test (VUT) correctly responds as soon as the execution violated the ODD constraints.
While this check can easily be done as the simulation is running, in order to perform it in a post processing mode, the test log should contain all the data on ODD attributes when it is sampled.
To check whether a world state, a state of a simulation, a recorded trace, or a measured real-world state satisfies the ODD constraints, a **mapping** of the current world state to the concepts appearing in the ODD definition is necessary, so that the ODD constraints can be checked.
This happens by creating an instance model of the ODD domain concepts based on the world state.
A mapping is required to map world state properties to the abstraction level of the ODD domain concepts.

The resulting instance model of the ODD domain concepts that reflect the current world state is called the **Current Operational Domain (COD)** according to ISO 34503 [[4](../bibliography.html#bib-iso34503)] terms.
When checking whether the current world state satisfies the ODD constraints, it also must be checked whether the COD model satisfies the constraints specified in the ODD definition.
[Figure 26](#fig-type-and-instance-models-scenario-based-vv-process) illustrates this approach by a simplified example.
The top left shows some of the types defined in a domain concept definition file that is based on the ISO 34503 taxonomy [[4](../bibliography.html#bib-iso34503)].
It shows the types `odd`, which is the root element in the ISO 34503 taxonomy [[4](../bibliography.html#bib-iso34503)], `environmental_conditions`, and `weather`.
The weather type defines two properties, `wind` and `rainfall`, that are typed over the enum data types `wind_kind` and `rain_kind`.

The ISO 34503 taxonomy hierarchy [[4](../bibliography.html#bib-iso34503)] is modeled as a hierarchy of structured types, which means a containment hierarchy, between the ASAM OpenSCENARIO DSL types.
The COD model at the bottom left always consists of an instance of the ODD root type, which contains, directly or indirectly, instances of other types as defined by the structured types` hierarchy.
In a use case where an ASAM OpenSCENARIO DSL engine executes a driving scenario, the simulation state must be mapped to the COD model.
The simulated world state typically has some more detailed representation of the current weather.

For example, the current wind speed is represented by some numeric value like `5.23 m/s`, which must be mapped to the corresponding wind kind, which is `gentle_breeze`.
The same holds for other properties of the weather, road types, road features, traffic properties, and so on , that are of interest at the ODD level.
For example, [Figure 26](#fig-type-and-instance-models-scenario-based-vv-process) illustrates that a coordinate location might be mapped to a geographical zone defined on the ODD level, for which certain constraints hold conditionally.

It may happen that certain world- or simulation-state concepts are mapped to enum values like wind kind, but that the same phenomenon is additionally represented by a numerical value on the ODD-level, for example a numerical representation of the wind speed.
In this case, it is the responsibility of the world- and simulation-state-to-COD-mapping to ensure that the values are mapped to the COD model consistently.

Based on this COD model, which reflects the world state properties, the constraint-checking capabilities of an ASAM OpenSCENARIO DSL engine can be used to check whether the COD satisfies the ODD constraints.
This information can be used to control the scenario, for example to check that the simulation satisfies the ODD constraints, to verify whether the VUT triggers appropriate ODD exit maneuvers when ODD constraints are violated, or to formulate ODD-based coverage goals.

![image](../_images/OpenSCENARIO_DSL/overview-type-and-instance-models-in-a-scenario-based-v-v-process.png)

Figure 26. Overview of types and instance models in a scenario-based V&V process

[Figure 22](../09_openscenario_dsl/09_01_overview.html#fig-overview-type-and-instance-models-in-a-scenario-based-v-v-process) shows an overview type and instance models in a scenario based V&V process.

The containment relationships among the types in the ODD domain concepts definition models, that resemble the taxonomy hierarchy, have a cardinality of one.
So, for example, an instance of the `EnvironmentalConditions` type always has exactly one contained instance of the `Weather` type.
Properties can be single-valued or many-valued.
For example, a vehicle may encounter multiple road features at the same time, like speed bumps, cracks, or potholes (see ISO 34503 [[4](../bibliography.html#bib-iso34503)], Section 9.3.7, “Drivable area surface”).

The ASAM OpenSCENARIO DSL ODD definition enables to implement the following:

* Stand alone ODD definitions, that can be imported to ODD agnostics scenarios
* Libraries of ODD definitions
* Checks and KPI measurements embedded within a scenario code
* Independent and reusable checks and KPI measurements that can be imported to odd agnostic scenarios, in other words “libraries of checkers”

## 9.6.4 Examples

### 9.6.4.1 ODD agnostic check

[Code 163](#code-odd-agnostic-check1) shows that the generic check is triggered for each ODD exit event, and checks if the exit was a valid one.
The scenario starts and engages a system:

Code 163. Example of generic check (free-form notation)

```
do serial():
    activate_ads_phase: sut.car.activate_ads(acc_cruise_speed)
    # possibly more behavior specified here
    wait @sut.car.cancel_ads or @sut.car.exit_tested_domain
```

The scenario executes, and when an `ODD_exit` event is emitted and captured, the check is called like in [Code 164](#code-odd-agnostic-check2):

Code 164. Example of check call (free-form notation)

```
extend sut_vehicle:
    # Check that exit ODD event is justified
    on @exit_tested_domain if tested_cod.in_ODD():
        # in_ODD() checks cod containment in ODD
        call sut_error(ODD_checks, "ODD: Exit ODDevent raised while within ODD")
```

As shown, after an ODD exit has been recorded, a method is called that checks whether the COD is located within the ODD.
If it is, then this was a false exit.
This check is generic, for every scenario and every ODD.

### 9.6.4.2 ODD agnostic coverage accumulator

As part of V&V, accumulating coverage data is a significant measurement to the quality of the V&V.
One piece of data to accumulate is, which taxonomy concepts or odd attributes were actually covered during testing.
This goal can be achieved by a generic library of coverage monitors, that can be imported to any test scenario.
[Code 165](#code-coverage-monitors) contains two generic coverage monitors:

Code 165. Example of coverage monitors (free-form notation)

```
cover(rain_kind, expression: environmental_conditions.weather.rain_kind)

cover(wind_kind, expression: environmental_conditions.weather.wind_kind)
```

These monitors observe the rain type and wind type during the test, and accumulate the relevant coverage data.

## 9.6.5 Summary

Model to ASAM OpenSCENARIO DSL mapping reference for ASAM OpenODD supplies the ability to model ODDs with ASAM OpenSCENARIO DSL.
The mapping reference enables the following:

* Usage of ASAM OpenSCENARIO DSL to formally specify the ODD
* Incorporation of ODD specification into your V&V flow
* Usage of ASAM OpenSCENARIO DSL for checks, KPI measurements, and ODD coverage measurements

The basic principles of model to ASAM OpenSCENARIO DSL mapping reference for ODD modeling are the following:

* Taxonomy: Define a set of ODD specification properties with ASAM OpenSCENARIO DSL types, for example ISO 34503 [[4](../bibliography.html#bib-iso34503)] taxonomy.
* Model the ODD by applying ASAM OpenSCENARIO DSL constraints on the types.
* Integration into the V&V scenarios, collection of metrics such as KPI and coverage.

These principles and approaches deliver a coherent way to model ODDs, CODs and TODs, and seamlessly incorporate them to V&V flows.
The benefits of reuse are strongly supported.