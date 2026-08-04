# ASAM OpenX® Standards Reference Library

[![License: ASAM Unrestricted](https://img.shields.io/badge/License-ASAM%20Unrestricted-blue.svg)](https://www.asam.net/license)

Machine-readable, version-pinned copies of ASAM OpenX® simulation standards
for use as reference material in ontology development and AI-assisted workflows.

## Legal Basis

All standards are redistributed under the **ASAM Unrestricted Distribution Clause**:

> *"The licensor grants everyone a basic, non-exclusive and unlimited license
> to use the standard ASAM [StandardName]."*

See [LICENSE](LICENSE) for full details. Copyright remains with ASAM e.V.

## Standards Included

| Directory | Standard | Version | Format | Source |
|-----------|----------|---------|--------|--------|
| `standards/asam-opendrive/` | ASAM OpenDRIVE® | v1.9.0 (2026-05-08) | Markdown (from HTML) + **XSD schema** + **UML model** | [Spec](https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/) |
| `standards/asam-openscenario-xml/` | ASAM OpenSCENARIO® XML | v1.4.0 (2026-06-02) | **XSD schema** + **UML model** | [Spec](https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_XML/latest/) |
| `standards/asam-openscenario-dsl/` | ASAM OpenSCENARIO® DSL | v2.2.0 (2026-03-19) | Markdown (from HTML) | [Spec](https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/) |
| `standards/asam-openodd/` | ASAM OpenODD® | v1.0.0 (2025-04-03) | Markdown (from HTML) | [Spec](https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/) |
| `standards/asam-openlabel/` | ASAM OpenLABEL® | v1.0.0 | Markdown + JSON Schema | [Schema](https://openlabel.asam.net/V1-0-0/schema/openlabel_json_schema.json) |
| `standards/asam-openmaterial-3d/` | ASAM OpenMATERIAL® 3D | BS 1.0.0 (2025-04-03) | Markdown (from HTML) | [Spec](https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/) |
| `standards/asam-opencrg/` | ASAM OpenCRG® | v1.2 | Overview + submodule | [GitHub](https://github.com/ASAM-ev/OpenCRG) |
| `standards/asam-osi/` | ASAM OSI® | v3.7+ | Overview + submodule | [GitHub](https://github.com/OpenSimulationInterface/open-simulation-interface) |
| `standards/asam-traffic-participants/` | ASAM TrafficParticipants | v1.0.2 | Overview only | Not publicly available |
| `standards/iso-345xx/` | ISO 34503:2023 | 2023 | Paraphrased summary | [ISO](https://www.iso.org/standard/78952.html) |

### UML models

OpenDRIVE and OpenSCENARIO XML additionally carry the **tool-neutral UML model** the
standard is authored in, exported once from Enterprise Architect to ShapeChange SCXML and
committed:

| Model | Version | Classes |
|---|---|---|
| [`standards/asam-opendrive/uml/`](standards/asam-opendrive/uml/README.md) | V1.9.0 | 238 |
| [`standards/asam-openscenario-xml/uml/`](standards/asam-openscenario-xml/uml/README.md) | V1.4.0 | 343 |

These exist so that generating ontologies, SHACL shapes or schemas from the standards
needs **no Enterprise Architect licence** — only the export step does, and it has already
been done. Each model's README records how its version is established against the
normative schema in the sibling `schema/` directory.

## Submodules

Standards with open-source repositories are included as Git submodules:

```bash
git submodule update --init --recursive
```

| Submodule | License | Repository |
|-----------|---------|------------|
| `submodules/open-simulation-interface` | MPL-2.0 | [OpenSimulationInterface/open-simulation-interface](https://github.com/OpenSimulationInterface/open-simulation-interface) |
| `submodules/OpenCRG` | Apache-2.0 | [ASAM-ev/OpenCRG](https://github.com/ASAM-ev/OpenCRG) |

## Directory Structure

```
asam-openx-standards/
├── LICENSE                    # Composite license (ASAM unrestricted + OSS)
├── NOTICE                     # Attribution and source URLs
├── README.md                  # This file
├── standards/                 # Spec text as markdown (one dir per standard)
│   ├── asam-opendrive/        # 95 chapters
│   │   ├── schema/            # Normative XSD (V1.9.0)
│   │   └── uml/               # Tool-neutral UML model, SCXML (V1.9.0)
│   ├── asam-openscenario-xml/ # Normative XSD + UML model (V1.4.0)
│   ├── asam-openscenario-dsl/ # 60 chapters
│   ├── asam-openodd/          # 67 chapters
│   ├── asam-openmaterial-3d/  # 27 chapters
│   ├── asam-openlabel/        # Overview + JSON schema reference
│   ├── asam-opencrg/          # Overview
│   ├── asam-osi/              # Overview
│   ├── asam-traffic-participants/ # Overview
│   └── iso-345xx/             # Paraphrased summary (copyright)
├── submodules/                # Git submodules for OSS standards
│   ├── open-simulation-interface/
│   └── OpenCRG/
└── scripts/                   # Download/refresh automation
    └── download_asam_specs.py
```

## Usage

### As a Git Submodule

```bash
# In your project:
git submodule add https://github.com/ASCS-eV/asam-openx-standards.git submodules/asam-openx-standards
```

### For AI/LLM Context

The markdown files are optimized for AI agent consumption:
- Each file has a metadata header (source URL, version, license, download date)
- Chapter-level granularity enables precise citation
- INDEX.md in each standard directory provides navigation

### Citation Convention

When referencing in code or schemas:

```yaml
# [OpenDRIVE] §7.3 — Lane borders
# [OpenODD] Annex B — ISO 34503 taxonomy
# [OpenSCENARIO] §5.2.1 — Entity types
```

## Refreshing Standards

```bash
python scripts/download_asam_specs.py --all --no-verify
```

Use `--standard <name>` for individual updates. See `--help` for options.

## About

Maintained by [ASCS e.V.](https://github.com/ASCS-eV) for the
[ENVITED-X](https://github.com/ASCS-eV/ontology-management-base) ontology
ecosystem.
