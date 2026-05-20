# ASAM OpenSCENARIO® DSL v2.2.0 — B.3 Workflows for auditors/regulators

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_auditors-regulators.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.3 Workflows for auditors/regulators

If you are an auditor or regulator you might be interested in the following workflows.

## B.3.1 Workflow list

* [Section B.3.2](#sec-up-workflow-1321)  
  As an auditor/regulator, I can understand how AV/ADAS developers are testing their products.
* [Section B.3.3](#sec-up-workflow-1323)  
  As a safety consultant, I can recommend specific scenarios and related conditions (parameters) to my clients to test their products.
* [Section B.3.4](#sec-up-workflow-1324)  
  As a government agency, I can understand what parts of the Operational Domain are verified by an AV/ADAS developer through each scenario.
* [Section B.3.5](#sec-up-workflow-1325)  
  As a regulator/technical service, I can specify, in an unambiguous way, the test scenarios required to demonstrate compliance with a particular regulation.
* [Section B.3.6](#sec-up-workflow-1326)  
  As a test engineer/auditor/regulator, I can easily trace test cases, scenarios and results back to the requirements.

## B.3.2 Understanding product testing

### B.3.2.1 Workflow short description

As an auditor/regulator, I can understand how AV/ADAS developers are testing their products.

### B.3.2.2 Workflow detailed description

This workflow has no detailed description.

### B.3.2.3 Workflow diagram

![Understanding product testing](../_images/diag-bdebf5fc44ad868ca6e0406ec2a3ee851b6bae49.png)

Figure 29. Understanding product testing

## B.3.3 Recommending scenarios and parameters

### B.3.3.1 Workflow short description

As a safety consultant, I can recommend specific scenarios and related conditions (parameters) to my clients to test their products.

### B.3.3.2 Workflow detailed description

This workflow has no detailed description.

### B.3.3.3 Workflow diagram

![Recommending scenarios and parameter](../_images/diag-0288feda46e38a4bfe3e7bb361a4ef0d876cf49b.png)

Figure 30. Recommending scenarios and parameter

## B.3.4 Understanding verification coverage

### B.3.4.1 Workflow short description

As a government agency, I can understand what parts of the Operational Domain are verified by an AV/ADAS developer through each scenario.

### B.3.4.2 Workflow detailed description

This workflow has no detailed description.

### B.3.4.3 Workflow diagram

![Understanding AV/ADAS developer scenarios](../_images/diag-d88e3629e3d324375929ab7fcf38457de08014c6.png)

Figure 31. Understanding AV/ADAS developer scenarios

## B.3.5 Specifying regulation scenarios

### B.3.5.1 Workflow short description

As a regulator/technical service, I can specify, in an unambiguous way, the test scenarios required to demonstrate compliance with a particular regulation.

### B.3.5.2 Workflow detailed description

An increasing number of regulation organizations need to provide scenarios for automated or assisted driving functions.

At some point those scenarios must be executed by a piece of software, but often, they are initially written in a human-readable, but not machine-readable way.

As a consequence a regulator or someone who needs to perform the test must interpret and formalize the scenario description first, so that a machine can execute it.
This means it must be possible to express the scenarios in a machine-readable, standardized and unambiguous manner.

This use case describes what is needed to turn a formal, but not machine-readable regulation scenario into something that can be executed by software in simulation or on a test track.

### B.3.5.3 Workflow diagram

![Specifying regulation scenarios](../_images/diag-189deafe3bf9a393dfe2124b03dfbe3bf49f8152.png)

Figure 32. Specifying regulation scenarios

### B.3.5.4 Steps for specifying regulation scenarios

The following steps are needed:

1. Analyze the setup and content of the regulation.
2. Define what the product must be able to do.
3. Turn the inputs from the first two steps into a scenario definition.
4. Define the parameters of the scenario so that there are no ambiguities left.
5. Execute the scenario.
6. Check the result.  
   If the test was passed the system is compliant with the regulation.

This use case was added to ensure that ASAM OpenSCENARIO can be used as a basis for defining executable scenarios based on regulation requirements.

## B.3.6 Tracing back requirements

### B.3.6.1 Workflow short description

As a test engineer/auditor/regulator, I can easily trace test cases, scenarios and results back to the requirements.

### B.3.6.2 Workflow detailed description

During a test campaign, ASAM OpenSCENARIO is just the tool used to describe scenarios and execute them in a simulator.
At the same time, each one of these scenarios are linked to test cases and requirements.

All in all this use case describes how an ASAM OpenSCENARIO user is able to get the results of a test case execution within a simulation and trace it back to the requirements.

### B.3.6.3 Workflow diagram

![Tracing back requirements](../_images/diag-e9b52f6d74683b3f1e81cb14e25d3ca4520e85eb.png)

Figure 33. Tracing back requirements

### B.3.6.4 Steps for tracing back requirements

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