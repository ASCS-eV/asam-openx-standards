# ASAM OpenODD® v1.0.0 — C.5 (informative) Multiple lane low speed example

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_c_case_studies_05_mlls.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# C.5 (informative) Multiple lane low speed example

## C.5.1 Introduction

This case study shows in tabular format a vehicle driving in Germany considering environmental data..

The case study is about describing the COD, understanding which logical expressions could be used for the ODD definition, how do taxonomy types work for the tabular schema (such as ranges at `CategoricalLiteral` instances), and how to compare ODD and COD.

The goal was to verify that the ASAM OpenODD® supports these use cases successfully.
This was achieved through creating a taxonomy, an ODD, and validating an COD against that OOD.

## C.5.2 Taxonomy

Table 158. Example case study taxonomy in tabular form


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE | EXPRESSION | CONCEPT\_NAME\_EN |
| --- | --- | --- | --- | --- | --- |
| country |  | categorical |  |  | Country |
| Germany | country | categorical\_literal |  |  | Germany |
| USA | country | categorical\_literal |  |  | United States of America |
| Japan | country | categorical\_literal |  |  | Japan |
| scenery |  | record |  |  | Scenery |
| zones | scenery | record |  |  | Zones |
| fixed\_zone\_types | zones | categorical |  |  | Fixed Zone Types |
| school\_zone | fixed\_zone\_types | categorical\_literal |  |  | School Zone |
| residential\_zone | fixed\_zone\_types | categorical\_literal |  |  | Residential Zone |
| lane\_specifications | scenery | record |  |  | Lane Specifications |
| number\_of\_left\_lanes | lane\_specifications | int |  |  | Number Of Left Lanes |
| number\_of\_right\_lanes | lane\_specifications | int |  |  | Number Of Right Lanes |
| subject\_vehicle |  | record |  |  | Subject Vehicle |
| speed | subject\_vehicle | float | velocity |  | Speed |
| environmental\_conditions |  | record |  |  | Environmental Conditions |
| wind\_speed | environmental\_conditions | float | velocity |  | Wind Speed |
| snowfall\_present | environmental\_conditions | boolean |  |  | Snowfall Present |

## C.5.3 ODD

Table 159. Example case study ODD in tabular form


| MODULE\_ID | ROLE | CONTENT or CONDITION |
| --- | --- | --- |
| 1 | handle | no\_snow\_module |
| 1 | type | odd |
| 1 | references | taxonomy |
| 1 | title-EN | No Snow Module |
| 1 | exclude\_and | snowfall\_present: true |
| 2 | handle | multiple\_lane\_low\_speed\_module |
| 2 | type | odd |
| 2 | references | taxonomy |
| 2 | title-EN | Multiple Lane Low Speed Module |
| 2 | include\_and | number\_of\_right\_lanes: > 1 |
| 2 | include\_and | speed: < 60 km/h |
| 3 | handle | specific\_module\_example\_1 |
| 3 | type | odd |
| 3 | references | taxonomy |
| 3 | title-EN | Specific Module Example 1 |
| 3 | include\_and | no\_snow\_module |
| 3 | include\_and | multiple\_lane\_low\_speed\_module |
| 3 | exclude\_and | wind\_speed: > 15 km/h |
| 3 | exclude\_and | fixed\_zone\_types: [school\_zone] |
| 4 | handle | specific\_module\_example\_2 |
| 4 | type | odd |
| 4 | references | taxonomy |
| 4 | title-EN | Specific Module Example 2 |
| 4 | include\_or | snowfall\_present: true |
| 4 | include\_or | wind\_speed: > 15 km/h |
| 4 | include\_or | fixed\_zone\_types: [school\_zone]; country: [Germany] |

## C.5.4 COD

Table 160. Example case study COD in tabular form


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | speed;km/h | wind\_speed;km/h | snowfall\_present | country | fixed\_zone\_types | number\_of\_right\_lanes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | "2024-09-12 12:00:00" | "52.5200, 13.4050" | 35 | 12 | false | Germany | residential\_zone | 2 |
| 2 | "2024-09-12 12:00:10" | "52.5198, 13.4060" | 38 | 13 | false | Germany | residential\_zone | 2 |
| 3 | "2024-09-12 12:00:20" | "52.5196, 13.4070" | 40 | 12 | false | Germany | residential\_zone | 2 |
| 4 | "2024-09-12 12:00:30" | "52.5194, 13.4080" | 42 | 14 | false | Germany | residential\_zone | 2 |
| 5 | "2024-09-12 12:00:40" | "52.5192, 13.4090" | 43 | 13 | false | Germany | residential\_zone | 2 |
| 6 | "2024-09-12 12:00:50" | "52.5190, 13.4100" | 42 | 12 | false | Germany | residential\_zone | 2 |
| 7 | "2024-09-12 12:01:00" | "52.5188, 13.4110" | 43 | 12 | false | Germany | residential\_zone | 2 |
| 8 | "2024-09-12 12:01:10" | "52.5186, 13.4120" | 40 | 13 | false | Germany | residential\_zone | 2 |
| 9 | "2024-09-12 12:01:20" | "52.5184, 13.4130" | 35 | 13 | false | Germany | residential\_zone | 1 |
| 10 | "2024-09-12 12:01:30" | "52.5182, 13.4140" | 30 | 12 | false | Germany | residential\_zone | 1 |
| 11 | "2024-09-12 12:01:40" | "52.5180, 13.4150" | 23 | 13 | false | Germany | residential\_zone | 1 |
| 12 | "2024-09-12 12:01:50" | "52.5178, 13.4160" | 24 | 14 | false | Germany | residential\_zone | 1 |
| 13 | "2024-09-12 12:02:00" | "52.5176, 13.4170" | 25 | 12 | false | Germany | residential\_zone | 1 |
| 14 | "2024-09-12 12:02:10" | "52.5174, 13.4180" | 26 | 13 | false | Germany | residential\_zone | 1 |
| 15 | "2024-09-12 12:02:20" | "52.5172, 13.4190" | 28 | 12 | false | Germany | residential\_zone | 1 |