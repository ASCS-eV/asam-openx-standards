# ASAM OpenSCENARIO® XML Enterprise Architect Project — V1.4.0

The original Enterprise Architect project from which
[`../openscenario.scxml`](../README.md) was exported. This is the **root input of the whole
pipeline**: everything else in this repository that describes OpenSCENARIO XML
structurally — the SCXML model, the OWL ontology, the SHACL shapes, the generated XSD —
derives from this file.

**This file is not an original work of this project.** Copyright © ASAM e.V., 2026.
Redistributed under the ASAM Unrestricted Distribution Clause; see the repository
[LICENSE](../../../../LICENSE) and [NOTICE](../../../../NOTICE), which name the UML models
explicitly.

## Provenance

| Field | Value |
|---|---|
| Standard | ASAM OpenSCENARIO® XML |
| Version | **V1.4.0** — matches the normative schema in [`../../schema/`](../../schema/README.md) |
| Deliverable | `ASAM_OpenSCENARIO_v1.4.0_Model.zip` |
| Source | <https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_XML/latest/> |
| Retrieved | 2026-07-28 — the same retrieval as the XSD deliverable in `../../schema/` |
| Format | Enterprise Architect project, `.qeax` (SQLite database) |

### Checksums (SHA-256)

| File | Bytes | SHA-256 |
|---|---:|---|
| `OpenSCENARIO.qeax` | 5,046,272 | `9a43d4c7423995c8a7604ab3aa7c17b92931afa4cd1fcf227074b8c24fddb8b1` |
| the `.zip` it came in | 5,811,782 | `0821528410caf47ca78f09769b052a0123b684a38e5f103495dcaa47e1c716c6` |

### Why only the `.qeax`

Unlike the OpenDRIVE deliverable, this zip contains **two** files: `OpenSCENARIO.eapx`
(65,163,264 bytes) and `OpenSCENARIO.qeax` (5,046,272 bytes). They are the same model in
two Enterprise Architect file formats. Only the `.qeax` is committed:

- it is the format the export actually consumes (`inputModelType=EA7`);
- it is a SQLite database and therefore readable without EA, which the `.eapx` is not;
- committing the `.eapx` as well would add ~60 MB for no additional information.

Anyone needing the `.eapx` should download the deliverable from the source URL above; its
zip checksum is recorded here so the retrieval can be matched to this one.

## This file is stored in Git LFS

`.gitattributes` routes `*.qeax` through Git LFS, because a `.qeax` is an opaque binary
that Git cannot delta-compress — without LFS every future ASAM revision would add its
full compressed size (~1.6 MB here) to history permanently.

**A clone without Git LFS gives you a ~130-byte pointer file, not the model.** If the file
you have is that small, or if its SHA-256 does not match the table above, run:

```bash
git lfs pull
```

The same applies to tarball downloads — `git archive` and GitHub's *Download ZIP* contain
pointers. CI must check out with `lfs: true`.

## Reading it without Enterprise Architect

A `.qeax` is a SQLite database, so **inspecting the model needs no EA licence** — only the
file:

```bash
sqlite3 OpenSCENARIO.qeax \
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

This model is where the cross-standard comparisons in the issue tracker come from. It
carries 48 `«union»` classes using the UML standard stereotype — which OpenDRIVE does not,
using `XSDunion` instead — as well as 171 `xor` stereotypes on connectors and 55 classes
tagged `modelGroup = choice`, none of which reach the current export.

## Regenerating the export

Only the export step needs Enterprise Architect. See
[Reproducing the export](../README.md#reproducing-the-export-requires-ea-once) in the
parent README for the ShapeChange build, the `eaapi` install and the exact command.

Note that this standard's export configuration carries a `<PackageInfo>` override, because
the OpenSCENARIO XML schema declares no XML `targetNamespace` at all and ShapeChange's
schema detection has nothing to find. See the comment in
[`../export-model-to-scxml.config.xml`](../export-model-to-scxml.config.xml).

## Updating

1. Download the new `*_Model.zip` from the source URL above.
2. Replace the `.qeax` and update the version, retrieval date, byte counts and both
   checksums in this file.
3. Re-run the export and regenerate every downstream artifact — the SCXML checksums in
   `../README.md` and `source_model.sha256` in `../../generated/provenance.json` all
   follow from these bytes.
