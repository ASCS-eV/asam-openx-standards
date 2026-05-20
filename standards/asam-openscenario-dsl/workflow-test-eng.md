# ASAM OpenSCENARIO® DSL v2.2.0 — B.13 Workflows for test engineers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_test_eng.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.13 Workflows for test engineers

Test engineers find useful resources here.

## B.13.1 Workflow list

* [Section B.13.2](#sec-up-workflow-1313)  
  As a test engineer working for an AV/ADAS development company, I can define scenarios to build and run tests to test what other developers at other companies are running.
* [Section B.13.3](#sec-up-workflow-1314)  
  As a test engineer, I can define scenarios and run tests as close as possible to each other regardless of the execution platforms.
* [Section B.13.4](#sec-up-workflow-1326)  
  As a test engineer/auditor/regulator, I can easily trace test cases, scenarios and results back to the requirements.
* [Section B.13.5](#sec-up-workflow-1328)  
  As a test engineer, I can use ASAM OpenSCENARIO to enable specification of a driving mission through inclusion of multiple maneuvers in a sequence or in parallel for both DUT and any other traffic agents.
* [Section B.13.6](#sec-up-workflow-1329)  
  As a test engineer, I can use ASAM OpenSCENARIO to accomplish a selected driving mission with an indication of whether the mission has been accomplished, what are the mission KPIs and how they are computed, and whether the unambiguous goals of the mission have been reached.
* [Section B.13.7](#sec-up-workflow-1342)  
  As a test engineer, I can create ASAM OpenSCENARIO scenarios based on abstract test descriptions, for example textual regulations like NCAP tests, UNECE regulations or a requirement list.
* [Section B.13.8](#sec-up-workflow-1346)  
  As a test engineer, I can reuse/combine scenario elements and complete scenario definitions for the creation of new scenarios without the need of copy-paste.
* [Section B.13.9](#sec-up-workflow-1347)  
  As a test engineer, I have a clear guideline where to specify test aspects (what is inside an abstract or logical scenario and what is outside of it (for example, in experiments or test case definitions or in a map file).
* [Section B.13.10](#sec-up-workflow-1348)  
  As a development project lead, I can create scenarios on an abstract level to document the functional behavior for legal reasons.
* [Section B.13.11](#sec-up-workflow-1349)  
  As a test engineer, I can use recorded real-world data to automatically detect/classify or generate scenarios that describe the recorded situation.
* [Section B.13.12](#sec-up-workflow-1381)  
  As a test engineer, I can execute different ASAM OpenSCENARIO files in an automated way with my ASAM OpenSCENARIO compliant tool chain.  
  No file modifications are needed.
* [Section B.13.13](#sec-up-workflow-1382)  
  As a test engineer, I can execute the same ASAM OpenSCENARIO files on different ASAM OpenSCENARIO compliant tool chains.
* [Section B.13.14](#sec-up-workflow-1383)  
  As a test engineer, I can leverage an ASAM OpenSCENARIO engine to convert abstract scenarios into concrete scenarios which can then be tested.
* [Section B.13.15](#sec-up-workflow-1384)  
  As a test engineer, I can run the same test case in a MiL, SiL, HiL environment as well as in a real car controlled by driving robots or human drivers, with a real or partially simulated environment.
* [Section B.13.16](#sec-up-workflow-1393)  
  Test engineers on a test track can define their own specific test track goals as coverage and work to achieve them.  
  They can also leverage the same scenario with other platforms.  
  In such a way tolerances and deviations between test description and test execution become obvious.
* [Section B.13.17](#sec-up-workflow-13210)  
  As a test engineer, I can set goals and measure the V&V progress using functional coverage.

## B.13.2 Using scenarios for cross-company testing

### B.13.2.1 Workflow short description

As a test engineer working for an AV/ADAS development company, I can define scenarios to build and run tests to test what other developers at other companies are running.

### B.13.2.2 Workflow detailed description

If you want to run a test using a scenario that was not build by yourself you need to import the scenario into your simulation platform somehow.

Usually another company (from now on called *'company B'*) delivers the scenario they use in some form.

### B.13.2.3 Workflow diagram

![Workflow for cross-company scenario testing](../_images/diag-72bd2e42a15f039cfb94ff8f3b62a5637dd57aa7.png)

Figure 50. Workflow for cross-company scenario testing

### B.13.2.4 Steps for testing a foreign scenario

Depending on the delivered format you need to follow different steps of conversion.

#### B.13.2.4.1 Overall workflow

1. Acquire the scenario from company B.  
   Depending on the setup used by company B you either get a file in ASAM OpenSCENARIO format or data in some other format.
2. Prepare the delivered scenario to get a compatible file.

   1. In case of a file delivery match the file against your database, see [Section B.13.2.4.2](#_adapting_the_asam_openscenario_file).
   2. In case of data delivery build a concrete scenario, see [Section B.13.2.4.3](#_creating_an_asam_openscenario_file_from_data).
3. Import the newly created ASAM OpenSCENARIO file into your simulation platform.
4. Compare the simulation output with the output from the simulation of company B.
5. Give feedback to company B.  
   Matching results as well as differences can be a valuable outcome for both sides.

#### B.13.2.4.2 Adapting the ASAM OpenSCENARIO file

If company B is able to deliver an ASAM OpenSCENARIO file directly, you just have to match this file against your own database.

1. Access your database.
2. Check all the database-relevant information.
3. Rewrite the ASAM OpenSCENARIO file.

The file is now fully compatible with your simulation environment.

#### B.13.2.4.3 Creating an ASAM OpenSCENARIO file from data

If company B does not deliver an ASAM OpenSCENARIO file you first have to update your local database with the data from company B.

1. Extract the key parameters from the data delivery.
2. Create an abstract scenario.  
   See [abstract scenario](../../conceptual-overview/scenario-abstraction.html#sec-global-terminology-abstract_scenario) for more information about abstract scenarios.
3. Access your own local database.
4. Create a concrete scenario.  
   See [concrete scenario](../../conceptual-overview/scenario-abstraction.html#sec-global-terminology-concrete_scenario) for more information about concrete scenarios.
5. Save this concrete scenario as an ASAM OpenSCENARIO file.

As a result you get an ASAM OpenSCENARIO file that is compatible with your local simulation platform.

You now can run and test the scenario that company B uses.

### B.13.2.5 Related topics

* Definition of an [abstract scenario](../../conceptual-overview/scenario-abstraction.html#sec-global-terminology-abstract_scenario).
* Definition of a [concrete scenario](../../conceptual-overview/scenario-abstraction.html#sec-global-terminology-concrete_scenario).

## B.13.3 Creating platform independent scenarios and tests

### B.13.3.1 Workflow short description

As a test engineer, I can define scenarios and run tests as close as possible to each other regardless of the execution platforms.

### B.13.3.2 Workflow detailed description

Simulation and test environments are offered from vendors and run on different hardware platforms.
The creation of scenarios that are platform independent is key for a successful and reliable scenario exchange.

### B.13.3.3 Workflow diagram

![Creating platform independent scenarios](../_images/diag-e4e34f7557d51eed249784eae1f61aefb96ffc6e.png)

Figure 51. Creating platform independent scenarios

### B.13.3.4 Steps for creating platform independent scenarios

Creating scenarios and tests that can be used on different platforms is straight forward.
Follow these instructions:

1. Get all the information you need to describe the target scenario.
2. Set the needed parameters for the scenario.  
   This can be, for example, a velocity, a distance or any other parameter or set of parameters valid within the domain.
3. Construct an abstract scenario with the desired behavior.  
   The desired behavior was determined in step 1.  
   For a definition of an abstract scenario see the [abstract scenario](../../conceptual-overview/scenario-abstraction.html#sec-global-terminology-abstract_scenario) definition.
4. Connect to the database.  
   See [[TODO]](#TODO) for more details.
5. Fill in the following information:

   1. Headline
   2. Catalogue lines
6. Generate an ASAM OpenSCENARIO file.  
   Refer to your source platform description on how to do that.
7. On the target execution platform import the previously generated file.

You now have a runnable scenario on your target platform with the same functionality as on your source platform.

### B.13.3.5 Related topics

* Definition of an [abstract scenario](../../conceptual-overview/scenario-abstraction.html#sec-global-terminology-abstract_scenario).
* Connecting to the database [[TODO]](#TODO).

## B.13.4 Tracing back requirements

### B.13.4.1 Workflow short description

As a test engineer/auditor/regulator, I can easily trace test cases, scenarios and results back to the requirements.

### B.13.4.2 Workflow detailed description

During a test campaign, ASAM OpenSCENARIO is just the tool used to describe scenarios and execute them in a simulator.
At the same time, each one of these scenarios are linked to test cases and requirements.

All in all this use case describes how an ASAM OpenSCENARIO user is able to get the results of a test case execution within a simulation and trace it back to the requirements.

### B.13.4.3 Workflow diagram

![Tracing back requirements](../_images/diag-e9b52f6d74683b3f1e81cb14e25d3ca4520e85eb.png)

Figure 52. Tracing back requirements

### B.13.4.4 Steps for tracing back requirements

The person taking these steps is a test engineer that has to link results and requirements after simulator execution.
Requirements, results and a scenario database already exist.

1. Get the requirement and the results database.
2. Get the scenario database.  
   In case it exists, also get the test case database.
3. After getting all the databases there shall be a vendor tool facilitating the task of linking results to test cases, and to requirements.
4. The test engineer shall ensure that each one of the test cases references a requirement.  
   As a result, a requirement for ASAM OpenSCENARIO is that it shall include a placeholder for requirements that can be later on easily searched in a database.

As a result all the requirements, test cases, scenarios and results are linked.

When the results are analyzed, tracing back the original requirements and the originating test cases can be done at any stage of the validation procedure.

## B.13.5 Specifying a driving mission

### B.13.5.1 Workflow short description

As a test engineer, I can use ASAM OpenSCENARIO to enable specification of a driving mission through inclusion of multiple maneuvers in a sequence or in parallel for both DUT and any other traffic agents.

### B.13.5.2 Workflow detailed description

ASAM OpenSCENARIO scenarios may include composition and mixes of multiple actions and scenarios that involved with multiple maneuvers.
This allows creating abstract building block libraries that are agnostic to the execution platform, ODD, automation function, maps and more.
Within the behavioral block of a scenario, the user can trigger or observe other sub-scenarios to be create in parallel or serial ordering.
These sub-scenarios may belong to multiple different actors, and their composition simplifies and reduce maintenance of complex scenario specifications.

### B.13.5.3 Workflow diagram

![Workflow specifying a driving mission](../_images/up_workflow_1328.png)

Figure 53. Specifying a driving mission

### B.13.5.4 Steps for specifying a driving mission

In the example scenario C is created as a parallel composition of scenario A and scenario B.

1. Use ASAM OpenSCENARIO features to determine the actor and actions that are needed in your scenario.  
   A rich set of features is provided to capture maneuvers (ASAM OpenSCENARIO actions) in sequential and parallel execution.
   Constraints can be applied to request how action is executed.
2. Set the coverage goals and needed KPIs.
3. Use ASAM OpenSCENARIO to run the scenarios on different execution platforms.
4. Analyze the KPI and coverage results.

The abstract definition in declarative format makes reading and writing of ASAM OpenSCENARIO code easy.
The use of abstract scenarios ensures
an efficient automated process that meets your driving mission goals.

## B.13.6 Accomplishing driving missions

### B.13.6.1 Workflow short description

As a test engineer, I can use ASAM OpenSCENARIO to accomplish a selected driving mission with an indication of whether the mission has been accomplished, what are the mission KPIs and how they are computed, and whether the unambiguous goals of the mission have been reached.

### B.13.6.2 Workflow detailed description

ASAM OpenSCENARIO scenarios are declarative and formal in nature.
They allow the capturing of the high-level generalized intent using constraints.
Therefore a tool can automatically plan multiple concrete instances of the generic scenario.

Once the scenario is executed, a tool may observe the actual execution.
The tool can then report if the observed behavior meets the high-level intent.
An ASAM OpenSCENARIO engine should be able to report whether the high-level intent was observed or not.

### B.13.6.3 Workflow diagram

![Workflow accomplishing driving missions](../_images/up_workflow_1329.png)

Figure 54. Accomplishing driving missions

### B.13.6.4 Steps for accomplishing driving missions

To accomplish driving missions, follow these steps:

1. Define or obtain abstract scenarios.
2. Set the coverage goals or KPIs.  
   The goals should reflect your concerns and desired scenario space.
   ASAM OpenSCENARIO combines coverage and recording syntax to allow a precise description of the goals.
   You can also include a description of the KPIs that needed to be collected for analysis.
3. Execute the scenario on any desired execution platforms.  
   The coverage and KPI information is collected.
4. Analyze the KPI data.
   The KPI can determine the performance of the SUT.
   Note that ASAM OpenSCENARIO also provides verdict analysis APIs to issue errors and warnings as needed.
5. Review the coverage result to ensure completeness.  
   An ASAM OpenSCENARIO tool can provide clear numeric grades about the achieved goals.
6. Re-run more regression to achieve goals that were not met yet.  
   If a few of the goals are not met, you can layer constraints to steer the automatic generation to get to coverage closure.

With the observed data from this use case you get a clear indication if the driving mission or the scenario intent was achieved or not.

## B.13.7 Converting abstract test descriptions into scenarios

### B.13.7.1 Workflow short description

As a test engineer, I can create ASAM OpenSCENARIO scenarios based on abstract test descriptions, for example textual regulations like NCAP tests, UNECE regulations or a requirement list.

### B.13.7.2 Workflow detailed description

The goal of this workflow is to have a scenario that can be used with any ASAM OpenSCENARIO compatible tool regardless of what kind of test description is given as input.

Test descriptions can be of different kind.
For example, a NCAP test description, UNECE regulations or any other requirements list.

The expected output is always a compatible ASAM OpenSCENARIO file.

### B.13.7.3 Workflow diagram

![Converting abstract test descriptions into scenarios](../_images/diag-8653245b8366df13fa98154155339d3bd4f11c39.png)

Figure 55. Converting abstract test descriptions into scenarios

### B.13.7.4 Steps for converting test descriptions into scenarios

Follow these steps to transform an abstract test description into a scenario that is compatible with ASAM OpenSCENARIO.

1. Analyze the abstract test description that is used as input.
2. Identify missing information that is required to create the test scenario.
3. Add missing information.  
   By the end of this step the test description has to be complete.
4. Convert the test description into an ASAM OpenSCENARIO file.  
   See [[TODO]](#TODO) and [[TODO]](#TODO) for more details.

The abstract test description is now available in an ASAM OpenSCENARIO compatible format.

### B.13.7.5 Related topics

* For more details on how to create ASAM OpenSCENARIO files see [[TODO]](#TODO)

## B.13.8 Reusing scenario elements and definitions

### B.13.8.1 Workflow short description

As a test engineer, I can reuse/combine scenario elements and complete scenario definitions for the creation of new scenarios without the need of copy-paste.

### B.13.8.2 Workflow detailed description

Several parts of a scenario can be reused.
In this context, it is appropriate to avoid copy-paste of the same parts all over several scenarios.

A much better approach is to store and reuse often used portions into libraries.
This approach leads to a cleaner and simpler scenario.
This approach also allows for easy corrections and sharing of parts.

### B.13.8.3 Workflow diagram

![Reuse/combine of scenario elements to avoid copy-paste](../_images/diag-8dc0949adedaedca48305da98eb1130aa2dfb8e1.png)

Figure 56. Reuse/combine of scenario elements to avoid copy-paste

### B.13.8.4 Steps reusing/combining scenario elements

As the need of a new scenario arises and its development starts, a good practice is to include a set of well-known libraries containing widely used and tested scenario elements and definitions.

When a given scenario element needs to be added to the scenario, one can search in the included libraries and reuse scenarios as-is without having to copy-paste it.

If such an element does not exist, the scenario developer has to create it and then he *may* add it to a library for reuse.

The same workflow can be followed for a given scenario definition.

In both cases the newly created scenario does not contain code that was copy-pasted.
This increases the readability and the maintainability of the code.

As a result the new scenario contains smartly reused code instead of copy-pasted parts of already existing code.

## B.13.9 Specifying test aspects

### B.13.9.1 Workflow short description

As a test engineer, I have a clear guideline where to specify test aspects (what is inside an abstract or logical scenario and what is outside of it (for example, in experiments or test case definitions or in a map file).

### B.13.9.2 Workflow detailed description

ASAM OpenSCENARIO as a standard is purposely created as an open and modular standard.
This use case aims to shed some light into the different possibilities that a user has when using the standard so as to combine in-house or out-f-the-recommended tools and processes while still using ASAM OpenSCENARIO.

### B.13.9.3 Workflow diagram

![Specifying test aspects](../_images/diag-2ba6f8f171d30e4fa4ba5a72e6c823847a7680c1.png)

Figure 57. Specifying test aspects

### B.13.9.4 Steps for specifying test aspects

This use case defines a number of items that shall be part of the ASAM OpenSCENARIO documentation as *modularity* is allowed by the standard.

1. ***Test cases***  
   The documentation shall contain explanations and examples on how to define test cases within the scenario files (ready-to-use ALKS test campaign ready to be ingested by any compatible simulator).
   Furthermore it shall contain how to define scenarios and how to use them with externally defined test cases (e.g. how to linking several scenarios to a test case and vice versa).
2. ***Map file***  
   The documentation shall contain explanations and examples on how to use OpenDRIVE file with ASAM OpenSCENARIO but also on how to use other map formats but still keep using ASAM OpenSCENARIO as the scenario definition format. It is important to note that OpenDRIVE remains the preferred format as part of the ASAM OpenX suite.
3. ***Simulation models***  
   The documentation shall contain explanations and guidelines on the usage of models within the standard.  
   It is foreseen that some users would like to specify which model database the simulator should use in the execution of the current scenario while some others may want to use the default set of models, thus not caring as much about which specific model is used to represent the actors that take part in the scenario.  
   Both options shall be made possible by the standard.

ASAM OpenSCENARIO is a modular standard.
While there are preferred ways of using it and recommended ways of executing the scenarios that are defined by using it, some users or tool vendors may choose to deviate from this guidelines.

Because it is important that ASAM OpenSCENARIO is adopted by as many users as possible, it has been purposely defined as an open and modular standard, allowing all these modes of execution and without restricting its usage.

## B.13.10 Converting between abstraction levels

### B.13.10.1 Workflow short description

As a development project lead, I can create scenarios on an abstract level to document the functional behavior for legal reasons.

### B.13.10.2 Workflow detailed description

ASAM OpenSCENARIO allows the capturing of the following references on any platform in a formal mathematical way:

* Needed scenarios
* Expected behavior
* Amount of exercised scenarios

This formal description, including the constraints and the coverage goals, provides a clear specification of the needs. This formal description leaves no space for interpretation.

Once you have captured the requirements and executed regressions, an ASAM OpenSCENARIO tool can transform this accurate format into documentation and reports of both the scenarios and the thoroughness of the execution.

### B.13.10.3 Workflow diagram

![Converting between abstraction levels](../_images/diag-794735a174a8fbb84c75675d5824cdfec6c5fc82.png)

Figure 58. Converting between abstraction levels

### B.13.10.4 Steps for converting between abstraction levels.

1. Capture the requirements in formal ASAM OpenSCENARIO format.  
   This step creates a clear definition of what is needed to be executed and in what circumstances it should be executed.  
   *Constraints* can be used to capture dependencies and mark the boundaries of the scenario space.  
   *Coverage goals* can be used to indicate all the circumstances in which the scenario need to be exercised on.  
   *Checkers* can be used to set the threshold of what is considered an error or a warning.
2. Produce documentation using an ASAM OpenSCENARIO tool.  
   An ASAM OpenSCENARIO tool can read the input format and produce documentation and visualization of the goals.
   Note that this can happen even before any execution or data-monitoring.
3. Execute regressions.  
   The use of abstract scenarios ensures high quality scenarios and a massive amount of created scenarios.
   As a result of the execution you get KPI values and a coverage result.
   Checkers may fire to indicate a suspected bad behavior of the DUT.
4. Create documentation or visualize the regression result.  
   Tools can now process the ASAM OpenSCENARIO definitions and the regression result data.
   The tools can visualize the result data or produce documentation.
   This documentation can be used for analysis, regulation or reporting purposes.

The results of this use case are accurate data-driven reports indicating both the goals and the achieved result in mathematical terms.

## B.13.11 Using real-world data for scenarios

### B.13.11.1 Workflow short description

As a test engineer, I can use recorded real-world data to automatically detect/classify or generate scenarios that describe the recorded situation.

### B.13.11.2 Workflow detailed description

Real world recorded data can be used to further analyze a scenario.
Raw recorded data can also be post-processed an re-played.

If a replay ASAM OpenSCENARIO scenario file already exists, the recorded data can be re-played immediately.
If such a scenario does not exist, it must be created before the recorded data can be re-played.

### B.13.11.3 Workflow diagram

![Using real-world data for scenarios](../_images/diag-575d281e352a6bf435eb1de63d043b5cf86d7aa2.png)

Figure 59. Using real-world data for scenarios

### B.13.11.4 Steps for handling real-world data

Starting with data recorded in a real-world situations, you have different ways to proceed:

* If you want to use the data as ground truths for data visualization, follow [Section B.13.11.4.1](#_using_data_as_ground_truth).
* If you want to have a scenario that models the real-world situation described by the data, follow [Section B.13.11.4.2](#_using_data_for_scenario_generation).

#### B.13.11.4.1 Using data as ground truth

1. If a further examination of the scenario is not needed, you can just use the real-world recorded data for data visualization.
2. You can store this data and use it later to compare scenario outputs with the real-world data.

#### B.13.11.4.2 Using data for scenario generation

You may want to have a scenario that describes a real-world situation.
You can use the real-world data to create such a scenario.

1. Synchronize the data.  
   You need to have all the data available for the following steps.
2. Clean the data.  
   Get rid of disrupted data and invalid values.
3. Extract the information that is useful for the scenario.  
   Useful data can be the ego trajectory, environmental object, road features, …​
4. Store the extracted data in a deliverable format.
5. Classify the data of the scenario.  
   Decide which kind or scenario describes the data best.
   This can be a cut-in, a cut-out, a car-following, a lane change or some other kind of scenario.
6. Do you need an ASAM OpenSCENARIO file?

   1. If yes, continue with the next step.
   2. If no, store the detected scenario in the scenario database.  
      Process finished.
7. If you need an ASAM OpenSCENARIO file, get the abstract template of the scenario type you identified in step 5.
8. Fill in the parameters and other detailed information based on the real-world data.
9. Generate the ASAM OpenSCENARIO file.
10. Start the simulation and compare the simulation output with the ground truths you get when following the steps in [Section B.13.11.4.1](#_using_data_as_ground_truth).

Depending on the processing goal, you now have one of two results: Either you got a visualization of the real-world data that you can use as ground truths.
Or you identified or created a scenario that in a simulation behaves similar to the real-world data.

### B.13.11.5 Related topics

* For a description of available data formats see [[TODO]](#TODO)
* For a description of ASAM OpenSCENARIO files see [[TODO]](#TODO)

## B.13.12 Performing automated scenario execution

### B.13.12.1 Workflow short description

As a test engineer, I can execute different ASAM OpenSCENARIO files in an automated way with my ASAM OpenSCENARIO compliant tool chain.  
No file modifications are needed.

### B.13.12.2 Workflow detailed description

This use case shows the workflow that a test engineer must follow to use ASAM OpenSCENARIO as a part of the execution process of tests within a simulator.
This use case is oriented towards the tools vendors and how they may streamline the workflow of using ASAM OpenSCENARIO as part of their simulation tooling.

### B.13.12.3 Workflow diagram

![Performing automated scenario execution](../_images/diag-eb2d5f8c19a2d94de3be062d547b38b69d4688e3.png)

Figure 60. Performing automated scenario execution

### B.13.12.4 Steps for performing automated scenario execution

This workflow assumes that a database of scenarios exists and that the test engineer has been given some test criteria.

1. Success criteria and KPI definition.
2. Query the ASAM OpenSCENARIO database for a relevant scenario related to that test case.
   An ASAM OpenSCENARIO file (abstract, logical or concrete).
3. The next steps is simulator dependant: if the simulator cannot deal with abstract or logical scenarios, a concretization step is needed.
   As a result you get an ASAM OpenSCENARIO file that the simulator can understand.
4. Simulator execution.  
   The file is imported, executed and the results are linked to the success criteria.
   A simulator may be able to automatically execute a batch of ASAM OpenSCENARIO files, or even test automate a single file by modifying the data models, so this is captured as part of the workflow.

As a result of this use case it is proven that ASAM OpenSCENARIO as a standard offers all the tools and capabilities to be used as a scenario description language that can be linked to success criteria for automated execution of test campaigns.

## B.13.13 Using different tool chains

### B.13.13.1 Workflow short description

As a test engineer, I can execute the same ASAM OpenSCENARIO files on different ASAM OpenSCENARIO compliant tool chains.

### B.13.13.2 Workflow detailed description

ASAM OpenSCENARIO is a high-level language with a standardized syntax and semantic.
This allows multiple vendors and tool developers to create ASAM OpenSCENARIO compliant tools and leverage the same ASAM OpenSCENARIO scenarios on different tool chains.

### B.13.13.3 Workflow diagram

![Workflow using different tool chains](../_images/up_workflow_1382.png)

Figure 61. Using different tool chains

### B.13.13.4 Steps for using different tool chains

1. Create or obtain legal ASAM OpenSCENARIO code.  
   The code can be created from scratch or be taken from a library with reusable code.
2. Run the code on the desired ASAM OpenSCENARIO compliant tool chain.  
   If the tool chain adheres to the ASAM OpenSCENARIO published standard, the scenario should be executable on all platforms.

Note that different platforms may not support specific kinds of action.
For example, a physical platform may not allow non-physical execution or an HMI that is not supported by the platform.
The tool chain is still ASAM OpenSCENARIO compliant in this case.

Running the same scenario on multiple platforms saves a lot of implementation time.
It also improves the communication across teams as the teams share and exchange executable formats.

### B.13.13.5 Related topics

* Please refer to use case [Running tests in different environments](#top-up-workflow-1384) on how to create a qualification layer to notify users if a certain scenario cannot be executed on a specific tool chain.

## B.13.14 Converting abstract to concrete scenarios

### B.13.14.1 Workflow short description

As a test engineer, I can leverage an ASAM OpenSCENARIO engine to convert abstract scenarios into concrete scenarios which can then be tested.

### B.13.14.2 Workflow detailed description

Abstract scenarios include both free dimensions and ranges.
Abstract scenarios also include dependencies between actions and actors.
This allows technology to process and generate multiple legal concrete scenarios.

ASAM OpenSCENARIO allows the capturing of abstract road descriptions.
ASAM OpenSCENARIO also allows technology to identify specific locations that meet for the abstract road location and the scenario needs. This provides a huge productivity boost for covering the entire ODD scenario space.

### B.13.14.3 Workflow diagram

![Workflow converting abstract to concrete scenarios](../_images/up_workflow_1383.png)

Figure 62. Converting abstract to concrete scenarios

### B.13.14.4 Steps for converting abstract to concrete scenarios

Note that a tool can provide a coverage result to indicate that the legal space of the abstract scenario was exercised.

1. Define Abstract scenarios using ASAM OpenSCENARIO.  
   Use ASAM OpenSCENARIO constraints to capture the dependencies of what is a legal or interesting scenario.
   You do not need to assign a specific value for a specific attribute.
   ASAM OpenSCENARIO allows capturing hard constraints but also preferences.
   Note that the location can also be abstract.
   You do not have to specify the location explicitly.
2. Define coverage goals for the specific scenario.  
   This code allows the measuring of the thoroughness of the regression.
3. Run a regression of the scenarios.  
   An ASAM OpenSCENARIO tool takes the legal ranges and the user constraints and produces multiple concrete simulations.
   All concrete executions meet the provided scenario constraints as specified by the user.
4. Review the regression coverage result and steer the ASAM OpenSCENARIO tool as needed.  
   It is possible to further steer the ASAM OpenSCENARIO result to specific unexplored areas.
   This can be done by layering constraints on top of the existing scenarios.

The result of the automatic abstraction is a large amount of legal scenarios that deeply stress and validate the DUT.

## B.13.15 Running tests in different environments

### B.13.15.1 Workflow short description

As a test engineer, I can run the same test case in a MiL, SiL, HiL environment as well as in a real car controlled by driving robots or human drivers, with a real or partially simulated environment.

### B.13.15.2 Workflow detailed description

ASAM OpenSCENARIO allows defining abstract scenarios that are agnostic to the execution platform.
This allows mapping the platform agnostic scenario to MiL, SiL, HiL, proving grounds and so on.  
Note that not all scenarios can be implemented in all platforms.
For example, on SiL you may request a non-physical execution that is possible in a simulated world but cannot
be achieved with physical testing like proving grounds.

ASAM OpenSCENARIO allows creating reusable scenarios.
You can also create a platform specific layer that notifies the user in case the scenario cannot be used on this platform.

Note that the implementation of specific ASAM OpenSCENARIO actions might be different between vendors and platforms and is not part of the ASAM OpenSCENARIO standard.
The ASAM OpenSCENARIO standard provides only the abstract standard definition and the desired execution semantic.

### B.13.15.3 Workflow diagram

![Workflow running tests in different environments](../_images/up_workflow_1384.png)

Figure 63. Running tests in different environments

### B.13.15.4 Steps for running tests in different environments

1. Define the platform-agnostic abstract scenario.  
   To maintain reusability, and as a methodology guideline, avoid adding any platform limitations to this reusable code.
2. Create platform specific scenario extensions.  
   You can create multiple platform specific scenario extensions. These scenarios can be designed for specific platform categories or specific vendors.
   For example, if a specific action is not defined on the platform in use, you can just set a constraint to false.

ASAM OpenSCENARIO also allows external C++ code to be executed. This code qualifies the provided values for the specific platform.

1. Run on the desired platform.  
   The result execution should be adequate for the specific platform.
   Note that the scenario may fail if you miss a specific limitation of the platform in use.
   Once you debugged the failure and identified the limitation, you can update the scenario extension to avoid failures in subsequent regressions.

Applying this use case results in a regression that is tunable for the desired platform.

## B.13.16 Describing test track scenarios

### B.13.16.1 Workflow short description

Test engineers on a test track can define their own specific test track goals as coverage and work to achieve them.  
They can also leverage the same scenario with other platforms.  
In such a way tolerances and deviations between test description and test execution become obvious.

### B.13.16.2 Workflow detailed description

The same ASAM OpenSCENARIO scenarios can be used in all execution platforms including test track.

Typically, SiL regression goals are more thorough than test track goals.
Some requirements may only be verified with physical testing.

ASAM OpenSCENARIO platform agnostic scenarios allow the setting of different goals corresponding to the platform strengths and capabilities.
The scenarios can be generated by either team or adopted from a reusable library.

Test engineers can capture the desired scenario in ASAM OpenSCENARIO formal executable format to be leveraged in other platforms.

The language extension capabilities allow the adjusting of the following settings:

* The ***execution***  
  For example, physical or non-physical execution.
* The ***checking***  
  Some checks can be performed on one platform and not others.
* The ***coverage***  
  Enables to tune to the platform specific goals.

### B.13.16.3 Workflow diagram

![Workflow describing test track scenarios](../_images/up_workflow_1393.png)

Figure 64. Describing test track scenarios

### B.13.16.4 Steps for describing test track scenarios

1. Capture the test track instructions in OCS2.0.  
   ASAM OpenSCENARIO can capture the scenario, the expected KPI and the coverage that the scenario requires.
2. Adjust the scenario to other platforms (optional step).  
   In this step engineers can tune the scenario itself, the checkers or the coverage for specific platform capabilities and needs.
3. Use the scenario in any desired platform.

Note that it is also possible to adopt scenarios that were created for SiL purposes and run these on test tracks.

As a result test engineers leverage their knowledge of the test track.
The gathered knowledge can be used early on for SiL or other platform regressions.

## B.13.17 Measuring the verification progress

### B.13.17.1 Workflow short description

As a test engineer, I can set goals and measure the V&V progress using functional coverage.

### B.13.17.2 Workflow detailed description

ASAM OpenSCENARIO enables automated translation of abstract scenarios into multiple legal concrete scenarios.

The automated concretization process allows a tool to select random values for the missing abstract scenario attributes that are consistent with the rest of the scenario.

To ensure that all the desired scenario goals are achieved, ASAM OpenSCENARIO provides a rich set of functional coverage features to capture the project goals.
This executable forma; plan allows a user to measure the V&V status throughout the verification process and improve the quality of the DUT.

### B.13.17.3 Workflow diagram

![Measuring the verification progress](../_images/diag-4a357b09cc23549a3c7e998b53e580328f987b2b.png)

Figure 65. Measuring the verification progress

### B.13.17.4 Steps for measuring the verification progress

The following steps introduce an end-to-end V&V process with the special focus on the coverage related aspects.

1. Plan goals and outcome +This is typically a team effort to agree on the specific V&V goals, and the specific requirements, scenarios and circumstances that are needed for the V&V process.
   The plan can be written in functional level.
2. Create executable plan  
   ASAM OpenSCENARIO provides coverage features to set the goals of the verification.
   This constitutes an executable plan to measure the progress of the V&V process.
   Note that the plan can be refined overtime.
3. Statically validate the plan  
   Because ASAM OpenSCENARIO allows describing both the abstract scenarios and the desired goals in executable form, technology can statically report unreachable coverage goals, without running any scenarios.
4. Create abstract scenarios  
   ASAM OpenSCENARIO enables a user to write his abstract scenarios in a machine-readable way to enable automated creation of multiple concrete scenarios.
   These scenario should include coverage goals.
   For example, in a cut-in scenario, the user code that the cut-in scenario should be executed on both left and right sides, on multiple speeds and multiple light conditions.
   All of these goals can be captured in ASAM OpenSCENARIO functional coverage.
   ASAM OpenSCENARIO also allows creating library of well-encapsulated modular scenarios.
   Leveraging these building blocks can assist greatly to compose the scenarios needed for the V&V project.
   ASAM OpenSCENARIO provides coverage extensions capabilities that allows refining the generic reusable coverage definitions, to a specific project needs.
5. Develop the DUT automation function and setup the tool-chain  
   These steps are needed for executing the scenarios and achieve the verification task.
6. Run regression on multiple platforms  
   In this step KPI information is evaluated to issue error messages or warning.
   ASAM OpenSCENARIO also allows to record data for further off-line review.
   Note that ASAM OpenSCENARIO support all execution platforms including HiL, SiL, proving grounds and real street driving.
7. Debug failures  
   Different vendors may offer different debug capabilities.
   Note that errors might also be issued from the execution platforms and not necessarily from ASAM OpenSCENARIO code.
8. Fix bug or tune checkers  
   An error message or a warning may be issued from a system malfunction or from a bad checker definition.
   At this points you wish to fix the issue and rerun the regressions.
   This iterative process continues till all errors are resolved.
9. Check the V&V goals status   
   At this point, the user can observe the coverage result.
   This gives a data-driven indication of how much of the scenario goals were reached.
   If some of the planned scenarios were not executed, you may need to rerun the regressions and steer the ASAM OpenSCENARIO tool to focus on these missed areas of concern.
   If you finished the plan without any error, you are done with your V&V project.

### B.13.17.5 Code sample for setting goals

The following code demonstrates the standard way for setting functional coverage goals.

Code 93. Setting functional coverage goals

```
extend cut_in_and_slow:
    cover(side)
    cover(car_kind)
```

Note that you may have different goals for different execution platforms.
As a methodology, it is desired to place the coverage definitions in a file extensions and to select the right extension for proper platforms.