# ASAM Openodd v1.0.0 — C.6 (informative) Multiple intersections example

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_c_case_studies_06_intersections.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# C.6 (informative) Multiple intersections example

## C.6.1 Introduction

The content of this issue includes the tree major assets of the ASAM OpenODD model: taxonomy, COD, and ODD (modules).

## C.6.2 Taxonomy

We have represented ISO 34503 [[4](../bibliography.html#bib-iso34503)] taxonomy in YAML notation, see  [Annex B.3, *YAML ISO 34503*](11_e_iso34503_03_yaml.html#top-example-iso34503-yaml).
There are some small changes, commented with `newly added for value ranges` to make the taxonomy machine-processable.

In the following examples we have used a different taxonomy because the ISO 34503 [[4](../bibliography.html#bib-iso34503)] taxonomy is only defining a limited, brief aspect of the world.
Nevertheless the taxonomy concepts in the example should be self-explaining.

## C.6.3 COD

We derived three CODs from reality focusing on scenery elements only:

Table 161. Example case study CODs


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | junction\_feature;categorical\_literal | merge\_section\_junction;boolean | departure\_section\_junction;boolean | lane\_type;categorical\_literal | restricted\_lane;categorical\_literal | road\_marking\_edge\_is\_existing;categorical\_literal | road\_marking\_lane\_is\_existing;boolean | on\_street\_parking\_type;categorical\_literal | on\_street\_parking\_feature;categorical\_literal | number\_of\_lanes\_in\_subject\_vehicle\_direction;count | lane\_protection;categorical\_literal | regulatory\_sign;categorical\_literal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 01.06.2024 12:00:00 | 53.578821, 9.988865 | simple | false | true | go\_straight, straight+left, straight+right, left+right, left | Bicycle | existing | true |  |  | [1 .. 2] | protected | right\_of\_way, road\_usage |
| 2 | 01.06.2024 12:00:00 | 53.570141, 10.027062 | channelized, flared | true | true | go\_straight, right, straight+left, straight+right | Bus | not\_existing | true | parallel\_parking\_on\_one\_side | off\_curb | [2 .. 5] | protected | right\_of\_way, road\_usage |
| 3 | 01.06.2024 12:00:00 | 53.573275, 9.999399 | simple | false | true | straight+right, straight+left, right+left, straight+right+left |  | existing | false |  |  | 1 | unprotected | right\_of\_way, road\_usage |

## C.6.4 ODD (module)

Based on these COD we have build the use case module in [Code 230](#code-case-study-intersection-yaml) to define suitable intersections.
All of the three intersections are suitable but differ in terms of complexity and special features.

Code 230. Example case study use case module (YAML)

```
IMPORT:
    - VWG_taxonomy.yml

MODULE:
    ucm_intersection:
        TITLE: use case all intersections
        DESCRIPTION: this is the use case module combining all variants of suitable intersections
        INCLUDE_AND:
            intersection_generic: true
            OR:
                intersection_small: true
                intersection_large: true
            OR:
                intersection_with_restricted_lane: true
                intersection_with_parking_lane: true

    intersection_generic:
        TITLE: generic intersections in Hamburg # based on the three COD examples
        LABELS:
            - intersections
        INCLUDE_AND:
            number_of_road_links: "< 6"
            junction_feature:
                - simple
                - flared
                - channelized
            merge_section_junction: [false, true]
            departure_section_junction: true
            lane_type:
                - go straight
                - straight+left
                - straight+right
                - straight+right+left
                - left+right
                - left
                - right
            road_marking_edge_is_existing: [false, true]
        EXCLUDE_OR:
            number_of_levels_junction: "> 1"

    intersection_with_restricted_lane:
        TITLE: generic intersections extended by restricted lanes
        LABELS:
            - intersections
        TAGS:
            - special_case
        INCLUDE_AND:
            intersection_generic: true
            restricted_lane:
                - unknown
                - bus
                - bicycle

    intersection_with_parking_lane:
        TITLE: generic intersections extended by parking possibilities
        LABELS:
            - intersections
        TAGS:
            - special_case
        INCLUDE_AND:
            intersection_generic: true
            on_street_parking_type:
                - unknown
                - parallel_parking_on_one_side
            on_street_parking_feature:
                - unknown
                - off_curb

    intersection_small:
        TITLE: small generic intersections
        LABELS:
            - intersections
        INCLUDE_AND:
            intersection_generic: true
            number_of_lanes_in_subject_vehicle_direction: "< 2"
            lane_protection:
                - protected_lane
                - unprotected_lane
            road_marking_lane_is_existing: [false, true]

    intersection_large:
        TITLE: large generic intersections
        LABELS:
            - intersections
        INCLUDE_AND:
            intersection_generic: true
            number_of_lanes_in_subject_vehicle_direction: "> 1"
            lane_protection:
                - protected_lane
            road_marking_lane_is_existing: true
            regulatory_sign:
                - right_of_way_sign
```

The first module `ucm_intersection` is a use case module that can be accompanied with a lot of additional use cases such as roundabouts, various road types and so on.
All of them will be used in a top-level ODD definition.

The use case module incorporates the definition of intersections in general and additional conditional statements , for example, regarding intersection size.
To be able to handle large intersections, traffic lights and road markings are necessary, but this is not necessary for smaller ones.

Additionally special cases are added to cover, for example, restricted lanes or parking close to the intersections.

The generic intersection module is included both in the use case module and included in the special cases.
This seems to be done twice but this is done to avoid that the special cases are accidentally used "outside" the context of an intersection.
Additionally the generic module do not have to be mentioned a second time in the use case module in the second `OR` subsection.