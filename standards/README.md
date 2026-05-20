# Reference Specifications

This directory contains downloaded copies of external ASAM OpenX and ISO specifications for offline reference and AI agent access.

## ⚠️ Important Notice

**These files are NOT original works of this project.**

They are copies of specifications published by their respective standards organizations. The original terms, conditions, and licenses of each specification apply.

All ASAM OpenX standards included here are distributed under ASAM's unrestricted license:
> "The licensor grants everyone a basic, non-exclusive and unlimited license to use the standard."

## Directory Structure

```
docs/specs/references/
├── README.md                          # This file
├── asam-openodd/                      # ASAM OpenODD® v1.0.0 (2025-04-03)
├── asam-openlabel/                    # ASAM OpenLABEL v1.0.0
├── asam-opendrive/                    # ASAM OpenDRIVE® v1.9.0 (2026-05-08)
├── asam-openscenario-dsl/             # ASAM OpenSCENARIO® DSL v2.2.0 (2026-03-19)
├── asam-osi/                          # ASAM OSI (Open Simulation Interface)
├── asam-opencrg/                      # ASAM OpenCRG v1.2
├── asam-openmaterial-3d/              # ASAM OpenMATERIAL® 3D
├── asam-traffic-participants/         # ASAM TrafficParticipants v1.0.2
└── iso-345xx/                         # ISO 34501/34503/34504 summaries (copyright)
```

## Standards Index

| Directory | Standard | Version | Organization | License | Source URL |
|-----------|----------|---------|--------------|---------|-----------|
| `asam-openodd/` | ASAM OpenODD® | v1.0.0 (2025-04-03) | ASAM e.V. | Unrestricted | [Spec](https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/index.html) |
| `asam-openlabel/` | ASAM OpenLABEL | v1.0.0 | ASAM e.V. | Unrestricted | [Spec](https://www.asam.net/standards/detail/openlabel/) |
| `asam-opendrive/` | ASAM OpenDRIVE® | v1.9.0 (2026-05-08) | ASAM e.V. | Unrestricted | [Spec](https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/index.html) |
| `asam-openscenario-dsl/` | ASAM OpenSCENARIO® DSL | v2.2.0 (2026-03-19) | ASAM e.V. | Unrestricted | [Spec](https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/index.html) |
| `asam-osi/` | ASAM OSI | v3.7+ | ASAM e.V. | MPL-2.0 | [GitHub](https://github.com/OpenSimulationInterface/open-simulation-interface) |
| `asam-opencrg/` | ASAM OpenCRG | v1.2 | ASAM e.V. | Apache-2.0 | [GitHub](https://github.com/asam-ev/OpenCRG) |
| `asam-openmaterial-3d/` | ASAM OpenMATERIAL® 3D | BS 1.0.0 (2025-04-03) | ASAM e.V. | Unrestricted | [Spec](https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/index.html) |
| `asam-traffic-participants/` | ASAM TrafficParticipants | v1.0.2 | ASAM e.V. | Unrestricted | [Spec](https://publications.pages.asam.net/standards/ASAM_trafficparticipants/ASAM_TrafficParticipants_Specification/v1.0.2/specification/index.html) |
| `iso-345xx/` | ISO 34501/34503/34504 | 2022-2023 | ISO | Copyright (summary only) | [ISO](https://www.iso.org/standard/78952.html) |

## Download Date

- **ASAM OpenODD®**: 2026-05-19
- **ASAM OpenLABEL**: 2026-05-19
- **ASAM OpenDRIVE®**: 2026-05-19
- **ASAM OpenSCENARIO® DSL**: 2026-05-19
- **ASAM OSI**: 2026-05-19
- **ASAM OpenCRG**: 2026-05-19
- **ASAM OpenMATERIAL® 3D**: 2026-05-19
- **ASAM TrafficParticipants**: 2026-05-19

## Usage

These files are provided for:

1. **AI agent context** — Allow AI assistants to implement against authoritative specifications with precise section-level citations
2. **Offline reference** — Access specs without internet connectivity
3. **Version pinning** — Ensure consistent spec versions during development
4. **LinkML cross-references** — Schemas reference these via `[OpenODD] §6.4.3` notation

## Referencing Convention (for LinkML schemas)

```yaml
# In schema header:
# ============================================================================
# SPECIFICATION REFERENCES
# ============================================================================
# [OpenODD]     ASAM OpenODD® v1.0.0
#               https://publications.pages.asam.net/standards/ASAM_OpenODD/...
#               Local: docs/specs/references/asam-openodd/
# [OpenLABEL]   ASAM OpenLABEL v1.0.0
#               Local: docs/specs/references/asam-openlabel/
# [ISO-34503]   ISO 34503:2023
#               Local: docs/specs/references/iso-345xx/iso-34503-summary.md

# In slots/classes:
slots:
  WeatherRain:
    comments:
      - "[ISO-34503] Clause 10.2.1; [OpenODD] Annex B row 'rainfall_type'"
```

## Updates

To refresh a spec after a new version release:

1. Re-download the relevant chapters from the source URL
2. Update the version and download date in this README
3. Update any LinkML schema references that cite changed section numbers

## Relationship to ENVITED-X Domains

| ASAM Standard | ENVITED-X Domain(s) | Relationship |
|---------------|---------------------|--------------|
| OpenODD | openlabel-v2 | Shared ISO 34503 taxonomy; OpenODD adds logic rules |
| OpenLABEL | openlabel, openlabel-v2 | Direct source standard |
| OpenDRIVE | hdmap | HD map format definition |
| OpenSCENARIO DSL | scenario | Scenario description language |
| OSI | ositrace | Sensor data interface format |
| OpenCRG | surface-model | Road surface profile format |
| OpenMATERIAL 3D | environment-model | Material properties for sensors |
| TrafficParticipants | scenario, openlabel-v2 | Road user type classifications |

## Authoritative Sources

Always refer to the original sources for the most up-to-date and legally binding versions:

- **ASAM OpenODD®**: https://www.asam.net/standards/detail/openodd/
- **ASAM OpenLABEL**: https://www.asam.net/standards/detail/openlabel/
- **ASAM OpenDRIVE®**: https://www.asam.net/standards/detail/opendrive/
- **ASAM OpenSCENARIO® DSL**: https://www.asam.net/standards/detail/openscenario-dsl/
- **ASAM OSI**: https://www.asam.net/standards/detail/osi/
- **ASAM OpenCRG**: https://www.asam.net/standards/detail/opencrg/
- **ASAM OpenMATERIAL® 3D**: https://www.asam.net/standards/detail/openmaterial-3d/
- **ASAM TrafficParticipants**: https://www.asam.net/standards/detail/trafficparticipants/
- **ISO 34503**: https://www.iso.org/standard/78952.html
- **ISO 34504**: https://www.iso.org/standard/78953.html
- **ISO 34501**: https://www.iso.org/standard/78951.html

## Disclaimer

These copies are provided "as is" for convenience. The ENVITED-X project makes no warranties about the accuracy or completeness of these copies. For authoritative interpretations, consult the original specifications and their issuing organizations.
