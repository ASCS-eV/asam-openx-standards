# ASAM Openodd v1.0.0 — 9.2 Modeling taxonomy

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/09_openscenario_dsl/09_02_modeling_taxonomy.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.2 Modeling taxonomy

## 9.2.1 Modeling structured taxonomies for ODDs

A taxonomy is modeled by using ASAM OpenSCENARIO DSL `struct`, which provides a way to build complex structured types from simpler types.
A `struct` can have multiple instances of `field` and multiple instances of `method`.
A `field` represents a named attribute of a `struct` that can be typed over:

* `structs`
* primitive types, like float, Boolean, integer, or string
* enumerated types
* physical types
* lists of the above

ASAM OpenSCENARIO DSL distinguishes **parameter** fields and **variable** fields.
Parameter fields are immutable and their value must be defined during the creation of struct instances, while variable fields can change over time.
Taxonomies use parameter fields.

This implies that a mapping (see [Section 9.1.5, "Illustrative overview"](09_01_overview.html#sec-illustrative-overview)) from a world or a simulation state to a COD must create a new COD instance whenever the world or simulation state changes.
Depending on the supporting tool, this may be realized differently.

[Code 110](#code-modeling-odd-taxonomy) shows how structs and parameter fields are used to model a taxonomy with ASAM OpenSCENARIO DSL.
The "root" type is the struct `odd`.
This example ODD struct has two parameter fields `environmental_conditions` and `scenery`, which are again typed over other structs.
The struct `environmental_conditions` has a field `weather`, typed over a struct that has the fields `wind` and `rainfall`.
These fields are typed over the enumerated (`enum`) types `wind_kind` and `rain_kind`.

|  |  |
| --- | --- |
|  | The ASAM OpenSCENARIO DSL convention is that all names, which includes type and field names, are written with lowercase letters and words separated by underscores. |

|  |  |
| --- | --- |
|  | ASAM OpenSCENARIO DSL requires that all fields of a structured type (struct) have unique names. This also prohibits name clashes between inherited fields or fields in type extensions. However, it is allowed that two fields of two different structs have the same name or that a field has the same name as another type. In contrast, the ASAM OpenODD model (see [Section 6.1.5, "Taxonomies in ASAM OpenODD"](../06_model_concept/06_01_openodd_model.html#sec-taxonomies-in-this-standard)) requires that all named elements have unique IDs. When aligning or mapping taxonomies and ODDs across these formats, this restriction must be considered. |

In the following code examples, the following conventions are used:
Taxonomy structs fields/members and their types will have the same name.
For example: `scenery : scenery` implies a `scenery` struct field, of type `scenery`.
For enumerated (categorical) types, the type defined is `_kind` (for example `wind_kind`), while the field/member name is "as is" (for example `wind)`.

Code 109. Example for naming conventions for taxonomy examples (ASAM OpenSCENARIO DSL notation)

```
struct environmental_conditions:
    weather : weather

struct weather:
    wind : wind_kind
```

Code 110. Example modeling of a taxonomy (ASAM OpenSCENARIO DSL notation)

```
struct odd:
	environmental_conditions : environmental_conditions
	scenery : scenery

struct environmental_conditions:
	weather : weather

struct weather:
 	wind : wind_kind
 	rainfall : rain_kind

enum wind_kind: [
    no_wind,
    calm,
    light_air,
    light_breeze,
    gentle_breeze,
    moderate_breeze,
    fresh_breeze,
    strong_breeze,
    near_gale,
    gale,
    strong_gale,
    storm,
    violent_storm,
    hurricane]

enum rain_kind: [
    no_rain,
    drizzle,
    light_rain,
    moderate_rain,
    heavy_rain,
    violent_rain,
    cloudburst]

struct scenery:
    ...
```

## 9.2.2 Primitive types, physical dimensions, and units

Fields can be typed over the **primitive types** `bool` (Boolean), `int` and `uint` (integer and unsigned integer, 64-bit), `float` (floating-point, 64-bit), and `string` (sequence of unicode characters).

|  |  |
| --- | --- |
|  | The term *physical type* is matching the class `UnitType` of the ASAM OpenODD model. |

Moreover, fields can be typed over **physical types**.
A physical type is defined by a name and a **basic unit definition** based on the SI base units:

* second (**s**, the unit of time)
* meter (**m**, length)
* kilogram (**kg**, mass)
* ampere (**A**, electric current)
* kelvin (**K**, temperature)
* mole (**mol**, amount of substance)
* candela (**cd**, luminous intensity)

[Code 111](#code-physical-type-definition) shows an example of a physical type definition, which defines the physical types `speed` and `acceleration` based on the SI-units m (meter) and s (seconds).
The definition indicates the exponents:

* Speed is length divided by time.
  The time exponent is negative one.
* Acceleration is length divided by time squared.
  The time exponent is negative two.

Code 111. Example physical type definition (ASAM OpenSCENARIO DSL notation)

```
type speed is SI(m: 1, s: -1)
type acceleration is SI(m: 1, s: -2)
```

**Units** can be defined on the basis of physical type definitions by introducing a unit name, a conversion factor, and an offset from the physical type unit definition.
[Code 112](#code-defining-units) is an example, that measures speed in unit kilometers per hour:

Code 112. Example for defining a unit (ASAM OpenSCENARIO DSL notation)

```
unit kmph of speed is SI(m: 1, s: -1, factor: 0.277777778)
```

[Code 113](#code-odd-taxonomy-structs) shows taxonomy structs that have fields typed over primitive and physical types:

Code 113. Example taxonomy structs (ASAM OpenSCENARIO DSL notation)

```
struct scenery:
    traffic : traffic

struct traffic:
    pedestrians : bool
    traffic_speed : speed
```

## 9.2.3 Geographical zones

As illustrated in [Figure 23](09_01_overview.html#fig-overview-geo-zones-in-a-scenario-based-v-v-process), geographical zones are represented by an enum type, for example `zone`.

Within a taxonomy, the authors of ODD specifications should be able to specify restrictions that may depend on the geographical zone in which the vehicle in question is currently located.

To enable the specification of such constraints, the taxonomy must provide two elements:

* A field that represents the *current zone* in which the subject vehicle is located.
  Its value must be derived by a world-state-to-COD mapping, see [Figure 23](09_01_overview.html#fig-overview-geo-zones-in-a-scenario-based-v-v-process).
* Define an enum datatype for such a field:
  This enumeration can already contain values if specific geographical zones are already defined at the taxonomy level.
  Should this not be the case, the enum may only define one enum value, for example `zone_undefined`, which represents an undefined geographical location.
  In an ODD definition, this enum type can be extended to add ODD-definition-specific geographical zones.

Example:

Code 114. Example enum datatype (ASAM OpenSCENARIO DSL notation)

```
struct odd:
    ...
	scenery : scenery

struct scenery:
	...
    current_zone : zone

enum zone: [ zone_undefined ] # to be extended in ODD definitions.
```

## 9.2.4 Definition modes

|  |  |
| --- | --- |
|  | Definition modes is a concept/feature introduced by ISO 34503 [cite:iso34503]. This concept is not standardized by this release of ASAM OpenODD. Please note that there may be different ODD formats which may enable to express more concepts/features than those standardized in this release of ASAM OpenODD. In these cases, it is left up to the implementation to ensure if a modeled ODD/OD/COD is still compliant with ASAM OpenODD. |

The ISO 34503 introduces three different definition modes *default*, *permissive*, and *restrictive*, which specify what attribute values are allowed when no constraints are specified for some attributes [cite:iso34503].
The ODD definition modes *default*, *permissive*, and *restrictive* can be defined separately for each concept (struct) of the ODD domain concepts definition (taxonomy).

To model this in ASAM OpenSCENARIO DSL, each taxonomy concept struct should have a field `definition_mode` typed over the `enum definition_mode: [_default, permissive, restrictive, parent]` that represents the three different definition modes.
The fourth value, `parent`, is not a definition mode itself, but expresses that a struct’s definition mode shall be derived from the definition mode of the parent in the domain concepts definition (taxonomy) struct hierarchy.
The enum value for the default definition mode is written with a leading underscore, because `default` is a reserved keyword in ASAM OpenSCENARIO DSL.

Defining a `definition_mode` field for every struct in the domain concepts definition (taxonomy) model can be achieved by defining a strut supertype that defines this field and then have all other structs inherit from it.
ODD domain concepts definition (taxonomy) authors can also choose other ways of introducing this property.

In the example below (see [Code 115](#code-enum-definition-mode)), the struct is called supertype `odd_element` and set its definition `parent` via a *default constraint*.
Default constraints in ASAM OpenSCENARIO DSL is a constraint that can be overridden by subtypes or type extensions, see ASAM OpenSCENARIO DSL [[2](../bibliography.html#bib-oscdsl)] specification, Section 7.3.11.3.2, "Default constraints".

If now, in an ODD, the definition mode for the root struct `struct odd` is constrained to another value, for example `permissive`, this means that the ODD shall be interpreted in permissive mode across the full domain concepts definition (taxonomy) hierarchy.
This is because all other structs retain their definition mode `parent` as defined by the default constraint and thus, the definition mode set for the root struct holds recursively for all child structs further downward in the struct hierarchy.
Once another definition mode is specified for another struct, then this definition mode holds recursively for all of its child structs further downward in the struct hierarchy.

If an ODD does not constrain the definition mode of the root struct to another value than `parent`, then the definition mode for the ODD is undefined.
This release of ASAM OpenODD does not define how this shall be interpreted.
It may be that the assumed definition mode in this case is `_default` or it may be seen as invalid not to constrain the definition mode of the root struct to another value than `parent`.

Code 115. Example enum definition mode (ASAM OpenSCENARIO DSL notation)

```
enum definition_mode: [_default, permissive, restrictive, parent]

struct odd_element:
    definition_mode : definition_mode
    keep (default definition_mode == parent)

struct odd inherits odd_element:
	environmental_conditions : environmental_conditions
	scenery : scenery
    ...

struct environmental_conditions inherits odd_element:
	weather : weather
    ...

struct weather inherits odd_element:
    wind : wind_kind
    rainfall : rain_kind
    ...

...
```

## 9.2.5 Sampling time and location

The root struct `odd` can be equipped with sampling time and location metadata.
This can be done for example as shown in [Code 116](#code-sampling-time-and-location).
The struct types `geo_location_3D` and `date_time` can be used to capture the sampling time and location in a COD, which is an instance of the type `odd`.

The `SPATIAL_EXTENT` and `TEMPORAL_EXTENT` from the ASAM OpenODD model can be mapped to the fields `geo_location_3D` and `date_time` as can be seen in [Code 116](#code-sampling-time-and-location).
The valid ranges for the fields are given in the comments.

Code 116. Example sampling time and location (ASAM OpenSCENARIO DSL notation)

```
type length is SI(m: 1)
type angle is SI(rad: 1)
type time is SI(s: 1)

struct odd:
    ...
    sampling_metadata : sampling_metadata

struct sampling_metadata:
    sampling_time : date_time
    sampling_location : geo_location_3D

struct geo_location_3D:
    latitude: angle  # Valid range: -90 to 90 degrees
    longitude: angle  # Valid range: -180 to 180 degrees
    altitude: length  # Typically no less than -400 meters (below sea level)

struct date_time:
    year: int  # calendar year, four-digit value, based on Gregorian calendar
    month: int  # calendar month, Valid range: 1 to 12
    day: int  # calendar day, valid range: 1 to 31
    hour: time  # use unit h, valid range: 0 to 23 h
    minute: time  # use unit min, valid range: 0 to 59 min
    second: time  # use unit s, valid range: 0 to 59 s
    millisecond: time  # use unit ms, valid range: 0 to 999 ms
```

## 9.2.6 Extending ODD domain concepts

ODD domain concept definitions (taxonomies) can be extended in two ways, by using *type extension* or *inheritance*.

* **Type extension**: By using type extension, a struct type can be extended with additional fields and constraints without introducing a new struct subtype.
* **Inheritance**: Inheritance introduces a new struct type that is a specialization of another struct type.
  The subtype inherits all fields and constraints from its supertype and can introduce additional fields.

|  |  |
| --- | --- |
|  | When to use type extension?  Type extension is used to extend an existing type across all its usages, effectively evolving the definition of that type for the whole scope in which the type extension is visible. The type extension is visible in the ASAM OpenSCENARIO DSL file where it is defined and all files that import that file. Type extension is suited if the goal is to extend a type in an existing struct hierarchy and when the addition is universally applicable, which means that one does not need to distinguish between the original type and the extended one. Type extension can also be used to add new enum literals to existing enum types. This is useful if an existing range of categories needs to be extended. |

|  |  |
| --- | --- |
|  | When to use inheritance?  Inheritance can be used to introduce a new type that builds upon an existing one. This new type, however, does not replace the existing type and does not automatically become part of an existing struct hierarchy (taxonomy). Instead, if a struct attribute shall be typed over the new, specialized struct, that attribute must be defined in a new struct as well. This means that inheritance is suited if the goal is to create a specialized struct type that can be integrated into a new struct hierarchy. |

Both type extension and inheritance, combined with the ability to import ASAM OpenSCENARIO DSL files to other ASAM OpenSCENARIO DSL files, allows ODD domain concepts definition (taxonomy) authors to extend existing ODD domain concepts definitions (taxonomies) or reuse parts of existing ODD domain concepts definitions (taxonomies) to create new ones.

[Code 117](#code-extending-odd-domain-concepts) shows an example of how to use type extension to extend an existing struct as well as to extend an existing enum type.
The example code first imports an existing ODD domain concepts definition (taxonomy) file `Domain_Concepts_Definition_ISO_34503.osc`.
We assume that the imported file contains a struct type `weather` and an enum type `rain_kind`.
The example code shows how the weather type is extended with a new attribute `cloud_cover` that did not yet exist in the weather struct definition in the imported `Domain_Concepts_Definition_ISO_34503.osc`.
The attribute `cloud_cover` is typed over the enum type `cloud_cover_type` that is introduced as a new enum type, without extending an existing one.
The second type extension happens to the `rain_kind` enum type, which is extended with additional rain categories, `mist` and `monsoon_rain`.

Code 117. Example extension of ODD domain concepts (ASAM OpenSCENARIO DSL notation)

```
# Import existing domain concepts definition (taxonomy) file
import "Domain_Concepts_Definition_ISO_34503.osc"

# extend weather struct type with new field
extend weather:
    cloud_cover : cloud_cover_type

enum cloud_cover_type: [clear, mostly_clear, partly_cloudy, mostly_cloudy, overcast]

# Extend rain_kind sub-type (enum) with new rain categories
extend rain_kind : [mist, monsoon_rain]
```

[Code 118](#code-using-inheritance) shows how to use inheritance to introduce a new struct type `special_weather` that specializes the struct type `weather` from an imported ASAM OpenSCENARIO DSL file, `Domain_Concepts_Definition_ISO_34503.osc`.

This new, specialized struct type `special_weather` can be integrated into a new struct hierarchy (taxonomy), for example by creating a new struct `special_odd` that has an attribute typed over `special_weather`.

Code 118. Example use of inheritance "Domain\_Concepts\_Definition\_ISO\_34503\_MyExtended.osc" (ASAM OpenSCENARIO DSL notation)

```
# Import existing domain concepts definition (taxonomy) file
import "Domain_Concepts_Definition_ISO_34503.osc"

struct special_weather inherits weather:
    cloud_cover : cloud_cover_type

enum cloud_cover_type: [clear, mostly_clear, partly_cloudy, mostly_cloudy, overcast]

struct special_odd:
    weather : special_weather
    ...
```

|  |  |
| --- | --- |
|  | The purpose for the two code examples (type extension in [Code 117](#code-extending-odd-domain-concepts) and inheritance in [Code 118](#code-using-inheritance)) is different: The type extension is used to evolve an existing type (weather) by adding a new attribute (cloud\_cover), ensuring that all instances of weather—wherever they are used—now include this new attribute. This approach is suitable where one does not require distinguishing between the original and extended versions.  In contrast, inheritance in [Code 118](#code-using-inheritance) is used to create a distinct, specialized type (special\_weather) that builds upon weather but remains separate. This allows special\_weather to be part of a new struct hierarchy while maintaining compatibility with weather. This approach is useful when the goal is to introduce variations of an existing type rather than modifying it globally. |