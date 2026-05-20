# ASAM Openodd v1.0.0 — 7.3 COD/OD

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/07_model_reference/07_03_cod-od.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.3 COD/OD

## 7.3.1 COD and OD Part

### 7.3.1.1 Overview

The COD/OD related classes of {THIS\_STANDARD} model

Figure 18. The COD/OD related classes of ASAM OpenODD model

[Figure 18](#fig-reference-COD_OD-COD_OD-classes) shows most of the classes related to class `COD_OD`, so [Figure 18](#fig-reference-COD_OD-COD_OD-classes) is a subset of the ASAM OpenODD model.

### 7.3.1.2 Class CODorOD

An instance of this class represents a collection of CODs or ODs.

Basic information
:   Table 100. Basic information of class CODorOD


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 101. Class CODorOD


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | name | String | yes | Unique name of the COD or OD. |

### 7.3.1.3 Class TaxonomyConceptValues

An instance of this class is a container for a collection of instances of class `Value` like a header of a column within an instance of class `COD_OD`.

Basic information
:   Table 102. Basic information of class TaxonomyConceptValues


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Children** | SpatialExtent, TemporalExtent |

Parameters
:   Table 103. Class TaxonomyConceptValues


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | name | String | yes | The name of a `TaxonomyConceptValues` instance must be unique within the scope of a `COD_OD` instance. |

### 7.3.1.4 Class Value

An instance of this class is a container holding values for CODs or ODs.

Basic information
:   Table 104. Basic information of class Value


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 105. Class Value


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | val | <Type> | yes | The type of field `val` is taken from one of the instances of the subclasses to `Type` of a given `Taxonomy`. It depends on the used taxonomies. |

### 7.3.1.5 Class TemporalExtent

For COD it specifies a single point in time; for OD it can also specify a time range.

Basic information
:   Table 106. Basic information of class TemporalExtent


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | TaxonomyConceptValues |

### 7.3.1.6 Class SpatialExtent

For COD it specifies a single location; for OD it can also specify an area.

Basic information
:   Table 107. Basic information of class SpatialExtent


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | TaxonomyConceptValues |