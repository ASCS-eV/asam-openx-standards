# ASAM OpenSCENARIO® XML Schema — V1.4.0

Normative XSD schema of ASAM OpenSCENARIO® XML V1.4.0, matching the UML model in
[`../uml/`](../uml/). This is the machine-readable source of truth for every OpenSCENARIO
enumeration (`PrecipitationType`, `ConditionEdge`, `Rule`, …) used by downstream consumers,
and the reference the [structural parity check](../../../pipeline/README.md#checking-it-the-xsd-structural-parity-check)
compares the generated schema against.

Unlike OpenDRIVE, ASAM publishes OpenSCENARIO XML as a **single** schema document rather than a
per-package split, so this directory holds one file.

**This file is not an original work of this project.** Copyright © ASAM e.V., 2026.
Redistributed under the ASAM Unrestricted Distribution Clause; see the repository
[LICENSE](../../../LICENSE) and the notice in the file's XML header:

> *"In alteration to the regular license terms, ASAM allows unrestricted distribution of this
> standard. Paragraph 2 (1) of ASAM's regular license terms is therefore substituted by the
> following clause: 'The licensor grants everyone a basic, non-exclusive and unlimited license
> to use the standard ASAM OpenSCENARIO XML'."*

## Provenance

| Field | Value |
|---|---|
| Standard | ASAM OpenSCENARIO® XML |
| Version | **V1.4.0** |
| Deliverable | `ASAM_OpenSCENARIO_XML_V1.4.0.zip` |
| Source | <https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_XML/latest/> |
| Retrieved | 2026-07-28 |
| Target namespace | none — the schema is unqualified, as is OpenDRIVE's |

### File checksum (SHA-256, truncated)

| File | SHA-256 |
|---|---|
| `OpenSCENARIO.xsd` | `949fe2bcebd1f3fd…` |

The checksum covers the file **as ASAM shipped it**, line endings included. `.gitattributes`
marks `standards/*/schema/**` as not text so neither Git nor a pre-commit hook rewrites them;
normalising line endings would invalidate this checksum and the file would no longer be
verifiable against the deliverable. This schema happens to ship with LF, where OpenDRIVE's seven
ship with CRLF — another reason not to let either be normalised on the assumption they match.

## Relationship to the UML model

Both describe V1.4.0, and the parity check confirms **251 enumeration values in each**. They are
not interchangeable: the schema encodes most properties as XML attributes, while the UML model
selects no attribute encoding, and the schema declares `*Ref` properties as `type="String"` name
references where the UML models associations. See
[`pipeline/README.md`](../../../pipeline/README.md#one-property-asam-models-as-a-reference-to-a-union)
for what that difference costs and which of it is filed as a change request to ASAM.

Where the two disagree, **this file wins**: it is the normative deliverable, and the OWL and
SHACL in [`../generated/`](../generated/) are derived artifacts.

## Updating

1. Download the deliverable from the source URL above.
2. Replace the file here and update the version, date and checksum in this README.
3. Re-run the parity check; a changed enumeration count will fail it, which is intentional.
4. Downstream consumers that pin enumerations against this file will fail until their
   constraints are re-derived. In `ontology-management-base`, run `just validate-enums`, and
   re-derive the vendored copy with `python -m omb.utils.asam_imports`.
