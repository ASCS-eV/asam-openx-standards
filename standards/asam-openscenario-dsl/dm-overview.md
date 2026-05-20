# ASAM Openscenario Dsl v2.2.0 — 8.1 Domain model introduction

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/dm_overview.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.1 Domain model introduction

This section gives an introduction to the domain model.

## 8.1.1 Introduction

This introduction presents definitions of the term *domain model*, introduces the ASAM OpenSCENARIO domain model, and lists relations to other standards.

## 8.1.2 About domain models

*Fowler* [[14](../bibliography.html#bib-Fowler_2021)] defines domain models as

> an object model of the domain that incorporates both behavior and data.

— Martin Fowler  
P of EAA: Domain Model

*Brown* [[15](../bibliography.html#bib-Brown_2014)] describes domain models in more detail as

> […​] your organized and structured knowledge of the problem.
> The Domain Model should represent the vocabulary and key concepts of the problem domain and it should identify the relationships among all of the entities within the scope of the domain.

— Philip Brown  
Culttt: What is the Domain Model in Domain Driven Design?

Domain models can also be referred to as *"Conceptual Models"* or *"Concept Systems"*, for example, as described in ISO704 [[16](../bibliography.html#bib-iso704)].

## 8.1.3 ASAM OpenSCENARIO domain model

The domain model of ASAM OpenSCENARIO provides a set of standard solutions for entities and their actions (see  [Section 8.8, "Movement actions"](actions.html#top-dm-movement_actions)).

More specifically, the top-level entities or *actors* are:

* [Physical objects](entity.html#sec-dm-entities-physical-objects) with dedicated actions, mostly to define their motion
* [Environment](environment-actors.html#sec-dm-entities-environment) with actions, for example, to define the weather conditions
* [Maps](dm_abstract_road_network.html#sec-dm-roads-maps) to describe the road network in an abstract form

Furthermore:

* [Physical types and structs](physical_types.html#top-dm-physical-types) include a normative set of scalar and compound types with units.
* [Primitive types and structs](primitive_types.html#top-dm-primitive-types) include a normative set of methods on primitive types.

Using these pre-defined entities has the following advantages:

* Ensure interoperability of scenario definitions between tools
* Save development time
* Lead users to a correct methodology

However, no committee can predict all possible actors, actions, and fields for all current and future industry purposes.
Therefore, an extension mechanism for the domain model is presented in a separate document to enable customization of the domain model.

Due to the rapidly evolving nature of the domain addressed by ASAM OpenSCENARIO, [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](../index.html) is built to allow easy, non-normative extension of the domain model.
Later releases of the standard will be extended to meet industry demand with additional entities and actions.

The domain model is structured into sub-modules, allowing partial use where necessary or wanted:

Types
:   The sub-module `types` consists of the primitive types as defined in [Primitive types and structs](primitive_types.html#top-dm-primitive-types), the physical types and unit definitions, as well as related basic structs as defined in [Physical types and structs](physical_types.html#top-dm-physical-types).
    These are considered universal parts of the domain model.
    All definitions of this sub-module reside in the `stdtypes` namespace.

Domain
:   The sub-module `domain` reflects the remainder of the domain model.
    All definitions of this sub-module reside in the `std` namespace.

The section [Importing the standard library](../language-reference/Libraries.html#code-lc-libraries-file-import-standard-library) explains how to make the functionalities of the standard library available to users of ASAM OpenSCENARIO, including the ability to selectively import only sub-modules, or the whole standard library.

## 8.1.4 Harmonization

Harmonization of the domain model across different ASAM standards and other standards is desirable and has the following advantages:

* Harmonization supports the seamless use of these standards with ASAM OpenSCENARIO.
* Harmonization avoids user confusion caused by conflicting terms and definitions.

Therefore, the following standards have been taken into account:

* *ASAM OpenSCENARIO XML 1.3.1*  
  Features related to the domain model of ASAM OpenSCENARIO XML 1.3.1 are covered to ensure this version of ASAM OpenSCENARIO is a super-set of ASAM OpenSCENARIO XML 1.3.1.
* *ASAM OSI*  
  Align with ASAM OSI where possible, to enable coherent reuse of attributes from scenario definition in sensor models.
* *ASAM OpenDRIVE*  
  Align with ASAM OpenDRIVE where possible, to avoid conflicting terms and definitions without restricting the usage to maps defined in ASAM OpenDRIVE format.
* *ASAM OpenXOntology*  
  Collaboration with ASAM OpenXOntology to aim at improved harmonization of ASAM standards.
* *UN ECE/TRANS/WP.29/78/Rev.6*  
  Used as a basis for the [categorization of vehicles](entity.html#sec-trafficparticipant-enum-vehicle_category).