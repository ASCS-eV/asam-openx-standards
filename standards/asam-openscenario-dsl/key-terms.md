# ASAM Openscenario Dsl v2.2.0 — 6.2 Key terminology

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/conceptual-overview/key_terms.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 6.2 Key terminology

This section provides a summary of key terminology used throughout this standard.

## 6.2.1 Operational design domain (ODD)

The complete range of space where the system under test is expected to operate.

## 6.2.2 Action

A fundamental, non-decomposable behavior of an [actor](../terms_and_definitions.html#sec-global-terminology-actor-short). An action is a piece of behavior that can be executed or observed. Actions are abstract and their actual implementation is platform-specific and outside of the scope of this standard.

### 6.2.2.1 Action details

Actions are used whenever the state of an [actor](../terms_and_definitions.html#sec-global-terminology-actor-short) is expected to change.
Typical examples include:

* A vehicle changing speed, changing lanes, or activating a turn signal.
* Pedestrians walking on the sidewalk or crossing the street.
* A traffic light changing color.

[Actors](../terms_and_definitions.html#sec-global-terminology-actor-short) may perform multiple actions simultaneously.

### 6.2.2.2 More information about actions

* Actions constitute the fundamental building block for [scenarios](../terms_and_definitions.html#sec-global-terminology-scenario-short) and a typical [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) is a composite of multiple actions (and, potentially, other [scenarios](../terms_and_definitions.html#sec-global-terminology-scenario-short)).
* The temporal or logical organization of actions within the [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) is achieved through *temporal operators* (for example, `serial`, `parallel`, or `one_of`) using [*events*](../terms_and_definitions.html#sec-global-terminology-event-short) to trigger the start or end of an action, or both.
* Unlike [scenarios](../terms_and_definitions.html#sec-global-terminology-scenario-short), actions are not intended to be decomposed into smaller parts.
* Actions can consume zero or non-zero (simulation- or clock-) time to be executed.
* Actions can be interrupted by instantiation of another action or invocation of another [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short).

## 6.2.3 Scenario

A description of the behavior or temporal evolution of physical objects and environmental conditions on the driving infrastructure over an interval of time, including the movement of traffic participants or the change of environmental conditions.

* It is a base building block of the storyboard hierarchy.
* It can represent a definition of a single [action](../terms_and_definitions.html#sec-global-terminology-action-short).
* It can use composition operators to define equivalents to `Event`, `Maneuver`, `Act`, `Story`, and all the levels up to a description of a complete *scenario* of ASAM OpenSCENARIO XML 1.3.1.

Scenarios can be expressed in multiple levels of [*abstraction*](../terms_and_definitions.html#sec-global-terminology-abstraction-level-short).

An ASAM OpenSCENARIO scenario can be used to define scenarios in the following contexts:

* SOTIF (ISO 21448 - Safety of the intended functionality)
* UNECE/WP.29 Regulations - World Forum For harmonization of vehicle regulations
* [Euro] NCAP - New Car Assessment Program
* Other safety or regulation frameworks

### 6.2.3.1 Scenario details

A full scenario description should answer the following questions:

* Where does the scenario take place?

  + Answer: On the driving infrastructure of the driving domain (N1).
    The driving infrastructure includes the road layout, road furniture, and other static objects (like buildings and vegetation).
* Who participates in the scenario?

  + Answer: [Actors](../terms_and_definitions.html#sec-global-terminology-actor-short) (like vehicles, objects, people, and traffic lights) participate in the scenario; environmental conditions (N2) (like weather and lighting) can be set or changed in the scenario, or both.
* What do the participants do?

  + Answer: [Actions](../terms_and_definitions.html#sec-global-terminology-action-short) describe the behavior of the [actors](../terms_and_definitions.html#sec-global-terminology-actor-short); environmental actions (N2) describe changing environmental conditions during the scenario.
* When do the [actions](../terms_and_definitions.html#sec-global-terminology-action-short) take place?

  + Answer: This is achieved through the following language elements:

    1. *Compositional operators*
    2. *Temporal directives*
    3. *Events*
  + OpenSCENARIO *compositional operators* - such as `serial`, `parallel`, `one_of`, and so on - allow users to construct phases or temporal labels for when a scenario invocation or action instantiation occurs.
  + *Temporal directives* - such as `wait`, `on`, or `until` - reference events.
  + ASAM OpenSCENARIO *events* resolve to a specific point in time within the scenario.  
    This allows users to:

    1. Resolve the start and/or end of a phase.
    2. Resolve a moment to take a measurement in the scenario.

### 6.2.3.2 More information about scenarios

* A scenario may include a specification of validity criteria.
* OpenSCENARIO language enables a scenario to include commands to control the test execution platform.
* A scenario may refer to simulations, physical tests, driving data, or any combination thereof.
* There is not necessarily a one-to-one relation between one scenario and one ASAM OpenSCENARIO file.
* A single ASAM OpenSCENARIO file can contain several scenarios, or the definition of a single scenario can be distributed across different ASAM OpenSCENARIO files, or both.

## 6.2.4 Scenario instance

The [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) that is executed, whether it is passively observed or actively controlled.

By definition, the scenario instance is [concrete](scenario-abstraction.html#sec-global-terminology-concrete_scenario).
For example, a user may ask for a cut-in [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) (scenario request), execute it and observe the scenario instance that might be different from the [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) request.

## 6.2.5 Abstraction

Generalization of one or more related specific implementations or situations. In this standard, abstraction refers to the generalization of [scenarios](../terms_and_definitions.html#sec-global-terminology-scenario-short). Abstraction is the opposite of [concretization](../terms_and_definitions.html#sec-global-terminology-concretization-short).

The degree of abstraction is defined as [abstraction levels](#sec-global-terminology-abstraction-level).

## 6.2.6 Abstraction levels

For more information, see the detailed concrete scenario definition.

Gradation spectrum of generalization ([abstraction](../terms_and_definitions.html#sec-global-terminology-abstraction-short)) of a [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short).

The following definitions list the different levels of abstractions in which a scenario can be specified:

* [Concrete scenario](scenario-abstraction.html#sec-global-terminology-concrete_scenario) - A [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) for which the exact evaluation of any of its parameters are completely determined to a fixed value for any point in time.
* [Logical scenario](scenario-abstraction.html#sec-global-terminology-logical_scenario) - A [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) that does not specify all values for all parameters but provides a range of values that can be selected.
* [Abstract scenario](scenario-abstraction.html#sec-global-terminology-abstract_scenario) - A formal scenario that conceptualizes [scenarios](../terms_and_definitions.html#sec-global-terminology-scenario-short) to the level of the scenario intent.
* [Functional scenario](scenario-abstraction.html#sec-global-terminology-functional_scenario) - Non-formal natural language description of a [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short).

This picture from [[13](../bibliography.html#bib-Neurohr_2021)] shows the different levels of abstraction in which a scenario can be specified.

![Levels of scenario abstraction](../_images/up_scenario_levels.png)

Figure 1. Levels of scenario abstraction (Source: [[13](../bibliography.html#bib-Neurohr_2021)])

|  |  |
| --- | --- |
|  | Abstraction levels are a spectrum and not limited to the four layers. |

The levels of abstraction and other of their key aspects are discussed in more detail in  [Section 6.3, "Scenario abstraction"](scenario-abstraction.html).
Guidelines on how to move a scenario more towards either end of this spectrum are described in [Concretization and abstraction guidelines](scenario-abstraction.html#sec-up-scenario-abstraction-guidelines).