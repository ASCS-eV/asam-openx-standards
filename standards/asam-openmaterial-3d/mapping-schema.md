# ASAM OpenMATERIAL® 3D latest — 7.6 Mapping schema

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/07_geometry/mapping-schema.html
> **Standard**: ASAM OpenMATERIAL® 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.6 Mapping schema

## 7.6.1 metadata

The key meta information about the mapping table, including its identity, authorship, technical specifications, and legal details.

**Type:** `object`  
**Required:** Yes

### 7.6.1.1 name

The display name of the material mapping table.

**Type:** `string`  
**Required:** Yes

### 7.6.1.2 description

Short description of the mapping table in 2 - 3 sentences.

**Type:** `string`  
**Required:** No

### 7.6.1.3 uuid

Universally unique identifier for the mapping table in 8-4-4-4-12 format, see [[12](../bibliography.html#bib-uui)]. The uuid stays the same, even if version is updated.

**Type:** `string`  
**Pattern:** `\\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\\b$`  
**Required:** Yes

### 7.6.1.4 mappingVersion

The version number of the mapping table, following semantic versioning (for example, '1.0.0').

**Type:** `string`  
**Pattern:** `^\\d+\\.\\d+\\.\\d+$`  
**Required:** Yes

### 7.6.1.5 openMaterial3dVersion

The version of the ASAM OpenMATERIAL® 3D specification used, adhering to semantic versioning (for example, '1.0.0').

**Type:** `string`  
**Pattern:** `^\\d+\\.\\d+\\.\\d+$`  
**Required:** Yes

### 7.6.1.6 copyrights

Indicates copyright details, including the year and copyright holder (for example, '© 2024 ACME Inc.').

**Type:** `array`  
**Required:** Yes

### 7.6.1.7 license

Describes the license for mapping table distribution. Use an SPDX identifier for open-source licenses (for example, 'MIT'), or provide a URL or filename for proprietary licenses.

**Type:** `string`  
**Required:** Yes

### 7.6.1.8 authors

Lists the author(s) of the mapping table as a name, email, or company.

**Type:** `array`  
**Required:** Yes

### 7.6.1.9 creationDate

The date and time of mapping table creation, formatted as YYYYMMDDTHHMMSSZ according to ISO 8601 [[8](../bibliography.html#bib-iso8601)] (for example, '20240703T101728Z').

**Type:** `string`  
**Pattern:** `^\\d{8}T\\d{6}Z$`  
**Required:** No

## 7.6.2 materialMapping

Array containing material mappings.

**Type:** `array`  
**Required:** Yes

Columns of the table:

* Column 1: Material name or RGB code. The RGB code represents color values in an ASAM OpenMATERIAL® 3D assignment texture.
* Column 2: File path to the material.
* Column 3: Description of the material.