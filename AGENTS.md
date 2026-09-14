# Agent Instructions for ASAM OpenX Standards

This repository does **two** things. Confusing them is the most common way to get work
here wrong, so read this section before anything else.

## 1. It is a generation pipeline (the primary engineering artifact)

ASAM authors OpenDRIVE and OpenSCENARIO XML as **UML models in Enterprise Architect**.
Those models are the normative source the published XSD schemas are themselves derived
from, but they ship as a proprietary `.qeax`/`.eapx` EA project that almost nobody can
open.

This repository exists to break that lock-in:

```
ASAM_OpenDRIVE.qeax         proprietary EA project — ASAM's normative model
        │
        │  ShapeChange ModelExport, run ONCE, output committed
        ▼                   ← this is the only step that needs an EA licence
standards/<std>/uml/<std>.scxml     tool-neutral, diff-friendly, committed
        │                             *** SOURCE OF TRUTH for everything below ***
        ├──▶ ShapeChange OWL target ──▶ standards/<std>/generated/<std>.owl.ttl
        │                                      │
        │                                      ▼ SHACL Play! + owl2shacl rules
        │                               standards/<std>/generated/<std>.shacl.ttl
        │
        └──▶ ShapeChange XSD target ──▶ regenerated XSD, compared against ASAM's
                                        normative schema in standards/<std>/schema/
                                        (evidence, never committed)
```

The goal is that **the normative XSD, an OWL 2 ontology and SHACL shapes are all
reproducible from one open model by one open-source toolchain**, with no EA licence and
no hand-editing — so that [ontology-management-base](https://github.com/ASCS-eV/ontology-management-base)
and downstream tools can consume machine-readable ASAM semantics.

**The full runbook is [`pipeline/README.md`](pipeline/README.md). Read it before touching
anything under `pipeline/`, `scripts/` or `standards/*/generated/`.**

## 2. It is a reference library (for citation)

It also holds version-pinned markdown copies of the ASAM specification text. The ENVITED-X
ontologies describe **searchable metadata** for simulation assets; they align with,
summarize and extend the standards documented here. When adding or modifying ontology
properties, cite the normative source from these references — see
[Citation Pattern](#citation-pattern).

## Hard rules for agents

These are not style preferences. Each one has cost real debugging time.

1. **`standards/*/generated/**` is generated output. Never hand-edit it.** Not the OWL, not
   the SHACL, not `provenance.json`. CI (`verify-generated.yml`) proves every committed
   artifact is in RDFC-1.0 canonical form; a hand-edit is detected as a non-canonical file.

2. **Nothing is post-processed.** Both generation stages are off-the-shelf tools driven by
   the configuration in `pipeline/`; the script only resolves paths and runs them in order.
   If an artifact is wrong, exactly one of three things is wrong — the **model**, the
   **configuration**, or the **tool** — and the fix belongs *there*. Do not add a
   fix-up pass.

3. **A tool fix goes upstream, not into a local patch.** Every change to ShapeChange,
   SHACL Play! or owl2shacl is written as a self-contained, single-commit upstream PR, with
   a mirrored PR in the `ASCS-eV` fork so it stays trackable. A fork exists only for as long
   as its contributions are unmerged; `carried_commits: []` in the lock is the **goal
   state**, not a defect.

4. **`pipeline/toolchain-lock.json` and `scripts/requirements.txt` are release-like edits,
   never routine ones.** They pin every input that determines the output bytes. Changing one
   means rebasing the fork, regenerating **both** standards twice with clean builds,
   confirming the fingerprints and bytes are identical between runs, and committing the
   lock, the artifacts and the provenance together. Bumping a pin without regenerating in
   the same change is a defect.

5. **A green exit code does not mean the model was fully encoded.** ShapeChange reports a
   class it cannot encode as a *warning* and carries on. `check_shapechange_log()` gates
   this against an explicit allowlist — widening that allowlist requires saying why, in the
   same change.

6. **Deviating from ASAM is allowed, but only with argumentation.** Where the open model
   must differ from the EA model to reproduce the normative artifacts, record the deviation
   and the standards-based reason. Where the *standard itself* looks wrong, open an issue so
   it can be reported to ASAM — do not silently work around it.

## Where things are decided

| Question | Authoritative file |
|---|---|
| How do I set up a machine to run this? | [`pipeline/SETUP.md`](pipeline/SETUP.md) |
| How do I run the pipeline? | [`pipeline/README.md`](pipeline/README.md) |
| Which tool commit is used, and what does it carry? | [`pipeline/toolchain-lock.json`](pipeline/toolchain-lock.json) |
| Which OWL/XSD encoding rules, and why each one? | `pipeline/*-owl.config.xml`, `pipeline/*-xsd.config.xml` |
| How was this model exported, and what does it *not* carry? | `standards/*/uml/README.md` ("Known encoding gaps") |
| What produced the committed artifacts? | `standards/*/generated/provenance.json` |
| What differs from ASAM's normative XSD, and is it accepted? | `pipeline/*-xsd-content-baseline.json` |
| Which differences are ASAM's to fix, and what is the evidence? | [`pipeline/asam-change-requests.md`](pipeline/asam-change-requests.md) |
| What are ASAM's original models, and how do I read them? | `standards/*/uml/source/README.md` |

## Quick Reference: Concept → File → Section

### Enumerations (most commonly needed)

**Authoritative source: `asam-opendrive/uml/opendrive.scxml`.** It carries all **56**
OpenDRIVE enumerations with literals that match the normative XSD exactly, including the
V1.9.0 additions (`e_layerType`, `e_personCategory`, `e_vehicleCategory`). The prose table
below and `ENUMERATIONS.yaml` are convenience indexes over a subset — `map-uml-enumerations.md`
is a Markdown conversion of the specification annex and does not contain the `e_*` type
identifiers at all, so it cannot be grepped by type name. Prefer the model, or the XSD in
`asam-opendrive/schema/`, whenever a complete or exact value set matters.

| Concept | File | Section |
|---------|------|---------|
| Road types | `asam-opendrive/map-uml-enumerations.md` | A.6.2 `e_roadType` |
| Lane types | `asam-opendrive/map-uml-enumerations.md` | A.3.7 `e_laneType` |
| Object types | `asam-opendrive/map-uml-enumerations.md` | A.4.5 `e_objectType` |
| Junction types | `asam-opendrive/map-uml-enumerations.md` | A.2.1 `e_junction_type` |
| Signal semantics | `asam-opendrive/map-uml-enumerations.md` | A.7.5 `e_signals_semantics_lane` |
| Road mark types | `asam-opendrive/map-uml-enumerations.md` | A.3.4 `e_roadMarkType` |
| Road mark colors | `asam-opendrive/map-uml-enumerations.md` | A.3.10 `e_roadMarkColor` |
| CRG mode/purpose | `asam-opendrive/map-uml-enumerations.md` | A.2.2–A.2.3 |
| Junction group types | `asam-opendrive/map-uml-enumerations.md` | A.2.5 `e_junctionGroup_type` |

### Definitions & Core Concepts

| Concept | File | What You'll Find |
|---------|------|-----------------|
| Road network terms | `asam-opendrive/03-terms-and-definitions.md` | Normative definitions (road, lane, junction, signal, etc.) |
| OpenDRIVE scope | `asam-opendrive/01-scope.md` | What the standard covers |
| Header/metadata | `asam-opendrive/06-04-header.md` | File metadata structure |
| Georeferencing | `asam-opendrive/08-*` chapters | Coordinate systems |
| Lane model | `asam-opendrive/11-*` chapters | Lane structure, widths, sections |
| Junctions | `asam-opendrive/12-*` chapters | Junction connections, types |
| Signals | `asam-opendrive/14-*` chapters | Traffic signs, signals, markings |
| Objects | `asam-opendrive/13-*` chapters | Roadside objects, tunnels, bridges |

### ODD / Scenario Concepts

| Concept | File | What You'll Find |
|---------|------|-----------------|
| ODD taxonomy | `asam-openodd/06-02-*` through `06-08-*` | Full ODD module breakdown |
| ODD scenery | `asam-openodd/06-*` chapters | Road, environment, weather |
| Scenario structure | `asam-openscenario-dsl/02-*` through `05-*` | Domain model, actions, triggers |
| Tagging model & semantics | `asam-openlabel/08-scenario-tagging.md` | Full tagging spec: ontology, subsets, values, use cases |
| Label taxonomy | `asam-openlabel/09-references.md` | Complete JSON schema class reference |
| OpenLABEL ontology (source) | `asam-openlabel/Source/ontologies/` | Original scenario tagging ontology (Turtle) |
| OpenLABEL JSON schema | `asam-openlabel/Source/openlabel_json_schema-v1.0.0.json` | Full JSON schema (draft-07) |
| OpenLABEL examples | `asam-openlabel/Source/examples/` | 10 annotation examples |

### Material / Environment

| Concept | File | What You'll Find |
|---------|------|-----------------|
| Material properties | `asam-openmaterial-3d/` chapters | 3D material/geometry schemas |
| Sensor simulation | `asam-osi/INDEX.md` | Overview of OSI interface |
| Road surfaces | `asam-opencrg/INDEX.md` | OpenCRG road profile format |

## Search Strategies

### Find an enumeration's valid values
```bash
grep -A 50 "e_laneType" standards/asam-opendrive/map-uml-enumerations.md
```

### Find a concept definition
```bash
grep -i "junction" standards/asam-opendrive/03-terms-and-definitions.md
```

### Find OpenLABEL tagging semantics
```bash
grep -i "boundary\|subset\|tagging value" standards/asam-openlabel/08-scenario-tagging.md
```

### Find OpenLABEL ontology class hierarchy
```bash
grep "rdfs:subClassOf" standards/asam-openlabel/Source/ontologies/openlabel_ontology_scenario_tags.ttl
```

### Check version history (introduced/deprecated)
Look for "Introduced" and "Deprecated" columns in enumeration tables in
`map-uml-enumerations.md`. Values show the version where they were added/removed.

### Find cross-standard relationships
See `CROSS_REFERENCES.md` for concept equivalences across standards.

### Find machine-readable enum data
See `ENUMERATIONS.yaml` for structured enum definitions with deprecation metadata.

## Citation Pattern

When modifying ontologies in ontology-management-base, cite sources as:

**In SHACL comments:**
```turtle
sh:description "Road types per OpenDRIVE v1.9.0, Annex A.6.2 (e_roadType)"@en ;
```

**In OWL annotations:**
```turtle
dcterms:source "ASAM OpenDRIVE v1.9.0, Annex A.6.2, Table 194" ;
```

**In LinkML slots:**
```yaml
comments:
  - "[OpenDRIVE] Annex A.3.7, Table 176 (e_laneType)"
see_also:
  - https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/...
```

## Directory Layout

```
pipeline/                    # ← the generation pipeline's configuration
├── README.md                #   THE RUNBOOK — read this first
├── SETUP.md                 #   machine setup: JDK/Maven versions, checkouts, known traps
├── toolchain-lock.json      #   exact tool commits, build env, content fingerprints
├── *-owl.config.xml         #   ShapeChange OWL target, per standard
├── *-xsd.config.xml         #   ShapeChange XSD target, per standard (verification only)
├── mapentries-asam.xml      #   ASAM primitive type -> XSD datatype (OWL stage)
├── xsdmapentries-asam.xml   #   the same, for the XSD stage
└── *-xsd-content-baseline.json  # accepted deviations from ASAM's normative XSD

scripts/
├── generate_semantic_artifacts.py  # runs both stages; builds the tools from the lock
├── check_xsd_structural_parity.py  # regenerates XSD, compares to ASAM's normative one
├── xsd_content_model.py            # the content-model comparison oracle
├── check_toolchain_lock.py         # static: lock <-> provenance consistency (runs in CI)
├── check_canonical.py              # committed artifacts are in RDFC-1.0 canonical form
└── download_asam_specs.py          # refreshes the markdown reference library

standards/
├── asam-opendrive/          # 95 chapters — road network format (v1.9.0)
│   ├── schema/              # normative XSD as ASAM published it (byte-exact, checksummed)
│   ├── uml/                 # tool-neutral UML model, SCXML (v1.9.0) — 238 classes
│   └── generated/           # *** GENERATED — never hand-edit ***
│       ├── opendrive.owl.ttl     #   OWL 2 ontology
│       ├── opendrive.shacl.ttl   #   SHACL shapes
│       └── provenance.json       #   what produced them
├── asam-openscenario-xml/   # scenario file format (v1.4.0), no prose chapters
│   ├── schema/              # normative XSD (v1.4.0)
│   ├── uml/                 # tool-neutral UML model, SCXML (v1.4.0) — 343 classes
│   └── generated/           # *** GENERATED — never hand-edit ***
├── asam-openscenario-dsl/   # 59 chapters — scenario language (v2.2.0)
├── asam-openodd/            # 62 chapters — operational design domain (v1.0.0)
├── asam-openmaterial-3d/    # 27 chapters — material/geometry (BS 1.0.0)
├── asam-openlabel/          # 13 chapters + Source/ — labeling & tagging (v1.0.0)
├── asam-osi/                # 1 file — open simulation interface
├── asam-opencrg/            # 1 file — road surface profiles
├── asam-traffic-participants/ # 1 file — road user types
└── iso-345xx/               # 1 file — ISO 34503 (paraphrased summary)

submodules/
├── open-simulation-interface/ # Full OSI source (MPL-2.0)
└── OpenCRG/                  # Full OpenCRG source (Apache-2.0)
```

Only `standards/*/uml/` and `standards/*/generated/` exist for OpenDRIVE and
OpenSCENARIO XML — those are the two standards the pipeline covers. Everything else under
`standards/` is reference text only.

## The toolchain, and where it lives

The generators are **sibling checkouts** (`../ShapeChange`, `../shacl-play`,
`../owl2shacl`), never nested inside this repository, each pinned to an exact commit by
`pipeline/toolchain-lock.json`. Their `ASCS-eV` forks exist only to carry contributions
that upstream has not merged yet:

| Tool | Role | Fork status |
|---|---|---|
| ShapeChange | UML → OWL, and UML → XSD for verification | forked; carries the unmerged OWL union fix |
| SHACL Play! | OWL → SHACL | ✅ fully upstreamed; pinned at plain upstream |
| owl2shacl | the OWL→SHACL conversion *rules* (`owl2sh-closed.ttl`) | ✅ fully upstreamed; pinned at plain upstream |
| diffable-rdf | RDFC-1.0 canonicalization, so regeneration is byte-stable | ASCS-eV-owned, consumed from PyPI |

Running the pipeline needs **JDK 21 and Maven**. CI deliberately does *not* run it — the
workflows only verify canonical form, lock/provenance consistency, and the committed
models' checksums.

## Ontology ↔ Standard Mapping

| ENVITED-X Domain | Primary Standard | Key Reference Files |
|-----------------|-----------------|-------------------|
| `hdmap` | OpenDRIVE | `map-uml-enumerations.md`, `03-terms-and-definitions.md` |
| `scenario` | OpenSCENARIO DSL | `02-*` through `05-*` (domain model) |
| `openlabel-v2` | OpenLABEL + OpenODD + ISO 34503 | `asam-openlabel/08-scenario-tagging.md`, `asam-openodd/06-*`, `iso-345xx/` |
| `ositrace` | OSI | `asam-osi/INDEX.md`, submodule source |
| `surface-model` | OpenCRG + OpenDRIVE | `asam-opencrg/`, CRG sections in OpenDRIVE |
| `environment-model` | OpenMATERIAL 3D | `asam-openmaterial-3d/` chapters |
