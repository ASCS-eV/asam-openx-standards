# ASAM OpenODD® v1.0.0 — §3 Terms and Definitions

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/03_terms_and_definitions/03_terms_and_definitions.html
> **Standard**: ASAM OpenODD® Base Standard 1.0.0 Specification, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2025-05-19

---

## ASAM OpenODD® model

The ASAM OpenODD® model defines an abstract model to describe taxonomies, operational design domains (ODD), operational domains (OD), and current operational domains (COD). ASAM OpenODD® uses UML class diagrams (classes and relationships) as formal specification language for the ASAM OpenODD® model. ASAM OpenODD® model is technology and language independent. ASAM OpenODD® model can be mapped to various technologies and languages for creating concrete models to define taxonomies, ODDs, ODs, and CODs.

## Attribute

Attributes are specific characteristics or properties that are relevant for the description of an operational domain. In the ASAM OpenODD® model, attributes define the fields or elements that make up the structure of the ASAM OpenODD® record. For example, an attribute might represent a field such as 'road_type' within a record.

## Current Operational Domain, COD

Specific set of operating conditions which exists presently in the immediate vicinity of an ADS, including, but not limited to, environmental, geographical, and time-of-day restrictions, and/or the requisite presence or absence of certain traffic or roadway characteristics. Source: ISO 34503 [4]

## Data model

Data models define the structure of data, including the types of data, the relationships between data elements, and the rules for how data can be manipulated and accessed.

## Database schema

Database schemas define how data is organized within a database component. For relational databases it describes tables, columns, data types, rows, and possible constraints linking different rows in different tables. Other database organizations may have different schemas [7].

## Inside ODD

"Inside ODD" is the state of all current conditions being within attribute ranges stated by the defined ODD. In this state the COD is inside the ODD.

## Measure

Taxonomy concepts are measured using _measure attributes_ expected to be of numeric types. For example, length, height, depth, duration, and so on are measures. ASAM OpenODD® does not define or restrict "measure attributes" as they are part of the taxonomy.

## Numeric aggregation

Numeric aggregations are restricted/pre-defined taxonomy concepts to provide statistical information about taxonomy concepts. ASAM OpenODD® defines, for example, minimum/min, maximum/max, average/avg, and so on as numeric aggregations.

## ODD boundary

ODD boundaries are limits separating the operational design domain from the rest of possible operating conditions.

## Operational Design Domain, ODD

Operational conditions under which a given driving automation system or feature thereof is specifically designed to function, including, but not limited to, environmental, geographical, and time-of-day restrictions, and/or the requisite presence or absence of certain traffic or roadway characteristics. Source: SAE J3016

## Operational Domain, OD

Set of operating conditions, including, but not limited to, environmental, geographical, and time-of-day restrictions, and/or the requisite presence or absence of certain traffic or roadway characteristics. Source: ISO 34503 [4]

## Outside ODD

"Outside ODD" is the state of one or more current conditions being outside attribute ranges stated in the defined ODD. In this state the COD is outside the ODD.

## Situation

In the context of ASAM OpenODD®, a situation represents the specific set of values that conform to an ODD taxonomy and are required to evaluate the truth values of conditions. It corresponds to an assignment of values to the fields that are defined in the ODD conditions and enables the assessment of whether the current operational conditions satisfy the defined ODD.

## Target Operational Domain, TOD

Set of operating conditions in which an ADS is expected to operate, including, but not limited to, environmental, geographical, and time-of-day restrictions, and/or the requisite presence or absence of certain traffic or roadway characteristics. Source: ISO 34503 [4]

## Taxonomy

A taxonomy (or taxonomical classification) is a scheme of classification, especially a hierarchical classification, in which things are organized into groups or types [8].

## Taxonomy concept

A taxonomy concept is a node within a taxonomy, representing a specific term used to organize and classify concepts related to ODD, OD, COD, and TOD.

## Uncertainty

Uncertainty refers to epistemic situations involving imperfect or unknown information. It applies to predictions of future events, to physical measurements that are already made, or to the unknown. Uncertainty arises in partially observable or stochastic environments, as well as due to ignorance, indolence, or both [9]. In the context of ASAM OpenODD®, uncertainty can be described by various measures, for example, risk can be defined using occurrence_rate.
