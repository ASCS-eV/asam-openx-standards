# ASAM OpenDRIVE® XML Schema — V1.9.0

Normative XSD schema files of ASAM OpenDRIVE® V1.9.0, matching the specification
text in the parent directory. These are the machine-readable source of truth for
every OpenDRIVE enumeration (`e_roadType`, `e_laneType`, `e_objectType`, …) used by
downstream consumers.

**These files are not original works of this project.** Copyright © ASAM e.V., 2026.
Redistributed under the ASAM Unrestricted Distribution Clause; see the repository
[LICENSE](../../../LICENSE) and the notice in each file's XML header:

> *"Any use is limited to the scope described in the ASAM license terms. This file is
> distributable in accordance with the ASAM license terms."*

## Provenance

| Field | Value |
|---|---|
| Standard | ASAM OpenDRIVE® |
| Version | **V1.9.0** (schema files dated 2026-04-29) |
| Deliverable | `ASAM_OpenDRIVE_v1-9-0_xsd_schema_files.zip` |
| Source | <https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/> |
| Retrieved | 2026-07-28 |
| Target namespace | `http://code.asam.net/simulation/standard/opendrive_schema` |

### File checksums (SHA-256, truncated)

| File | SHA-256 |
|---|---|
| `OpenDRIVE_Core.xsd` | `d32cd06133d3c261…` |
| `OpenDRIVE_Junction.xsd` | `fb2aca2bcc980948…` |
| `OpenDRIVE_Lane.xsd` | `9d364b8b409ae851…` |
| `OpenDRIVE_Object.xsd` | `953eda8aaa9483fa…` |
| `OpenDRIVE_Railroad.xsd` | `3aa472aeb5a4d090…` |
| `OpenDRIVE_Road.xsd` | `138064212a66dc9a…` |
| `OpenDRIVE_Signal.xsd` | `d3689f3460a88918…` |

## Updating

1. Download the `*_xsd_schema_files.zip` deliverable from the source URL above.
2. Replace the files in this directory and update the version, date and checksums here.
3. Downstream consumers that pin enumerations against these files will fail until their
   constraints are re-derived — that is intentional. In `ontology-management-base`, run
   `just validate-enums`.
