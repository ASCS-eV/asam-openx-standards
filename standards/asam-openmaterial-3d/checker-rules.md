# ASAM Openmaterial 3D latest — Annex A (normative): Checker rules

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/09_annexes/checker-rules.html
> **Standard**: ASAM Openmaterial 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex A (normative): Checker rules

## Concept

Checker rules are semantic and syntactic requirements that shall be applied to both parts of ASAM OpenMATERIAL 3D (material and geometry).
ASAM OpenMATERIAL 3D defines a basic set of rules that apply to the entire standard, as well as specific rules for the two parts of ASAM OpenMATERIAL 3D.
Rules consist of a name, a UID (a unique identifier of the rule), and a description that specifies the requirements.

The UID is a string that encapsulates a sequence of concepts that identify a rule across different domains.
The concepts are ordered and separated by the separation character `:`.

The concepts for a rule UID are:

* **Emanating entity**: A domain name for the entity (organization or company) that declares the rule UID. For ASAM OpenMATERIAL 3D, it is `asam.net`.
* **Standard**: A short string that represents the standard or the domain to which the rule is applied. For ASAM OpenMATERIAL 3D, there are three different standard strings:

  + `xom`: General rules applicable for both parts or not categorizable because they are in-between.
  + `xom-geo`: Rules that only apply to the geometry part of ASAM OpenMATERIAL 3D.
  + `xom-mat`: Rules that only apply to the material part of ASAM OpenMATERIAL 3D.
* **Definition setting**: The version of the standard or the domain to which the rule appears or is applied for the first time, for example, `1.0.0`.
* **Rule full name**: The full name of the rule, as dot-separated, snake\_lower\_case string. The full name of a rule is composed of the rule set and the rule name, a unique string inside the categorization. The rule set can be nested, meaning that it can be defined as an arbitrary sequence of dot-separated names. The name is the snake\_case string after the last dot of the full name.

The following is a visual description of a rule UID:

```
<emanating-entity>:<standard>:x.y.z:rule_set.rule_name
```

|  |  |
| --- | --- |
|  | Third party rule UID creators (that is, emanating entities different from ASAM) should still fill all the concepts above. If that is not possible, concepts shall be left blank. Separation by `:` is still required (for example, `example.com:::rulename` is valid). |

UIDs are designed to be queried, for example, implementations may use UNIX pattern matching.

|  |  |
| --- | --- |
|  | Read the [ASAM Quality Checker Framework](https://github.com/asam-ev/qc-framework) documentation to see detailed information on how and which checks are implemented. |

## A.1 General rules

### A.1.1 General

#### valid\_json\_document

UID
:   asam.net:xom:1.0.0:general.valid\_json\_document

Description
:   ASAM OpenMATERIAL 3D files with the file extensions .xoma, .xomm, .xomp, or .xompt shall be valid JSON documents.

#### schema\_references

UID
:   asam.net:xom:1.0.0:general.schema\_references

Description
:   ASAM OpenMATERIAL 3D files with the file extensions .xoma, .xomm, .xomp, or .xompt shall contain a reference url to the corresponding schema in the second line of the file as "$schema": "https://raw.githubusercontent.com/asam-ev/OpenMATERIAL-3D/refs/tags/v<VERSION>/schemas/<CORRESPONDING\_SCHEMA>.json".

#### valid\_schema

UID
:   asam.net:xom:1.0.0:general.valid\_schema

Description
:   ASAM OpenMATERIAL 3D files with the file extensions .xoma, .xomm, .xomp, or .xompt shall be valid according to their corresponding JSON schema.

#### uris\_exist

UID
:   asam.net:xom:1.0.0:general.uris\_exist

Description
:   If a URI property to other file is set in a JSON file, the file linked in that property shall exist.

### A.1.2 XOMA

#### material\_textures\_exist

UID
:   asam.net:xom:1.0.0:xoma.material\_textures\_exist

Description
:   Textures mapped to material names in the 'materialTextureAssignment' field of .xoma files shall exist.

## A.2 Geometry

### A.2.1 XOMA

#### vehicle\_class\_data\_defined

UID
:   asam.net:xom-geo:1.0.0:xoma.vehicle\_class\_data\_defined

Description
:   If an asset is of type 'vehicle', the property 'vehicleClassData' must be set in the metadata.

#### human\_class\_data\_defined

UID
:   asam.net:xom-geo:1.0.0:xoma.human\_class\_data\_defined

Description
:   If an asset is of type 'human', the property 'humanClassData' must be set in the metadata.

#### texture\_assignment\_requires\_mapping

UID
:   asam.net:xom-geo:1.0.0:xoma.texture\_assignment\_requires\_mapping

Description
:   If the property 'materialTextureAssignment' is set, 'materialMappingUri' must also be set.

#### all\_texture\_rgba\_codes\_defined

UID
:   asam.net:xom-geo:1.0.0:xoma.all\_texture\_rgba\_codes\_defined

Description
:   If the property 'materialTextureAssignment' is set, all color codes of all referenced textures shall be covered by the material mapping table referenced in 'materialMappingUri'.

## A.2 Material

### A.2.1 XOMP

#### look\_up\_tables\_unique\_wavelengths

UID
:   asam.net:xom-mat:1.0.0:xomp.look\_up\_tables\_unique\_wavelengths

Description
:   Look-up tables referenced in a .xomp file should not have overlapping wavelength ranges. (Warning level)

### A.2.2 XOMPT

#### tables\_sorted\_correctly

UID
:   asam.net:xom-mat:1.0.0:xompt.tables\_sorted\_correctly

Description
:   Arrays in look-up tables shall be sorted based on the columns starting with the first.