# ASAM OpenODD® v1.0.0 — Annex F: (informative) Parameters

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_g_parameterization.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex F: (informative) Parameters

## F.1 Overview

In the following parameterized expressions are presented.
In future versions of ASAM OpenODD® parameterized expressions can be developed further and be declared as normative.

## F.2 Parameterized expressions

The ASAM OpenODD® model supports the parameterization of expressions that allow defining parameters for later use.
To parameterize expressions, we can use the class `TaxonomyConcept` (see [Section 6.2.4, "Specializations of `TaxonomyConcept`"](../06_model_concept/06_02_openodd_taxonomy.html#sec-specializations-of-taxonomyconcepts)), which can either be a `Container` aggregating multiple `TaxonomyConcept` instances or a `Type` including `Record`, `PrimitiveType`, `CategoricalLiteral`, and `Categorical`.

It is recommended to use the `$ as prefix` for parameterized expressions to distinguish them from other `TaxonomyConcept` instances.

What **ODD** Parameters are **not**:

* ODD Parameters are not "arguments to functions"; modules do not have functions.
* ODD Parameters are not **local variables** in modules; modules do not have variables.
* ODD Parameters are not scenario parameters because the ODD is not representing scenarios.
* ODD Parameters are not representing the configuration of the ADS, ADAS or CDAS system; ODD represents the environment rather than the vehicle.
* ODD Parameters are not representing the environment configuration; the environment is not controlled by engineering and is not a design artifact.
* ODD Parameters are not different from taxonomy concepts.

What parameters **are**:

* ODD Parameters are taxonomy concepts.
* ODD Parameters are instantiated in OD/COD much like any other taxonomy concepts.
* ODD Parameters can be used in expressions.
* ODD Parameters are means to provide meaningful values and avoid "hardcoding meaningless constants".

As an example, we can consider the following reasonable use of parameters:

Code 231. Example parameterized expressions (free-form notation)

```
TAXONOMY:
    region_parameters comprises
        $REGION_COUNTRY is one of
            - United States
            - Germany
        $SERVICE_AREA is a shapefile # binary record format
    parking_garage_parameters:
        $MAX_ALLOWED_SPEED_BUMP_HEIGHT: float length
        $MIN_REQUIRED_CLEARANCE: float length

MODULES:
    truck_parking_module:
        INCLUDES:
            speed_bump_height: "< $MAX_ALLOWED_SPEED_BUMP_HEIGHT" # max speed bump enabling truck to drive safely

        EXCLUDES:
            min_clearance: "< $MIN_REQUIRED_CLEARANCE" # required clearance required for truck to pass
```

This module includes 3 garage types, and a range of speed\_bump\_heights smaller than a threshold. The module excludes COds with min\_clearance greater than a threshold.

Further, consider the example COD in [Code 232](#code-example-instantiating-parameters) to illustrate the applicability of this module:

Code 232. Example instantiating parameters (free-form notation)

```
 Num   TEMPORAL_EXTENT     SPATIAL_EXTENT    $REGION_COUNTRY  $SERVICE_AREA      $MAX_ALLOWED_SPEED_BUMP_HEIGHT;cm    $MIN_REQUIRED_CLEARANCE;cm  SPEED_BUMP_HEIGHT;cm     MIN_CLEARANCE;cm
COD#1    08:16:45.341       13.401,52.521     Germany          svc_shapefile.shp    25                                   190                         10                       300
COD#2    10:31:53.917       13.402,52.522     Germany          svc_shapefile.shp    25                                   190                         20                       180
COD#3    13:36:03.180       13.403,52.523     Germany          svc_shapefile.shp    25                                   190                         30                       200
COD#4    15:42:22.843       13.404,52.524     Germany          svc_shapefile.shp    25                                   190                         30                       180
```

Coming back to the top, the following is the interpretation of the module and the COD:

* All CODs specify uniform values for the $MAX\_ALLOWED\_SPEED\_BUMP\_HEIGHT and $MIN\_REQUIRED\_CLEARANCE.
* COD#1 is **inside** the ODD because the SPEED\_BUMP\_HEIGHT satisfies the include condition, and MIN\_CLEARANCE does **not** satisfy the exclude condition.
* COD#2 is **outside** the ODD because **MIN\_CLEARANCE satisfies the exclude condition**.
* COD#3 is **outside** the ODD because SPEED\_BUMP\_HEIGHT does **not** satisfy the include condition\*.
* COD#4 is **outside** the ODD because SPEED\_BUMP\_HEIGHT does **not** satisfy the include condition\* and **MIN\_CLEARANCE satisfies the exclude condition**.

Going back to what parameters **are**:

* $MAX\_ALLOWED\_SPEED\_BUMP\_HEIGHT and $MIN\_REQUIRED\_CLEARANCE are taxonomy concepts.
* $MAX\_ALLOWED\_SPEED\_BUMP\_HEIGHT and $MIN\_REQUIRED\_CLEARANCE are instantiated in OD/COD much like any other taxonomy concepts.
* $MAX\_ALLOWED\_SPEED\_BUMP\_HEIGHT and $MIN\_REQUIRED\_CLEARANCE can be used in expressions.
* $MAX\_ALLOWED\_SPEED\_BUMP\_HEIGHT and $MIN\_REQUIRED\_CLEARANCE are means to provide meaningful values and avoid "hardcoding meaningless constants":

  + Instead of indicating speed\_bump\_height: "< 25" it is indicated that the number "25" has a specific meaning and thus speed\_bump\_height: "< $MAX\_ALLOWED\_SPEED\_BUMP\_HEIGHT"
  + Instead of indicating min\_clearance: "< 190" it is indicated that the number "190" has a specific meaning and thus min\_clearance: "< $MIN\_REQUIRED\_CLEARANCE"

## F.3 Assigning Parameter Values

The ASAM OpenODD® model allows combining COD files, see [Section 6.3.5, "Combining COD files"](../06_model_concept/06_03_openodd_od.html#sec-combining-cod-files).
This capability can be used to assign parameter values as follows:

Code 233. Example ASAM OpenODD® "config COD" used to instantiate parameters (free-form notation)

```
 Num        TEMPORAL_EXTENT        SPATIAL_EXTENT     $REGION_COUNTRY  $SERVICE_AREA      $MAX_ALLOWED_SPEED_BUMP_HEIGHT;cm    $MIN_REQUIRED_CLEARANCE;cm
COD#9999    Jan 1970 - Jan 2050    Europe              Germany          svc_shapefile.shp   25                                  190
```

The COD in this example:

* Defines a broad temporal and spatial extent which can be combined to any COD in Europe up until 2050.
* Specializes the region to Germany, and the service area to a specific shape file.
* Specifies the values for the parameters of $MAX\_ALLOWED\_SPEED\_BUMP\_HEIGHT and $MIN\_REQUIRED\_CLEARANCE using units of centimeters.

Key implications:

* Parameter names need to be unique; cannot have conflicting parameter names.
* Parameters definitions are global taxonomy concepts; their role is similar to the role of "CONSTANTS".
* Parameter (constant) values are scoped to specific SPATIAL and TEMPORAL EXTENTS.
* All parameters are global, much as system configuration is global for the system, and a schema is global for database systems.
* Neither taxonomies, modules nor imports instantiate parameters; CODs instantiate and assign values to them.
* Conditions within modules select matching CODs but do not assign values to those parameters, much as queries select rows satisfying specific value matches but do not assign values to fields in records.
* Multiple COD (config) files can be used, each instantiating a subset of the parameters.
* There is no need to join a (config) COD for parameters not used in a (main) COD.

Parameterized expressions can used in conditions.
The example [Code 234](#code-example-instantiating-parameters-2) demonstrates how `$region` and `$min_speed` can be integrated into conditions:

Code 234. Example instantiating parameters (free-form notation)

```
COD is
    $region is Germany
    $min_speed is 5 km/h
    ...

MODULES specification is as follows
    use_parameters is
        TITLE is "Example of using parameters"
    INCLUDE_AND when
        country is $region
        speed is greater than $min_speed
```

The value of $min\_speed can only be assigned in a COD:

* A dedicated (config) COD can be used to assign a value to $min\_speed for specific regions and times.
* Each row in that (config) represents different different $max\_speed values for different zones (e.g. low vs high speed zones), winter vs summer, or in bad weather CODs, e.g. when roads are icy.
* The parameter instantiations in a dedicated (config) COD is applied by joining it to other CODs, specifying different columns (representing other taxonomy concepts) much as tables are joined in databases, by matching the TEMPORAL\_EXTENT and SPATIAL\_EXTENT.
* It is not required to create a separate parameter (config) COD; instead, those parameters can be inlined as columns in each COD which needs them.

## F.4 Handling parameterized conditions in tabular formats

The parameterization of TaxonomyConcept instances within a `Module` or ODD specification provides more flexibility, as discussed in [Section F.2, “Parameterized expressions”](#sec-parameterized-expressions).
`TaxonomyConcept` `Attribute` instances can remain undefined during initial specification and be assigned values during usage.
This is typically indicated by the use of the `$ as prefix` for a `TaxonomyConcept` instance, which is a recommendation as outlined in [Section F.2, “Parameterized expressions”](#sec-parameterized-expressions).

The ASAM OpenODD® model supports parameterization of a `TaxonomyConcept`, enabling the use of placeholders in module, ODD, and COD specifications.
[Table 168](#tab-taxonomy-params) provides a tabular representation of a parameterized `Module` based on user-defined parameter `TaxonomyConcept` instances.

Table 168. Parameterized taxonomy - param\_taxonomy.csv


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE |
| --- | --- | --- | --- |
| scenery |  | record |  |
| ego\_parameters | scenery | record |  |
| **$ego\_width** | ego\_parameters | float | length |
| **$ego\_length** | ego\_parameters | float | length |
| **$ego\_height** | ego\_parameters | float | length |
| region\_parameters | scenery | record |  |
| **$region\_country** | region\_parameters | categorical |  |
| United States | **$region\_country** | categorical\_literal |  |
| Germany | **$region\_country** | categorical\_literal |  |
| **$service\_area** |  | shapefile |  |
| roads | scenery | record |  |
| road\_width | roads | float | length |
| dynamic\_environment |  | record |  |
| **$min\_speed** | dynamic\_environment | float | velocity |

Table 169. Module parameterization support


| MODULE\_ID | ROLE | CONTENT or CONDITION |
| --- | --- | --- |
| 001 | id | parametrized\_module1 |
| 001 | type | module |
| 001 | references | param\_taxonomy.csv |
| 001 | title-EN | Parametrized ODD template |
| 002 | include\_and | region: **$region\_country** |
| 002 | include\_and | road\_width: > 2 \* **$ego\_width** |