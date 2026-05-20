# ASAM Openscenario Dsl v2.2.0 — 9.3 Extending the domain model

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/user-guide/extending_the_domain_model.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.3 Extending the domain model

## 9.3.1 Introduction

ASAM OpenSCENARIO allows users to *extend* the normative domain model using the *extension mechanism*.

The extension mechanism allows to:

* Define actors and actions from scratch.
* Tune the normative domain model to project needs.
* Map the ASAM OpenSCENARIO domain model to other existing standards or commercial domain models.

The extension mechanism is defined in [Section 7.3.9, "Extension"](../language-reference/types.html#sec-lc-extension).

This document discusses *possible extensions and adjustments* that can be made through the extension mechanism.

## 9.3.2 ASAM OpenSCENARIO extension features

The ASAM OpenSCENARIO language provides multiple features for extensions and adjustments.

Users can use one of the following programming paradigms:

* *Aspect Oriented Programming (AOP)*  
  AOP allows adding any struct member to extend structs without introducing new type names.
  Note that you can also extend enumerated types to include new values.
* *Object Oriented Programming (OOP)*  
  OOP with traditional inheritance allows the introduction of a new struct name to the type system.
  This is done by deriving (also called *inheriting*) the new name from an existing one.

With the extension mechanism, users can define or extend actions, actors, and structs to add specific members.

Typical reasons for extending the domain model are:

* Layering constraints to add an ODD or a test constraint to steer the desired generated values and probabilities to explore unvisited areas or to match a specific distribution
* Adding fields for controlling or monitoring purposes
* Adding new or overriding existing coverage definitions
* Adding or tuning checkers
* Extending the definition of an enumerated type to include another value

The domain model pre-provided structs and types can be extended as any user-defined type using the ASAM OpenSCENARIO language capabilities.
The following guidelines show how to extend the ASAM OpenSCENARIO domain model for specific purposes.

## 9.3.3 Adding a new behavior

Primitive behaviors are implemented in ASAM OpenSCENARIO using actions.
Actions can be executed or observed in a scenario.

If you need to activate or observe a new behavior or automation function as part of your development and V&V process, you can add and use that new behavior or function.

### 9.3.3.1 Recommended process

The following process is recommended for adding new behaviors:

1. Identify the container actor.
2. Check the ASAM OpenSCENARIO domain model, to see if one of the existing actors matches your needs.  
   For example, if you want to make an entity of type person jump, you can extend the actor `person` and add a `jump` action to it.
3. If no actor matches your needs, define a new actor.  
   For example, if you want to make a horse gallop across the road, define a new actor `horse` and associate the `gallop` action to it.
4. Add the needed action to the actor.

### 9.3.3.2 Examples

#### 9.3.3.2.1 Adding an action to an existing standard actor

The following example adds the action `jump` to the existing actor `person`.

Code 87. Extending person with jump

```
extend person:
    age: uint with:
        keep(it in [1..120])

    action jump:
        height: length
        jump_num: uint with:
            keep(it in [1..5])
        keep(age > 60 => height < 0.1m)
```

**Comments:**

* A constraint was added between the new jump scenario and the age.
* Note that all person actors and derivatives have an `age` attribute, which is randomized now.
* Connecting the abstract action to the execution platform (meaning implementing or observing the jump) is implementation-specific and outside of the scope of the ASAM OpenSCENARIO standard.

#### 9.3.3.2.2 Adding an action to activate the ACC function

This example demonstrates how an action sets a state variable.
Conditions are, that the ACC automation function can be activated or deactivated at a certain cruising speed.

Code 88. Extending actor `vehicle` to request ACC-mode in different speeds

```
extend vehicle:
    action request_acc_mode:
        cruise_speed: speed
        turn_on: bool
```

#### 9.3.3.2.3 Adding a new actor

A horse is not part of the ASAM OpenSCENARIO domain model.
In this example, a new actor for a horse is created.
It makes sense to derive a horse from animal.

Code 89. Adding a horse actor with a gallop action

```
actor horse: animal:
    scenario gallop:
        speed: speed
```

#### 9.3.3.2.4 Using conditional inheritance

ASAM OpenSCENARIO allows extending a struct under certain conditions.
For example, you may want to add a boolean `siren` field to entities of type emergency vehicle.
The following code demonstrates how to do this.

Code 90. Conditionally adding a siren field

```
actor vehicle:
    is_emergency: bool  #each vehicle can be an emergency or not

actor emergency_vehicle: vehicle(is_emergency:true):
    siren: bool
```

**Comments:**

* The actor `emergency_vehicle` is defined to be a `vehicle`.
  Its value `vehicle_category` is `emergency`.
  `emergency_vehicle` inherits all `vehicle` attributes with the addition of a `siren` boolean field.
* Note that randomizing a vehicle may generate an emergency vehicle, which in turn has a siren field that is randomly turned on or off.

### 9.3.3.3 Extending an existing struct

Often users do not need a brand-new actor or action.
They only want to extend existing entities with new struct members, such as a new field, constraint, cover point, event, and so on.

The following example demonstrates these capabilities.

Code 91. Adding a struct member to an existing struct

```
enum size: [small, medium, large]

extend vehicle:
    my_size: size          # field extension
    keep (speed < 60kph)   # layer a constraint

    event stopped          # add an event
```

#### 9.3.3.3.1 Extending enumerated types

ASAM OpenSCENARIO allows the extension of enumerated types.
This may affect all structs that contain a field of that type.
For example, if a new car model is defined, both generation and coverage automatically adjusts to contain the new added car model.

Assume the following definition:

```
type size: [small, medium, large]

actor vehicle;
    my_size: size   # size can be either small, medium, or large
```

To add another option of the vehicle, in this case the vehicle should also be huge, you can extend the enumerated type as follows:

```
extend size: [huge]
```

The base definition with the extension is equivalent to the following code:

```
enum size: [small, medium, large, huge]

actor vehicle;
    my_size: size   # can be small, medium, large, huge
```

#### 9.3.3.3.2 An example for extending

Create a `reach_acceleration` action that gets a vehicle to a certain acceleration.
The following example achieves the desired result.

Code 92. Extend an actor with `reach_acceleration`

```
scenario vehicle.reach_acceleration:
        target_acceleration: acceleration

        do drive() with:
            acceleration(target_acceleration, at: end)
```

Once this code is loaded into an OpenSCENARIO tool, a new `reach_acceleration` specialized action is available and can be used in any user scenario.

|  |  |
| --- | --- |
|  | This simple example triggers a single drive action. Users may create more sophisticated compositions for more complicated maneuvers using composition of other actions and scenarios. |

## 9.3.4 Extending the Abstract Road network

The modifiers explained in  [Section 8.5, "Abstract road network"](../domain-model/dm_abstract_road_network.html#top-dm-road-introduction) help users build certain parts of a route of a road network. This section provides an example of how these can be further extended.

### 9.3.4.1 An example of extending a crossing

A potential addition to a crossing that allows for `start_line` and `end_line` in addition to `start_lane` and `end_lane`.

Suggestion: Allow for `start_line` and `end_line` to also be used to define crossings, since all a lane is to `crossing_connects()` is a centerline of the lane.

Future definition: A crossing is an overlay or virtual path that acts as a route and has a direct relationship to lanes or lines made with `free_space_points`.

When a crossing is a route, it may also be used in the following way with four instances of `route_point` that form two straight lines:

Any straight line could be used as a starting line and ending line just like a `start_lane` and `end_lane`.

However, geometry is still reserved for future implementation.
The following description does not create an accurate definition for the creation of a line from points.

* The origin of a crossing for s-coordinates is determined from a lane centerline and s-position along that line.  
  However, its origin can also originate along a line defined by two free space points.
* The `start_lane` assigns which lane starts the crossing.  
  Alternatively, `start_line` assigns which line starts the crossing.
* The `end_lane` assigns which lane completes the crossing.  
  Alternatively, `end_line` assigns which line completes the crossing.
* In the case of straight line geometry, the crossing ends at the natural connection with the centerline of the end lane or a line defined by two free-space points.

```
map: map
free_space_line1: list of route_point = [point1, point2]
sidewalk1: lane
crossing1: crossing with:
    keep(it.width == 3.5m)

map.crossing_connects(crossing1,
                  start_line: free_space_line1,
                  end_lane: sidewalk1,
                  start_s_coord: 5m,
                  start_angle: 90deg)
```

![Crossing with line from free space points](_images/dm_crossing_with_line_from_freespace_points.png)

Figure 27. Crossing with line from free space points

|  |  |
| --- | --- |
|  | The red dot is the origin on the `start_line` and the blue dot is an `end_point` in `end_lane`. |

A crossing may also be specified with a specific `start_angle`:

```
map: map
free_space_line1: list of free_space_point = [point1, point2]
free_space_line2: list of free_space_point = [point3, point4]
crossing1: crossing with:
    keep(it.width == 3.5m)

map.crossing_connects(crossing1,
                    start_line: free_space_line1,
                    end_line: free_space_line2,
                    start_s_coordinate: 5m,
                    start_angle: 85deg)
```

![Picture of crossing with specified start_angle](_images/dm_crossing_with_start_angle.png)

Figure 28. Picture of crossing with specified start\_angle

## 9.3.5 Mapping to other languages and domain models

Today, the automotive industry uses multiple languages and domain models to describe scenarios, actors, and actions.
These languages and domain models are either proprietary or inconsistent to one another and not standardized.

The domain model of ASAM OpenSCENARIO contains generic and specialized actions:

* The *generic actions* provide a flexible mechanism to describe a rich set of scenarios.
* The *specialized actions* are a simplified interface for a few of the commonly used actions.

Users can also add specialized actions to map the ASAM OpenSCENARIO domain model into existing commercial or proprietary solutions.