# ASAM Openmaterial 3D latest — 8.4 Material optical schema

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/08_material/material-optical-schema.html
> **Standard**: ASAM Openmaterial 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.4 Material optical schema

## 8.4.1 metadata

The key meta information about the optical look-up table.

**Type:** `object`  
**Required:** Yes

### 8.4.1.1 name

The display name of the material, such as 'Red brick' or 'Dark asphalt'.

**Type:** `string`  
**Required:** Yes

### 8.4.1.2 description

Short description of the material in 2 - 3 sentences.

**Type:** `string`  
**Required:** No

### 8.4.1.3 uuid

Universally unique identifier for the material in 8-4-4-4-12 format, see [[12](../bibliography.html#bib-uui)]. The uuid stays the same, even if version is updated.

**Type:** `string`  
**Pattern:** `\\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\\b$`  
**Required:** Yes

### 8.4.1.4 materialVersion

The version number of the material, following semantic versioning (for example, '1.0.0').

**Type:** `string`  
**Pattern:** `^\\d+\\.\\d+\\.\\d+$`  
**Required:** Yes

### 8.4.1.5 openMaterial3dVersion

The version of the ASAM OpenMATERIAL 3D specification used, adhering to semantic versioning (for example, '1.0.0').

**Type:** `string`  
**Pattern:** `^\\d+\\.\\d+\\.\\d+$`  
**Required:** Yes

### 8.4.1.6 copyrights

Indicates copyright details, including the year and copyright holder (e.g., '© 2024 ACME Inc.').

**Type:** `array`  
**Required:** Yes

### 8.4.1.7 license

Describes the license for material distribution. Use an SPDX identifier for open-source licenses (for example, 'MIT'), or provide a URL or filename for proprietary licenses.

**Type:** `string`  
**Required:** Yes

### 8.4.1.8 authors

Lists the author(s) of the material as a name, email, or company.

**Type:** `array`  
**Required:** Yes

### 8.4.1.9 creationDate

The date and time of material creation, formatted as YYYYMMDDTHHMMSSZ according to ISO 8601 [[8](../bibliography.html#bib-iso8601)] (for example, '20240703T101728Z').

**Type:** `string`  
**Pattern:** `^\\d{8}T\\d{6}Z$`  
**Required:** No

### 8.4.1.10 sources

Sources of the optical property data. Was it measured, simulated, or taken from literature? Multiple sources should be comma-separated.

**Type:** `string`  
**Required:** Yes

## 8.4.2 opticalProperties

**Type:** `array`  
**Required:** Yes

Array of optical property values, with each item representing a different property. The array shall be sorted based on the columns starting with the first.

Columns of the table:

* Column 1: Wavelength of radiation in free-space in meters (m). The value shall be within the range of 1e-09 to 17.16e-03 (upper limit corresponds to 20 kHz).
* Column 2: Temperature of material in Kelvin (K). The value shall not be below 0.
* Column 3: Real part of index of refraction of material, which is \(n^{'}\) in \(n = n^{'} - j \kappa\).
* Column 4: Imaginary part of index of refraction of material, which is \(\kappa\) in \(n = n^{'} - j \kappa\).