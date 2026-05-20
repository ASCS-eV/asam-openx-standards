# ASAM Openscenario Dsl v2.2.0 — 6.3 Scenario abstraction

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/conceptual-overview/scenario-abstraction.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 6.3 Scenario abstraction

This section defines the abstraction spectrum and the terms used throughout this standard regarding scenario abstraction levels. It also provides guidelines on transitioning between levels throughout the spectrum.

## 6.3.1 Levels of scenario abstraction

[Concretization](../terms_and_definitions.html#sec-global-terminology-concretization-short) and [abstraction](../terms_and_definitions.html#sec-global-terminology-abstraction-short) are concepts working in opposite directions.
Concretization is sometimes also called refinement.

### 6.3.1.1 Level definitions

* *Abstracting a scenario* means that the legal space captured by a scenario is enlarged.
* *Concretizing a scenario* means that the legal space captured by a scenario is reduced.

In the case of two scenarios - scenario A and scenario B - this means:

* If the legal space that is captured by scenario A is a *subset* of the legal space that is captured by scenario B, then scenario A is a *concretization* of scenario B.
* If the legal space that is captured by scenario A is a *superset* of the legal space that is captured by scenario B, then scenario A is an *abstraction* of scenario B.

The mechanisms of concretization and abstraction create a spectrum of abstraction degrees.
In theory, this spectrum is continuous.

### 6.3.1.2 Level spectrum structure

To give more structure to this spectrum, different abstraction levels are defined.
The most common ones are the following scenario levels:

* [*Concrete*](#sec-global-terminology-concrete_scenario)
* [*Logical*](#sec-global-terminology-logical_scenario)
* [*Abstract*](#sec-global-terminology-abstract_scenario)

Concrete, logical and abstract scenarios constitute a spectrum of abstraction levels.
The [abstraction](../terms_and_definitions.html#sec-global-terminology-abstraction-short) can be on the [actor](../terms_and_definitions.html#sec-global-terminology-actor-short), maneuver, or road element levels, allowing a tool to accept abstract user descriptions with multiple dependencies and produce multiple concrete scenarios that adhere to an abstract description.

Within the same abstraction level, different degrees of abstraction exist.
For example, a certain abstract scenario may be more abstract than another abstract scenario although they belong to the same abstraction level.

Stepping from the abstract to the concrete scenario level means:
A concrete scenario needs to choose specific values from the parameter ranges of an abstract scenario to be a concretization of it.

If all the parameter ranges of a concrete scenario meet all the constraints of an abstract scenario, then the concrete scenario is a concretization of that abstract scenario.

For more information, see the detailed concrete scenario definition.

#### 6.3.1.2.1 Concrete scenario

A [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) for which the exact evaluation of any of its parameters are completely determined to a fixed value for any point in time.

There are two possibilities to specify such a [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short):

1. Specify concrete locations and trajectories.
2. Reference deterministic models.

Deterministic models determine the evolution of values during [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) execution.
Examples are `driver`, `traffic`, weather, or vehicle dynamics.

|  |  |
| --- | --- |
|  | "Deterministicly assigning values" refers to all variables that may influence how the system behaves and how its resulting behavior is measured. |

There are two levels of [concrete scenarios](#sec-global-terminology-concrete_scenario) that can be specified using ASAM OpenSCENARIO:

1. Trajectory-level concrete  
   In a trajectory-level concrete specification, the position and status of each [actor](../terms_and_definitions.html#sec-global-terminology-actor-short) is provided for any execution time.
   The example [of a concrete scenario](#code-up-key-terminology-concrete-scenario) demonstrates an attribute-level [concrete scenario](#sec-global-terminology-concrete_scenario).
2. Attribute-level concrete  
   In an attribute-level [concrete scenario](#sec-global-terminology-concrete_scenario), all attribute values are specified by the user but the corresponding actual trajectories are still determined by ASAM OpenSCENARIO 2.0 technology.

#### 6.3.1.2.2 Logical scenario

A [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short) that does not specify all values for all parameters but provides a range of values that can be selected.

The goal is to allow a variation of parameter values during simulation or testing by choosing concrete values out of the ranges.
This can be done in one of the following ways:

* Predefined steps
* Distribution function
* Randomly

The free dimensions of the [logical scenario](#sec-global-terminology-logical_scenario) constitute a scenario space.

Once a single parameter value of a concrete scenario is not provided, the scenario becomes a [logical scenario](#sec-global-terminology-logical_scenario).

#### 6.3.1.2.3 Abstract scenario

A formal scenario that conceptualizes [scenarios](../terms_and_definitions.html#sec-global-terminology-scenario-short) to the level of the scenario intent.

This level of abstraction is a formal, declarative description.
This level is both machine- and human-readable.
This level can be read and processed by tools to generate scenario descriptions at more concrete levels of abstraction.

[Abstract scenarios](#sec-global-terminology-abstract_scenario) may capture dependencies and relations between attributes and behaviors using constraints.

The level of abstraction applies to scenario maneuvers, locations, and ODD needs.

Examples:

* *"An emergency vehicle in a three-lane motorway."*
* *"An aggressive cut-in by a large vehicle."*

#### 6.3.1.2.4 Functional scenario

Non-formal natural language description of a [scenario](../terms_and_definitions.html#sec-global-terminology-scenario-short).

This description is not machine-readable.

Conversion of functional scenarios to [abstract scenarios](#sec-global-terminology-abstract_scenario) is often dependent on user experience or subjective interpretation, or both.

Note that [abstract scenarios](#sec-global-terminology-abstract_scenario) can also be expressed in natural language.
The difference between functional and [abstract scenario](#sec-global-terminology-abstract_scenario) is that the [abstract scenario](#sec-global-terminology-abstract_scenario) is formal and machine-readable.

### 6.3.1.3 Level examples

This section contains examples for the three most commonly used types of scenarios as well as an example for different degrees of abstraction between two abstract scenarios.

#### 6.3.1.3.1 Concrete scenario

Code 6. A concrete scenario

```
scenario my_concrete_scenario:
    map.set_map_file("my_map.xodr")
    my_road: route = map.create_route(get_odr_points(my_file))

    car1: vehicle with:
        keep(car1.color == red)
        keep(car1.model == lincoln_mkz2017)
        keep(car1.category == car)

    do serial:
        car1.drive(duration: 24s) with:
            along(my_road)
            speed(0kph, at:start)
            speed(60kph, at: end)
            lane(3)
            position(distance:50m, at:start)
            position(distance:250m, at:end)
            acceleration(...)
```

All attributes are fully specified for any point in time.
This includes:

* Map
* Specific path
* Distances
* Speed
* All drive attributes

#### 6.3.1.3.2 Logical scenario

Code 7. A logical scenario

```
scenario my_logical_scenario:
    map.set_map_file("my_map.xodr")
    my_road: route = map.create_route(get_odr_points(my_file))

    car1: vehicle with:
        keep(car1.color in [red,green])
        keep(car1.model == lincoln_mkz2017)
        keep(car1.category == car)

    do serial:
        car1.drive(duration: 24s) with:
        along(my_road)
        speed([0kph..20kph], at:start)
        speed([40kph..80kph], at: end)
        lane([2..4])
        position(distance:[25m..60m],at:start)
        position(distance:[150m..350m],at:end)
```

The logical scenario space might include non-feasible scenarios.
For example, the combination of certain values for duration, distance, and speed may break real-life physical laws of speed, time, and distance.
The same combination of values may also exceed the length of the provided road segment without fulfilling the desired maneuver.

#### 6.3.1.3.3 Abstract scenario

Code 8. An abstract scenario

```
scenario sut.right_cut_in_by_emergency_vehicle:
    # any road that matches these constraints and not hardcoded to any specific map
    my_road: road with:
        keep(it.min_lanes>=2)

    #object constraints
    my_emergency_car: emergency_vehicle  #emergency_vehicle would need to be extension of the domain model

    do cut_in() with:         #cut_in would need to be an extension to actions or within composable scenarios.
        keep(side == right)
        keep(road == my_road)
        keep(car1 == my_emergency_car)
```

This scenario abstracts

* Locations  
  Any location with more than two lanes.
* Actors  
  Emergency that may have different structures and attributes.
* Maneuvers  
  Cut-in from the left.

The following example is a more abstracted scenario that mixes the abstract scenario with other components:

Code 9. An abstract that uses composition

```
scenario sut.cut_in_and_danger: # Getting more abstract
    p: person

    road: road
    do parallel(duration:[20s..40s]):
        right_cut_in_by_emergency_vehicle(my_road: road)
        p.cross_road(my_road:road)
        one_of: #one of several bad things
            snow_storm()
            mechanical_failure()
            ...
```

This second example shows how a few scenarios can be mixed to create interesting, potentially unpredictable scenarios.

#### 6.3.1.3.4 Comparison of two abstract scenarios

Consider the following examples:

Code 10. An abstract scenario

```
scenario sut.right_cut_in_emergency_vehicle:
    my_emergency_car: emergency_vehicle
    my_road: road with:
        keep(it.min_lanes>=2)

    # this scenario invokes a previously defined cut_in scenario
    do cut_in() with:
        keep(side == right)
        keep(road == my_road)
        keep(vehicle1 == my_emergency_car)
```

The emergency vehicle actor can be randomized into a police car, an ambulance, or a fire truck.
Once randomized, it drives using the randomized vehicle dynamics.

Code 11. A more concrete abstract scenario

```
scenario sut.right_cut_in_police_vehicle:
    my_police_car: police_vehicle
    my_road: road with:
        keep(it.min_lanes>=2)

    do cut_in() with:
        keep(side == right)
        keep(road == my_road)
        keep(vehicle1 == my_police_car)
```

[Code 10](#code-up-concrete-abstract-scenario1) is more abstract than [Code 11](#code-up-concrete-abstract-scenario2) because the second example is hard-coding the emergency vehicle to be a police car.
Therefore the second example is the more concrete version.

Another example is an abstract scenario that takes place in a specified location.
The timing and orchestration can be inferred by tooling that takes into account all constraints and dependencies, but the location itself is specified.

Note that even if all the attributes of an abstract scenario are specified, the scenario is still not trajectory-level concrete (meaning not all the locations and attributes are specified for any given point at all time of the scenario execution).
This last step of trajectory level concretization may be specified by the user or left for an ASAM OpenSCENARIO tool to determine.

## 6.3.2 Concretization and abstraction guidelines

As part of the development and V&V tasks, multiple [scenarios](../terms_and_definitions.html#sec-global-terminology-scenario-short) in different [levels of abstraction](key_terms.html#sec-global-terminology-abstraction-level) are produced.

Users often need to manually or automatically shift the level of abstraction.
The following chapters provide guidelines and tips on circumstances, methodology, and ASAM OpenSCENARIO language capabilities to move between the abstraction levels.

### 6.3.2.1 Moving from abstract to concrete

Humans think and communicate in an abstract way.
When friends are talking about an aggressive cut-in that took place on their way to the office, they do not need to detail the car trajectories or specifics to comprehend the dangerous scenario.

Natural language verification plans can use a similar level of abstraction.
They can also be open to human interpretation, inviting to close the gap in different ways.
The verification plan may call for an aggressive cut-in with a few specific values or location characteristics.
Then test writers need to describe the rest using their own judgment.

Executing or observing a scenario on any execution platform requires concrete attributes.
A vehicle always drives on a specific road and on a specific trajectory.

ASAM OpenSCENARIO allows capturing the validation and verification plan or specification in an abstract way including the definition of the relationship between actors and activities.
Implementations can then translate this abstract specification into one or more concrete executions that follow the user-specified abstract scenario.

![up abstract to concrete.drawio](_images/up_abstract_to_concrete.drawio.png)

Figure 2. From abstract to concrete

### 6.3.2.2 Moving from abstract to concrete in ASAM OpenSCENARIO

An abstract scenario can be moved to a concrete scenario when all values for all scenario attributes are specified.
This includes location, weather conditions, and more.

Users have two possibilities to move to a concrete scenario:

1. Derive from an abstract scenario and specify a value for each attribute to make it concrete.
2. Extend the abstract scenarios.

There are differences between the two kinds of use cases:

* Users need to execute any concrete scenario.  
  At this point, an automated concretization is desired.
* Users wish to take full control and they want to manually assign all values for a specified scenario.

Even if users are willing to do all the concretization work, having the abstract scenario is still useful for checking that the concrete values do not break the abstract scenario dependencies.
With an abstract scenario, users can also decide if the concrete values are consistent.

Note that it is impossible to convert an abstract scenario to a finite set of logical scenarios.
On any given map there are endless numbers of locations, possible speeds, or latencies.
Their dependencies result in an infinite number of logical scenarios with different ranges.

### 6.3.2.3 Moving from concrete to abstract

A provided concrete scenario often holds an interesting high-level intent that scenario developers may wish to duplicate.
For example, specific trajectories of two cars can be provided without explicitly stating that the scenario is a cut-in scenario.

Abstracting the high-level intent of the scenario allows replicating the intent and achieving a diverse set of similar scenarios.

Examples include:

* Developers create a concrete scenario to check a specific driving function.  
  Then they deliver the scenario to the V&V team to create more scenarios similar to this simple scenario.
* A concrete collision in the field.  
  Multiple concrete scenarios are defined based on a specific traffic accident in order to challenge the driving function and better understand the root cause.
* A concrete bug is identified using random scenario generation on a virtual platform.  
  The virtual platform can be, for example, a simulator.
  In this case, users analyze the cause of a failure or a unique combination of events.
  Then they decide that this combination represents a category of scenarios that is not mentioned in the plan.
  Users can abstract the combination and replicate its essence in multiple circumstances.
* A verification plan that goes into detail.

To achieve an abstract scenario, users need to:

1. Analyze the concrete scenario.
2. Understand the relations or combinations that make the scenario special.
3. Codify the dependencies in ASAM OpenSCENARIO formal description.

Once the intent is captured in an abstract description, multiple scenario instances can be produced automatically.

![up concrete to abstract.drawio](_images/up_concrete_to_abstract.drawio.png)

Figure 3. From concrete to abstract

### 6.3.2.4 Moving from concrete to abstract in ASAM OpenSCENARIO

ASAM OpenSCENARIO allows users to capture the abstract intent of the scenario.
To generalize concrete scenarios, they need to analyze the essence of the scenarios and capture the essence in ASAM OpenSCENARIO code.

For example, the essence of a cut-in is that a car in a different lane moves in front of another car.

On top of just capturing the intent, users can replace concrete values or the location with randomized attributes and ranges.

It is important to capture the dependencies between such attributes to ensure that the resulting scenario is consistent.
For example, specifying a velocity of 5 kph for 2 s forces a specific distance.
Picking a different value causes an infeasible scenario.