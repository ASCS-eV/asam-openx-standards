# ASAM OpenSCENARIO® DSL v2.2.0 — B.15 Workflows for tool providers or consumers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_tool_providers-consumers.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.15 Workflows for tool providers or consumers

Tool providers and tool consumers should have a look at the following workflows.

## B.15.1 Workflow list

* [Section B.15.2](#sec-up-workflow-1334)  
  As a provider or consumer of an existing tool, I can migrate information from previous versions of ASAM OpenSCENARIO into ASAM OpenSCENARIO.
* [Section B.15.3](#sec-up-workflow-1391)  
  A simulation tool can describe randomly executed simulation runs.  
  If you want to have a concrete description of what has happened in the scenario, run the simulation with stochastic metrics. The simulation tool presents the description in ASAM OpenSCENARIO format.

## B.15.2 Migrating from ASAM OpenSCENARIO XML 1.3.1 to ASAM OpenSCENARIO

### B.15.2.1 Workflow short description

As a provider or consumer of an existing tool, I can migrate information from previous versions of ASAM OpenSCENARIO into ASAM OpenSCENARIO.

### B.15.2.2 Workflow detailed description

A tool provider or a consumer wants to migrate information from a previous version of ASAM OpenSCENARIO to this version of ASAM OpenSCENARIO.

ASAM OpenSCENARIO shall allow him to do so.

### B.15.2.3 Workflow diagram

![Migrating from {THIS_STANDARD}{nbsp}{VER_XML_LATEST} to {THIS_STANDARD}](../_images/diag-2ccac40fa2285bc2984db41eb7cd8f982788193f.png)

Figure 68. Migrating from ASAM OpenSCENARIO XML 1.3.1 to ASAM OpenSCENARIO

### B.15.2.4 Steps for migrating from ASAM OpenSCENARIO XML 1.3.1 to ASAM OpenSCENARIO

ASAM OpenSCENARIO must enable a tool provider or a user to migrate his legacy information to the newest release.

1. Get the legacy information.  
   Starting data is *legacy* information.
2. Compare data against the ASAM OpenSCENARIO rules.
3. Adapt the information according to the new rules until no conflicts are found.  
   All data is now *updated* information.
4. Do a final review of the updated information.  
   All data is now *revised* updated information.  
   All the information is updated to ASAM OpenSCENARIO

At the end of the process the tool provider or the consumer migrated legacy ASAM OpenSCENARIO information to ASAM OpenSCENARIO.

## B.15.3 Executing simulations randomly

### B.15.3.1 Workflow short description

A simulation tool can describe randomly executed simulation runs.  
If you want to have a concrete description of what has happened in the scenario, run the simulation with stochastic metrics. The simulation tool presents the description in ASAM OpenSCENARIO format.

### B.15.3.2 Workflow detailed description

ASAM OpenSCENARIO allows the definition of *abstract random* scenarios and *concrete fully specified* scenarios.

With the *random scenario* a tool may automatically produce multiple known and unknown scenarios.
Some of these scenarios are of great importance and some are less interesting.

The *functional coverage* features of ASAM OpenSCENARIO allow a precise description of the goals and a measuring if all execution goals were met.

Note that both random and concrete values are represented in the functional coverage.
Functional coverage delivers a combined picture of what was exercised.

### B.15.3.3 Workflow diagram

![Workflow executing simulations randomly](../_images/up_workflow_1391.png)

Figure 69. Executing simulations randomly

### B.15.3.4 Steps for executing simulations randomly

Both the abstract scenario and the coverage goals are processed by the ASAM OpenSCENARIO tool chain.
The tool chain then produces a report representing the completeness of the regression compared to the goals.

1. Define the functional and non-functional requirements.  
   It is a good idea to do this definition in collaboration with multiple stakeholders.
2. Code the abstract scenarios using ASAM OpenSCENARIO.  
   The abstract scenario might be created from scratched or reused from a reusable library.
   Note that abstract scenarios allows capturing dependencies between attributes and behaviors using constraints.
3. Code the coverage goals using ASAM OpenSCENARIO.  
   The functional coverage features of ASAM OpenSCENARIO allows describing the legal desired scenario space in measurable terms.
4. Run the regression.  
   Use your favorite tool chain and scripts and run a regression.
5. Observe the coverage results.  
   Load the regression result into your ASAM OpenSCENARIO tool and observe the results.
   The results indicate which scenarios and attributes were exercised and which scenarios were not performed.
6. Add constraints or run more scenarios to ensure a thorough V&V process.  
   To hit unexplored goals, repeat until the tool achieves convergence.

This use cases delivers the following outcome:

* A combination of random and unexpected scenarios to hit the unknowns.
* The executable proof that the V&V goals were accomplished.