# ASAM OpenODD® v1.0.0 — 10.3 COD/OD mapping

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/10_yaml/10_03_cod_od_mapping.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.3 COD/OD mapping

The mapping of ASAM OpenODD® model for COD and OD into YAML is achieved by specifying tabular data using a list of YAML data objects under an "COD" or "OD" element, respectively.
The COD and OD are defined using a collection of `TaxonomyConceptValues` arrays.
The mapping is achieved as follows:

* Each `TaxonomyConceptValues` instance is associated with a `TaxonomyConcept` (or `TEMPORAL_EXTENT` or `SPATIAL_EXTENT`), thus the list of `TaxonomyConceptValues` gives rise to a list of `TaxonomyConcept` instances.
* The collection of all first items in all `TaxonomyConceptValues` arrays (including the required `TEMPORAL_EXTENT` and `SPATIAL_EXTENT`) are associated with the first YAML object.
  In [Code 179](#code-example-cod) all elements with the first `-` are representing the first YAML object.
  Each of the fields within that object are mapped to a single TaxonomyConcept.
  Order does not matter and all fields are optional (that is can be empty).
* Similarly, the collection of all i-th items in each of the `TaxonomyConceptValues` is mapped to the i-th YAML object, comprising of the same list of fields based on the corresponding list of TaxonomyConcepts.
  Order does not matter and all fields are optional (that is can be empty).

Intuitively, a `TaxonomyConceptValues` represents a column in a spreadsheet, for example column A or B or C.
All columns have a uniform number of cells according to the total number of rows in that spreadsheet.
The 1st row in the spreadsheet represents the 1st cell in each column and the i-th row represents the i-th cell in each column.
This is illustrated by converting an example COD, provided in [Table 147](#tab-example-cod), into a list of YAML objects, provided in [Code 179](#code-example-cod).

As an example, consider [Table 147](#tab-example-cod), representing a number of interesting cases:

Table 147. Example COD as table


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAINFALL\_RATE;mm/hr | RAINFALL\_LEVEL;categorical\_literal | IS\_PEDESTRIANS;boolean | PEDESTRIAN\_COUNT;count |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01 08:12:53.784" | "48.0232 11.7153" | 6.214 | moderate\_rain |  |  |
| 2 | "2024-06-01 08:12:54.149" | "48.0232 11.7153" |  |  | true | 1 |
| 3 | "2024-06-02 11:42:21.913" | "48.0232 11.7153" | 1.783 | light\_rain |  |  |
| 4 | "2024-06-02 11:42:22.427" | "48.0232 11.7153" |  |  | false | 0 |
| 5 | "2024-06-02 23:09:02.376" | "48.0232 11.7153" | 0.000 | no\_rain |  |  |
| 6 | "2024-06-02 23:09:02.508" | "48.0232 11.7153" |  |  | true | 2 |
| 7 | "2024-06-02 18:33:57.681" | "48.0232 11.7153" | 0.000 | no\_rain |  |  |
| 8 | "2024-06-02 18:34:04.262" | "48.0232 11.7153" |  |  |  |  |

|  |  |
| --- | --- |
|  | Missing values are valid and expected, simply because the sensors provide their data at different rates and values for `TEMPORAL_EXTENT`. The interpretation of missing values depends on the semantics and the toolchain. |

[Code 179](#code-example-cod) shows this COD using YAML.

Code 179. Example COD as YAML

```
COD:
    - TEMPORAL_EXTENT:                     "2024-06-01 08:12:53.784"
      SPATIAL_EXTENT:                      "48.0232 11.7153"
      RAINFALL_RATE;mm/hr:                 6.614
      RAINFALL_LEVEL;categorical_literal:  moderate_rain
    - TEMPORAL_EXTENT:                     "2023-06-01 08:12:54.149"
      SPATIAL_EXTENT:                      "48.0232 11.7153"
      IS_PEDESTRIANS;boolean:              true
      PEDESTRIAN.COUNT;count:              1
    - TEMPORAL_EXTENT:                     "2024-06-02 11:42:21.913"
      SPATIAL_EXTENT:                      "48.0232 11.7153"
      RAINFALL_RATE;mm/hr:                 1.783
      RAINFALL_LEVEL;categorical_literal:  light_rain
    - TEMPORAL_EXTENT:                     "2024-06-02 11:42:22.427"
      SPATIAL_EXTENT:                      "48.0232 11.7153"
      IS_PEDESTRIANS;boolean:              false
      PEDESTRIAN.COUNT;count:              0
    - TEMPORAL_EXTENT:                     "2024-06-02 23:09:02.376"
      SPATIAL_EXTENT:                      "48.0232 11.7153"
      RAINFALL_RATE mm/hr:                 0.000
      RAINFALL_LEVEL;categorical_literal:  no_rain
    - TEMPORAL_EXTENT:                     "2024-06-02 23:09:02.50"
      SPATIAL_EXTENT:                      "48.0232 11.7153"
      IS_PEDESTRIANS;boolean:              true
      PEDESTRIAN.COUNT;count:              2
    - TEMPORAL_EXTENT:                     "2024-06-02 18:33:57.681"
      SPATIAL_EXTENT:                      "48.0232 11.7153"
      RAINFALL_RATE;mm/hr:                 0.000
      RAINFALL_LEVEL;categorical_literal:  no_rain
    - TEMPORAL_EXTENT:                     "2024-06-02 18:34:04.262"
      SPATIAL_EXTENT:                      "48.0232 11.7153"
```

|  |  |
| --- | --- |
|  | The last row in [Table 147](#tab-example-cod) and [Code 179](#code-example-cod) is left empty to illustrate the possibility of missing values. Empty rows are valid, but not useful. |