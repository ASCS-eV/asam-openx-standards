# ASAM OpenSCENARIO® DSL v2.2.0 — B.8 Workflows for safety engineers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_safety_eng.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.8 Workflows for safety engineers

For safety engineers the study of the following workflows is recommended.

## B.8.1 Workflow list

* [Section B.8.2](#sec-up-workflow-1351)  
  As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to derive a simulation scenario from findings of a SOTIF analysis. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.
* [Section B.8.3](#sec-up-workflow-1352)  
  As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to derive new hazardous events, system insufficiencies or triggering conditions for SOTIF from findings during a simulation run. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.
* [Section B.8.4](#sec-up-workflow-1353)  
  As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to replay different variants of a critical scenario observed on the road in simulation, to derive new SOTIF insights from it. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.
* [Section B.8.5](#sec-up-workflow-1354)  
  As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to create scenarios that are going to produce emergent behavior of the DUT to discover knowns and unknowns. ASAM OpenSCENARIO shall enable a demonstration that minimizes residual risk to the DUT. The SOTIF workflow focuses on ensuring the absence of unreasonable risk because of hazards resulting from insufficiencies in the intended functionality or from reasonably foreseeable misuse.

## B.8.2 Deriving a simulation scenario from findings of a SOTIF analysis

### B.8.2.1 Workflow short description

As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to derive a simulation scenario from findings of a SOTIF analysis. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.

### B.8.2.2 Workflow detailed description

Testing scenarios often do not cover all the safety aspects of a topic/feature.
Some safety problems are unfortunately uncovered too late in the development/testing timeline, as they are present even if the system is functioning as defined.
Safety issues can be discovered by a SOTIF engineer, a V&V engineer, an AV developer or a scenario creator using ASAM OpenSCENARIO.
As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to derive a simulation scenario from findings of a SOTIF analysis. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.

### B.8.2.3 Workflow diagram

![Deriving a simulation scenario from findings of a SOTIF analysis](../_images/diag-a1a91acb25f8db76d4214825a6f2b12ff22a38a8.png)

Figure 42. Deriving a simulation scenario from findings of a SOTIF analysis

### B.8.2.4 Steps for discovering scenarios that uncover safety hazards

ASAM OpenSCENARIO must enable a SOTIF engineer, a V&V engineer, an AV developer or a scenario creator to discover safety issues.

#### B.8.2.4.1 Handling stub

1. Model the scenario Stub in semiformal language.  
   A scenario stub is a fragment from an (abstract or concrete) scenario that covers just the moment immediately before a supposed hazard or accidents and contains just the actors and details that are necessary to characterize what supposedly could lead to a hazard.
   Example: Another car is overtaking the ego vehicle, then merging into the ego vehicle’s lane at short distance and braking hard immediately after.
2. Formalize scenario Stub.
3. Generalize scenario Stub.  
   Generalization refers to the removal of unintended constraining conditions.  
   Example: "Another car is overtaking the ego vehicle…​" → Could it also be a truck or motorcycle that provokes the same outcome?

#### B.8.2.4.2 Handling context

1. Specify context.  
   Context is the ODD subset (or operational situation in ISO 26262 [[19](../../bibliography.html#bib-iso26262)] language) where the scenario plays.  
   Example: Driving on a highway at medium speed under reduced visibility conditions.
2. Formalize context.

#### B.8.2.4.3 Handling conditions

1. Specify hazardous condition.  
   A hazardous condition is a guard condition that indicates that a hazard is present and that shall be monitored later during simulation.  
   Example: The distance to the predecessor vehicle is lower than 1 m when the ego speed is higher than 10 km/h.

#### B.8.2.4.4 Creating scenarios

1. Formalize observer condition for simulation.  
   Semiformal notation can be tables, activity diagrams, template language and so on. Formalizing means to …​
2. Create new logical scenario if existing scenario pool does not contain appropriate base scenario and environment.
3. Enrich logical scenario.  
   Enrichment means to add further details that were not present in the scenario stub (for example, weather effects, roadside objects, actors).

#### B.8.2.4.5 Analyzing and refining

1. Perform sensitivity analysis to find out relevant parameters.
2. Create parameter variants by setting parameters.
3. Add new concrete scenarios with observer conditions to simulation backlog.

At the end of the process the SOTIF engineer, the V&V engineer, the AV developer or the scenario creator can derive a simulation scenario from findings of a SOTIF analysis.

## B.8.3 Deriving new hazardous events, system insufficiencies or triggering conditions for SOTIF from findings during a simulation run

### B.8.3.1 Workflow short description

As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to derive new hazardous events, system insufficiencies or triggering conditions for SOTIF from findings during a simulation run. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.

### B.8.3.2 Workflow detailed description

Testing scenarios often do not cover all the safety aspects of a topic/feature.
Some safety problems are unfortunately uncovered too late in the development/testing timeline, as they are present even if the system is functioning as defined.
Safety issues can be discovered by a SOTIF engineer, a V&V engineer, an AV developer or a scenario creator using ASAM OpenSCENARIO.
As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to derive new hazardous events, system insufficiencies or triggering conditions for SOTIF from findings during a simulation run. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.

### B.8.3.3 Workflow diagram

![Deriving new hazardous events, system insufficiencies or triggering conditions for SOTIF from findings during a simulation run](../_images/diag-44b9b070bc9a6cc7a081b48ef4d9f5a7bb395f34.png)

Figure 43. Deriving new hazardous events, system insufficiencies or triggering conditions for SOTIF from findings during a simulation run

### B.8.3.4 Steps for discovering scenarios that uncover safety hazards

ASAM OpenSCENARIO must enable a SOTIF engineer, a V&V engineer, an AV developer or a scenario creator to discover safety issues.

The workflow for a *hazardous scenario from simulation* is a straight forward workflow.
Two of the steps consist of several sub-steps that are described in detail in the next chapters.

#### B.8.3.4.1 Main steps

1. Log incident.
2. Analyze scenario in parallel.  
   See [Section B.8.3.4.2](#_analyzing_scenario_in_parallel) for a description of the tasks that can run in parallel.
3. Perform sensitivity analysis to find out relevant parameters.
4. Add new logical scenario(s) if existing scenario pool is insufficient to reproduce the incident in all the imagined variants.
5. Extract information.  
   See [Section B.8.3.4.3](#_extracting_information_in_parallel) for tasks that can run in parallel.
6. Export context, triggering conditions (with occurrence frequency estimate) and hazardous behavior to SOTIF analysis tool.

#### B.8.3.4.2 Analyzing scenario in parallel

The following steps are part of the second step in [Section B.8.3.4.1](#_main_steps).
They can be performed in parallel.

1. Extract underlying base scenario  
   The logical base scenario contains the context situation (for example, driving on a highway at night), the placement of the objects and actors and the script for the storyline.
   It has open parameters.
   The behavior of the ego vehicle (and potentially other actors) is not determined by the scenario, but by its own control functions.
2. Extract specific parameters.
3. Handle other actors.

   1. Analyze other actors' behavior  
      In some simulation environments, other actors are given a certain freedom to act, specifying just their driving policy.
      This induces some non-determinism. To replay the scenario, their behavior must be captured, analyzed and formalized through driving analytics.
   2. Model other actors' behavior for replay.
4. Handle observer.

   1. Analyze hazardous behavior of ego vehicle.
   2. Formalize observer condition for simulation.  
      An observer condition is a logical condition that characterizes the presence of a hazard or a faulty behavior of the ego vehicle during simulation.  
      Example: Vehicle decelerates without a reason; distance to predecessor vehicle is getting too low.

#### B.8.3.4.3 Extracting information in parallel

The following steps are part of the fifth step in [Section B.8.3.4.1](#_main_steps).
They can be performed in parallel.

1. Extract Context Situation for SOTIF analysis.
2. Extract Triggering Conditions for SOTIF analysis.
3. Optional: Estimate occurrence frequency of scenario.  
   This usually requires external data sources and can be regarded as an activity outside of this use case.

At the end of the process the SOTIF engineer, the V&V engineer, the AV developer or the scenario creator can derive new hazardous events, system insufficiencies or triggering conditions for SOTIF from findings during a simulation run.

## B.8.4 Replaying different variants of a critical scenario observed on the road in simulation, to derive new SOTIF insights from it

### B.8.4.1 Workflow short description

As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to replay different variants of a critical scenario observed on the road in simulation, to derive new SOTIF insights from it. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.

### B.8.4.2 Workflow detailed description

Testing scenarios often do not cover all the safety aspects of a topic/feature.
Some safety problems are unfortunately uncovered too late in the development/testing timeline, as they are present even if the system is functioning as defined.
Safety issues can be discovered by a SOTIF engineer, a V&V engineer, an AV developer or a scenario creator using ASAM OpenSCENARIO.
As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to replay different variants of a critical scenario observed on the road in simulation, to derive new SOTIF insights from it. This refers to SOTIF and safety hazards that can be present even if the system is functioning as designed, without a malfunction.

### B.8.4.3 Workflow diagram

![Replaying different variants of a critical scenario observed on the road in simulation, to derive new SOTIF insights from it.](../_images/diag-d79b48f05a3cb8408d4e7ef05f51011395b37189.png)

Figure 44. Replaying different variants of a critical scenario observed on the road in simulation, to derive new SOTIF insights from it.

### B.8.4.4 Steps for discovering scenarios that uncover safety hazards

ASAM OpenSCENARIO must enable a SOTIF engineer, a V&V engineer, an AV developer or a scenario creator to discover safety issues.

Processing a *hazardous scenario from road testing or field operation* is straight forward.
See [main steps](#_main_steps).
Two steps contain sub-steps that can be processed in parallel.

#### B.8.4.4.1 Main steps

1. Ingest incident report, vehicle data logger recordings and camera footage/sensor logs.
2. Extract and formalize.  
   See [Section B.8.4.4.2](#_extracting_and_formalizing) for more details.
3. Create new logical scenario if existing scenario pool does not contain appropriate base scenario and environment.  
   The logical base scenario contains the context situation (for example, driving on a highway at night), the placement of the objects and actors, and the script for the storyline.
   It has open parameters.
   The behavior of the ego vehicle (and potentially other actors) is not determined by the scenario, but by its own control functions.
4. Create scenario output.  
   See [Section B.8.4.4.3](#_creating_scenario_output) for more details.

#### B.8.4.4.2 Extracting and formalizing

The following steps are part of the second step in [Section B.8.3.4.1](#_main_steps).
They can be performed in parallel.

1. Formalize Ego Vehicle trajectory and actions.
2. Handle other actors.

   1. Identify relevant other actors.
   2. Formalize other actors' trajectory and actions.
3. Extract relevant road geometry and markings.
4. Extract relevant environmental conditions.
5. Extract relevant objects.
6. Handle observer.

   1. Analyze hazardous behavior of Ego vehicle.
   2. Formalize observer condition for simulation.  
      An observer condition is a logical condition that characterizes the presence of a hazard or a faulty behavior of the ego vehicle during simulation.  
      Example: Vehicle decelerates without a reason; distance to predecessor vehicle is getting too low.

#### B.8.4.4.3 Creating scenario output

The following steps are part of the fourth step in [Section B.8.3.4.1](#_main_steps).
They can be performed in parallel.

1. Prepare scenario.

   1. Enrich and set parameters to create concrete scenario.  
      The concrete scenario is the abstract scenario with selected parameters.
      In this case it is intended to be a good approximation of what happened on the road.
   2. Model other actors' behavior for replay.  
      In some simulation environments, other actors are given a certain freedom to act, specifying just their driving policy. This induces some non-determinism.
      To replay the scenario, their behavior must be captured, analysed and formalized through driving analytics.
   3. Optional: Perform sensitivity analysis to find out relevant parameters.
      Depending on the verification phase it may be enough to reproduce just the concrete scenario that created the issue, or to derive variants to see which parameters are significant, and which other scenarios may also result in hazardous behavior.
   4. Optional: Create parameter variants by setting parameters.
   5. Optional: Add new concrete scenarios with observer conditions to simulation backlog.
2. Export Context, Triggering Conditions (With Occurrence Frequency Estimate) and hazardous behavior to SOTIF analysis tool.

At the end of the process the SOTIF engineer, the V&V engineer, the AV developer or the scenario creator discovers safety hazard thanks to ASAM OpenSCENARIO.

## B.8.5 Evaluating of residual risk because of unknown scenario

### B.8.5.1 Workflow short description

As a SOTIF safety engineer and/or V&V engineer, AV developer, scenario creator, I can use ASAM OpenSCENARIO to create scenarios that are going to produce emergent behavior of the DUT to discover knowns and unknowns. ASAM OpenSCENARIO shall enable a demonstration that minimizes residual risk to the DUT. The SOTIF workflow focuses on ensuring the absence of unreasonable risk because of hazards resulting from insufficiencies in the intended functionality or from reasonably foreseeable misuse.

### B.8.5.2 Workflow detailed description

Residual risk of hazardous behavior can be caused by unknown situations.

Demonstrating that this residual risk is acceptably low is a requirement of current AD safety standards (for example, ISO 21448 [[7](../../bibliography.html#bib-iso21448)], UL 4600 [[20](../../bibliography.html#bib-ul4600)]).

To demonstrate that the risk is low you can use this two-step task:

1. Identify unknown situations leading to hazard.
2. Argue that the risk caused by those situations is still unknown.

You can form the following hypothesis for your argumentation of step 2:

1. Sufficiently dense coverage of the entire ODD by test scenarios reveals almost all such situations.
2. The risk that some situations leading to hazards still slip through is low enough to be acceptable.

ASAM OpenSCENARIO in combination with OpenODD and OpenXOntology can support this procedure by allowing scenario variant creation to cover the ODD and by providing metrics for sufficient coverage.

The general process to derive abstract scenarios from the ODD and concretize them, and to measure the coverage of the ODD, can be described as follows.

The ODD, as specified in the ASAM OpenODD® language, can be understood as a multi-dimensional delimited space.
The dimensions are the ODD aspects like road type, lane number, lane with, weather conditions, visibility, presence of infrastructure like guardrails and so on.

The value ranges have one of the following characteristics:

* They are *discrete by nature*.  
  (For example, the number of lanes.)
* They are *made discrete* by the underlying ontology.  
  (For example, road type = {highway, country road, city street, off-road}.)
* They are from a *continuous range*.  
  (For example, lane width, visibility range.)

With the OpenODD language you can to define equivalence classes (like short visibility = 0..50 m, medium visibility = 50..150 m, and so on).

You can use these inputs to define abstract scenarios that cover all combinations.
You can also define scenarios that cover a systematically derived subset of all combinations.
The define step can be done automatically.
Strategies for automatic definition are known from software testing, see for instance [[21](../../bibliography.html#bib-Ostrand_1988)], [[22](../../bibliography.html#bib-Grochtmann_1995)], [[23](../../bibliography.html#bib-Kruse_2010)].

Note that coverage of the ODD, which is similar to an empty space, is not enough.

On top of the *basic ingredients* of a scenario that was selected from the ODD categories (for example, road type, weather, number of lanes…​) other ingredients are needed:

* *Variable elements*  
  like road decoration (bridges, road signs)
* *Static objects*  
  (buildings, obstacles)
* *Other traffic participants*  
  and their potential maneuvers
* *Associated parameters*  
  (for example, road friction).
  Catalogs should be available as an input for these parameters.

Approaches to define these ingredients are described for instance in [[24](../../bibliography.html#bib-Pegasus_2019)], [[25](../../bibliography.html#bib-Schuldt_2018)], [[26](../../bibliography.html#bib-Scholtes_2021)].

### B.8.5.3 Workflow diagram

![Evaluating of residual risk because of unknown scenario](../_images/diag-8dd745966dec494f6a4938184f769c37f7ae4cf7.png)

Figure 45. Evaluating of residual risk because of unknown scenario

### B.8.5.4 Steps for evaluating of residual risk because of unknown scenario

1. The workflow consists of a few operations that can be done in parallel:

   1. Ingest an ODD, potentially in OpenODD compliant format
   2. Ingest a catalog of road decoration, static objects, …​
   3. Ingest a catalog of actors and their potential behaviors
2. All of these steps mus be followed by an equivalence class partitioning.
3. A new logical scenario must be added to the existing scenario pool, but only if it does not exist yet.
4. The logical scenario can be enriched with the required objects and actors.
5. All these actions can be done while the definition of the criteria for coverage density is ongoing.
6. Finally, a concrete scenario can be created and added to the simulation backlog.

At the end of the SOTIF review process it is proven that the test case helps to ensure minimum residual risk.