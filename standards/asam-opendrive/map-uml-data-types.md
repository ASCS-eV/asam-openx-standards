# ASAM Opendrive v1.9.0 — Annex B (normative): Data types

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/map_uml_data_types.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex B (normative): Data types

## B.1 Core

### B.1.1 e\_unit

Table 207. e\_unit


| Type | Relations |
| --- | --- |
| `union` | [e\_unitDistance](enumerations/map_uml_enumerations.html#top-EAID_00C01E54_46BF_4ad3_879B_3D03570EA74D)  [e\_unitSpeed](enumerations/map_uml_enumerations.html#top-EAID_491DC05E_01C6_49b3_83BE_A06DD81F9C35)  [e\_unitMass](enumerations/map_uml_enumerations.html#top-EAID_8485C23B_4024_4a69_8628_CC0E106B3384)  [e\_unitSlope](enumerations/map_uml_enumerations.html#top-EAID_16B12C77_9C6E_4b8f_82A9_A135230A0A4F) |

### B.1.2 t\_grEqZero

Table 208. t\_grEqZero


| Type | Restriction |
| --- | --- |
| `double` | [0,∞[ |

### B.1.3 t\_grEqZeroOrContactPoint

Table 209. t\_grEqZeroOrContactPoint


| Type | Restriction |
| --- | --- |
| `double` | start ; end ; [0,∞[ |

### B.1.4 t\_grZero

Table 210. t\_grZero


| Type | Restriction |
| --- | --- |
| `double` | ]0,∞[ |

### B.1.5 t\_zeroOne

Table 211. t\_zeroOne


| Type | Restriction |
| --- | --- |
| `double` | [0;1] |

## B.2 Road

### B.2.1 e\_countryCode

Table 212. e\_countryCode


| Type | Restriction |
| --- | --- |
| `string` | [A-Z]{2} |

### B.2.2 t\_maxSpeed

Table 213. t\_maxSpeed


| Type | Restriction |
| --- | --- |
| `e_maxSpeedString` | no limit ; undefined ; [0,∞[ |