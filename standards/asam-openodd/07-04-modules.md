# ASAM OpenODD® v1.0.0 — 7.4 ODD modules

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/07_model_reference/07_04_modules.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.4 ODD modules

## 7.4.1 Module and section part

### 7.4.1.1 Overview

The module and condition related classes of {THIS\_STANDARD} model

Figure 19. The module and condition related classes of ASAM OpenODD® model

[Figure 19](#fig-reference-modules-module-classes) shows most of the classes related to class `Module` and class `Condition`, so [Figure 19](#fig-reference-modules-module-classes) is a subset of the ASAM OpenODD® model.

### 7.4.1.2 Class Module

An instance of class `Module` comprises of at least one include or exclude `Section` (either `AND` or `OR`). At most one include `Section` and one exclude `Section` are allowed. A comprehensive description of modules can be found in [Section 6.4, "ODD modules"](../06_model_concept/06_04_openodd_modules.html) .

Basic information
:   Table 108. Basic information of class Module


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 109. Class Module


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | The `Module` id, also referred to as handle, according to specifications in [Section 6.4.4.1, "Module specification"](../06_model_concept/06_04_openodd_modules.html#sec-module-specification) . This ID must be unique within the ASAM OpenODD® transmission. |
    | title | LangString | yes | This represents the title of the `Module`. It can be translated into other languages. At least an English title must be provided. |
    | description | LangString | no | This represents a description of the `Module`. It can be translated into other languages. |
    | comment | LangString | no | This represents a comment about the `Module`. It can be translated into other languages. |
    | is\_root | boolean | yes | If set to true this instance of class `Module` will be used as entry point for inference, no other instance of class `Module` can depend on it. |
    | is\_active | boolean | yes | A flag indicating whether an instance of class `Module` is active and its conditions shall be evaluated (active == true) or whether it should be ignored maybe temporarily (active == false) |
    | export\_instructions | String | no | The export instructions are used to specify where to export and in which format. See [Section 6.4.8.4, "Module export instruction format"](../06_model_concept/06_04_openodd_modules.html#sec-module-export-instruction-format) . |

### 7.4.1.3 Class Label

Instances of class `Label` are propositions which evaluate to `true` if at least one of the instances of class `Module` referencing it in its Label section evaluates to `true`. See [Section 6.4.3.4, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics) . `Label` instances can be used within Boolean `Expression` instances.

Basic information
:   Table 110. Basic information of class Label


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 111. Class Label


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | An identifier of the instance of class `Label` (not translated to multiple languages). This `id` string must not be a duplicate of a `Module` `id` or a `TaxonomyConcept` `id`. |

### 7.4.1.4 Class Tag

Each `Module` comprises zero or more instances of class `Tag`, each specifying a name string. These tags are used for organizational purposes only. Tags do not have semantic interpretation.

Basic information
:   Table 112. Basic information of class Tag


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 113. Class Tag


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | name | LangString | yes | The name of the instance of class `Tag`. It is not required to be unique and can be translated into other languages. |

### 7.4.1.5 Class Condition

Comprises a `TaxonomyConcept` and a boolean `Expression`.

Basic information
:   Table 114. Basic information of class Condition


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 115. Class Condition


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | is\_active | boolean | yes | A flag indicating whether a `Condition` is active shall be evaluated (active == true) or whether it should be ignored maybe temporarily (active == false) |
    | description | LangString | no | This represents a description of the instance of class `condition`. It can be translated into other languages. |
    | comment | LangString | no | This represents a comment about the instance of class `condition`. It can be translated into other languages. |

### 7.4.1.6 Class Section

A `Section` is a set of `Conditions` linked to a `Module`, comprising of a list of `Conditions`. The link defines whether it is an `EXCLUDE` or an `INCLUDE` section. The `Conditions` may be combined using the `SectionOperator`. [Section 6.4, "ODD modules"](../06_model_concept/06_04_openodd_modules.html)  explains the details of module sections.

Basic information
:   Table 116. Basic information of class Section


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 117. Class Section


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | operator | String | yes | Specifies whether the instance of class `Section` is an `AND` or an `OR` section. |

### 7.4.1.7 Enum SectionOperator

A `SectionOperator` can either be `AND` or `OR` where `AND` denotes that all included conditions must be fulfilled and `OR` means that at least one must be fulfilled.

Basic information
:   Table 118. Basic information of enum SectionOperator


    |  |  |
    | --- | --- |
    | **Instantiable** | no |

## 7.4.2 Expression part

### 7.4.2.1 Overview

The expression related classes of {THIS\_STANDARD} model

Figure 20. The expression related classes of ASAM OpenODD® model

[Figure 20](#fig-reference-modules-expression-classes) shows most of the classes related to class `Expression`, so [Figure 20](#fig-reference-modules-expression-classes) is a subset of the ASAM OpenODD® model.

### 7.4.2.2 Class Expression

An instance of this class is representing an expression denoting the meaning of a `Condition` or defining ranges for a `CategoricalLiteral` (see [Section 6.4.3.4, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics) ).

Basic information
:   Table 119. Basic information of class Expression


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Children** | CategoricalList, Equal, LowerBound, Range, UpperBound |

Parameters
:   Table 120. Class Expression


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | expr | String | yes | The value of this field contains the expression string having a well-structured syntax. |

### 7.4.2.3 Class LowerBound

`LowerBound` expressions: These expressions may specify inclusion or exclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance greater than a specified instance of class `Value`. It may also specify the meaning of the largest `CategoricalLiteral` within a categorical `TaxonomyConcept`.

Basic information
:   Table 121. Basic information of class LowerBound


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |

### 7.4.2.4 Class UpperBound

`UpperBound` expressions: These expressions may specify inclusion or exclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance lesser than a specified instance of class `Value`. It may also specify the meaning of the smallest `CategoricalLiteral` within a categorical `TaxonomyConcept`.

Basic information
:   Table 122. Basic information of class UpperBound


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |

### 7.4.2.5 Class Equal

These expressions may specify inclusion or exclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance equal to a specified instance of class `Value`.

Basic information
:   Table 123. Basic information of class Equal


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |

### 7.4.2.6 Class Range

These expressions may specify inclusion or exclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance between two instances of class `Value`. It may also specify the meaning of the `CategoricalLiteral` within a categorical `TaxonomyConcept`.

Basic information
:   Table 124. Basic information of class Range


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |

### 7.4.2.7 Class CategoricalList

These expressions may specify inclusion in the ODD of environment conditions with a `TaxonomyConceptValues` instance of `Categorical` type having at least one of a list of specified `CategoricalLiteral`. It may also specify the meaning of the `CategoricalLiteral` within a categorical `TaxonomyConcept`.

Basic information
:   Table 125. Basic information of class CategoricalList


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | Expression |