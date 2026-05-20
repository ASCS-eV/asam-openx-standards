# ASAM OpenSCENARIO® DSL v2.2.0 — 8.6 Behavioral model

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/dm_behavioral_model.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.6 Behavioral model

## 8.6.1 Overview

This chapter explains the main qualities of behavioral models.

The key functionality of behavioral models is to connect the scenario description with external assets that are dynamically involved during the execution of the scenario.

Once a scenario has been described in ASAM OpenSCENARIO, an implementation should be able to execute the scenario.
For such execution, the behavioral characteristics of each actor must be realized.
This can be achieved by using models in simulation, with real hardware, or as a combination of both.
A scenario could be executed in various ways, including but not limited to:

* In a simulation, using simple kinematic models
* In a simulation, using complex dynamic models
* With a human driver in a driving simulator
* On a closed proving ground with real vehicles

In any of these cases, there are behavioral aspects of the scenario actors that are implementation-specific and therefore fall beyond the scope of ASAM OpenSCENARIO.
But sometimes it may be practical, or even essential, to include some of these characteristics in the scenario description.

ASAM OpenSCENARIO behavioral models allow users to connect their scenario description to implementation-specific details that influence actor behavior.
Some possible use cases of behavioral models include but are not limited to:

* Select a dynamic model to realize the behavioral characteristics of an actor.
* Adjust the parameters of a dynamic model used in scenario simulation.
* Assign external modules to control the motion of an actor.
* Expose internal signals of an actor implementation to use them in the scenario description.

### 8.6.1.1 Key characteristics

* All physical actors have behavioral models.

  + Note that such a behavioral model can either refer to the dynamic model that implements the behavior of an actor, to a controller that guides an actor to execute the scenario instructions, or a combination of both.
  + Therefore, a fully-controlled behavioral model is also considered a behavioral model.
* All behavioral models are implementation-specific.
* Each actor can be assigned a behavioral model that is initialized by the initial\_bm parameter.

  + The `initial_bm` field can be set using constraints, or it may be left unspecified by the user.
  + The default value is implementation-specific.
    It supports most of the behavior modifiers as specified.
  + Individual fields inside the `initial_bm` can also be changed using user-defined methods.
  + It is recommended that the initial behavioral model of actor is specified by the definition of actor.
  + If no behavioral model is specified, the language compiler has no influence on behavioral model.
    The behavioral model of an actor can be implicitly set by the simulator.
* Behavioral model can also be set or modified during scenario execution through `set_bm(<new-bm>)` method.

  + Note that this type of modification is only possible if the simulator allows changes to the behavioral model during scenario execution.
  + Note that `set_bm(<new-bm>)` does not impact the `initial_bm`.
* The behavioral model for a vehicle could have parameters influencing the behavior of the vehicle.
  For example:

  + Driver aggressiveness, or other user-defined driver attributes
  + Tire properties, or other attributes affecting the dynamic response of the vehicle
  + Sub-objects (see [Section 8.6.2, “Data structures”](#sec-dm-behavioral-model-data-structures))
  + The parameters of the behavioral model are randomized within the defined constraints.

The following information is not contained in the behavioral model:

* The motion states (position, speed, acceleration) of the actor.
  These are part of the standard ASAM OpenSCENARIO domain model.

## 8.6.2 Data structures

### 8.6.2.1 Defining a specific behavioral model

An ASAM OpenSCENARIO behavioral model is a struct that can be expanded by the user.

Code 62. Behavioral models struct

```
struct behavioral_model:
    bm_engine: bm_engine  # Reference to the "behavioral model engine"
```

Based on this base `behavioral_model` class, users are free to define their own classes by inheriting from it.

Code 63. User-defined behavioral model classes

```
struct vehicle_bm inherits behavioral_model:
    # More fields defined by the users...

struct fully_controlled_vehicle_bm inherits vehicle_bm:
    # More fields defined by the users...
```

How to define a specific new behavioral model:

Code 64. Specifying a new behavioral model

```
struct sumo_idm_bm inherits behavioral_model:
    tau: time
    # More fields defined by the users...
```

### 8.6.2.2 Behavioral model engine

Behavioral models have a reference to their behavioral model engine.

* The behavioral model engine provides the actual implementation of the behavioral model.
* The `bm_engine` field is a reference to the ASAM OpenSCENARIO object representing the `bm_engine`, whose content is implementation-specific.
* An example is `keep(my_bm.bm_engine == bm_engines.sumo_bm_engine_object)`.

### 8.6.2.3 Splitting into sub-structs

You can split the `vehicle_bm` into multiple sub-structs.

Please note that the following code is just an example.
The ASAM OpenSCENARIO domain model does not define an obligatory structure of `vehicle_bm`.

Code 65. Splitting into sub-structs

```
da_model, lld_model, sb_model, lc_model: behavioral_model

struct vehicle_bm inherits behavioral_model

extend vehicle_bm:
    driver_like_attributes: da_model
    low_level_dynamics: lld_model
    signaling_behavior: sb_model
    lateral_controller: lc_model
```

These sub-structs could refer to aspects of the behavioral model.
Users and implementers are free to define the structure and functionality that suits their particular needs.

Even if the behavioral model is split into sub-structs, they are still encapsulated within a single behavioral model object.
Because of that, the user can set the behavioral model using a single constraint or action (see [Section 8.6.3, “Examples”](#sec-dm-behavioral-model-examples)).

## 8.6.3 Examples

### 8.6.3.1. Using `initial_bm` and `set_bm()`

This example changes the whole behavioral model of v2 at once.

Code 66. Changing the behavioral model for a vehicle

```
scenario top.foo:
    my_sumo_bm: sumo_idm_bm with:
        keep(tau == 2.2s)
    my_sumo_bm_2: sumo_idm_bm with:
        keep(tau == 3.0s)

    car: vehicle with:
        keep(initial_bm == my_sumo_bm)
                   # This is the initial BM for v2
    do serial:
        car.drive() # Using the initial BM my_sumo_bm
        car.set_bm(my_sumo_bm_2) # Change the BM for my_sumo_bm_2
        car.drive() # Using the new BM
```

### 8.6.3.2. Using specific `set_bm` methods

Sometimes you may want to change just a single field of the behavioral model, like the `signaling_behavior` sub-struct or even just the `signaling_behavior.avoid_signaling` fields.

This is possible because of specific `set_bm_*()` methods for the different fields.

Now you can change the previous example:

Code 67. Without set\_bm method

```
v2.set_bm(my_sumo_bm_2) # Change the BM for v2
```

Code 68. With set\_bm method

```
v2.set_bm_avoid_signaling(true)  # Set that specific field to true
```

You can also use `v2.set_bm_signaling_behavior()` to set the whole struct.
This replaces either the previous value of the struct or the null value that was there before.

### 8.6.3.3 Vehicles in a vehicle group

This is how the behavioral model for vehicles in a vehicle group can be set.

Code 69. Vehicles in a vehicle group

```
g: vehicle_group
for c in g.cars:
     keep(c.initial_bm == my_bm)
```

### 8.6.3.4 Motion controller

This is how a user can set a behavioral model to establish the status of longitudinal and lateral motion control for an actor.

Code 70. Motion controller

```
motion_control inherits behavioral_model:
    longitudinal: bool
    lateral: bool

my_controller: motion_control with:
    keep(longitudinal == True)
    keep(lateral == True)

my_controlled_car: vehicle with:
    keep(initial_bm == my_controller)
```

### 8.6.3.5 Assistive device

This is how the behavioral model for vehicles in a vehicle group can be set.

Code 71. Randomized behavioral model

```
adas_device inherits behavioral_model:
    driver_setting: enum[off, on]
    current_status: enum[off, standby, engaged]

my_adas: adas_device

adas_car: vehicle with:
    keep(initial_bm == my_adas)

do serial:
    adas_car.set_bm_driver_setting(off)
    adas_car.drive()
    adas_car.set_bm_driver_setting(on)
    adas_car.drive()
```

### 8.6.3.6 Randomization of behavioral model

This example illustrates how the randomization of behavioral models is restrained.
After the randomization the parameters of the behavioral models of the actors are the same, as they are initialized with the same instance.

```
struct vehicle_bm inherits behavioral_model:

veh1: vehicle with:
    keep(initial_bm == vehicle_bm)
veh2: vehicle with:
    keep(initial_bm == vehicle_bm)
```

Alternatively, two independent behavioral models of the same type can be assigned to actors.

```
bm_1: vehicle_bm
bm_2: vehicle_bm

veh1: vehicle with:
    keep(initial_bm == bm_1)
veh2: vehicle with:
    keep(initial_bm == bm_2)
```

In this case the parametrization of 'vehicle\_bm' is independently randomized for `veh1` and `veh2`, although the behavioral model is of the same type.