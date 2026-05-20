# ASAM OpenODD® v1.0.0 — C.4 (informative) Motor vehicles in different countries example

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_c_case_studies_04_mvdc.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# C.4 (informative) Motor vehicles in different countries example

## C.4.1 Introduction

This case study shows in tabular format a vehicle passing the border between Greece and Turkey, description considering environmental data and road conditions.

The case study is about describing the COD, understanding which logical expressions could be used for the ODD definition, how do taxonomy types work for the tabular schema (such as ranges at `CategoricalLiteral` instances), and how to compare ODD and COD.

The goal was to verify that the ASAM OpenODD® supports these use cases successfully.
This was achieved through creating a taxonomy, an ODD, and validating an COD against that OOD.

## C.4.2 Taxonomy

Table 155. Example case study taxonomy in tabular form


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE | VALUE | CONCEPT\_NAME\_EN |
| --- | --- | --- | --- | --- | --- |
| country |  | Categorical |  |  | Country |
| turkey | country | CategoricalLiteral |  |  | Turkey |
| greece | country | CategoricalLiteral |  |  | Greece |
| scenery\_elements |  | Record |  |  | Scenery Elements |
| drivable\_area | scenery\_elements | Record |  |  | Drivable Area |
| drivable\_area\_lane\_specification | drivable\_area | Record |  |  | Drivable Area Lane Specification |
| lane\_type | drivable\_area\_lane\_specification | Categorical |  |  | Lane Type |
| traffic\_lane | lane\_type | CategoricalLiteral |  |  | Traffic Lane |
| emergency\_lane | lane\_type | CategoricalLiteral |  |  | Emergency Lane |
| environmental\_conditions |  | Record |  |  | Environmental Conditions |
| weather | environmental\_conditions | Record |  |  | Weather |
| wind\_speed | weather | Float | velocity |  | Wind Speed |
| wind\_level | weather | Categorical |  |  | Wind Level |
| no\_wind | wind\_level | CategoricalLiteral |  |  | No Wind |
| wind\_speed | no\_wind | UpperBound | velocity | "< 0.1 m/s" | Wind Speed Range |
| calm | wind\_level | CategoricalLiteral |  |  | Calm |
| wind\_speed | calm | Range | velocity | "[0.1 .. 0.2] m/s" | Wind Speed Range |
| light\_air | wind\_level | CategoricalLiteral |  |  | Light Air |
| wind\_speed | light\_air | Range | velocity | "[0.2 .. 1.5] m/s" | Wind Speed Range |
| light\_breeze | wind\_level | CategoricalLiteral |  |  | Light Breeze |
| wind\_speed | light\_breeze | Range | velocity | "[1.5 .. 3.3] m/s" | Wind Speed Range |
| gentle\_breeze | wind\_level | CategoricalLiteral |  |  | Gentle Breeze |
| wind\_speed | gentle\_breeze | Range | velocity | "[3.3 .. 5.4] m/s" | Wind Speed Range |
| moderate\_breeze | wind\_level | CategoricalLiteral |  |  | Moderate Breeze |
| wind\_speed | moderate\_breeze | Range | velocity | "[5.4 .. 7.9] m/s" | Wind Speed Range |
| fresh\_breeze | wind\_level | CategoricalLiteral |  |  | Fresh Breeze |
| wind\_speed | fresh\_breeze | Range | velocity | "[7.9 .. 10.7] m/s" | Wind Speed Range |
| strong\_breeze | wind\_level | CategoricalLiteral |  |  | Strong Breeze |
| wind\_speed | strong\_breeze | Range | velocity | "[10.7 .. 13.8] m/s" | Wind Speed Range |
| near\_gale | wind\_level | CategoricalLiteral |  |  | Near Gale |
| wind\_speed | near\_gale | Range | velocity | "[13.8 .. 17.1] m/s" | Wind Speed Range |
| gale | wind\_level | CategoricalLiteral |  |  | Gale |
| wind\_speed | gale | Range | velocity | "[17.1 .. 20.7] m/s" | Wind Speed Range |
| strong\_gale | wind\_level | CategoricalLiteral |  |  | Strong Gale |
| wind\_speed | strong\_gale | Range | velocity | "[20.7 .. 24.4] m/s" | Wind Speed Range |
| storm | wind\_level | CategoricalLiteral |  |  | Storm |
| wind\_speed | storm | Range | velocity | "[24.4 .. 28.4] m/s" | Wind Speed Range |
| violent\_storm | wind\_level | CategoricalLiteral |  |  | Violent Storm |
| wind\_speed | violent\_storm | Range | velocity | "[28.4 .. 32.6] m/s" | Wind Speed Range |
| hurricane\_force | wind\_level | CategoricalLiteral |  |  | Hurricane Force |
| wind\_speed | hurricane\_force | LowerBound | velocity | "> 32.6 m/s" | Wind Speed Range |
| rain | weather | Record |  |  | Rain |
| rainfall\_rate | rain | Float | precipitation\_rate |  | Rainfall Rate |
| rainfall\_intensity | rain | Categorical |  |  | Rainfall Intensity |
| no\_rain | rainfall\_intensity | CategoricalLiteral |  |  | No Rain |
| rainfall\_rate | no\_rain | UpperBound | precipitation\_rate | "⇐ 0 mm/h" | Rainfall Intensity Range |
| light\_rain | rainfall\_intensity | CategoricalLiteral |  |  | Light Rain |
| rainfall\_rate | light\_rain | Range | precipitation\_rate | "[0 .. 2.5] mm/h" | Rainfall Intensity Range |
| moderate\_rain | rainfall\_intensity | CategoricalLiteral |  |  | Moderate Rain |
| rainfall\_rate | moderate\_rain | Range | precipitation\_rate | "[2.5 .. 7.6] mm/h" | Rainfall Intensity Range |
| heavy\_rain | rainfall\_intensity | CategoricalLiteral |  |  | Heavy Rain |
| rainfall\_rate | heavy\_rain | Range | precipitation\_rate | "[7.6 .. 50] mm/h" | Rainfall Intensity Range |
| violent\_rain | rainfall\_intensity | CategoricalLiteral |  |  | Violent Rain |
| rainfall\_rate | violent\_rain | Range | precipitation\_rate | "[50 .. 100] mm/h" | Rainfall Intensity Range |
| cloudburst | rainfall\_intensity | CategoricalLiteral |  |  | Cloudburst |
| rainfall\_rate | cloudburst | LowerBound | precipitation\_rate | ">= 100 mm/h" | Rainfall Intensity Range |
| drivable\_area\_signs | drivable\_area\_lane\_specification | Record |  |  | Drivable Area Signs |
| has\_signs | drivable\_area\_signs | Boolean |  |  | Has Signs |
| sign\_types | drivable\_area\_signs | Categorical |  |  | Sign Types |
| regulatory\_signs | sign\_types | CategoricalLiteral |  |  | Regulatory Signs |
| warning\_signs | sign\_types | CategoricalLiteral |  |  | Warning Signs |
| information\_signs | sign\_types | CategoricalLiteral |  |  | Information Signs |
| dynamic\_elements |  | Record |  |  | Dynamic Elements |
| traffic\_agents | dynamic\_elements | Record |  |  | Traffic Agents |
| agent\_type | traffic\_agents | Categorical |  |  | Agent Type |
| motor\_vehicle | agent\_type | CategoricalLiteral |  |  | Motor Vehicle |
| animals | agent\_type | CategoricalLiteral |  |  | Animals |

## C.4.3 ODD

Table 156. Example case study ODD in tabular form


| MODULE\_ID | ROLE | CONTENT or CONDITION |
| --- | --- | --- |
| 1 | handle | odd\_module\_1 |
| 1 | type | odd |
| 1 | title-EN | ODD Module Example 1 |
| 1 | include\_and | lane\_type: [traffic\_lane] |
| 1 | exclude\_or | wind\_level: [light\_breeze, moderate\_breeze] |
| 1 | exclude\_or | country: [greece] |
| 1 | include\_and | rainfall\_rate: < 5 mm/s |
| 2 | handle | sign\_recognition\_module |
| 2 | type | odd |
| 2 | title-EN | Sign Recognition Module |
| 2 | exclude\_or | has\_signs: false |
| 2 | include\_and | sign\_types: [regulatory\_signs, warning\_signs, information\_signs] |
| 3 | handle | aeb\_module\_motor\_vehicles\_greece\_turkey |
| 3 | type | odd |
| 3 | title-EN | AEB Module Against Motor Vehicles in Greece and Turkey |
| 3 | include\_and | agent\_type: [motor\_vehicle] |
| 3 | include\_and | country: [greece]; country:[turkey] |
| 4 | handle | aeb\_module\_good\_weather |
| 4 | type | odd |
| 4 | title-EN | AEB Module Good Weather |
| 4 | include\_and | agent\_type: [motor\_vehicle, animals] |
| 4 | include\_and | wind\_level: ⇐ moderate\_breeze |
| 4 | include\_and | rainfall\_intensity: ⇐ moderate\_rain |
| 4 | exclude\_or | wind\_speed: > 17 m/s |
| 4 | exclude\_or | rainfall\_rate: > 7.5 mm/s |

## C.4.4 COD

Table 157. Example case study COD in tabular form


| SPATIAL\_EXTENT | country | lane\_type | wind\_speed;m/s | rainfall\_rate;mm/h | has\_signs | sign\_types | agent\_type |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 40.910968, 26.366728 | turkey | traffic\_lane | 1 | 2,6 | true | regulatory\_signs | motor\_vehicle |
| 40.912338, 26.364415 | turkey | traffic\_lane | 1,2 | 2,5 | false |  | motor\_vehicle |
| 40.913186, 26.362867 | turkey | traffic\_lane | 1,4 | 2,4 | false |  | motor\_vehicle |
| 40.914470, 26.360713 | turkey | traffic\_lane | 1,6 | 2,3 | true | warning\_signs | motor\_vehicle |
| 40.915709, 26.358528 | turkey | traffic\_lane | 1,8 | 2,2 | false |  |  |
| 40.917176, 26.356282 | turkey | traffic\_lane | 2 | 2,1 | false |  |  |
| 40.918529, 26.353946 | turkey | traffic\_lane | 2,2 | 2 | true | regulatory\_signs |  |
| 40.919836, 26.351579 | turkey | traffic\_lane | 2,4 | 1,9 | true | warning\_signs |  |
| 40.920662, 26.349849 | turkey | emergency\_lane | 2,6 | 1,8 | true | information\_signs |  |
| 40.922152, 26.347300 | turkey | emergency\_lane | 2,8 | 1,7 | false |  | motor\_vehicle |
| 40.924694, 26.343148 | turkey | emergency\_lane | 3 | 1,9 | false |  | motor\_vehicle |
| 40.926794, 26.339648 | turkey | traffic\_lane | 3,2 | 2,1 | true | warning\_signs | animals |
| 40.929084, 26.335534 | turkey | traffic\_lane | 3,4 | 2,3 | false |  |  |
| 40.930693, 26.333008 | turkey | traffic\_lane | 3,6 | 2,5 | true | information\_signs |  |
| 40.938728, 26.321875 | turkey | traffic\_lane | 3,8 | 2,7 | false |  | motor\_vehicle |
| 40.941781, 26.318628 | greece | traffic\_lane | 4 | 2,9 | true | regulatory\_signs |  |
| 40.943880, 26.316246 | greece | traffic\_lane | 4,2 | 3,1 | true | regulatory\_signs |  |
| 40.945025, 26.313287 | greece | traffic\_lane | 4,4 | 3,3 | false |  | motor\_vehicle |
| 40.945352, 26.309281 | greece | traffic\_lane | 4,6 | 3,5 | true | regulatory\_signs |  |
| 40.945461, 26.306610 | greece | emergency\_lane | 4,8 | 3,7 | true | regulatory\_signs |  |
| 40.945706, 26.303976 | greece | emergency\_lane | 5 | 3,9 | true | information\_signs | motor\_vehicle |
| 40.946006, 26.300043 | greece | traffic\_lane | 5,2 | 4,1 | false |  | motor\_vehicle |
| 40.946388, 26.294882 | greece | traffic\_lane | 5,4 | 4,3 | false |  | motor\_vehicle |
| 40.946633, 26.290949 | greece | traffic\_lane | 5,6 | 4,5 | true | warning\_signs | motor\_vehicle |
| 40.946933, 26.285824 | greece | traffic\_lane | 5,8 | 4,7 | false |  | motor\_vehicle |
| 40.947560, 26.277921 | greece | traffic\_lane | 6 | 4,9 | true | warning\_signs |  |
| 40.948078, 26.272761 | greece | traffic\_lane | 6,2 | 5,1 | false |  |  |
| 40.948378, 26.268791 | greece | traffic\_lane | 6,4 | 5,3 | true | warning\_signs |  |
| 40.948650, 26.265002 | greece | traffic\_lane | 6,6 | 5,5 | true | information\_signs |  |
| 40.948923, 26.261104 | greece | traffic\_lane | 6,8 | 5,7 | false |  |  |
| 40.949195, 26.257856 | greece | traffic\_lane | 7 | 5,9 | false |  | animals |
| 40.949413, 26.254573 | greece | traffic\_lane | 7,2 | 6,1 | true | warning\_signs |  |
| 40.949686, 26.250350 | greece | traffic\_lane | 7,4 | 6,3 | true | information\_signs |  |
| 40.949849, 26.247175 | greece | traffic\_lane | 7,6 | 6,5 | false |  |  |