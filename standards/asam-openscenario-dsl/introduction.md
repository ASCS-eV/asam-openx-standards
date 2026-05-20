# ASAM Openscenario Dsl v2.2.0 — Introduction

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/introduction.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Introduction

## Overview

To verify the safety and the correct functionality of an Autonomous Vehicle (AV) or an Advanced Driver Assistance System (ADAS), it is necessary to observe its behavior in various evolving situations.
These evolving situations are called *scenarios*.

Using ASAM OpenSCENARIO, scenarios can be created that describe the behavior of the autonomous vehicle as well as other actors or entities in the environment.

[ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) covers the following key concepts:

* [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) is a *domain-specific* language.  
  The language is tailored for describing complex traffic system scenarios at various abstraction levels.
  ASAM OpenSCENARIO also provides a *domain model* that captures the central concepts of dynamic traffic systems in the form of types and actions that can be used as the basic building blocks when modeling scenarios.
* [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) scenarios can be *high-level abstract descriptions*.  
  Many specific variants of a scenario can be created by varying the scenario parameters, for example, speed, vehicle type, weather conditions, and so on.
  Tools that support [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) can generate these variants automatically, within the constraints that can be specified.
  These tools then collect and aggregate parameter data from successful tests.
  This data enables to measure the safety of autonomous vehicles.
* [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) is a *programming* language.  
  When designing and specifying scenarios, it is essential to think of them as software programs.
  To define complex behaviors, scenarios can be composed in different ways.
  For example, scenarios can invoke other scenarios in sequence or in parallel.
  One scenario can be chosen as the entry point for execution; executing this scenario leads to the execution of the behaviors that it is composed of.
* [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) is a *declarative* language.  
  The language describes what should happen, rather than instructing *how* it should happen.
  The language uses *constraints* to specify these expectations.
* [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) is a *constraint-based* language.  
  *Concrete values* can be specified for parameters, for example, vehicle speeds, scenario durations, execution orders, and so on.
  Also, *constraints* can be specified over these parameters.
  This allows to define scenarios in a more abstract way: A scenario model can be created that encompasses a whole family of many concrete scenarios.
* [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) is an *aspect-oriented* programming language.  
  Behavior of a given base scenario model can be modified without disturbing the original description of the scenario.
  This is useful for the following purposes:

  + The whole behavior or aspects of the behavior can be modified.
  + The behavior of some or of all instances of an object can be modified.
  + The behavior can be modified to suit a particular test or simulation.

### Chapter overview

[ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) consists of the following parts:

* [Section 6, "Conceptual overview"](conceptual-overview/conceptual_overview.html#top-0343fd24-ebc4-4288-b6bf-d86231d920e9)  
  The conceptual overview describes central concepts of [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html), particularly scenarios and key terminology.
* [Section 7, "Language reference manual"](language-reference/language-reference.html#top-40ce7591-c88e-4e44-8b23-ae775e2251f2)  
  The language reference manual contains a complete definition of the domain-specific language that is used to describe scenarios.
* [Section 8, "Domain model reference"](domain-model/domain-model.html#top-bc4ef39d-50c4-4f09-9060-57e795a226ce)  
  The domain model defines the entities needed to build scenarios.
  It defines different actions and properties of these entities.
* [Section 9, "User guide"](user-guide/user-guide.html#top-16cc8975-d82a-404c-bb04-1ddd7a940562)  
  The user guide contains extension guidelines that explain how additional entities can be created and added to the domain model. It also provides guidelines on writing reusable scenarios and styling of [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html) syntax.

### Features of this documentation

This section explains enhanced functionality for accessing the content of this standard.

On the top right, a full text search is present.
When entering one or more terms into the search bar, the entire content of the standard is searched and topics that contain those terms are listed.

On the right, a table of contents for subsections is present.
This additional table enables easier access to subtopics.

Within continuous text, content is linked where it is useful to provide related and additional content or more specific explanations to a subject.

To return to the landing page, click on [**ASAM OpenSCENARIO DSL**](index.html) in the table of contents on the left hand side.

### Target group

The following users were explicitly considered during the creation of ASAM OpenSCENARIO:

Auditors/regulators


AV/ADAS developer companies


Content or model developers


Development project leaders


Researchers


Safety engineers


Service providers


Software developers


Stakeholders


System engineers


Test engineers


Tool developers


Tool providers or consumers

## Conventions and notations

### Units

See [Section 7.3.4, "Physical types and units"](language-reference/types.html#sec-lc-physical-types).

### Modal verbs

To ensure compliance with the ASAM OpenSCENARIO specification, users need to be able to distinguish between requirements, recommendations, permissions, possibilities and capabilities, and external constraints.

The following rules for using modal verbs apply:

Table 1. Verbal forms for expressions of provisions


| Provision | Verbal form | Definition |
| --- | --- | --- |
| Requirement | shall, shall not | A requirement conveys objectively verifiable criteria to be fulfilled and from which no deviation is permitted if conformance with the document is to be claimed. |
| Recommendation | should, should not | A recommendation conveys a suggested possible choice or course of action deemed to be particularly suitable without necessarily mentioning or excluding others. |
| Permission | may | A permission conveys consent or liberty (or opportunity) to do something. |
| Possibility and capability | can, cannot | A possibility conveys expected or conceivable material, physical or causal outcome.  A capability conveys the ability, fitness, or quality necessary to do or achieve a specified thing. |
| External constraint | must | An external constraint or obligation on the user of the document, for example laws of nature or particular conditions existing in some countries or regions, that is not stated as a provision of the document. External constraints are not requirements of the document. They are given for the information of the user. |

### Normative and informative content

Content in this standard can be normative or informative.
The sections listed in [Table 2](#tab-normative-informative-content) are normative or informative per definition.

Table 2. Normative and informative sections


| Section | Indication |
| --- | --- |
| Foreword | Informative |
| Introduction | Informative |
| Scope | Normative |
| Normative references | Informative |
| Terms and definitions | Normative |
| Abbreviations | Normative |
| Annexes | Annexes can be normative or informative. The annex heading contains the indication "(normative)" or "(informative)". |
| Bibliography | Informative |

All other sections in this standard are normative as long as not explicitly stated otherwise.
Informative sections are highlighted using the non-normative tag:

|  |  |
| --- | --- |
|  | Please note that the following section and its sub-sections are non-normative. |

The non-normative tag is valid for the section and all of its sub-sections.

### Typographic conventions

Table 3. Typographic conventions


| Mark-up | Definition |
| --- | --- |
| `Code elements` | This format is used for code elements, such as technical names of classes and attributes, as well as attribute values. |
| *Terms* | This format is used to introduce glossary terms and new terms and to emphasize terms. |

## Deliverables

The following deliverables are provided for ASAM OpenSCENARIO:

* [ASAM OpenSCENARIO® DSL BS 2.2.0 Specification, 2026-03-19](index.html), this document
* The [domain model library](domain-model/_attachments/ASAM_OpenSCENARIO_DSL_v2.2.0_Domain_model_library.zip), consisting of `standard.osc` and the sub-modules `types.osc` and `domain.osc`.  
  An informative consolidation of the normative content of  [Section 8, "Domain model reference"](domain-model/domain-model.html#top-bc4ef39d-50c4-4f09-9060-57e795a226ce).
* A consolidated [extended Backus-Naur form (EBNF)](language-reference/_attachments/grammar.ebnf).  
  An informative consolidation of the normative content of [Section 7.2.2, "Grammar of ASAM OpenSCENARIO"](language-reference/language_syntax.html#sec-lc-syntax-grammar)

## Entry points

This section provides common entry points where to start reading, depending on knowledge, interests and needs.

### Getting familiar with ASAM OpenSCENARIO

The [Introduction](introduction.html) provides an overview about ASAM OpenSCENARIO, the target group, and the deliverables provided with ASAM OpenSCENARIO.

### Understanding the concept of ASAM OpenSCENARIO

[Section 6, "Conceptual overview"](conceptual-overview/conceptual_overview.html) provides a summary of the features, terminology and specific concepts used in ASAM OpenSCENARIO.

### ASAM OpenSCENARIO language specification

[Section 7, "Language reference manual"](language-reference/language-reference.html) contains the normative specification of the language, its syntax, grammar, semantics and more.
This documentation helps to start creating scenarios right away, and in getting familiar with the domain-specific language that is used in ASAM OpenSCENARIO.

### Using the domain model

[Section 8, "Domain model reference"](domain-model/domain-model.html) contains information how to use the domain model.
The documentation defines the different entities in the *"world"* of ASAM OpenSCENARIO.

### Using ASAM OpenSCENARIO

[Section 9, "User guide"](user-guide/user-guide.html) contains guidelines how to write reusable scenarios, and how to properly format ASAM OpenSCENARIO code.

[Section 9.3, "Extending the domain model"](user-guide/extending_the_domain_model.html) explains how to define various entities in ASAM OpenSCENARIO, for example actors, structs or actions.
New entities can then be added and used in scenarios.

## Extending ASAM OpenSCENARIO

Scenario developers may need functionality that is not available in this release.
Such functionality may be missing because it has not been implemented yet (but is a candidate for future releases) or because it has been considered implementation-specific (and has therefore been left out intentionally).

The language offers self-extension capabilities as well as the ability to bind to external software (methods that are implemented in a different language or mechanism).

Consult the instructions on extending the domain model to use entities, actors, or actions that are not currently defined in the domain model (see  [Section 9.3, "Extending the domain model"](user-guide/extending_the_domain_model.html#top-dm-extension-guidelines-main)).

Scenario developers can use calls to external functions if they have to implement missing functionality.
For example, this version of ASAM OpenSCENARIO does not define a built-in distribution function for parameter values.
Such distribution functions can be implemented by an external method (see [Section 7.3.7, "Methods"](language-reference/types.html#sec-lc-methods) for the definition of external methods).
Parameters can be constrained by such an external method (see  [Annex C, *Parameter distributions (informative)*](annexes/parameter_distribution.html) for an example).