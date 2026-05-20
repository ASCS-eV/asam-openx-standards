# ASAM Openodd v1.0.0 — 6.1 Conceptual Overview

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/06_model_concept/06_01_openodd_model.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 6.1 Conceptual Overview

## 6.1.1 Introduction

The specified ODD is used to determine if any conditions that are encountered by the ADS are inside or outside of the ODD.
The ASAM OpenODD model defines rules to represent ODD, COD, OD, and taxonomy specifications.
The rules are defined by taxonomy concepts, conditions and other ASAM OpenODD model constructs.

The ASAM OpenODD model is the technology independent core of ASAM OpenODD.

The JSON serialization

|  |  |
| --- | --- |
|  | See  [Section 3, "Terms and definitions"](../03_terms_and_definitions/03_terms_and_definitions.html#top-terms_and_definitions-terms_and_definitions) for a definition of the term *ASAM OpenODD model*. |

|  |  |
| --- | --- |
|  | This chapter, [Section 6.1, "Conceptual Overview"](06_01_openodd_model.html), provides an overview of the concepts of ASAM OpenODD and the ASAM OpenODD model. Detailed technical aspects are covered in  [Section 6.2, "Taxonomy"](06_02_openodd_taxonomy.html#top-openodd-taxonomy),  [Section 6.3, "COD/OD"](06_03_openodd_od.html#top-concept-codod), and  [Section 6.4, "ODD modules"](06_04_openodd_modules.html#top-concept-modules). |

The ASAM OpenODD model describes the overall structure of an ASAM OpenODD specification.
The core of this structure revolves around the following key classes:

* Taxonomy:  
  This class and related classes represent a hierarchy of concepts used to model the ODD.
* Current Operation Domain (COD) / Operational Domain (OD):  
  This class represents the set of operating conditions related to taxonomy concepts.
* Module:  
  A modular rule specifies which environment conditions are included and which are excluded from the ODD.

  + Operational Design Domain (ODD):  
    Represents the environmental conditions of all modules.
  + Target Operational Domain (TOD):  
    Represents the expected environmental conditions of all modules.

A core principle of the ASAM OpenODD specification is the ability to export and import multiple formats via multiple interfaces.
Instances of class `Taxonomy` and `Module` provide their own export instructions.
Exports can result in a collection of files.
ASAM OpenODD provides the specifications for export and import that enable unambiguous exchange with respect to taxonomy, the COD/OD and the ODD boundary conditions across the compliant mapping references.
For limitations and restrictions, see the individual mapping references.
For example, ASAM OpenODD allows the import of an ASAM OpenODD YAML specification and its export as an ASAM OpenSCENARIO DSL specification.

## 6.1.2 ASAM OpenODD design goals

|  |  |
| --- | --- |
|  | A requirements analysis was conducted for this standard, resulting in the definition of several requirements. These requirements served as the basis for deriving the design goals. For a comprehensive overview of the requirements, see  [Annex E, *(informative) Requirements*](../11_annexes/11_a_requirements.html#top-requirements-analysis). |

The following high-level design goals shape the design approach of the ASAM OpenODD model:

1. Provide the structural representation of the ODD taxonomy including data types and unit types.
2. Provide the structural representation for defining CODs and ODs based on ODD taxonomy concepts in a data-centric fashion, including timestamp and location.
3. Provide the structural representation for the modular definition of ODDs and their constraining expressions based on ODD taxonomy concepts.
4. Provide a standard ASAM OpenODD model framework composed of the aforementioned structural representations, which the machine-readable ASAM OpenODD mapping references adhere to for the sake of interoperability.
   For limitations and restrictions, see the individual mapping references.
   Instead of developing a narrow specification for a single language, the current approach focuses on a model and corresponding interoperability requirements.
   This approach enables ASAM OpenODD to be interchangeable across all compliant mapping references, supporting multiple machine-readable languages and human-readable descriptions in multiple natural languages.

Offering this flexibility shall give ASAM OpenODD the capability to support the full ADS development life cycle:

* Requirements specification
* Engineering and development
* Simulation and testing
* Safety analysis
* Homologation
* Operation
* Dissemination of documentation

## 6.1.3 Supported features

### 6.1.3.1 Taxonomy features

ASAM OpenODD was designed with the following user stories for the taxonomy representation in mind:

* Define a taxonomy with diverse concept types:
  As a user, I want to create taxonomies that include concepts with various types such as records, categorical, or primitive to represent numerical, complex, temporal, and spatial taxonomy concepts.
* Support constrained ranges for categorical fields:
  As a user, I need to define categories using specific numeric ranges, to be able to express range of values.
* Support for user-defined types at various levels:
  As a user, I want the flexibility to define (complex) user-defined types.
* Support for user-defined measures on concepts:
  As a user, I want the expressibility for measures (for example, length) of a specific concept (for example, highway) in my taxonomy.
* Support aggregations on numeric fields:
  As a user, I need to calculate aggregated values such as maximum or average from my data fields, for example "maximum number of lanes", where "number of lanes" is a taxonomy concept.
* Support for assembling taxonomies from multiple sources:
  As a user, I want to build on existing taxonomies by importing concepts from other files from different sources.
* Extend concepts and types from imported taxonomies:
  As a user, I need the ability to extend imported taxonomies with my own custom types or add additional concepts.
* Multi-lingual support for taxonomy definitions:
  As a user, I want to define taxonomies in multiple languages to make them accessible across different regions.
* Specify unit conversions for numeric fields:
  As a user, I want to define valid unit conversions for my numeric fields to ensure consistency in measurements across different datasets.
* Search based on meta-data:
  As a user, I want to enrich taxonomy concepts with user-defined key-value pair information.

### 6.1.3.2 COD/OD features

ASAM OpenODD was designed with the following features for COD/OD representation in mind:

* Specification of a large number of CODs, for example billions, in a simple tabular format
* Support for simple standard formats such as tabular format (for example CSV, spreadsheet, Parquet and JSONL), XML, ASAM OpenLABEL, ASAM MDF.
  Other formats can be supported through translation to one of these formats.
* Specification of CODs with concepts, measures and units defined in taxonomy files
* Specification of uncertainty and confidence levels in CODs
* Specification of temporal (timestamps) and spatial (geo-location) extents at which each COD is measured
* Support for explicit negation, for example, `pedestrians: false`
* Interpretation of missing values as `unknown` to avoid the need for defaulting
* Support for merging multiple CODs with mismatching columns into a single COD file
* Definition of valid unit conversions
* Compiling an arbitrary collection of CODs into a single OD
* Support for comparison between ODs

### 6.1.3.3 ODD features

ASAM OpenODD was designed with the following features for ODD representation in mind:

* Modular rule specifications consisting of simple interpretable include and exclude sections
* Clear composition semantics using the constructs of `INCLUDE_AND`, `INCLUDE_OR`, `EXCLUDE_OR`, `EXCLUDE_AND`
* Support for expressive 2-level `AND`-`OR` expressions for each include as well as exclude statement
* Support for upper-bound, lower-bound and range constraints
* Definition of valid unit conversions
* Support for documentation with titles, descriptions and tags
* Enabled detection of interactions between modules, for example roadwork zones on freeways
* Multi-lingual support
* Support for traceability by external references, for example using metadata which may contain permalinks, and so on.
* Support for module re-use by importing modules into other files
* Support for module re-use by using asserted labels
* Definition of a module dependency tree, starting from a top-level ODD, using module handles and labels as tree edges
* Support for simple semantics with well defined propositional logic
* Support for rules with either open world semantics, by default, or closed world semantics, at the field level, for example, `EXCLUDE_*: officer: unknown`
* Specification of required fields, for example, `EXCLUDE_*: officer: unknown`, and forbidden fields
* Support for local inline-taxonomies to avoid the need to impact global taxonomy libraries
* Support for union and intersection of ODDs
* Associating meta data with every taxonomy concept

## 6.1.4 Exchange requirements

### 6.1.4.1 General information

The ASAM OpenODD specification is standardizing the exchange format.
In other words, it provides the export and import specification.
When exporting an ASAM OpenODD, the export is expected to include the taxonomy concepts required to support the subject:

* When exporting only a taxonomy, then only taxonomy content is needed.
  The export can contain a single file, or multiple files which use the `IMPORT` keyword linking the files.
* When exporting conditions within modules only, then the taxonomy file needs to be included with the export files (archive file).
  Note that some export formats support specifying both taxonomy and conditions within modules in the same file, while others require that taxonomy is exported in a separate file from the conditions (modules).
* When COD or OD are exported, the taxonomy file shall also be exported.
  The tabular representation also supports inclusion of an optional manifest used to map data table columns to taxonomy concepts in lieu of using the column headers.
* When both conditions within modules and COD or OD are exported, then the taxonomy export is also required.

### 6.1.4.2 Compliance requirements

An ODD specification, written using one of the ASAM OpenODD mapping references, is considered compliant if it remains equivalent after being translated into another mapping reference.
For example, `ODD1.csv` specification modeled with ASAM OpenODD model to tabular mapping reference (for example, using an additional Manifest construct) shall be equivalent when the same specification is modeled in ASAM OpenODD model to YAML mapping reference to be considered compliant.
Any additional constructs which are not specified or included in the mapping references are not compliant with ASAM OpenODD.

### 6.1.4.3 File specification

The model contains a class `File`. Instances of this class represent the artifacts transmitted to implement the standardized ASAM OpenODD exchange.
The format of each file is determined by the technology used to represent the content.
A single transmission, that is sending files from one stakeholder to another stakeholder, could include multiple files and use multiple formats.
As an example, a single transmission may comprise taxonomy, modular conditions and COD content.
The taxonomy content may be exchanged using YAML format, the modular condition may be exchanged using DSL format, and the COD or OD content may be exchange using tabular format (for example CSV or spreadsheet).
In other examples, a multi-language taxonomy content may be exchanged via e-mail comprising of spreadsheet attachments.
The collection of all files in a single transmission can be further encapsulated in a single archive file.

Each instance of class `File` shall be associated with a file name.
Files may refer to other files by means of an `IMPORT` which specifies file names.
ASAM OpenODD uses the standard file naming approaches commonly used by commercial operating systems, for example, file name followed by dot and file extension.
The specification of valid file names is not in scope for this standard.
The name of every file shall be unique within the scope of a single transmission.

### 6.1.4.4 Class File

Instances of this class represent the source files, for example, of `Taxonomy`, modular conditions and COD content.

Basic information
:   Table 5. Basic information of class File


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 6. Class File


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | name | String | yes | The file name |

### 6.1.4.5 Basic validation requirements

To ensure that every transmission is complete, the files required for each use case are listed:

* **Transmission of taxonomy only:** At least one taxonomy file is required.
  When multiple taxonomy files are transmitted, their IDs shall be unique within the set of transmitted taxonomy files.
  Each file can use `IMPORT` statements referring to other taxonomy files; the resulting dependency map shall not be cyclic.
* **Transmission of modules:** At least one module file is required as well as one or more taxonomy files in which the concepts referenced by the modules are defined.
  The module files need to be self-contained and include all referenced modules.
  It is not required that all taxonomy concepts are referenced; there is no need to remove unreferenced concepts.
  Similarly, it is not required that all modules are referenced by the dependency chain from the main root modules (of "ODD" kind); there is no need to remove unreferenced modules.
  Each file can use `IMPORT` statements referring to other module or taxonomy files; the resulting dependency map shall not be cyclic.
  Note that files may contain both taxonomy and modules.
* **Transmission of COD or OD:** At least one OD file is required as well as one or more taxonomy files in which the concepts referenced by the COD or OD are defined.
  The recommended option is for the column headers to use the concept names defined in the associated taxonomy file.
  Alternatively, a manifest file can be leveraged to specify the mapping of data columns to taxonomy concepts and units.
* **Transmission of modules with COD or OD:** Combine the requirements of "Transmission of modules" and "Transmission of COD or OD" for modules and COD or OD.

Transmission of the files can be done with or without an archive format.
There is no restriction on the number of files exported.
Specifically, it is recommended to pack all files as a single zip file, with or without a manifest.

To facilitate roundtrip validation, whereby the imported files are exported back and validated to be identical, the concept of "export instructions" was introduced.
Each format requires specifying the "export instructions" which enable reproducing the files imported to facilitate such roundtrip validation; the exact format of those instruction may differ across compliant exchange formats.
For example, one exchange format (for example YAML or XML or DSL) may use `IMPORT` statements, whereas a tabular format (for example CSV or spreadsheet) may specify the "export file column".

## 6.1.5 Taxonomies in ASAM OpenODD

### 6.1.5.1 Overview

This section introduces a model to capture various taxonomies, that is a meta model for taxonomies.
This means that taxonomies are instances of the classes (that is data objects) specified in this chapter and shown in the diagrams below.
This part of the model does not specify a concrete taxonomy.

The taxonomy related classes of {THIS\_STANDARD} model

Figure 1. The taxonomy related classes of ASAM OpenODD model

[Figure 1](#fig-concept-overview-taxonomy-classes) shows most of the classes related to class `Taxonomy`, so [Figure 1](#fig-concept-overview-taxonomy-classes) is a subset of the ASAM OpenODD model.

### 6.1.5.2 Taxonomy specification

A taxonomy is defined by an instance of class `Taxonomy` which is the main root entry point for the taxonomy.
It is possible to have multiple instances of class `Taxonomy` in a single ASAM OpenODD specification.
This enables the use of external taxonomies, for example, specifications based on ISO 34503 [[4](../bibliography.html#bib-iso34503)] and other standards.
Each instance of class `Taxonomy` represents an entire concept tree.
An instance of class `Taxonomy` shall contain zero or more instances of class `TaxonomyConcept`.
An instance of `TaxonomyConcept` represents a concept and consists of a taxonomy tree or subtree.
Deleting an instance of class `Taxonomy` leads to the deletion of all related instances of class `TaxonomyConcept`.

### 6.1.5.3 Class Taxonomy

`Taxonomy` is the root class of a taxonomy hierarchy of one or more instances of class `TaxonomyConcept`.

Basic information
:   Table 7. Basic information of class Taxonomy


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 8. Class Taxonomy


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | Unique identifier of a `Taxonomy` instance. It needs to be unique within an ASAM OpenODD transmission |
    | name | LangString | yes | This represents the name of the `Taxonomy`. It can be translated into other languages. At least an English name must be provided. |
    | affiliation | String | no | The source of a specific taxonomy. It can be used to distinguish `TaxonomyConcept` instances with the same name stemming from different sources. |

### 6.1.5.4 TaxonomyConcept specification

Each instantiation of class `TaxonomyConcept` shall specify:

* `ID` field  
  The `ID` is a unique string specifying an ID.
* `Export_Instructions` field  
  The export instructions are optional, and consist of a string with the export and import instruction, using one of the following options (a single uniform option shall be selected for all instances of class `Taxonomy`).
  The format of the instructions are specified in [Section 6.2.8, "Taxonomy export instruction format"](06_02_openodd_taxonomy.html#sec-taxonomy-export-instruction-format) and [Section 6.4.4.2, "Module export instructions details"](06_04_openodd_modules.html#sec-module-export-instructions-details).
* `Name` field  
  A list of values of type `LangString` that consists of two fields, one containing the name and a second one denoting the language using ISO 639 [[10](../bibliography.html#bib-iso639)] with two characters, for example, „weather“, „en“.
* `Description` field  
  Each containing a string with the description, and referencing a language using an ISO 639 [[10](../bibliography.html#bib-iso639)] with two characters.  
  A list of values of type `LangString` that consists of two fields, one containing the description and a second one denoting the language using ISO 639 [[10](../bibliography.html#bib-iso639)] with two characters.
  Each `LangString` entry represents a translation to a different language.
  Each language shall have a single translation.
* `Comment` field  
  A list of values of type `LangString` that consists of two fields, one containing the comment and a second one denoting the language using ISO 639 [[10](../bibliography.html#bib-iso639)] with two characters.
  Each `LangString` entry represents a translation to a different language.
  Each language shall have a single translation.  
  A single instance of class `TaxonomyConcept` can be referenced by multiple instances of class `LangString` representing a translation to a different language.  
  Multiple instances of class `LangString` with a common language may refer to a single instance of class `TaxonomyConcept`.
  There is no requirement that comments in different languages represent faithful translations.

### 6.1.5.5 Class TaxonomyConcept

An instance of `TaxonomyConcept` is a node within the `Taxonomy` tree or subtree.

Basic information
:   Table 9. Basic information of class TaxonomyConcept


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Children** | Container |

Parameters
:   Table 10. Class TaxonomyConcept


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | id | String | yes | This represents a unique textual handle of every `TaxonomyConcept` serving as the name for the reference to the concept in conditions. The key must be unique within the taxonomy files that are transmitted. Global uniqueness is not required. IDs shall be in English and are not translated to other languages. |
    | name | LangString | yes | This represents the name of the `TaxonomyConcept`. It can be translated into other languages. At least one name in English must be provided. |
    | description | LangString | no | This represents a description of the `TaxonomyConcept`. It can be translated into other languages. |
    | comment | LangString | no | This represents a comment about the `TaxonomyConcept`. It can be translated into other languages. |
    | export\_instructions | String | no | A string representing the export instruction. The format for instructions are specified in [Section 6.2.8, "Taxonomy export instruction format"](../06_model_concept/06_02_openodd_taxonomy.html#sec-taxonomy-export-instruction-format) . |

## 6.1.6 Type

### 6.1.6.1 Overview

The type-related classes of {THIS\_STANDARD} model

Figure 2. The type-related classes of ASAM OpenODD model

[Figure 2](#fig-concept-overview-type-classes) shows most of the classes related to class `Type`, so [Figure 2](#fig-concept-overview-type-classes) is a subset of the ASAM OpenODD model.

### 6.1.6.2 Type specification

Class `Type` is a subclass of class `TaxonomyConcept` and is specified as follows:

* A `Record` is a subclass of a `Type`.
  Instances of class `Record` are composed of one or more instances of type `Attribute`.
* An instance of class `Record` is related to one or more instances of class `Attribute`.
* Class `Attribute` contains two fields, `id` a string denoting the identifier of the attribute, and a reference to an instance of `Type`, denoting the type of the value of an attribute instance.
  Removal of the attribute does not remove the referenced `Type` specification.

  + Class `PrimitiveType` is a subclass of class `Type` and is one of `integer`, `float` or `boolean`.
  + Class `Categorical` is a subclass of class `Type`.
    An instance of `Categorical` is composed of one or more instances of class `CategoricalLiteral`.

    - Class `CategoricalLiteral` consists of a string representing a single possible `CategoricalLiteral` value.

      * The strings used in all instances of `CategoricalLiteral` within the scope of a single instance of class `Categorical` shall be unique.
      * An instance of `CategoricalLiteral` consists of a single expression specifying its relationship with an instance of `PrimitiveType`.  
        See [Section 6.4.8, "Expressions"](06_04_openodd_modules.html#sec-expressions) for more details.
      * All instances of class `CategoricalLiteral` referencing an instance of class `Expression` have an induced order based on the ranges specified.
        More details and examples are available in the  [Section 6.2, "Taxonomy"](06_02_openodd_taxonomy.html#top-openodd-taxonomy).
      * All instances of class `CategoricalLiteral` referencing an instance of class `Expression` shall satisfy the following requirements:

        + All references mentioned in an instance of class `Expression` shall specify a single common `PrimitiveType` instance.
        + At least a single instance of class `LowerBound` (expression) shall exist.
        + At least a single instance of class `UpperBound` (expression) shall exist.
        + The union of all ranges or lists in the corresponding expression shall cover all values for referenced instance of `PrimitiveType`.
      * An order is induced for all instances of class `CategoricalLiteral` which are referring to an instance of class `Expression`.
        More details and examples are available in the  [Section 6.2, "Taxonomy"](06_02_openodd_taxonomy.html#top-openodd-taxonomy).

### 6.1.6.3 Class Type

A typed `TaxonomyConcept`, which can either be a `Record` (that is a structured `Type` with `Attribute` instances), a `Categorical`, or a `PrimitiveType`.

Basic information
:   Table 11. Basic information of class Type


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | `TaxonomyConcept` |

### 6.1.6.4 Specification of measure

Measures are not explicitly represented by the model because they are specified as part of the `Taxonomy` instances.
As an example, the taxonomy author can introduce a `length` measure for the `contamination` of class `CategoricalLiteral` using the name `contamination.length`.
Such a measure can be used in a condition, for example, `contamination.length is less than 50 m` or as a column in an OD table representing the length of the contamination.

|  |  |
| --- | --- |
|  | For details on dot-notation, see [Section 6.4.6, "Conditions with user defined structures"](06_04_openodd_modules.html#sec-conditions-with-user-defined-structures). |

### 6.1.6.5 Illustrating taxonomy model usage

To illustrate usage of this model, consider the following ASAM OpenODD compliant example taxonomy:

* The root concept is called `weather`.
* The `wind` conditions are specified using a `wind_speed` numeric `Attribute`.
* `rainfall` conditions are specified using a `rainfall_rate` numeric `Attribute`.  
  In addition, a `rainfall_type` defines the three rain categories of `dynamic`, `convective` and `orographic`.

|  |  |
| --- | --- |
|  | Following this example taxonomy will be displayed in three different ways. [Figure 3](#fig-concept-overview-object_diagram-example_taxonomy) illustrates how the ASAM OpenODD model can be utilized to create an object diagram. [Figure 4](#fig-openodd-example-taxonomy-weather) simplifies the object diagram as a block diagram which should be easier to read. [Code 1](#code-openodd-example-taxonomy-weather) demonstrates the use of free-form notation to represent the object diagram in [Figure 3](#fig-concept-overview-object_diagram-example_taxonomy) and block diagram in [Figure 4](#fig-openodd-example-taxonomy-weather).  It is important to note that the ASAM OpenODD model operates at a meta-level. In the subsequent sections, examples often employ a free-form notation. The free-form notation is tighter and ensures better readability than object and block diagrams. |

A example taxonomy represented as an object diagram

Figure 3. A example taxonomy represented as an object diagram

[Figure 3](#fig-concept-overview-object_diagram-example_taxonomy) shows a object diagram visualization of an ASAM OpenODD compliant example taxonomy.

![image](../_images/06_openodd_model/odd_taxonomy_model_example.png)

Figure 4. A example taxonomy represented as a block diagram

[Figure 4](#fig-openodd-example-taxonomy-weather) shows a block diagran visualization of an ASAM OpenODD compliant example taxonomy.

|  |  |
| --- | --- |
|  | What is the free-form notation  ASAM OpenODD utilizes a free-form notation to describe concepts in a structured yet technology-independent manner. This structured notation provides a human-readable way to describe the concepts of ASAM OpenODD through examples. |

Code 1. A taxonomy example in free-form notation

```
weather is                                                          # This is a Record.
    wind is                                                         # This is a Record.
        wind_speed is a float representing velocity                 # This is an Attribute.
    rainfall is                                                     # This is a Record.
        rainfall_rate is a float representing precipitation_rate    # This is an Attribute.
        rainfall_type is                                            # This is an Attribute of type Categorical
            dynamic                                                 # This is a CategoricalLiteral specified by the categorical_literal symbol "dynamic".
            convective                                              # This is a CategoricalLiteral specified by the categorical_literal symbol "convective".
            orographic                                              # This is a CategoricalLiteral specified by the categorical_literal symbol "orographic".
```

This example is interpreted as follows:

* The `weather` `TaxonomyConcept` has two children, `wind`, for specifying wind-related concepts, and `rainfall`, to specify rain-related concepts.
* The `wind` concepts include a single numeric instance of class `Attribute` `wind_speed` representing the velocity of the wind; this field can be used to describe (later using modules) which wind speeds are within the ODD.
* The `rainfall` concepts includes which can also be used to describe (using modules) the corresponding rainfall conditions included in the ODD:

  + The numeric `Attribute` `rainfall_rate` representing the precipitation rate, namely the amount of rain falling per unit of time, and
  + The categorical `Attribute` `rainfall_type` for specifying the 3 types of rain which are supported.
    The defined types are `dynamic`, `convective` and `orographic`.

## 6.1.7 COD and OD

### 6.1.7.1 Overview

The COD/OD related classes of {THIS\_STANDARD} model

Figure 5. The COD/OD related classes of ASAM OpenODD model

[Figure 5](#fig-concept-overview-COD_OD-classes) shows most of the classes related to class `COD_OD`, so [Figure 5](#fig-concept-overview-COD_OD-classes) is a subset of the ASAM OpenODD model.

### 6.1.7.2 COD/OD concept overview

The Operational Domain (OD) describes all possible conditions that may be encountered by an Automated Driving System (ADS).
The Current Operational Domain (COD) represents measurements of environment conditions at a specific point in time and location.
Both COD and OD may include safe and unsafe conditions.
In the ASAM OpenODD model a common class `COD_OD` is used to represent both CODs and ODs.
All fields used in `COD_OD` COD instances and `COD_OD` OD instances must be defined in the `Taxonomy`.
Both OD and COD may include a small subset of the `Taxonomy` fields, and may have a disjoint set of fields.
It is possible that the fields used in a `COD_OD` instance for a COD, for example `wind_speed`, are aggregated in the `COD_OD` OD instance, for example as `wind_speed.avg`.

The modules, specified in the corresponding sections below, define the subset of safe conditions.
These modules specify ODD inclusion conditions using instances of class `TaxonomyConcept`.
A COD or OD is within an ODD when all conditions (described by modules) are satisfied.

In addition to the following chapters see also  [Section 6.3, "COD/OD"](06_03_openodd_od.html#top-concept-codod).

### 6.1.7.3 Current operational domain (COD) specifications

The COD and the OD are similar to each other.
The difference is that the environment observations at the COD are assumed to be made instantaneously.
For example, `TemporalExtent` and `SpatialExtent` represent a single point in time and a single geographic position.
Each set of instantaneous measurements is defined as a single COD.
An instance of class `COD_OD` representing an OD can be semantically considered as a large number of CODs, for example, the values may cover a large `TemporalExtent` or `SpatialExtent`.

If an instance of `COD_OD` represents a COD, it shall satisfy the following requirements:

* It shall be associated with a collection of instances of `TaxonomyConceptValues`.
  Intuitively, each `TaxonomyConceptValues` instance represent a column in a table or a spreadsheet, whereby the releated `TaxonomyConcept` - either a `Record` or an `Attribute` - provides the column name and description.
  A list or an array of values is associated to each instance of `TaxonomyConceptValues` to represent the cells within that column whereby the i-th element represent the cell in the i-th row.
* These values are represented by class `Value`. Therefore, a `TaxonomyConceptValues` instance itself can be related to zero to many of these `Value` instances.
* In case the `TaxonomyConceptValues` instance is associated with a **numeric** `PrimitiveType` then it needs to be associated with a `Unit` that is related to the same `UnitType`.
* Furthermore, each of these instances of `TaxonomyConceptValues` shall be associated to an array of instances of class `Value`.
* Deletion of an instance of class `TaxonomyConceptValues` removes all dependent instances of class `Value`.
* All these arrays of instances of class `Value` shall have the same length if the instances of class `TaxonomyConceptValues` belong the same instance of class `COD_OD`.
* The `TaxonomyConceptValues` instance is an array of `Value` instances belonging to the same instance of `COD_OD` derived from a measurement at specific locations, for example, at specific geo-coordinates, and point in time if this instance represents a COD.
  In this case it is also required, that the resolution for timestamp, latitude, and longitude for all arrays is uniform.
* When data is not available for the n-th measurement, that value at the n-th position in the array shall be empty and regarded as missing.
* It refers to exactly one instance of class `TemporalExtent`.
* It refers to exactly one instance of class `SpatialExtent`.

The representation of a missing value must always be the same within the scope of one instance of class `COD_OD`.

The following is left unconstrained:

* There is no minimum resolution requirement for the timestamp nor the latitudinal or longitudinal geo location associated with each measurement.
* Each instance of class `COD_OD` may have a different representation of a missing value as long as the library for loading the data can identify missing values.
* A COD-related `Value` instance within a `TaxonomyConceptValues` array may represent an `Attribute`, a complex `Record`, and possibly nested `Records`.  
  For example, consider the `Record` structure in [Code 2](#code-example-record-structure):

Code 2. Example record structure (JSON as commonly used in big data domain)

```
  {"center": {"lat": "48.0232 deg", "lon": "11.7153 deg"}, "type": "T_junction"}
```

|  |  |
| --- | --- |
|  | The JSON serialization needs to include units for numeric `Type` instances as expected from stand-alone fields (not within complex `Record` structures). |

For a more complex example see [Section 6.3.4, "COD/OD with complex structures"](06_03_openodd_od.html#sec-concept-COD_OD-with-complex-structures) or [Table 138](../08_tabular/08_03_openodd_tabular_od.html#tab-tabular-complexexamplecodtable) in model to tabular format mapping reference.

### 6.1.7.4 Example COD

|  |  |
| --- | --- |
|  | A COD can be represented with a table, but there are also different ways to represent a COD which is conform with ASAM OpenODD. This presentation was chosen so that it is easy for the reader to understand. |

[Table 12](#tab-examplecodtable) represents a number of interesting cases:

Table 12. Example CODs table. Each line represents a COD.


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAINFALL\_RATE; mm/h | RAINFALL\_LEVEL; categorical\_literal | IS\_PEDESTRIANS; boolean | PEDESTRIAN\_COUNT; count |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01 08:12:53.784" | "48.0232 11.7153" | 6.214 | moderate\_rain |  |  |
| 2 | "2024-06-01 08:12:54.149" | "48.0232 11.7153" |  |  | true | 1 |
| 3 | "2024-06-02 11:42:21.913" | "48.0232 11.7153" | 1.783 | light\_rain |  |  |
| 4 | "2024-06-02 11:42:22.427" | "48.0232 11.7153" |  |  | false | 0 |
| 5 | "2024-06-02 23:09:02.376" | "48.0232 11.7153" | 0.000 | no\_rain |  |  |
| 6 | "2024-06-02 23:09:02.508" | "48.0232 11.7153" |  |  | true | 2 |
| 7 | "2024-06-02 18:33:57.681" | "48.0232 11.7153" | 0.000 | no\_rain |  |  |
| 8 | "2024-06-02 18:34:04.262" | "48.0232 11.7153" |  |  |  |  |

[Table 12](#tab-examplecodtable) shows:

* Row #1 represents a sensor logging of `rainfall_rate equals 6.214 mm/h`.
  This rainfall rate is considered as `RAINFALL_LEVEL equals moderate_rain`.
  The pedestrian detector did not provide data for this timestamp.
* Row #2 represents a single pedestrian detection per `pedestrian.count equals 1` implying that `is_pedestrian equals true`.
  The rain sensor did not provide data for this timestamp.
* Row #3 represents a sensor logging of `rainfall_rate equals 1.783 mm/h`.
  This rainfall rate is considered as `RAINFALL_LEVEL equals light_rain`.
  The pedestrian detector did not provide data for this timestamp.
* Row #4 represents a single pedestrian detection per `pedestrian.count equals 0` implying that `is_pedestrian equals false`.
  The rain sensor did not provide data for this timestamp.
* Row #5 represents a sensor logging of `rainfall_rate equals 0.000 mm/h`.
  This rainfall rate is considered as `RAINFALL_LEVEL equals no_rain`.
  The pedestrian detector did not provide data for this timestamp.
* Row #6 represents a single pedestrian detection per `pedestrian.count equals 2` implying that `is_pedestrian equals true`.
  The rain sensor did not provide data for this timestamp.
* Row #7 represents a sensor logging of `rainfall_rate equals 0.000 mm/h`.
  This rainfall rate is considered as `RAINFALL_LEVEL equals no_rain`.
  The pedestrian detector did not provide data for this timestamp.
* Row #8 represents no detections at all.
  The row is empty.

Missing values are valid and expected, because the sensors provide their data at different rates and `TEMPORAL_EXTENTs`.
The interpretation of missing values depends on the semantics and the toolchain.

|  |  |
| --- | --- |
|  | In a COD represented as tabular format each row is an instance of class `TaxonomyConceptValues`. |

|  |  |
| --- | --- |
|  | If non-English languages are used to specify the values, the language shall be associated with the COD file and shall be uniform for all fields in a single COD. |

### 6.1.7.5 Operational domain (OD) specifications

Each instance of class `COD_OD` representing an operational domain (OD) consists of a collection of aggregate environment conditions, that are associated with a geographic area and a time interval.
Each such instance shall specify an ID string and compose one or more instances of class `TaxonomyConceptValues`.

Instances of class `TaxonomyConceptValues` associated with a COD\_OD instance representing an OD shall satisfy the following requirements:

* Refer to a single instance of class `Record`, class `Categorical` or class `Attribute`.
* Compose an array of zero or more instances of class `Value`.  
  Deletion of an instance of class `TaxonomyConceptValues` removes all dependent instances of class `Value`.
* Refer to an instance of class `Unit`.

Class `TemporalExtent` is a subclass of class `TaxonomyConceptValues`.
Instances of this class specify the time interval during which the environment conditions described by the OD were observed.
See temporal extent specification section for details on the supported time formats.

The `SpatialExtent` is a subclass of class `TaxonomyConceptValues`.
Instances of this class specify a geographic area where the environment conditions described by the OD were observed.
See spatial extent specification section for details on the supported file formats.

The OD schema shall satisfy the following requirements:

* Each row in the [Table 13](#tab-exampleodtable) represents an aggregation of a collection of COD `instances`, in one or more files.
* A single `TEMPORAL_EXTENT` column is provided instead of the COD `TEMPORAL_EXTENT`.
  This column contains non-null values for all instances.
* A single `SPATIAL_EXTENT` column is provided instead of the COD `SPATIAL_EXTENT`.
  This column contains non-null values for all instances.
* Each column in the OD corresponds to a column in the source COD.
  The only exceptions are the `TEMPORAL_EXTENT` and `SPATIAL_EXTENT` columns.

Table 13. Example ODs table


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | RAINFALL\_RATE; mm/h | RAINFALL\_TYPE; categorical\_literal | PEDESTRIAN\_COUNT\_AVG; count |
| --- | --- | --- | --- | --- | --- |
| 1 | "2024-06-01" | "ShapeFile\_GeoFenceArea1.shp" | [5.023 .. 6.571] | convective |  |
| 2 | "2024-06-02" | "ShapeFile\_GeoFenceArea1.shp" |  |  | 10.2 |
| 3 | "2024-06-03" | "ShapeFile\_GeoFenceArea1.shp" | [0.412 .. 2.194] | dynamic |  |
| 4 | "2024-06-04" | "ShapeFile\_GeoFenceArea1.shp" |  |  | 57.4 |
| 5 | "2024-06-05" | "ShapeFile\_GeoFenceArea1.shp" | 0.000 |  |  |
| 6 | "2024-06-06" | "ShapeFile\_GeoFenceArea1.shp" |  |  | 23.7 |
| 7 | "2024-06-07" | "ShapeFile\_GeoFenceArea1.shp" | 0.000 |  |  |
| 8 | "2024-06-08" | "ShapeFile\_GeoFenceArea1.shp" |  |  |  |

[Table 13](#tab-exampleodtable) shows:

* The OD comprises eight instances of class `TaxonomyConceptValues`.
  Each instance represents aggregate measurement performed during an entire day.
* The `TEMPORAL_EXTENT` column represents time interval during which the measurements were aggregated.
  In this case, it is a single day.
* The `SPATIAL_EXTENT` column represents the geographic area for which the measurements were aggregated.
  In this case, it is a single shape file. Other spatial extent formats are possible, including lat-long geo-coordinates.
* The `RAINFALL_RATE` column represents an instance of class `TaxonomyConceptValues` that points to the `Attribute` named `RAINFALL_RATE`.
  The `RAINFALL_RATE` is a float provided with the unit of `mm/h`.
* The `RAINFALL_TYPE` column represents an instance of class `TaxonomyConceptValues` that points to the `Attribute` named `RAINFALL_LEVEL`.
  The possible values are specified by the categorical literals `dynamic` or `convective`.
* The `PEDESTRIAN_COUNT_AVG` column represents an instance of class `TaxonomyConceptValues` that points to the `Attribute` named `pedestrian_count_avg`.
  The `pedestrian_count_avg` is a float without unit.
* Rows 1, 3, 5, and 7 specify values for the `RAINFALL_RATE` and `RAINFALL_TYPE`, but no value for `PEDESTRIAN_COUNT_AVG`.
  The values for `PEDESTRIAN_COUNT_AVG` during those days are unknown.
* Rows 2, 4, 6, and 8 specify values for `PEDESTRIAN_COUNT_AVG`, but no values for `RAINFALL_RATE` and `RAINFALL_TYPE`.
  The values for `RAINFALL_RATE` and `RAINFALL_TYPE` during those days are unknown.

The conditions, that are specified by the ASAM OpenODD modules, show which rows are within the ODD and which are outside.
The processing of the conditions needs to handle missing values.
The semantics of the modules' conditions is detailed in  [Section 6.4, "ODD modules"](06_04_openodd_modules.html#top-concept-modules).

|  |  |
| --- | --- |
|  | When the value of the field `name` of class `TaxonomyConceptValues` is in a non-English language, the language shall be associated with the COD file and shall be uniform for all instances of class `TaxonomyConceptValues` in the scope of an instance of class `COD_OD`. |

### 6.1.7.6 Class CODorOD

An instance of this class represents a collection of CODs or ODs.

Basic information
:   Table 14. Basic information of class CODorOD


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 15. Class CODorOD


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | name | String | yes | Unique name of the COD or OD. |

## 6.1.8 ODD condition modules (rules)

### 6.1.8.1 ODD condition modules overview

The module, condition and expression related classes of {THIS\_STANDARD} model

Figure 6. The module, condition and expression related classes of ASAM OpenODD model

[Figure 6](#fig-concept-overview-module-classes) shows most of the classes related to class `Module` and class `Condition`, so [Figure 6](#fig-concept-overview-module-classes) is a subset of the ASAM OpenODD model.

The ODD describes the conditions in which the ADS is intended to function.
ASAM OpenODD enables a modular specification of these conditions.

A collection of instances of class `Module` specifies the conditions.
The `Module` marked as root is used as the entry point for inference and can be understood as the ODD.
Each instance of `Module` defines an `IF-THEN` rule.
The `IF` section uses `INCLUDE` and `EXCLUDE` sections, and the `THEN` section sets a propositional fact to `true`.

For example, the conditions could be that the ADS can drive safely only when the `downlink_latency is less than 10 milliseconds` and the `downlink_throughput is larger than 1 Mbit/s`.
[Code 3](#code-if-then-condition-rule) shows how it can be done using the conceptual `IF-THEN` rule:

Code 3. Example specifying conditions (free-form notation)

```
IF (downlink_latency is less than 10 ms)
    AND (downlink_throughput is greater than 1 Mbit/s)
THEN good_connectivity;

IF good_connectivity
THEN included in ODD.
```

The modules are intended to represent such rules.

### 6.1.8.2 Module specification

#### 6.1.8.2.1 Classes and their relationships

The ASAM OpenODD model defines the following classes and their relationships.

Each instance of class `Module` represents a rule for including or excluding specific environment conditions from the ODD.
Each `Module` instance comprises one or more instances of class `Section`.

Each `Section` instance composes one or more instances of class `Condition`.
The deletion of a `Section` instance removes all `Condition` instances of which the `Section` consists.
A `Section` specifies a `section_operator` that can only be `AND` or `OR`.
A maximum of two nesting levels are permitted for `Section`:

* `AND` sections can compose only `OR` sections.
* `OR` sections can compose only `AND` sections.

It is not possible to assemble a single module across multiple files.
A `Condition` instance refers to a single instance of class `Expression` whereby deleting the `Condition` instances removes the related `Expression` instances as well.
See [Section 6.4.8, "Expressions"](06_04_openodd_modules.html#sec-expressions) for details about the specification of expressions.

There are four types of sections: `INCLUDE_AND`, `INCLUDE_OR`, `EXCLUDE_AND`, and `EXCLUDE_OR`.
All generic examples are given in free-form notation.

#### 6.1.8.2.2. `INCLUDE_AND`

All conditions have to be satisfied to satisfy the entire section.
[Code 4](#code-example-include-and) shows which conditions the `INCLUDE_AND` section can contain:

Code 4. Example INCLUDE\_AND (free-form notation)

```
INCLUDE_AND when
    downlink_latency is less than 10 ms
    downlink_throughput is greater than 1 MB/s
```

The ODD includes situations in which both `downlink_latency is less than 10 milliseconds`, and `downlink_throughput is greater than 1 megabyte per second`.

Within `INCLUDE_AND`, a nested subtype of `OR` can be used to provide a **single level** of disjunction within a section.
[Code 5](#code-example-include-and-with-subtype) shows how [Code 4](#code-example-include-and) can be extended to require that either `GPS` or `beacon_positioning` is available.

Code 5. Example INCLUDE\_AND with subtype OR (free-form notation)

```
INCLUDE_AND when
    downlink_latency is less than 10 ms
    downlink_throughput is greater than 1 MB/s
    OR
        global_positioning equals GPS
        local_positioning equals beacon_positioning
```

|  |  |
| --- | --- |
|  | The ODD would contain the additional condition that one of the positioning systems is supported. |

#### 6.1.8.2.3. `INCLUDE_OR`

At least one condition needs to be satisfied to satisfy the entire section.
[Code 6](#code-example-include-or) shows how the ODD can include situations in which either the barrier is a jersey barrier or a road marking is present:

Code 6. Example INCLUDE\_OR (free-form notation)

```
INCLUDE_OR when
    barrier equals jersey      # there is a jersey barrier
    road_marking equals any    # any type of road markings are present
```

Within `INCLUDE_OR`, a nested subtype of `AND` can be used to provide a **single level** of conjunction within a section.
[Code 7](#code-example-include-or-with-subtype) shows how [Code 6](#code-example-include-or) can be extended by adding the option to support operating within a geo-fenced area during operating hours:

Code 7. Example INCLUDE\_OR with subtype AND (free-form notation)

```
INCLUDE_OR when
    barrier equals jersey
    road_marking equals any
    AND
        region equals service_area1.shp
        time_of_day equals operating_hours
```

|  |  |
| --- | --- |
|  | The additional nested `AND` condition is optional, because it is nested within the `INCLUDE_OR`.  If the conditions `region` and `time_of_day` shall be fulfilled, this ODD condition can assume a situation even if the `barrier` is not a jersey barrier and no road marking is present. |

#### 6.1.8.2.4. `EXCLUDE_OR`

All conditions have to be unsatisfied to satisfy the entire section.

For example, [Code 8](#code-example-exclude-or) shows how the ODD can exclude situations in which the signs are not visible, **or** there are detour structures:

Code 8. Example EXCLUDE\_OR (free-form notation)

```
EXCLUDE_OR when
    not is_sign_visible
    temporary_road_structures equals construction_site_detours
```

|  |  |
| --- | --- |
|  | Two conditions are within an `EXCLUDE_OR` section. If either of them is `true` the situation is excluded. |

Within `EXCLUDE_OR`, a nested subtype of `AND` can be used to provide a **single level** of conjunction within a section.
[Code 9](#code-example-exclude-or-subtype-and) shows how [Code 8](#code-example-exclude-or) can be extended to only exclude detour structures on an expressway:

Code 9. Example EXCLUDE\_OR with subtype AND (free-form notation)

```
EXCLUDE_OR when
    is_sign_visible equals false
    AND
        temporary_road_structures equals construction_site_detours
        road_type equals expressway
```

|  |  |
| --- | --- |
|  | The additional nested `AND` condition is nested within the `EXCLUDE_OR`.  When the `construction_site_detours` is present and the `road_type` is `expressway`, then the situation is excluded regardless of sign visibility. |

#### 6.1.8.2.5. `EXCLUDE_AND`

At least one condition has to be NOT satisfied to satisfy the entire section.
[Code 10](#code-example-exclude-and) shows how the ODD can exclude situations in which **both** the signs are not visible, **and** there are detour structures:

Code 10. Example EXCLUDE\_AND (free-form notation)

```
EXCLUDE_AND when
    is_sign_visible equals false
    temporary_road_structures equals construction_site_detours
```

|  |  |
| --- | --- |
|  | Two conditions are within an `EXCLUDE_AND` section. If both of them are `true` the situation is excluded. |

Within `EXCLUDE_AND`, a nested subtype of `OR` can be used to provide a **single level** of disjunction within a section.
[Code 11](#code-example-exclude-and-subtype-or) shows how [Code 10](#code-example-exclude-and) can be extended to further require either channelized junctions or a double roundabout:

Code 11. Example EXCLUDE\_AND with subtype OR (free-form notation)

```
EXCLUDE_AND when
    temporary_road_structures equals construction_site_detours
    OR
        junction_feature equals channelized
        roundabout_size equals double_roundabout
```

|  |  |
| --- | --- |
|  | The additional nested `OR` condition is nested within the `EXCLUDE_AND`.  This results in reducing the exclusions with an additional condition to exclude `channelized` junctions or `double_roundabout`. |

A module can have zero or one `INCLUDE_*` sections, and zero or one `EXCLUDE_*` sections.
A module cannot have both `INCLUDE_AND` and `INCLUDE_OR` sections.
Similarly, a module cannot have both `EXCLUDE_OR` and `EXCLUDE_AND` sections.

#### 6.1.8.2.6 Further specification examples

A `Condition` within a section specifies a single concept where the condition can be specified in more detail like in the following examples.

[Code 12](#code-example-specific-categorical-value) shows a specific categorical value:

Code 12. Example specific categorical value (free-form notation)

```
temporary_road_structures is construction_site_detours
```

A list of possible values that each fulfill the condition.
That is called disjunction.
[Code 13](#code-example-possible-values) shows how situations with a `road_type` of `town_expressway`, `town_collector`, `town_arterial`, or `town_local` can be accepted:

Code 13. Example possible values (free-form notation)

```
road_type in
    town_expressway
    town_collector
    town_arterial
    town_local
```

[Code 14](#code-example-specific-numeric-value) shows a specific numeric value for situations with roundabout two lanes:

Code 14. Example specific numeric value (free-form notation)

```
roundabout_number_of_lanes equals 2
```

[Code 15](#code-example-upper-lower-bound-constraint) shows an upper bound constraint for rainfall of less than 2.5 mm/h:

Code 15. Example upper or lower bound constraint (free-form notation)

```
rainfall_rate is less than 2.5 mm/h
```

[Code 16](#code-example-range-constraint) shows a range constraint for `rainfall_rate` between 2.5 and 7.6 mm/h:

Code 16. Example range constraint (free-form notation)

```
rainfall_rate is in [2.5 .. 7.6] mm/h
```

[Code 17](#code-example-relative-constraint) shows a relative constraint for lane width of 0.5 m over the vehicle’s width:

Code 17. Example relative constraint (free-form notation)

```
min_lane_width is greater than 0.5 m + ego_vehicle_width
```

[Code 18](#code-example-exclude-wildcard) shows a condition that requires data to be available excluding `unknown` (reserved keyword):

Code 18. Example EXCLUDE\_\* (free-form notation)

```
EXCLUDE_* when
    officer is unknown    # value is required; cannot be missing
```

Where `EXCLUDE_*` is a placeholder for either `EXCLUDE_AND` or `EXCLUDE_OR`.

A module can specify a `Module` ID (string) as a dependency, followed by a 'true' or 'false' value.
For example, a `main_module` may specify the exclusion of a `bad_weather_module` and therefore excluding situations corresponding to bad weather conditions.
The example below excludes situations in which the module `bad_weather_module` evaluates to `true`.
[Code 19](#code-example-conditions-two-modules) shows how the conditions could be described:

Code 19. Example conditions of two modules (free-form notation)

```
main_module is
    EXCLUDE_OR when
        bad_weather_module is true

bad_weather_module is
    INCLUDE_OR when
        wind_speed is greater than 50 km/h
        ...
```

A `Module` instance can specify a `Label` that is confirmed when it is fulfilled.
This `Label` can be used in another condition.
For example, consider the possibility of several modules defining bad weather conditions that all set the `Label` `bad_weather` to `true`.
[Code 20](#code-example-conditions-multiple-modules) shows how these conditions could be described:

Code 20. Example conditions of multiple modules (free-form notation)

```
main_module is
    EXCLUDE_OR when
        bad_weather is true

bad_weather_module_1 is
    LABEL is bad_weather
    INCLUDE_OR when
        ...

bad_weather_module_2 is
    LABEL is bad_weather
    EXCLUDE_OR when
        ...
```

### 6.1.8.3 Missing value semantics

The ability to correctly handle missing data is critical for any data driven system.
In the context of propositional logic, there is a long history of attempts to automatically interpret missing values within the semantics:

* 3-values logic: Introduce a new 3rd value called `unknown` in addition to `true` and `false`, and define a 3-values truth table.  
  This solution has failed due to undesired and counter-intuitive interpretation of expression.
* Default values: Introduce a default value for every field.  
  This approach fails because the introduction of incorrect values leads to incorrect conclusions.
* Non-monotonic logic: Introduce a complex semantics that automatically determines how to interpret missing values based on the context.  
  This solution fails due to incorrect and counter-intuitive inferences that cannot be explained.

In the context of the ODD, all of these approaches result in incorrect assessment of safe operation.

ASAM OpenODD requires that handling of missing values will be specified explicitly in the conditions.
This is called missing value semantics.

|  |  |
| --- | --- |
|  | ASAM OpenODD model is able to specify equality expressions, but it is not intended to list the special value `unknown`. It is possible to use equality expressions that compare to `unknown` literals. |

* Close-World semantics (CWS):  
  Everything unspecified is assumed to be `false`.
  Situations with missing values for condition fields would be **excluded** as this condition would be evaluated as `false`.
  When using [Code 21](#code-example-1-missing-value-semantics), this is not desirable, as these situations are excluded in the usual situations in which fog does not play a role.
* Open-World semantics (OWS):  
  Everything unspecified is assumed to be `true`.
  Situations with missing values for condition fields would be **included** as this condition would be evaluated as `true`.
  When using [Code 22](#code-example-2-missing-value-semantics), this is not desirable, as in situations where no geo-fence data is available, these situations are included.

The ASAM OpenODD also uses:

* Missing-Value semantics (MVS):  
  Unless a value is explicitly required, use open-world semantics (OWS).
  The ODD condition shall specify exactly which data is required for the assessment of safe operation; otherwise, use close-world semantics (CWS).

[Code 21](#code-example-1-missing-value-semantics) and [Code 22](#code-example-2-missing-value-semantics) show that the missing value semantics can be described as a middle-ground between close-world and open-world semantics:

Code 21. Example 1 missing value semantics (free-form notation)

```
If fog_level is severe then exclude from ODD.
```

Code 22. Example 2 missing value semantics (free-form notation)

```
If vehicle in a geofenced service area then include in ODD.
```

Considering [Code 21](#code-example-1-missing-value-semantics):
When the ODD condition specifies, that fog data is required, then situations without fog data are excluded.
When fog data is not required, then situations without fog data are included.

Considering [Code 22](#code-example-2-missing-value-semantics):
When the ODD condition specifies, that geofence data is required, then situations without geofence data are excluded.
When geofence data is not required, then situations without geofence data are included.

The data can be required in two forms.

* Option 1: Include situation when a field value is `any`.
  For example, `include when fog is any` or `include when geofence is any`.
* Option 2: Exclude situation when a field value is `unknown`.
  For example, `exclude when fog is unknown` or `exclude when geofence is unknown`.

See [Section 6.1, "Conceptual Overview"](06_01_openodd_model.html) for details.

## 6.1.9 Modeling patterns

### 6.1.9.1 Basic use case decomposition

Use case decomposition is applicable to top-level specification of an ODD.
Instead of specifying all use cases in a single model, this pattern is applied to have a single top-level module that lists all use cases.
Each use case is represented by one or more use case modules.

Consider an example for specifying the ODD for a sample ADS, by listing the list of use cases covered.
This can be achieved by an `INCLUDE_OR` section that lists the supported use cases.

[Code 23](#code-example-odd-sample) shows how this pattern is characterized by using an `INCLUDE_OR` section in the ODD root module specification, and specifying the list of use cases within that section.

Code 23. Example ODD for sample ADS (free-form notation)

```
ODD_sample_v1.01.23 is
    INCLUDE_OR when
        ucm_passenger_pickup is true
        ucm_city_street_driving is true
        ucm_highway_driving is true
        ucm_passenger_dropoff is true
        ucm_self_parking is true

ucm_passenger_pickup is
    INCLUDE_OR when
        ...

ucm_city_street_driving is
    INCLUDE_OR when
        ...

...
```

[Code 23](#code-example-odd-sample) contains:

* The specified ODD version is `sample_v1.01.23`.
* Each use case is defined in a module:

  + The "passenger pickup" use case is defined in the `ucm_passenger_pickup` module.
  + The "city street driving" use case is defined in the `ucm_city_street_driving` module.
  + The "highway driving" use case is defined in the `ucm_highway_driving` module.
  + The "passenger dropoff" use case is defined in the `ucm_passenger_dropoff` module.
  + The "self parking" use case is defined in the `ucm_self_parking` module.

The module’s semantic interpretation can be summarized as follows:

* A situation is included in the ODD if it is included in one of the use case modules listed in the `INCLUDE_OR` section of `sample_v1.01.23`.
* A situation is excluded if it is not allowed in **all** listed modules.

The classification of the use case applicable to each situation is either:

* based on sensors external to the ADS, for example, weather conditions, or
* based on internal ADS signals originating from an on-board planning component.

These signals can be added to the COD and OD to support interpretation of situations.

### 6.1.9.2 Cartesian product decomposition

A more complicated requirement involves specifying a collection of use cases that represent all possible combinations of components.
As an example, consider representing the use cases from the previous section.
In addition, indicate when operation is allowed, which cities are included, and what type of positioning is required.
It is important that not all combinations of modules are specified.

The following combination (expressed by the id/title) represents a less modular definition, which becomes a collection of very specific definitions.
This approach is not recommended.
The user is encouraged to follow modular definitions which enable more flexibility.

* Define a module for `passenger_pickup_normal_operation_hours_hanover_gps`.
* Define a module for `passenger_pickup_normal_operation_hours_hanover_lps`.
* Define a module for `passenger_pickup_normal_operation_hours_munich_gps`.
* Define a module for `passenger_pickup_normal_operation_hours_munich_lps`.
* Define a module for `passenger_pickup_emergency_to_hospital_hanover_gps`.
* Define a module for `passenger_pickup_emergency_to_hospital_hanover_lps`.
* …​

|  |  |
| --- | --- |
|  | Following example `ODD_Sample_v1.1.23` will be represented in three different variants. The instantiated object diagram for this example is provided in [Figure 7](#fig-concept-overview-object_diagram-example_module). The same example is shown in [Figure 8](#fig-concept-overview-modules-example) as a simplified block diagram. The same example is shown in [Code 24](#code-example-AND-OR-nesting-pattern) in a free-form notation. The free-form notation is tighter and ensures better readability than the block and the object diagrams. |

Example AND-OR nesting pattern represented as object diagram

Figure 7. Example AND-OR nesting pattern represented as object diagram

[Figure 7](#fig-concept-overview-object_diagram-example_module) shows the example as object diagram.
The same example is presented as simplified block diagram in [Figure 8](#fig-concept-overview-modules-example) and as free-form notation in [Code 24](#code-example-AND-OR-nesting-pattern).

![image](../_images/06_openodd_model/odd_example_moya.png)

Figure 8. Example AND-OR nesting pattern represented as block diagram

[Figure 8](#fig-concept-overview-modules-example) shows the example as block diagram.
The same example is presented as free-form notation in [Code 24](#code-example-AND-OR-nesting-pattern).

Code 24. Example AND-OR nesting pattern (free-form notation)

```
ODD_sample_v1.01.23 is
    INCLUDE_AND when
        OR
            passenger_pickup is true
            city_street_driving is true
            highway_driving is true
            passenger_dropoff is true
            self_parking is true
        OR
            normal_operation_hours is true
            emergency_pickup_to_hospital is true
            special_event_charter is true
        city is
            hanover
            munich
        positioning is
            global_positioning_system
            local_positioning_beacon
```

[Code 24](#code-example-AND-OR-nesting-pattern) shows how to avoid specifying all these combinations by using an `AND-OR` nesting pattern:

* Use a top-level `INCLUDE_AND`.
* Use a nested `OR` for each cartesian product component.

Subsequently, modules shall be defined for the use cases of `passenger_pickup`, `city_street_driving`, `highway_driving`, `passenger_dropoff`, `self_parking`.
Similarly, modules shall be defined for `normal_operation_hours`, `emergency_pickup_to_hospital` and `special_event_charter`.

[Code 24](#code-example-AND-OR-nesting-pattern) contains:

* The specified ODD version is `sample_v1.01.23`.
* A top-level `INCLUDE_AND` section collates all the components of the cartesian product.
* A collection of use cases is listed under the first `OR` sub-section.
  Each use case is defined in a module.
* A collection of temporal conditions is listed in the second `OR` sub-section.
  Temporal conditions define when to operate.
  Each temporal condition is defined in its own module.

|  |  |
| --- | --- |
|  | The city and positioning conditions are included directly under the `INCLUDE_AND` section because they represent a nested `OR` sub-section (within the parent 'INCLUDE\_AND' section). In other words, the `INCLUDE_AND` section can contain zero or more `OR` sub-sections. Similarly, the `INCLUDE_OR` section can contain zero or more `AND` sub-sections. The same applies for the `EXCLUDE_AND` and `EXCLUDE_OR` sections. |

The semantic interpretation of [Code 24](#code-example-AND-OR-nesting-pattern) is as follows:

A situation is included in the ODD:

* In any of the use case modules listed in the 1st `OR` sub-section.
* In any of the temporal conditions listed in the 2nd `OR` sub-section.
* If the situation is located in one of the cities listed under the condition for city.
* If the situation is supported by one of the positioning options listed under the positioning condition.

A situation is **excluded** in the ODD:

* In any use cases **except** those listed within the first nested `OR`.
* In the context of any temporal constraints **not** listed within the second `OR`.
* If the situation is not located in any of the cities listed.
* If the situation is not supported by any of the connectivity technologies listed.

### 6.1.9.3 Taxonomy based decomposition

Another important decomposition pattern is the restriction of the concepts used in the conditions to the concepts of a taxonomy subtree.
Such restrictions avoid the unmanageable combinatorics associated with the specification and evaluation of conditions for multiple environment domains.

As an example, consider a taxonomy hierarchy that contains subtrees for environmental conditions, scenery elements, and dynamic elements.
Such a hierarchy could be used to decompose conditions by grouping all environmental related conditions in an environmental module, all scenery related conditions in a scenery element’s module, and all dynamic environment conditions in a dynamic element’s module.

Such a decomposition can be applied recursively.
For example, the scenery modules can be decomposed according to acceptable `road_conditions` and `intersection_conditions`.

This pattern is characterized by using an `INCLUDE_AND` section that refers to condition modules.
The condition modules refer to concepts within a pre-determined taxonomy subtree.

To illustrate the hierarchical decomposition based on the taxonomy, consider a taxonomy that defines a weather sub-tree and a scenery sub-tree.
[Code 25](#code-example-referring-sub-trees) shows how to define a top-level module referring to the two sub-trees:

Code 25. Example referring to sub-trees (free-form notation)

```
passenger_pickup is
    INCLUDE_AND when
        acceptable_weather is true
        supported_scenery is true
```

[Code 26](#code-example-defining-sub-trees) shows how to define the modules for each of the sub-trees by further listing the weather and scenery components:

Code 26. Example defining sub-trees (free-form notation)

```
acceptable_weather is
    INCLUDE_AND when
        acceptable_lighting is true
        acceptable_rainfall is true
        acceptable_wind is true
    ...

supported_scenery is
    INCLUDE_AND when
        acceptable_road_conditions
        acceptable_intersection_conditions
```

[Code 26](#code-example-defining-sub-trees) comprises:

* The modules defined based on the taxonomy subtrees of weather and scenery.
* The main `passenger_pickup` use case module is decomposed into the taxonomy-based subtree modules of `acceptable_weather` and `supported_scenery`.
* A top-level `INCLUDE_AND` section collates all the components of the cartesian product `supported_scenery`.
  The section is further decomposed into the taxonomy-based subtree modules of `acceptable_road_conditions` and `acceptable_intersection_conditions`.

The semantics of this decomposition example is a simple `AND` of the entire tree.
More complex decompositions can use an `AND-OR` tree of conditions.

The semantic interpretation of [Code 26](#code-example-defining-sub-trees) is as follows:

A situation is included in the ODD:

* If the lighting, rainfall and wind falls within the acceptable ranges in the `INCLUDE_AND` section in `module acceptable_weather`.
* If the road and intersection conditions qualify as acceptable in the `INCLUDE_AND` section in `module supported_scenery`.

### 6.1.9.4 Conditional include and exclude

In many cases, the inclusion criteria should be linked to conditions.
For example, an ODD could specify that the speed on rural roads can only be greater than 70 km/h if the lane markings are solid.
Otherwise, the speed shall be less than 70 km/h.

The challenge is that the speed limit depends on the lane type.
[Code 27](#code-example-disjunctive-include-or) shows how to correctly model this use case by using a disjunctive `INCLUDE_OR` condition for different lane markers:

Code 27. Example disjunctive INCLUDE\_OR (free-form notation)

```
ODD_sample_v1.01.23 is
    INCLUDE_AND when
        ucm_rural_capabilities is true

ucm_rural_capabilities is
    INCLUDE_AND when
        road_type equals rural
        OR
            lane_solid_speed_limit is true
            lane_all_speed_limit is true

lane_solid_speed_limit is
    INCLUDE_AND when
        lane_marker equals solid
        speed_allowed is greater than 70 km/h

lane_all_speed_limit is
    INCLUDE_AND when
        speed_allowed is less than 70 km/h
```

[Code 27](#code-example-disjunctive-include-or) illustrates:

* The `ucm_` prefix indicates that this module is intended to scope a use case (use case module).
* The `ucm_rural_capabilities` module includes rural roads only when specific lane conditions are satisfied that are defined by other modules.
* It is sufficient for one of the two specific lane conditions to be satisfied for inclusion to occur:  
  Either `lane_solid_speed_limit` or `lane_all_speed_limit` are satisfied.
* The `lane_solid_speed_limit` is satisfied for high-speed situations, when `lane_marker equals solid`.
* The `lane_all_speed_limit` is satisfied for low-speed situations regardless of the `lane_marker`.

This pattern can be applied for exclusion sections as well.

### 6.1.9.5 Shared include and exclude sub-condition

An interesting challenge is modeling capabilities with specific shared sub-conditions.
The following examples illustrate this challenge:

* [Code 28](#code-example-1-highway-conditions) shows which highways the ADS can handle:

Code 28. Example 1 highway conditions (free-form notation)

```
road_type equals motorway
marker_type equals solid or broken
number_of_lanes is greater than 4
road_marking_color equals white
max_speed is less than 130 km/h
```

* [Code 29](#code-example-2-highway-conditions) shows which highways the ADS can also handle:

Code 29. Example 2 highway conditions (free-form notation)

```
road_type equals motorway
marker_type equals solid or broken
sign equals construction_zone
road_marking_color equals yellow
number_of_lanes is less than 2
max_speed is less than 80 km/h
```

* The ADS cannot handle highways with construction sites over 80 km/h

[Code 30](#code-example-shared-conditions) shows which elements the two conditions share:

Code 30. Example shared conditions (free-form notation)

```
road_type
marker_type
```

[Code 31](#code-example-different-conditions-1) and [Code 32](#code-example-different-conditions-2) show which elements the two conditions do NOT share:

Code 31. Example different conditions — condition #1 (free-form notation)

```
road_marking_color equals white
number_of_lanes is greater than 4
max_speed is less than 130 km/h
```

Code 32. Example different conditions — condition #2 (free-form notation)

```
sign equals construction_zone
road_marking_color equals yellow
number_of_lanes is less than 2
max_speed is greater than 80 km/h
```

The pattern to support this use case is as follows:

* Define a top-level module with an `INCLUDE_AND`.
* Specify the shared condition in the `INCLUDE_AND` section.
  This section shall not cover non-shared conditions.
* Add an `OR` sub-section that specifies the non-shared components.
* Specify the overall exclusion in the top-level `EXCLUDE_AND` section.

[Code 33](#code-example-shared-sub-conditions) shows how this pattern can be specified:

Code 33. Example shared sub-conditions (free-form notation)

```
combined_module is
    INCLUDE_AND when
        shared_elements is true
        OR
            non_shared_elements_1 is true
            non_shared_elements_2 is true
    EXCLUDE_AND when
        sign equals construction_zone
        max_speed is greater than 80 km/h

shared_elements is
    INCLUDE_AND when
        road_type equals motorway
        marker_type equals solid or broken

non_shared_elements_1 is
    INCLUDE_AND when
        road_marking_color equals white
        number_of_lanes is greater than 4
        max_speed is less than 130 km/h

non_shared_elements_2 is
    INCLUDE_AND when
        road_marking_color equals yellow
        sign in construction_zone
        number_of_lanes is less than 2
        max_speed is greater than 80 km/h
```

### 6.1.9.6 Extensible label disjunction

It is important that a collection of modules can be extended to include or exclude additional situations without explicitly changing the already defined conditions.
Such a capability is unlocked by the extensible label disjunction pattern (that is an OR operation).
Consider defining a list of hazardous environment conditions.
Initially, the list of conditions is limited to one point.
For example, the raindrops are too large and reduce the effectiveness of the camera systems to an unacceptable level.
Over time, additional hazardous conditions are added, for example icy road surfaces.

[Code 34](#code-example-extensible-label-disjunction) shows how inclusion and exclusion conditions can be added without the need to modify previously developed modules:

Code 34. Example extensible label disjunction (free-form notation)

```
passenger_pickup is
    INCLUDE_AND when
        supported_pickup_locations is true
        ...
    EXCLUDE_OR when
        hazardous_conditions is true

pickup_locations_group1 is
    LABEL is supported_pickup_locations
    INCLUDE_AND when
        street_section in
            main_st_sec1
            main_st_sec2

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
        rain_rate equals heavy_rain
        ...

icy_road_conditions is
    LABEL is hazardous_conditions
    INCLUDE_AND when
        road_surface_condition equals black_ice
        ...
```

The semantic interpretation of [Code 34](#code-example-extensible-label-disjunction) is as follows:

* A COD/OD is included in the ODD if it fulfills the `supported_pickup_locations` but not the `hazardous_conditions`.

The key benefit of this pattern in the context of [Code 34](#code-example-extensible-label-disjunction) is as follows:

* The label `supported_pickup_locations` evaluates to `true` whenever either module `pickup_locations_group1` evaluates to `true`, or the module `pickup_locations_group2` evaluates to `true`.  
  Additional modules can be added to satisfy the label `supported_pickup_locations` without modifying the existing modules.
* The label `hazardous_conditions` evaluates to `true` whenever either module `too_much_rain` evaluates to `true`, or the module `icy_road_conditions` evaluates to `true`.  
  Additional modules can be added to satisfy the label `hazardous_conditions` without modifying the existing modules.

For more information on label semantics see [Section 6.4.3.4, "Label semantics"](06_04_openodd_modules.html#sec-concept-modules-label_semantics).

### 6.1.9.7 Implicit include

In many cases it is useful not to list all included conditions explicitly.
In other words, if some elements are excluded all other elements are implicitly included.

As an example, consider specifying that all rain types are acceptable, except `toroidal_rain`.
[Code 35](#code-example-implicit-include) shows how it is characterized as an unsupported combination of rain and wind and how it can be described:

Code 35. Example implicit include (free-form notation)

```
acceptable_weather is
    EXCLUDE_OR when
        rain_type equals toroidal_rain
        ...
```

[Code 35](#code-example-implicit-include) illustrates:

* `EXCLUDE` is used to specify a few excluded items, thereby implicitly including all other items.
* The only `rain_type` excluded is `toroidal_rain`, whereas all other rain types are included.

The semantic interpretation of [Code 35](#code-example-implicit-include) is as follows:

* A situation is included whenever it either does not specify any type of rain, or when the `rain_type` specified is different from `toroidal_rain`.

### 6.1.9.8 Implicit exclude

In many cases it is useful not to list all excluded conditions explicitly.
In other words, if some elements are included all other elements are implicitly excluded.

As an example, consider specifying that no-rain is acceptable but all other rain levels are excluded.
[Code 36](#code-example-implicit-exclude) shows how an implicit exclude can be described:

Code 36. Example implicit exclude (free-form notation)

```
acceptable_weather is
    INCLUDE_OR when
        rain_level equals no_rain
        ...
```

[Code 36](#code-example-implicit-exclude) illustrates:

* `INCLUDE` is used specifying a few included items, thereby implicitly excluding all other items.
* The only `rain_level` included is `no_rain`, whereas all other rain levels are excluded.

The semantic interpretation of [Code 36](#code-example-implicit-exclude) is as follows:

* A situation is included by this module if the specified `rain_level` is exactly `no_rain`.

### 6.1.9.9 Negated module

It is useful to have modules that represent reusable exclusions.
As an example, consider specifying an exclusion for bad weather.
[Code 37](#code-example-negated-module) shows how this can be described by using an unprotected module:

Code 37. Example negated module (free-form notation)

```
my_use_case_module is
    INCLUDE_OR when
        ...
    EXCLUDE_OR when
        bad_weather is true

bad_weather is
    INCLUDE_OR when
        rain_level equals heavy_rain
        rain_type equals toroidal_rain
        wind_speed is greater than or equal to 5 km/h
        fog_severity_type is greater than or equal to dense_fog
        ...
```

[Code 37](#code-example-negated-module) illustrates:

* The reusable negated module `bad_weather` specifies a number of bad weather conditions, one of which is sufficient to exclude a situation from the ODD.
* The host module `my_use_case_module` uses the reusable `bad_weather` in the list of exclusions.

The semantic interpretation of [Code 37](#code-example-negated-module) is as follows:

* The reusable negated module `bad_weather` evaluates to `true` if at least one of the conditions it specifies are `true`.
* The host module `my_use_case_module` evaluates to `true` if the `bad_weather` module evaluates to `false`.  
  This means that all conditions specified in the negated module `bad_weather` have to be not satisfied for the module `my_use_case_module` to accept a situation.

### 6.1.9.10 Protected boundaries

It is important to provide top-level scope boundary conditions that cannot be overwritten by extending conditions in referenced modules.

[Code 38](#code-example-protected-boundaries) shows how this can be done by using an unprotected module:

Code 38. Example protected boundaries (free-form notation)

```
ODD_sample_v1.01.23 is
    INCLUDE_OR when
        city_street_driving is true
        ...
```

It is possible that users add rules extending the situations that are accepted by the `city_street_driving` module.
This is done by enlarging the scope of an `INCLUDE_OR` section in that module.
To prevent such an accident, an `EXCLUDE` section can be added to the ODD root module.
The module acts as a “protective guardrail” preventing scope expansion.

[Code 39](#code-example-extending-rules) shows how to protect against undesired scope increases:

Code 39. Example extending rules (free-form notation)

```
ODD_sample_v1.01.23 is
    INCLUDE_OR when
        city_street_driving is true
    EXCLUDE_OR when
        not_hamburg is true

not_hamburg is
    INCLUDE_OR when
        city equals hamburg
```

[Code 39](#code-example-extending-rules) illustrates:

* The root module for ODD `sample_v1.01.23` uses an `EXCLUDE_OR` to specify the guardrails.
* The guardrail module `not_hamburg` is a “negated module” that is intended to prevent an expansion of the `city_street_driving` from including.
* Even if the `city_street_driving` situation is accepted, for example in London, the ODD `sample_v1.01.23` will only accept situations within Hamburg.

### 6.1.9.11 Conflicting concept decomposition

#### 6.1.9.11.1 General information

Conflicting concepts often arise when evolving the ODD modules.
[Code 40](#code-example-conflicting-concepts) shows how to include motorways in support for a highway pilot for version 1.0.
The module specifies the `road_type` as `motorway` and the `road_marking_color` as `white`:

Code 40. Example conflicting concepts (free-form notation)

```
version 1.0 is
   sample_v1.01.23 is
      INCLUDE_OR when
            highway_pilot is true

    highway_pilot is
        INCLUDE_AND when
            highway_pilot_scenery is true

    highway_pilot_scenery is
        INCLUDE_AND when
            road_type equals motorway
            road_marking_color equals white
```

[Code 41](#code-example-adding-considerations) shows how to add construction zone considerations to the highway use case:

Code 41. Example adding considerations (free-form notation)

```
version 2.0 is
    sample_v1.02.04 is
        INCLUDE_OR when
            highway_pilot is true

    highway_pilot is
        INCLUDE_AND when
            highway_pilot_scenery is true
            highway_pilot_construction_site is true

    highway_pilot_scenery is
        INCLUDE_AND when
            road_type equals motorway
            road_marking_color equals white

    highway_pilot_construction_site is
        INCLUDE_AND when
            road_type equals motorway
            road_marking_color equals yellow
```

The unintended outcome for a COD, in which the `road_type` is `motorway` and the `road_marking_color` is `yellow`, is challenging.
The expected result is that the ADS is inside the ODD when driving on a white highway.
However, the inference suggests the opposite:

* For COD with `road_type equals motorway` and `road_marking_color equals white` the `highway_pilot_scenery` is `true` but `highway_pilot_construction_site` is `false`.
* For COD with `road_type equals motorway` and `road_marking_color equals yellow` the `highway_pilot_construction_site` is `true` but the `highway_pilot_scenery` is `false`.

The root cause of this problem is that the `road_marking_color` is a shared attribute with conflicting values.

When new modules are added with attributes that conflict with existing modules, the rules shall be refactored to avoid shared attributes with conflicting values.

There are two possible solutions:

* Option a:
  Change the conflicting condition in the newly added module to use other unique markers for the situation.
* Option b:
  Add new modules with shared attributes, but restructure the use case module to use an `OR`.

#### 6.1.9.11.2 Option a: Use unique markers

[Code 42](#code-example-change-conflicting-conditions) shows how to replace the `road_marking_color` with `road_signs` or other construction site indicators in the new `module_motorway_construction_site` module:

Code 42. Example unique markers (free-form notation)

```
module_motorway_construction_site is
    INCLUDE_AND when
        road_type equals motorway
        road_signs equals construction_signs    # modified from the original
```

#### 6.1.9.11.3 Option b: Restructure use case module

[Code 43](#code-example-refactor-conflicting-conditions) shows how to restructure the use case module by extending the UCM to reference a specific motorway construction site:

Code 43. Example restructured use case module (free-form notation)

```
sample_v1.02.04 is
    INCLUDE_AND when
        ucm_highway_pilot is true

ucm_highway_pilot is
    INCLUDE_OR when
        module_motorway is true
        module_motorway_construction_site is true    # new reference

module_motorway is
    INCLUDE_AND when
        road_type equals motorway
        road_marking_color equals white

module_motorway_construction_site is                 # only used for highway pilot
    INCLUDE_AND when
        road_type equals motorway
        module_generic_construction_site is true

module_generic_construction_site:                    # used for other use cases
    INCLUDE_AND
        road_marking_color equals yellow
        road_signs equals construction_signs
```

The following steps are recommended for refactoring from option a to option b:

1. Identify the generic elements `EXCLUDE` part of the construction site module of a module that is not part of the use case.
2. Build the use case module by combining the defined modules.
   The defined modules build the use case with a logical `OR` connection and exclude the elements that are not part of the use case.

### 6.1.9.12 Risk modeling with categorical numeric aggregations

It is often necessary to quantify the risk to determine the safe driving conditions.
For example, in a bad weather environment it may be useful to indicate that heavy rain for more than 1 hour is risky.
In contrast, heavy rain for 5 min is not.

[Code 44](#code-example-risk-modeling) shows an example of risk modeling using numeric aggregation:

Code 44. Example risk modeling (free-form notation)

```
ODD_sample_v1.02.04 is
    INCLUDE_AND when
        ucm_acceptable_rainfall is true

ucm_acceptable_rainfall is
    INCLUDE_OR when
        rain_level is less than or equal to heavy_rain
        heavy_rain.duration is less than 1 hour
    EXCLUDE_OR when
        flood.water_depth is greater than 20 cm
```

[Code 44](#code-example-risk-modeling) illustrates:

* The ODD includes the single use case module (ucm) `ucm_acceptable_rainfall`.
* The module `ucm_acceptable_rainfall` is satisfied if at least one of the two conditions is `true`:

  + The `rain_level` is less than `heavy_rain`.
    Therefore, it is either `no_rain`, `light_rain`, or `moderate_rain`.
  + The `heavy_rain.duration` is less than one hour.
* In addition, this module evaluates to `false` during a flood if `flood.water_depth` is more than 20 cm.

This approach enables the development of rules that are consistent with specific testable conditions.

### 6.1.9.13 Modeling uncertainty

Quantifying uncertainty is necessary to determine safe driving conditions.
For example, it is essential to specify that the highway pilot is safe only when cyclists are unlikely to be present.
Roads where cyclists frequently appear are considered to be too risky.

[Code 45](#code-example-modeling-uncertainty) shows an example of such uncertainty modeling using the `occurrence_rate` aggregation:

Code 45. Example modeling uncertainty (free-form notation)

```
ODD_sample_v1.02.04 is
    INCLUDE_AND when
        ucm_acceptable_risk is true

ucm_acceptable_risk is
    INCLUDE_OR when
        rain_level is less than or equal to heavy_rain
        heavy_rain.duration is less than 1 hour
    EXCLUDE_OR when
        cyclist.occurrence_rate is greater than 1 per day
        pedestrian.occurrence_rate is greater than 2 per hour
```

[Code 45](#code-example-modeling-uncertainty) illustrates:

* The ODD includes the single use case module (ucm) `ucm_acceptable_risk`.
* The module `ucm_acceptable_risk` is satisfied when at least one of the two conditions is `true`:

  + The `rain_level` is less than `heavy_rain`.
    Therefore, it is either `no_rain`, `light_rain`, or `moderate_rain`.
  + The `heavy_rain` duration is less than one hour.
* In addition, this module evaluates to `false` if either:

  + The `cyclist.occurrence_rate` is greater than one per day.
  + The `pedestrian.occurrence_rate` is greater than two per hour.

This approach enables the development of rules that are consistent with specific testable conditions.

## 6.1.10 Internationalization (multi-lingual support)

### 6.1.10.1 LangString specification

Since ADAS/ADS functions of a vehicle will be usually used in more than one country, it is evident that ODDs shall support multiple natural languages in order to be able to create artifacts containing names, descriptions, and comments in various natural languages, for example, "bad weather", "schlechtes Wetter", "mauvais temps".

The ASAM OpenODD model introduced in this document implements this by means of the following modeling constructs:

* A data type `LangString` associating a text (string) to an ISO 639 [[10](../bibliography.html#bib-iso639)], for example, ["bad weather", "en"]
* Classes that need multi-lingual support have fields of data type `LangString`.
* Since more than one language should be supported, those fields are multi-valued.

For instance, a taxonomy concept instance defined in an ODD and multi-lingual support might look like follows:

An instance of class `TaxonomyConcept`

Figure 9. An instance of class `TaxonomyConcept`

[Figure 9](#fig-concept-overview-internationalization-example) shows an instance of class `TaxonomyConcept` with a name and a description in three different natural languages.

Note that the given model neither specifies which languages shall be supported nor does it require a specific sequence of languages, but it shall include at least English.

### 6.1.10.2 Class LangString

Basic information
:   Table 16. Basic information of class LangString


    |  |  |
    | --- | --- |
    | **Instantiable** | no |

Parameters
:   Table 17. Class LangString


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | value | String | yes | The language-dependent text string, like a name or a description. |
    | intlCode | String | yes | A string denoting an international ISO 639 language code, for example, EN, DE, FR, ES (not case sensitive) |