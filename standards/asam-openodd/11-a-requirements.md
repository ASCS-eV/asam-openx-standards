# ASAM OpenODD® v1.0.0 — Annex E: (informative) Requirements

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_a_requirements.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex E: (informative) Requirements

## E.1 Requirements context

Industry has various expectations for language to describe ODD.
Stakeholders interested in ASAM OpenODD® come from many domains (OEMs, regulators, tool vendors, simulation, safety and many others) and have different needs.
The requirements specification given in this annex is the result of analysis and elicitation process and addresses most basic and common expectations toward ASAM OpenODD® capabilities.

The purpose of this document is to provide the reader with a summary of requirements analysis and elicitation process for ASAM OpenODD®.

## E.2 Method for Requirements Analysis

This section describes briefly the requirements analysis and elicitation process.
The starting point of the requirements analysis for ASAM OpenODD® is based on the preceding ASAM OpenODD® concept project.
In scope of the project proposal, an initial stakeholder analysis was performed and formulation of preliminary requirements by user stories. The following stakeholders were considered:

* Business Developer
* Data Annotation Engineer
* Data Scientist
* Development Engineer
* Environmental Subject Matter Expert
* Infrastructure Operator
* ODD Specification Author
* Product Manager
* Regulator
* Requirement Engineer
* Safety Engineer
* Test Engineer
* Tool Developer

|  |  |
| --- | --- |
|  | During the development of the standard, the requirements were defined with the intention that the standard would include a model, one or more languages, and a database representation. This approach was overhauled and refined. ASAM OpenODD® comprises the ASAM OpenODD® model (the technology-independent core) and multiple mapping references, including the tabular format, ASAM OpenSCENARIO® DSL (language), and YAML (language). In the requirements, the term "model" refers specifically to the ASAM OpenODD® model. When requirements mention "language" they apply to the mapping references that are languages. Similarly, when the "tabular" is referenced in a requirement, they apply to the mapping references that are tabular like. |

During several discussions and workshops, a refined set of user stories has been created and agreed upon.
Based on these user stories together with the initial set of high-level requirements from the preceding ASAM OpenODD® concept project, the initial set of needs and required capabilities were derived and further decomposed, that have led to the final set of requirements.
The final set of requirements has been divided into two parts.
First, the requirements specification that shall be considered in ASAM OpenODD®.
The specification entails a categorization, which parts of the standard are affected by the requirement: model, language, tabular.
Second, there have been proposed requirements that were considered to out-of-scope of this version, but could be part of future versions of ASAM OpenODD®.
Both of these lists of requirements are described in the following sections.

## E.3 Requirements Specification

### E.3.1 Combined Requirements

Table 168. Complete requirements specification


| ID | Category | Requirement text |
| --- | --- | --- |
| oODD\_REQ\_1.1 | Purpose | ASAM OpenODD® (model, language, tabular) shall provide capabilities to describe:  * Operational Domain (OD) * Current Operational Domain (COD) * Target Operational Domain (TOD) * Operational Design Domain (ODD) |
| oODD\_REQ\_1.2 | Purpose | ASAM OpenODD® (model, language, tabular) shall implement "OD description statement" for description of Operational Domain and Current Operational Domain. |
| oODD\_REQ\_1.3 | Purpose | ASAM OpenODD® (model, language, tabular) shall implement "ODD description statement" for description of Target Operational Domain and Operational Design Domain. |
| oODD\_REQ\_2.1 | Taxonomy | Description of COD/OD/TOD/ODD (model, language, tabular) shall be based on at least one taxonomy. |
| oODD\_REQ\_2.2 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall provide capability to reference multiple taxonomies and their elements individually. |
| oODD\_REQ\_2.3 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall provide semantics for referencing hierarchical taxonomy concepts (on any level of hierarchy). |
| oODD\_REQ\_2.4 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall support usage of taxonomy hierarchy in "OD description statements" and "ODD description statements". |
| oODD\_REQ\_2.5 | Taxonomy | At least one taxonomy concept shall be used in each "OD description statement" or "ODD description statement" (model, language, tabular). |
| oODD\_REQ\_3.1.1 | Machine readability | ASAM OpenODD® (language) shall have syntax defined. |
| oODD\_REQ\_3.1.2 | Machine readability | ASAM OpenODD® (language) shall have semantics defined. |
| oODD\_REQ\_3.2 | Machine readability | ASAM OpenODD® (language) syntax shall be of textual format. |
| oODD\_REQ\_3.3 | Machine readability | ASAM OpenODD® (language) semantics shall be unambiguous. |
| oODD\_REQ\_3.4 | Machine readability | ASAM OpenODD® (model, language, tabular) syntax shall include commenting feature allowing marking parts of COD/OD/TOD/ODD descriptions which are excluded from semantic interpretation. |
| oODD\_REQ\_3.4.1 | Machine readability | ASAM OpenODD® (model, language, tabular) shall provide syntax of commenting feature allowing relating it to:  * the overall COD/OD/TOD/ODD definition * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_3.5 | Machine readability | ASAM OpenODD® (model, language, tabular) shall provide formal grammar supporting querying of COD/OD/TOD/ODD description. |
| oODD\_REQ\_4.1 | Composability | ASAM OpenODD® (model, language, tabular) shall provide capability to encapsulate full or partial definitions of COD/OD/TOD/ODD into named entities. |
| oODD\_REQ\_4.2 | Composability | ASAM OpenODD® (model, language, tabular) shall provide capability to include encapsulated COD/OD/TOD/ODD definitions as named entities into given COD/OD/TOD/ODD definition. |
| oODD\_REQ\_4.3 | Composability | ASAM OpenODD® (language) semantics of inclusion mechanism of encapsulated COD/OD/TOD/ODD definitions shall be unambiguous. |
| oODD\_REQ\_5.1 | Parametrization and templating | ASAM OpenODD® (language, tabular, [optional: model]) shall provide capability to define named parameters which can be resolved into concrete value. |
| oODD\_REQ\_5.2 | Parametrization and templating | ASAM OpenODD® (language, tabular, [optional: model]) shall provide capability to use defined parameters in:  * another parameter definition * conditional statements * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_6.1 | Conditional statement | ASAM OpenODD® (language, tabular, model) shall provide capabilities to express conditions under which given "ODD description statement" is interpreted semantically. |
| oODD\_REQ\_7.1 | Binary boundary | ASAM OpenODD® (language, model, tabular) shall ensure "ODD description statement" can be resolved into boolean value (true or false). |
| oODD\_REQ\_8.1 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall provide set of data types applicable in COD/OD/TOD/ODD definitions. |
| oODD\_REQ\_8.1.1 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall provide methodology for using external data types in referenced taxonomy concepts within COD/OD/TOD/ODD definitions. |
| oODD\_REQ\_8.1.2 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce assignment of data type for every referenced taxonomy concepts. |
| oODD\_REQ\_8.1.3 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce assignment of data type for every defined parameter. |
| oODD\_REQ\_8.3 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall conform to ASAM Unit Handling standard v. 1.0.0. |
| oODD\_REQ\_8.2 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce unit and unit type (as per ASAM Unit Handling) being assigned to every taxonomy concept or defined parameter. |
| oODD\_REQ\_9.0 | Expressions and operators | ASAM OpenODD® (language, tabular) syntax shall conform to ASAM AE Expressions standard v. 1.0.1. |
| oODD\_REQ\_9.1 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define mathematical operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.2 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following mathematical operators expressing semantics of:  * addition * subtraction * multiplication * division |
| oODD\_REQ\_9.3 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define relation operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.4 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following relation operators expressing semantics of:  * equals * not equal * greater than * greater than or equal * less than * less than or equal |
| oODD\_REQ\_9.5 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define logical operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.6 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following logical operators expressing semantics of:  * negation * logical conjunction * logical disjunction |
| oODD\_REQ\_9.7 | Expressions and operators | ASAM OpenODD® (language) syntax and semantics shall provide means of grouping logical expressions. |
| oODD\_REQ\_9.8 | Expressions and operators | In ASAM OpenODD® (language) an grouped logical expression shall be possible to use in another logical expression as one of operands. |
| oODD\_REQ\_9.9 | Expressions and operators | ASAM OpenODD® (language) shall define ODD boundary operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.10 | Expressions and operators | ASAM OpenODD® (language, tabular, model) shall implement at least following ODD boundary operators expressing semantics of:  * inclusion * exclusion |
| oODD\_REQ\_10.1 | Global mode | ASAM OpenODD® (model, language, tabular) shall provide means to handle taxonomy concepts not referenced by any "ODD description statements" in ODD description with at least following semantics: inclusion, exclusion, indifference. |
| oODD\_REQ\_11.1 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of referenced taxonomies and their elements. |
| oODD\_REQ\_11.2 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of "OD description statements" used in COD or OD definition. |
| oODD\_REQ\_11.3 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of "ODD description statements" used in TOD or ODD definition. |
| oODD\_REQ\_12.2 | Custom user data and labeling | ASAM OpenODD® (model, language, tabular) syntax shall provide capability to mark parts of COD/OD/TOD/ODD description dedicated for custom user data and excluded from semantic interpretation. |
| oODD\_REQ\_12.1 | Custom user data and labeling | ASAM OpenODD® (model, language, tabular) syntax shall provide capability to relate custom user data to:  * the overall COD/OD/TOD/ODD definition * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_13.1 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall provide a mechanism to state time and location for:  * the overall COD/OD definition * OD description statements |
| oODD\_REQ\_13.2 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall implement at least following ways to express time:  * point in time (timestamp) * timespan |
| oODD\_REQ\_13.3 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall implement at least following ways to express location:  * single point * area |

### E.3.2 Model Requirements

Subset of the requirements that are relevant for the ASAM OpenODD® Model.

Table 169. model requirements specification


| ID | Category | Requirement text |
| --- | --- | --- |
| oODD\_REQ\_1.1 | Purpose | ASAM OpenODD® (model, language, tabular) shall provide capabilities to describe:  * Operational Domain (OD) * Current Operational Domain (COD) * Target Operational Domain (TOD) * Operational Design Domain (ODD) |
| oODD\_REQ\_1.2 | Purpose | ASAM OpenODD® (model, language, tabular) shall implement "OD description statement" for description of Operational Domain and Current Operational Domain. |
| oODD\_REQ\_1.3 | Purpose | ASAM OpenODD® (model, language, tabular) shall implement "ODD description statement" for description of Target Operational Domain and Operational Design Domain. |
| oODD\_REQ\_2.1 | Taxonomy | Description of COD/OD/TOD/ODD (model, language, tabular) shall be based on at least one taxonomy. |
| oODD\_REQ\_2.2 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall provide capability to reference multiple taxonomies and their elements individually. |
| oODD\_REQ\_2.3 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall provide semantics for referencing hierarchical taxonomy concepts (on any level of hierarchy). |
| oODD\_REQ\_2.4 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall support usage of taxonomy hierarchy in "OD description statements" and "ODD description statements". |
| oODD\_REQ\_2.5 | Taxonomy | At least one taxonomy concept shall be used in each "OD description statement" or "ODD description statement" (model, language, tabular). |
| oODD\_REQ\_3.4 | Machine readability | ASAM OpenODD® (model, language, tabular) syntax shall include commenting feature allowing marking parts of COD/OD/TOD/ODD descriptions which are excluded from semantic interpretation. |
| oODD\_REQ\_3.4.1 | Machine readability | ASAM OpenODD® (model, language, tabular) shall provide syntax of commenting feature allowing relating it to:  * the overall COD/OD/TOD/ODD definition * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_3.5 | Machine readability | ASAM OpenODD® (model, language, tabular) shall provide formal grammar supporting querying of COD/OD/TOD/ODD description. |
| oODD\_REQ\_4.1 | Composability | ASAM OpenODD® (model, language, tabular) shall provide capability to encapsulate full or partial definitions of COD/OD/TOD/ODD into named entities. |
| oODD\_REQ\_4.2 | Composability | ASAM OpenODD® (model, language, tabular) shall provide capability to include encapsulated COD/OD/TOD/ODD definitions as named entities into given COD/OD/TOD/ODD definition. |
| oODD\_REQ\_5.1 | Parametrization and templating | ASAM OpenODD® (language, tabular, [optional: model]) shall provide capability to define named parameters which can be resolved into concrete value. |
| oODD\_REQ\_5.2 | Parametrization and templating | ASAM OpenODD® (language, tabular, [optional: model]) shall provide capability to use defined parameters in:  * another parameter definition * conditional statements * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_6.1 | Conditional statement | ASAM OpenODD® (model, language, tabular) shall provide capabilities to express conditions under which given "ODD description statement" is interpreted semantically. |
| oODD\_REQ\_7.1 | Binary boundary | ASAM OpenODD® (model, language, tabular) shall ensure "ODD description statement" can be resolved into boolean value (true or false). |
| oODD\_REQ\_8.1 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall provide set of data types applicable in COD/OD/TOD/ODD definitions. |
| oODD\_REQ\_8.1.1 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall provide methodology for using external data types in referenced taxonomy concepts within COD/OD/TOD/ODD definitions. |
| oODD\_REQ\_8.1.2 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce assignment of data type for every referenced taxonomy concepts. |
| oODD\_REQ\_8.1.3 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce assignment of data type for every defined parameter. |
| oODD\_REQ\_8.3 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall conform to ASAM Unit Handling standard v. 1.0.0. |
| oODD\_REQ\_8.2 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce unit and unit type (as per ASAM Unit Handling) being assigned to every taxonomy concept or defined parameter. |
| oODD\_REQ\_9.10 | Expressions and operators | ASAM OpenODD® (model, language, tabular) shall implement at least following ODD boundary operators expressing semantics of:  * inclusion * exclusion |
| oODD\_REQ\_10.1 | Global mode | ASAM OpenODD® (model, language, tabular) shall provide means to handle taxonomy concepts not referenced by any "ODD description statements" in ODD description with at least following semantics: inclusion, exclusion, indifference. |
| oODD\_REQ\_11.1 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of referenced taxonomies and their elements. |
| oODD\_REQ\_11.2 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of "OD description statements" used in COD or OD definition. |
| oODD\_REQ\_11.3 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of "ODD description statements" used in TOD or ODD definition. |
| oODD\_REQ\_12.2 | Custom user data and labeling | ASAM OpenODD® (model, language, tabular) syntax shall provide capability to mark parts of COD/OD/TOD/ODD description dedicated for custom user data and excluded from semantic interpretation. |
| oODD\_REQ\_12.1 | Custom user data and labeling | ASAM OpenODD® (model, language, tabular) syntax shall provide capability to relate custom user data to:  * the overall COD/OD/TOD/ODD definition * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_13.1 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall provide a mechanism to state time and location for:  * the overall COD/OD definition * OD description statements |
| oODD\_REQ\_13.2 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall implement at least following ways to express time:  * point in time (timestamp) * timespan |
| oODD\_REQ\_13.3 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall implement at least following ways to express location:  * single point * area |

### E.3.3 Language requirements

Subset of the requirements that are relevant for the mapping references of ASAM OpenODD® which are languages.

Table 170. Language requirements specification


| ID | Category | Requirement text |
| --- | --- | --- |
| oODD\_REQ\_1.1 | Purpose | ASAM OpenODD® (model, language, tabular) shall provide capabilities to describe:  * Operational Domain (OD) * Current Operational Domain (COD) * Target Operational Domain (TOD) * Operational Design Domain (ODD) |
| oODD\_REQ\_1.2 | Purpose | ASAM OpenODD® (model, language, tabular) shall implement "OD description statement" for description of Operational Domain and Current Operational Domain. |
| oODD\_REQ\_1.3 | Purpose | ASAM OpenODD® (model, language, tabular) shall implement "ODD description statement" for description of Target Operational Domain and Operational Design Domain. |
| oODD\_REQ\_2.1 | Taxonomy | Description of COD/OD/TOD/ODD (model, language, tabular) shall be based on at least one taxonomy. |
| oODD\_REQ\_2.2 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall provide capability to reference multiple taxonomies and their elements individually. |
| oODD\_REQ\_2.3 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall provide semantics for referencing hierarchical taxonomy concepts (on any level of hierarchy). |
| oODD\_REQ\_2.4 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall support usage of taxonomy hierarchy in "OD description statements" and "ODD description statements". |
| oODD\_REQ\_2.5 | Taxonomy | At least one taxonomy concept shall be used in each "OD description statement" or "ODD description statement" (model, language, tabular). |
| oODD\_REQ\_3.1.1 | Machine readability | ASAM OpenODD® (language) shall have syntax defined. |
| oODD\_REQ\_3.1.2 | Machine readability | ASAM OpenODD® (language) shall have semantics defined. |
| oODD\_REQ\_3.2 | Machine readability | ASAM OpenODD® (language) syntax shall be of textual format. |
| oODD\_REQ\_3.3 | Machine readability | ASAM OpenODD® (language) semantics shall be unambiguous. |
| oODD\_REQ\_3.4 | Machine readability | ASAM OpenODD® (model, language, tabular) syntax shall include commenting feature allowing marking parts of COD/OD/TOD/ODD descriptions which are excluded from semantic interpretation. |
| oODD\_REQ\_3.4.1 | Machine readability | ASAM OpenODD® (model, language, tabular) shall provide syntax of commenting feature allowing relating it to:  * the overall COD/OD/TOD/ODD definition * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_3.5 | Machine readability | ASAM OpenODD® (model, language, tabular) shall provide formal grammar supporting querying of COD/OD/TOD/ODD description. |
| oODD\_REQ\_4.1 | Composability | ASAM OpenODD® (model, language, tabular) shall provide capability to encapsulate full or partial definitions of COD/OD/TOD/ODD into named entities. |
| oODD\_REQ\_4.2 | Composability | ASAM OpenODD® (model, language, tabular) shall provide capability to include encapsulated COD/OD/TOD/ODD definitions as named entities into given COD/OD/TOD/ODD definition. |
| oODD\_REQ\_4.3 | Composability | ASAM OpenODD® (language) semantics of inclusion mechanism of encapsulated COD/OD/TOD/ODD definitions shall be unambiguous. |
| oODD\_REQ\_5.1 | Parametrization and templating | ASAM OpenODD® (language, tabular, [optional: model]) shall provide capability to define named parameters which can be resolved into concrete value. |
| oODD\_REQ\_5.2 | Parametrization and templating | ASAM OpenODD® (language, tabular, [optional: model]) shall provide capability to use defined parameters in:  * another parameter definition * conditional statements * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_6.1 | Conditional statement | ASAM OpenODD® (language, tabular, model) shall provide capabilities to express conditions under which given "ODD description statement" is interpreted semantically. |
| oODD\_REQ\_7.1 | Binary boundary | ASAM OpenODD® (language, model, tabular) shall ensure "ODD description statement" can be resolved into boolean value (true or false). |
| oODD\_REQ\_8.1 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall provide set of data types applicable in COD/OD/TOD/ODD definitions. |
| oODD\_REQ\_8.1.1 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall provide methodology for using external data types in referenced taxonomy concepts within COD/OD/TOD/ODD definitions. |
| oODD\_REQ\_8.1.2 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce assignment of data type for every referenced taxonomy concepts. |
| oODD\_REQ\_8.1.3 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce assignment of data type for every defined parameter. |
| oODD\_REQ\_8.3 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall conform to ASAM Unit Handling standard v. 1.0.0. |
| oODD\_REQ\_8.2 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce unit and unit type (as per ASAM Unit Handling) being assigned to every taxonomy concept or defined parameter. |
| oODD\_REQ\_9.0 | Expressions and operators | ASAM OpenODD® (language, tabular) syntax shall conform to ASAM AE Expressions standard v. 1.0.1. |
| oODD\_REQ\_9.1 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define mathematical operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.2 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following mathematical operators expressing semantics of:  * addition * subtraction * multiplication * division |
| oODD\_REQ\_9.3 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define relation operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.4 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following relation operators expressing semantics of:  * equals * not equal * greater than * greater than or equal * less than * less than or equal |
| oODD\_REQ\_9.5 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define logical operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.6 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following logical operators expressing semantics of:  * negation * logical conjunction * logical disjunction |
| oODD\_REQ\_9.7 | Expressions and operators | ASAM OpenODD® (language) syntax and semantics shall provide means of grouping logical expressions. |
| oODD\_REQ\_9.8 | Expressions and operators | In ASAM OpenODD® (language) an grouped logical expression shall be possible to use in another logical expression as one of operands. |
| oODD\_REQ\_9.9 | Expressions and operators | ASAM OpenODD® (language) shall define ODD boundary operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.10 | Expressions and operators | ASAM OpenODD® (language, tabular, model) shall implement at least following ODD boundary operators expressing semantics of:  * inclusion * exclusion |
| oODD\_REQ\_10.1 | Global mode | ASAM OpenODD® (model, language, tabular) shall provide means to handle taxonomy concepts not referenced by any "ODD description statements" in ODD description with at least following semantics: inclusion, exclusion, indifference. |
| oODD\_REQ\_11.1 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of referenced taxonomies and their elements. |
| oODD\_REQ\_11.2 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of "OD description statements" used in COD or OD definition. |
| oODD\_REQ\_11.3 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of "ODD description statements" used in TOD or ODD definition. |
| oODD\_REQ\_12.2 | Custom user data and labeling | ASAM OpenODD® (model, language, tabular) syntax shall provide capability to mark parts of COD/OD/TOD/ODD description dedicated for custom user data and excluded from semantic interpretation. |
| oODD\_REQ\_12.1 | Custom user data and labeling | ASAM OpenODD® (model, language, tabular) syntax shall provide capability to relate custom user data to:  * the overall COD/OD/TOD/ODD definition * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_13.1 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall provide a mechanism to state time and location for:  * the overall COD/OD definition * OD description statements |
| oODD\_REQ\_13.2 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall implement at least following ways to express time:  * point in time (timestamp) * timespan |
| oODD\_REQ\_13.3 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall implement at least following ways to express location:  * single point * area |

### E.3.4 Tabular requirements

Subset of the requirements that are relevant for the mapping references of ASAM OpenODD® which are tabular like.

Table 171. tabular requirements specification


| ID | Category | Requirement text |
| --- | --- | --- |
| oODD\_REQ\_1.1 | Purpose | ASAM OpenODD® (model, language, tabular) shall provide capabilities to describe:  * Operational Domain (OD) * Current Operational Domain (COD) * Target Operational Domain (TOD) * Operational Design Domain (ODD) |
| oODD\_REQ\_1.2 | Purpose | ASAM OpenODD® (model, language, tabular) shall implement "OD description statement" for description of Operational Domain and Current Operational Domain. |
| oODD\_REQ\_1.3 | Purpose | ASAM OpenODD® (model, language, tabular) shall implement "ODD description statement" for description of Target Operational Domain and Operational Design Domain. |
| oODD\_REQ\_2.1 | Taxonomy | Description of COD/OD/TOD/ODD (model, language, tabular) shall be based on at least one taxonomy. |
| oODD\_REQ\_2.2 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall provide capability to reference multiple taxonomies and their elements individually. |
| oODD\_REQ\_2.3 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall provide semantics for referencing hierarchical taxonomy concepts (on any level of hierarchy). |
| oODD\_REQ\_2.4 | Taxonomy | ASAM OpenODD® (model, language, tabular) shall support usage of taxonomy hierarchy in "OD description statements" and "ODD description statements". |
| oODD\_REQ\_2.5 | Taxonomy | At least one taxonomy concept shall be used in each "OD description statement" or "ODD description statement" (model, language, tabular). |
| oODD\_REQ\_3.4 | Machine readability | ASAM OpenODD® (model, language, tabular) syntax shall include commenting feature allowing marking parts of COD/OD/TOD/ODD descriptions which are excluded from semantic interpretation. |
| oODD\_REQ\_3.4.1 | Machine readability | ASAM OpenODD® (model, language, tabular) shall provide syntax of commenting feature allowing relating it to:  * the overall COD/OD/TOD/ODD definition * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_3.5 | Machine readability | ASAM OpenODD® (model, language, tabular) shall provide formal grammar supporting querying of COD/OD/TOD/ODD description. |
| oODD\_REQ\_4.1 | Composability | ASAM OpenODD® (model, language, tabular) shall provide capability to encapsulate full or partial definitions of COD/OD/TOD/ODD into named entities. |
| oODD\_REQ\_4.2 | Composability | ASAM OpenODD® (model, language, tabular) shall provide capability to include encapsulated COD/OD/TOD/ODD definitions as named entities into given COD/OD/TOD/ODD definition. |
| oODD\_REQ\_5.1 | Parametrization and templating | ASAM OpenODD® (language, tabular, [optional: model]) shall provide capability to define named parameters which can be resolved into concrete value. |
| oODD\_REQ\_5.2 | Parametrization and templating | ASAM OpenODD® (language, tabular, [optional: model]) shall provide capability to use defined parameters in:  * another parameter definition * conditional statements * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_6.1 | Conditional statement | ASAM OpenODD® (language, tabular, model) shall provide capabilities to express conditions under which given "ODD description statement" is interpreted semantically. |
| oODD\_REQ\_7.1 | Binary boundary | ASAM OpenODD® (language, model, tabular) shall ensure "ODD description statement" can be resolved into boolean value (true or false). |
| oODD\_REQ\_8.1 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall provide set of data types applicable in COD/OD/TOD/ODD definitions. |
| oODD\_REQ\_8.1.1 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall provide methodology for using external data types in referenced taxonomy concepts within COD/OD/TOD/ODD definitions. |
| oODD\_REQ\_8.1.2 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce assignment of data type for every referenced taxonomy concepts. |
| oODD\_REQ\_8.1.3 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce assignment of data type for every defined parameter. |
| oODD\_REQ\_8.3 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall conform to ASAM Unit Handling standard v. 1.0.0. |
| oODD\_REQ\_8.2 | Datatypes and units | ASAM OpenODD® (model, language, tabular) shall enforce unit and unit type (as per ASAM Unit Handling) being assigned to every taxonomy concept or defined parameter. |
| oODD\_REQ\_9.0 | Expressions and operators | ASAM OpenODD® (language, tabular) syntax shall conform to ASAM AE Expressions standard v. 1.0.1. |
| oODD\_REQ\_9.1 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define mathematical operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.2 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following mathematical operators expressing semantics of:  * addition * subtraction * multiplication * division |
| oODD\_REQ\_9.3 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define relation operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.4 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following relation operators expressing semantics of:  * equals * not equal * greater than * greater than or equal * less than * less than or equal |
| oODD\_REQ\_9.5 | Expressions and operators | ASAM OpenODD® (language, tabular) shall define logical operators, their operands, syntax and semantics. |
| oODD\_REQ\_9.6 | Expressions and operators | ASAM OpenODD® (language, tabular) shall implement at least following logical operators expressing semantics of:  * negation * logical conjunction * logical disjunction |
| oODD\_REQ\_9.10 | Expressions and operators | ASAM OpenODD® (language, tabular, model) shall implement at least following ODD boundary operators expressing semantics of:  * inclusion * exclusion |
| oODD\_REQ\_10.1 | Global mode | ASAM OpenODD® (model, language, tabular) shall provide means to handle taxonomy concepts not referenced by any "ODD description statements" in ODD description with at least following semantics: inclusion, exclusion, indifference. |
| oODD\_REQ\_11.1 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of referenced taxonomies and their elements. |
| oODD\_REQ\_11.2 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of "OD description statements" used in COD or OD definition. |
| oODD\_REQ\_11.3 | Traceability from external systems | ASAM OpenODD® (model, language, tabular) shall provide syntax and semantics for unique identification of "ODD description statements" used in TOD or ODD definition. |
| oODD\_REQ\_12.2 | Custom user data and labeling | ASAM OpenODD® (model, language, tabular) syntax shall provide capability to mark parts of COD/OD/TOD/ODD description dedicated for custom user data and excluded from semantic interpretation. |
| oODD\_REQ\_12.1 | Custom user data and labeling | ASAM OpenODD® (model, language, tabular) syntax shall provide capability to relate custom user data to:  * the overall COD/OD/TOD/ODD definition * "OD description statements" * "ODD description statements" |
| oODD\_REQ\_13.1 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall provide a mechanism to state time and location for:  * the overall COD/OD definition * OD description statements |
| oODD\_REQ\_13.2 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall implement at least following ways to express time:  * point in time (timestamp) * timespan |
| oODD\_REQ\_13.3 | Timestamp and location | ASAM OpenODD® (model, language, tabular) shall implement at least following ways to express location:  * single point * area |

## E.4 Out-of-scope Requirements

This section summarizes the requirements that have been proposed during the elicitation process, but were considered as out-of-scope of ASAM OpenODD® v.1.0.0.
The following table gives a list of these requirements together with a brief description of the rationale. It should be noted that these requirements might be taken into account in future versions of ASAM OpenODD®.

Table 172. List of requirements that are not in ASAM OpenODD® v.1.0.0


| ID | Category | Requirement text |
| --- | --- | --- |
| future\_1 | operators | The language shall define probability operators, their syntax and semantics. |
| Rationale: Handle with taxonomy extensions in v.1.0.0. | | |
| future\_2 | operators | The language shall implement at least following probability operators:  * P@x |
| Rationale: Handle with taxonomy extensions in v.1.0.0. | | |
| future\_3 | external library extensions | The language shall provide capabilities to define external functions realized by external implementations (libraries, scripts, programs?). |
| Rationale: Definitions in v.1.0.0 should be self-contained and not dependent on external entities. | | |
| future\_4 | external library extensions | The language shall enforce definition of external function, its input parameters (with data types) and output result (with datatype). |
| Rationale: Definitions in v.1.0.0 should be self-contained. | | |
| future\_5 | external library extensions | The language shall provide capabilities to use external functions in "OD description statements" and "ODD boundary statements". |
| Rationale: OD description statements and ODD boundary statements in v.1.0.0 should be self-contained. | | |
| future\_6 | external library extensions | The language shall provide capability to define internal taxonomy. |
| Rationale: To maintain a clear separation between taxonomy definition and ODD definition.  Changes in the taxonomy should be done in the taxonomy directly. | | |
| future\_7.1 | spatial and temporal aspects | The language shall be able to express relative positioning or temporal aspects of ODD elements towards the system. |
| Rationale: Handle with taxonomy extensions in v.1.0.0. | | |
| future\_7.2 | spatial and temporal aspects | The language shall be able to express a sequence of events, in which one or more ODD attributes are involved. |
| Rationale: Handle with taxonomy extensions in v.1.0.0. | | |
| future\_8 | Composability | The language shall enable combining/grouping elements in ODD to detail the statements (for OD and COD may be covered in v1.x). |
| Rationale: Handle with taxonomy extensions in v.1.0.0. | | |