# ASAM Openscenario Dsl v2.2.0 — B.14 Workflows for tool developers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/workflows/workflow_tool_devs.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.14 Workflows for tool developers

The following information is especially useful for tool developers.

## B.14.1 Workflow list

* [Section B.14.2](#sec-up-workflow-1331)  
  As a tool developer, I can reuse constructs, artifacts and libraries to create tools compatible with other tool vendors in industry.
* [Section B.14.3](#sec-up-workflow-1334)  
  As a provider or consumer of an existing tool, I can migrate information from previous versions of ASAM OpenSCENARIO into ASAM OpenSCENARIO.

## B.14.2 Re-using constructs, artifacts and libraries

### B.14.2.1 Workflow short description

As a tool developer, I can reuse constructs, artifacts and libraries to create tools compatible with other tool vendors in industry.

### B.14.2.2 Workflow detailed description

ASAM OpenSCENARIO allows to reuse constructs, artifacts and libraries.
If the construct (or artifact, or library) already exists, it can be reused as-is.
If the construct (or artifact, or library) does not exist yet, it can be created.
After the creation, the construct (or artifact, or library) shall be *privately* reviewed until the required level of quality is reached.
After that, the construct (or artifact, or library) shall be *publicly* reviewed until the required level of quality is reached.
After that, the construct (or artifact, or library) is ready for reuse.

### B.14.2.3 Workflow diagram

![Re-using constructs, artifacts and libraries](../_images/diag-d200fb0997c1416320aa424000d546fe00c16071.png)

Figure 66. Re-using constructs, artifacts and libraries

### B.14.2.4 Steps for re-using constructs, artifacts and libraries

A new construct (or artifact, or library) shall be privately and publicly reviewed in an iterative way before being declared ready for reuse.

1. New construct (or artifact, or library)  
   Initial implementation (most likely to be refined)
2. Private review  
   Privately revised implementation (most likely to be refined more)
3. Public review  
   Publicly reviews implementation (finalized)
4. New construct (or artifact, or library) ready for reuse

At the end of the process the auditor (or the regulator) has a fully compliant and validated ASAM OpenSCENARIO.

## B.14.3 Migrating from ASAM OpenSCENARIO XML 1.3.1 to ASAM OpenSCENARIO

### B.14.3.1 Workflow short description

As a provider or consumer of an existing tool, I can migrate information from previous versions of ASAM OpenSCENARIO into ASAM OpenSCENARIO.

### B.14.3.2 Workflow detailed description

A tool provider or a consumer wants to migrate information from a previous version of ASAM OpenSCENARIO to this version of ASAM OpenSCENARIO.

ASAM OpenSCENARIO shall allow him to do so.

### B.14.3.3 Workflow diagram

![Migrating from {THIS_STANDARD}{nbsp}{VER_XML_LATEST} to {THIS_STANDARD}](../_images/diag-2ccac40fa2285bc2984db41eb7cd8f982788193f.png)

Figure 67. Migrating from ASAM OpenSCENARIO XML 1.3.1 to ASAM OpenSCENARIO

### B.14.3.4 Steps for migrating from ASAM OpenSCENARIO XML 1.3.1 to ASAM OpenSCENARIO

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