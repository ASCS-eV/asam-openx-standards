# ASAM Openmaterial 3D latest — 8.6 Material reflection coefficient schema

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/08_material/material-reflection-coefficient-schema.html
> **Standard**: ASAM Openmaterial 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.6 Material reflection coefficient schema

## 8.6.1 metadata

Metadata about the material.

**Type:** `object`  
**Required:** Yes

### 8.6.1.1 name

The display name of the material, such as 'Red brick' or 'Dark asphalt'.

**Type:** `string`  
**Required:** Yes

### 8.6.1.2 description

Short description of the material in 2 - 3 sentences.

**Type:** `string`  
**Required:** Yes

### 8.6.1.3 uuid

Universally unique identifier for the material in 8-4-4-4-12 format, see [[12](../bibliography.html#bib-uui)]. The uuid stays the same, even if version is updated.

**Type:** `string`  
**Pattern:** `\\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\\b$`  
**Required:** Yes

### 8.6.1.4 materialVersion

The version number of the material, following semantic versioning (for example, '1.0.0').

**Type:** `string`  
**Pattern:** `^\\d+\\.\\d+\\.\\d+$`  
**Required:** Yes

### 8.6.1.5 openMaterial3dVersion

The version of the ASAM OpenMATERIAL 3D specification used, adhering to semantic versioning (for example, '1.0.0').

**Type:** `string`  
**Pattern:** `^\\d+\\.\\d+\\.\\d+$`  
**Required:** Yes

### 8.6.1.6 copyrights

Indicates copyright details, including the year and copyright holder (e.g., '© 2024 ACME Inc.').

**Type:** `array`  
**Required:** Yes

### 8.6.1.7 license

Describes the license for material distribution. Use an SPDX identifier for open-source licenses (for example, 'MIT'), or provide a URL or filename for proprietary licenses.

**Type:** `string`  
**Required:** Yes

### 8.6.1.8 authors

Lists the author(s) of the material as a name, email, or company.

**Type:** `array`  
**Required:** Yes

### 8.6.1.9 creationDate

The date and time of material creation, formatted as YYYYMMDDTHHMMSSZ according to ISO 8601 [[8](../bibliography.html#bib-iso8601)] (for example, '20240703T101728Z').

**Type:** `string`  
**Pattern:** `^\\d{8}T\\d{6}Z$`  
**Required:** Yes

### 8.6.1.10 sources

Sources of the reflection coefficient data. Was it measured, simulated, or taken from literature? Multiple sources should be comma-separated.

**Type:** `string`  
**Required:** Yes

## 8.6.2 reflectionCoefficient

Reflection coefficient lookup table including relevant meta data. The reflection coefficient is defined as the ratio of amplitudes of the reflected electromagnetic wave over the incident electromagnetic wave \(r = E\_{\textrm{r}} / E\_{\textrm{i}}\). This complex value is represented by angle- and wavelength-dependent magnitude and phase values.

**Type:** `object`  
**Required:** Yes

### 8.6.2.1 wavelengths

List of all wavelengths in meters contained in the lookup table. The wavelength values shall be within the range of 1e-09 to 17.16e-03 (upper limit corresponds to 20 kHz).

**Type:** `array`  
**Required:** Yes

### 8.6.2.2 lookupTable

Array of reflection coefficient values, with each item representing a different property. The array shall be sorted based on the columns starting with the first.

**Type:** `array`  
**Required:** Yes

Columns of the table:

* Column 1: Wavelength of radiation in free-space in meters (m). The value shall be within the range of 1e-09 to 17.16e-03 (upper limit corresponds to 20 kHz).
* Column 2: Incident zenith angle relative to the surface normal in rad. It shall be within a range of \(0\) to \(\pi/2\).
* Column 3: Exit zenith angle relative to the surface normal in rad. It shall be within a range of \(0\) to \(\pi/2\).
* Column 4: Exit azimuth angle in rad. It shall be within a range of \(0\) to \(2 \pi\). The value is relative to the incident azimuth angle. The incident azimuth angle is set to 0° as the incident ray is used as reference.
* Column 5: Polarized plane angle in rad. This is the angle between the plane containing the incident, exit, and normal vector, and the plane of polarization. The plane of polarization contains the direction of propagation and the electric vector. The value shall be within a range of \(0\) to \(\pi\).
* Column 6: Magnitude within the linearly polarized plane. The magnitude is given as an absolute relative value compared to an ideal reflector. The value shall be between 0 and 1
* Column 7: Phase within the linearly polarized plane. It shall be within a range of \(-\pi\) to \(\pi\). If the phase is not taken into account, it is null.