# ASAM Openodd v1.0.0 — Introduction

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/00_preface/00_introduction.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Introduction

## Overview

The focus of ASAM OpenODD is on an abstract model to define ODD as well as operational domains (OD), current operational domains (COD), and target operational domains (TOD) and implement these models in various formats.

The ASAM OpenODD model enables the definition of ODD conditions (environmental and other conditions) as well as if and when these conditions are included or excluded from the ODD specification.

The main part of ASAM OpenODD consists of multiple sections:

* [Section 6, "Model concept"](../06_model_concept/06_00_openodd_model_concept.html#top-model-concept) introduces the overall concept of ASAM OpenODD and focuses on the ASAM OpenODD model, the technology independent core of ASAM OpenODD.
* [Section 7, "Model reference"](../07_model_reference/07_00_model_reference.html#top-model-reference) presents a collection of all relevant class tables and the class diagram.
* [Section 8, "Model to tabular format mapping reference"](../08_tabular/08_00_tabular.html#top-model-tabular-mapping-reference),  [Section 9, "Model to ASAM OpenSCENARIO® DSL mapping reference"](../09_openscenario_dsl/09_00_openscenario_dsl.html#top-model-asam-openscenario-dsl-mapping-reference), and  [Section 10, "Model to YAML mapping reference"](../10_yaml/10_00_yaml.html#top-model-yaml-mapping-reference) are focusing on mapping references.
  The mapping references explain how to map from the ASAM OpenODD model, to a specific format/technology.

## Conventions and notations

### Modal verbs

To ensure compliance with the ASAM OpenODD specification, users need to be able to distinguish between requirements, recommendations, permissions, possibilities and capabilities, and external constraints.

Table 1. Verbal forms for expressions of provisions


| Provision | Verbal form | Definition |
| --- | --- | --- |
| Requirement | shall, shall not | A requirement conveys objectively verifiable criteria to be fulfilled and from which no deviation is permitted if conformance with the document is to be claimed. |
| Recommendation | should, should not | A recommendation conveys a suggested possible choice or course of action deemed to be particularly suitable without necessarily mentioning or excluding others. |
| Permission | may | A permission conveys consent or liberty (or opportunity) to do something. |
| Possibility and capability | can, cannot | A possibility conveys expected or conceivable material, physical or causal outcome.  A capability conveys the ability, fitness, or quality necessary to do or achieve a specified thing. |
| External constraint | must | An external constraint or obligation on the user of the document, for example laws of nature or particular conditions existing in some countries or regions, that is not stated as a provision of the document. External constraints are not requirements of the document. They are given for the information of the user. |

### Normative and informative content

Content in this specification can be normative or informative.
The sections listed in [Table 2](#tab-normative-informative-content) are normative or informative per definition.
Further informative content is shown in [Table 3](#tab-informative-text-components).

Table 2. Normative and informative sections


| Section | Indication |
| --- | --- |
| Foreword | Informative |
| Introduction | Informative |
| Scope | Normative |
| Normative references | Informative |
| Terms and definitions | Normative |
| Abbreviations | Normative |
| Backward compatibility | Normative |
| Model concept | Normative |
| Model reference | Normative |
| Model to tabular format mapping reference | Normative |
| Model to ASAM OpenSCENARIO DSL mapping reference | Normative, except for the Usage Guide which is informative (the heading contains the indication "(informative)") |
| Model to YAML mapping reference | Normative |
| Annex | Annexes can be normative or informative. The annex heading contains the indication "(normative)" or "(informative)". |
| Bibliography | Informative |

All other sections in this specification are normative.

Table 3. Informative text components


| Text components | Indication | Hints |
| --- | --- | --- |
| Notes | Informative | The document shall be usable without notes. |
| Footnotes | Informative | The document shall be usable without footnotes. |
| Examples | Informative | The document shall be usable without examples. |
| Sequence diagrams | Informative | The document shall be usable without sequence diagrams. |

Notes, footnotes, and examples shall not contain requirements or any information considered indispensable for the use of the document, for example, instructions or permission.

### Typographic conventions

This documentation uses the following typographical conventions:

Table 4. Typographical conventions


| Mark-up | Definition |
| --- | --- |
| `Code elements` | This format is used for code elements, such as technical names of classes and attributes, as well as attribute values. |
| *Terms* | This format is used to introduce glossary terms, new terms and to emphasize terms. |
| `Mathematical elements` | This format is used for calculations and mathematical elements. |
| `<element>` | This describes a tag for an element within the XML specification. |
| @attribute | The "@" identifies an attribute of any ASAM OpenODD element. |

## Deliverables

The following deliverables are provided for ASAM OpenODD:

* ASAM OpenODD Base Standard 1.0.0 Specification, 2025-04-03 (this document, contained in this site)