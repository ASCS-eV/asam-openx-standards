# ASAM Openodd v1.0.0 — D.3 Tabular Format weather COD

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_d_further_examples_03_weather_cod.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# D.3 Tabular Format weather COD

## D.3.1 Introduction

This is an illustrative example for COD comprising weather information recorded at single point location.

## D.3.2 COD Specification without manifest

The recorded data can be specified using tabular format specification as shown in [Table 166](#tab-recorded-data).

Table 166. Example for recorded data


| TemporalExtent;datetime | SpatialExtent;shp | AirTemp;K | Wind;m/s | Rainfall;mm/hr | MOR;m |
| --- | --- | --- | --- | --- | --- |
| 20/10/2022 05:00 | <single point geo-coordinate> | 287.7 | 2.9 | 0.007 | 10000 |

## D.3.3 COD Specification using manifest

Alternatively, if the recorded data is available already in a tabular form (for example, csv), the COD data can be specified as manifest file, see [Table 167](#tab-tabular-manifest), as defined by the tabular format specification.

Table 167. Example for tabular manifest


| FieldID | FileName | Type | Column | Unit | TaxonomyID | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| 001 | iso34503.csv | taxonomy |  |  |  | Refers to ISO 34503 taxonomy |
| 002 | ASAM\_OpenODD\_WP9\_rain\_V1.csv | cod | AirTemp | K | air\_temperature | The ambient air temperature (mean value over 1 minute). To convert to deg C, subtract 273.15. Recorded during intense period of rainfall. |
| 003 | ASAM\_OpenODD\_WP9\_rain\_V1.csv | cod | Wind | m/s | wind | The mean wind speed (evaluated over 1 minute). Recorded during intense period of rainfall |
| 004 | ASAM\_OpenODD\_WP9\_rain\_V1.csv | cod | Rainfall | mm/hr | rainfall | The mean rainfall intensity as might be measured by a rain gauge at a single point, evaluated over 1 minute. Recorded during intense period of rainfall |
| 005 | ASAM\_OpenODD\_WP9\_rain\_V1.csv | cod | MOR | m | visibility | The visibility expressed as "Meteorological Optical Range" (MOR). When provided in WP in the WP9, it should be interpreted as the visibility due to fog. Recorded during intense period of rainfall |
| 006 | ASAM\_OpenODD\_WP9\_fog\_V1.csv | cod | AirTemp | K | air\_temperature | The ambient air temperature (mean value over 1 minute). To convert to deg C, subtract 273.15. Recorded during fog event |
| 007 | ASAM\_OpenODD\_WP9\_fog\_V1.csv | cod | Wind | m/s | wind | The mean wind speed (evaluated over 1 minute). Recorded during fog event |
| 008 | ASAM\_OpenODD\_WP9\_fog\_V1.csv | cod | Rainfall | mm/hr | rainfall | The mean rainfall intensity as might be measured by a rain gauge at a single point, evaluated over 1 minute. Recorded during fog event |
| 009 | ASAM\_OpenODD\_WP9\_fog\_V1.csv | cod | MOR | m | visibility | The visibility expressed as "Meteorological Optical Range" (MOR). When provided in WP in the WP9, it should be interpreted as the visibility due to fog. Recorded during fog event |