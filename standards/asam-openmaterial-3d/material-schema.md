# ASAM OpenMATERIAL® 3D latest — 8.2 Material schema

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/08_material/material-schema.html
> **Standard**: ASAM OpenMATERIAL® 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.2 Material schema

## 8.2.1 metadata

The key meta information about the material properties.

**Type:** `object`  
**Required:** Yes

### 8.2.1.1 name

The display name of the material, such as 'Red brick' or 'Dark asphalt'.

**Type:** `string`  
**Required:** Yes

### 8.2.1.2 description

Short description of the material in 2 - 3 sentences.

**Type:** `string`  
**Required:** No

### 8.2.1.3 uuid

Universally unique identifier for the material in 8-4-4-4-12 format, see [[12](../bibliography.html#bib-uui)]. The uuid stays the same, even if version is updated.

**Type:** `string`  
**Pattern:** `\\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\\b$`  
**Required:** Yes

### 8.2.1.4 materialVersion

The version number of the material, following semantic versioning (for example, '1.0.0').

**Type:** `string`  
**Pattern:** `^\\d+\\.\\d+\\.\\d+$`  
**Required:** Yes

### 8.2.1.5 openMaterial3dVersion

The version of the ASAM OpenMATERIAL® 3D specification used, adhering to semantic versioning (for example, '1.0.0').

**Type:** `string`  
**Pattern:** `^\\d+\\.\\d+\\.\\d+$`  
**Required:** Yes

### 8.2.1.6 copyrights

Indicates copyright details, including the year and copyright holder (for example, '© 2024 ACME Inc.').

**Type:** `array`  
**Required:** Yes

### 8.2.1.7 license

Describes the license for material distribution. Use an SPDX identifier for open-source licenses (for example, 'MIT'), or provide a URL or filename for proprietary licenses.

**Type:** `string`  
**Required:** Yes

### 8.2.1.8 authors

Lists the author(s) of the material as a name, email, or company.

**Type:** `array`  
**Required:** Yes

### 8.2.1.9 creationDate

The date and time of material creation, formatted as YYYYMMDDTHHMMSSZ according to ISO 8601 [[8](../bibliography.html#bib-iso8601)] (for example, '20240703T101728Z').

**Type:** `string`  
**Pattern:** `^\\d{8}T\\d{6}Z$`  
**Required:** No

## 8.2.2 materialProperties

Properties related to the material.

**Type:** `object`  
**Required:** Yes

### 8.2.2.1 surfaceRoughness

Information about the surface roughness of the material.

**Type:** `object`  
**Required:** No

#### 8.2.2.1.1 surfaceHeightRms

Root mean square of surface height deviations, called RMS-Roughness, being a vertical measure of roughness and given in meters (m).

**Type:** `number`  
**Minimum value:** `0`  
**Required:** Yes

#### 8.2.2.1.2 surfaceCorrelationLength

Correlation length of the surface height deviations, being the distance after autocorrelation function has dropped to 1/e. Thus being a horizontal measure of roughness and given in meters.

**Type:** `number`  
**Minimum value:** `0`  
**Required:** Yes

#### 8.2.2.1.3 sources

Sources of the surface roughness data. Multiple sources should be comma-separated.

**Type:** `string`  
**Required:** Yes

### 8.2.2.2 emissivityData

Emissivity data of the material.

**Type:** `object`  
**Required:** No

#### 8.2.2.2.1 emissivityCoefficient

Emissivity describes the ability to emit energy as thermal radiation. Given as the fraction of thermal radiation emitted by a surface relative to the radiation emitted by an ideal black body at the same temperature. Here the hemispherical total emissivity is used which considers full emission over all wavelengths, directions and polarization for a given particular temperature: ε(T).

**Type:** `number`  
**Minimum value:** `0`  
**Maximum value:** `1`  
**Required:** Yes

#### 8.2.2.2.2 temperature

Temperature of material in Kelvin (K) at which the emissivity is measured.

**Type:** `number`  
**Minimum value:** `0`  
**Required:** Yes

#### 8.2.2.2.3 sources

Sources of the emissivity data. Multiple sources should be comma-separated.

**Type:** `string`  
**Required:** Yes

### 8.2.2.3 elasticityData

Information about the elasticity of the material.

**Type:** `object`  
**Required:** No

#### 8.2.2.3.1 youngsModulus

Young’s modulus of the material in Pascal (Pa). The value shall be in the range of 0 to 1.5e12 Pa (Young’s modulus of a diamond)

**Type:** `number`  
**Minimum value:** `0`  
**Maximum value:** `1500000000000`  
**Required:** Yes

#### 8.2.2.3.2 poissonsRatio

Poisson’s ratio of the material.

**Type:** `number`  
**Minimum value:** `-1`  
**Maximum value:** `0.5`  
**Required:** Yes

#### 8.2.2.3.3 sources

Sources of the elasticity data. Multiple sources should be comma-separated.

**Type:** `string`  
**Required:** Yes

### 8.2.2.4 densityData

Information about the density of the material.

**Type:** `object`  
**Required:** No

#### 8.2.2.4.1 density

Density of the material in kg/m3. The value shall be in the range of 0 to 25000 (density of Osmium)

**Type:** `number`  
**Minimum value:** `0`  
**Maximum value:** `25000`  
**Required:** Yes

#### 8.2.2.4.2 sources

Sources of the density data. Multiple sources should be comma-separated.

**Type:** `string`  
**Required:** Yes

### 8.2.2.5 retroreflectivityData

Information about the retro-reflective properties of the material in the visible light spectrum.

**Type:** `object`  
**Required:** No

#### 8.2.2.5.1 coefficientOfRetroreflection

Coefficient of retro-reflection in candela per lux per square metre (cd lx-1 m-2).

**Type:** `number`  
**Minimum value:** `0`  
**Maximum value:** `5000`  
**Required:** Yes

#### 8.2.2.5.2 sources

Sources of the retro-reflectivity data. Multiple sources should be comma-separated.

**Type:** `string`  
**Required:** Yes

### 8.2.2.6 electromagneticPropertiesUri

Relative path to a property lookup table file with electromagnetic material properties.

**Type:** `string`  
**Pattern:** `.*_emp\\.xompt$`  
**Required:** No

### 8.2.2.7 opticalPropertiesUri

Relative path to a property lookup table file with optical material properties.

**Type:** `string`  
**Pattern:** `.*_optical\\.xompt$`  
**Required:** No

### 8.2.2.8 brdfUris

Relative paths to one or multiple property lookup table files with wavelength-dependent bidirectional reflectance distribution functions.

**Type:** `array`  
**Required:** No

### 8.2.2.9 reflectionCoefficientUris

Relative paths to one or multiple property lookup table files with wavelength-dependent reflection coefficient values.

**Type:** `array`  
**Required:** No

### 8.2.2.10 customProperties

Non-standardized material properties for custom tools or tool chains.

**Type:** `object`  
**Required:** No