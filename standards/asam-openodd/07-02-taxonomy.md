# ASAM Openodd v1.0.0 — 7.2 Taxonomy

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/07_model_reference/07_02_taxonomy.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.2 Taxonomy

## 7.2.1 Taxonomy Part

### 7.2.1.1 Overview

The taxonomy related classes of {THIS\_STANDARD} model

Figure 16. The taxonomy related classes of ASAM OpenODD model

[Figure 16](#fig-reference-taxonomy-taxonomy-classes) shows most of the classes related to class `Taxonomy`, so [Figure 16](#fig-reference-taxonomy-taxonomy-classes) is a subset of the ASAM OpenODD model.

### 7.2.1.2 Class Taxonomy

`Taxonomy` is the root class of a taxonomy hierarchy of one or more instances of class `TaxonomyConcept`.

Basic information
:   Table 77. Basic information of class Taxonomy


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 78. Class Taxonomy


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | Unique identifier of a `Taxonomy` instance. It needs to be unique within an ASAM OpenODD transmission |
    | name | LangString | yes | This represents the name of the `Taxonomy`. It can be translated into other languages. At least an English name must be provided. |
    | affiliation | String | no | The source of a specific taxonomy. It can be used to distinguish `TaxonomyConcept` instances with the same name stemming from different sources. |

### 7.2.1.3 Class TaxonomyConcept

An instance of `TaxonomyConcept` is a node within the `Taxonomy` tree or subtree.

Basic information
:   Table 79. Basic information of class TaxonomyConcept


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Children** | Container |

Parameters
:   Table 80. Class TaxonomyConcept


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | This represents a unique textual handle of every `TaxonomyConcept` serving as the name for the reference to the concept in conditions. The key must be unique within the taxonomy files that are transmitted. Global uniqueness is not required. IDs shall be in English and are not translated to other languages. |
    | name | LangString | yes | This represents the name of the `TaxonomyConcept`. It can be translated into other languages. At least one name in English must be provided. |
    | description | LangString | no | This represents a description of the `TaxonomyConcept`. It can be translated into other languages. |
    | comment | LangString | no | This represents a comment about the `TaxonomyConcept`. It can be translated into other languages. |
    | export\_instructions | String | no | A string representing the export instruction. The format for instructions are specified in [Section 6.2.8, "Taxonomy export instruction format"](../06_model_concept/06_02_openodd_taxonomy.html#sec-taxonomy-export-instruction-format) . |

### 7.2.1.4 Class Container

An aggregation of a set of children of class `TaxonomyConcept`.

Basic information
:   Table 81. Basic information of class Container


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | TaxonomyConcept |

### 7.2.1.5 Class MetaData

`MetaData` can be added to `TaxonomyConcept`, `Module`, module level, section level, condition level, or the value level.

Basic information
:   Table 82. Basic information of class MetaData


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 83. Class MetaData


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | key | String | yes | A key of an instance of class `MetaData`. The key must be unique within all instances of `MetaData` - not required to be unique globally. |
    | value | <ASAM\_Data\_Type> | yes | A value for describing the metadata. The type must be one of ASAM standard data types as specified in ASAM Data Types [[1](../bibliography.html#bib-dt)]. |

### 7.2.1.6 Class File

Instances of this class represent the source files, for example, of `Taxonomy`, modular conditions and COD content.

Basic information
:   Table 84. Basic information of class File


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 85. Class File


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | name | String | yes | The file name |

### 7.2.1.7 Class LangString

Basic information
:   Table 86. Basic information of class LangString


    |  |  |
    | --- | --- |
    | **Instantiable** | no |

Parameters
:   Table 87. Class LangString


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | value | String | yes | The language-dependent text string, like a name or a description. |
    | intlCode | String | yes | A string denoting an international ISO 639 language code, for example, EN, DE, FR, ES (not case sensitive) |

## 7.2.2 Type Part

### 7.2.2.1 Overview

The type-related classes of {THIS\_STANDARD} model

Figure 17. The type-related classes of ASAM OpenODD model

[Figure 17](#fig-reference-taxonomy-type-classes) shows most of the classes related to class `Type`, so [Figure 17](#fig-reference-taxonomy-type-classes) is a subset of the ASAM OpenODD model.

### 7.2.2.2 Class Type

A typed `TaxonomyConcept`, which can either be a `Record` (that is a structured `Type` with `Attribute` instances), a `Categorical`, or a `PrimitiveType`.

Basic information
:   Table 88. Basic information of class Type


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | `TaxonomyConcept` |

### 7.2.2.3 Class Record

A structured type consisting of a set of instances of class `Attribute` as well as other instances of class `Record`.

Basic information
:   Table 89. Basic information of class Record


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | `Type` |

### 7.2.2.4 Class Attribute

A `TaxonomyConcept` used as an attribute within a `Record` structure. This is a leaf in the taxonomy tree which has no children.

Basic information
:   Table 90. Basic information of class Attribute


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 91. Class Attribute


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | This represents a unique textual handle of every `Taxonomy` element serving as the name for the reference to the concept in `Condition`. The key must be unique within the taxonomy files that are transmitted. Global uniqueness is not required. IDs shall be in English and are not translated to other languages. |
    | name | LangString | yes | An array of multi-language translations, at least an English name must exist. |
    | export\_instructions | String | no | A string representing the export instruction. The format for instructions are specified in [Section 6.2.8, "Taxonomy export instruction format"](../06_model_concept/06_02_openodd_taxonomy.html#sec-taxonomy-export-instruction-format) . |

### 7.2.2.5 Class PrimitiveType

A `PrimitiveType` is one of `boolean`, `integer`, `long`, `float`, `double`.

Basic information
:   Table 92. Basic information of class PrimitiveType


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | `Type` |

### 7.2.2.6 Class Categorical

A concept which accepts a predefined list of `CategoricalLiteral`. This is equivalent to an enumerated type.

Basic information
:   Table 93. Basic information of class Categorical


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | `Type` |

### 7.2.2.7 Class CategoricalLiteral

Specifies a possible value of a `Categorical` attribute, for example `road_type` is `expressway`. It can be associated with a range of values (using a `Range` expression, for example `rain_level` is [`medium` .. `high`]) or a `PrimitiveType` concept (having upper/lower bounds, for example, `rain_level` less than `high`) or a numerated list of `CategoricalLiteral` instances (using `CategoricalList` expression, for example, `road_type` is [`expressway`, `collector`, `arterial`, `town_local`]).

Basic information
:   Table 94. Basic information of class CategoricalLiteral


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 95. Class CategoricalLiteral


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | name | LangString | yes | An array of multi-language translation of the literal (at least English must be provided). The name must be unique within an ASAM OpenODD file transmission. |

### 7.2.2.8 Class UnitType

The type of unit used to identify unit groups which are compatible among which conversion is meaningful. The class is called physical dimension in the ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)].

Basic information
:   Table 96. Basic information of class UnitType


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 97. Class UnitType


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | A well-known unique English string identifying the instance of class `UnitType` according to the ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)], for example `velocity`, `precipitation_rate` |

### 7.2.2.9 Class Unit

A specific `Unit` associated with a numeric attribute and associated with a `UnitType`.

Basic information
:   Table 98. Basic information of class Unit


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 99. Class Unit


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | A unique string identifying the `Unit`, for example, `kph`. The list of unique strings is defined in the ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)] and can be extended as needed. |
    | name | String | yes | A name used for display but may not be unique |
    | factor | double | yes | Used for translation per ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)] |
    | offset | double | yes | Used for translation per ASAM Unit Handling Guide [[3](../bibliography.html#bib-uhg)] |