# ASAM Openodd v1.0.0 — C.3 (informative) Automated lane keeping system example

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_c_case_studies_03_alks.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# C.3 (informative) Automated lane keeping system example

## C.3.1 Introduction

This case study shows an example in YAML format.
This case study for Automated Lane Keeping System (ALKS) was created by collecting the ODD-related statements from UNECE R157 [[15](../bibliography.html#bib-unecer157)].
Many of the attributes were missing in ISO 34503 [[4](../bibliography.html#bib-iso34503)] taxonomy and also BSI PAS 1883 [[16](../bibliography.html#bib-pas1883)] so a taxonomy file is created (see [Code 227](#code-case-study-alks-taxonomy-yaml)).
The COD is also created in YAML format.

UN Regulation No. 157 [[15](../bibliography.html#bib-unecer157)] is a regulatory document for an Automated Lane Keeping Systems (ALKS).
This regulation outlines the safety requirements, fallback mechanisms and also conditions under which the ALKS shall operate.
For example, one of the paragraphs of UN Regulation No. 157 [[15](../bibliography.html#bib-unecer157)] that is clearly specifying ODD for ALKS is as follows:
“ALKS can be activated under certain conditions on roads where pedestrians and cyclists are prohibited and which, by design, are equipped with a physical separation that divides the traffic moving in opposite directions and prevent traffic from cutting across the path of the vehicle.
In a first step, the original text of this Regulation limits the operational speed to 60 km/h maximum and passenger cars (M1 vehicles).”

We collected all ODD-related statements form UN Regulation No. 157 and created this case study.
Since many of the attributes mentioned in UN Regulation No. 157 were missing in ISO 34503 [[4](../bibliography.html#bib-iso34503)], we started by creating a taxonomy and then creating the ODD that is implied from ALKS regulations.

The goal is two-fold.
First, to show how regulations can impact ODD specification.
For example, when regulation specifies absence of pedestrians as a precondition for activation of the system, it shall be reflected in ODD specification file.
Secondary goal is to show that sometimes the taxonomy in current standards need to be extended to be able to specify ODDs.

## C.3.2 Taxonomy

Code 227. Example case study taxonomy (YAML) - file ALKS\_taxonomy.yaml

```
TAXONOMY:
    scenery_elements:
        drivable_area:
            drivable_area_type:
                - motorway
                - primary_road
                - local_road
            solid_barriers: boolean            # Not defined in ISO 34503
        drivable_area_lane_specification:
            lane_marking: boolean
            number_of_lane: integer count      # Not defined in ISO 34503
        junction:
            t_junction: boolean
            y_junction: boolean
            grade_separation: boolean          # Not defined in ISO 34503
        temporary_drivable_area_structure:
            construction_site_detour: boolean
    dynamic_elements:
        traffic_agent:
            emergency_vehicle: boolean
            small_obstacle: boolean            # Not defined in ISO 34503
        subject_vehicle:
            operational_speed: float velocity  # Not defined in ISO 34503
            power_supply: boolean              # Not defined in ISO 34503
            braking_system: boolean            # Not defined in ISO 34503
            tire_pressure: boolean             # Not defined in ISO 34503
            self_check_system: boolean         # Not defined in ISO 34503
```

## C.3.3 ODD

Code 228. Example case study ODD (YAML)

```
IMPORT:
    - ALKS_taxonomy.yaml

ODD:
    odd_main_module:
        TITLE: ODD for ALKS system based on UNECE R157
        INCLUDE_AND:
            drivable_area_type: motorway
            solid_barriers: true
            lane_marking: visible
            number_of_lane: ">= 2"
            t_junction: false
            y_junction: false
            grade_separation: true
            construction_site_detour: false
            operational_speed: "< 60 km/h" # Without Lane Change Procedure
            subject_vehicle_module: true
            dynamic_traffic_module: true

MODULES:
    subject_vehicle_module:
        TITLE: Internal attributes of the subject vehicle
        INCLUDE_AND:
            power_supply: true
            braking_system: true
            tire_pressure: true
            self_check_system: true

    dynamic_traffic_module:
        TITLE: Traffic attributes of the operational domain
        INCLUDE_AND:
            emergency_vehicle: false
            small_obstacle: false
```

## C.3.4 COD

Code 229. Example case study COD (YAML)

```
COD:
  - TEMPORAL_EXTENT:                        "2024-06-01 08:12:53.784"
    SPATIAL_EXTENT:                         "48.0232 11.7153"
    drivable_area_type;categorical_literal: motorway
    solid_barriers;boolean:                 true
    lane_marking;boolean:                   true
    number_of_lane;count:                   2
    t_junction;boolean:                     false
    y_junction;boolean:                     false
    grade_separation;boolean:               true
    construction_site_detour;boolean:       false
    emergency_vehicle;boolean:              false
    small_obstacle;boolean:                 false
    maximum_operational_speed;km/h:         90.5
    power_supply;boolean:                   true
    braking_system;boolean:                 true
    tire_pressure;boolean:                  true
    self_check_system;boolean:              true
```