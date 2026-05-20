# ASAM OpenSCENARIO® DSL v2.2.0 — 8.4 Actions and modifiers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/dm_actions_and_modifiers.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.4 Actions and modifiers

Multiple considerations are taken into account for the creation of the ASAM OpenSCENARIO domain model actions and modifiers.

Key requirements for actions and modifiers are:

* [Provide ease of use and software engineering fundamentals](#sec-dm-actions-ease-of-use)
* [Allow the tuning of actions within the context of a scenario](#sec-dm-actions-tuning-actions)
* [Support concrete goals and achieve unknowns](#sec-dm-actions-goals-and-unknowns)
* [Provide a similar API and use-model for both actions and scenarios](#sec-dm-actions-api-and-use-model)
* [Provide actions that are platform- and implementation-agnostic](#sec-dm-actions-agnosticism)
* [Support generic and specialized action styles](#sec-dm-actions-styles-and-modifiers)

These key requirements are explained in more detail in the following sections.

## 8.4.1 Ease of use

Actions combine ease of use and simplicity with reusability and generality.
This allows creating reusable assets and libraries.
The ASAM OpenSCENARIO domain model is designed for the creation of modular and composable scenarios leveraged by software engineering fundamentals.

As a result of balancing ease of use and re-usability, the ASAM OpenSCENARIO language allows users to further specialize the ASAM OpenSCENARIO domain model.

## 8.4.2 Tuning actions

Actions are encapsulated pieces of behaviors that can be activated in multiple scenarios and contexts.
Users can create an abstract action and further direct or tune this action for a specific scenario need.
This can be achieved on the type level and on the instance level.

Therefore users can:

* Tune actions by locking one of the parameter values.  
  Example: Ego’s speed is 5 kph throughout the drive.
* Narrow the allowed range.  
  Example: Ego’s speed is between 5 kph and 10 kph.
* Apply a constraint.  
  Example: Ego’s speed is less than 60 kph.
* Introduce a dependency between attributes.  
  Example: Ego’s speed is slower than that of a target vehicle.

## 8.4.3 Goals and unknowns

As part of a project, users may want to explore the unknown or the unexpected as per SOTIF.

This can be done with two approaches:

1. Explicitly specify a scenario execution.
2. Provide the generic direction in a stochastic approach.

Users often want to use a combination of the two approaches: Some of the parameters are specified and some are automatically inferred in a consistent way to the provided values.

This is possible with ASAM OpenSCENARIO, which allows the combination of both concrete and abstract statements while also reusing the same assets.

ASAM OpenSCENARIO allows users to control the level of freedom.
For example, consider a lane change towards the curbside of a road.
It is likely not reasonable for an ASAM OpenSCENARIO solver to be able to change lanes onto a curb leaving the drivable surface area via a lane change maneuver.

## 8.4.4 API and use-model

While actions represent atomic pieces of behavior, scenarios represent composite behaviors that are built from other actions or scenarios.
Because users may need to replace an atomic behavior with a composite behavior for different platform needs, ASAM OpenSCENARIO provides consistency in both triggering and observing actions and scenarios.
For example, invoking scenarios and actions is done the same way.
Much of the motivation in these chapters is valid for both actions and scenarios.

## 8.4.5 Agnosticism

ASAM OpenSCENARIO enables a cross-industry language that can be used for all platforms including physical and virtual testing.

This means that:

* The same ASAM OpenSCENARIO engine can be connected to multiple platforms.  
  Exactly how individual vendors connect the high-level language to a simulator, HiL or test truck is beyond the scope of the standard and this documentation.
* The same scenario code can serve both physical platforms and platforms with platform-related additions.

## 8.4.6 Action styles and modifiers

Two possible styles are provided for scenario specification:

* [Generic actions](#sec-dm-actions-generic-actions)  
  Generic actions only have the arguments that are inherited from the parent action class.  
  Generic actions activate a rich set of controls on how to perform the action with the use of modifiers for actions.
  This makes generic actions multi-purpose.  
  Example: *"Drive with fast speed at the beginning and slow speed at the end."*
* [Specialized actions](#sec-dm-actions-specialized-actions)  
  Specialized actions have additional arguments to create single-purpose actions.  
  Each specialized action reflects a commonly used behavior in scenario description.
  This improves readability.  
  Example: *"Reach high speed and later reach a lower speed."*

These two styles are facets of the same language and methodology can be mixed in the same scenario.

As the behavior of specialized actions is defined in the domain model they are less flexible and less extendable than generic actions.
However, this also means that specialized actions offer significantly easier readability and more clearly communicate an author’s intent.

The benefits of the generic style are:

* A wider set of concrete instances can result from the same action invocation.
* More options for tuning the behavior are available.
* Non-intrusive extension is allowed.  
  It is possible to extend an already existing scenario and non-intrusively tune it.
  Example: Users have specified a drive action at a certain speed.
  Later on, they wish to tune the scenario to drive fast at the beginning and slow later on.
  In the fragmented style, such enhancement is impossible.
  In the descriptive style, this translates into an extension with a modifier asking for the needed speeds at the beginning or at the end.

Actions are structs with unique semantics.
As such, any legal struct member can be an action or a scenario member.

### 8.4.6.1 Generic actions

The following snippet describes the parallel behavior of two vehicles.
The drive action for the two vehicles is called with the speed and position modifiers:

Code 56. Generic actions

```
scenario my_scenario:
    do parallel:
        d1: vehicle1.drive() with:
            speed([50kph..120kph])
        d2: vehicle2.drive() with:
             position(distance: [5m..100m], behind: vehicle1, at: start)
             position(distance: [5m..15m], ahead_of: vehicle1, at: end)
```

This code calls the drive action for the two vehicles and uses domain-model modifiers to express how to drive.

Available modifiers to describe the desired drive are:

* speed
* position
* distance
* lane

The values can be in absolute or relative terms, for example, position in absolute term or relative to another actor.

The values can be applied at the beginning, at the end, or throughout the phase, for example, start the drive action at the speed of 10 to 20 kph and finish at the speed of 40 to 60 kph.

This style uses a natural language to simplify scenario description by using a limited set of domain model modifiers.
User-defined modifiers for different purposes can be added on top of these for both generic and specialized actions.

### 8.4.6.2 Specialized actions

A specialized action is a wrapper for an underlying generic action and various constraints.
These constraints serve to restrict the generic action to the behavior expected of the specialized action.
Each scenario invocation of a specialized action thus activates the underlying generic action.

Code 57. Specialized actions

```
scenario my_scenario:
    do parallel:
        d1: vehicle1.reach_speed(5kph)
        d2: vehicle2.reach_speed(10kph)
```

The example shows specialized actions that abstract away the full API of the standard, lowering the barrier of entry to scenario authoring.

### 8.4.6.3 Action implementation

The generic actions and the specialized actions can be mixed because of the domain model implementation point of view:
The specialized actions are wrappers of the generic actions.
These wrappers expose a subset of the APIs.
The implementation wrapper is published to allow users to layer constraints and even use modifiers on top of the wrapped generic actions.

The following is an implementation example of the `reach_speed` specialized action:

Code 58. Action implementation

```
scenario vehicle.reach_speed:
        speed: speed
        do drive() with: speed(speed, at: end)
```

Note that the specialized actions are carefully selected to optimize the number of standard actions.
If users wish to create their own scenario actions, they can use the ASAM OpenSCENARIO language to achieve this.

To express that a vehicle should reach a speed and change lanes at the same time, users need to parallelize the request on the same actor.

Code 59. Parallel action implementation

```
scenario my_scenario:
    v1: vehicle
    do parallel:
        v1.reach_speed(5kph)
        v1.target_lane(2)
```

Note that in such situations two drive actions are invoked.
This is similar to the defined behavior of the generic actions.
An ASAM OpenSCENARIO tool should identify that the drive directives are on the same instance, and create the desired effect of both reaching the speed and changing the lane.

Using the generic actions is similar to the previous one:

Code 60. Generic action implementation

```
scenario my_scenario:
    v1: vehicle
    do v1.drive() with:
            speed(5kph, at: end)
            lane(2, at: end)
```