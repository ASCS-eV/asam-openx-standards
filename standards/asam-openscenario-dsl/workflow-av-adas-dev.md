# ASAM OpenSCENARIO® DSL v2.2.0 — B.4 Workflows for AV/ADAS developer companies

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_av-adas_dev.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.4 Workflows for AV/ADAS developer companies

If you are working for an AV/ADAS developer company the following workflows might be of interest for you.

## B.4.1 Workflow list

* [Section B.4.2](#sec-up-workflow-1311)  
  As an AV/ADAS developer company, I can share with other companies the scenarios I built to test my technology.
* [Section B.4.3](#sec-up-workflow-1316)  
  As an AV/ADAS developer company, I can share with auditors and regulators the scenarios I have applied for safety assurance of my technology.

## B.4.2 Sharing scenarios with other companies

### B.4.2.1 Workflow short description

As an AV/ADAS developer company, I can share with other companies the scenarios I built to test my technology.

### B.4.2.2 Workflow detailed description

Every company defines scenarios using their own technology.
A scenario chosen for sharing shall be checked for ASAM OpenSCENARIO compliancy.
If the scenario is non-compliant, it shall be adapted and checked again in an iterative way.

When the scenario is finally ASAM OpenSCENARIO compliant, it can be saved into a repository.
Access to this repository can be granted to partner companies.
Other parties accessing this scenario are sure that they can reuse it without having to make any changes to it.

### B.4.2.3 Workflow diagram

![Sharing scenarios with other companies](../_images/diag-f2266bfa14ed40577763cd4369e4b683da31463a.png)

Figure 34. Sharing scenarios with other companies

### B.4.2.4 Steps for sharing scenarios

As stated before, the process of providing a compliant ASAM OpenSCENARIO scenario is iterative.

You should start with an already well formed file and review it against the ASAM OpenSCENARIO compliancy guidelines, then correct it and refine it, possibly several times, until compliant.
When the scenario is finally compliant, it can be saved on a repository and shared with other companies.

1. Start with a well formed ASAM OpenSCENARIO scenario.  
   This is the initial scenario. It is most probably not compliant.
2. Review and correct the scenario according to the compliancy rules.  
   You get a reviewed scenario, which is still most probably not compliant.
3. Perform other reviews and corrections according to the compliancy rules.  
   You get a reviewed scenario, which is possibly still not compliant.
4. …​  
   Reviewed scenario.
5. Perform a final review ensuring full compliancy.  
   You get a fully compliant scenario ready to be shared.
6. Save the scenario in a repository.
7. Share the scenario with other companies.

At the end of the process you have a fully compliant ASAM OpenSCENARIO scenario that can be safely shared with other companies, being sure that it can be run without any modification needed, leading to the same results.

## B.4.3 Sharing scenarios with auditors and regulators

### B.4.3.1 Workflow short description

As an AV/ADAS developer company, I can share with auditors and regulators the scenarios I have applied for safety assurance of my technology.

### B.4.3.2 Workflow detailed description

Every company can share their scenarios in a private or publicly accessible repository.
Auditors (and regulators) entities shall have access to this repository for validation.

Auditors and regulators can use the repositories in several ways.

* Browse the repository and select the scenario they are interested in.
* Execute the scenario on their own.
* Compare the results they have obtained against the results provided by the scenario owner.  
  If the results are in line, the auditor (or the regulator) validates the scenario.  
  If the results are not in line, the auditor (or the regulator) shall give feedback to the scenario owner to find out what is the problem.

### B.4.3.3 Workflow diagram

![Scenario sharing with auditors and regulators](../_images/diag-fe8db6a0a4959b6283eec7459a961da24a6b1271.png)

Figure 35. Scenario sharing with auditors and regulators

### B.4.3.4 Steps for sharing scenarios

After having gotten access to the repository of interest and browsed it to find a scenario that is relevant for his work, an auditor (or a regulator) shall run it to ensure that the results he has correspond to the results the scenario creator had.
If this is not the case, the auditor (or the regulator) shall contact the scenario owner to understand why the same scenario is leading to different results.
The auditor (or the regulator) shall not validate the scenario until this clarification has been done.

1. Locate the ASAM OpenSCENARIO scenario coming from an industry repository.  
   You found your initial scenario.
2. Auditor (or regulator) runs the scenario locally to get results.  
   Local results are created.
3. Auditor (or regulator) compares local results with scenario owner’s results.  
   Results comparison is available.

   1. If the results match, the auditor (or the regulator) can validate the scenario.
   2. If the results do not match, the auditor (or the regulator) shall contact the scenario owner before validating it.

At the end of the process the auditor (or the regulator) has a fully compliant and validated ASAM OpenSCENARIO.