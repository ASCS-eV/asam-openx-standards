# ASAM Openodd v1.0.0 — 10.4 ODD module mapping

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/10_yaml/10_04_openodd_export_modules_yaml.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.4 ODD module mapping

## 10.4.1 ODD modular conditions

### 10.4.1.1 Module condition semantics

The expression specified within a YAML condition shall follow the methods of [Section 6.4.8.3, "Condition and expression structure"](../06_model_concept/06_04_openodd_modules.html#sec-condition-and-expression-structure) in ASAM OpenODD model.
The following examples illustrate these semantics.

In [Section 6.4.3.3, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics), the free-form notation in [Code 65](../06_model_concept/06_04_openodd_modules.html#code-example-module1-include-and) is mapped to YAML, as illustrated in [Code 180](#code-example-1).
The description below the free-form notation provides details on its semantics.

Code 180. Example INCLUDE\_AND

```
MODULES:
    example_module_1:
        INCLUDE_AND:
            wind_speed: "< 40 km/h"
            rainfall_rate: "< 20 mm/h"
```

In [Section 6.4.3.3, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics), the free-form notation in [Code 66](../06_model_concept/06_04_openodd_modules.html#code-example-module2-include-or) is mapped to YAML, as illustrated in [Code 181](#code-example-2).
The description below the free-form notation provides details on its semantics.

Code 181. Example INCLUDE\_OR

```
MODULES:
    example_module_2:
        INCLUDE_OR:
            wind_speed: "< 40 km/h"
            rainfall_rate: "< 20 mm/h"
```

In [Section 6.4.3.3, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics), the free-form notation in [Code 67](../06_model_concept/06_04_openodd_modules.html#code-example-module3-exclude-and) is mapped to YAML, as illustrated in [Code 182](#code-example-3).
The description below the free-form notation provides details on its semantics.

Code 182. Example EXCLUDE\_AND

```
MODULES:
    example_module_3:
        EXCLUDE_AND:
            wind_speed: "> 40 km/h"
            rainfall_rate: "> 20 mm/h"
```

In [Section 6.4.3.3, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics), the free-form notation in [Code 68](../06_model_concept/06_04_openodd_modules.html#code-example-module4-exclude-or) is mapped to YAML, as illustrated in [Code 183](#code-example-4).
The description below the free-form notation provides details on its semantics.

Code 183. Example EXCLUDE\_OR

```
MODULES:
    example_module_4:
        EXCLUDE_OR:
            wind_speed: "> 40 km/h"
            rainfall_rate: "> 20 mm/h"
```

In [Section 6.4.3.3, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics), the free-form notation in [Code 69](../06_model_concept/06_04_openodd_modules.html#code-example-include-and-exclude-or) is mapped to YAML, as illustrated in [Code 184](#code-example-5).
The description below the free-form notation provides details on its semantics.

Code 184. Example INCLUDE\_AND and EXCLUDE\_OR

```
MODULES:
    example_module_5:
        INCLUDE_AND:
            wind_speed: "< 40 km/h"
            rainfall_rate: "< 20 mm/h"
        EXCLUDE_OR:
            fog_visibility: "< 50 m"
            connectivity_bandwidth: "< 1 Mbps"
```

In [Section 6.4.3.3, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics), the free-form notation in [Code 70](../06_model_concept/06_04_openodd_modules.html#code-example-include-or-exclude-and) is mapped to YAML, as illustrated in [Code 185](#code-example-6).
The description below the free-form notation provides details on its semantics.

Code 185. Example INCLUDE\_OR and EXCLUDE\_AND

```
MODULES:
    example_module_6:
        INCLUDE_OR:
            wind_speed: "< 40 km/h"
            rainfall_rate: "< 20 mm/h"
        EXCLUDE_AND:
            fog_visibility: "< 50 m"
            connectivity_bandwidth: "< 1 Mbps"
```

In [Section 6.4.3.3, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics), the free-form notation in [Code 71](../06_model_concept/06_04_openodd_modules.html#code-example-complex-module) is mapped to YAML, as illustrated in [Code 186](#code-example-7).
The description below the free-form notation provides details on its semantics.

Code 186. Example complex module

```
MODULES:
    example_module_7:
        INCLUDE_AND:
            downlink_latency: "< 10 msec"
            downlink_throughput: "> 1 Mbps"
            OR:
                global_positioning: GPS
                local_positioning: beacon_positioning
        EXCLUDE_OR:
            is_sign_visible: false
            AND:
                temporary_road_structures:
                    - construction_site_detours
                road_type:
                    - expressway
```

### 10.4.1.2 Nested module semantics

Nested modules (see [Section 6.4.3.5, "Nested module semantics"](../06_model_concept/06_04_openodd_modules.html#sec-concept-modules-nested_module_semantics)) can be mapped to YAML like the following:

In [Section 6.4.3.5, "Nested module semantics"](../06_model_concept/06_04_openodd_modules.html#sec-concept-modules-nested_module_semantics), the free-form notation in [Code 75](../06_model_concept/06_04_openodd_modules.html#code-example-parent-module) is mapped to YAML, as illustrated in [Code 187](#code-example-8).
The description below the free-form notation provides details on its semantics.

Code 187. Example nested modules

```
MODULES:
    parent_module:
        INCLUDE_AND:
            example_module_1: true
            example_module_7: false
```

In [Section 6.4.3.5, "Nested module semantics"](../06_model_concept/06_04_openodd_modules.html#sec-concept-modules-nested_module_semantics), the free-form notation in [Code 76](../06_model_concept/06_04_openodd_modules.html#code-example-parent-module-2) is mapped to YAML, as illustrated in [Code 188](#code-example-9).
The description below the free-form notation provides details on its semantics.

Code 188. Example nested modules two

```
MODULES:
    parent_module_1:
        EXCLUDE_OR:
            hazard: true

    parent_module_2:
        EXCLUDE_OR:
            hazard_module_1: true
            hazard_module_2: true

    hazard_module_1:
        LABELS:
            - hazard
        INCLUDE_OR:
            wind_speed: "> 50 km/h"

    hazard_module_2:
        LABELS:
            - hazard
        INCLUDE_OR:
            rainfall_rate: "> 20 mm/h"
```

## 10.4.2 Module specification details

### 10.4.2.1 Module instance details

For the specification of class `Module` in ASAM OpenODD model see [Section 6.4.4, "Module details"](../06_model_concept/06_04_openodd_modules.html#sec-concept-modules-module-details).
See following how a `Module` instance shall be represented in YAML:

* `id` field:  
  This is a unique name which is unique across all ODD modules.
  The element under which the `module` is defined is the `id` for example `odd_main_module_1`.
* `title` field:  
  It is specified using the `TITLE` YAML element, and its content is a free-form title.
* `description` field:
  It is specified using the `DESCRIPTION` YAML element, and its content is a free-form description.
* `comment` field:  
  It is specified using the `#` special char, and its content is a free-form comment.
* `is_root` field:  
  All modules specified under the ODD element are root modules.
  Any module which is **not** referenced by other modules is regarded as the root module, namely `is_root = true`.
* `is_active` field:  
  This is indicated using the `ACTIVE` element.
* A `Module` shall compose at least one `INCLUDE` section or `EXCLUDE` section.
* A `Module` shall compose at most one `INCLUDE` section.
* A `Module` shall compose at most one `EXCLUDE` section.
* Deletion of a `Module` deletes all `Section` objects it composes.

Each `Module` references a single `Module Kind` object, which represents one of the following:

* ODD: An ODD module representing a top-level module typically referring to other modules.
* TOD: A TOD module representing a top-level module typically referring to other modules.
* Standard: Any other module, that means this is the default kind.
* Additional kinds such as `Boundary Module`:  
  A rule describing general boundary conditions which cannot be violated by any other module.

Each `Module` references zero or more `Label` instances, each specifying an ID string which cannot be a duplicate of a `Module` ID or a `TaxonomyConcept` ID.
Each `Module` comprises zero or more `Tag` instances, each specifying a `name` string.

### 10.4.2.2 Basic modular ODD specifications

To map the examples from [Section 6.4.4.3, "Basic modular ODD specifications"](../06_model_concept/06_04_openodd_modules.html#sec-basic-modular-ODD-specifications) to YAML, consider the YAML examples [Code 189](#code-file2-yml-data-mode-and-semantics) and [Code 190](#code-file1-yml-data-mode-and-semantics):

Code 189. Example file file2.yml for ASAM OpenODD model and semantics

```
IMPORT:
    - taxonomy.yml  # assumes all taxonomy concepts are defined in this file
    - file1.yml     # connectivity definition

ODD:
    odd_main_module_1:  # The main ODD specification entry point
        TITLE: ODD for ADS v0.23
        INCLUDE_AND:
            road_type:  # Only specific road types are inside ODD
                - town_expressway
                - town_collector
                - town_arterial
        EXCLUDE_OR:                 # These are not safe for V0.23
            bad_weather: true       # Numerous distinct conditions may represent bad weather
            bad_connectivity: true  # Numerous distinct conditions may represent bad connectivity
            AND:                          # Exclude a very specific type of work zones
              road_type: town_expressway  # on the town_expressway road type
              zone_type: work_zone

    bad_weather_module_1:
        LABEL:
            bad_weather            # This module defines one of the bad weather conditions
        INCLUDE_AND:
            rain_intensity_type:   # This type of rain results in too many vision subsystem detection errors
                - convective
                - orographic

    bad_weather_module_2:
        LABEL:
            bad_weather            # This module defines one of the bad weather conditions
        INCLUDE_OR:
            wind_speed: "> 50 km/h"  # This wind intensity results in unstable sensors, leading to too many vision subsystem detection errors
```

|  |  |
| --- | --- |
|  | The quotes are added to ensure the validity of the YAML. A simple pre-processor can be used to add them in to avoid the need to specify them manually. |

Code 190. Example file file1.yml for ASAM OpenODD model and semantics

```
IMPORT:
    - taxonomy.yml  # assumes all taxonomy concepts are defined in this file

MODULES:
    bad_connectivity_module_1:
        TITLE: conditions for bad connectivity
        LABELS:
            bad_connectivity       # This module defines one of the bad connectivity conditions
        INCLUDE_OR:
            downlink_latency: "> 10 msec"       # Need to receive real-time events
            downlink_throughput: "< 1 Mbps"     # Need to receive large amounts of data

    bad_connectivity_module_2:
        TITLE: unacceptable positioning
        LABELS:
            bad_connectivity        # This module defines one of the bad connectivity conditions
        INCLUDE_OR:                     # The minimal positioning are:
            global_positioning: true    # it is sufficient to have GNSS
            local_positioning: true     # it is sufficient to have positioning beacons
```

|  |  |
| --- | --- |
|  | The quotes are added to ensure the validity of the YAML. A simple pre-processor can be used to add them in to avoid the need to specify them manually. |

The YAML export in [Code 189](#code-file2-yml-data-mode-and-semantics) and [Code 190](#code-file1-yml-data-mode-and-semantics) is limited because it does not include module IDs, export instructions nor multi-language translation.

To address this limitation, for example, CSV export can be used.
See  [Section 8, "Model to tabular format mapping reference"](../08_tabular/08_00_tabular.html#top-model-tabular-mapping-reference) for the full export specifications.

See the export specification of each format (YAML, ASAM OpenSCENARIO DSL, CSV, and XML) for the detailed specification of each export format and implied import requirements.

### 10.4.2.3 Leveraging user defined types in conditions

The custom types can be leveraged in conditions using the dot-notation.
Conditions over individual fields within the type are specified using the concept name, followed by the field within the type.

Consider the example [Code 191](#code-user-type-conditions):

Code 191. Example for user defined types in conditions

```
TAXONOMY:
    relative_radial_vector:                         # Vector relative to direction of travel
       radius: float length                         # Intensity
       angle: float angle                           # Direction
    wind_trajectory: relative_radial_vector         # No units defined because this is a record representing user defined type
ODD:
    top_level_odd_module:
        INCLUDE_AND:
            wind_trajectory.angle: "[-20 .. 20] deg"  # Minimum alignment with travel direction
        EXCLUDE_OR:
            wind_trajectory.radius: "> 50 km/h"     # Maximum acceptable intensity
```

The example [Code 191](#code-user-type-conditions) accepts in the ODD situations in which the trajectory is within ±20 degrees relative to the road center, but excluding tangential velocities above 50 km/h relative to the road center.

### 10.4.2.4 Using measures in conditions

Measures are referenced in conditions using the dot-notation.
In contrast to non-measure concepts, where specifying the parent is optional, for measures, specifying the parent concept is required.
Consider the following examples:

* Conditions over the maximum height of speed bumps can be specified using `speed_bump.height.max: < 3 cm`.
* Conditions over the exposure to pedestrians in terms of occurrences per hour can be specified using `pedestrian.occurrence_rate: < 1e-8 1/hr`.
* Conditions over the confidence of cyclist detection can be specified using `cyclist.confidence: > 95 %`.

### 10.4.2.5 Examples of complex conditions

This section presents some export examples.
See the corresponding export sections for the format specification.

Consider a simple example module represented within a single YAML file `file1.yml`.

|  |  |
| --- | --- |
|  | The module files can import taxonomy definitions from other files using the `IMPORT` statement, but they may also define the concepts within the same file as the module. |

The following is an example of a modules file which is importing a taxonomy file:

Code 192. Example for file import

```
IMPORT:
    - taxonomy.yml # contains definitions for all concepts used in the modules

ODD:
    odd1:
        TITLE: The baseline ODD for SuperShuttle v1.0
        INCLUDE_AND:
            low_speed_roads: true
            good_connectivity: true
        EXCLUDE_OR:
            bad_weather: true

MODULES:
    low_speed_roads:
        TITLE: Low speed traffic conditions
        INCLUDE_AND:
            road_type:
               - town_local
               - dead_end
            lane_count: < 3
        EXCLUDE_OR:
            is_mixed_zone: true
            is_parallel_parking: true

    bad_weather:
        TITLE: Conditions for bad weather
        INCLUDE_OR:
            rainfall_level:
                - heavy_rain
            is_dangerous_wind: true

    good_connectivity:
        TITLE: conditions for good connectivity
        INCLUDE_AND:
            downlink_latency: "< 10 msec"
            downlink_throughput: "> 1 Mbps"
            OR:
                global_positioning:
                    - GNSS
                local_positioning:
                    - beacon_positioning
        EXCLUDE_OR:
            is_sign_visible: false
            AND:
                temporary_road_structures:
                    - construction_site_detours
                road_type:
                    - expressway
```

The `Module` `odd1` is defined within the ODD element, and is therefore a root `Module`, `is_root=true`.

## 10.4.3 Geo-fenced service area specification

Specification of geo-fenced service area can be done using shape files.

Code 193. Example for shape file usage

```
TAXONOMY:
    scenery:
        service_area: shapefile

MODULES:
    service_area_conditions:
        TITLE: Specification of the Service Area
        INCLUDE_AND:
            service_area: service_area_boundary.shp
```

## 10.4.4 Conditions with user defined structures

### 10.4.4.1 General information

The class `Type` enables the definition of user-defined structures as `TaxonomyConcept` instances.
Such structures can be referenced in `Expression` instances.
The syntax for such references shall use the dot-notation as follows:

* Assume a `Type` instance defines a `<struct>` with a child `<field>` and that another `Type` instance defines `<concept>` to be of type `<struct>`.
* Use the syntax `<concept>.<field>` to refer to the field within the struct.

Consider the example [Code 194](#code-conditions-user-defined):

Code 194. Example for user defined condition

```
TAXONOMY:
    vector_types:
        radial_vector:
            r: float velocity
            a: float angle
    dynamic_environment:
        vehicle:
            trajectory: radial_vector
            velocity: radial_vector

 MODULES:
    main_module:
        INCLUDE_AND:
            trajectory.a: "[-20 .. 20] deg"
        EXCLUDE_OR:
            velocity.r: "> 50 km/h"
```

[Code 194](#code-conditions-user-defined) accepts into the ODD situations in which the trajectory is within ±20 degrees relative to the road center, but excluding tangential velocities above 50 km/h relative to the road center.

This approach can be further used to perform qualitative comparisons in addition to numeric comparisons:

* Numeric comparison is performed against the numeric field used to define the range constraints.
* Qualitative comparison is performed against the categorical field for which the range constraints are defined.

This is illustrated using example [Code 195](#code-conditions-user-defined-comparison), whereby the module `use_case1` performs numeric comparison, but `use_case2` performs qualitative comparison.
Further, the module `use_case3` leverages the order induced on categorical literals to provide a categorical lower bound condition.

Code 195. Example for user defined comparison

```
TAXONOMY:
    scenery:
        road_type:
            - expressway
            - town_local
            - rural
            - play_street
    traffic:
        traffic_speed_rate: float velocity
        traffic_speed_level:
            slow:
                traffic_speed_rate: "< 20 km/h"
            moderate:
                traffic_speed_rate: "[20 .. 80] km/h"
            fast:
                traffic_speed_rate: "> 80 km/h"

    subjective_vehicle:
        speed_rate: traffic_speed_rate
        speed_level: traffic_speed_level

MODULES:
    use_case1:
        INCLUDE_AND: # a condition comparing speed numerically.
            road_type:
                - town_local
                - rural
            speed_rate: "< 15 km/h"

    use_case2:
        INCLUDE_AND: # a condition comparing speed qualitatively.
            speed_level: slow
            road_type:
                - play_street

    use_case3:
        INCLUDE_AND: # a condition comparing speed qualitatively.
            speed_level: > slow
            road_type:
                - expressway
```

The following is an explanation:

* The `Taxonomy` specification defines a `scenery` hierarchy with a single a `Categorical` instance called `road_type`, having value literals which are not ordered.
* The `Taxonomy` also defines a `traffic` hierarchy with a `traffic_speed_level` `Categorical` instance having ordered values: Each of the `CategoricalLiteral` instances is associated with an `Expression` instance.
  The `Expression` instances induce the following ordering: `slow` < `moderate` < `fast`
* The `Module` `use_case1` defines a `Condition` which is satisfied when the `speed_rate` is less than 15 km/h (that means `UpperBound` `Expression`) and the `road_type` is either `town_local` or `rural` (that means `CategoricalList` `Expression`).
  A COD may only specify one of those values, but an OD may specify both (in case two CODs with different values are aggregated).
* The `Module` `use_case2` defines a `Condition` which is satisfied when the `road_type` is `play_street` (that means `Equal` constraint) and the `speed_level` is `slow` (that means `Equal` `Expression`).
* The `Module` `use_case3` defines a `Condition` which is satisfied when the `road_type` is `expressway` (that means `Equal` constraint) and the `speed_level` is greater than `slow` (that means `LowerBound` `Expression` leveraging an ordered `CategoricalLiteral`).

|  |  |
| --- | --- |
|  | Use Case modules should be directly referenced by root modules, which are specified directly under the ODD element. |

### 10.4.4.2 Module MetaData

See [Section 6.4.6.3, "Module MetaData"](../06_model_concept/06_04_openodd_modules.html#sec-concept-modules-module-metadata) how MetaData is defined in ASAM OpenODD model.
When using YAML notation, a `MetaData` instance can be added within comments by using the `#/` characters at the end of every line.

`MetaData` instances can be attached to `Module` instances and `Section` instances.
In addition, `MetaData` instances can be specified within structured comments associated with specific fields and values.

Consider the YAML example in [Code 196](#code-module-meta-data):

Code 196. Example for meta data

```
MODULES:
    example_module_metadata:
        METADATA:
            key1: value1
            key2: value2
        TITLE: Illustrating Metadata
        INCLUDE_AND:
            METADATA:
                key3: value3
                key4: value4
            road_type: #/ key5:value5, key6:value6
                - town_expressway  #/ key7:value7, key8:value8
                - town_collector
                - town_arterial
```

In this example:

* The `Module` as a whole is associated with `key1: value1` and `key2: value2`.
* The `INCLUDE_AND` section is associated with `key3: value3` and `key4: value4`.
* The `road_type` concept within the `CategoricalList` expression is associated with `key5: value5` and `key6: value6`.
* The `CategoricalLiteral` `town_expressway` within the `Condition` is associated with `key7: value7` and `key8: value8`.

### 10.4.4.3 Working with uncertainty

Measurements have uncertainty of two types:

* Aleatoric uncertainty:
  The limitations of the sensors result in an uncertain measurement.
  As an example, position and distance measurement by the vehicle is uncertain.
  Such uncertainty can be modeled by providing a range of values, for example `distance: [10.6 .. 10.7] m`.
* Epistemic uncertainty:
  The limitations of sensor fusion and neural network detections.
  As an example, the detection of cyclists is uncertain.
  Such uncertainty can be represented either by using multiple values, for example `vru: [cyclist, motorcycle]`, or using a confidence measure, for example `cyclist.confidence: 0.73`.

To illustrate how ASAM OpenODD supports both types of uncertainty, consider the example module in [Code 197](#code-uncertainty):

Code 197. Example for uncertainty

```
TAXONOMY:
    scenery:
        road_surface_condition:
            - dry_road
            - wet_road
            - icy_road
    dynamic_environment:
        vru:
            - pedestrian
            - cyclist
MODULES:
    example_uncertainty_module:
        EXCLUDE_OR:
            pedestrian.occurrence: "> 1e-6 occ/hr"   # Aleatoric uncertainty
            icy_road.probability: "> 1e-4 occ/hr"    # Aleatoric uncertainty
            pedestrian.detection_confidence: < 0.8 # Epistemic uncertainty
            icy_road.detection_confidence: < 0.7   # Epistemic uncertainty
```

In this example, the taxonomy defines `icy_road` as a categorical literal for `road_surface_condition`, and `pedestrian` as a categorical literal for `vru`.
The `example_uncertainty_module` defines an exclusion condition representing uncertainty:

* The **Lower Bound** expression `pedestrian.occurrence: > 1e-8 occ/hr` evaluates to `true` if the probability of **encountering** a `pedestrian` is less than once per 10^8 hours.
* The **Lower Bound** expression `icy_road.probability: > 1e-4 occ/hr` evaluates to `true` if the probability of **encountering** an `icy_road` is less than once per 10^4 hours.
* The **Upper Bound** expression `pedestrian.detection_confidence: < 0.8` evaluates to `true` if the probability of **detecting** a `pedestrian` is less than 80%.
* The **Upper Bound** expression `icy_road.detection_confidence: < 0.7` evaluates to `true` if the probability of **detecting** an `icy_road` is less than 70%.

In addition, uncertainty exists when data is missing.
In example [Code 198](#code-uncertainty-data-missing), a condition can require that we know how many pedestrians are on the road section in which the vehicle resides:

Code 198. Example for missing data

```
TAXONOMY:
    scenery:
        current_road:
            - road_type
        current_road.pedestrian_count: integer count

MODULES:
    example_value_required:
        EXCLUDE_OR:
            current_road.pedestrian_count: unknown
```

|  |  |
| --- | --- |
|  | * The concept `current_road` is a categorical defined to have the same categorical literals as `road_type` has. * The measure `pedestrian_count` is defined for the concept `current_road` with a type of `integer` and unit types of `count`. * `unknown` is a **special keyword** used to indicate that the value of a field is missing or empty; this is equivalent to an empty JSON value or python `None` value or a null pointer value (see condition type specifications above). * The expression `current_road.pedestrian_count: unknown` is an **Equal Expression** which evaluates to `true` if and only if the value of `current_road.pedestrian_count` is missing from the COD or OD record. |

## 10.4.5 Expressions

### 10.4.5.1 General information

See [Section 6.4.8, "Expressions"](../06_model_concept/06_04_openodd_modules.html#sec-expressions) for general information on expressions.

### 10.4.5.2 Formal expression syntax

The formal expression syntax consists of [Code 88](../06_model_concept/06_04_openodd_modules.html#code-example-formal-expression-syntax) and [Code 199](#code-yaml-operator-definition).

Code 199. YAML operator definition (free-form notation)

```
<OperatorEqual>             ::=   " "
<OperatorGreaterThan>       ::=   ">"
<OperatorGreaterEqual>      ::=   ">="
<OperatorLessThan>          ::=   "<"
<OperatorLessEqual>         ::=   "<="
```

### 10.4.5.3 Examples

Code 200. Example for equal expressions

```
rain_level: low
number_of_lanes: 3
```

Code 201. Example for categorical list expressions

```
rain_level:
    - low
    - medium
fog_heavy: [fog_mist, fog_medium, fog_heavy]
```

Code 202. Example for lower bound expressions

```
rain_rate: "> 2 mm/h"
lane_width: "> 1.75*ego_width"
```

Code 203. Example for upper bound expressions

```
rain_rate: "< 10 mm/h"
lane_width: < 2.25*ego_width
```

Code 204. Example for range expressions

```
rain_rate: "[2 .. 10] mm/h"
lane_width: [1.25*ego_width .. 2.25*ego_width]
```

|  |  |
| --- | --- |
|  | No units with parameterized expressions. |

### 10.4.5.4 Parameterized expressions

The ASAM OpenODD model supports parametrization of expressions using taxonomy concepts.
Consider defining, for example like in [Code 205](#code-parameterized-expressions), the region as a parameter, and the minim speed as a second parameter:

Code 205. Example for parameterized expressions

```
TAXONOMY:
    scenery:
        ego_parameters:
            $ego_width: float length
            $ego_length: float length
            $ego_height: float length
        region_parameters:
            $region_country:
                - United States
                - Germany
            $service_area: shapefile # binary record format
        roads:
            road_width: float length
    dynamic_environment:
        $min_speed:  float velocity

MODULES:
    parameterized_module:
        INCLUDE_AND:
            region:  $region_country
            road_width: > 2*$ego_width
```

These parameters can be used in conditions as in [Code 206](#code-parameters-conditions):

Code 206. Example for parameters used in conditions

```
COD:
  - SPATIAL_EXTENT:              ...
    TEMPORAL_EXTENT:             ...
    $region;categorical_literal: Germany
    $min_speed;km/h:             5

MODULES:
    use_parameters:
        TITLE: Example of using parameters.
        INCLUDE_AND:
            country:
              - $region
            speed: > $min_speed
```

### 10.4.5.5 CategoricalLiteral with Expressions with an OD

This section is about leveraging class `CategoricalLiteral` with class `Expression` in conjunction with an OD.
Class `CategoricalLiteral` in combination with class `Expression` is helpful for modularization and parameterization.

Consider [Code 207](#code-boolean-conditions) of specifying boolean conditions using explicit thresholds:

Code 207. Example for boolean conditions

```
MODULES:
    bad_weather:
        INCLUDE_OR:
            rain_rate: "> 5 mm/h"
            wind_speed: "> 50 km/h"
```

Each location (for example country, state, and so forth) may have a different speed limit or acceptable precipitation rate for their climate.
Using this explicit approach, it is impossible to adjust these thresholds without taking local conditions into account.

Instead of using the explicit threshold conditions, we can use the taxonomy to define thresholds, as in [Code 208](#code-threshold-conditions):

Code 208. Example for threshold conditions

```
TAXONOMY:
    rain_rate: float precipitation_rate
    rain_level:
        no_rain:
            rain_rate: "0 mm/h"
        light_rain:
            rain_rate: "<= 1 mm/h"
        moderate_rain:
            rain_rate: "[1 .. 5] mm/h"
        heavy_rain:
            rain_rate: "> 5 mm/h"
    wind_speed: float velocity
    is_dangerous_wind:
        true:
            wind_speed: "> 50 km/h"
        false:
            wind_speed: "<= 50 km/h"
```

With this approach, the thresholds can be modified simply by importing a different file, as follows:

Given this taxonomy, consider the module condition like in [Code 209](#code-threshold-import):

Code 209. Example for threshold import

```
IMPORT:
   - locale_taxonomy.yml

MODULES:
    bad_weather:
        INCLUDE_OR:
            rain_level:
                - heavy_rain
            is_dangerous_wind: true
```

Moreover, the use of categorical literal with expressions further induces an order amongst the categorical literals.
It enables, for example, using the categorical literals in lower and upper bound constraints.

Consider the (undesired) explicit list expression in [Code 210](#code-list-expression):

Code 210. Example for

```
    rain_level:
        - no_rain
        - light_rain
        - moderate_rain
```

One can avoid hardcoding the full list of literals using the simplified and more-readable expression of [Code 211](#code-simplified-expression):

Code 211. Example for

```
    rain_level: < heavy_rain
```

To further illustrate the utility of the implied order between the categorical literals, consider modeling the requirement:

"If wind is below `light_breeze` the rain is up to `heavy_rain`, but if wind is stronger than `light_breeze`, wind is up to `light_rain`."

Code 212. Example for

```
ODD:
    odd1:
        INCLUDE_OR:
            windy_rain_1: true
            windy_rain_2: true
MODULES:
    windy_rain_1:
        INCLUDE_AND:
            wind_level:
                - no_wind
            rain_level: <= heavy_rain
    windy_rain_2:
        INCLUDE_AND:
            wind_level: > no_wind
            rain_level: <= light_rain
```

The ODD in [Code 212](#code-complex-expression) is interesting because it defines a union which otherwise will be difficult to express in a compact fashion:

* There are two acceptable windy rain conditions within the ODD: `windy_rain_1` and `windy_rain_2`.
* For `windy_rain_1`, we are including heavy rain without any wind.
* For `windy_rain_2`, when we have (even slight) wind, then we are limiting the acceptable rain level to `light_rain` or less,

The YAML in [Code 212](#code-complex-expression) is (relatively) easy to understand by non-programmers (for example regulators).

[Table 148](#tab-windyrainexamblecod) shows a compatible COD:

Table 148. Windy rain example compatible COD


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | rain\_level;categorical\_literal | road\_type;categorical\_literal |
| --- | --- | --- | --- | --- |
| 1 | "2023-06-01 08:12:53.784" | "45.024 10.261" | moderate\_rain | motorway |
| 2 | "2023-06-01 08:12:54.149" | "45.024 10.261" | light\_rain | local\_road |
| 3 | "2023-06-02 11:42:21.913" | "45.024 10.261" | no\_rain | bundesautobahn |

Next, consider changing the taxonomy by adding the `paved_road` as shown in [Code 213](#code-changed-taxonomy-with-paved-road).

Code 213. Example for changed taxonomy with added `paved_road`

```
TAXONOMY:
    paved_road:
        - RQ28
        - RQ31
        - RQ36
        - RQ43-5
    road_type:
        motorway:
            paved_road: [RQ31,RQ36]
        local_road:
            paved_road: RQ28
        bundesautobahn:
            paved_road: RQ43-5
```

This change does not invalidate the above OD, because the values of `motorway`, `local_road` and `bundesautobahn` are still valid.
With this approach, the above OD is equivalent to:

[Table 149](#tab-pavedroadexamblecod) shows a compatible COD.

Table 149. Paved road example compatible COD


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | rain\_level;categorical\_literal | paved\_road;categorical\_literal |
| --- | --- | --- | --- | --- |
| 1 | "2023-06-01 08:12:53.784" | "45.024 10.261" | moderate\_rain | RQ31;RQ36 |
| 2 | "2023-06-01 08:12:54.149" | "45.024 10.261" | light\_rain | RQ28 |
| 3 | "2023-06-02 11:42:21.913" | "45.024 10.261" | no\_rain | RQ43-5 |

## 10.4.6 Module export instruction format

The same specification as provided in [Section 6.2.8, "Taxonomy export instruction format"](../06_model_concept/06_02_openodd_taxonomy.html#sec-taxonomy-export-instruction-format) applies.