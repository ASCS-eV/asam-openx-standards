# ASAM Openscenario Dsl v2.2.0 — B.5 Workflows for content or model developers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_content_model_devs.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.5 Workflows for content or model developers

If your main focus is creating content and modelling scenarios, these workflows are for you.

## B.5.1 Workflow list

* [Section B.5.2](#sec-up-workflow-1317)  
  As a content developer, I can use ASAM OpenSCENARIO to create test scenarios that I can supply to my customers who use an ASAM OpenSCENARIO compliant tool chain.
* [Section B.5.3](#sec-up-workflow-1371)  
  As a traffic model developer, an ADAS developer or an end-to-end V&V-engineer, I can use ASAM OpenSCENARIO to enable the inclusion of multiple traffic models and AI-based traffic agents in the scenarios and evaluators.
* [Section B.5.4](#sec-up-workflow-1392)  
  A traffic observer (either a person or an automatic system) can describe what occurred in the real world with ASAM OpenSCENARIO.
* [Section B.5.5](#sec-up-workflow-13411)  
  As a scenario developer, I want to identify failure in the DUT behavior and ensure that a scenario intent was met using ASAM OpenSCENARIO.

## B.5.2 Sharing scenarios with customers

### B.5.2.1 Workflow short description

As a content developer, I can use ASAM OpenSCENARIO to create test scenarios that I can supply to my customers who use an ASAM OpenSCENARIO compliant tool chain.

### B.5.2.2 Workflow detailed description

A customer has a need for a specific ASAM OpenSCENARIO scenario.
The content developer shall read and understand the scenario description, as provided by the customer.
The content developer shall translate the scenario description into ASAM OpenSCENARIO code using a certified and compliant tool chain.
The content developer shall check and validate his implementation of the scenario.
The content developer shall deliver the scenario to the client.

### B.5.2.3 Workflow diagram

![Sharing scenarios with customers](../_images/diag-5f1a89c6403bd5cfe87c5217ade6956a7f0c71cd.png)

Figure 36. Sharing scenarios with customers

### B.5.2.4 Steps for creating and supplying scenarios

A customer describes the scenario he needs using plain natural language or code or pseudo-code and gives this description to the content developer.

The content developer reads, understands, converts and validates the scenario before providing it to the customer.

1. Customer describes the needed scenario.  
   The result is an initial scenario in natural language, code or pseudo-code.
2. Content developer reads and understands the scenario, then converts it ASAM OpenSCENARIO code.  
   The result is an ASAM OpenSCENARIO scenario.
3. Content developer validates the scenario.
4. Content developer shares the scenario with the customer.

At the end of the process the auditor (or the regulator) has a fully compliant and validated ASAM OpenSCENARIO.

## B.5.3 Including traffic models and agents

### B.5.3.1 Workflow short description

As a traffic model developer, an ADAS developer or an end-to-end V&V-engineer, I can use ASAM OpenSCENARIO to enable the inclusion of multiple traffic models and AI-based traffic agents in the scenarios and evaluators.

### B.5.3.2 Workflow detailed description

You should identify your role as a *model developer*, an *ADAS developer* or a *V&V engineer*.

The subsequent operations do not change, regardless of your role.
You need to check if the *scenario*, the *traffic model* and the *traffic agent* already exist.
Add what is missing and change what is already defined if needed.

Finally, you can create and play a scenario with the modified data.

### B.5.3.3 Workflow diagram

![Including traffic models and agents](../_images/diag-eecbbbb22b768398f415959b7bbc7e575c0d5ab8.png)

Figure 37. Including traffic models and agents

### B.5.3.4 Steps for including models and agents

You might want to include traffic models and traffic agents in your scenarios if you own one of these roles:

* Traffic model developer
* ADAS developer
* V&V engineer

#### B.5.3.4.1 General steps

No matter which of the roles you own, the proceedings are always the same.
If your current role does not fit one of the three roles, you simply skip the step of updating the scenario and only follow the [Section B.5.3.4.1](#_general_steps).

1. Are you a traffic model developer, an ADAS developer of a V&V engineer?

   1. If yes, continue with [Section B.5.3.4.2](#_scenario_update).
   2. If no, continue with step 2.
2. Create a playable scenario.
3. Launch the created scenario.
4. Does the scenario show the desired behavior?

   1. If yes, task finished.
   2. If no, improve the scenario and start again with step 1.

#### B.5.3.4.2 Scenario update

In the scenario update step you check traffic models and traffic agents of an existing scenario.
Check for scenario compatibility.

1. Does a scenario exist that matches your needs?

   1. If yes, continue with step 2.
   2. If no, request rework and stop.
2. Does a traffic model exist in the scenario?

   1. If yes, replace the traffic model.
   2. If no, include a traffic model in the scenario.
3. Does a traffic agent exist in the scenario?

   1. If yes, replace the traffic agent.
   2. If no, include a traffic agent in the scenario.

The scenario now has a traffic model and traffic agent included and shows the expected result.

### B.5.3.5 Related topics

* For more information on [traffic models](#TODO) see [[TODO]](#TODO)
* For more information on [traffic agents](#TODO) see [[TODO]](#TODO)

## B.5.4 Describing real world with scenarios

### B.5.4.1 Workflow short description

A traffic observer (either a person or an automatic system) can describe what occurred in the real world with ASAM OpenSCENARIO.

### B.5.4.2 Workflow detailed description

This use case is linked to closing the loop between the physical tests and the simulation.
There are fleets of vehicles which are out there driving and collecting data.
Much of that data is projected to be used to improve the performance and safety of the next generation of vehicles in that fleet.
To do that, the collected data needs to be transformed into a virtual scenario.

All in all this use case describes how to get real-life events and convert them into ASAM OpenSCENARIO format, thus virtualizing them.

### B.5.4.3 Workflow diagram

![Describing real world with scenarios](../_images/diag-dc6b3b1441cd6326ece94d659b4894d66c665e94.png)

Figure 38. Describing real world with scenarios

### B.5.4.4 Steps describing real world with scenarios

1. Record a real-life event.
2. Tag recorded data.
3. Classify the tagged data
   A number of scenarios are identified from the tagged data.
4. Create the road on that the actors drive.  
   This is either a manual or an automated step, depending on the existing methodologies.  
   Typically the road file has been the form of an OpenDRIVE file accompanying the ASAM OpenSCENARIO file.
5. Create the scenario file by identifying lateral and longitudinal movements.  
   A concrete ASAM OpenSCENARIO file is created.
6. Optional: Perform ASAM OpenSCENARIO aggregation. +If this virtualization is part of a bigger campaign, there may be a final process of aggregation, identifying several of these concrete scenarios as the same scenario class and thus merging them into a single logical scenario file.

As a result of this use case it is proven that ASAM OpenSCENARIO as a standard offers all the tools and capabilities to be used as a virtualization tool when recording real-life data.
The different levels of abstraction allow for aggregation of the data, offering a post-processing step that helps simplifying the result.

## B.5.5 Creating self-checking scenarios

### B.5.5.1 Workflow short description

As a scenario developer, I want to identify failure in the DUT behavior and ensure that a scenario intent was met using ASAM OpenSCENARIO.

### B.5.5.2 Workflow detailed description

The goal of a verification and validation process is to identify flaws in the DUT behavior.
Ensuring success criteria involves both identifying a proper DUT behavior and ensuring that the scenario intent was met.

ASAM OpenSCENARIO allows the recording of values at specific execution points.
The recorded data can then be used for further offline analysis.
ASAM OpenSCENARIO also allows performing a verdict analysis for example to check if the intended scenario behaviour is happening as expected or to warn about suspected erroneous DUT behavior.

The following use case describes the process of both identifying failure and ensuring that an intent was met using ASAM OpenSCENARIO.

### B.5.5.3 Workflow diagram

![Creating self-checking scenarios](../_images/diag-2307f1ba2d78bc921cae9df6d967e368b50bc7c5.png)

Figure 39. Creating self-checking scenarios

### B.5.5.4 Steps for creating self-checking scenarios

The following steps introduce an end-to-end V&V process with the special focus on the checking related aspects.

1. Plan goals and outcome  
   This is a team effort to agree on the specific checks and the specific scenarios that are needed for the V&V process.
2. Create executable plan  
   ASAM OpenSCENARIO provides coverage features to set the goals of the verification.
   This constitutes an executable plan to measure the progress of the V&V process.
   Note that the plan can be refined over time.
3. Statically validate the plan  
   Because ASAM OpenSCENARIO allows describing both the abstract scenarios and the desired goals in executable form, technology can statically report unreachable goals without running any scenarios.
4. Create abstract scenarios  
   ASAM OpenSCENARIO enables a user to write his abstract scenarios in a machine-readable way to enable automated creation of multiple concrete scenarios.
   These scenario may include the expected behavior checkers.
   ASAM OpenSCENARIO also allows creating library of well-encapsulated modular scenarios.
   Leveraging these building blocks can assist greatly to compose the scenarios needed for the V&V project.
5. Develop the DUT automation function and setup the tool-chain  
   These steps are needed for executing the scenarios and to achieve the verification task.
6. Run regression on multiple platforms  
   In this step KPI information is evaluated to issue error messages or warnings.
   ASAM OpenSCENARIO also allows to record data for further off-line review.
   Note that ASAM OpenSCENARIO support all execution platforms including HiL, SiLL, proving grounds and real street driving.
7. Debug failures  
   Different vendors may offer different debug capabilities.
   Note that errors might also be issued from the execution platforms and not necessarily from ASAM OpenSCENARIO code.
8. Fix bug or tune checkers  
   An error message or a warning may be issued from a system malfunction or from a bad checker definition.
   At this point you wish to fix the issue and rerun the regressions.
   This iterative process continues till all errors are resolved.
9. Check the V&V goals status  
   The user can now observe the coverage result.
   If some of the planned scenarios were not executed, you may need to rerun the regressions and steer the ASAM OpenSCENARIO tool to focus on these missed areas of concern.

If you finished the plan without any error, you are done with your V&V project.