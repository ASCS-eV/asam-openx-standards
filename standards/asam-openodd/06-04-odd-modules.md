# ASAM OpenODD v1.0.0 — §6.4 ODD Modules

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/06_model_concept/06_04_openodd_modules.html
> **Standard**: ASAM OpenODD Base Standard 1.0.0 Specification, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2025-05-19

---

## 6.4.3.1 Condition specification

Conditions are used to determine which situations are inside the ODD, and which are outside, whereby individual situations are described using CODs, and aggregate situations are described using an OD.

Class `Condition` contains the following fields:

- **Description** field: An array of values of type `LangString` where each value contains a string to represent the description, and to reference a language by using an ISO 639 with two characters. Each language shall have a single translation. At least an English description shall be provided.

- **Comment** field: An array of zero or more values of type `LangString` where each value contains a string to represent the comment (distinct from its description), and to reference a language by using an ISO 639 with two characters. It is not necessary for comments in different languages to be faithful translations.

- **Is_Active** field: A boolean flag indicating whether a condition is active or not. By default, all conditions are active, namely the default value is `true`. When this flag is `false`, then it is ignored.

### Example: Parking assistant ODD condition

```
MODULES condition specification is as follows
    parking_assistant_module is
        INCLUDE_AND when
            road_surface is paved
            OR
                service_zone_1 is a shapefile representing geo-fenced service area
                service_zone_2 is a shapefile representing geo-fenced service area
```

This describes a module having a single `AND` section, comprising of:
- a requirement that the `road_surface` (= `TaxonomyConcept`) is `paved` (= a `CategoricalLiteral`)
- an `OR` between (union of) two service areas, each specified using a shape file

The ASAM OpenODD model indicates a reference from `Condition` to `Module`. This enables a `Condition` instance to refer to a `Module` instance:

```
ODD specification is as follows
    main_module is_root is true
    main_module is
        INCLUDE_OR when
            parking_assistant_module is true    # specified in modules below
            highway_pilot is true               # specified in modules below

MODULES specification is as follows
    parking_assistant_module is
        ...
    highway_pilot is
        ...
```

## 6.4.3.2 Class Condition

Comprises a `TaxonomyConcept` and a boolean `Expression`.

| Property | Value |
|----------|-------|
| Instantiable | yes |

### Parameters

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| is_active | boolean | yes | A flag indicating whether a `Condition` is active shall be evaluated (active == true) or whether it should be ignored maybe temporarily (active == false) |
| description | LangString | no | This represents a description of the instance of class `condition`. It can be translated into other languages. |
| comment | LangString | no | This represents a comment about the instance of class `condition`. It can be translated into other languages. |

## 6.4.3.3 Module condition semantics

(ODD boundary) conditions in ASAM OpenODD are specified using propositions which determine what is inside or outside the ODD.

A Proposition is a statement or assertion that can be either `true` or `false`. Propositions serve as the basic building blocks in logical reasoning. The boolean propositional semantics of the ASAM OpenODD module conditions uses contributions to the field by Harald Ganzinger (1950–2004).

Key concepts in propositional semantics include:

### Propositional variables
Symbols that represent statements that can be either `true` or `false`, often denoted by letters such as `p`, `q`, `r`.

### Logical connectives
Operations applied to propositions to form more complex propositions:
- **Conjunction (∧)**: Represents `AND`. `p∧q` is true if both `p` and `q` are `true`.
- **Disjunction (∨)**: Represents `OR`. `p∨q` is `true` if at least one of `p` or `q` is `true`.
- **Negation (¬)**: Represents `NOT`. `¬p` is `true` if `p` is `false`.
- **Implication (→)**: Represents `IF…THEN`. `p→q` is `true` unless `p` is `true` and `q` is `false`.
- **Biconditional (↔)**: Represents `IF AND ONLY IF`. `p↔q` is `true` if `p` and `q` have the same truth value.

### Truth tables
Tables that represent the truth values of complex propositions based on the truth values of their constituent propositions.

### Semantic equivalence
Two propositions are semantically equivalent if they have the same truth value under all possible truth value assignments.

### Validity and satisfiability
A proposition is valid if it is true under all possible truth value assignments. A proposition is satisfiable if there exists at least one truth value assignment that makes it true.

## 6.4.3.4 INCLUDE and EXCLUDE semantics

A condition is true if and only if its expression evaluates to true. The truth value of a `Section` (`INCLUDE_*` and `EXCLUDE_*`) is determined based on their **Conditions**. The truth value of a `Module` is determined based on the combination of the value of its `INCLUDE_*` section and its `EXCLUDE_*` section.

### Interpretation of MODULE

```
MODULE === INCLUDE AND (NOT EXCLUDE)
```

- The `Module` is `true` when `INCLUDE_*` is `true` and `EXCLUDE_*` is `false`.
- The `Module` is `false` when `INCLUDE_*` is `false` (regardless of `EXCLUDE_*`).
- The `Module` is `false` when `EXCLUDE_*` is `true` (regardless of `INCLUDE_*`).

### Missing sections

- When `EXCLUDE_*` is missing: `Module` truth value equals `INCLUDE_*`
- When `INCLUDE_*` is missing: `Module` truth value equals `NOT EXCLUDE_*`
- When both are missing: `Module` evaluates to `true`

### Section types

- **INCLUDE_AND**: evaluates to `true` if and only if ALL its conditions evaluate to `true`
- **INCLUDE_OR**: evaluates to `true` if and only if at LEAST ONE condition evaluates to `true`
- **EXCLUDE_AND**: evaluates to `true` if and only if ALL its conditions evaluate to `true`
- **EXCLUDE_OR**: evaluates to `true` if and only if at LEAST ONE condition evaluates to `true`

### Expression evaluation

An instance of class `Condition` comprises a Boolean `Expression` that refers to a `TaxonomyConcept`, a `Value`, and a `Unit`:

- **UpperBound** evaluates to `true` if field ≤ threshold
- **LowerBound** evaluates to `true` if field ≥ threshold
- **Equal** evaluates to `true` if field == value
- **Range** evaluates to `true` if value is within [lower, upper]
- **List** evaluates to `true` if value is in the specified list

### Example: INCLUDE_AND

```
example_module_1 is
    INCLUDE_AND when
        wind_speed is less than 40 km/h
        rainfall_rate is less than 20 mm/h
```

Evaluates to `true` for COD/OD instances where wind_speed < 40 km/h AND rainfall_rate < 20 mm/h.

### Example: INCLUDE_OR

```
example_module_2 is
    INCLUDE_OR when
        wind_speed is greater than or equal to 40 km/h
        rainfall_rate is greater than or equal to 20 mm/h
```

Evaluates to `true` for COD/OD instances where wind_speed ≥ 40 km/h OR rainfall_rate ≥ 20 mm/h.

### Example: INCLUDE_AND with EXCLUDE_OR

```
example_module_5 is
    INCLUDE_AND when
        wind_speed is less than 40 km/h
        rainfall_rate is less than 20 mm/h
    EXCLUDE_OR when
        fog_visibility is less than 50 m
        connectivity_bandwidth is less than 1 Mbps
```

A COD/OD instance is **inside** the ODD if:
- wind_speed < 40 km/h AND rainfall_rate < 20 mm/h
- AND fog_visibility ≥ 50 m AND connectivity_bandwidth ≥ 1 Mbps

### Example: Complex module with nested logic

```
example_module_7 is
    INCLUDE_AND when
        downlink_latency is less than 10 msec
        downlink_throughput is greater than 1 Mbps
        OR
            global_positioning is GPS
            local_positioning is beacon_positioning
    EXCLUDE_OR when
        is_sign_visible is false
        AND
            temporary_road_structures is construction_site_detours
            road_type is expressway
```

Truth value: `dl AND dt AND (gp OR lp) AND NOT(is OR (ts AND rt))`

## 6.4.3.5 Class Label

Instances of class `Label` are propositions which evaluate to `true` if at least one of the instances of class `Module` referencing it in its Label section evaluates to `true`. `Label` instances can be used within Boolean `Expression` instances.

| Property | Value |
|----------|-------|
| Instantiable | yes |

### Parameters

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| id | String | yes | An identifier of the instance of class `Label` (not translated). Must not be a duplicate of a `Module` `id` or `TaxonomyConcept` `id`. |

## 6.4.3.6 Label semantics

The class `Label` is used to enable extending a collection of `Module` instances to include or exclude additional situations without explicit changes to already defined conditions (extensible label disjunction pattern).

Semantic definition:
- Let `Module` `M_1` use the `Label` `L` in one of its conditions.
- Let modules `M_1` to `M_n` be modules specifying `Label` `L`.
- The truth value of `L` is (`M_1` OR … OR `M_n`).

`Module` instances addressed with labels are considered as an OR collection. If one `Module` instance labeled with `suitable_roads` is `true` then `suitable_roads` is `true`. If no `Module` instance labeled with `unsuitable_weather` evaluates to `true`, then `unsuitable_weather` evaluates to `false`.

### Example: Extensible conditions via labels

```
passenger_pickup is
    INCLUDE_OR when
        supported_pickup_locations is true
    EXCLUDE_OR when
        hazardous_conditions is true

# Later, without modifying passenger_pickup:
heavy_rain_module labels hazardous_conditions
heavy_rain_module is
    INCLUDE_AND when
        rainfall_rate is greater than 50 mm/h

icy_road_module labels hazardous_conditions
icy_road_module is
    INCLUDE_AND when
        road_surface_temperature is less than 0 °C
        road_surface_moisture is wet
```
