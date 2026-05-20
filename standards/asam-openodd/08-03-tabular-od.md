# ASAM OpenODD® v1.0.0 — 8.3 COD/OD mapping

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/08_tabular/08_03_openodd_tabular_od.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.3 COD/OD mapping

## 8.3.1 COD and OD tabular representation

The purpose of the tabular format specification is to provide a standardized format for exporting and importing current operational domain (COD) measurements and operational domain (OD).
This specification supports any tabular format including CSV, spreadsheet, and parquet files formats.

The COD and OD files can be provided with or without a manifest.

|  |  |
| --- | --- |
|  | A manifest file is a document containing metadata for a group of accompanying files that are part of a set or coherent unit. |

The manifest is useful to bind the COD table columns, that are not specified in taxonomy, with the taxonomy, and enables attaching additional *meta data* to each data column.
When a manifest file is used, it describes the full list of files in a data package.

A manifest file is recommended for COD and OD representation, discussed later in [Section 8.3.4, “Use of manifest file”](#sec-manifest-usage), but it is not required.
[Section 8.3.2, “Representation of a current operational domain without manifest”](#sec-representation-cod-without-manifest) demonstrates COD and OD representation without a manifest file, followed by instructions for specifying a COD and OD data package with a manifest file, see [Section 8.3.4, “Use of manifest file”](#sec-manifest-usage).

## 8.3.2 Representation of a current operational domain without manifest

### 8.3.2.1 General information and examples

If a manifest file is **not** provided, the following requirements apply to the OD and COD files:

The COD is a collection of measurements.
The representation of those measurements is a table, which satisfies the following constraints:

* Each row in the COD table represents a measurement for a specific `TEMPORAL_EXTENT` and `SPATIAL_EXTENT`.
* A single `TEMPORAL_EXTENT` column is provided with non-null values for all rows.
* A single `SPATIAL_EXTENT` column is provided with non-null values for all rows.

Refer to the format of shapefiles as defined by ESRI [[14](../bibliography.html#bib-esrishapefile)].

Every other column in the COD table, except `TEMPORAL_EXTENT` and `SPATIAL_EXTENT`, represents a taxonomy concept:

* Numeric columns:

  + Numeric fields shall be associated with a unit.
  + The unit is uniform for all rows and measurements.
  + The unit is specified as part of the header, for example the column name could be `rain_rate;mm/hr`.
  + When possible, numeric columns are associated with a specific value, for example `rain_rate;mm/hr: 5`.
  + When specific values are not known, numeric fields may specify a value range that represents uncertainty, for example `rain_rate.min;mm/hr: 4.9` or `rain_rate.max;mm/hr: 5.1`.
  + If quantitative uncertainty is needed, the metric aggregation columns can be used to quantify such uncertainty, for example `rain_rate.confidence_interval_min;%`, `rain_rate.confidence_interval_max;%`, `rain_rate.p75`, and so on.
* Categorical columns:

  + The enumerated values assigned shall be taxonomy concepts.
  + No units are associated with the field.
  + When possible, a single enumerated value is assigned to that column.
  + When uncertainty results in multiple detections that are associated with confidence levels, additional columns can be added to represent that uncertainty, for example `rain_level.confidence;%`, `rain_level.confidence.p75`, and so on.
* Object count columns:

  + An integer is used to specify a count, for example `pedestrian.count`.
  + When possible, a single value should be assigned that represents the measured count, for example from an object detection neural network.
  + Uncertainty can be represented using a range of values, for example `pedestrian.count: [3 .. 5]`.
* Boolean flag columns:

  + A categorical column is used to represent booleans.
  + When possible, limit the list of values to `true` and `false`.
  + Uncertainty can be represented with an `unknown` value.
    Adding `unknown` to the taxonomy is not necessary.
  + When quantitative uncertainty is needed, it can be represented with additional fields, for example `pedestrians.occurrence_rate;1/hr: < 1e-8`.
* Missing values:

  + When information is not available, the corresponding value is left empty.
  + Missing values are different than default values.
    No default values are provided in the COD.
  + Missing values are interpreted as `unknown`.
    Populating all missing values with the keyword `unknown` is not necessary.

[Table 130](#tab-cod-table) represents a number of interesting cases; more complex cases are discussed in [Section 8.3.4.4, “COD with complex structures”](#sec-complex-structures).
The units are only associated with numeric fields:

Table 130. Example COD table


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_RATE; mm/hr | RAIN\_LEVEL | IS\_PEDESTRIANS; boolean | PEDESTRIAN.COUNT |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | "2023-06-01 08:12:53.784" | "45.024 10.261" | 6.214 | moderate\_rain |  |  |
| 2 | "2023-06-01 08:12:54.149" | "45.024 10.261" |  |  | true | 1 |
| 3 | "2023-06-02 11:42:21.913" | "45.024 10.261" | 1.783 | light\_rain |  |  |
| 4 | "2023-06-02 11:42:22.427" | "45.024 10.261" |  |  | false | 0 |
| 5 | "2023-06-02 23:09:02.376" | "45.024 10.261" | 0.000 | no\_rain |  |  |
| 6 | "2023-06-02 23:09:02.508" | "45.024 10.261" |  |  | true | 2 |
| 7 | "2023-06-02 18:33:57.681" | "45.024 10.261" | 0.000 | no\_rain |  |  |
| 8 | "2023-06-02 18:34:04.262" | "45.024 10.261" |  |  |  |  |

[Table 130](#tab-cod-table) is interpreted as follows:

* Row #1 represents a sensor logging of `rain_rate = 6.214 mm/hr`, which is considered as `rain_level = moderate_rain`, but the pedestrian detector did not provide data for this timestamp.
* Row #2 represents a single pedestrian detection per `pedestrian.count = 1`, implying that `is_pedestrian = true`, but the rain sensor did not provide data for this timestamp.
* Row #3 represents a sensor logging of `rain_rate = 1.783 mm/hr`, which is considered as `rain_level = light_rain`, but the pedestrian detector did not provide data for this timestamp.
* Row #4 represents a single pedestrian detection per `pedestrian.count = 0`, implying that `is_pedestrian = false`, but the rain sensor did not provide data for this timestamp.
* Row #5 represents a sensor logging of `rain_rate = 0.000 mm/hr`, which is considered as `rain_level = no_rain`, but the pedestrian detector did not provide data for this timestamp.
* Row #6 represents a single pedestrian detection per `pedestrian.count = 2`, implying that `is_pedestrian = true`, but the rain sensor did not provide data for this timestamp.
* Row #7 represents a sensor logging of `rain_rate = 0.000 mm/hr`, which is considered as `rain_level = no_rain`, but the pedestrian detector did not provide data for this timestamp.
* Row #8 represents no detections at all.
  The row is empty.

|  |  |
| --- | --- |
|  | Missing values are valid and expected, because the sensors provide their data at different rates and TEMPORAL\_EXTENTs. The interpretation of missing values depends on the semantics and the toolchain. |

[Table 131](#tab-taxonomyexpressions) shows the taxonomy that supports the example in [Table 130](#tab-cod-table):

Table 131. Use of expressions for defining taxonomy concepts


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE | EXPRESSION | AFFILIATION\_SOURCE | AFFILIATION\_CONCEPT |
| --- | --- | --- | --- | --- | --- | --- |
| scenery |  | record |  |  | ISO 34503 | Scenery |
| vru | scenery | record |  |  | ISO 34503 | VRU |
| is\_pedestrians | vru | boolean |  |  | ISO 34503 | IsPedestrian |
| pedestrian | vru | integer |  |  | ISO 34503 | IsPedestrian |
| environmental\_conditions |  | record |  |  | ISO 34503 | environmental\_conditions |
| weather | environmental\_conditions | record |  |  | ISO 34503 | Weather |
| rainfall | weather | record |  |  | ISO 34503 | Rainfall |
| rain\_quantity | rainfall | float | precipitation\_rate |  | ISO 34503 | Rainfall Quantity |
| rain\_level | rain\_quantity | categorical | precipitation\_rate |  | ISO 34503 | environmental\_conditions |
| light\_rain | rain\_level | categorical\_literal |  | rain\_quantity < 2.5 mm/h | ISO 34503 | environmental\_conditions |
| moderate\_rain | rain\_level | categorical\_literal |  | rain\_quantity: [2.5,7.6] mm/h | ISO 34503 | environmental\_conditions |

[Code 102](#code-environment-conditions) shows how to map from the ASAM OpenODD® model to a tabular representation in [Table 131](#tab-taxonomyexpressions)

Code 102. Example environment conditions (free-form notation)

```
environment_condition is
    weather is
        rainfall is
            rain_quantity is a float representing precipitation rate
            rain_quantity_level is
                light_rain when rain_quantity is less than 2.5 mm/h
                moderate_rain when rain_quantity between 2.5 .. 7.6 mm/h
            vru is
                is_pedestrians is a boolean
                pedestrian.count is an integer representing count
```

|  |  |
| --- | --- |
|  | The columns of `TEMPORAL_EXTENT` and `SPATIAL_EXTENT` do not need to be in the taxonomy. |

### 8.3.2.2 Joining COD files

CODs are represented with data files.
Therefore, multiple files with CODs in overlapping geographical areas and time intervals may be merged.
When merging is performed, while the original COD files may contain overlapping fields, the merged COD file comprises the union of the fields, whereby shared fields are not duplicated.

[Code 102](#code-environment-conditions) represents the merge of [Table 132](#tab-examplecodrain1) and [Table 133](#tab-examplecodrain2):

Table 132. File1: cod\_rain.csv


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_RATE;mm/hr | RAIN\_LEVEL |
| --- | --- | --- | --- | --- |
| 1 | "2023-06-01 08:12:53.784" | "45.024 10.261" | 6.214 | moderate\_rain |
| 3 | "2023-06-02 11:42:21.913" | "45.024 10.261" | 1.783 | light\_rain |
| 5 | "2023-06-02 23:09:02.376" | "45.024 10.261" | 0.000 | no\_rain |
| 7 | "2023-06-02 18:33:57.681" | "45.024 10.261" | 0.000 | no\_rain |

Table 133. File2: cod\_vru.csv


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | IS\_PEDESTRIANS; boolean | PEDESTRIAN.COUNT |
| --- | --- | --- | --- | --- |
| 2 | "2023-06-01 08:12:54.149" | "45.024 10.261" | true | 1 |
| 4 | "2023-06-02 11:42:22.427" | "45.024 10.261" | false | 0 |
| 6 | "2023-06-02 23:09:02.508" | "45.024 10.261" | true | 2 |

The merged COD comprises the union of all columns, namely:

Code 103. Example union of all columns (free-form notation)

```
{ TEMPORAL_EXTENT, SPATIAL_EXTENT, RAIN_RATE;mm/hr  RAIN_LEVEL }
{ TEMPORAL_EXTENT, SPATIAL_EXTENT, IS_PEDESTRIANS, PEDESTRIAN.COUNT }
  =
{ TEMPORAL_EXTENT, SPATIAL_EXTENT, RAIN_RATE;mm/hr  RAIN_LEVEL, IS_PEDESTRIANS, PEDESTRIAN.COUNT }
```

## 8.3.3 Representation of an operational domain without manifest

The Operational Domain (OD) can be an aggregation of COD measurements in an area over a duration of time, which is equivalent to a `GROUP BY TEMPORAL_EXTENT and SPATIAL_EXTENT` in a database
However, OD can include data which is not coming from COD measurements, and such may include fields not specified in an COD, for example, the total length of roads covered.

This domain is specified in a tabular format, which specifies a list of columns, `n` on the composition.
Each column specifies a single `TaxonomyConcept` instance, `1` on the aggregation, and a single unit symbol, `0` on the aggregation, both defined outside the OD.
OD can include fields not specified in an COD, for example, the total length of roads covered.

The requirements for the OD table are identical to the requirements for COD, with the following adjustments:

* Each row in the OD may represent an aggregation of a collection of COD rows in one or more files.
* Instead of the `TEMPORAL_EXTENT` column, a single `TEMPORAL_EXTENT` column with non-zero values is provided for all rows.
* Instead of the `SPATIAL_EXTENT` column, a single `SPATIAL_EXTENT` column with non-zero values is provided for all rows.

OD can allow the representation of a superset of CODs.

[Table 134](#tab-od-row) combines all COD rows, from [Code 103](#code-union-of-all-columns) into a single OD row:

Table 134. Example OD row


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_RATE.MIN;mm/hr | RAIN\_RATE.MAX;mm/hr | RAIN\_LEVEL | IS\_PEDESTRIANS;boolean | PEDESTRIAN.COUNT.min | PEDESTRIAN.COUNT.max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ["2023-06-01 08:12:53.784","2023-06-02 18:34:04.262"] | shape.poly | 0.000 | 6.214 | [no\_rain, light\_rain, moderate\_rain] | [true,false] | 0 | 2 |

The use of min and max aggregations instead of range values is expressly permitted.
In this case, all ranges shall be translated into min-max values.

Inconsistent use of ranges and min-max is not permitted.
Either all ranges are converted to min-max or they remain in range format.

[Code 104](#code-single-record) is an OD, which represents a single record:

Code 104. Example single record (free-form notation)

```
TEMPORAL_EXTENT:        ["2023-06-01 08:12:53.784","2023-06-02 18:34:04.262"]
SPATIAL_EXTENT:         shape.poly
RAIN_RATE;mm/hr:        [0.000 .. 6.214]
RAIN_LEVEL:             [no_rain, light_rain, moderate_rain]
IS_PEDESTRIANS:         [true, false]
PEDESTRIAN.COUNT:       [0 .. 2]
```

Explicitly allowed:

* Rather than specifying the `RAIN_RATE` range [0.000 .. 6.214], better define two min-max columns, `RAIN_RATE.MIN=0.000` and `RAIN_RATE.MAX=6.214`.
  Similarly, the `PEDESTRIAN.COUNT` can be replaced by `PEDESTRIAN.COUNT.MIN` and `PEDESTRIAN.COUNT.MAX`.
  Further, the `RAIN_LEVEL` can be replaced with `RAIN_LEVEL.MIN` and `RAIN_LEVEL.MAX`.
  This eliminates the need for custom parsing of the range values.
* For the aggregation of CODs, the missing values may be removed or handled separately.

Strict Guidelines:

* For a given concept, the use of two-column min-max format together with range min-max format is not allowed.
* For a given concept, the mix of ranges and single values in the same column is not allowed.
* For a given concept, the use of lists of categorical literals and single categorical literals in the same column is not allowed.

The taxonomy required to support the above OD is the same as the taxonomy described above for the COD.

|  |  |
| --- | --- |
|  | The columns of `TEMPORAL_EXTENT` and `SPATIAL_EXTENT` do not need to be in the taxonomy. |

## 8.3.4 Use of manifest file

### 8.3.4.1 General information

An OD and COD is represented by a collation of data files that are collated using a manifest.
The following is the ASAM OpenODD® OD and COD file structure:

* An **optional manifest** file that specifies which files are part of the OD or COD, and how their columns map to the taxonomy.
* A collection of tabular files, for example csv, spreadsheets, or parquet, that compromise the data:

  + One or more taxonomy file that contains the taxonomy concepts that are referenced in the manifest.
  + One or more COD or OD file that contains the columns that are referenced in the manifest.

### 8.3.4.2 Manifest file specification

The optional manifest file is a tabular file that meets the following requirements:

* The file format can be csv, parquet or another tabular format.
* It comprises the following columns:

  + FIELD\_ID: An identifier for the field that is unique within the manifest file.
  + FILE\_NAME: The name of the file relative to the location of this manifest file.
  + TYPE: The type of the file, for example "taxonomy","od" or "cod".
    If the field names appear multiple times, the file type shall be the same.

    - taxonomy: A row of this type populates the FILE\_NAME, TYPE and Comment columns only.
    - cod: A row of this type populates all columns
  + COLUMN: The name of the column in the specified file.
  + TAXONOMY\_ID: The ID of the taxonomy concept which is represented by the column.
  + UNIT: The unit of the values specified.
    It is only populated for numeric values.
  + COMMENT: Should be used to provide the concept name, and possibly description that complements the ID specification.

### 8.3.4.3 Example file structure with manifest

This section provides an example file structure, with a single manifest file, a single taxonomy file and two COD files.

[Table 135](#tab-tabular-examplecodrain) is an example weather data file:

Table 135. File1: cod\_rain.csv


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RRTE | RL | value2 |
| --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01 08:12:53.784" | "48.0232 11.7153" | 6.214 | moderate\_rain | 300 |
| 2 | "2024-06-02 11:42:21.913" | "48.0232 11.7153" | 1.783 | light\_rain | 150 |
| 3 | "2024-06-02 11:42:21.913" | "48.0232 11.7153" | 0.000 | no\_rain |  |
| 4 | "2024-06-02 18:33:57.681" | "48.0232 11.7153" | 0.000 | no\_rain |  |

[Table 136](#tab-tabular-examplecodvru) is an example VRU data file:

Table 136. File2: cod\_vru.csv


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | PEDS | PCNT | value2 |
| --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01 08:12:54.149" | "48.0232 11.7153" | true | 1 | true |
| 2 | "2024-06-02 11:42:21.913" | "48.0232 11.7153" | false | 0 | true |
| 3 | "2024-06-02 23:09:02.508" | "48.0232 11.7153" | true | 2 | false |

Joining multiple COD files that include measurements and pertain to a single taxonomy concept shall be done on the basis of temporal and spatial extents, depending on the use-case.

These two files shall be collated using a manifest file that links them to the taxonomy.
[Table 137](#tab-tabular-examplemanifest) shows an example manifest file linking them:

Table 137. File3: cod\_manifest.csv


| FIELD\_ID | FILE\_NAME | TYPE | COLUMN | TAXONOMY\_ID | UNIT | COMMENT |
| --- | --- | --- | --- | --- | --- | --- |
| 001 | taxonomy.csv | taxonomy |  |  |  | Taxonomy CSV export of all concepts used by this COD. |
| 002 | cod\_rain.csv | cod | RRTE | rainfall\_rate | mm/hr | RAIN\_RATE |
| 003 | cod\_rain.csv | cod | RL | rainfall\_level |  | RAINFALL\_LEVEL |
| 004 | cod\_rain.csv | cod | value2 | droplet\_size | microns | DROPLET\_SIZE |
| 005 | cod\_vru.csv | cod | PEDS | is\_pedestrians |  | IS\_PEDESTRIANS |
| 006 | cod\_vru.csv | cod | PCNT | pedestrian.count |  | PEDESTRIAN.COUNT |
| 007 | cod\_vru.csv | cod | value2 | is\_gated |  | IS\_GATED |

[Table 137](#tab-tabular-examplemanifest) describes the meaning of each column relative to IDs that are specified in a taxonomy file.

### 8.3.4.4 COD with complex structures

The COD may be associated with `TaxonomyConceptValues` that refer to a `Record` `Type` (see [Section 6.2.5, "User defined types"](../06_model_concept/06_02_openodd_taxonomy.html#sec-concept-taxonomy-user-defined-types)).
In those cases, the value in each item within the `TaxonomyConceptValues` is a serialization of a complex structure.

[Code 105](#code-taxonomy-record-structure) is an example:

Code 105. Example taxonomy record structure (free-form notation)

```
TAXONOMY
    location comprises                                                 # record
        lat is a float attribute representing an angle                 # attribute
        lan is a float attribute representing an angle                 # attribute
    intersection comprises                                             # record
        center is a location attribute                                 # attribute
        type is a categorical accepting the following literal values   # categorical attribute
            T_junction                                                 # categorical literal
            Y_junction                                                 # categorical literal
```

For a COD with a **Taxonomy Concept Value** that points to the `intersection`, the **Record** could specify the value with a JSON format as in [Code 106](#code-json-format):

Code 106. Example JSON format

```
  {"center": {"lat": 48.0232, "lon": 11.7153}, "type": "T_junction"}
```

|  |  |
| --- | --- |
|  | With JSON, missing values are simply not specified:  * A **Record** in which all values are missing is denoted as `{}`. * A `location` with a missing `lat` value is denoted as `{"lon": 11.7153}`. * JSON does not provide typed value specifications. * JSON Schema may be used to validate the structure of a JSON serialization if required.  The following shall not be allowed and considered as an error: The library used for interpreting the COD data shall be able to detect a "missing value code" and shall be handled. |

Table 138. Example COD table with JSON **Record**


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_RATE;mm/h | RAINFALL\_TYPE | INTERSECTION |
| --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01 08:12:53.784" | "48.0232 11.7153" | 6.214 | convective | {"center": {"lat": 48.0232 "lon": 11.7153}, "type": "T\_junction"} |
| 3 | "2024-06-03 11:42:21.913" | "48.0232 11.7283" | 1.783 | dynamic | {"center": {"lat": 48.0232 "lon": 11.7283}, "type": "Y\_junction"} |
| 5 | "2024-06-05 11:42:21.913" | "48.0215 11.7153" | 0.000 |  | {"center": {"lat": 48.0215 "lon": 11.7153}, "type": "X\_junction"} |
| 7 | "2024-06-07 18:33:57.681" | "48.0208 11.7132" | 0.000 |  | {"center": {"lat": 48.0208 "lon": 11.7132}, "type": "Y\_junction"} |

### 8.3.4.5 OD with complex structures

The OD is similar to the COD, except that the values in the cell can be aggregates.
Therefore, the intersection example above is represented in a similar fashion.
The following is an example OD with complex structures:

* The `TEMPORAL_EXTENT` specifies an entire day rather than a timestamp.
* The `SPATIAL_EXTENT` contains a shape file that represents the polygon encompassing the intersection.
* The `RAIN_RATE` column represents a range of numeric values.
* The `RAINFALL_TYPE` column represents a list of possible categorical literal values.

Table 139. Example OD table with JSON **Record**


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_RATE;mm/h | RAINFALL\_TYPE | INTERSECTION |
| --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01" | "ShapeFile\_Intersection1.shp" | [5.023 .. 6.571] | convective | {"center": {"lat": 48.0232 "lon": 11.7153}, "type": "T\_junction"} |
| 3 | "2024-06-03" | "ShapeFile\_Intersection2.shp" | [0.412 .. 2.194] | dynamic | {"center": {"lat": 48.0232 "lon": 11.7283}, "type": "Y\_junction"} |
| 5 | "2024-06-05" | "ShapeFile\_Intersection3.shp" | 0.000 |  | {"center": {"lat": 48.0215 "lon": 11.7153}, "type": "X\_junction"} |
| 7 | "2024-06-07" | "ShapeFile\_Intersection4.shp" | 0.000 |  | {"center": {"lat": 48.0208 "lon": 11.7132}, "type": "Y\_junction"} |

### 8.3.4.6 Combining COD files

CODs are represented with data files.
Therefore, it could be necessary to merge multiple files that contain CODs in overlapping geographic areas and time intervals.
When merging is performed, while the original COD files may contain overlapping fields, the merged COD file comprises the union of the fields, whereby shared fields are **not** duplicated.
However, the processing of content from multiple files depends on the application or use case.

[Table 140](#tab-examplecodrain3) and [Table 141](#tab-examplecodvru3) are two examples for COD files:

Table 140. File1: cod\_rain.csv


| TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_RATE;mm/h | RAINFALL\_LEVEL |
| --- | --- | --- | --- |
| "2024-06-01 08:12:53.784" | "48.0232 11.7153" | 6.214 | moderate\_rain |
| "2024-06-02 11:42:21.913" | "48.0232 11.7153" | 1.783 | light\_rain |
| "2024-06-02 11:42:21.913" | "48.0232 11.7153" | 0.000 | no\_rain |
| "2024-06-02 18:33:57.681" | "48.0232 11.7153" | 0.000 | no\_rain |

Table 141. File2: cod\_vru.csv


| TEMPORAL\_EXTENT | SPATIAL\_EXTENT | IS\_PEDESTRIANS;boolean | PEDESTRIAN.COUNT |
| --- | --- | --- | --- |
| "2024-06-01 08:12:54.149" | "48.0232 11.7153" | true | 1 |
| "2024-06-02 11:42:21.913" | "48.0232 11.7153" | false | 0 |
| "2024-06-02 23:09:02.508" | "48.0232 11.7153" | true | 2 |

As shown above, the summarized COD comprises the combination of all columns, namely:

Code 107. Example combination of columns (free-form notation)

```
  { TEMPORAL_EXTENT, SPATIAL_EXTENT, RAIN_RATE;mm/hr  RAINFALL_LEVEL;categorical_literal }
  { TEMPORAL_EXTENT, SPATIAL_EXTENT, IS_PEDESTRIANS;boolean, PEDESTRIAN.COUNT;count }
  =
  { TEMPORAL_EXTENT, SPATIAL_EXTENT, RAIN_RATE;mm/hr  RAINFALL_LEVEL;categorical_literal, IS_PEDESTRIANS;boolean, PEDESTRIAN.COUNT }
```

The temporal and spatial extent are used to determine which rows need to be combined.
[Table 142](#tab-tabular-examplecodcombined) is the combined file:

Table 142. CombineFile: cod\_combined.csv


| TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_RATE;mm/h | RAINFALL\_LEVEL | IS\_PEDESTRIANS;boolean | PEDESTRIAN.COUNT |
| --- | --- | --- | --- | --- | --- |
| "2024-06-01 08:12:53.784" | "48.0232 11.7153" | 6.214 | moderate\_rain |  |  |
| "2024-06-01 08:12:54.149" | "48.0232 11.7153" |  |  | true | 1 |
| "2024-06-02 11:42:21.913" | "48.0232 11.7153" | 1.783 | light\_rain | false | 0 |
| "2024-06-02 23:09:02.376" | "48.0232 11.7153" | 0.000 | no\_rain |  |  |
| "2024-06-02 23:09:02.508" | "48.0232 11.7153" |  |  | true | 2 |
| "2024-06-02 18:33:57.681" | "48.0232 11.7153" | 0.000 | no\_rain |  |  |

Table 143. File3: cod\_manifest2.csv


| FIELD\_ID | FILE\_NAME | TYPE | COLUMN | TAXONOMY\_ID | UNIT | COMMENT |
| --- | --- | --- | --- | --- | --- | --- |
| 001 | taxonomy.csv | taxonomy |  |  |  | Taxonomy CSV export of all concepts used by this COD. |
| 002 | cod\_combined.csv | cod | RAIN\_RATE | rainfall\_rate | mm/hr | RAIN\_RATE |
| 003 | cod\_combined.csv | cod | RAIN\_LEVEL | rainfall\_level |  | RAINFALL\_LEVEL |
| 004 | cod\_combined.csv | cod | IS\_PEDESTRIANS | is\_pedestrian |  | IS\_PEDESTRIANS |
| 005 | cod\_combined.csv | cod | PEDESTRIAN\_COUNT | pedestrian.count |  | PEDESTRIAN\_COUNT |

Here in the [Table 143](#tab-tabular-examplemanifest2), a single manifest file captures the relevant information (for example, taxonomy id, unit) contained in the combined COD - [Table 142](#tab-tabular-examplecodcombined). Note that the column headers need not specify unit (as in [Table 142](#tab-tabular-examplecodcombined)), since this information is captured within a manifest file.
In case, multiple manifest files are created for each COD, their aggregation must ensure traceability within the combined COD.

### 8.3.4.7 OD aggregation of COD

An OD may aggregate one of more CODs.
The aggregation rules are as follows:

* An OD instance may compose zero or more COD instances.
* When an OD aggregates one of more COD, the aggregation requirements are as follows:

  + Every row in a COD is mapped to at most one row of an OD.
    In other words, an OD row composes multiple COD rows, and no COD row is shared between two OD rows.
  + The temporal extent of an OD row represents a time interval which is a union of all temporal extents of the COD rows that are mapped to it.
  + The spatial extent of an OD row represents a polygon which is a union of all lat-long positions of all COD rows to which it is mapped.
  + For each OD row, the values of each OD cell are an aggregation of all corresponding cells in all COD rows that are assigned to it.

|  |  |
| --- | --- |
|  | * The n-th COD or OD row is specified by the collection of all n-th items in the corresponding `TaxonomyConceptValues` instances of which the OD or COD is composed.   For example, considering a COD with 5 fields (=columns) and 9 measurements.   The COD has 5 `TaxonomyConceptValues` instances.   Each `TaxonomyConceptValues` instance of that COD is an array of 9 elements.   The 1st row comprises the 1st element from the first array (=column), plus the 1st element from the 2nd array (= 2nd field / column), plus the 1st element from the 3rd array (= 2nd field / column) and so forth. * There may be multiple ODs, each aggregating multiple CODs. * Both ODs and CODs may be stored in multiple files. * A single COD file may be aggregated into multiple OD files. |

### 8.3.4.8 Handling uncertainty associated with COD measurements

Measurements have uncertainty of two types:

* Aleatoric uncertainty means the limitations of the sensors results in an uncertain measurement.
  As an example, the position and distance measurement by the vehicle is uncertain.
  Such uncertainty can be modeled by providing a range of values, for example `distance: [10.6 .. 10.7] m`.
* Epistemic uncertainty means the limitations of sensor fusion and neural network detections.
  As an example, the detection of cyclists is uncertain.
  Such uncertainty can be represented either by multiple values, for example `vru: [cyclist, motorcycle]`, or by a confidence measure, for example `cyclist.confidence: 0.73`.

Furthermore, it may be crucial to capture the error or distribution that is associated with individual measurements.
This is particularly advantageous when performing inside or outside ODD analysis with COD specifications. (See [Section 6.4.6.4, "Working with uncertainty"](../06_model_concept/06_04_openodd_modules.html#sec-model-concept-modules-working-with-uncertainty))

Table 144. CombineFile: cod\_uncertain.csv


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAIN\_RATE;mm/h | RAINFALL\_LEVEL | IS\_PEDESTRIANS;boolean | PEDESTRIAN.CONFIDENCE;fraction |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01 08:12:53.784" | "48.0232 11.7153" | 6.214 | moderate\_rain |  |  |
| 2 | "2024-06-01 08:12:54.149" | "48.0232 11.7153" |  |  | true | 91% |
| 3 | "2024-06-02 11:42:21.913" | "48.0232 11.7153" | 1.783 | light\_rain | false |  |
| 4 | "2024-06-02 23:09:02.376" | "48.0232 11.7153" | 0.000 | no\_rain |  |  |
| 5 | "2024-06-02 23:09:02.508" | "48.0232 11.7153" |  |  | true | 75% |
| 6 | "2024-06-02 18:33:57.681" | "48.0232 11.7153" | 0.000 | no\_rain |  |  |

[Table 144](#tab-examplecoduncertain) demonstrates a possible way to incorporate uncertainty into a dataset that is relevant to COD measurements, or any relevant parameters.

* `TEMPORAL_EXTENT`:
  The exact timestamp of the measurement.
* `SPATIAL_EXTENT`:
  The geographic location where the measurement was taken, for example latitude or longitude.
* `RAIN_RATE` (mm/hr):
  The measured rainfall rate, which could be associated with the error in the COD measurement.
* `RAINFALL_LEVEL` (categorical\_literal):
  A categorical representation of the rainfall intensity, for example `light_rain`, `moderate_rain`, or `heavy_rain`.
* `IS_PEDESTRIANS` (Boolean):
  The indication whether pedestrians were detected.
* `PEDESTRIAN.CONFIDENCE` (fraction):
  A probability or confidence level that is associated with the pedestrian detection and acknowledges the uncertainty in this determination.

|  |  |
| --- | --- |
|  | Measures are regular numeric taxonomy attributes, and therefore are the responsibility of the taxonomy author. Every categorical concept can be associated with a measure by the taxonomy. Every column that represents a measure shall be linked to a taxonomy attribute. |