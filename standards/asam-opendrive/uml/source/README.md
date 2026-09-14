# ASAM OpenDRIVE® Enterprise Architect Project — V1.9.0

The original Enterprise Architect project from which
[`../opendrive.scxml`](../README.md) was exported. This is the **root input of the whole
pipeline**: everything else in this repository that describes OpenDRIVE structurally —
the SCXML model, the OWL ontology, the SHACL shapes, the generated XSD — derives from
this file.

**This file is not an original work of this project.** Copyright © ASAM e.V., 2026.
Redistributed under the ASAM Unrestricted Distribution Clause; see the repository
[LICENSE](../../../../LICENSE) and [NOTICE](../../../../NOTICE), which name the UML models
explicitly.

## Provenance

| Field | Value |
|---|---|
| Standard | ASAM OpenDRIVE® |
| Version | **V1.9.0** — matches the normative schema in [`../../schema/`](../../schema/README.md) |
| Deliverable | `ASAM_OpenDRIVE_v1-9-0_Enterprise_Architect_UML_model.zip` |
| Source | <https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/> |
| Retrieved | 2026-07-28 — the same retrieval as the XSD deliverable in `../../schema/` |
| Format | Enterprise Architect project, `.qeax` (SQLite database) |

### Checksums (SHA-256)

| File | Bytes | SHA-256 |
|---|---:|---|
| `ASAM_OpenDRIVE.qeax` | 3,330,048 | `831448bd0581000918d1e13db67f62bbc5b705799500f4bb06055388538c5e5a` |
| the `.zip` it came in | 766,200 | `cd82b0c43fdc68b60044bcc4406107c8b2d040da71535201af083feab967ecb4` |

The zip contains exactly one entry, this `.qeax`. It is committed unpacked so that its
checksum can be verified directly and so that the file can be opened without an
intermediate step.

## This file is stored in Git LFS

`.gitattributes` routes `*.qeax` through Git LFS, because a `.qeax` is an opaque binary
that Git cannot delta-compress — without LFS every future ASAM revision would add its
full compressed size (~780 KB here) to history permanently.

**A clone without Git LFS gives you a ~130-byte pointer file, not the model.** If the file
you have is that small, or if its SHA-256 does not match the table above, run:

```bash
git lfs pull
```

The same applies to tarball downloads — `git archive` and GitHub's *Download ZIP* contain
pointers. CI must check out with `lfs: true`.

## Reading it without Enterprise Architect

A `.qeax` is a SQLite database, so **inspecting the model needs no EA licence** — only the
file. This is what makes the claims elsewhere in this repository checkable rather than
merely asserted:

```bash
sqlite3 ASAM_OpenDRIVE.qeax \
  "SELECT Client, Description FROM t_xref WHERE Name = 'Stereotypes';"
```

Useful tables:

| Table | Holds |
|---|---|
| `t_object` | classes and packages (`Stereotype` here holds **only one** stereotype — prefer `t_xref`) |
| `t_xref` where `Name='Stereotypes'` | the authoritative, multi-valued stereotype listing |
| `t_attribute`, `t_attributetag` | properties and their tagged values |
| `t_connector`, `t_connectortag` | associations and their tagged values |
| `t_objectproperties` | class-level tagged values |

Two examples of why this matters. The model marks 468 attributes `XSDattribute`, exactly
matching the 468 `xs:attribute` declarations in the normative schema; and
`t_road_planView_geometry` carries the tagged value `modelGroup = choice`, which is the
evidence that ASAM does declare that content model even though the export dropped it.

## Regenerating the export

Only the export step needs Enterprise Architect. See
[Reproducing the export](../README.md#reproducing-the-export-requires-ea-once) in the
parent README for the ShapeChange build, the `eaapi` install and the exact command.

## Updating

1. Download the new `*_Enterprise_Architect_UML_model.zip` from the source URL above.
2. Replace the `.qeax` and update the version, retrieval date, byte count and both
   checksums in this file.
3. Re-run the export and regenerate every downstream artifact — the SCXML checksums in
   `../README.md` and `source_model.sha256` in `../../generated/provenance.json` all
   follow from these bytes.
