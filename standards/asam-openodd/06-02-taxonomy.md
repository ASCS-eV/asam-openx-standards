# ASAM OpenODD® v1.0.0 — §6.2 Taxonomy

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/06_model_concept/06_02_openodd_taxonomy.html
> **Standard**: ASAM OpenODD® Base Standard 1.0.0 Specification, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2025-05-19

---

## 6.2.4.1 Overview

The type-related classes of the ASAM OpenODD® model define how taxonomy concepts are structured.

A `TaxonomyConcept` is either one of two specializations:

- **Container**: an aggregation of arbitrary instances of `TaxonomyConcept`
- **Type**: a certain type of `TaxonomyConcept` which can be one of the following:
  - **Categorical**: is similar to "enumerated variables" and are associated with a list of instances of `CategoricalLiteral`. It is further possible to associate those `CategoricalLiteral` instances with ranges.
  - **PrimitiveType**: an elementary type like a number, boolean, date, or aggregation (min/max/average/percentile).
  - **Record**: a structured type consisting of one or more typed instances of class `Attribute`. Each attribute is associated with an instance of class `Type`, which means that an attribute can represent either a `PrimitiveType` or `Categorical` value or an instantiation of a `Record`, a nested record.

## 6.2.4.2 Class Type

A typed `TaxonomyConcept`, which can either be a `Record` (that is a structured `Type` with `Attribute` instances), a `Categorical`, or a `PrimitiveType`.

| Property | Value |
|----------|-------|
| Instantiable | yes |
| Parents | `TaxonomyConcept` |

## 6.2.4.3 PrimitiveType specification

Numeric `TaxonomyConcept` instances are taxonomy attributes specified by a primitive type followed by the unit type. For example, it is possible to specify a simple concept element type such as `rain_rate` which is a floating-point value having a unit-type of `precipitation_rate`.

Boolean `TaxonomyConcept` instances are specified by the keyword `boolean` but without a unit type. For example, `is_road_closed` Boolean without specifying the corresponding unit type because Booleans are not associated with units.

Date `TaxonomyConcept` instances are specified by an ISO 8601 formatted string compliant with the Date specification.

Time `TaxonomyConcept` instances are specified by an ISO 8601 formatted string compliant with the Time specification.

DateTime `TaxonomyConcept` instances are specified by an ISO 8601 formatted string compliant with the DateTime specification.

## 6.2.4.4 Class PrimitiveType

A `PrimitiveType` is one of `boolean`, `integer`, `long`, `float`, `double`.

| Property | Value |
|----------|-------|
| Instantiable | yes |
| Parents | `Type` |

## 6.2.4.5 Categorical specification

`Categorical` `TaxonomyConcept` instances are specified by providing a list of instances of `CategoricalLiteral`. For example, the taxonomy may provide a list of `road_type` values such as `highway`, `town_local`, and so forth.

## 6.2.4.6 Class Categorical

A concept which accepts a predefined list of `CategoricalLiteral`. This is equivalent to an enumerated type.

| Property | Value |
|----------|-------|
| Instantiable | yes |
| Parents | `Type` |

## 6.2.4.7 CategoricalLiteral specification

`CategoricalLiteral` `Value` instances may specify instances of `Range`, according to range constraints.

### Example: Rainfall rate classification

```
not_detectable when rainfall_rate is less than 0.1 mm/h
light_rain when     rainfall_rate in [0.1 .. 2.5] mm/h
moderate_rain when  rainfall_rate in [2.5 .. 7.6] mm/h
heavy_rain when     rainfall_rate in [7.6 .. 50] mm/h
violent_rain when   rainfall_rate in [50 .. 100] mm/h
cloud_burst when    rainfall_rate is greater than 100 mm/h
```

When ranges are specified, these ranges induce an order among the `CategoricalLiteral` instances.

### Example: Categorical instances with thresholds

```
is_dangerous_wind is                                   # categorical instance
    true when                                          # categorical literal instance
        wind_speed is greater than 50 km/h             # upper bound expression
    false when                                         # categorical literal instance
        wind_speed is less than or equal to 50 km/h    # lower bound expression
```

Requirements for categorical instances with range expressions:
- There is a single upper bound expression and a single lower bound expression
- A single common numeric `Attribute` is used in both upper and lower bound expressions
- The threshold used by the conditions shall be identical
- Boolean types are not appropriate because they would not allow specifying range thresholds

### Example: Fog levels with visibility ranges

```
fog_level is                                                     # categorical attribute
    fog_not_detectable when                                      # categorical literal
        fog_visibility_range is greater than 1609 m              # lower bound expression
    fog_mist when                                                # categorical literal
        fog_visibility_range in [805 .. 1609] m                  # range expression
    fog_medium when                                              # categorical literal
        fog_visibility_range in [450 .. 805] m                   # range expression
    fog_heavy when                                               # categorical literal
        fog_visibility_range in [50 .. 450] m                    # range expression
    fog_thick when                                               # categorical literal
        fog_visibility_range is less than 50 m                   # upper bound expression
```

Requirements for CategoricalLiteral with Range expressions:
- A single `UpperBound` expression
- A single `LowerBound` expression
- All others shall be `Range` expressions
- The ranges shall cover the entire range of possible values for the numeric type

### Example: Categorical concepts (road types)

```
paved_road is
    RQ28
    RQ31
    RQ36
    RQ43-5
road_type is                        # categorical type instance
    motorway when
        paved_road in RQ31, RQ36    # categorical list expression
    local_road when
        paved_road in RQ28          # categorical list expression
    bundesautobahn when
        paved_road in RQ43-5        # categorical list expression
```

## 6.2.4.8 Class CategoricalLiteral

Specifies a possible value of a `Categorical` attribute, for example `road_type` is `expressway`. It can be associated with:
- A range of values (using a `Range` expression, e.g., `rain_level` is [medium .. high])
- A `PrimitiveType` concept (having upper/lower bounds, e.g., `rain_level` less than `high`)
- An enumerated list of `CategoricalLiteral` instances (using `CategoricalList` expression)

| Property | Value |
|----------|-------|
| Instantiable | yes |

### Parameters

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| name | LangString | yes | An array of multi-language translation of the literal (at least English must be provided). The name must be unique within an ASAM OpenODD® file transmission. |
