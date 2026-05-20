# ASAM Openodd v1.0.0 — 9.4 Modeling ODD

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/09_openscenario_dsl/09_04_modeling_odd.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.4 Modeling ODD

## 9.4.1 General definition

Modeling ODDs in ASAM OpenSCENARIO DSL is done by importing one or more domain concept definitions (taxonomies) and extending their type definitions with constraints.

## 9.4.2 Constraints

Constraints can be added to types via `keep`-statements that can be added to struct type definitions or extensions.
[Code 121](#code-constraints-keep-statements) shows how to add constraints on the `weather` type.

* The first constraint forbids wind strengths of storm and above.
* The second constraint forbids rain or, only when there is no wind, allows light rain or drizzle.
  The second constraint contains a typical example of a conditional expression that uses logical implication to express an if-then-condition:
  "If there is no wind, rain can be drizzle or light rain".

Code 121. Example constraints via keep statements (ASAM OpenSCENARIO DSL notation)

```
# Import domain concepts definition (taxonomy) file
import "Domain_Concepts_Definition_ISO_34503.osc"

extend weather:
    keep(not wind in [storm, violent_storm, hurricane])
    keep(rain == no_rain or (wind == no_wind => rain in [drizzle, light_rain]))
```

In ASAM OpenSCENARIO DSL, multiple `keep` constraints are logically equivalent to a single `keep` constraint with all expressions combined using the logical `AND` operator.
However, using separate `keep` expressions for different ODD requirements enhances readability and maintainability.

[Code 122](#code-high-constraints) shows how constraints can also be placed higher up in the struct hierarchy:

Code 122. Example of placing constraints higher-up in the struct hierarchy (ASAM OpenSCENARIO DSL notation)

```
extend odd:
    keep(not environmental_conditions.weather.wind in [storm, violent_storm, hurricane])
    keep(environmental_conditions.weather.rain == no_rain or (environmental_conditions.weather.wind == no_wind => environmental_conditions.weather.rain in [drizzle, light_rain]))
```

However, the constraints should be placed as low in the struct hierarchy as possible to avoid lengthy "dot" navigation expressions.

Sometimes, however, if constraints span aspects that are defined in different parts of the struct hierarchy, constraints must be placed in the lowest common parent struct.
Then navigating to the fields defined further downwards in the struct hierarchy via "dot" navigation expressions cannot be avoided.
[Code 123](#code-constraints-via-dot) shows how a constraint is added to the scenery struct type that forbids the presence of pedestrians for certain geographical zone that the subject vehicle is located in:

Code 123. Example constraints via dot (ASAM OpenSCENARIO DSL notation)

```
extend zone : [airport_departure_zone, airport_arrival_zone, shuttle_service_area, cargo_zone, emergency_service_area]

extend scenery:
    keep(current_zone in [shuttle_service_area, cargo_zone] => traffic.pedestrians == false)
```

Since in this example the `current_zone` field is located in the scenery struct and the `pedestrians` field is located in the `traffic` struct, which is referenced from the `scenery` struct, this is the ideal placement of this constraint.

|  |  |
| --- | --- |
|  | [Code 123](#code-constraints-via-dot) shows how to extend the `zone` enum in an ODD definition and formulate constraints that are conditional on the current location of the subject vehicle, see [Section 9.2.3, "Geographical zones"](09_02_modeling_taxonomy.html#sec-geographical-zones). |

The following example [Code 124](#code-constraints-on-same-attribute-wind-speed) also shows a case where constraints must be placed in the top-most struct `odd`, because the expressions refers to attributes that appear in different branches of domain concepts definition (taxonomy).
At the same time, the example shows a case where conditional constraints are placed on the same attribute:
The maximum allowed wind speed is `50 km/h` on highways or interstates, `100 km/h` on rural and minor roads, and `150 km/h` otherwise.

Code 124. Example constraints on the same attribute (wind-speed) (ASAM OpenSCENARIO DSL notation)

```
extend odd:
    keep(scenery.drivable_area.drivable_area_type ==
        motorways_or_highways_or_interstates
        => environmental_conditions.weather.wind_speed <= 50 kmph)
    keep(scenery.drivable_area.drivable_area_type ==
        minor_or_local_roads
        => environmental_conditions.weather.wind_speed <= 100 kmph)
    # the last constraint is a general constraint on wind_speed.
    # This constraint could be placed also on the level of the weather struct
    # to avoid the lengthy "dot" navigation, but keeping it next to the other
    # constraints above, which constrain the same attribute, improves readability.
    keep(environmental_conditions.weather.wind_speed <= 150 kmph)
```

In ODDs modeled with ASAM OpenSCENARIO DSL, constraints (`keep(…​)` statements) must be contained within structured types (structs).
The text above describes where they should ideally be placed, via type extension, in the taxonomy hierarchy.
This placement has no impact on the semantics of the condition expression.
The ASAM OpenODD model, by contrast, organizes constraints in modules (see [Section 6.4.3, "Modular conditions"](../06_model_concept/06_04_openodd_modules.html#sec-concept-modules-modular-conditions)) where the relations between modules are independent of the taxonomy hierarchy.
When mapping ASAM OpenODD ODD specifications to ASAM OpenSCENARIO DSL, the constraints expressed in modules are translated to `keep(…​)` statements.
See [Section 9.5.4.7, "Mapping constraints over taxonomy attributes"](09_05_mapping_model_to_osc_dsl.html#sec-mapping-constraints-over-taxonomy-attribute) on how to map ASAM OpenODD model constraints to ASAM OpenSCENARIO DSL.

The constraint expressions must evaluate to a Boolean value, which means `true` or `false`, and can be formed using field identifiers, literal values (enum values, primitive values, physical values with units), range expressions, list expressions, logical-, arithmetic-, and relational operators, as well as list-membership operators.
Details on the expression syntax of ASAM OpenSCENARIO DSL can be found in Section 7.4, "Expressions" of ASAM OpenSCENARIO DSL [[2](../bibliography.html#bib-oscdsl)].

## 9.4.3 Specifying definition modes

Each domain concepts definition (taxonomy) struct provides a field `definition_mode`, see [Section 9.2.4, "Definition modes"](09_02_modeling_taxonomy.html#sec-definition-modes), which represents the definition mode assigned to the fields in this struct.
This implies that different definition modes can be specified on the level of structs, but not on the granularity of single fields (taxonomy leaves).

There are the four modes `default`, `permissive`, `restrictive`, and `parent`.
The semantics of the definition modes are the following:

* `default`: If the definition mode for a struct is `_default`, the values of fields of that struct that do not appear in any ODD definition constraints are unspecified by the ODD.
  The ODD does not make any statement about whether a certain value of this field is allowed or not.
* `permissive`: If the definition mode for a struct is `permissive`, all the values of the fields in that struct are permitted, unless they are constrained any ODD definition constraint.
* `restrictive`: If the definition mode for a struct is `restrictive`, all the values of the fields in that struct are forbidden, unless the field appears in any ODD definition constraint.
  In the case that the field appears in any ODD definition constraint, all values are permitted that are valid with respect to the ODD definition constraints.
* `parent`: If the definition mode for a struct is `parent`, the definition mode of that struct is inherited from the parent struct in the domain concepts definition (taxonomy) struct hierarchy.
  The parent struct can in turn have the definition model `parent`, so that the definition modes are recursively defined by the first parent structure, which is higher up in the hierarchy of the domain concept definition (taxonomy) and defines a different definition mode.

[Code 125](#code-permissive-definition-mode) shows how to define the `permissive` definition mode for the whole ODD, but define a `_default` definition mode for the weather aspects:

Code 125. Example permissive definition mode (ASAM OpenSCENARIO DSL notation)

```
extend odd:
    keep(definition_mode == permissive)

extend weather:
    keep(definition_mode == _default)
```

Defining constraints on the `definition_mode` as shown in [Code 125](#code-permissive-definition-mode) overrides the default constraints in the domain concepts definition (taxonomy) structs, see [Section 9.2.4, "Definition modes"](09_02_modeling_taxonomy.html#sec-definition-modes).

If no definition mode is defined in an ODD definition and the default value `parent` is not overridden by any constraints as shown in [Code 125](#code-permissive-definition-mode), then the default mode interpretation holds for the complete ODD definition.
[Code 126](#code-default-definition-mode) shows the default definition mode for the root struct:

Code 126. Example default definition mode (ASAM OpenSCENARIO DSL notation)

```
extend odd:
    keep(definition_mode == _default)
```

## 9.4.4 Parametrization

One way of making ODDs easily customizable is to parameterize ODD definitions.
This requires three different models:

* A domain concepts definition model (taxonomy) that defines special fields that serve as parameters.
* A parameterized ODD definition that specifies constraints where, instead of constraining fields against particular boundary values, it refers to the parameter fields.
* A concrete ODD definition that imports and extends a parameterized ODD definition, but now defines concrete values for the parameter fields, so that all constraints of the parameterized ODD definition now constrain against concrete boundary values.

[Code 127](#code-parameterized-odd-definition1) shows an example of the definition and concrete application of such a parameterized ODD definition.

First, the domain concepts definition model (taxonomy) defines parameter fields.
A naming convention may be chosen to help distinguish parameter fields from other fields.

ASAM OpenSCENARIO DSL parameters are regular variable names in the language.
As such it is suggested to adapt a naming convention in order to identify parameters generated from the ASAM OpenODD mapping.
For example, the prefix `param_` can be added to indicate that these are ASAM OpenODD originated parameters.
The parameter fields are first defined in the definition model (taxonomy).

Code 127. Example 1 parameterized ODD definition (ASAM OpenSCENARIO DSL notation)

```
# (1) domain concepts definition model (taxonomy)
# Domain_Concepts_Definition_ISO_34503.osc

...

struct subject_vehicle inherits odd_element:
    # normal taxonomy fields
    speed : speed
    ...
    # parameter fields:
    param_max_subject_vehicle_speed : speed
    ...

struct lane_dimensions inherits odd_element:
    # normal taxonomy fields
    width: meters
    height: meters
    ...
    # parameter fields:
    param_min_lane_width : length
    ...


struct weather inherits odd_element:
    # normal taxonomy fields
    ambient_air_temperature : temperature
    wind : wind_kind # (10.2.3)
    rainfall : rain_kind
    snowfall : snow_kind
    ...
    # parameter fields:
    param_forbidden_wind_kinds : list of wind_kind
    ...
```

[Code 128](#code-parameterized-odd-definition2) shows how a parameterized ODD definition imports this domain concepts definition model (taxonomy) and formulates constraints based on the parameter fields:

Code 128. Example 2 parameterized ODD definition (ASAM OpenSCENARIO DSL notation)

```
# (2) Parameterized ODD definition
# Parameterized_ODD_Definition_ISO_34503.osc

import "Domain_Concepts_Definition_ISO_34503.osc"

extend subject_vehicle:
	keep(speed <= param_max_subject_vehicle_speed)
    ...

extend lane_dimensions:
    keep(width >= param_min_lane_width)
    ...

extend weather:
    keep(not (wind in param_forbidden_wind_kinds))
    ...
```

[Code 129](#code-concrete-odd-definition) shows a concrete ODD definition that imports the parameterized ODD definition and specifies concrete values for the parameter fields by using constraints:

Code 129. Example concrete ODD definition (ASAM OpenSCENARIO DSL notation)

```
# (3) Concrete ODD definition
# ODD_Shuttle_Service_Barcelona_Airport.osc

import "Parameterized_ODD_Definition_ISO_34503.osc"

extend subject_vehicle:
	keep(param_max_subject_vehicle_speed == 120.0 kmph)
    ...

extend lane_dimensions:
    keep(param_min_lane_width == 4.2m)
    ...

extend weather:
    keep(param_forbidden_wind_kinds == [storm, violent_storm, hurricane])
    ...
```