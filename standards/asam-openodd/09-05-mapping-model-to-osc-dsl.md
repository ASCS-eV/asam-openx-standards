# ASAM Openodd v1.0.0 — 9.5 Mapping ASAM OpenODD to ASAM OpenSCENARIO DSL

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/09_openscenario_dsl/09_05_mapping_model_to_osc_dsl.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.5 Mapping ASAM OpenODD to ASAM OpenSCENARIO DSL

## 9.5.1 Overview

This section defines how to map ODD definitions as well as COD data from the ASAM OpenODD model to ASAM OpenSCENARIO DSL.
This mapping definition is split into three parts:

1. Mapping taxonomies in the form of ASAM OpenODD model to ASAM OpenSCENARIO DSL types [Section 9.5.2, “Taxonomy mapping”](#sec-dsl-taxonomy-mapping).
2. Mapping COD and OD data to ASAM OpenSCENARIO DSL compare [Section 9.5.3, “COD/OD mapping”](#sec-mapping-dsl-cod-od).
3. Mapping ODD modules, which are used in the ASAM OpenODD model to encode constraints, to ASAM OpenSCENARIO DSL expression [Section 9.5.4, “ODD module mapping”](#sec-mapping-dsl-odd-module).

## 9.5.2 Taxonomy mapping

### 9.5.2.1 Overview

The model of ASAM OpenODD describes how to represent a  [Section 6.2, "Taxonomy"](../06_model_concept/06_02_openodd_taxonomy.html#top-openodd-taxonomy):
A file can contain multiple taxonomies.
Each taxonomy can have multiple root taxonomy concepts, which again can be containers that contain other taxonomy concepts, hence giving rise to a hierarchy of taxonomy concepts.
A taxonomy concept contained by either a container or directly by a taxonomy can also be a primitive type, a categorical type (with categorical literals), or a record (with attributes).

[Figure 24](#fig-taxonomy-model-to-osc-mapping-overview) gives an overview of how concepts for representing taxonomies in the ASAM OpenODD model are mapped to ASAM OpenSCENARIO DSL concepts:

1. Each free-form notation file is mapped to an ASAM OpenSCENARIO DSL file where import references are mapped as import statements.
2. Taxonomies, containers and records are mapped to structs.
3. Records' attributes are mapped to fields or structs.
4. Categorical types and their literals are mapped to enumeration type definitions with enumeration literals.
5. Primitive types are mapped to ASAM OpenSCENARIO DSL built-in primitive types, limited to bool, int, float, and string supported.

![ASAM OpenODD model to ASAM OpenSCENARIO DSL mapping overview](../_images/OpenSCENARIO_DSL/mapping-OpenODD-model-OSC-overview.svg)

Figure 24. ASAM OpenODD model to ASAM OpenSCENARIO DSL mapping overview

[Figure 24](#fig-taxonomy-model-to-osc-mapping-overview) shows an overview of mapping ASAM OpenODD model to ASAM OpenSCENARIO DSL.

The following subsections describe the mapping in more detail.

### 9.5.2.2 Mapping files to files

Each taxonomy file is mapped to an ASAM OpenSCENARIO DSL file with the same name.
Imports references to other files are mapped to equivalent ASAM OpenSCENARIO DSL import statements.

| ASAM OpenODD model | ASAM OpenSCENARIO DSL |
| --- | --- |
| **Mapping ASAM OpenODD model → ASAM OpenSCENARIO DSL** | |
| File  * id: String * imports: File | Becomes a file with name id. Import references become ASAM OpenSCENARIO DSL import statements |
| **Example** | |
| There are two files "example\_taxonomy\_file.openoddmodel" and "other\_taxonomy\_file.openoddmodel", where "example\_taxonomy\_file.openoddmodel" imports "other\_taxonomy\_file.openoddmodel". | These files are mapped to the files  "example\_taxonomy\_file.osc" and "other\_taxonomy\_file.osc" where "example\_taxonomy\_file.osc" has `import "other_taxonomy_file.osc"` as only content. |

### 9.5.2.3 Mapping taxonomies to structs

A file can contain zero or more taxonomies.
Usually it contains one.
Each taxonomy element is mapped to a struct that represents the root of that taxonomy.

| ASAM OpenODD model | ASAM OpenSCENARIO DSL |
| --- | --- |
| **In the context of a previous mapping of:** | |
| File | File |
| **Mapping: ASAM OpenODD model concept becomes ASAM OpenSCENARIO DSL concept:** | |
| A taxonomy contained in a file that has the following attributes:  * id: String | Is mapped to a struct where the name is the id of the taxonomy. |
| **Prerequisites:** | |
| * The id of the taxonomy must be a valid ASAM OpenSCENARIO DSL identifier string. * The length of the id string should be limited for readability of the resulting ASAM OpenSCENARIO DSL code. | |

Code 130. ASAM OpenODD model: Mapping taxonomies to structs (free-form notation)

```
# file example_taxonomy.freeformnotation

taxonomy
    id is "example_taxonomy"
```

Code 131. ASAM OpenSCENARIO DSL: Mapping taxonomies to structs (ASAM OpenSCENARIO DSL notation)

```
# file example_taxonomy.osc

struct example_taxonomy
```

### 9.5.2.4 Mapping containers to structs

Each container in a taxonomy in the ASAM OpenODD model is mapped to a struct in the corresponding ASAM OpenSCENARIO DSL file:

| ASAM OpenODD model | ASAM OpenSCENARIO DSL |
| --- | --- |
| **In the context of a previous mapping of:** | |
| Taxonomy | Struct |
| **Or in the context of a previous mapping of:** | |
| Container | Struct (recursive mapping rule) |
| **Mapping: ASAM OpenODD model concept becomes ASAM OpenSCENARIO DSL concept:** | |
| A container with the following attributes, that is either contained in another container or a direct child of a taxonomy:  * id: String * name: LangString[0..\*] * description: LangString[0..\*] * comment: LangString[0..\*] | Is mapped to a structure, where the name is the name specified for the container in English, with spaces replaced by underscores and uppercase letters replaced by lower case letters. English-language descriptions and comments are translated into comments in the structure definition.  In addition, a field must be added to the structure that corresponds to the parent taxonomy or parent container of the container that represents this parent-child relationship. The name of this field is the same as the name of the assigned container. |
| **Prerequisites:** | |
| * Each container has an English-language name string, which must be a valid ASAM OpenSCENARIO-DSL identifier string or becomes a valid ASAM OpenSCENARIO-DSL identifier string after spaces have been replaced by underscores and uppercase letters have been converted to lowercase letters. * The English taxonomy concept names and taxonomy IDs within a file must be sufficiently different so that their assignment, as described above, does not lead to conflicts of structure names. * The length of the name string should be limited for readability of the resulting ASAM OpenSCENARIO DSL code. | |

Code 132. ASAM OpenODD model: Mapping containers to structs (free-form notation)

```
# file example_taxonomy.freeformnotation

taxonomy
    id is "example_taxonomy"
    roots are
        type Container
            id is "env_conditions"
            name is
                intlCode is "en"
                value is "Environmental Conditions"
            description is
                intlCode is "en"
                value is "env conditions description"
            comment is
                intlCode is "en"
                value is "env conditions comment"
```

Code 133. ASAM OpenSCENARIO DSL: Mapping containers to structs (ASAM OpenSCENARIO DSL notation)

```
# file example_taxonomy.osc

struct example_taxonomy
    environmental_conditions : environmental_conditions

struct environmental_conditions
    # description: env conditions description
    # comment: env conditions comment
```

### 9.5.2.5 Mapping records to structs

Each record is mapped to a struct.

| ASAM OpenODD model | ASAM OpenSCENARIO DSL |
| --- | --- |
| **In the context of a previous mapping of:** | |
| Taxonomy | Struct |
| **Or in the context of a previous mapping of:** | |
| Container | Struct (recursive mapping rule) |
| **Mapping: ASAM OpenODD model concept becomes ASAM OpenSCENARIO DSL concept:** | |
| A record with the following attributes, that is either contained in another container or a direct child of a taxonomy:  * id: String * name: LangString[0..\*] * description: LangString[0..\*] * comment: LangString[0..\*] | Is mapped to a structure, where the name is the name specified for the container in English, with spaces replaced by underscores and uppercase letters replaced by lower case letters. English-language descriptions and comments are translated into comments in the structure definition.  In addition, a field must be added to the structure that corresponds to the parent taxonomy or parent container of the container that represents this parent-child relationship. The name of this field is the same as the name of the assigned container. |
| **Prerequisites:** | |
| * The same prerequisites hold as in [Section 9.5.2.4, “Mapping containers to structs”](#sec-mapping-containers-to-structs). | |

Code 134. ASAM OpenODD model: Mapping records to structs (free-form notation)

```
# file example_taxonomy.freeformnotation

taxonomy
    id is "example_taxonomy"
    roots are
        type Container
            id is "env_conditions"
            name is
                intlCode: "en"
                value is "Environmental Conditions"
            description is
                intlCode is "en"
                value is "Env Conditions description"
            comment is
                intlCode is "en"
                value is "Env Conditions description"
            contains
                type Record
                    id is "weather"
                    name is
                        intlCode is "en"
                        value is "Weather"
                    description is
                        intlCode is "en"
                        value is "Weather description"
                    comment is
                        intlCode is "en"
                        value is "Weather comment"
```

Code 135. ASAM OpenSCENARIO DSL: Mapping records to structs (ASAM OpenSCENARIO DSL notation)

```
# file example_taxonomy.osc

struct example_taxonomy
    environmental_conditions : environmental_conditions

struct environmental_conditions
    # description: env conditions description
    # comment: env conditions comment
    weather : weather

struct weather
    # description: Weather description
    # comment: Weather comment
```

### 9.5.2.6 Mapping categorical types to enum types

| ASAM OpenODD model | ASAM OpenSCENARIO DSL |
| --- | --- |
| **In the context of a previous mapping of:** | |
| Taxonomy | Struct |
| **Or in the context of a previous mapping of:** | |
| Container | Struct (recursive mapping rule) |
| **Mapping: ASAM OpenODD model concept becomes ASAM OpenSCENARIO DSL concept:** | |
| A categorical type with the following attributes, that is either contained in another container or a direct child of a taxonomy:  * id: String * name: LangString[0..\*] * description: LangString[0..\*] * comment: LangString[0..\*] * literals: CategoricalLiteral[0..\*] | Is mapped to an enumeration type, where the name is the English name specified for the categorical type, with spaces replaced by underscores and uppercase letters replaced by lowercase letters. English language descriptions and comments are translated into comments that precede the structure definition.  Each categorical literal is mapped to a literal of the enumeration type definition. The name of the categorical literal is translated into the name of the enumeration literal. |
| **Prerequisites:** | |
| * The same prerequisites for naming hold as in [Section 9.5.2.4, “Mapping containers to structs”](#sec-mapping-containers-to-structs). * Categorical literal strings must be valid OpenSCENARIO DSL identifier strings.   A categorical literal must not have two literals with identical literal strings after replacing capital letters with lowercase letters. | |

Code 136. ASAM OpenODD model: Mapping categorical types to enum types (free-form notation)

```
# file example_taxonomy.freeformnotation

taxonomy
    id is "example_taxonomy"
    roots are
        type Container
            id is "env_conditions"
            name is
                intlCode is "en"
                value is "Environmental Conditions"
            description is
                intlCode is "en"
                value is "Env Conditions description"
            comment is
                intlCode is "en"
                value is "Env Conditions description"
            contains
                type CategoricalType
                    id is "wind_kind"
                    name is
                        intlCode is "en"
                        value is "Wind Kind"
                    description is
                        intlCode is "en"
                        value is "wind kind description"
                    comment is
                        intlCode is "en"
                        value is "wind kind comment"
                    literals are
                        no_wind
                        calm
                        light_air
```

Code 137. ASAM OpenSCENARIO DSL: mapping categorical types to enum types (ASAM OpenSCENARIO DSL notation)

```
# file example_taxonomy.osc

struct example_taxonomy:
    environmental_conditions : environmental_conditions

struct environmental_conditions
    # description: env conditions description
    # comment: env conditions comment

# description: wind kind description
# comment: wind kind comment
enum wind_kind: [
    no_wind,
    calm,
    light_air ]
```

### 9.5.2.7 Mapping categorical literals with range expressions

The ASAM OpenODD model supports adding expressions to categorical literals.
The purpose of this feature is to align the categorical value of an attribute with a numerical value of another attribute.
Example: Having an attribute typed over the `wind_kind` categorical and another attribute of `wind_speed` of `UnitType` `speed`.
Then it is possible to add expressions to each `wind_kind` categorical literal that associates the categorical literal with a range of wind speed.

Such a mapping is not directly supported by ASAM OpenSCENARIO DSL, but such expressions can be mapped to `keep` constraints that enforce consistency among attributes.
See the code examples below.

Code 138. ASAM OpenODD model: Example of categorical range expressions (free-form notation)

```
# file example_taxonomy.freeformnotation

example_taxonomy
    weather is                                                          # record
        wind_speed is float representing velocity                       # attribute primitive type
        wind_kind is                                                    # attribute categorical
            no_wind when   wind_speed is less than or equal to 0 m/s    # categorical literal upper bound expression
            calm when      wind_speed in [0   .. 0.2] m/s               # categorical literal with range expression
            light_air when wind_speed in [0.2 .. 1.5] m/s               # categorical literal with range expression
            ...
        ...
```

Code 139. ASAM OpenSCENARIO DSL: mapping categorical range expressions to consistency constraints in ASAM OpenSCENARIO DSL (ASAM OpenSCENARIO DSL notation)

```
# file example_taxonomy.osc

...

struct weather:
    wind_kind : wind_kind
    wind_speed : speed
    keep (wind_kind == no_wind => wind_speed == 0.0 mps)
    keep (wind_kind == calm => wind_speed < 0.2 mps)
    keep (wind_kind == light_air =>
            wind_speed >= 0.2 mps and wind_speed < 1.5 mps)
    ...

enum wind_kind: [
    no_wind,
    calm,
    light_air, ... ]
...
```

### 9.5.2.8 Mapping attributes to fields

Each attribute of a data record is assigned to a field with a type that corresponds to the type of the attribute:

| ASAM OpenODD model | ASAM OpenSCENARIO DSL |
| --- | --- |
| **In the context of a previous mapping of:** | |
| Record | Struct |
| **Mapping: ASAM OpenODD model concept becomes ASAM OpenSCENARIO DSL concept:** | |
| An attribute with the following attributes:  * id: String * type: Type | Is mapped to a field in the context structure, whereby the name is the ID specified for the attribute and uppercase letters are replaced by lower case letters.  The type of the attribute is mapped to the field type as follows:  * If the attribute is typed over a primitive type without an attached unit type, the field is typed over the corresponding primitive type.   Only Boolean, int, float, and string are supported by the mapping. * If the attribute is typed over a categorical type, the field is typed over the corresponding enumeration type. * If the attribute is typed over a primitive type with a unit type, the field is typed over the corresponding unit type according to the ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)], see also [Section 6.2.7.1, "Unit specification"](../06_model_concept/06_02_openodd_taxonomy.html#sec-unit-specification). |
| **Prerequisites:** | |
| * The ID specified for the attribute, in which uppercase letters are replaced by lower case letters, must be a valid ASAM OpenSCENARIO DSL identifier. * Only unit types are used that are listed in the ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)]. * Only Primitive types named boolean, int, float, and string can be mapped. | |

Code 140. ASAM OpenODD model: Mapping attributes to fields (free-form notation)

```
# file example_taxonomy.freeformnotation

taxonomy
    id is "example_taxonomy"
    roots are
        type is PrimitiveType
            id is "bool"
            name is
                intlCode is "en"
                value is "boolean"
        type is PrimitiveType
            id is "float_wind_speed"
            name is
                intlCode is "en"
                value is "float"
        unitType is
            id is "speed"
        type is Container
            id is "env_conditions"
            name is
                intlCode is "en"
                value is "Environmental Conditions"
            contains
                type CategoricalType
                    id is "wind_kind"
                    name is
                        intlCode is "en"
                        value is "Wind Kind"
                    literals are
                        no_wind
                        calm
                        light_air
        type is Record
            id is "weather"
            name is
                intlCode is "en"
                value is "Weather"
            attributes are
                id is "wind_kind"
                    type is wind_kind
                id is "wind_speed"
                    type is float_wind_speed
                id is "is_gusty"
                    type is boolean
```

Code 141. ASAM OpenSCENARIO DSL: Mapping attributes to fields (ASAM OpenSCENARIO DSL notation)

```
# file example_taxonomy.osc

struct example_taxonomy:
    environmental_conditions : environmental_conditions

type speed is SI(m: 1, s: -1)

struct environmental_conditions:
    weather : weather

enum wind_kind: [
    no_wind,
    calm,
    light_air ]

struct weather:
    wind_kind : wind_kind
    wind_speed : speed
    is_gusty : bool
```

## 9.5.3 COD/OD mapping

See following how CODs or ODs in the ASAM OpenODD model can be mapped to an ASAM OpenSCENARIO DSL representation.

A COD or OD in the ASAM OpenODD model is represented by an instance of the `COD_OD` class which can be associated with a `TemporalExtent` and `SpatialExtent`, that is, information of when and where a COD was recorded.
Additionally, a `COD_OD` instance has a list of `TaxonomyConceptValues` instances, which in ASAM OpenSCENARIO DSL map types in the domain concepts definition model (taxonomy) to concrete values.
The values are primitive-, categorical-, or record-values, depending on the type of the referenced taxonomy type.
A record value is a hierarchical structure that again maps record attribute to values.

The mapping from a ASAM OpenODD model COD or OD structure to OpenSCENARIO DSL consists in mapping of

1. `TaxonomyConceptValues` instances (type-to-values mappings)
2. Record values (attribute-to-values mappings)

Both map to `keep`-statements that specify the values for the ASAM OpenSCENARIO DSL struct attributes that correspond to the ASAM OpenODD model class `Type` or ASAM OpenODD model class `Record` attributes.
Moreover, the classes `TemporalExtent` and `SpatialExtent` are mapped to keep statements that assign values to the attributes of the `date_time` and `geo_location_3D` structs.

The following example illustrates the mapping.

[Table 146](#tab-codtablejsonrecord_row1) shows a COD in a tabular format, which is based on the taxonomy in [Code 142](#code-example-core-model-cod-complex-structure).
(The examples are taken from [Section 6.3.4.1, "TaxonomyConceptValues specification"](../06_model_concept/06_03_openodd_od.html#sec-concept-cod_od-TaxonomyConceptValues-specification)).

Table 146. Example COD table with JSON **Record**


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAINFALL\_RATE; mm/h | RAINFALL\_TYPE; categorical\_literal | INTERSECTION; record |
| --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01 08:12:53.784" | "48.0232 11.7153" | 6.214 | convective | {"features": {"refuge\_island\_count": 2, "number\_of\_ways": 4, "is\_signalized": True}, "type": "X\_junction"} |

Code 142. Example ASAM OpenODD model taxonomy with complex structure (free-form notation)

```
TAXONOMY specification is as follows
    weather is                                                  # record
        rainfall_rate is float representing velocity             # attribute
        rainfall_intensity is                                   # categorical attribute
            dynamic                                             # categorical literal
            convective                                          # categorical literal
            orographic                                          # categorical literal
    intersection_features is                                    # record
        refuge_island_count is an integer representing count    # numeric attribute
        number_of_ways is an integer representing count         # numeric attribute
        is_signalized is a boolean                              # boolean attribute
   intersection is                                              # record
        features is an intersection_features type               # attribute
        type is                                                 # categorical attribute
            T_junction                                          # categorical literal
            Y_junction                                          # categorical literal
            X_junction                                          # categorical literal
```

The taxonomy can be mapped to the following ASAM OpenSCENARIO DSL representation (by applying the mapping rules as described in [Section 9.5.2, “Taxonomy mapping”](#sec-dsl-taxonomy-mapping)).

Code 143. ASAM OpenSCENARIO DSL: domain concepts definition model (taxonomy) corresponding to the taxonomy in [Code 142](#code-example-core-model-cod-complex-structure) (ASAM OpenSCENARIO DSL notation)

```
# file example-taxonomy.osc

struct example_taxonomy:
    environmental_conditions : environmental_conditions
    scenery : scenery


type speed is SI(m: 1, s: -1)


struct environmental_conditions:
    weather : weather


struct weather:
    rainfall_rate : speed
    rainfall_type : rainfall_type


enum rainfall_type : [dynamic, convective, orographic]


struct scenery:
    intersection : intersection


struct intersection:
    intersection_type : intersection_type
    intersection_features: intersection_features


struct intersection_features:
    refuge_island_count : int
    number_of_ways : int
    is_signalized : int


enum intersection_type: [
    no_intersection,
    T_junction,
    X_junction,
    Y_junction
    ]
```

[Code 144](#code-example-OSC-DSL-COD-intersection-weather) shows the ASAM OpenSCENARIO DSL representation of the COD in [Table 146](#tab-codtablejsonrecord_row1):

1. The `TemporalExtent` and `SpatialExtent` are mapped to keep constraints that specify values for the `date_time` and `geo_location_3D` structs.
2. The attribute values of the `weather` record are mapped to `keep`-statements of the weather-struct
3. The attribute values of the `intersection` and `intersection_features` records are mapped to `keep`-statements of the corresponding structs.

Code 144. ASAM OpenSCENARIO DSL: COD corresponding to the COD in [Table 146](#tab-codtablejsonrecord_row1) (ASAM OpenSCENARIO DSL notation)

```
# file example-COD.osc
import "example-taxonomy.osc"


# A COD may need to define additional units if they are not already defined in domain concepts model (taxonomy)
unit mmph of speed is SI(m: 1, s: -1, factor: 0.000277778)
unit s of time is SI(s: 1)  # Seconds
unit ms of time is SI(s: 1, factor: 0.001)  # Milliseconds
unit min of time is SI(s: 1, factor: 60)  # Minutes
unit h of time is SI(s: 1, factor: 3600)  # Hours
unit deg of angle is SI (rad: 1, factor: 0.01745329251) # pi/180


# temporal extent "2024-06-01 08:12:53.784"
extend date_time:
    keep (year == 2024)
    keep (month == 6)
    keep (day == 1)
    keep (hour == 8 h)
    keep (minute == 12 min)
    keep (second == 53 s)
    keep (millisecond == 784 ms)


# Spatial extent "48.0232 11.7153"
extend geo_location_3D:
    keep (latitude = 48.0232 deg)
    keep (longitude = 11.7153 deg)
    # keep (altitude = ??) -- no altitude given


# RAINFALL_RATE;mm/hr: 6.214
# RAINFALL_TYPE: convective
extend weather:
    keep(rainfall_rate == 6.214 mmph)
    keep(rainfall_type == convective)


# "type": "X_junction"
extend intersection:
    keep(intersection_type == X_junction)


# "features": {"refuge_island_count": 2, "number_of_ways": 4, "is_signalized": True}
extend intersection_features:
    keep(refuge_island_count == 2)
    keep(number_of_ways == 4)
    keep(is_signalized == True)
```

## 9.5.4 ODD module mapping

### 9.5.4.1 Overview

In the ASAM OpenODD model, a module is a reusable building block for defining and structuring an ODD or TOD.
A module is a combination of conditions and evaluates to a Boolean outcome (see ASAM OpenODD model classes `Module` and `Condition`).
A module may be referenced by other modules, thus allowing for a hierarchical definition of an ODD or TOD.

This mapping is based on the assumption, that the source ASAM OpenODD model instance is in a file that defines a taxonomy (or imports a taxonomy) as well as a list of modules, where one of the `Module` instances has the field `is_root` set to `true` (see [Section 6.4.4, "Module details"](../06_model_concept/06_04_openodd_modules.html#sec-concept-modules-module-details)).
That means it is the root (or main) `Module` instance from which to infer and map the full ODD specification.
This `Module` can reference other `Module` instances and `Label` instances in that file or imported files.
This main `Module` instance is then mapped in ASAM OpenSCENARIO DSL to a `keep` statement, or set of `keep` statements, located in the structure corresponding to the taxonomy element, see [Section 9.5.2.3, “Mapping taxonomies to structs”](#sec-mapping-taxonomies-to-structs).
Other inferred modules are mapped as keep statements to the relevant taxonomy concepts structs.

[Section 9.5.4.2, “Module structure”](#sec-module-structure) revisits the fundamental components of a module, [Section 9.5.4.3, “Mapping module sections”](#sec-mapping-module-sections) proceeds to present an algorithm for mapping modules in ASAM OpenODD to ASAM OpenSCENARIO DSL.
For each module structure, the focus is on its mapping to a Boolean expression.
The notation \(\mathcal{M}\)(<Module-Component>) is used to denote the Boolean expression mapping of a module component in ASAM OpenSCENARIO DSL.

### 9.5.4.2 Module structure

Each `Module` instance has a unique identifier `id`.
It may also contain additional information such as a `name`, `title`, `description`, and a `comment`.
A `Module` instance can declare a collection of `Label` instances as well as `Tag` instances, and is composed of at most two `Section` instances: one `INCLUDE` `Section` and one `EXCLUDE` `Section`.

### 9.5.4.3 Mapping module sections

A module section can be either an `INCLUDE` or an `EXCLUDE` section, each of which can be further refined into an `AND` constraint or an `OR` constraint.
A module \(M\) that has one of these sections is mapped to an ASAM OpenSCENARIO DSL expression \(\mathcal{M}\)(\(M\)) as follows:

* `INCLUDE_AND`: This constraint type represents the Boolean *conjunction* of a collection of unordered Boolean constraints  
  \(C\_1\), \(C\_2\), …​, \(C\_n\), that is, \(C\_1 \wedge C\_2 \wedge …​ \wedge C\_n\).  
  If module \(M\) consists of an `INCLUDE_AND`(\(C\_1\), \(C\_2\), …​, \(C\_n\)), then the following mapping rule applies:  
  \(\mathcal{M}\)(\(M\)) = \(\mathcal{M}\)(\(C\_1\)) `AND` \(\mathcal{M}\)(\(C\_2\)) `AND` …​ \(\mathcal{M}\)(\(C\_n\))
* `INCLUDE_OR`: This constraint type represents the Boolean *disjunction* of a collection of unordered Boolean constraints  
  \(C\_1\), \(C\_2\), …​, \(C\_n\), that is, \(C\_1 \vee C\_2 \vee …​ \vee C\_n\).  
  If module \(M\) consists of an `INCLUDE_OR`(\(C\_1\), \(C\_2\), …​, \(C\_n\)), then the following mapping rule applies:  
  \(\mathcal{M}\)(\(M\)) = \(\mathcal{M}\)(\(C\_1\)) `OR` \(\mathcal{M}\)(\(C\_2\)) `OR` …​ \(\mathcal{M}\)(\(C\_n\))
* `EXCLUDE_AND`: This constraint type represents the negation of the Boolean conjunction of a collection of unordered Boolean constraints  
  \(C\_1\), \(C\_2\), …​, \(C\_n\), that is, \(\neg (C\_1 \wedge C\_2 \wedge …​ \wedge C\_n) \equiv (\neg C\_1 \vee \neg C\_2 \vee …​ \vee \neg C\_n)\).  
  If module \(M\) consists of an `EXCLUDE_AND`(\(C\_1\), \(C\_2\), …​, \(C\_n\)), then the following mapping rule applies:  
  \(\mathcal{M}\)(\(M\)) = `NOT(` \(\mathcal{M}\)(\(C\_1\)) `AND` \(\mathcal{M}\)(\(C\_2\)) `AND` …​ \(\mathcal{M}\)(\(C\_n\)) `)`
* `EXCLUDE_OR`: This constraint type represents the negation of the Boolean disjunction of a collection of unordered Boolean constraints  
  \(C\_1\), \(C\_2\), …​, \(C\_n\), that is, \(\neg (C\_1 \vee C\_2 \vee …​ \vee C\_n) \equiv (\neg C\_1 \wedge \neg C\_2 \wedge …​ \wedge \neg C\_n)\).  
  If module \(M\) consists of an `EXCLUDE_OR`(\(C\_1\), \(C\_2\), …​, \(C\_n\)), then the following mapping rule applies:  
  \(\mathcal{M}\)(\(M\)) = `NOT(` \(\mathcal{M}\)(\(C\_1\)) `OR` \(\mathcal{M}\)(\(C\_2\)) `OR` …​ \(\mathcal{M}\)(\(C\_n\)) `)`

In these descriptions, a constraint \(C\_i\), where \(i\) is the index of the constraint, is an expression over module identifiers, label identifiers, or a constraint over taxonomy attribute, and evaluates to a Boolean value.
Moreover, \(\mathcal{M}\)(\(C\_i\)) is the mapping of expression \(C\_i\) to an ASAM OpenSCENARIO DSL expression.

A module may have two sections.
The mapped sections are logically combined using an `and` operator.
These mappings are demonstrated in the examples below.

Consider [Code 145](#code-repeat-from-dm-example-module1-include-and) which has a single `INCLUDE_AND` section.

Code 145. Example `INCLUDE_AND` (free-form notation)

```
example_module_1 is
    INCLUDE_AND when
        wind_speed is less than 40 km/h
        rainfall_rate is less than 20 mm/h
```

[Code 145](#code-repeat-from-dm-example-module1-include-and) translates to the following expression in OpenSCENARIO DSL:

Code 146. Example `INCLUDE_AND` (ASAM OpenSCENARIO DSL notation)

```
# MODULE_NAME: example_module_1
wind_speed < 40 kmph and rainfall_rate < 20 mmph
```

The mapping example [Code 146](#code-oscdsl-example-module1-include-and) above also shows that the module name is mapped to a code comment in the ASAM OpenSCENARIO DSL code.
Module names, titles, descriptions, and comments as well as labels can be mapped to such code comments.
However, this is optional and only treated informally in the following code examples.

Consider [Code 147](#code-repeat-from-dm-example-module2-include-or) which has a single `INCLUDE_OR` section.

Code 147. Example `INCLUDE_OR` (free-form notation)

```
example_module_2 is
    INCLUDE_OR when
        wind_speed is greater than or equal to 40 km/h
        rainfall_rate is greater than or equal to 20 mm/h
```

[Code 147](#code-repeat-from-dm-example-module2-include-or) translates to the following expression in OpenSCENARIO DSL:

Code 148. Example `INCLUDE_AND` (ASAM OpenSCENARIO DSL notation)

```
# MODULE_NAME: example_module_2
wind_speed >= 40 kmph or rainfall_rate >= 20 mmph
```

Consider [Code 149](#code-repeat-from-dm-example-module3-exclude-and) which has a single `EXCLUDE_AND` section.

Code 149. Example `EXCLUDE_AND` (free-form notation)

```
example_module_3 is
    EXCLUDE_AND when
        wind_speed is greater than 40 km/h
        rainfall_rate is greater than 20 mm/h
```

[Code 149](#code-repeat-from-dm-example-module3-exclude-and) translates to the following expression in OpenSCENARIO DSL:

Code 150. Example EXCLUDE\_AND (ASAM OpenSCENARIO DSL notation)

```
# MODULE_NAME: example_module_3
not ( wind_speed < 40 kmph and  rainfall_rate < 20 mmph )
```

Consider [Code 151](#code-repeat-from-dm-example-module4-exclude-or) which has a single `EXCLUDE_OR` section.

Code 151. Example `EXCLUDE_OR` (free-form notation)

```
example_module_4 is
    EXCLUDE_OR when
        wind_speed is greater than 40 km/h
        rainfall_rate is greater than 20 mm/h
```

[Code 151](#code-repeat-from-dm-example-module4-exclude-or) translates to the following expression in ASAM OpenSCENARIO DSL:

Code 152. Example `EXCLUDE_OR` (ASAM OpenSCENARIO DSL notation)

```
# MODULE_NAME: example_module_4
not ( wind_speed >= 40 kmph or rainfall_rate >= 20 mmph )
```

Consider [Code 153](#code-repeat-from-dm-example-include-and-exclude-or) which has a single `INCLUDE_AND` and a single `EXCLUDE_OR` section.

Code 153. Example `INCLUDE_AND` and `EXCLUDE_OR` (free-form notation)

```
example_module_5 is
    INCLUDE_AND when
        wind_speed is less than 40 km/h
        rainfall_rate is less than 20 mm/h
    EXCLUDE_OR when
        fog_visibility is less than 50 m
        connectivity_bandwidth is less than 1 Mbps
```

[Code 153](#code-repeat-from-dm-example-include-and-exclude-or) translates to the following expression in ASAM OpenSCENARIO DSL:

Code 154. Example `INCLUDE_AND` and `EXCLUDE_OR` (ASAM OpenSCENARIO DSL notation)

```
# MODULE_NAME: example_module_5
( wind_speed < 40 kmph and  rainfall_rate < 20 mmph ) and
not ( fog_visibility < 50 m or connectivity_bandwidth < 1 Mbps)
```

Consider [Code 155](#code-repeat-from-dm-example-include-or-exclude-and) which has a single `INCLUDE_OR` and a single `EXCLUDE_AND` section.

Code 155. Example `INCLUDE_OR` and `EXCLUDE_AND` (free-form notation)

```
example_module_6 is
    INCLUDE_OR when
        wind_speed is less than 40 km/h
        rainfall_rate is less than 20 mm/h
    EXCLUDE_AND when
        fog_visibility is less than 50 m
        connectivity_bandwidth is less than 1 Mbps
```

[Code 155](#code-repeat-from-dm-example-include-or-exclude-and) translates to the following expression in ASAM OpenSCENARIO DSL:

Code 156. Example `INCLUDE_OR` and `EXCLUDE_AND` (ASAM OpenSCENARIO DSL notation)

```
# MODULE_NAME: example_module_6
( wind_speed < 40 kmph or  rainfall_rate < 20 mmph ) and
not ( fog_visibility < 50 m and connectivity_bandwidth < 1 Mbps)
```

Consider [Code 157](#code-repeat-from-dm-example-complex-module) which has an `INCLUDE_AND` with an `OR` and an `EXCLUDE_OR` with an `AND` section.

Code 157. Example complex module (free-form notation)

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

[Code 157](#code-repeat-from-dm-example-complex-module) translates to the following expression in ASAM OpenSCENARIO DSL:

Code 158. Example complex module (ASAM OpenSCENARIO DSL notation)

```
# MODULE_NAME: example_module_7
(
  ( downlink_latency < 10 msec and downlink_throughput > 1 Mbps )
  and (
    global_positioning == GPS or local_positioning == beacon_positioning
  )
)
and not (
  is_sign_visible == false
  or (
    temporary_road_structures == construction_site_detours and
    road_type == expressway
  )
)
```

A module may also reference other modules within `INCLUDE` and `EXCLUDE` sections.
In such cases, the mapping rule is recursively applied to the module identifier in place.
This leads to the referenced module identifier being expanded into a Boolean expression (as shown in [Code 158](#code-oscdsl-example-complex-module)), inline within the mapped `INCLUDE` or `EXCLUDE` statement it is part of.

Code 159. Example inclusion and exclusion conditions (free-form notation)

```
pickup_locations_group1 is
    LABEL is supported_pickup_locations
    INCLUDE_AND when
        street_section in
            main_st_sec1
            main_st_sec2
    ...

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
        rain_rate equaks heavy_rain
    ...

icy_road_conditions is
    LABEL is hazardous_conditions
    INCLUDE_AND when
        road_surface_condition equals black_ice
    ...
```

Now consider the module `passenger_pickup` defined in [Code 160](#code-example-module-reference-include-or-exclude-or).
The module makes reference to module identifiers `pickup_locations_group1` and `pickup_locations_group2` within the `INCLUDE_OR` section (potentially, along with other expressions), and makes reference to `too_much_rain` and `icy_road_conditions` within its `EXCLUDE_OR` section (potentially, along with other expressions), within [Code 159](#code-example-modules-labels-inclusion-exclusion-conditions).

Code 160. Example `INCLUDE_OR` and `EXCLUDE_OR` containing Modules (free-form notation)

```
passenger_pickup is
    INCLUDE_OR when
        pickup_locations_group1 is true
        pickup_locations_group2 is true
    ...
    EXCLUDE_OR when
        too_much_rain is true
        icy_road_conditions is true
    ...
```

[Code 160](#code-example-module-reference-include-or-exclude-or), taken together with [Code 159](#code-example-modules-labels-inclusion-exclusion-conditions), translates to the expression [Code 161](#code-oscdsl-example-module-reference-include-or-exclude-or) in ASAM OpenSCENARIO DSL:

Code 161. Example `INCLUDE_OR` and `EXCLUDE_OR` containing Modules (ASAM OpenSCENARIO DSL notation)

```
# MODULE_NAME: passenger_pickup
(
  # MODULE_NAME: passenger_pickup -> pickup_locations_group1
  # MODULE_LABEL: pickup_locations_group1: supported_pickup_locations
  ( street_section in [main_st_sec1, main_st_sec2] ... )
  or
  # MODULE_NAME: passenger_pickup -> pickup_locations_group2
  # MODULE_LABEL: pickup_locations_group2: supported_pickup_locations
  ( train_station in [pole5, pole11] ... )
  ...
)
and not (
  # MODULE_NAME: passenger_pickup -> too_much_rain
  # MODULE_LABEL: too_much_rain: hazardous_conditions
  ( rain_rate == heavy_rain ...)
  or
  # MODULE_NAME: passenger_pickup -> icy_road_conditions
  # MODULE_LABEL: icy_road_conditions: hazardous_conditions
  ( road_surface_condition == black_ice ...)
  ...
)
```

The ellipses in [Code 160](#code-example-module-reference-include-or-exclude-or) refer to mappings of respective ellipses within [Code 73](../06_model_concept/06_04_openodd_modules.html#code-example-inclusion-exclusion-conditions) and [Code 160](#code-example-module-reference-include-or-exclude-or).

### 9.5.4.4 Mapping label constraints

A `Module` can declare its affiliation to zero or more `Label` instances.
Each `Label` instance has a unique identifier, which is unique amongst all `Module` instances' identifiers and taxonomy attribute identifiers.
A `Label` instance is used to reference the truth of one or more modules.
The truth of a `Label` instance is the disjunction of the truths of the `Module` instance in which the `Label` instance is declared.

For example, consider modules \(M\_1\), \(M\_2\), …​, \(M\_k\) which all reference the label identifier \(L\).
The truth of \(L\) is defined as \(L \equiv M\_1 \vee M\_2 \vee …​ \vee M\_k\).

A `Module` instance may declare multiple `Label` instances.
For instance consider the following examples:

* Module \(M\_1\) declares labels \(L\_1\), \(L\_2\), \(L\_3\)
* Module \(M\_2\) declares label \(L\_1\)
* Module \(M\_3\) declares label \(L\_2\)
* Module \(M\_4\) declares label \(L\_3\)
* Module \(M\_5\) declares label \(L\_3\), \(L\_4\)

The truths of the `Label` instances are as follows: \(L\_1 \equiv (M\_1 \vee M\_2)\), \(L\_2 \equiv (M\_1 \vee M\_3)\), \(L\_3 \equiv (M\_1 \vee M\_4 \vee M\_5)\), and \(L\_4 \equiv M\_5\).

`Label` instances can be in include and exclude sections of `Module` instances in expressions "\(L\) : true" or "\(L\) : false".
"\(L\) : true" means that the condition represented by \(L\) holds.
"\(L\) : false" means that the condition represented by \(L\) does not hold.

Therefore, the following assignment rules apply to a label \(L \equiv (M\_1 \vee M\_2 …​ \vee M\_n)\):

* If \(C\) is a constraint "\(L\) : true", then \(\mathcal{M}\)(\(C\)) = `(` \(\mathcal{M}\)(\(M\_1\)) `OR` \(\mathcal{M}\)(\(M\_2\)) `OR` …​ \(\mathcal{M}\)(\(M\_n\)) `)`
* If \(C\) is a constraint "\(L\) : false", then \(\mathcal{M}\)(\(C\)) = `(NOT(` \(\mathcal{M}\)(\(M\_1\)) `OR` \(\mathcal{M}\)(\(M\_2\)) `OR` …​ \(\mathcal{M}\)(\(M\_n\)) `))`

Consider the `Module` instance `passenger_pickup` defined in [Code 162](#code-example-labels-reference-include-or-exclude-or).

Code 162. Example `INCLUDE_OR` and `EXCLUDE_OR` containing modules (free-form notation)

```
passenger_pickup is
    INCLUDE_OR when
        supported_pickup_locations is true
    ...
    EXCLUDE_OR when
        hazardous_conditions is true
    ...
```

[Code 162](#code-example-labels-reference-include-or-exclude-or) has an equivalent semantic as [Code 160](#code-example-module-reference-include-or-exclude-or), and also translates to the expression shown in [Code 161](#code-oscdsl-example-module-reference-include-or-exclude-or) in OpenSCENARIO DSL.

### 9.5.4.5 Mapping constraints over taxonomy attributes

The ASAM OpenODD model defines different kinds of expressions that refer to taxonomy attributes.

*Lower- and upper-bound expressions* compare a numerical or unit-typed attribute to a numerical or unit value.
Comparing values of categorical types via lower- and upper-bound expressions is also possible according to the ASAM OpenODD model.
However, ASAM OpenSCENARIO DSL does not assume any order among the literals of enumeration types. Hence, the mapping **does not support lower- and upper-bound expressions relating to categorical type attributes.**
(The ASAM OpenODD model supports extending categorical literals with expressions that can map each literal to a range of values or some numerical attribute.
In ASAM OpenSCENARIO DSL, this is possible via constraints, compare [Section 9.5.2.7, “Mapping categorical literals with range expressions”](#sec-dsl-mapping-categorical-literals-with-range-expressions), but this still does not enable relation operators to be used with enum values.)

*Equal expression* forces an attribute value to be equal to a given value of primitive or categorical type.

*Range expression* forces that the value of a numerical or unit-typed attribute is between two given numerical or unit values.
The restriction of values of categorical types via range expressions is also possible, depending on the ASAM OpenODD model.
However, for the reasons given above, the mapping **does not support range expressions relating to categorical type attributes.**

* Assuming that a constraint \(C\) is a *lower-bound expression* \(C\) = \(<attribute>\) > \(<value>\) \(<unit>\) (unit is optional), \(C\) is mapped to an ASAM OpenSCENARIO DSL expression as follows:
  \(\mathcal{M}\)(\(C\)) = `( <attribute> > <value> <unit>)`.
  (unit is optional)
* Assuming that a constraint \(C\) is an *upper-bound expression* \(C\) = \(<attribute>\) < \(<value>\) \(<unit>\), \(C\) is mapped to an ASAM OpenSCENARIO DSL expression as follows:
  \(\mathcal{M}\)(\(C\)) = `( <attribute> < <value> <unit>)`. (unit is optional)
* Assuming that a constraint \(C\) is an *equals expression* \(C\) = \(<attribute>\) = \(<value>\) \(<unit>\) (unit is optional), \(C\) is mapped to an ASAM OpenSCENARIO DSL expression as follows:
  \(\mathcal{M}\)(\(C\)) = `( <attribute> = <value> <unit>)`.
  (unit is optional)
* Assuming that a constraint \(C\) is a *range expression* \(C\) = \(<attribute>\) [\(<lower-value>\) .. \(<upper-value>\)] \(<unit>\) (unit is optional), \(C\) is mapped to an ASAM OpenSCENARIO DSL expression as follows:
  \(\mathcal{M}\)(\(C\)) = `( <attribute> in [<lower-value> .. <upper-value>] <unit>)`.
  (unit is optional)

In these mapping rules:

* `<attribute>` refers to an attribute expression that references the mapped taxonomy attribute.
  In ASAM OpenSCENARIO DSL, this expression is an expression that navigates through the hierarchy of structs that represent the nested taxonomy structure via dot-expressions (like `environmental_conditions.weather.wind_speed`).
* `<value>` is a one-to-one mapping of the given value
* `<unit>` is a mapping to the unit.
  Here, without specifying the details, the mapping implies that units corresponding to ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)] are defined in the ASAM OpenSCENARIO DSL file or an imported file, so that all units supported by the ASAM OpenODD model can be mapped.

Examples of mapping expressions are provided in the running examples in earlier sections.