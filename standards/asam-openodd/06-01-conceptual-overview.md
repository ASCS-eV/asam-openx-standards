# ASAM OpenODD v1.0.0 — §6.1 Conceptual Overview

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/06_model_concept/06_01_openodd_model.html
> **Standard**: ASAM OpenODD Base Standard 1.0.0 Specification, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2025-05-19

---

## 6.1.9 Module Decomposition Patterns

### 6.1.9.1 Basic use case decomposition

Use case decomposition is applicable to top-level specification of an ODD. Instead of specifying all use cases in a single model, this pattern is applied to have a single top-level module that lists all use cases. Each use case is represented by one or more use case modules.

```
ODD_sample_v1.01.23 is
    INCLUDE_OR when
        ucm_passenger_pickup is true
        ucm_city_street_driving is true
        ucm_highway_driving is true
        ucm_passenger_dropoff is true
        ucm_self_parking is true

ucm_passenger_pickup is
    INCLUDE_OR when
        ...
```

The module's semantic interpretation:
- A situation is included in the ODD if it is included in one of the use case modules listed in the `INCLUDE_OR` section.
- A situation is excluded if it is not allowed in **all** listed modules.

The classification of the use case applicable to each situation is either:
- based on sensors external to the ADS (e.g., weather conditions), or
- based on internal ADS signals originating from an on-board planning component.

### 6.1.9.2 Cartesian product decomposition

A more complicated requirement involves specifying a collection of use cases that represent all possible combinations of components. The `AND-OR` nesting pattern avoids specifying all combinations explicitly:

```
ODD_sample_v1.01.23 is
    INCLUDE_AND when
        OR
            passenger_pickup is true
            city_street_driving is true
            highway_driving is true
            passenger_dropoff is true
            self_parking is true
        OR
            normal_operation_hours is true
            emergency_pickup_to_hospital is true
            special_event_charter is true
        city is
            hanover
            munich
        positioning is
            global_positioning_system
            local_positioning_beacon
```

Key points:
- Use a top-level `INCLUDE_AND`
- Use nested `OR` for each cartesian product component
- The `INCLUDE_AND` section can contain zero or more `OR` sub-sections
- The `INCLUDE_OR` section can contain zero or more `AND` sub-sections

### 6.1.9.3 Taxonomy based decomposition

Restriction of concepts used in conditions to concepts of a taxonomy subtree. This avoids unmanageable combinatorics.

```
passenger_pickup is
    INCLUDE_AND when
        acceptable_weather is true
        supported_scenery is true

acceptable_weather is
    INCLUDE_AND when
        acceptable_lighting is true
        acceptable_rainfall is true
        acceptable_wind is true

supported_scenery is
    INCLUDE_AND when
        acceptable_road_conditions
        acceptable_intersection_conditions
```

### 6.1.9.4 Conditional include and exclude

Linking inclusion criteria to conditions. Example: speed on rural roads > 70 km/h only if lane markings are solid:

```
ucm_rural_capabilities is
    INCLUDE_AND when
        road_type equals rural
        OR
            lane_solid_speed_limit is true
            lane_all_speed_limit is true

lane_solid_speed_limit is
    INCLUDE_AND when
        lane_marker equals solid
        speed_allowed is greater than 70 km/h

lane_all_speed_limit is
    INCLUDE_AND when
        speed_allowed is less than 70 km/h
```

### 6.1.9.5 Shared include and exclude sub-condition

Modeling capabilities with specific shared sub-conditions. Pattern:
- Define a top-level module with `INCLUDE_AND`
- Specify shared conditions in the `INCLUDE_AND` section
- Add an `OR` sub-section for non-shared components
- Specify overall exclusion in the `EXCLUDE_AND` section

### 6.1.9.6 Extensible label disjunction

Enables extending a collection of modules without modifying previously defined conditions:

```
passenger_pickup is
    INCLUDE_AND when
        supported_pickup_locations is true
    EXCLUDE_OR when
        hazardous_conditions is true

pickup_locations_group1 is
    LABEL is supported_pickup_locations
    INCLUDE_AND when
        street_section in main_st_sec1, main_st_sec2

too_much_rain is
    LABEL is hazardous_conditions
    INCLUDE_AND when
        rain_rate equals heavy_rain

icy_road_conditions is
    LABEL is hazardous_conditions
    INCLUDE_AND when
        road_surface_condition equals black_ice
```

Key benefits:
- Additional modules can be added to satisfy labels without modifying existing modules
- Labels evaluate to `true` when ANY module with that label evaluates to `true`

### 6.1.9.7 Implicit include

Use `EXCLUDE` to specify a few excluded items, implicitly including all others:

```
acceptable_weather is
    EXCLUDE_OR when
        rain_type equals toroidal_rain
```

### 6.1.9.8 Implicit exclude

Use `INCLUDE` to specify a few included items, implicitly excluding all others:

```
acceptable_weather is
    INCLUDE_OR when
        rain_level equals no_rain
```

### 6.1.9.9 Negated module

Reusable exclusions. Define a module that captures "bad conditions" and reference it via label in EXCLUDE sections.
