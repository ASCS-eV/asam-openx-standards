# ASAM Openscenario Dsl v2.2.0 — B.6 Workflows for development project leaders

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_dev_project_lead.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.6 Workflows for development project leaders

Project leaders may find the following workflows useful.

## B.6.1 Workflow list

* [Section B.6.2](#sec-up-workflow-1344)  
  As a development project lead, I can create scenarios on an abstract level to document the functional behavior for legal reasons.

## B.6.2 Creating abstract scenarios for documentation purposes

### B.6.2.1 Workflow short description

As a development project lead, I can create scenarios on an abstract level to document the functional behavior for legal reasons.

### B.6.2.2 Workflow detailed description

Functional behaviors are very often required to be tracked for legal reasons.

After aggregating all the necessary information, you must check if some scenarios that cover your needs already exist.
Then you can reuse existing scenarios and create new ones as needed.

Given a functional behavior, check if some legal regulation already exists that covers this behavior.  
If such a legal regulation exists, check if your functional behavior behaves according to the regulation or not.

In the simplest case, you just need to create a new functional behavior and document the missing corresponding legal regulation.
In the more complicated case, a deeper analysis is needed.

### B.6.2.3 Workflow diagram

![Creating abstract scenarios for documentation purposes](../_images/diag-4738db2b73996f7364d32cb12f1ee3252a2406cf.png)

Figure 40. Creating abstract scenarios for documentation purposes

### B.6.2.4 Steps for creating abstract scenarios for documentation purposes

1. Given a new or existing functional behavior that you want to check against legal regulation, the first step is to aggregate all the information about it.
2. Check if there are already scenarios covering it or not.

   1. If scenarios exist, start from them and adapt them as needed.
   2. If scenarios do not exist, create a new scenario.
3. With one or more scenarios defined that cover your functional behavior, check if some legal regulations already exist for that specific behavior.

   1. If legal regulations exist, continue with step 4.
   2. If no legal regulations exist, continue with step 5.
4. If there are legal regulations covering the behavior, check for their actual applicability.

   1. If the regulation is applicable, focus on the applicable legal regulations.

      1. If you are dealing with a *new* functional behavior, be sure to write it respecting the legal regulations that apply.
      2. If you are dealing with an *already existing* functional behavior, be sure to modify it respecting the legal regulations that apply.
   2. If the regulation is not applicable, document all the non-applicabilities.
   3. At the end of the process, save the functional behavior to a scenario.
   4. Workflow finished.
5. If there are no legal regulations covering the behavior, proceed with the following steps:

   1. Define the new behavior.
   2. Save it to a scenario.
   3. Document that no legal regulation covers the scenario.
   4. Workflow finished.

As a result you get a scenario containing functional behaviors with one of the following possibilities:

* The functional behaviors are compliant with the legal regulations.
* The functional behaviors do not have applicable legal regulations and this is documented.
* The functional behaviors do not have existing legal regulations and this is documented.