# ASAM Openscenario Dsl v2.2.0 — 6.1 ASAM OpenSCENARIO scenarios

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/conceptual-overview/writing_a_scenario.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 6.1 ASAM OpenSCENARIO scenarios

## 6.1.1 Writing ASAM OpenSCENARIO scenarios

ASAM OpenSCENARIO is a domain-specific language that is designed for describing scenarios where actors move through an environment, for example, vehicles and pedestrians.
These scenarios have parameters that let you control and constrain the actors, their movements and their environment.

ASAM OpenSCENARIO is designed to facilitate the composition of scenarios and tests, which makes it possible to define complex behaviors by using your own methodology.

There is a minimal, extensible set of actors, scenarios, and actions provided by the domain model, which are the fundamental building blocks for defining more complex behaviors.

For example, there is a `vehicle.drive()` action that can be used to compose a more complex behavior, such as *"a vehicle is approaching a yield sign"*.

Behaviors can be composed serially or in parallel.
For example, a weather scenario can be executed in parallel with a vehicle scenario to model a vehicle scenario that is taking place in specific weather conditions.

New actors and new scenarios can be created as needed, either from scratch, based on the building blocks supplied by the domain model, or by building on what you have defined so far.

### 6.1.1.1 Scenario creation tutorial

This tutorial is a quick guide for scenario creation.
Scenario developers should start here when they read or write a scenario for the first time.

#### 6.1.1.1.1 About this tutorial

This tutorial explains the following components for creating scenarios and setting goals:

* The language concepts
* The building blocks
* The mindset

#### 6.1.1.1.2 The cut-out scenario example

The cut-out scenario introduces three vehicles.
A *lead vehicle* cuts out in front of the *ego vehicle*, exposing a stopped *other vehicle*.

The functional description of the scenario in naturally spoken English language is as follows:

* The `start_driving` phase  
  *"Three vehicles start driving."*
* The `lead_vehicle` phase  
  *"The lead vehicle gets in front of the ego vehicle, while the other vehicle gets to a desired position and stops."*
* The `cut_out` phase  
  *"The lead vehicle cuts out to the left or the right, while the other vehicle remains stopped.
  At this phase, the ego vehicle is challenged to avoid a collision safely and conveniently."*

The ASAM OpenSCENARIO language allows to capture the essence of the cut-out scenario in a format that is both human- and machine-readable.
This level of abstraction is called an *abstract scenario description*.

The cut-out scenario can take place in multiple driving circumstances, for example:

* On different roads
* With different speeds
* With different distances between the vehicles
* In different weather conditions

A more concrete scenario can be achieved by adding constraints to the scenario description.
Then, ASAM OpenSCENARIO technology can perform such a scenario with multiple necessary conditions as part of a specific test.

For more information on abstraction levels, see [Section 6.3.1, "Levels of scenario abstraction"](scenario-abstraction.html#sec-up-scenario-abstraction).

#### 6.1.1.1.3 A world built of actors and actions

The main building blocks of scenarios are *actors* that perform *actions*.

Examples of actors include:

* Vehicles
* Pedestrians
* Traffic lights
* A rock on the road
* Weather

Actors can perform actions.
Actions are behaviors.

Examples:

* *Vehicles* can *drive*
* *Pedestrians* can *walk*

In the cut-out example, three actors are involved:

1. The *ego vehicle*, which is the vehicle-under-test.
2. The *lead vehicle*.
3. The *other vehicle*.

The following code shows how actors are instantiated in an example scenario.

Code 1. Actors within a cut-out scenario

```
scenario cut_out:            (1)
    lead_vehicle: vehicle    (2)
    other_vehicle: vehicle   # this is a comment (3)
```

The ego vehicle instance exists and does not need to be instantiated as part of the cut-out.

|  |  |
| --- | --- |
| **1** | `scenario` keyword with the name `cut_out` |
| **2** | `lead_vehicle` instantiation  The ASAM OpenSCENARIO language uses the modern popular Python syntactic conventions. The `lead_vehicle` actor is of struct `vehicle`. The `vehicle` struct and a basic set of attributes, such as *vehicle\_category* and *vehicle\_color*, are provided in the ASAM OpenSCENARIO domain model.  Since all attributes of the vehicles are yet unspecified, they may be initialized to arbitrary values, possibly randomized, as long as these values satisfy the constraints that will be added to the scenario as the scenario is developed further. Note that indentation matters. The four spaces before the `lead_vehicle` definition mean, that the `lead_vehicle` is within the `cut_out` scenario definition. |
| **3** | `other_vehicle` instantiation  This line contains a comment that starts with a *hash character* (`#`), and extends to the end of the line. |

For more information about the built-in domain model, see  [Section 8, "Domain model reference"](../domain-model/domain-model.html#top-bc4ef39d-50c4-4f09-9060-57e795a226ce).

At this point, the behavior of the actors is not yet defined.
This happens within the scenario’s `do` block.

#### 6.1.1.1.4 Describing actions over time

The following code illustrates the `do` block:

Code 2. Scenario behavior within the `do` block

```
    do serial():   (1)
        start_driving: parallel():   (2)
            sut.vehicle.drive()      (3)
            lead_vehicle.drive()     (3)
            other_vehicle.drive()    (3)

        lead: parallel():   (4)
            sut.vehicle.drive()
            lead_vehicle.drive() with:
                lane(same_as: sut.vehicle, at: end)
                position([20m..200m], ahead_of: sut.vehicle, at: end)
            other_vehicle.drive() with:
                lane(same_as: sut.vehicle, at: end)
                speed(0kph, at: end)
                position([20m..200m], ahead_of: lead_vehicle, at: end)

        cut_out: parallel(duration: [1s..4s]):   (5)
            sut.vehicle.drive()
            lead_vehicle.drive() with:
                lane(side_of: sut.vehicle, side: side, at: end)
            other_car.drive() with:
                speed(speed: 0kph)
```

|  |  |
| --- | --- |
| **1** | `do` block  The `do` block contains invocations of actions and scenarios that can happen serially or in parallel. In this example, scenario defines three phases that run in series, while each phase describes the behavior of the participating vehicles happening in parallel. |
| **2** | `start_driving` phase  A label, such as the *start\_driving* label shown here, allows for referencing and refining this part of the scenario later. For example, this scenario can be refined to an edge case with high-speed aggressive driving (see more on this further below). |
| **3** | `start_driving` phase  Within the `start_driving` phase, the vehicles are driving. Note that there is no initial speed or position defined. ASAM OpenSCENARIO allows scenario designers to keep scenarios abstract. This is important, since determining the right initialization values requires engineering time. Hard-coding the scenario for specific values also means less reuse and limits the ability to explore unknown variations of scenarios. |
| **4** | `lead` phase  In this phase, each vehicle set to a desired position and speed. You can define specific values for the speed or location of a vehicle at the beginning, end, or throughout the phase. Modifiers, such as lane and position modifiers, provide simplified means of control of the drive action.  In the example the `lead_vehicle` should drive in the following way: 1. On the same lane as the ego (`lane(same_as: sut.vehicle, at: end)`). 2. 20 to 200 meters in front of the ego (`position([20m..200m], ahead_of: sut.vehicle, at: end)`), while the `other_vehicle` stops (`speed(speed: 0kph)`). |
| **5** | `cut_out` phase  Here the vehicles keep driving, while the `lead_vehicle` performs the cut-out. |

#### 6.1.1.1.5 Setting the scenario goals

The abstract scenario shown in [Code 2](#code-up-tutorial-behavior-do-block) can produce an unlimited amount of concrete scenarios.

ASAM OpenSCENARIO provides functional coverage features.
These can be used to set measurable goals to determine if sufficient testing was performed.

The goal for this example is: Exercise at least 10 cut-outs to the right and 10 cut-outs to the left.

This is how to set the scenario goals:

Code 3. Setting the scenario goals.

```
extend cut_out:
    cover(side, event: end, target: 10)   (1)
```

|  |  |
| --- | --- |
| **1** | The key coverage attributes include what expression to sample, and when to sample it. In this case, sampling the `side` expression at the `end` of the scenario. The scenario’s built-in `end` event is used for that. |

The ASAM OpenSCENARIO breadth of coverage features allows to precisely describe any ODD, project or scenario need.

Examples of coverage features include:

* Ignoring specific values.
* Defining ranges to measure continuous values, such as speeds or distances.
* Cross-covering of more than a single item (for example to try all vehicle categories cutting out for both sides).
* …​

For more information on ASAM OpenSCENARIO coverage features, please refer to  [Section 7.5, "Coverage"](../language-reference/coverage_main.html#top-lc-coverage-main).

#### 6.1.1.1.6 Layering constraints to fill a coverage hole

If a coverage goal is not reached, ASAM OpenSCENARIO allows to layer a constraint to steer the ASAM OpenSCENARIO technology and fill the missing scenario.

If the coverage result did not observe enough cut-out scenarios from the right side, an extension can correct this.

The following code tunes the result to make only cut-outs from the `right`.

Code 4. Extending the cut-out

```
extend cut_out:   (1)
    keep(side == right)
```

|  |  |
| --- | --- |
| **1** | The extension can be placed in a separate file and be loaded together with the original scenario definition. This separation allows defining a single abstract reusable scenario that can be tuned to achieve various purposes, without modifying the original code. |

For more information on constraint layering and extensions, please refer to  [Section 9.3, "Extending the domain model"](../user-guide/extending_the_domain_model.html#top-dm-extension-guidelines-main).

### 6.1.1.2 Implementing ASAM OpenSCENARIO

#### 6.1.1.2.1 Language characteristics

The language is a "Python style" language.
This implies, that *line breaks* and *indentation* have meaning, and are part of the language structure.

An ASAM OpenSCENARIO scenario may look like this:

Code 5. An ASAM OpenSCENARIO scenario

```
scenario vehicle.two_phases:
    do serial (duration : [10s..30s]):
        phase1: actor.drive() with:
            speed(speed: 0kph, at: start)
            speed(speed: 10kph, at: end)
        phase2: actor.drive() with:
            speed(speed: [10kph..15kph])
```

|  |  |
| --- | --- |
|  | This is only an example, some details may be omitted. |

The key building blocks of ASAM OpenSCENARIO can be seen as data structures:

* *Simple structs*  
  Basic entities containing attributes, constraints, and so on
* *Actors*  
  Are like structs, but also contain scenarios
* *Scenarios*  
  Describe the behavior of actors

These structures have attributes that hold scalar values, lists, or other structures.
Attribute values can be described as expressions or calculated by external method definitions.
You can control attribute values with `keep()` constraints, for example:

```
keep(car1.speed < 50kph)
```

The language has additional building blocks like:

* Parameters
* Modifiers
* Events
* …​

The language reference manual presents all the constructs of the language as well as its types and expressions.

#### 6.1.1.2.2 Parts of the domain model

The ASAM OpenSCENARIO domain model contains the following entities that can be used for scenario implementation:

* *Vehicles and vehicle properties*  
  You can find how to define a vehicle, or what properties or attributes a vehicle can have.
* *Coordinate systems*  
  Geometrical definitions such as:

  ```
  struct position_3d:
      x: distance
      y: distance
      z: distance
  ```
* *Environment*  
  For example, the weather conditions.
* *Units*  
  Units are based on the International System of Units (SI).
* *Road abstraction*  
  The domain model specification has a chapter on road abstraction.
  The approach of this version of ASAM OpenSCENARIO enables scenario developers to describe the road network, on which the scenario occurs, in an abstract way.
  You can refer to the road network within the scenario.
  Using this level of abstraction, scenarios can be matched to various locations on a given map topology.

#### 6.1.1.2.3 Building a simulation engine

ASAM OpenSCENARIO is a declarative and constraint-based language.
Therefore, this standard provides a *declarative* language semantics definition that is based on the notion of *trace acceptance*: It defines which behaviors (executions) of a traffic system are *valid* with respect to a given ASAM OpenSCENARIO model.

Implementers of an ASAM OpenSCENARIO simulation engine may be interested in *operational* semantics that define how such an engine shall perform the next step in an ongoing execution.
However, this standard does not provide any particular operational semantics description.

Instead, implementers are free to choose an operational interpretation of the declarative semantics, as long as the behaviors produced are valid with respect to the declarative semantics in this standard.

Depending on the use case, one of the following behaviors of an ASAM OpenSCENARIO simulation engine may be desired:

* Produce only *one execution* of all the valid executions.
  This may be sufficient in some cases.
* Produce a *representative subset* of all the valid executions.
* Produce *executions* in a way that efficiently satisfies certain *coverage goals*.

However, this standard does not define any specific requirements in that regard.