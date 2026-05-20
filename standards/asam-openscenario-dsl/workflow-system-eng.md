# ASAM OpenSCENARIO® DSL v2.2.0 — B.12 Workflows for system engineers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_system_eng.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.12 Workflows for system engineers

The following workflows concentrate on typical jobs for system engineers.

## B.12.1 Workflow list

* [Section B.12.2](#sec-up-workflow-1327)  
  As a system engineer working for an AV/ADAS developer company, I can fully trace which hardware and software in the AV/ADAS stack is verified by which tests.

## B.12.2 Tracing back verification

### B.12.2.1 Workflow short description

As a system engineer working for an AV/ADAS developer company, I can fully trace which hardware and software in the AV/ADAS stack is verified by which tests.

### B.12.2.2 Workflow detailed description

ASAM OpenSCENARIO is agnostic to the execution platform including the used hardware and software.
This means that an abstract scenario should not be hardcoded for a specific implementation nature or version.

At the same time, an ASAM OpenSCENARIO tool chain allows the tracing between the execution log result and the abstract executed scenario.
The actions level of abstraction can be determined by the user.

### B.12.2.3 Workflow diagram

![Workflow tracing back verification](../_images/up_workflow_1327.png)

Figure 49. Tracing back verification

### B.12.2.4 Steps for tracing back verification

1. Choose the level of abstraction of your scenario  
   The scenario can be composed of low-level or high-level actions.
   Typically scenarios are high-level vehicle level use-cases, but it is up to the user to create a more refined scenario.
2. Create coverage attributes to identify which hardware or software system is executed in each scenario.
   Note that each scenario exercises multiple hardware and software units.
   You can set goals for each unit capturing the depth.
3. Execute the scenarios and observe the coverage data.
4. Review the coverage result to understand if the goals for the HW and SW components are met.

The result of running this use case is a clear understanding of which hardware and software components were executed, in which challenges they ran and how well they did.