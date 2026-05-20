# ASAM OpenODD® v1.0.0 — 10.2 Taxonomy mapping

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/10_yaml/10_02_openodd_export_taxonomy_yaml.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.2 Taxonomy mapping

## 10.2.1 Modeling taxonomies

Consider the following example compliant taxonomy:

* The root concept is called `environment_conditions`.
* The `wind` conditions are specified using a `wind_speed` numeric attribute.
* The `rainfall` conditions are specified using a `rainfall_rate` numeric attribute.
  In addition, a `rainfall_type` defines the three rain categories of `dynamic`, `convective` and `orographic`.

|  |  |
| --- | --- |
|  | In some parsers it might be needed to add double quotes to codes like `wind_speed: float velocity` to `wind_speed: "float velocity"`. |

The example taxonomy can be specified using [Code 166](#code-example-taxonomy-yaml-specification):

Code 166. YAML specification for example taxonomy

```
TAXONOMY:
    environmental_conditions:                             # This is a Record.
        weather:                                          # This is a Record.
            wind:                                         # This is a Record.
                wind_speed: float velocity                # This is an attribute of type "float" having a unit type of "velocity".
            rainfall:                                     # This is a Record.
                rainfall_rate: float precipitation_rate   # This is an attribute of type "float" having a unit type of "precipitation_rate".
                rainfall_type:                            # This is an attribute of type Categorical.
                    - dynamic                             # This is a Categorical Literal specified by the categorical_literal symbol "dynamic".
                    - convective                          # This is a Categorical Literal specified by the categorical_literal symbol "convective".
                    - orographic                          # This is a Categorical Literal specified by the categorical_literal symbol "orographic".
```

The advantage of this format is that:

* Each line represents a single `TaxonomyConcept`.
  The type is implicit as illustrated in the comments.
* It is easy to parse and interpret using standard YAML tools.
* It is easy for non-technical individuals (for example, regulators) to read and understand the taxonomy.

## 10.2.2 Attribute mappings

### 10.2.2.1. Numeric `TaxonomyConcept`

A numeric `TaxonomyConcept` is specified by a `PrimitiveType` followed by the `UnitType`.

|  |  |
| --- | --- |
|  | A numeric `TaxonomyConcept` is verified against an `Expression` referring to this `TaxonomyConcept`. |

[Code 167](#code-example-numeric-taxonomy-element) shows an example for a numeric `TaxonomyConcept`.

Code 167. Example of a numeric `TaxonomyConcept`

```
TAXONOMY:
    rainfall_rate: float precipitation_rate
```

### 10.2.2.2. Boolean `TaxonomyConcept`

A Boolean `TaxonomyConcept` is specified by a Boolean keyword but without a `UnitType`.

|  |  |
| --- | --- |
|  | A Boolean `TaxonomyConcept` is verified against an `Expression` referring to this `TaxonomyConcept`. |

[Code 168](#code-example-boolean-taxonomy-element) shows an example for a Boolean `TaxonomyConcept`.

Code 168. Example of a Boolean `TaxonomyConcept`

```
TAXONOMY:
    is_dangerous: boolean
```

### 10.2.2.3. Categorical `TaxonomyConcept`

A categorical `TaxonomyConcept` is specified by providing a list of instances of class `CategoricalLiteral`.

[Code 169](#code-example-categorical-taxonomy-element) shows two examples for a categorical `TaxonomyConcept`.

Code 169. Example of a categorical `TaxonomyConcept`

```
TAXONOMY:
    rainfall_level:
        - light_rain
        - moderate_rain
        - heavy_rain
        - violent_rain
        - cloud_burst
    fog_level: [fog_not_detectable, fog_mist, fog_medium, fog_heavy, fog_thick]
```

|  |  |
| --- | --- |
|  | YAML notation hint  In YAML a sequence can be defined either in one or multiple lines. |

`CategoricalLiteral` `Value` instances may specify instances of `Range`, according to `replace by range constraints`.
Each instance of class `CategoricalLiteral` range shall have its unit specified to avoid ambiguities as its unit type may have multiple units referring to it.

Code 170. Example of instances of class `CategoricalLiteral` values with ranges

```
TAXONOMY:
    rainfall_rate: float precipitation_rate
    rainfall_level:
        no_rain:
            rainfall_rate: "< 0.1 mm/h"
        light_rain:
            rainfall_rate: "[0.1 .. 2.5] mm/h"
        moderate_rain:
            rainfall_rate: "[2.5 .. 7.6] mm/h"
        heavy_rain:
            rainfall_rate: "[7.6 .. 50] mm/h"
        violent_rain:
            rainfall_rate: "[50 .. 100] mm/h"
        cloud_burst:
            rainfall_rate: "> 100 mm/h"
```

|  |  |
| --- | --- |
|  | The quotes are added to ensure the validity of the YAML. A simple pre-processor can be used to add them in to avoid the need to specify them manually. |

Instances of class `Categorical` may refer to instances of class `Expression` in order to define Boolean thresholds.
The `TaxonomyConcept` used within those expressions shall be uniform and of numeric type.
There shall be a single `UpperBound` and a single `LowerBound` `Expression` type.
A single common numeric `Attribute` instance used both `UpperBound` and `LowerBound` `Expression` instances.
The threshold by the `Condition` instances shall be identical.

[Code 171](#code-example-categorical-boolean) shows an example of `CategoricalLiteral` instances with Boolean thresholds.

Code 171. Example of categorical literals with Boolean thresholds

```
TAXONOMY:
    environment_conditions:                # record
        wind_speed: float velocity         # numerical attribute
        is_dangerous_wind:                 # categorical
            true:                          # categorical literal (*not* boolean primitive type)
                wind_speed: "> 50 km/h"    # upper bound expression
            false:                         # categorical literal (*not* boolean primitive type)
                wind_speed: "<= 50 km/h"   # lower bound expression
```

Instances of class `CategoricalLiteral` may be associated with `Range` `Expression` instances to define the thresholds associated with multiple levels.
The `TaxonomyConcept` used within those expressions shall be uniform and of numeric type.
The `Expression` shall satisfy:

* A single `UpperBound` `Expression`.
* A single `LowerBound` `Expression`.
* All others shall be `Range` `Expression`.

The ranges used by the conditions shall cover the entire range of possible values for the numeric type.

[Code 172](#code-example-range-expressions) shows as example a representation of fog levels in terms of visibility ranges.

Code 172. Example of categorical literals with range expressions

```
TAXONOMY:
    environment_conditions:                              # record
        fog_visibility_range: float length               # numeric attribute
        fog_level:                                       # categorical attribute
            fog_not_detectable:                          # categorical literal
                fog_visibility_range: "> 1609 m"         # lower bound expression
            fog_mist:                                    # categorical literal
                fog_visibility_range: "[805 .. 1609] m"   # range expression
            fog_medium:                                  # categorical literal
                fog_visibility_range: "[450 .. 805] m"    # range expression
            fog_heavy:                                   # categorical literal
                fog_visibility_range: "[50 .. 450] m"     # range expression
            fog_thick:                                   # categorical literal
                fog_visibility_range: "< 50 m"             # upper bound expression
```

|  |  |
| --- | --- |
|  | The quotes are added to ensure the validity of the YAML. A simple pre-processor can be used to add them in to avoid the need to specify them manually. |

For such instances of class `CategoricalLiteral`, the range expression induces an order.
In [Code 172](#code-example-range-expressions) the induced order is as follows:

`fog_not_detectable` < `fog_mist` < `fog_medium` < `fog_heavy` < `fog_thick`

The ranges within the expressions determine the order.
The sequence of the expressions in the ASAM OpenODD® specification file is not relevant.

`CategoricalLiteral` instances may refer to expressions which specify a list of values from other categorical concepts.
Consider to define road types based on German `paved_road` classifications [[12](../bibliography.html#bib-guidelinesmotorways)] as shown in [Code 173](#code-example-motorway-design).

Code 173. Example of referred categorical literals

```
TAXONOMY:
    paved_road:
        - RQ28
        - RQ31
        - RQ36
        - RQ43-5
    road_type:
        motorway:
            paved_road: [RQ31, RQ36] # categorical list expression
        local_road:
            paved_road: RQ28         # categorical list expression
        bundesautobahn:
            paved_road: RQ43-5       # categorical list expression
```

|  |  |
| --- | --- |
|  | YAML notation hint  In YAML `[XX, XY, XZ]` is an alternate way to express multiple possible values without using multiple lines. |

### 10.2.2.4 User defined types

User defined types are supported via the `Record` class (see [Section 6.2.5, "User defined types"](../06_model_concept/06_02_openodd_taxonomy.html#sec-concept-taxonomy-user-defined-types)).

[Code 174](#code-example-user-type) shows an example of a user defined type.

Code 174. Example of a user type object

```
TAXONOMY:
    reusable_object:        # record
        vector:             # any record can be a user define re-usable struct, or class
            x: float length # numeric attribute
            y: float length # numeric attribute
            z: float length # numeric attribute
```

[Code 175](#code-example-user-type-complex) shows a more complex re-usable object specification.

Code 175. Example of a more complex user type object

```
TAXONOMY:
    vector_types:                              # record
        cartesian_vector:                      # record
            x: float length                    # numeric attribute
            y: float length                    # numeric attribute
            z: float length                    # numeric attribute
        radial_vector:                         # record
            r: float length                    # numeric attribute
            a: float angle                     # numeric attribute
    dynamic_environment:                       # record
        vehicle:                               # record
            vehicle_position: cartesian_vector # complex attribute
            vehicle_trajectory: radial_vector  # complex attribute
            vehicle_velocity: radial_vector    # complex attribute
            vehicle_type:                      # categorical
                - motorcycles                  # categorical literal
                - cars                         # categorical literal
                - trucks                       # categorical literal
        vru:                                   # record
            vru_position: cartesian_vector     # complex attribute
            vru_trajectory: radial_vector      # complex attribute
            pedestrian:                        # categorical
                - adult                        # categorical literal
                - child                        # categorical literal
                - stroller                     # categorical literal
            cyclist:                           # categorical
                - bicycle                      # categorical literal
                - tricycle                     # categorical literal
```

In this example, records are used to specify the two user-defined objects of `cartesian_vector` and `radial_vector`.
In addition, a record is used to specify the re-usable `vehicle` object.

### 10.2.2.5 Measures

Measures are regarded as regular instances of class `Attribute` (see [Section 6.2.6, "Measures"](../06_model_concept/06_02_openodd_taxonomy.html#sec-concept-taxonomy-measures)).
The name of a measure `Attribute` instance shall have the dot notation format `<element_name>.<measure_name>`.
A measure name shall satisfy the same requirements as a `TaxonomyConcept`.
A measure type shall be `float` or `integer`.

[Code 176](#code-example-measures) shows an example for measures.

Code 176. Example of measures

```
heavy_rain.duration: float time
oil_contamination.depth: float length
pollen_contamination.length: float length
black_ice.occurrence: float risk
```

## 10.2.3 Unit mappings

A `TaxonomyConcept` instance shall reference zero or one `UnitType` instance.
Each `UnitType` instance may be referenced by zero or more `Unit` instances.
Each `Unit` instance specifies:

* ID: A unique string identifying the unit, for example `meters_per_sec`.
* name: A name used for display but may not be unique; it is not translated to multiple languages.
* factor: Used for translation per ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)]
* offset: Used for translation per ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)]

[Code 177](#code-example-basic-unit-types) shows the basic unit types that are supported and that are associated with reserved keywords.

Code 177. Basic unit types

```
unit_types:
    - length
    - area
    - volume
    - angle
    - force
    - weight = force
    - duration
    - time
    - count
    - fraction # (for example, 0.315), % is fraction * 100
    - temperature
    - frequency
    - charge
    - illuminance
    - luminous_flux
    - sound_intensity
    - cloud_coverage
    - grains
    - electric_potential
    - electric_current
    - electric_current_density
    - power
    - data_size
    - velocity = length / time
    - precipitation_rate = length / time # not volume over time
    - occurrence = count / time
    - bandwidth = data_size / time
    - pressure = force / area
    - torque = force * length
    - acceleration = velocity / time^2
    - risk = occurrence / time
    - reliability = occurrence / time
    - confidence = occurrence / count
    - percentile = count / count
```

Unit conversion is performed between units sharing a scale factor.
The conversion specification needs to provide the scale factor between every pair of units.
[Code 178](#code-example-unit-conversion) shows an example for the length conversions using YAML.

Code 178. Example of unit conversions

```
conversion:
    temperature:
        C:
            F:
                scale: 1.8
                offset: 32
            K:
                scale: 1.0
                offset: 273.15
    length:
        m:
            mm:
                scale: 1000
                offset: 0
            cm:
                scale: 100
                offset: 0
            km:
                scale: 0.001
                offset: 0
            in:
                scale: 39.37008
                offset: 0
            mi:
                scale: 0.00062
                offset: 0
```

With this specification, conversion from `m` to `mm` multiplies the number by 1000.
Similarly, conversion from `m` to `km` multiplies the number by `0.001`.