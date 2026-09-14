# ASAM OpenX® Standards Reference Library

[![License: ASAM Unrestricted](https://img.shields.io/badge/License-ASAM%20Unrestricted-blue.svg)](https://www.asam.net/license)

This repository does two things:

1. **An open pipeline from ASAM's normative UML to OWL and SHACL.** ASAM authors
   OpenDRIVE and OpenSCENARIO XML as Enterprise Architect UML models. Those models are
   exported **once** to a tool-neutral, committed format, and an open-source toolchain
   regenerates an OWL 2 ontology, SHACL shapes, and — for verification — the normative XSD
   itself. No Enterprise Architect licence is needed to use, check or extend any of it.
   → **[`pipeline/README.md`](pipeline/README.md)** is the runbook.
2. **A version-pinned reference library** of the ASAM specification text as markdown, for
   citation in ontology development and AI-assisted workflows.

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

### Generated artifacts

From those models, [`scripts/generate_semantic_artifacts.py`](scripts/generate_semantic_artifacts.py)
produces and commits:

| Standard | OWL 2 ontology | SHACL shapes | Provenance |
|---|---|---|---|
| OpenDRIVE V1.9.0 | [`standards/asam-opendrive/generated/opendrive.owl.ttl`](standards/asam-opendrive/generated/opendrive.owl.ttl) | [`opendrive.shacl.ttl`](standards/asam-opendrive/generated/opendrive.shacl.ttl) | [`provenance.json`](standards/asam-opendrive/generated/provenance.json) |
| OpenSCENARIO XML V1.4.0 | [`standards/asam-openscenario-xml/generated/openscenario.owl.ttl`](standards/asam-openscenario-xml/generated/openscenario.owl.ttl) | [`openscenario.shacl.ttl`](standards/asam-openscenario-xml/generated/openscenario.shacl.ttl) | [`provenance.json`](standards/asam-openscenario-xml/generated/provenance.json) |

Every class in both models reaches the ontology — 238 and 343 respectively, asserted on
every run. These files are **generated output and must never be hand-edited**: they are
written in RDFC-1.0 canonical form so that regenerating an unchanged model reproduces the
bytes, and CI fails any artifact that is not canonical.

Two properties make a diff in them diagnosable rather than mysterious:

- **The toolchain is locked.** [`pipeline/toolchain-lock.json`](pipeline/toolchain-lock.json)
  pins the exact commit of every generator, the JDK/Maven build environment, content-based
  fingerprints of the built binaries, and the exact serialization library versions.
- **Nothing is post-processed.** If an artifact is wrong, the model, the configuration or
  the tool is wrong — and every tool fix is contributed upstream rather than patched
  locally.

### Checking it against the normative schema

ASAM publishes the XSD independently of the UML, which gives the pipeline something rare:
a second, independently produced description of the same standard to check against.
[`scripts/check_xsd_structural_parity.py`](scripts/check_xsd_structural_parity.py)
regenerates an XSD from the same committed model and compares it to ASAM's — enumeration
values match exactly (292 and 251), and the content-model comparison reports where the
model cannot yet express what the normative schema declares. That evidence is not
committed; the accepted differences are recorded in `pipeline/*-xsd-content-baseline.json`.

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
├── AGENTS.md                  # Orientation for AI agents
├── pipeline/                  # Generation pipeline configuration
│   ├── README.md              #   The operational runbook
│   ├── toolchain-lock.json    #   Exact tool commits + build environment
│   ├── *-owl.config.xml       #   ShapeChange OWL target config
│   ├── *-xsd.config.xml       #   ShapeChange XSD target config (verification)
│   ├── *mapentries-asam.xml   #   ASAM primitive type mappings
│   └── *-xsd-content-baseline.json  # Accepted deviations from the normative XSD
├── scripts/
│   ├── generate_semantic_artifacts.py  # Runs the OWL + SHACL stages
│   ├── check_xsd_structural_parity.py  # Compares regenerated XSD to ASAM's
│   ├── xsd_content_model.py            # Content-model comparison oracle
│   ├── check_toolchain_lock.py         # Lock <-> provenance consistency (CI)
│   ├── check_canonical.py              # Canonical-form check (CI)
│   └── download_asam_specs.py          # Refreshes the markdown library
├── standards/                 # Spec text as markdown (one dir per standard)
│   ├── asam-opendrive/        # 95 chapters
│   │   ├── schema/            # Normative XSD (V1.9.0), byte-exact + checksummed
│   │   ├── uml/               # Tool-neutral UML model, SCXML (V1.9.0)
│   │   └── generated/         # OWL + SHACL + provenance (generated, do not edit)
│   ├── asam-openscenario-xml/ # Normative XSD + UML model + generated (V1.4.0)
│   ├── asam-openscenario-dsl/ # 60 chapters
│   ├── asam-openodd/          # 67 chapters
│   ├── asam-openmaterial-3d/  # 27 chapters
│   ├── asam-openlabel/        # Overview + JSON schema reference
│   ├── asam-opencrg/          # Overview
│   ├── asam-osi/              # Overview
│   ├── asam-traffic-participants/ # Overview
│   └── iso-345xx/             # Paraphrased summary (copyright)
└── submodules/                # Git submodules for OSS standards
    ├── open-simulation-interface/
    └── OpenCRG/
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

## Regenerating the OWL and SHACL artifacts

Needs JDK 21, Maven, and the three generator checkouts as **siblings** of this repository,
each at the commit pinned in [`pipeline/toolchain-lock.json`](pipeline/toolchain-lock.json):

```bash
pip install -r scripts/requirements.txt

for standard in asam-opendrive asam-openscenario-xml; do
  python scripts/generate_semantic_artifacts.py \
      --standard "$standard" \
      --shapechange ../ShapeChange \
      --shaclplay ../shacl-play \
      --rules ../owl2shacl/owl2sh-closed.ttl
done
```

The script validates every checkout against the lock before building anything, and builds
both Java tools from source, so the binaries that run are provably the ones the lock
describes. Read [`pipeline/README.md`](pipeline/README.md) first — updating a pin is a
release-like action that must regenerate both standards in the same change.

CI does not run this (it needs a JDK and Maven). CI verifies the cheap invariants instead:
canonical form of the committed artifacts, lock↔provenance consistency, the content-model
oracle's own test suite, and the checksums of the redistributed models and schemas.

## Refreshing Standards

```bash
python scripts/download_asam_specs.py --all --no-verify
```

Use `--standard <name>` for individual updates. See `--help` for options.

## About

Maintained by [ASCS e.V.](https://github.com/ASCS-eV) for the
[ENVITED-X](https://github.com/ASCS-eV/ontology-management-base) ontology
ecosystem.
