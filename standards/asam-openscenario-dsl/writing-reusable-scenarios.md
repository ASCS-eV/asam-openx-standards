# ASAM OpenSCENARIO® DSL v2.2.0 — 9.1 Writing reusable scenarios

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/user-guide/writing_reusable_scenarios.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.1 Writing reusable scenarios

## 9.1.1 Introduction

These methodology guidelines are based on existing industry experience and lengthy technical discussions, which took place as part of the standardization process. The guidelines enable users to easily create reusable scenario assets.

### 9.1.1.1 Motivation

ASAM OpenSCENARIO enables the creation of *reusable* scenarios through language constructs that are a fundamental part of modern software development.

These include:

* Extensibility
* Object-oriented inheritance
* Hierarchical composition

For example, it is possible to take a reusable *cut-in* scenario and an *oncoming-traffic* scenario to create a larger composite scenario that includes both scenarios.

The chapter contains the following methodology guidelines:

* [Use `.osc` as file extension](#sec-up-guidelines-file-extension)
* [Use abstract scenarios](#sec-up-guidelines-abstract-scenarios)
* [Use wide-ranges](#sec-up-guidelines-wide-ranges)
* [Be careful with initializations](#sec-up-guidelines-initialization)
* [Use abstract road locations](#sec-up-guidelines-abstract-road-locations)
* [Use labels](#sec-up-guidelines-labels)
* [Use generic actions](#sec-up-guidelines-generic-actions)
* [Use generic scenarios](#sec-up-guidelines-generic-scenarios)

## 9.1.2. Use `.osc` as file extension

**Prefer using `.osc` as file extension.**

For consistency and easy identification, use `.osc` as file extension for all ASAM OpenSCENARIO files.
For example, for a *cut-in* scenario definition use the file name `cut_in.osc`.

## 9.1.3 Use abstract scenarios

**Prefer declaring abstract scenarios instead of concrete scenarios.**

One of the key features of ASAM OpenSCENARIO is abstraction.
Instead of repeating the entire scenario description in each scenario variation, the language allows factoring out the commonality between scenarios and capturing this in abstract reusable scenarios.
Later on, the abstract scenarios can be used for concrete purposes or they can be composed to achieve other abstract scenarios.

This approach also allows the incremental accretion of concretizations, which supports incremental development of scenarios by delaying the specification of details until these details are known.

Assume that a cut-in scenario is listed in the requirements or requested by the development team.
If the requirement calls for a generic abstract cut-in, for example, "try different kinds of cut-in", the language provides the proper abstraction to represent the request in executable format including all the scenario dependencies in constraints.
Note that even if the requirement calls for a concrete cut-in with specific values or specific location, it might still be useful to first create an abstract scenario representation.
Such a scenario can then be further constrained to achieve the concrete request and eventually many others.

Implementing the concrete request directly in a concrete scenario may work against the user in the medium or long term, as validation typically involves running multiple cut-ins in various locations.
There is a high probability that another variation of cut-ins will be required in current or future projects.
The recommended solution is to define the needed abstract scenario as a *reusable asset*.

A cut-in scenario intent is defined as follows:

1. Start behind the ego on an adjacent lane.
2. Move in front of the ego.
3. Change the lane in front of the ego.

Capturing the distilled scenario intent above without hard-coding of specific speeds, distances, lanes, and locations will enable a more reusable scenario that does not require code duplication to achieve variations.
Once the reusable scenario is in place, it is possible to further constrain the scenario for the needed concrete values.

Working with abstraction and thinking of reuse is a fundamental concept in modern software engineering.
As opposed to creating lengthy code with multiple repetitions, engineers identify functions that can be parameterized and can be used across the code base.
They may also factor out abstract classes and derive sub-classes to achieve variations without code duplication.
These practices enable productivity and save development time and maintenance cost.

It is important to point out that concrete scenarios are still needed for specific purposes, including simulation execution or to ensure exact exchangeability.
While concrete scenarios can be be manually implemented in ASAM OpenSCENARIO, they can also be exported as a result of a scenario concretization tool chain.
Determining the proper level of abstraction for scenarios is the recommended practice to maximize reuse, and to minimize the problem of accidentally narrowing the test space by encoding concrete details at too early a stage in development.

## 9.1.4 Use wide-ranges

**Use wide-ranges to enable reusability.**

This tip is related to the guideline [Section 9.1.3, “Use abstract scenarios”](#sec-up-guidelines-abstract-scenarios).

When selecting ranges and placing constraints on values, provide wide-ranges for parametrized attributes to enable running corner-case scenarios.

## 9.1.5 Be careful with initializations

**Do not set initial speed or scenario conditions.**

Users may be tempted to select an interesting concrete speed and starting point for each vehicle.

Such concrete values may be part of specific requirements.
However setting the initial speed and conditions on the scenario makes it less reusable.

Examples:

* You cannot execute this scenario after scenarios that require different ending points.
* If the initial positions of the vehicles in a cut-in scenario are set, performing two consecutive cut-ins is not possible.

The recommended approach to maintain reusability is to *decompose* such a scenario into two parts:

1. A *generic reusable scenario* that is independent from the initial speed and conditions.
2. Provide the *specific conditions* later.

There are two possible use models here:

1. Let an OpenSCENARIO tool figure out the needed initial speed and conditions to accommodate the specified scenario.
   This is one of the biggest motivations of ASAM OpenSCENARIO to enable high volume of achieved concrete scenarios.
2. If specific initial conditions are needed, create these in a less reusable scenario wrapper that activates a reusable scenario with the needed initial condition and speeds.

The way to specify initial conditions for a reusable scenario is with the generic actions `at` attribute on the first action of the scenario.

The `at: start` constrains the needed attribute just for the beginning of the phase.
This way the initial conditions can be changed later.

The following example shows a scenario that requires an initial speed of 40 to 60 kph.

Code 80. Constraint speed

```
scenario my_scenario:
    s: speed with:
        keep (it in [40kph..60kph])

    do serial:
        init: car1.drive() with:
            speed(speed: s, at: start)  #note that it is recommended to specify an initial range for speed and not a concrete speed
```

The example can be made concrete by providing a concrete speed:

Code 81. Concrete speed

```
extend my_scenario:
    keep (s == 43kph)
```

You can always run more actions in parallel on top of the same actor to further constrain the initial behavior of the actor.

The following example illustrates that option.

Code 82. Further constraints after start

```
scenario my_other_scenario:
    do parallel:

        init: car1.drive() with:             # starts at t=0
            speed(speed: 40kph, at: start)

        a1: car1.drive() with:               # further initial conditions for car1. This affects the same initial drive
            lateral(speed: 2kph, at:start)
```

## 9.1.6 Use abstract road locations

**Use abstract definitions of roads and locations.**

ASAM OpenSCENARIO allows an abstract definition of roads and locations.

It is highly recommended to use these abstract definitions.
Do *not* hard-code the specific location and specific map in which the scenario takes place.

The recommended approach is to provide the minimal amount of road description to allow reusing the scenario in multiple locations.

Furthermore, OpenSCENARIO tools may allow finding random locations on the map to create unexpected, surprising scenarios.

## 9.1.7 Use labels

**Use labels for external scenario tuning.**

ASAM OpenSCENARIO supports assigning labels for the different phases of the scenario.

For example, a cut-in scenario may be composed of phases with the following labels defined:

1. `start_behind`
2. `get_ahead`
3. `change_lane`

These labels are useful for commenting, tagging, and readability.

Labels also have a key reuse aspect: A user can extend scenarios using labels.

In this example you can build a 'stack' of constraints:
Use the `change_lane` label to layer a constraint on the desired speed used during the `change_lane` phase.

## 9.1.8 Use generic actions

**Prefer using generic actions over specialized actions for readability and extendibility.**

While beginners may find a function-like API easier to read, using the generic actions allows for more external tuning and reuse.

For example, it is possible to specify an extension.
This is how to use a speed modifier in the extension:

1. Specify the desired speed at the end of the `change_lane` phase.
2. Put this specification on top of the generic drive.

It is not possible to achieve such an extension without using the `reach_speed` specialized actions.

Code 83. Using a generic action to extend a scenario phase

```
scenario sut.my__scenario:
    car1: vehicle
    car2: vehicle

    do serial:
        phase1: car1.drive(duration: 24s) with:
            speed([40kph..80kph], at: end)
            lane([2..4])
        phase2: car1.drive(duration: 24s) with:
            speed([70kph..60kph], at: end)
```

With generic actions, `phase2` can be extended and more modifiers can be added to the second `drive`.

## 9.1.9 Use generic scenarios

**Create generic scenarios to run on all execution platforms.**

In general, a scenario description is meant to run on all execution platforms.

Specific platform limitations should *not* be part of the generic scenario.

Do *not* hard-code parameters in the generic scenario that would lead to non-physical movements.

The aforementioned restrictions can be applied as an extension to a reusable scenario, allowing for a clean separation of the generic and use-case specific aspects.
For example, a generic overtake scenario could be extended with additional parameters specific to a proving ground use case with an automated driver model.