# ASAM Openodd v1.0.0 — 6.4 ODD modules

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/06_model_concept/06_04_openodd_modules.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 6.4 ODD modules

## 6.4.1 Overview

The module and condition related classes of {THIS\_STANDARD} model

Figure 13. The module and condition related classes of ASAM OpenODD model

[Figure 13](#fig-concept-module-module-and-condition-classes) shows most of the classes related to class `Module` and class `Condition`, so [Figure 13](#fig-concept-module-module-and-condition-classes) is a subset of the ASAM OpenODD model.

## 6.4.2 Sections

### 6.4.2.1 Class Section

A `Section` is a set of `Conditions` linked to a `Module`, comprising of a list of `Conditions`. The link defines whether it is an `EXCLUDE` or an `INCLUDE` section. The `Conditions` may be combined using the `SectionOperator`. [Section 6.4, "ODD modules"](../06_model_concept/06_04_openodd_modules.html)  explains the details of module sections.

Basic information
:   Table 56. Basic information of class Section


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 57. Class Section


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | operator | String | yes | Specifies whether the instance of class `Section` is an `AND` or an `OR` section. |

### 6.4.2.2 Enum SectionOperator

A `SectionOperator` can either be `AND` or `OR` where `AND` denotes that all included conditions must be fulfilled and `OR` means that at least one must be fulfilled.

Basic information
:   Table 58. Basic information of enum SectionOperator


    |  |  |
    | --- | --- |
    | **Instantiable** | no |

## 6.4.3 Modular conditions

### 6.4.3.1 Condition specification

Conditions are used to determine which situations are inside the ODD, and which are outside, whereby individual situations are described using CODs, and aggregate situations are described using an OD.

Class `Condition` contains the following fields:

* **Description** field:  
  An array of values of type `LangString` where each value contains a string to represent the description, and to reference a language by using an ISO 639 [[10](../bibliography.html#bib-iso639)] with two characters.  
  Each language shall have a single translation.  
  At least an English description shall be provided.
* **Comment** field:  
  An array of zero or more values of type `LangString` where each value contains a string to represent the comment (distinct from its description), and to reference a language by using an ISO 639 [[10](../bibliography.html#bib-iso639)] with two characters.  
  It is not necessary for comments in different languages to be faithful translations.
* **Is\_Active** field:  
  A boolean flag indicating whether a condition is active or not.
  By default, all conditions are active, namely the default value is `true`.
  When this flag is `false`, then it is ignored.

The ASAM OpenODD conditions are described using `INCLUDE` and `EXCLUDE` sections.
As an example, consider specifying the ODD of a parking assistant to require that only paved roads are supported, within two specific geo-fenced areas:

Code 63. Example condition (free-form notation)

```
MODULES condition specification is as follows
    parking_assistant_module is
        INCLUDE_AND when
            road_surface is paved
            OR
                service_zone_1 is a shapefile representing geo-fenced service area  # A `TaxonomyConcept` of `Record` type representing shapefile
                service_zone_2 is a shapefile representing geo-fenced service area  # A `TaxonomyConcept` of `Record` type representing shapefile
```

[Code 63](#code-example-condition) describes a module having a single `AND` section, comprising of:

* a requirement that the `road_surface` (= `TaxonomyConcept`) is `paved` (= a `CategoricalLiteral`).
* an `OR` between (that is union of) two service areas, each specified using a shape file.

The ASAM OpenODD model indicates a reference from `Condition` to `Module`.
This enables a `Condition` instance to refer to a `Module` instance.
For example, consider the following example:

Code 64. Example ODD specification (free-form notation)

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

In [Code 64](#code-example-condition-module), the root `Module` instance specifies an `OR` `Condition`, which evaluates to `true`, that is including a situation, if the `Module` instance `parking_assistant_module` or by the `Module` `highway_pilot` is validated to `true`.
If both validate to `false`, `main_module` would validate to `false`.

### 6.4.3.2 Class Condition

Comprises a `TaxonomyConcept` and a boolean `Expression`.

Basic information
:   Table 59. Basic information of class Condition


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 60. Class Condition


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | is\_active | boolean | yes | A flag indicating whether a `Condition` is active shall be evaluated (active == true) or whether it should be ignored maybe temporarily (active == false) |
    | description | LangString | no | This represents a description of the instance of class `condition`. It can be translated into other languages. |
    | comment | LangString | no | This represents a comment about the instance of class `condition`. It can be translated into other languages. |

### 6.4.3.3 Module condition semantics

(ODD boundary) conditions in ASAM OpenODD are specified using propositions which determine what is inside or outside the ODD.

|  |  |
| --- | --- |
|  | A Proposition is a statement or assertion that can be either `true` or `false`. Propositions serve as the basic building blocks in logical reasoning, allowing us to construct arguments, draw inferences, and develop formal systems of logic. The boolean propositional semantics of the ASAM OpenODD module conditions uses contributions to the field by Harald Ganzinger (1950 - 2004) [[13](../bibliography.html#bib-First-Order_Logic_2013)]. |

Conditions in the ASAM OpenODD model are based on propositions.
(ODD) conditions are organized in modules.
These modules specify presence or absence of certain characteristics beforehand introduced as taxonomy concepts.
These conditions are facilitated by expressions and structured within include and/or an exclude sections.

Key concepts in propositional semantics include:

Propositional variables
:   Propositional variables are symbols that represent statements that can be either `true` or `false`.
    These are often denoted by letters such as `p`, `q`, `r`.

Logical connectives
:   Logical connectives are operations that can be applied to propositions to form more complex propositions.
    Common logical connectives include:

    * Conjunction (`∧`): Represents `AND`.
      For example, `p∧q` is true if both `p` and `q` are `true`.
    * Disjunction (`∨`): Represents `OR`.
      For example, `p∨q` is `true` if at least one of `p` or `q` is `true`.
    * Negation (`¬`): Represents `NOT`.
      For example, `¬p` is `true` if `p` is `false`.
    * Implication (`→`): Represents `IF…​THEN`.
      For example, `p→q` is `true` unless `p` is `true` and `q` is `false`.
    * Biconditional (`↔`): Represents `IF AND ONLY IF`.
      For example, `p↔q` is `true` if `p` and `q` have the same truth value.

Truth tables
:   Truth tables are tables that represent the truth values of complex propositions based on the truth values of their constituent propositions.

Semantic equivalence
:   Two propositions are semantically equivalent if they have the same truth value under all possible truth value assignments to their constituent propositions.

Validity and satisfiability
:   A proposition is valid if it is true under all possible truth value assignments to its constituent propositions.
    A proposition is satisfiable if there exists at least one truth value assignment that makes it true.

### 6.4.3.4 INCLUDE and EXCLUDE semantics

A condition is true if and only if its expression evaluates to true.
The truth value of a `Section` (`INCLUDE_*` and `EXCLUDE_*`) is determined based on their **Conditions**.
The truth value of a `Module` is determined based on the combination of the value of its `INCLUDE_*` section and its `EXCLUDE_*` section.

|  |  |
| --- | --- |
|  | Interpretation of MODULE  The `Module` is `true` when `INCLUDE_*` is `true` and, simultaneously, `EXCLUDE_*` is `false`.  The `Module` is `false` when `INCLUDE_*` is `false` and, simultaneously, `EXCLUDE_*` is `false`.  The `Module` is `false` when `INCLUDE_*` is `true` and, simultaneously, `EXCLUDE_*` is `true`.  The `Module` is `false` when `INCLUDE_*` is `false` and, simultaneously, `EXCLUDE_*` is `true`.  That is `MODULE === INCLUDE AND (NOT EXCLUDE)`.  Missing sections are handled as follows:  When `EXCLUDE_*` is missing then `Module` truth value equals the truth value of `INCLUDE_*`.  When `INCLUDE_*` is missing then `Module` truth value equals negation of `EXCLUDE_*`, that is not `EXCLUDE_*`.  When both are missing `Module` evaluates to `true`. |

There are two types of `INCLUDE_*` sections and `EXCLUDE_*` sections:

* `INCLUDE_AND`  
  An `INCLUDE_AND` section evaluates to `true` if and only if all its **conditions** evaluate to `true`.
* `INCLUDE_OR`  
  An `INCLUDE_OR` section evaluates to `true` if and only if at least one of its **conditions** evaluate to `true`.
* `EXCLUDE_AND`  
  An `EXCLUDE_AND` section evaluates to `true` if and only if all its **conditions** evaluate to `true`.  
  Conversely, `EXCLUDE_AND` section evaluates to `false` if at least one of its **conditions** evaluate to `false`.
* `EXCLUDE_OR`  
  An `EXCLUDE_OR` section evaluates to `true` if and only if at least one of its **conditions** evaluate to `true`.  
  Conversely, `EXCLUDE_OR` section evaluates to `false` if all its **conditions** evaluate to `false`.

An instance of class `Condition` comprises a Boolean `Expression`, that refers to a `TaxonomyConcept`, a `Value`, and an `Unit`.
The truth value of an expression is determined as follows:

* An `UpperBound` `Expression` instance evaluates to `true` if the specified field is smaller or equal to the specified threshold.
* A `LowerBound` `Expression` instance evaluates to `true` if the specified field is greater or equal to the specified threshold.
* An `Equal` `Expression` instance evaluates to `true` if the specified field is equal to the value specified in the condition.
* A `Range` `Expression` instance evaluates to `true` if the value of the specified field is within the upper and lower bounds specified by the range.
* A `List` `Expression` instance evaluates to `true` if the value of the specified field is in the list of values specified in the expression.

Truth values of conditions are based on expressions which are evaluated against `COD/OD` instances.

[Code 65](#code-example-module1-include-and) has a single `INCLUDE_AND` section, which means the `INCLUDE_AND` section evaluates to `true` if all its conditions evaluate to `true`.

Code 65. Example INCLUDE\_AND (free-form notation)

```
example_module_1 is
    INCLUDE_AND when
        wind_speed is less than 40 km/h
        rainfall_rate is less than 20 mm/h
```

In [Code 65](#code-example-module1-include-and) `example_module_1` evaluates to `true` for `COD/OD` instances in which the `wind_speed` is less than `40 km/h`, **and** the `rainfall_rate` is less than `20 mm/h`.

[Code 66](#code-example-module2-include-or) has a single `INCLUDE_OR` section, which means the `INCLUDE_OR` section evaluates to `true` if one of its conditions evaluates to `true`.

Code 66. Example INCLUDE\_OR (free-form notation)

```
example_module_2 is
    INCLUDE_OR when
        wind_speed is greater than or equal to 40 km/h
        rainfall_rate is greater than or equal to 20 mm/h
```

In [Code 66](#code-example-module2-include-or) `example_module_2` evaluates to `true` when the `INCLUDE_OR` section evaluate to `true`.
The `INCLUDE_OR` section evaluates to `true` for `COD/OD` instances in which `wind_speed` is greater or equal than `40 km/h`, **or** the `rainfall_rate` is greater or equal than `20 mm/h`.
Conversely, in [Code 66](#code-example-module2-include-or) `example_module_2` evaluates to `false` when the `INCLUDE_OR` section evaluate to `false`.
The `INCLUDE_OR` section evaluates to `false` for `COD/OD` instances in which `wind_speed` is less than `40 km/h`, **and** the `rainfall_rate` is less than `20 mm/h`.

[Code 67](#code-example-module3-exclude-and) has a single `EXCLUDE_AND` section, which means the `EXCLUDE_AND` section evaluates to `false` if at least one of its conditions evaluate to `false`.

Code 67. Example EXCLUDE\_AND (free-form notation)

```
example_module_3 is
    EXCLUDE_AND when
        wind_speed is greater than 40 km/h
        rainfall_rate is greater than 20 mm/h
```

In [Code 67](#code-example-module3-exclude-and) `example_module_3` evaluates to `true` when the `EXCLUDE_AND` section evaluates to `false`.
The `EXCLUDE_AND` section evaluates to `false` for `COD/OD` instances in which the `wind_speed` is less or equal to `40 km/h`, **or** the `rainfall_rate` is less than or equal to `20 mm/h`.
Conversely, in [Code 67](#code-example-module3-exclude-and) `example_module_3` evaluates to `false` when the `EXCLUDE_AND` section evaluates to `true`.
The `EXCLUDE_AND` section evaluates to `true` for `COD/OD` instances in which `wind_speed` is greater than `40 km/h`, **and** the `rainfall_rate` is greater than `20 mm/h`.

[Code 68](#code-example-module4-exclude-or) has a single `EXCLUDE_OR` section, which means the `EXCLUDE_OR` section evaluates to `false` if all its conditions evaluate to `false`.

Code 68. Example EXCLUDE\_OR (free-form notation)

```
example_module_4 is
    EXCLUDE_OR when
        wind_speed is greater than 40 km/h
        rainfall_rate is greater than 20 mm/h
```

In [Code 68](#code-example-module4-exclude-or) `example_module_4` evaluates to `true` when the `EXCLUDE_OR` section evaluates to `false`.
The `EXCLUDE_OR` section evaluates to `false` for `COD/OD` instances in which the `wind_speed` is less or equal to `40 km/h`, **and** the `rainfall_rate` is less than or equal to `20 mm/h`.
Conversely, in [Code 68](#code-example-module4-exclude-or) `example_module_4` evaluates to `false` when the `EXCLUDE_OR` section evaluates to `true`.
The `EXCLUDE_OR` section evaluates to `true` for `COD/OD` instances in which `wind_speed` is greater than `40 km/h`, **or** the `rainfall_rate` is greater than `20 mm/h`.

[Code 69](#code-example-include-and-exclude-or) has a single `INCLUDE_AND` and a single `EXCLUDE_OR` section.

Code 69. Example INCLUDE\_AND and EXCLUDE\_OR (free-form notation)

```
example_module_5 is
    INCLUDE_AND when
        wind_speed is less than 40 km/h
        rainfall_rate is less than 20 mm/h
    EXCLUDE_OR when
        fog_visibility is less than 50 m
        connectivity_bandwidth is less than 1 Mbps
```

Intuitively, it is sufficient for a single condition in the exclude section to be satisfied in order to exclude the `COD/OD` instance from the ODD.
In other words, a `COD/OD` row is **inside** the ODD if both include conditions are satisfied, **and** **both** the exclude conditions are **not** satisfied.
Consequently, [Code 69](#code-example-include-and-exclude-or) evaluates to `true` for `COD/OD` instances in which:

* The `wind_speed` is less than `40 km/h`, **and** the `rainfall_rate` is less than `20 mm/h`
* **and** the `fog_visibility` is greater or equal to `50 m` **and** the `connectivity` is greater or equal to `1 Mbps`.

[Code 70](#code-example-include-or-exclude-and) has a single `INCLUDE_OR` and a single `EXCLUDE_AND` section.

Code 70. Example INCLUDE\_OR and EXCLUDE\_AND (free-form notation)

```
example_module_6 is
    INCLUDE_OR when
        wind_speed is less than 40 km/h
        rainfall_rate is less than 20 mm/h
    EXCLUDE_AND when
        fog_visibility is less than 50 m
        connectivity_bandwidth is less than 1 Mbps
```

Intuitively, both conditions in the exclude section have to be satisfied in order to exclude the `COD/OD` instance from the ODD.
In other words, a `COD/OD` instance is outside the ODD if either include conditions are satisfied, **and** **either** of the exclude conditions is **not** satisfied.
Consequently, [Code 70](#code-example-include-or-exclude-and) evaluates to `true` for `COD/OD` instance in which:

* The `wind_speed` is less than `40 mm/h`, **or** the `rainfall_rate` is less than `20 mm/h`
* **or** the `fog_visibility` is greater or equal to `50 m` **or** the `connectivity` is greater or equal to `1 Mbps`.

[Code 71](#code-example-complex-module) has an `INCLUDE_AND` with an `OR` and an `EXCLUDE_OR` with an `AND` section.

Code 71. Example complex module (free-form notation)

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

To evaluate [Code 71](#code-example-complex-module), it is helpful to define propositions for each condition:

* Introduce a proposition `dl` defined to be `true` if and only if `(downlink_latency is less than 10 msec)`
* Introduce a proposition `dt` defined to be `true` if and only if `(downlink_throughput is greater than 1 Mbps)`
* Introduce a proposition `gp` defined to be `true` if and only if `(global_positioning is GPS)`
* Introduce a proposition `lp` defined to be `true` if and only if `(local_positioning is beacon_positioning)`
* Introduce a proposition `is` defined to be `true` if and only if `(is_sign_visible is false)`
* Introduce a proposition `ts` defined to be `true` if and only if `(temporary_road_structures is construction_site_detours)`
* Introduce a proposition `rt` defined to be `true` if and only if `(road_type is expressway)`

Using the above propositions, the `Module` `example_module_7` in [Code 71](#code-example-complex-module) evaluate to `true` if and only if:

Code 72. Truth value of `example_module_7` in [Code 71](#code-example-complex-module) (free-form notation)

```
dl AND dt AND (gp OR lp) AND NOT(is OR (ts AND rt))
```

### 6.4.3.5 Class Label

Instances of class `Label` are propositions which evaluate to `true` if at least one of the instances of class `Module` referencing it in its Label section evaluates to `true`. See [Section 6.4.3.4, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics) . `Label` instances can be used within Boolean `Expression` instances.

Basic information
:   Table 61. Basic information of class Label


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 62. Class Label


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | An identifier of the instance of class `Label` (not translated to multiple languages). This `id` string must not be a duplicate of a `Module` `id` or a `TaxonomyConcept` `id`. |

### 6.4.3.6 Label semantics

The class `Label` is used to enable extending a collection of `Module` instances to include or exclude additional situations without explicit changes to the already defined conditions.
Such a capability is unlocked by the extensible label disjunction pattern.

The semantic of the labels is defined as follows:

* Let `Module` `M_1` use the `Label` `L` in one of its conditions.
* Let the `Module` instances `M_1` to `M_n` be a list of `Module` instances specifying a `Label` `L`.

The truth value of `L` is (`M_1` or …​ or `M_n`).
This truth value is interpreted based on the condition in which it resides.

`Module` instances addressed with the help of labels are considered as `OR` collection.
`Label` instances are used in the conditions like Boolean `Condition` instances.
If one `Module` instance labeled with `suitable_roads` is `true` then `suitable_roads` are `true`, since you can be only at one location at the time.
If no `Module` instance labeled with `unsuitable_weather` evaluates to `true`, then `unsuitable_weather` evaluates to `false`, meaning no hazardous conditions are present.

For example, consider defining a list of hazardous environment `Condition` instances.
Initially, the list of `Condition` instances is limited, for example when the rain drops are too large and reduce the effectiveness of the camera vision systems to an unacceptable level.
Over time, additional hazardous `Condition` instances are added, for example when the road surface is icy.
[Code 73](#code-example-inclusion-exclusion-conditions) shows how inclusion and exclusion `Condition` instances can be added without modifying previously developed `Module` instances.

Code 73. Example inclusion and exclusion conditions (free-form notation)

```
passenger_pickup is
    INCLUDE_OR when
        supported_pickup_locations is true
    ...
    EXCLUDE_OR when
        hazardous_conditions is true

pickup_locations_group1 is
    LABEL is supported_pickup_locations
    INCLUDE_AND when
        street_section in
            main_st_sec1
            main_st_sec2

pickup_locations_group2 is
    LABEL is supported_pickup_locations
    INCLUDE_AND when
        train_station in
            pole5
            pole11
    ...

too_much_rain is
    LABEL is hazardous_conditions
    INCLUDE_AND when
        rain_rate equals heavy_rain
    ...

icy_road_conditions is
    LABEL is hazardous_conditions
    INCLUDE_AND when
        road_surface_condition equals black_ice
    ...
```

[Code 74](#code-example-include-or-exclude-or) is equivalent to [Code 73](#code-example-inclusion-exclusion-conditions) regarding semantics:

Code 74. Example INCLUDE\_OR and EXCLUDE\_OR (free-form notation)

```
passenger_pickup is
    INCLUDE_OR when
        pickup_locations_group1 is true
        pickup_locations_group2 is true
    ...
    EXCLUDE_OR when
        too_much_rain is true
        icy_road_conditions is true
```

The benefits of using an instance of class `Label` is extending the conditions without explicitly listing all its components.
This improves the maintainability of the ODD specification.

### 6.4.3.7 Nested module semantics

An instance of class `Module` has a field `id` of type `string` that is also referred to as its ID.
The `id` of a `Module` instance is regarded as a Boolean proposition that evaluates to `true` if and only if its module evaluates to `true`.
An `Expression` instance can refer to a `Module` instance by their `id`, that can accept a value of `true` or `false`.

[Code 75](#code-example-parent-module) evaluates to `true` if and only if `example_module_1` evaluates to `true` and `example_module_7` evaluates to `false`.

Code 75. Example nested modules (free-form notation)

```
parent_module is
    INCLUDE_AND when
        example_module_1 is true
        example_module_7 is false
```

[Code 76](#code-example-parent-module-2) shows an illustrative example for using labels to define hazardous conditions:

Code 76. Example nested modules two (free-form notation)

```
parent_module_1 is        # top-level module
    EXCLUDE_OR when
        hazard is true    # leveraging a label; indirectly referencing an 'or' between the two modules

parent_module_2 is                 # hazard top-level module
    EXCLUDE_OR when
        hazard_module_1 is true    # *not* using label; directly referring to the module
        hazard_module_2 is true    # *not* using label; directly referring to the module

hazard_module_1 is
    LABELS is hazard    # can add other multiple labels if needed
    INCLUDE_OR when
        wind_speed is greater than 50 km/h

hazard_module_2 is
    LABELS is hazard    # can add other multiple labels if needed
    EXCLUDE_OR when
        rainfall_rate is greater than 20 mm/h
```

The `Module` instances `parent_module_1` and `parent_module_2` are equivalent:

* `parent_module_1` evaluates to `false` if and only if the `hazard` label is `true`.
  The `hazard` label evaluates to `true` if either `hazard_module_1` or `hazard_module_2` are `true`.
* `parent_module_2` evaluates to `false` if either `hazard_module_1` **or** `hazard_module_2` evaluate to `true`.

The pattern defined in `parent_module_1` is preferred because it is not necessary to list all hazard defining modules, which enables extensions without changing the top -level modules.

## 6.4.4 Module details

### 6.4.4.1 Module specification

Each instance of class `Module` contains the following fields:

* **ID** field:  
  This is a string field within the `Module` representing a Unique Identifier.
  A globally unique name, possibly achieved using a dot-notation, for example, `weather.wind.wind_speed`.
  For details on dot-notation, see [Section 6.4.6, “Conditions with user defined structures”](#sec-conditions-with-user-defined-structures).
  This requires that the name is globally unique.
  Further, the name should be provided in a single language, for example, English, for all language variants.  
  **Explicitly forbidden**: Module UIDs shall not include the string `unknown`.
* **Title** field:  
  Each contains a `LangString` to represent the name, and to reference a language using an ISO 639 2-char country code.
  A single instance of class `Module` may compose multiple instances of class `LangString` that represent a translation to a different language.
  Each language shall have a single translation.
* **Description** field:  
  The description field comprises a list of one or more instances of `LangString` representing the description, with possible translations to multiple languages.
  Each language shall have a single translation.
* **Comment** field:  
  The comment field comprises a list of one or more instances of `LangString` representing a single comment.
  Each comment can be specified in a different language.
* **Is\_Root** field:  
  This is a boolean attribute.
  When this field is `true`, it indicates that this module is designated as "root" modules.
  This field is used only when performing inference.
  The inference steps shall start from a single module with this field set to `true`.
* **Is\_Active** field:  
  A boolean flag indicating whether a module is active or not.
  By default, all modules are active, namely the default value is `true`.
  When this flag is `false`, then it is ignored, and all conditions referring to it or its negation are automatically satisfied.
* **Export\_Instructions** field  
  The export instructions are optional, and consist of a string with the export and import instruction, using one of the following options (a single uniform option shall be selected for all instances of class `Taxonomy`).
  The format of the instructions are specified in [Section 6.2.8, "Taxonomy export instruction format"](06_02_openodd_taxonomy.html#sec-taxonomy-export-instruction-format).

A `Module` shall compose at least one instance of class `Section`, which may compose another instance of class `Section`, as follows:

* A `Module` shall compose at least one `INCLUDE` section or `EXCLUDE` section.
* A `Module` shall compose at most one `INCLUDE` section.
* A `Module` shall compose at most one `EXCLUDE` section.
* The deletion of a `Module` deletes all instances of class `Section` of which it consists.

Each `Module` references zero or more instances of class `Label`.
The instances specify an ID string that cannot be a duplicate of a `Module` ID or a `TaxonomyConcept` ID.
Labels do not need translations; they shall be English-comprehensible strings.
Each `Module` comprises zero or more instances of class `Tag`.
Each instance specifies a **name** string.

Explicitly forbidden:

* Modules semantics is always consistent with the "default" mode defined in ISO 34503 [[4](../bibliography.html#bib-iso34503)].
* Label names shall not include the string `unknown`.

### 6.4.4.2 Class Module

An instance of class `Module` comprises of at least one include or exclude `Section` (either `AND` or `OR`). At most one include `Section` and one exclude `Section` are allowed. A comprehensive description of modules can be found in [Section 6.4, "ODD modules"](../06_model_concept/06_04_openodd_modules.html) .

Basic information
:   Table 63. Basic information of class Module


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 64. Class Module


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | The `Module` id, also referred to as handle, according to specifications in [Section 6.4.4.1, "Module specification"](../06_model_concept/06_04_openodd_modules.html#sec-module-specification) . This ID must be unique within the ASAM OpenODD transmission. |
    | title | LangString | yes | This represents the title of the `Module`. It can be translated into other languages. At least an English title must be provided. |
    | description | LangString | no | This represents a description of the `Module`. It can be translated into other languages. |
    | comment | LangString | no | This represents a comment about the `Module`. It can be translated into other languages. |
    | is\_root | boolean | yes | If set to true this instance of class `Module` will be used as entry point for inference, no other instance of class `Module` can depend on it. |
    | is\_active | boolean | yes | A flag indicating whether an instance of class `Module` is active and its conditions shall be evaluated (active == true) or whether it should be ignored maybe temporarily (active == false) |
    | export\_instructions | String | no | The export instructions are used to specify where to export and in which format. See [Section 6.4.8.4, "Module export instruction format"](../06_model_concept/06_04_openodd_modules.html#sec-module-export-instruction-format) . |

### 6.4.4.3 Module export instructions details

|  |  |
| --- | --- |
|  | The export instructions are optional, and used to specify specific location or file breakdown of an export. |

The instruction comprises a string that represents the export and import instructions with one of the following options.
The content of the instruction shall select a single uniform location option for all instances of class `Module`:

* **FILE:** File name that will contain the export or from which an import was performed.
  See the `File` export import instructions section for the detailed format specification of this string.
* **DB**: Database connection string that refers to the database that will contain the export or from which an import is performed.
  See the `Export_Instructions` field in [Section 6.4.4.1, “Module specification”](#sec-module-specification).
* **SERVICE**: Service endpoint to which the export or from which an import is performed.
  See the `Export_Instructions` field in [Section 6.4.4.1, “Module specification”](#sec-module-specification).

The export functionality shall satisfy the following roundtrip requirements:

* Each `Module` and related content shall be sent to the location specified in the instructions within a specific file or database, or it shall be pushed to the specified service.
* An import operation of the unmodified exported content shall result in an identical representation.
* An import and a subsequent export of the same set of modules shall result in identical data.

### 6.4.4.4 Basic modular ODD specifications

To define the ODD in modular form, it is necessary to support the following capabilities:

* An ODD refers to "library" components that are reusable.
* Generic conditions such as "bad weather" and "bad connectivity" can occur in numerous unpredictable situations.

[Code 77](#code-example-content-of-modules-file1) illustrates how the ASAM OpenODD model and above semantics are used to realize the above capabilities:

Code 77. Example content of modules\_file1.txt (free-form notation)

```
IMPORT the following files
    taxonomy.txt                         # assumes all taxonomy concepts are defined in this file

MODULES are as follows
    bad_connectivity_module_1 is
        TITLE is "conditions for bad connectivity"
        LABELS is bad_connectivity       # this module defines one of the bad connectivity conditions
        INCLUDE_OR when
            downlink_latency is greater than 10 msec   # Need to receive real-time events
            downlink_throughput is less than 1 Mbps # Need to receive large amounts of data

    bad_connectivity_module_2 is
        TITLE is "unacceptable positioning"
        LABELS is bad_connectivity       # this module defines one of the bad connectivity conditions
        INCLUDE_OR when                  # the minimal positioning are:
            global_positioning is true   #     it is sufficient to have GNSS
            local_positioning is true    #     it is sufficient to have positioning beacons
```

Code 78. Example content of modules\_file2.txt (free-form notation)

```
IMPORT the following files
    taxonomy.txt                            # assumes all taxonomy concepts are defined in this file
    module_file1.txt                        # connectivity definition

ODD is defined as follows
    odd_main_module_1 is                    # The main ODD specification entry point
        TITLE is "ODD for ADS v0.23"
        INCLUDE_AND when
            road_type is in                 # Only specific road types are inside ODD
                town_expressway             # categorical literal
                town_collector              # categorical literal
                town_arterial               # categorical literal
        EXCLUDE_OR when                     # These are not safe for V0.23
            bad_weather is true             # Numerous distinct conditions may represent bad weather
            bad_connectivity is true        # Numerous distinct conditions may represent bad connectivity
        AND                                 # exclude a very specific type of work zones
            road_type is town_expressway    # on the town_expressway road type
            zone_type is work_zone

    bad_weather_module_1 is
        LABELS is bad_weather               # this module defines one of the bad weather conditions
        INCLUDE_AND when
            rain_intensity_type is in       # this type of rain results in too many vision subsystem detection errors
                convective                  # categorical literal
                orographic                  # categorical literal

    bad_weather_module_2 is
        LABELS is bad_weather               # this module defines one of the bad weather conditions
        INCLUDE_OR when
            wind_speed is greater than 50 km/h    # this wind speed results in unstable sensors, leading to too many vision subsystem detection errors
```

### 6.4.4.5 Using custom defined types in conditions

The custom types can be used in conditions using the dot-notation.
Conditions for individual fields within the type are specified by the concept name followed by the field within the type.

[Code 79](#code-example-custom-types) includes in the ODD situations where the trajectory is within ±20 degrees relative to the center of the road, but excluding tangential velocities above 50 km/h relative to the center of the road:

Code 79. Example custom types (free-form notation)

```
TAXONOMY defines the following concepts
    relative_radial_vector is                        # vector relative to direction of travel
        radius is float representing length          # intensity
        angle is float representing angle            # direction
        wind_trajectory is relative_radial_vector    # no units defined because this is a record representing user defined type

ODD is defined as follows
    top_level_odd_module is
        INCLUDE_AND when
            wind_trajectory.angle in [-20 .. 20] deg                      # minimum alignment with road
        EXCLUDE_OR when
            wind_trajectory.tangential_velocity is greater than 50 km/h   # maximum acceptable wind speed in direction of road
```

### 6.4.4.6 Using measures in conditions

Measures are referenced in conditions using the dot-notation.
In contrast to non-measure concepts, where the specification of the overarching concept is optional, the specification of the overarching concept is required for measures.
Consider the following examples:

* Conditions over the maximum height of speed bumps can be specified with `speed_bump.height.max is less than 3 cm`.
* Conditions over the exposure to pedestrians in terms of occurrences per hour can be specified with `pedestrian.occurrence_rate is less than 1e-8 1/hr`.
* Conditions over the confidence of cyclist detection can be specified with `cyclist.confidence is greater than 95 %`.

|  |  |
| --- | --- |
|  | For details on dot-notation, see [Section 6.4.6, “Conditions with user defined structures”](#sec-conditions-with-user-defined-structures). |

### 6.4.4.7 Examples of complex conditions

A complex `Condition` is, for example, a `Module` instance, including and/or excluding other `Module` instances.

[Code 80](#code-example-complex-conditions) shows a complex condition:

Code 80. Example complex conditions (free-form notation)

```
MODULES specification is as follows
    parking_assistant_module is                 # an instance of module
        INCLUDE_OR when                         # an INCLUDE_OR section
            parking_structure_module is true    # a condition referring to a module instance
            parallel_parking_module is true     # a condition referring to a module instance
            ...

    parking_structure_module is ...

    parallel_parking_module is ...
```

In [Code 80](#code-example-complex-conditions) `parking_structure_module` is a `Module` instance referenced from the first instance of class `Condition`.
In [Code 80](#code-example-complex-conditions) `parallel_parking_module` is a `Module` instance referenced from the second instance of class `Condition`.

### 6.4.4.8 Class Tag

Each `Module` comprises zero or more instances of class `Tag`, each specifying a name string. These tags are used for organizational purposes only. Tags do not have semantic interpretation.

Basic information
:   Table 65. Basic information of class Tag


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 66. Class Tag


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | name | LangString | yes | The name of the instance of class `Tag`. It is not required to be unique and can be translated into other languages. |

## 6.4.5 Geo-fenced service area specification

Geo-fencing generally refers to the definition of virtual boundaries on a map that can trigger specific actions when crossed.
Geo-fencing allows the definition of spatial boundaries where an ODD is scoped.

ASAM OpenODD uses ESRI Shapefiles [[14](../bibliography.html#bib-esrishapefile)] to define these regions.
A shapefile represents a vector-based geospatial format that describes the geometry (for example, polygons, points, lines) of service zones.
This enables precise mapping of operational boundaries.

The example below [Code 81](#code-example-shapefiles) demonstrates how geo-fenced service areas are specified using shapefiles in ASAM OpenODD.

Code 81. Example shapefiles (free-form notation)

```
MODULES specification is as follows
    parking_assistant_module is
        INCLUDE_OR when                                                         # ensures that at least one service zone must be valid for the module to be included in the ODD
            service_zone_1 is a shapefile representing geo-fenced service area  # a `TaxonomyConcept` of `Record` type representing shapefile
            service_zone_2 is a shapefile representing geo-fenced service area  # a `TaxonomyConcept` of `Record` type representing shapefile
            ...
```

ASAM OpenODD exclusively supports ESRI shapefiles for defining geo-fenced areas.
A valid shapefile consists of multiple files, each serving a specific function:

Table 67. ESRI shapefile functions


| File Type | Description |
| --- | --- |
| **shp** | Contains the actual vector-based **geometries** (points, lines, polygons). |
| **shx** | Provides an **index** for fast access to spatial data. |
| **dbf** | Stores **attribute data** (for example, region names, operational constraints) in dBase IV format. |
| **shp.xml** | Contains **geospatial metadata** in XML format (for example, ISO 19115-3:2023 metadata standard). |

A valid shapefile must contain at least `.shp`, `.shx`, and `.dbf` files.

## 6.4.6 Conditions with user defined structures

### 6.4.6.1 General information

The class `Type` enables the definition of user-defined structures as `TaxonomyConcepts`.
Such structures can be referenced in `Expression` instances.
The syntax for such references shall use the dot-notation as follows:

* An instance of class `Record` defines a structure concept with multiple child fields, each of which can be an instance of class `Record` or an instance of class `PrimitiveType` that represents an attribute.
* Use the syntax `<concept>.<field>` to refer to the field within the structure.

Consider, for example, defining a taxonomy comprising of a complex structure representing an `intersection`, having a `type` of `unprotected`, `signalized`, or `roundabout`, can be `simple`, `channelized` or `flared`, that can have multiple stages, and can have multiple ways in or out.
In addition, another complex structure may be used to provide the content specified by a list of `signs`.

[Code 82](#code-example-use-case-modules) shows a full example of use-case modules leveraging such a complex structure:

Code 82. Example use-case modules (free-form notation)

```
TAXONOMY specification is as follows
    scenery is
        road_type is
            expressway
            town_local
            rural
            play_street
    intersection is
        type is
            unprotected
            signalized
            roundabout
            no_intersection
        feature is
            simple
            flared
            channelized
        ways is an integer representing count
        stages is an integer representing count
    signs is
        speed_limit is a float representing velocity
        speed_level is
            low when speed_limit is less than 10 km/h
            medium when speed_limit is between 10 and 50 km/h
            high when speed_limit is greater than 50 km/h

MODULES specification is as follows
    use_case1 is as follows
        INCLUDE_AND when     # a condition comparing speed qualitatively
            road_type is
                play_street
            signs.speed_limit is less than 10 km/h
            intersection.type is signalized
            intersection.feature is simple

    use_case2 is as follows
        INCLUDE_AND when     # a condition comparing speed numerically
            road_type is
                town_local
                rural
            signs.speed_level is less or equal to medium
            intersection.type is unprotected or signalized
            intersection.feature is
                simple
                flared
                channelized

    use_case3 is as follows
        INCLUDE_AND when     # a condition comparing speed qualitatively
            speed_limit is greater than 50 km/h
            road_type is expressway
            intersection.type is no_intersection
```

[Code 82](#code-example-use-case-modules) is illustrated by the following example, whereby:

Explanation:

* The taxonomy specification defines a scenery hierarchy with a single categorical value called `road_type`, whose value literals are not ordered.
* The taxonomy specification defines a scenery hierarchy with a single numeric value called `speed_limit`, whose value literals are not ordered.
* The taxonomy also defines a `speed_level` categorical with ordered values `low` < `medium` < `high`.
* The `Module` instances `use_case1` and `use_case3` perform numeric comparison on the `speed_limit`.
* The `Module` instance `use_case2` performs qualitative comparison on the `speed_level` (less or equal to `medium`), relying on the order induced by the ranges.
* The `Module` instance `use_case1` accepts only intersections which are `simple` and `signalized`.
* The `Module` instance `use_case2` accepts only intersections which are `unprotected`, `signalized`, and further, requires that they are either `simple`, `flared`, `channelized`.
* The `Module` instance `use_case3` accepts only `road_type` of kind `expressway` for a scenery without any intersection.

The above is represented by the ASAM OpenODD model as follows:

* The `TaxonomyConcept` instances of `intersection` and `signs` are represented by records.
* The `TaxonomyConcept` instances of `speed_limit` and `speed_level` are attributes within the `signs` structure.

### 6.4.6.2 Discontinuous ODD

It is possible to have a transition from inside ODD to outside ODD of a conditionally automated driving function.
ASAM OpenODD allows the definition of conditions that trigger ODD exit events.
Some implentations may monitor the ODD attributes in both `INCLUDE_*` and `EXCLUDE_*` for triggering an ODD-exit.

Code 83. ODD Exit Conditions (free-form notation)

```
MODULES condition specification is as follows
    highway_autopilot is
        EXCLUDE_OR when
            road_type is low_speed_zone
            rain_level is heavy_rain
```

In this example, `EXCLUDE_OR` specifies the excluded **conditions that trigger an ODD exit**.
As an example, prior to the exit, the `road_type` is `autobahn`, and `rain_level` is `light`.
Once `road_type` changes to `low_speed_zone` or `rain_level` changes to `heavy_rain`, the `Module` `highway_autopilot` evaluates to `false` and exits the ODD.

### 6.4.6.3 Module MetaData

Every `Module` instance may compose zero or more meta data elements.
Deletion of the `Module` instance removes the corresponding meta data element.

An instance of class `MetaData` can be added to a `Module` instance at the `Module` level and the `Condition` level.
In addition, `MetaData` instances can be added at the `Section` level and the `Value` level, specified within structured comments associated with specific fields and values.
`MetaData` instances can be added within comments as shown in [Code 84](#code-example-module-metadata).

Code 84. Example module `MetaData` (free-form notation)

```
MODULES specification is as follows
    example_module_metadata is
        METADATA for the module
            key1 is value1
            key2 is value2
        TITLE is illustrating metadata
        INCLUDE_AND when
            METADATA for the condition
                key3 is value3
                key4 is value4
            road_type is                # key5 is value5, key6 is value6
                town_expressway         # key7 is value7, key8 is value8
                town_collector
                town_arterial
```

[Code 84](#code-example-module-metadata) illustrates:

* The `MetaData` instance for the whole module is associated with `key1 is value1` and `key2 is value2`.
* The `MetaData` instance for conditions in the `INCLUDE_AND` section is associated with `key3 is value3` and `key4 is value4`.
* The `MetaData` instance for `road_type` within the `CategoricalList` expression is associated with `key5 is value5` and `key6 is value6`.
* The `MetaData` instance for `CategoricalLiteral` values, like `town_expressway` within the `Condition` is associated with `key7 is value7` and `key8 is value8`, as specified in comments.

### 6.4.6.4 Working with uncertainty

There are two types of uncertainty in measurements:

* Aleatoric uncertainty: The limitations of the sensors result in an uncertain measurement.
  As an example, the position and distance measurement by the vehicle is uncertain.
  Such uncertainty can be modeled by providing a range of values, for example `distance is [10.6 .. 10.7] m`.
* Epistemic uncertainty: The limitations of sensor fusion and neural network detections result in an epistemic uncertainty.
  As an example, the detection of cyclists is uncertain.
  Such uncertainty can be represented either by using multiple values, for example `vru is [cyclist, motorcycle]`, or using a confidence measure, for example `cyclist.confidence is 0.73`.

[Code 85](#code-example-uncertainty) shows how ASAM OpenODD supports both types of uncertainty:

Code 85. Example uncertainty (free-form notation)

```
TAXONOMY specification is as follows
    scenery is
        road_surface_condition is
            dry_road
            wet_road
            icy_road
    dynamic_environment is
        vru is
            pedestrian
            cyclist

MODULES specification is as follows
    example_uncertainty_module is
        EXCLUDE_OR when
            pedestrian.occurrence is greater than 1e-6 occ/hr   # aleatoric uncertainty
            icy_road.probability is greater than 1e-4 occ/hr    # aleatoric uncertainty
            pedestrian.detection_confidence is less than 0.8    # epistemic uncertainty
            icy_road.detection_confidence is less than 0.7      # epistemic uncertainty
```

In [Code 85](#code-example-uncertainty), the taxonomy defines `icy_road` as a categorical literal for `road_surface_condition` and `pedestrian` as a categorical literal for `vru`.
The `example_uncertainty_module` defines an exclusion condition that represents uncertainty:

* The `LowerBound` expression `pedestrian.occurrence is greater than 1e-8 occ/hr` evaluates to `true` if the probability of **encountering** a `pedestrian` is less than once per 10^8 hours.
* The `LowerBound` expression `icy_road.probability is greater than 1e-4 occ/hr` evaluates to `true` if the probability of **encountering** an `icy_road` is less than once per 10^4 hours.
* The `LowerBound` expression `pedestrian.detection_confidence is less than 0.8` evaluates to `true` if the probability of **detecting** a `pedestrian` is less than 80%.
* The `LowerBound` expression `icy_road.detection_confidence is less than 0.7` evaluates to `true` if the probability of **detecting** an `icy_road` is less than 70%.

Uncertainty also exists when data is missing.
[Code 86](#code-example-missing-data) shows that a condition can require that the number of pedestrians on the road is known in which the vehicle resides:

Code 86. Example missing data (free-form notation)

```
TAXONOMY specification is as follows
    scenery is
        current_road is road_type
        current_road.pedestrian_count is an integer representing a count

MODULES specification is as follows
    example_value_required is
        EXCLUDE_OR when
            current_road.pedestrian_count equals unknown
```

* The concept `current_road` is a categorical defined to have the same categorical literals as `road_type` has.
* The measure `pedestrian_count` is defined for the concept `current_road` with a type of `integer` and unit types of `count`.
* `unknown` is a **special keyword** and is used to indicate that the value of a field is missing or empty.
  This is equivalent to an empty JSON value, a python `None` value, or a null pointer value.
  See condition type specifications above.
  `none`, `null` and `undefined` are all acceptable replacements for `unknown`.
* The expression `current_road.pedestrian_count equals unknown` is an **Equal Expression** that evaluates to `true` if and only if the value of `current_road.pedestrian_count` is missing in the `COD/OD` record.

## 6.4.7 Multi file exports

File export is facilitated using an instance of class `File`, as follows:

* A `File` instance may compose multiple `Taxonomy` instances.
* A `File` instance may compose multiple `Module` instances.
* A `File` instance may compose other `File` instances using an **import** operation.

See also [Section 6.1.4.3, "File specification"](06_01_openodd_model.html#sec-concept-overview-file-specification).

With this model:

* Each file can specify taxonomy concepts and conditions via modules.
* Files can import taxonomy concepts and conditions from other files.

## 6.4.8 Expressions

### 6.4.8.1 Overview

The expression related classes of {THIS\_STANDARD} model

Figure 14. The expression related classes of ASAM OpenODD model

[Figure 14](#fig-concept-module-expression-classes) shows most of the classes related to class `Expression`, so [Figure 14](#fig-concept-module-expression-classes) is a subset of the ASAM OpenODD model.

### 6.4.8.2 General information

Expressions in ASAM OpenODD define logical conditions for inclusion or exclusion in an ODD.
Expressions are used in two primary contexts:

* Conditions within `Module`:  
  Expressions define constraints on environmental factors affecting ODD validity.
  Conditions specifying numeric constraints - Expressions specify numeric upper and lower bound constraints on numeric taxonomy concepts, for example of type float.
* `CategoricalLiteral` definitions in taxonomies:  
  Expressions specify categorical values using range or list-based constraints.

The following expression subclasses are supported:

* The `LowerBound` class defines expressions specifying inclusion in the ODD when a `TaxonomyConceptValue` is greater than a specified value (see `<LowerBoundExpression>` in [Code 88](#code-example-formal-expression-syntax)).
  The expression syntax corresponds to that of the `<LowerBoundExpression>` in [Code 88](#code-example-formal-expression-syntax).
  The lower bound value can be either a `PrimitiveType` or a `CategoricalLiteral`.
  For example:

  + A lower bound expression with a numeric `PrimitiveType` is `downlink_throughput is greater than 1 Mbps`.
  + A lower bound expression with a `CategoricalLiteral` is `rain_level is greater than or equal to medium_rain`.
* The `UpperBound` class defines expressions specifying inclusion in the ODD when a `TaxonomyConceptValue` is smaller than a specified value (see `<UpperBoundExpression>` in [Code 88](#code-example-formal-expression-syntax)).
  The upper bound value can be either a `PrimitiveType` or a `CategoricalLiteral`.
  For example:

  + An upper bound expression with a numeric `PrimitiveType` is `downlink_throughput is less than 1 Mbps`.
  + An upper bound expression with a `CategoricalLiteral` is `rain_level is less than or equal to medium_rain`.
* The `Equal` class comprises an `Equal` expressions (see `<EqualExpression>` in [Code 88](#code-example-formal-expression-syntax)):
  These expressions specify inclusions in the ODD of environment conditions with a `TaxonomyConceptValue` equal to a specified value.
  The expression syntax corresponds to that of the `<EqualExpression>` in [Code 88](#code-example-formal-expression-syntax).
  The equal value can be either a `PrimitiveType` or a `CategoricalLiteral`.
  For example:

  + An equal expression with a numeric `PrimitiveType` is `number_of_lanes is 3`.
  + An equal expression with a `CategoricalLiteral` is `road_type is expressway`.
* The `Range` class comprises a `Range` expressions (see `<RangeExpression>` in [Code 88](#code-example-formal-expression-syntax)):
  These expressions specify inclusions in the ODD of environment conditions with a `TaxonomyConceptValue` between two values.
  The expression syntax corresponds to that of the `<RangeExpression>` in [Code 88](#code-example-formal-expression-syntax).
  The lower and upper bound values can be either a `PrimitiveType` or a `CategoricalLiteral`, but they shall both be of the same type.
  For example,

  + A range expression with a numeric `PrimitiveType` is `rain_rate is [2 .. 11] mm/h`.
  + A range expression with a `CategoricalLiteral` is `wind_level is [undetectable_wind .. moderate_wind]`.
* The `CategoricalList` comprises a `CategoricalList` expressions (see `<CategoricalListExpression>` in [Code 88](#code-example-formal-expression-syntax)):
  These expressions specify inclusions in the ODD of environment conditions with a `TaxonomyConceptValue` of type `Categorical` that have at least one of a list of specified `CategoricalLiteral`.
  The expression syntax corresponds to that of the `<CategoricalListExpression>` in [Code 88](#code-example-formal-expression-syntax).
  Mixing values from multiple `Categorical` is not allowed within a single expression.
  Therefore, all `CategoricalLiteral` instances shall be composed of a single `Categorical`.
  For example:

  + For `CategoricalLiteral` instances that reference an `Expression`, only a single `CategoricalLiteral` `Value` can be observed in a COD.
  + A list expression with a `CategoricalLiteral` is `road_type is [autobahn, expressway, arterial]`.

### 6.4.8.3 Condition and expression structure

This section specifies how to write conditions and expressions using a syntax independent structure.
Interchangeability of conditions and expressions between different formats is achieved through a consistent mapping of structures defined in this section.

|  |  |
| --- | --- |
|  | The expressions within the ASAM OpenODD model are not fully formalized as the ASAM OpenODD model is on a meta-level and focuses on ODDs. This section is formulated technology independently. |

The ASAM OpenODD model specifies that:

* A `Condition` references an `Expression`.
* An `Expression` references a `TaxonomyConcept`.

As such, the general structure defined in [Code 87](#code-example-condition-structure) would be used for a condition:

Code 87. General structure of a condition (free-form notation)

```
<Condition>   ::=   [ ( <TaxonomyConcept> | <Module> | <Label> ) :] <Expression>
```

[Code 88](#code-example-formal-expression-syntax) shows the structure of an expression:

Code 88. Expression structure for an expression (free-form notation)

```
<OperatorEqual>             ::=   defined by mapping reference
<OperatorGreaterThan>       ::=   defined by mapping reference
<OperatorGreaterEqual>      ::=   defined by mapping reference
<OperatorLessThan>          ::=   defined by mapping reference
<OperatorLessEqual>         ::=   defined by mapping reference

<Expression>                ::=   <UpperBoundExpression> | <LowerBoundExpression> | <EqualExpression> | <RangeExpression> | <CategoricalListExpression>
<UpperBoundExpression>      ::=   (<OperatorGreaterThan>, <OperatorGreaterEqual>) ((<NumericTerm> [<Unit>]) | <CategoricalLiteral>)
<LowerBoundExpression>      ::=   (<OperatorLessThan>, <OperatorLessEqual>) ((<NumericTerm> [<Unit>]) | <CategoricalLiteral>)
<EqualExpression>           ::=   <OperatorEqual> (<NumericTerm> [<Unit>]) | <OperatorEqual> ( <CategoricalLiteral> | "true" | "false" )
<RangeExpression>           ::=   "[" <NumericTerm> ( ".." | "," ) <NumericTerm> "]"  <Unit>
<CategoricalListExpression> ::=   "[" <CategoricalLiteral> { "," <CategoricalLiteral> } "]"
<Unit>                      ::=   One string from a list of pre-defined unit types
<NumericTerm>               ::=   <Factor> | <Factor> "*" <Factor> | <Factor> "/" <Factor>
<Factor>                    ::=   <NumericAttribute> | <Number>
<CategoricalLiteral>        ::=   A taxonomy defined categorical literal
<NumericAttribute>          ::=   A taxonomy defined attribute of types float or integer associated with a unit type

<Number>                    ::=   [<Sign>] <IntegerPart> ["." <FractionalPart>] [<Exponent>]
<IntegerPart>               ::=   <DigitSequence> | ε
<FractionalPart>            ::=   <DigitSequence>
<Exponent>                  ::=   "E" [<Sign>] <DigitSequence>
<Sign>                      ::=   "+" | "-"
<DigitSequence>             ::=   <Digit> { <Digit> }
<Digit>                     ::=   "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

|  |  |
| --- | --- |
|  | * Multiple white spaces are assumed to be replaced with a single space separating terms. * Dot notation of attributes within records are assumed to be part of the <TaxonomyConcept>. |

[Code 88](#code-example-formal-expression-syntax) illustrates:

* An `<Expression>` is one of the five possible expressions according to the ASAM OpenODD model.
* An `<UpperBoundExpression>` requires that a numeric taxonomy concept is **smaller** than the upper bound specified by a `<NumericTerm>`, followed by a `<Unit>`, or by a categorical literal associated with an expression.
* A `<LowerBoundExpression>` requires that a numeric taxonomy concept is **greater** than the lower bound specified by a `<NumericTerm>`, followed by a `<Unit>`, or by a categorical literal associated with an expression.
* An `<EqualExpression>` requires that a taxonomy concept, either numeric or categorical, equals a specific value specified by a `<NumericTerm>`, followed by a `<Unit>`, or by a categorical literal associated with an expression.
* A `<RangeExpression>` requires that a numerical taxonomy concept is greater than the first `<NumericTerm>` and smaller than the second `<NumericTerm>`.
  The two numeric terms can be separated by `..` or by `,`.
* A `<CategoricalListExpression>` expression is a comma separated list of taxonomy concepts.
* A `<NumericTerm>` is a numeric attribute or a number, possibly multiplied or divided by another `<Term>`.
  For simplicity, recursive expressions are excluded, and only simple expressions are allowed.

|  |  |
| --- | --- |
|  | The `<Unit>` is not part of the numeric term to allow specifying it outside the core of the expressions. Numeric terms that represent counts do not have units, and therefore the `<Unit>` is optional. |

* A `<Factor>` is a numeric attribute or a number.
* A `<Number>` is a floating-point or integer number.
  The condition and expression structure specification might be a bit confusing as it details the use of "." for the fraction and an "E" for scientific notation.
* A `<Unit>` is a string from a list of predefined units according to the ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)].
  The unit shall be associated with the unit type specified for the corresponding numeric attribute in the taxonomy.
  For example, the two strings `km/h` and `kph` are a valid specification of kilometers per hour, which has the unit type `velocity`.

Code 89. Example equal expressions (free-form notation)

```
rain_level equals low
number_of_lanes equals 3
```

Code 90. Example categorical list expressions (free-form notation)

```
rain_level is
    low
    medium
```

Code 91. Example lower bound expressions (free-form notation)

```
rain_rate is greater than 2 mm/h
lane_width is greater than 1.75*ego_width
```

Code 92. Example upper bound expressions (free-form notation)

```
rain_rate is less than 10 mm/h
lane_width is less than 2.25*ego_width
```

Code 93. Example range expressions (free-form notation)

```
rain_rate in [2 .. 10] mm/h
lane_width in [1.25*ego_width .. 2.25*ego_width]
```

|  |  |
| --- | --- |
|  | There are no units with parameterized expressions. |

### 6.4.8.4 Module export instruction format

The module export instruction format has the same specification as provided in [Section 6.2.8, "Taxonomy export instruction format"](06_02_openodd_taxonomy.html#sec-taxonomy-export-instruction-format).

### 6.4.8.5. Use of `CategoricalLiteral`

Class `CategoricalLiteral` in combination with class `Expression` is helpful for modularization and parameterization.

[Code 94](#code-example-boolean-conditions) shows how to specify boolean conditions with explicit thresholds:

Code 94. Example boolean conditions (free-form notation)

```
MODULES specification is as follows
    bad_weather is
        INCLUDE_OR when
            rain_rate is greater than 5 mm/h
            wind_speed is greater than 50 km/h
```

Each location, for example country, state, and so on, may have different speed limits or acceptable precipitation rates for its climate.
With this explicit approach, it is impossible to adjust these thresholds without taking local conditions into account.

[Code 95](#code-example-taxonomy) shows how to use taxonomy to define thresholds, instead of using the explicit threshold conditions:

Code 95. Example taxonomy (free-form notation)

```
TAXONOMY specification is as follows
    rain_rate is a float representing precipitation rate
    rain_level is
        no_rain when
            rain_rate is 0 mm/h
        light_rain when
            rain_rate is less than or equal to 1 mm/h
        moderate_rain when
            rain_rate in [1 .. 5] mm/h
        heavy_rain when
            rain_rate is greater than 5 mm/h
    wind_speed is a float representing velocity
    is_dangerous_wind is
        true when
            wind_speed greater than 50 km/h
        false when
            wind_speed is less than or equal to 50 km/h
```

[Code 96](#code-example-importing-file) shows how the thresholds can be modified by importing a different file and a module condition:

Code 96. Example module condition (free-form notation)

```
IMPORT specification is as follows
    locale_taxonomy.txt

MODULES specification is as follows
    bad_weather is
        INCLUDE_OR when
            rain_level is heavy_rain
            is_dangerous_wind is true
```

Moreover, the use of categorical literals with expressions induces an order between the categorical literals.
For example, this enables the use of categorical literals in lower and upper bound constraints.

[Code 97](#code-example-list-expression) shows the undesired explicit list expression:

Code 97. Example list expression (free-form notation)

```
rain_level is
    no_rain
    light_rain
    moderate_rain
```

[Code 98](#code-example-simplified-expression) shows how to avoid hardcoding the full list of literals by using a following simplified and more-readable expression:

Code 98. Example simplified expression (free-form notation)

```
rain_level is less than heavy_rain
```

Expressions such as `…​ is less than or equal to medium` require that the corresponding `TaxonomyConcept`, for example `medium` or `heavy_rain`, is associated with ranges.
See the illustration of ranges in [Code 48](06_02_openodd_taxonomy.html#code-example-categorical-literals) of [Section 6.2.4.4, "CategoricalLiteral specification"](06_02_openodd_taxonomy.html#sec-concept-taxonomy-categoricalliteral_specification).

To further illustrate the utility of the implied order between the categorical literals, consider modeling the requirement:

"If wind is below `light_breeze` the rain is up to `heavy_rain`, but if wind is stronger than `light_breeze`, wind is up to `light_rain`."

Code 99. Example requirement (free-form notation)

```
ODD is
    odd1 is
        INCLUDE_OR when
            windy_rain_1 is true
            windy_rain_2 is true

MODULES specification is as follows
    windy_rain_1 is
        INCLUDE_AND when
            wind_level is no_wind
            rain_level is less than or equal to heavy_rain
    windy_rain_2 is
        INCLUDE_AND when
            wind_level is greater than no_wind
            rain_level is less than or equal to light_rain
```

[Code 99](#code-example-requirement) is interesting because it defines a union that otherwise will be difficult to express in a compact fashion:

* There are two acceptable windy rain conditions within the ODD: `windy_rain_1` and `windy_rain_2`.
* For `windy_rain_1`, heavy rain without any wind is included.
* For `windy_rain_2`, when we have any kind of wind, only the rain level `light_rain` or less is accepted.

[Table 68](#tab-modules-windyrainexamblecod) is a set of CODs verifiable against the windy\_rain\_1 module:

Table 68. An example COD verifiable against windy\_rain\_1


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_LEVEL;categorical\_literal | ROAD\_TYPE;categorical\_literal |
| --- | --- | --- | --- | --- |
| 1 | "2023-06-01 08:12:53.784" | "45.024 10.261" | moderate\_rain | motorway |
| 2 | "2023-06-01 08:12:54.149" | "45.024 10.261" | light\_rain | local\_road |
| 3 | "2023-06-02 11:42:21.913" | "45.024 10.261" | no\_rain | bundesautobahn |

[Code 100](#code-example-changing-taxonomy) shows how to change the taxonomy by adding the `paved_road`:

Code 100. Example changing the taxonomy (free-form notation)

```
TAXONOMY specification is as follows
    paved_road is
        RQ28
        RQ31
        RQ36
        RQ43-5
    road_type is
        motorway when
            paved_road is
                RQ31
                RQ36
        local_road when
            paved_road is RQ28
        bundesautobahn when
            paved_road is RQ43-5
```

[Table 69](#tab-modules-pavedroadexamblecod) is a set of CODs leveraging the above paved road taxonomy:

Table 69. A set of CODs leveraging the above paved road taxonomy


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_LEVEL;categorical\_literal | PAVED\_ROAD;categorical\_literal |
| --- | --- | --- | --- | --- |
| 1 | "2023-06-01 08:12:53.784" | "45.024 10.261" | moderate\_rain | RQ31;RQ36 |
| 2 | "2023-06-01 08:12:54.149" | "45.024 10.261" | light\_rain | RQ28 |
| 3 | "2023-06-02 11:42:21.913" | "45.024 10.261" | no\_rain | RQ43-5 |

### 6.4.8.6 Class Expression

An instance of this class is representing an expression denoting the meaning of a `Condition` or defining ranges for a `CategoricalLiteral` (see [Section 6.4.3.4, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics) ).

Basic information
:   Table 70. Basic information of class Expression


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Children** | CategoricalList, Equal, LowerBound, Range, UpperBound |

Parameters
:   Table 71. Class Expression


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | expr | String | yes | The value of this field contains the expression string having a well-structured syntax. |

### 6.4.8.7 Class LowerBound

`LowerBound` expressions: These expressions may specify inclusion or exclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance greater than a specified instance of class `Value`. It may also specify the meaning of the largest `CategoricalLiteral` within a categorical `TaxonomyConcept`.

Basic information
:   Table 72. Basic information of class LowerBound


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |

### 6.4.8.8 Class UpperBound

`UpperBound` expressions: These expressions may specify inclusion or exclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance lesser than a specified instance of class `Value`. It may also specify the meaning of the smallest `CategoricalLiteral` within a categorical `TaxonomyConcept`.

Basic information
:   Table 73. Basic information of class UpperBound


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |

### 6.4.8.9 Class Equal

These expressions may specify inclusion or exclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance equal to a specified instance of class `Value`.

Basic information
:   Table 74. Basic information of class Equal


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |

### 6.4.8.10 Class Range

These expressions may specify inclusion or exclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance between two instances of class `Value`. It may also specify the meaning of the `CategoricalLiteral` within a categorical `TaxonomyConcept`.

Basic information
:   Table 75. Basic information of class Range


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |

### 6.4.8.11 Class CategoricalList

These expressions may specify inclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance of `Categorical` type having at least one of a list of specified `CategoricalLiteral`. It may also specify the meaning of the `CategoricalLiteral` within a categorical `TaxonomyConcept`.

Basic information
:   Table 76. Basic information of class CategoricalList


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |