# ASAM OpenODD v1.0.0 — §6.3 COD/OD

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/06_model_concept/06_03_openodd_od.html
> **Standard**: ASAM OpenODD Base Standard 1.0.0 Specification, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2025-05-19

---

## 6.3.4.1 TaxonomyConceptValues specification

An instance of class `COD/OD` may be associated with an arbitrary number of instances of `TaxonomyConceptValues`. Each of these instances refers to an instance of class `Attribute`. A `TaxonomyConceptValues` instance itself can be related to an arbitrary number of instances of `Record`s or `Attribute`s defined in the taxonomy, representing a measured value for this taxonomy concept.

The COD/OD is represented by an array of arrays of values. This suggests using a tabular format as a simple way to represent a COD/OD.

### Example: Complex taxonomy structure

```
TAXONOMY
    weather is                                             # record
      rainfall_rate is float representing velocity         # attribute
      rainfall_type is                                     # categorical attribute
          dynamic                                          # categorical literal
          convective                                       # categorical literal
          orographic                                       # categorical literal
    intersection_features is                               # record
        refuge_island_count is an integer                  # numeric attribute
        number_of_ways is an integer representing count    # numeric attribute
        is_signalized is a boolean                         # boolean attribute
    intersection is                                        # record
        features is an intersection_features type          # attribute
        type is                                            # categorical attribute
            T_junction                                     # categorical literal
            Y_junction                                     # categorical literal
            X_junction                                     # categorical literal
```

### Example: TaxonomyConceptValues as JSON

```json
{
  "intersection_features": {
    "refuge_island_count": 2,
    "number_of_ways": 3,
    "is_signalized": true
  },
  "intersection_type": "T_junction"
}
```

Missing values handling:
- A **Record** in which all values are missing is denoted as `{}`
- Missing values are simply omitted
- The JSON representation does not provide typed value specifications
- JSON schema may be extracted from the Taxonomy for validation

### Example: COD table

| # | TEMPORAL_EXTENT | SPATIAL_EXTENT | RAINFALL_RATE (mm/hr) | RAINFALL_TYPE | INTERSECTION (record) |
|---|----------------|----------------|----------------------|---------------|----------------------|
| 1 | 2024-06-01 08:12:53.784 | 48.0232 11.7153 | 6.214 | convective | {"features": {"refuge_island_count": 2, "number_of_ways": 4, "is_signalized": true}, "type": "X_junction"} |
| 3 | 2024-06-03 11:42:21.913 | 48.0232 11.7283 | 1.783 | dynamic | {"features": {"refuge_island_count": 0, "number_of_ways": 3, "is_signalized": false}, "type": "Y_junction"} |
| 5 | 2024-06-05 11:42:21.913 | 48.0215 11.7153 | 0.000 | — | {"features": {"refuge_island_count": 0, "number_of_ways": 3, "is_signalized": true}, "type": "T_junction"} |

### OD vs COD

The OD is similar to the COD, except that the values in the cells may be aggregations:
- `TEMPORAL_EXTENT` specifies an entire day rather than a timestamp
- `SPATIAL_EXTENT` contains a shape file representing the polygon enclosing the intersection
- `RAINFALL_RATE` represents a range of numeric values (e.g., `[5.023 .. 6.571]`)
- `RAINFALL_TYPE` represents a list of possible categorical literal values

Range values are implemented as instances of class `Record` having two fields (e.g., `RAINFALL_RATE_MIN`, `RAINFALL_RATE_MAX`).

## 6.3.4.2 Class TaxonomyConceptValues

An instance of this class is a container for a collection of instances of class `Value` like a header of a column within an instance of class `COD_OD`.

| Property | Value |
|----------|-------|
| Instantiable | yes |
| Children | SpatialExtent, TemporalExtent |

### Parameters

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| name | String | yes | The name must be unique within the scope of a `COD_OD` instance. |
