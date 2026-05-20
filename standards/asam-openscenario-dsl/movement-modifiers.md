# ASAM OpenSCENARIO® DSL v2.2.0 — 8.9 Movement modifiers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/movement-modifiers.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.9 Movement modifiers

## 8.9.1 Modifiers for movement actions

The movement of physical objects, including vehicles and pedestrians, is specified using *movement actions*.
These actions can be tuned with the use of *movement modifiers*.
These modifiers can be applied to either the generic movement actions, like `move()`, `drive()`, or `walk()`, or to the specialized movement actions, like `change_speed()`, `change_lane()`, and so on.
Users are free to combine modifiers and actions, as long as the combination provides a consistent set of constraints for the actor behavior.
These modifiers shall appear either as members of other action modifiers or as members of a movement action after `with`.

Code 75. Modifier drive() with speed value

```
do serial:
   vehicle1.drive() with:
       speed([30kph..70kph])
```

Code 76. Modifier follow\_lane() with position and speed constraints

```
do serial:
    vehicle2.follow_lane(offset: 0.375m, target: lane2) with:
        position(1m, ahead_of: ego_vehicle, at: start)
        speed(60kph)
```

Some parameters can be passed by order, meaning without the parameter name.
If no arguments are passed, the defaults are applied.

The following three invocations of `lane()` are supported and have the same effect:

Code 77. Different kinds of passing parameters

```
   lane(lane: 1)
   lane(1)
   lane()
```

### 8.9.1.1 Common parameters

The following parameters are common to all domain model movement modifiers.

#### 8.9.1.1.1. Parameter `at`

All movement modifiers have an optional parameter `at` with the following possible values:

* `all`  
  This constraint holds throughout this phase (default).
* `start`  
  This constraint holds at the start of the phase.
* `end`  
  This constraint holds at the end of the phase.

#### 8.9.1.1.2. Parameter `movement_mode`

The parameter `movement_mode` has the following values:

* `monotonous`  
  This movement mode adheres to the laws of physics.
  On top of that it limits the level of surprise that a movement may have.
* `other`  
  Not necessarily monotonous.
  This is the default.

#### 8.9.1.1.3. Parameter `track`

* `track`  
  Actual or projected.
  The default is actual, meaning that the vehicle reacts to the behavior of the referenced vehicle.

#### 8.9.1.1.4. Parameter `shape`

* `shape`  
  A shape struct is an object that contains a `duration()` and a `compute()` method, plus a set of parameters that allow users to shape the way a state variable (like lateral position, speed or acceleration) changes during an action/modifier invocation.
  The `duration()` method returns the time duration of the shape.
  The `compute()` method returns concrete values for the relevant state variable as a function of time.

The following is a typical use of a shape struct.

Code 78. Shape

```
scenario my_scenario:
    spd_shape: common_speed_shape with:
        keep(it.target == 50kph)
        keep(it.rate_profile == smooth)
        keep(it.rate_peak == 5mpsps)
    v1: vehicle

    do serial:
       v1.drive() with:
           speed(shape: spd_shape)
```

The example below exhibits the same behavior as the example above.
Note that, in general, the shape’s *target* parameter may overlap with `at: end` constraints introduced in the modifier.
In this case, the shape’s *target* parameter can be taken from the speed modifier.
However, to avoid confusion or contradictions, it is suggested to create shape struct instances that are fully defined.

Code 79. Shape with target parameter from speed modifier

```
scenario my_scenario:
    spd_shape: common_speed_shape with:
        keep(it.rate_profile == smooth)
        keep(it.rate_peak == 5mpsps)
    v1: vehicle

    do serial:
       v1.drive() with:
           speed(50kph, at: end, shape: spd_shape)
```

This shape example causes the vehicle `v1` to drive with *50 kph*.
This speed is achieved with a *smooth* acceleration profile with a peak acceleration of *5 mpsps*, as specified by the *rate\_profile* and *rate\_peak* parameters.

A set of built-in shape objects is provided in ASAM OpenSCENARIO.
Users can extend these built-in shape objects with their own desired shape objects.

Note that using the shape structs specifies the exact values for certain state variables (or their derivatives) throughout the corresponding action execution.
This can limit the degrees of freedom of the actor during the action execution and could have strict implications on other scenario attributes.
For example, when using a shape struct on a speed modifier, this will also constrain the acceleration attributes of the actor.
Be careful not to use excessive shape attributes on the modifier that may restrict the generated movements, unless this is your goal.

For more information on shape objects please read the shape object description below.

### 8.9.1.2 Shape object description

The shape structs are a way to describe the behavior of a state variable as a function of time within a modifier invocation, enabling a fine-grained control of the actor’s maneuver.
`any_shape` is the base struct of the shape hierarchy, thus any user-defined shape structs should inherit from `any_shape` or one of its children.
`any_shape` contains the `duration()` function which returns the time duration of that shape.

Concrete shape types implement their shape `compute()` function which gets a time argument and returns the corresponding value of the state variable that is modified by the shape.
The time is measured from the start of the scenario phase that invokes the modifier.

Specific shape objects can have additional arbitrary attributes.

The shape hierarchy definition is as follows:

```
struct any_shape:
    def duration() -> time is undefined

struct any_acceleration_shape inherits any_shape:
    def compute(time: time) -> acceleration is undefined

struct any_speed_shape inherits any_shape:
    def compute(time: time) -> speed is undefined

struct any_position_shape inherits any_shape:
    def compute(time: time) -> length is undefined

struct any_lateral_shape inherits any_shape:
    def compute(time: time) -> length is undefined
```

ASAM OpenSCENARIO also provides predefined shapes for common maneuvers.
The common shapes include a `target` parameter for the relevant state variable, as well as two parameters related to the first derivative of the state.
The `rate_profile` parameter indicates the type of `dynamic_profile` for the first derivative of the state.
The `rate_peak` parameter is the peak value that must be reached by the first derivative of the state during the maneuver.
These parameters provide a complete set of constraints to resolve the target shape of the state (as a function of time) that should be achieved during execution of the action.

Code 80. Built-in common shapes

```
struct common_acceleration_shape inherits any_acceleration_shape:
    rate_profile: dynamic_profile
    rate_peak: jerk
    target: acceleration

struct common_speed_shape inherits any_speed_shape:
    rate_profile: dynamic_profile
    rate_peak: acceleration
    target: speed

struct common_position_shape inherits any_position_shape:
    rate_profile: dynamic_profile
    rate_peak: speed
    target: length

struct common_lateral_shape inherits any_lateral_shape:
    rate_profile: dynamic_profile
    rate_peak: speed
    target: length
```

Users and implementers can extend the domain model and create their own shape structs with additional parameters to solve specific functional forms or sets of constraints for the shape of the state variable trajectory.

### 8.9.1.3 Absolute or relative movement modifiers

The scenario modifiers that set a speed, position, or lane can be either absolute or relative.

Code 81. Absolute and relative speed modifiers

```
position([10m..20m], at: start) # Absolute distance from the start of the path
speed([10kph..15kph], faster_than: vehicle1) # Relative with additive constant
speed([10kph..15kph], faster_than: vehicle1, factor: 1.1) # Relative with additive constant and multiplicative factor
lane(same_as: vehicle1) # Relative
```

The relative versions require two vehicles moving in parallel.
They may also have multiple parameters such as `faster_than` and `slower_than`, but at most you can specify one.
These two constraints are checked at compile time.
These modifiers have a `track` parameter that specifies whether the vehicle reacts to the actual behavior of the referenced vehicle or to its expected behavior.
By default, the vehicle reacts to the actual behavior of the referenced vehicle, but there may be cases where the referenced vehicle behaves in ways that you want the vehicle to ignore.
In those cases, you can require the vehicle to track the projected behavior of the referenced vehicle.
For example, consider the `l2: lane()` and the `p2: position()` modifiers in `phase2` of the following scenario.

Code 82. Movement modifiers

```
do serial():
    phase1: parallel(duration: [1.5s..3s]):
        d1: dut.vehicle.drive()
        d2: vehicle1.drive()
    phase2: parallel(duration: [1.5s..3s]):
        d3: dut.vehicle.drive()
        d4: vehicle1.drive() with:
            speed(speed: [30kph..200kph])
            l1: lane(side_of: dut.vehicle, at: start)
            p1: position(time: [0.5s..1s], ahead_of: dut.vehicle, at: start)
            l2: lane(same_as: dut.vehicle, at: end)
            p2: position(time: [1.5s..2s], ahead_of: dut.vehicle, at: end)
```

Because of these modifiers, at the end of `phase2` the following happens:

* `vehicle1` ends on the same lane as the ego, even if the ego has changed lanes.
* `vehicle1` ends ahead of the ego, even if it has accelerated.

This behavior may be exactly what is intended.
But maybe the following is intended:

* `vehicle1` ends in the lane where the ego was at the start of `p2`.
* `vehicle1` ends `[1.5s..2s]` seconds ahead of where the ego would have been, if it had continued at the same speed it was at the start of `p2`.

In this case, change the last two lines to:

Code 83. Adapting behavior

```
l2: lane(same_as: dut.vehicle, at: end, track: projected)
p2: position(time: [1.5s..2s], ahead_of: dut.vehicle, at: end, track: projected)
```

|  |  |
| --- | --- |
|  | Negative distance values are allowed and mean "going to the other side". |

Code 84. Negative distance values

```
lateral(distance: -2m, side: left)
```

The example shows being two meters to the right.

### 8.9.1.4. Range-typed vs scalar parameters

Some movement modifiers have range-valued parameters; the `speed()` modifier, for example, has the parameter `speed_range` in addition to the parameter `speed`. `speed_range` here is the range-valued counterpart to the scalar-valued `speed` parameter.

A scalar parameter represents a single value of a movement property — for instance, a specific speed that should be maintained for the entire duration of the movement action.

A range-typed parameter, in contrast, specifies an interval of permissible values within which a movement property shall remain — for example, a range of acceptable speeds during the movement action.

The following examples highlight the difference.

In the first example, the `speed` parameter is constrained with a range.
This means that one speed value within the specified range is selected through constraint resolution, and vehicle1 shall then maintain this value for the entire duration of the `drive()` movement action.

Code 85. Modifier drive() with a value specified for the scalar speed parameter

```
do serial:
   vehicle1.drive() with:
       speed(speed : [30kph..70kph])
```

In the second example, the range-typed parameter `speed_range` is used instead.
Here, `vehicle1` may continuously vary its speed within the specified range during the execution of the drive() movement action.
The range therefore defines the allowed interval of values for the movement property over time, rather than fixing it to a single constant value.
The specific method of how the values of the movement property vary is implementation-defined.

Code 86. Modifier drive() with a value specified for the range-typed speed\_range parameter

```
do serial:
   vehicle1.drive() with:
       speed(speed_range : [30kph..70kph])
```

Modifiers that have range-valued counterparts for scalar parameters require that at most one of them is used within an invocation of that modifier.

Using a range-valued parameter with `at: start` or `at: end` effectively constrains the state variable to the specified interval at a single discrete point in time.
This is equivalent to applying a range constraint to the corresponding scalar-valued parameter, except that the value being chosen is selected by the action, rather than constraint resolution.
The full expressive potential of range-valued parameters is leveraged when used with `at: all`, where they define a continuous admissible parameter space for the movement property over the entire temporal extent of the behavior.

## 8.9.2 Modifier position()

Purpose
:   Set the position of an actor along the s-coordinate of the road that the related actors are located on.

Category
:   Scenario modifier

Usage
:   Code 87. Position modifier

    ```
    position(distance: length | time: time
    | distance_range: range of length
    | time_range : range of time
    [, ahead_of: physical_object | behind: physical_object]
    [, <standard-movement-parameters>])

    position(distance: length | time: time,
    | distance_range: range of length
    | time_range : range of time
    [ahead_of_point: position_3d | behind_point: position_3d]
    [, <standard-movement-parameters>])

    position(at_point: position_3d, project_on_route: bool
    [, <standard-movement-parameters>])
    ```

Parameters
:   * `distance`  
      A target `length` value including a length unit.
      The distance is calculated using the route-based s-coordinate.
      It is mandatory to include one (and only one) of `distance` or `time` or `distance_range` or `time_range` or `at_point` arguments.
    * `time`  
      A target `time` value with a time unit to determine headway time between the actor and a movable object or point.
      It is mandatory to include one (and only one) of `distance` or `time` or `distance_range` or `time_range` or `at_point` arguments.
    * `ahead_of`  
      When ahead\_of is specified, the actor must be ahead of the physical\_object by the specified value using road coordinates.
    * `behind`  
      When behind is specified, the actor shall be behind the physical\_object by the specified value.
    * `ahead_of_point`  
      When ahead\_of\_point is specified, the actor shall be ahead of the specified point.
      By default, the projected route.
    * `behind_point`  
      When behind\_point is specified, the actor shall be ahead of the specified point.
      By default, the projected route.
    * `at_point`  
      When at\_point is specified, the actor must be at the specified point.
    * `project_on_route`  
      This option is relevant only if `at_point` is specified.
      If true (the default), project the point on the route of the actor as the reference point.
      If false, use the actual point.
      In all other cases (not using `at_point`), the `distance` or `time` values shall be projected on the road.
      If the point cannot be uniquely projected on the road (for example, the road ends before reaching this point), an error should be issued.
    * `<standard-movement-parameters>`  
      A set of parameters that are relevant for most movement modifiers.
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).
    * `distance_range`  
      A range of `length` values. Specifies an admissible interval for the actor’s position along the route (s-coordinate).
      It is mandatory to include one (and only one) of `distance` or `time` or `distance_range` or `time_range` or `at_point` arguments.
    * `time_range`  
      A range of `time` values with a time unit. Specifies an admissible interval for the time headway between the actor and a reference object or point.
      It is mandatory to include one (and only one) of `distance` or `time` or `distance_range` or `time_range` or `at_point` arguments.

Description
:   The `position()` modifier lets you specify the position of an actor relative to the start of the path or relative to another actor.

    You can specify the position either by distance or by time (but not both).
    Alternatively, you can define an admissible range for distance or time using the `distance_range` or `time_range` parameters,
    or specify the position directly via `at_point`.
    Exactly one of these five parameters shall be provided.

    When `ahead_of` is specified, the actor shall be ahead of vehicle by the specified value in the relevant period.
    `behind` contradicts `ahead_of`, so you cannot use them together.

    When `time` is specified along with `ahead_of` or `behind_of`, the physical distance is calculated using the speed of the vehicle that is behind (irrespective of whether it is the actor of the scenario or the referenced vehicle) and the location at that moment of the vehicle that is ahead.

    The speed of the vehicle that is ahead is not taken into the calculation.
    If the `at` parameter is *all*, the physical distance at any point in time refers to the speed of vehicle that is behind at that moment and the location of the vehicle that is ahead at that same moment (meaning that the physical distance may vary during the time period).

    The following two examples are equivalent.
    In both cases the physical distance is calculated according to the speed of vehicle2.

```
do parallel:
    vehicle1.drive() with:
        speed(speed: 30kph, at: end)
    vehicle2.drive() with:
        speed(speed: 40kph, at: end)
        position(time: 3second, behind: vehicle1, at: end)

# is identical to:

do parallel:
    vehicle1.drive() with:
        speed(speed: 30kph, at: end)
        position(time: 3second, ahead_of: vehicle2, at: end)
    vehicle2.drive() with:
        speed(speed: 40kph, at: end)
```

Examples
:   Code 88. Position modifier

    ```
    do serial:
        vehicle1.drive() with:
            # Absolute from the start of the path:
            # Shall maintain a fixed distance between
            # 10m to 20m from the start of the path.
            # (Distance cannot vary.)
            position([10m..20m])

    do serial:
        vehicle1.drive() with:
            # Absolute from the start of the path:
            # Shall maintain a distance between 10m to 20m
            # from start of the path.
            # (Distane can vary.)
            position(distance_range : [10m..20m])

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # 40 meters ahead of vehicle1 at end
             position(40meter, ahead_of: vehicle1, at: end)

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # Behind vehicle1 throughout
            position([20m..30m], behind: vehicle1)

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # Behind vehicle1, measured by time
            # Shall maintain a fixed time headway between 2s..3s
            # (Time headway cannnot vary.)
            position(time: [2s..3s], behind: vehicle1)

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # Behind vehicle1, measured by time
            # Time headway can vary between 2s..3s
            position(time_range: [2s..3s], behind: vehicle1)
    ```

## 8.9.3 Modifier keep\_position()

Purpose
:   Maintain absolute position of the actor for the current period.

Category
:   Scenario modifier

Usage
:   Code 89. Keep position modifier

    ```
    keep_position()
    ```

    Modifier constraints are enforced during both planning and execution.

Example
:   Code 90. Keep position modifier

    ```
    do serial:
        vehicle1.drive() with:
            keep_position()
    ```

## 8.9.4 Modifier speed()

Purpose
:   Set the speed of an actor for the current period.

Category
:   Scenario modifier

Usage
:   Code 91. Speed modifier

    ```
    speed(speed: speed
    | speed_range: range of speed
    [, direction: lon_lat]
    [, <standard-movement-parameters>])

    speed(speed: speed
    | speed_range: range of speed
    [, faster_than: physical_object | slower_than: physical_object | same_as: physical_object]
    [, direction: lon_lat]
    [, <standard-movement-parameters>]
    [, factor: float])
    ```

Parameters
:   * `speed`  
      A target `speed` value, including a speed unit.
      It is mandatory to include one (and only one) of `speed` or `speed_range`.
    * `faster_than` | `slower_than` | `same_as`  
      Use one (and only one) of these arguments to set the speed target relative to another `physical_object`, such as a vehicle, person, or movable object.
      The relative speed is calculated by adding the `speed` or `speed_range` value(s) to the product of the speed of the `physical_object` and the `factor` argument.
    * `factor`  
      Provides a floating-point factor that is multiplied with the speed of the `physical_object`.
      Defaults to 1.
    * `direction`  
      Determines the direction of the controlled speed.
      The default value is longitudinal, which controls the speed state as defined in [`movable_object` states](entity.html#tab-trafficparticipant-entity-movable_object-states).
      When the value is lateral, this modifies the lateral speed.
    * `<standard-movement-parameters>`  
      A set of parameters that are relevant for most movement modifiers, such as `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).
    * `speed_range`  
      A range of `speed` values, each including a speed unit.
      Specifies an admissible interval for the actor’s speed.
      It is mandatory to include one (and only one) of `speed` or `speed_range`.

Description
:   The `speed()` modifier defines the longitudinal or lateral speed of an actor, either as an absolute value or relative to another `physical_object`.

You can specify the speed either by an exact `speed` or by an admissible interval using `speed_range` (but not both).
Exactly one of these two parameters shall be provided.

If `faster_than`, `slower_than`, or `same_as` are specified, the actor’s speed is defined relative to the referenced object, based on the given `speed` or `speed_range` and `factor` values.
The arguments `slower_than`, `faster_than`, and `same_as` contradict each other and cannot be used together.

Examples
:   Code 92. Speed modifier

    ```
    do serial:
        vehicle1.drive() with:
            # Absolute speed range:
            # The speed will be fixed at a value within 10-20 kph
            # for the duration of the modified behavior
            speed(speed: [10kph..20kph])

    do serial:
        vehicle1.drive() with:
            # Absolute speed range that can vary between 10–20 kph
            speed(speed_range: [10kph..20kph])

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # Faster than vehicle1 by a fixed offset within [1–5 kph]
            # The offset is chosen once and remains constant
            # for the duration of the modified behavior
            speed(speed: [1kph..5kph], faster_than: vehicle1)

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # Faster than vehicle1 by a speed that can vary between 1–5 kph
            speed(speed_range: [1kph..5kph], faster_than: vehicle1)

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # Faster than vehicle1 by 10%
            speed(speed: 0kph, faster_than: vehicle1, factor: 1.1)

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # Faster than vehicle1 by 10%, plus a variable range of 1–5 kph
            speed(speed_range: [1kph..5kph], faster_than: vehicle1, factor: 1.1)

    do serial:
        vehicle1.drive() with:
            # Have a speed of 5 kph at the end of the phase
            speed(5kph, at: end)

    do parallel:
        vehicle1.drive()
        vehicle2.drive() with:
            # Either slower or faster than vehicle1 by up to ±20 kph
            # (The speed offset may change within the given interval)
            speed(speed_range: [-20kph..20kph], faster_than: vehicle1)
    ```

## 8.9.5 Modifier change\_speed()

Purpose
:   Change the speed of the actor for the current period.
    (Unlike the `speed()` modifier, which sets an absolute target speed, this modifier specifies a change (increase or decrease) relative to the actor’s current speed.)

Category
:   Scenario modifier

Usage
:   Code 93. Change speed modifier

    ```
    change_speed(speed: speed
    | speed_range: range of speed
    [, <standard-movement-parameters>])
    ```

Parameters
:   * `speed`  
      A target speed change value, including a speed unit.
      The value represents the desired change relative to the actor’s current speed (e.g., `+10kph` to accelerate or `-10kph` to decelerate).
      It is mandatory to include one (and only one) of `speed` or `speed_range`.
    * `<standard-movement-parameters>`  
      A set of parameters that are relevant for most movement modifiers.
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).
    * `speed_range`  
      A range of speed change values with a speed unit.
      Specifies an admissible interval for how much the actor’s speed should change.
      It is mandatory to include one (and only one) of `speed` or `speed_range`.

Examples
:   Code 94. Change speed modifier

    ```
    do serial:
        vehicle1.drive() with:
            # The speed change will be a fixed delta chosen within -20..20 kph
            # and applied relative to the current speed.
            # The resulting value remains constant for the duration of the behavior.
            change_speed(speed: [-20kph..20kph])

    do serial:
        vehicle1.drive() with:
            # The speed change may vary within the range -20..20 kph
            # during the duration of the behavior.
            change_speed(speed_range: [-20kph..20kph])
    ```

## 8.9.6 Modifier keep\_speed()

Purpose
:   Maintain absolute speed of the actor for the current period.

Category
:   Scenario modifier

Usage
:   Code 95. Keep speed modifier

    ```
    keep_speed()
    ```

Example
:   Code 96. Keep speed modifier

    ```
    do serial:
        vehicle1.drive() with:
        keep_speed()
    ```

## 8.9.7 Modifier acceleration()

Purpose
:   Specify the rate of acceleration of an actor.

Category
:   Scenario modifier

Usage
:   Code 97. Acceleration modifier

    ```
    acceleration(acceleration: acceleration
    | acceleration_range: range of acceleration
    [, <standard-movement-parameters>])
    ```

Parameters
:   * `acceleration`  
      A target `acceleration` value, with an acceleration unit.
      It is mandatory to include one (and only one) of `acceleration` or `acceleration_range`.
    * `<standard-movement-parameters>`  
      A set of parameters that are relevant for most movement modifiers.  
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).
    * `acceleration_range`  
      A range of `acceleration` values with an acceleration unit.
      Specifies an admissible interval for the actor’s acceleration.
      It is mandatory to include one (and only one) of `acceleration` or `acceleration_range`.

Description
:   The `acceleration()` modifier defines the rate at which an actor changes its speed over time.
    You can specify either an exact acceleration or an admissible interval using `acceleration_range`, but not both.
    Exactly one of these two parameters shall be provided.

Examples
:   Code 98. Acceleration modifier

    ```
    # Accelerate at a constant rate of 5 kph per second
    do serial:
        vehicle1.drive() with:
            acceleration(5kphps)

    # Accelerate at a rate chosen within 3–6 kph per second,
    # fixed for the duration of the behavior.
    do serial:
        vehicle1.drive() with:
            acceleration(acceleration: [3kphps..6kphps])

    # Accelerate with a rate that may vary between 3–6 kph per second
    # throughout the behavior.
    do serial:
        vehicle1.drive() with:
            acceleration(acceleration_range: [3kphps..6kphps])
    ```

## 8.9.8 Modifier lateral()

Purpose
:   Set location inside the lane along the lateral axis using road coordinates (t-axis).

Category
:   Scenario modifier

Usage
:   Code 99. Lateral modifier

    ```
    lateral(distance: length
    | distance_range: range of length
    [, side_of: vehicle, side: side_left_right]
    [, measure_by: lat_measure_by]
    [, <standard-movement-parameters>])
    ```

Parameters
:   * `distance`  
      The offset from the reference line.
      It is mandatory to include one (and only one) of `distance` or `distance_range`.
    * `distance_range`  
      A range of `length` values specifying an admissible interval for the lateral offset from the reference line.
      It is mandatory to include one (and only one) of `distance` or `distance_range`.
    * `side_of`  
      The location relative to a specific vehicle.
    * `side`  
      Set the location on the left or on the right.
    * `measure_by`  
      This parameter specifies the measurement start and end points.  
      For example, measuring the distance from the left side of one vehicle to the right side of another vehicle.  
      See the enum `lat_measure_by` for possible values.
    * `<standard-movement-parameters>`  
      A set of parameters that are relevant for most movement modifiers.
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).

The `lateral()` modifier specifies an actor’s lateral position (t-coordinate) relative to the road or another actor.
You can define this position as an exact `distance` offset or as an admissible `distance_range`.
Exactly one of these two parameters shall be provided.

If a `distance_range` is specified, the actor’s lateral offset shall stay within the specified interval throughout the entire duration of the behavior.

Examples
:   Code 100. Lateral modifier

    ```
    do serial:
        vehicle1.drive() with:
            lateral(distance: 1.5meter, measure_by: right_to_right, at: start)
            # Maintain a lateral distance of 1.5 meters measured from the right side of the vehicle to the lane edge on the right.

    do serial:
        vehicle1.drive() with:
            lateral(distance: 1.5meter, side_of: v1, side: right, measure_by: right_to_left, at: start)
            # Maintain a lateral distance of 1.5 meters measured from the right side of the vehicle to the left side of v1.

    do serial:
        vehicle1.drive() with:
            lateral(distance_range: [1.0m..2.5m], measure_by: right_to_right)
            # Maintain a lateral offset of 1.0 and 2.5 meters measured from the right side of the vehicle to the lane edge on the right. The distance may vary between 1.0 and 2.5 meters throughout the behavior.
    ```

## 8.9.9 Modifier yaw()

Purpose
:   Set the yaw (rotation around the vertical axis) of the vehicle.

Category
:   Scenario modifier

Usage
:   Code 101. Yaw modifier

    ```
    yaw(angle: angle
    | angle_range: range of angle
    [, <standard-movement-parameters>])

    yaw(angle: angle
    | angle_range: range of angle
    [, relative_to: physical_object]
    [, measure_by: yaw_measure_by]
    [, <standard-movement-parameters>])
    ```

Parameters
:   * `angle`  
      A target angle value, including an angle unit.
      It is mandatory to include one (and only one) of `angle` or `angle_range`.
    * `angle_range`  
      A range of angle values with an angle unit.
      Specifies an admissible interval for the actor’s yaw angle.
      It is mandatory to include one (and only one) of `angle` or `angle_range`.
    * `relative_to`  
      A named instance of the vehicle actor.
    * `measure_by`  
      This option is relevant only if `relative_to` is specified.
      Defines reference lines of the actor and the referenced physical\_object, where width is the x-axis and long is the y-axis.

      Values include:

      + length\_to\_length
      + length\_to\_width
      + width\_to\_length
      + width\_to\_width
      + relative\_to\_north
      + relative\_to\_road (default)
    * `<standard-movement-parameters>`  
      A set of parameters that is relevant for most movement modifiers.  
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).

Description
:   The `yaw()` modifier specifies the orientation of the actor around its vertical axis, either absolutely or relative to another object.
    You can define this orientation as an exact `angle` value or as an admissible `angle_range`.
    Exactly one of these two parameters shall be provided.
    If an `angle_range` is specified, the actor’s yaw shall remain within the specified interval throughout the entire duration of the behavior.

Examples
:   Code 102. Yaw modifier

    ```
    # The angle between the y-axis of the actor (vehicle1) and the s-axis of the lane
    # is within [2..3] radians; the value is fixed for the duration of the behavior.
    do serial:
        vehicle1.drive() with:
            yaw(angle: [2rad..3rad])

    # The angle between the y-axis of the actor (vehicle1) and the s-axis of the lane
    # may vary between [2..3] radians throughout the behavior.
    do serial:
        vehicle1.drive() with:
            yaw(angle_range: [2rad..3rad])

    # The angle between the y-axis of the actor (vehicle1) and the y-axis of car1
    # may vary between [2..3] radians throughout the behavior.
    do serial:
        vehicle1.drive() with:
            yaw(angle_range: [2rad..3rad], relative_to: car1, measure_by: length_to_length)
    ```

## 8.9.10 Modifier orientation()

Purpose
:   Specify the orientation of an actor.

Category
:   Scenario modifier

Usage
:   Code 103. Orientation modifier

    ```
    orientation(yaw: angle  [, pitch: angle] [, roll: angle]
    [, relative_to: physical_object] [, measure_by: orientation_measured_by]
    [, <standard-movement-parameters>])

    orientation(pitch: angle  [, roll: angle] [, yaw: angle]
    [, relative_to: physical_object] [, measure_by: orientation_measured_by]
    [, <standard-movement-parameters>])

    orientation(roll: angle  [, yaw: angle] [, pitch: angle]
    [, relative_to: physical_object] [, measure_by: orientation_measured_by]
    [, <standard-movement-parameters>])
    ```

Parameters
:   `yaw`, `pitch`, `roll`  
    are angle values, including angle units.
    Include one, two or three of the angle arguments.

    `relative_to`  
    is the object relative to whom the angles will be measured.
    Optional argument, default is global coordinate system.

    `measure_by`  
    defines how to measure the desired orientation.
    Values include absolute, relative\_to\_reference, relative\_to\_road.
    Optional argument, default is relative\_to\_road.

    `<standard-movement-parameters>`  
    is a set of parameters that is relevant for most movement modifiers.
    For example, `at`.
    For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).

Example
:   Code 104. Orientation modifier

    ```
    # The angle between the x-axis of the actor and the s-axis of the lane is between 2 and 3 radians.
    do serial:
        vehicle1.drive() with:
            orientation(yaw: [2rad..3rad])

    # The angle between the x-axis of the actor and the x-axis of car1 is between 60 and 80 degrees
    do serial:
        vehicle1.drive() with:
            orientation(yaw: [60deg..80deg], relative_to: car1, measure_by: length_to_length)
    ```

## 8.9.11 Modifier along()

Purpose
:   The actor moves along a route.

Category
:   Scenario modifier

Usage
:   Code 105. Along modifier

    ```
    along(route: route
    [, start_offset: length] [, end_offset: length]
    [, <standard-movement-parameters>])
    ```

Parameters
:   * `route`  
      The route to move along.
    * `start_offset`  
      How far along the route should the motion start.
      Default = 0m.
    * `end_offset`  
      How far from the end of the route should the motion end.
      Default = 0m.
    * `<standard-movement-parameters>`

      A set of parameters that are relevant for most movement modifiers.
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).

Example
:   Code 106. Along modifier

    ```
    # Move along a road
    my_road: road
    do:
        my_car.drive() with:
            along(my_road)

    # Move along a path
    my_path: path = map.create_path(my_list_of_points, smooth)
    do:
        my_car.drive() with:
            along(my_path)

    # Move along a compound route
    my_route: route = map.create_route([road_01, lane_A, road_34])
    do:
        my_car.drive() with:
            along(my_route)
    ```

## 8.9.12 Modifier along\_trajectory()

Purpose
:   The actor moves along a trajectory.

Category
:   Scenario modifier

Usage
:   Code 107. Along trajectory modifier

    ```
    along_trajectory(trajectory: trajectory
    [, start_offset: length] [, end_offset: length]
    [, <standard-movement-parameters>])
    ```

Parameters
:   * `trajectory`  
      The trajectory to move along.
    * `start_offset`  
      How far along the trajectory should the motion start.
      Default = 0m.
    * `end_offset`  
      How far from the end of the trajectory should the motion end.
      Default = 0m.
    * `<standard-movement-parameters>`

      A set of parameters that are relevant for most movement modifiers.
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).

Example
:   Code 108. Along trajectory modifier

    ```
    # car1 moves along the trajectory t
    car1.drive() with:
        along_trajectory(t)
    ```

## 8.9.13 Modifier distance()

Purpose
:   Constrain the distance traveled by an actor during a movement.

Category
:   Scenario modifier

Usage
:   Code 109. Distance modifier

    ```
    distance(distance: length)
    [, <standard-movement-parameters>]
    ```

Parameters
:   * `distance`  
      The distance the actor should travel in the current movement.
    * `<standard-movement-parameters>`  
      A set of parameters that are relevant for most movement modifiers.  
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).

Description
:   Constrains the distance traveled by an actor during a movement, such as drive().

Example
:   In the following example the distance traveled by vehicle1 during the d1 phase should be within 30 to 50 meters.

    Code 110. Distance modifier

    ```
    do serial()
        d1: vehicle1.drive() with:
            distance([30m..50m])
    ```

## 8.9.14 Modifier lane()

Purpose
:   Set the lane in which an actor moves.

Category
:   Scenario modifier

Usage
:   Code 111. Lane syntax

    ```
    lane(lane: uint, side_of: physical_object, side: side_left_right
    [, standard-movement-parameters])

    lane(lane: uint, from: side_left_right
    [, standard-movement-parameters])

    lane(same_as: physical_object
    [, standard-movement-parameters])
    ```

Parameters
:   * `lane`  
      A single unsigned integer or a range of unsigned integers indicating a lane or a range of lanes to move in, relative to a certain reference.
      The parameter value (range) specifies a relative number with respect to a certain reference.
      This reference is given through one of the other parameters.
      If no lane parameter is specified, the default is 1.
      For the interpretation of the uint-value see the other parameter descriptions.
    * `same_as`  
      Option to specify that the vehicle must be in the same lane as the referenced vehicle.
      The default-value for the lane-parameter must be neglected.
    * `side_of`  
      Option to specify that the vehicle must be in another lane than the referenced vehicle.
      Which side is specified with the following `side` parameter.
    * `side`  
      Depending on the value the actor shall be on the right or left side of the referenced physical\_object.
      How many lanes right or left of that physical\_object is specified by the lane-parameter.
    * `from`  
      Option to specify that the vehicle is in a certain lane with reference to the road.
      How many lanes from the right or left of the road is specified by the lane-parameter.
    * `<standard-movement-parameters>`  
      A set of parameters that are relevant for most movement modifiers.
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).

Description
:   Specify a lane for the actor to drive on.
    The lane can be chosen either relative to another physical\_object on the road, or relative to the edges of the road.

Examples
:   Code 112. Lane modifier

    ```
    do serial:
        vehicle1.drive() with:
            # Drive in lane closest to the right (right is the default)
            lane(1)

    do serial:
        vehicle1.drive() with:
            # Drive in lane closest to the left side
            lane(1, from: left)

    do parallel:
        vehicle2.drive()
        vehicle1.drive() with:
            # Drive one lane left of vehicle2
            lane(side_of: vehicle2, side: left)

    do parallel:
        vehicle2.drive()
        vehicle1.drive() with:
            # At the end of this phase, be either one or two lanes
            # to the right of vehicle2
            lane([1..2], side_of: vehicle2, side: right, at: end)

    do parallel:
        vehicle2.drive()
        vehicle1.drive() with:
            # Be in the same lane as vehicle2
            lane(same_as: vehicle2)

    do serial:
        vehicle1.drive() with:
            # Drive in lane closest to the inner side (closest to opposing traffic)
            lane(1, from: map.inner_side())

    do serial:
        vehicle1.drive() with:
            # Drive in lane closest to the outer side (farthest to opposing traffic)
            lane(1, from: map.outer_side())
    ```

## 8.9.15 Modifier change\_lane()

Purpose
:   Specify that the actor changes lane.

Category
:   Scenario modifier

Usage
:   Code 113. Change lane modifier

    ```
    change_lane(lane: int, side: side_left_right
    [, <standard-movement-parameters>])
    ```

Parameters
:   * `lane`  
      The number of lanes to change, counting from the lane where the actor starts the action.
      The default is 1.
    * `side`  
      Left or right.
      The side is randomized if not specified.
    * `<standard-movement-parameters>`  
      A set of parameters that are relevant for most movement modifiers.  
      For example, `at`.
      For more information please refer to [Section 8.9.1.1, "Common parameters"](#sec-dm-actions-drive-modifiers-common-parameters).

Examples
:   Code 114. Change lane modifier

    ```
    # Change lane one lane to the left
    do serial:
        vehicle1.drive() with:
            change_lane(side: left)

    # Change the lane 1, 2 or 3 lanes to the right
    do serial:
        vehicle1.drive() with:
            change_lane([1..3], right)
    ```

## 8.9.16 Modifier keep\_lane()

Purpose
:   Specify that the actor stays in the current lane.

Category
:   Scenario modifier

Usage
:   Code 115. Keep lane modifier

    ```
    keep_lane()
    ```

Example
:   Code 116. Keep lane modifier

    ```
    do serial:
        vehicle1.drive() with:
            keep_lane()
    ```

## 8.9.17 Modifier physical\_movement()

Purpose
:   Set the actor movement to be physical or non-physical.

Category
:   Scenario modifier

Usage
:   Code 117. Physical movement modifier

    ```
    physical_movement(option: movement_options)
    ```

Parameters
:   * `option`

      Can be:

      + *prefer\_physical*  
        Perform the movement in conformity with the laws of physics, if possible.
      + *prefer\_non\_physical*  
        Perform the movement disregarding the laws of physics, if the implementation allows that.
        For example, a test track may ignore this request.
      + *must\_be\_physical* (default)  
        An error message is issued if this action cannot be performed in conformity with the laws of physics.

Description
:   Describes the preferences with regard to the physical modeling of the movement of actors in the scenario.

Examples
:   Code 118. Physical movement modifier

    ```
    do serial:
        vehicle1.drive() with:
            speed(10kph)
        vehicle1.drive() with:
            # If possible, try to make speed jump from 10kph to 20kph in zero time
            speed(20kph)
            physical_movement(prefer_non_physical)
    ```

## 8.9.18 Modifier avoid\_collisions()

Purpose
:   Allow or disallow an actor to collide with another object.

Category
:   Scenario modifier

Usage
:   Code 119. Avoid collisions modifier

    ```
    avoid_collisions(avoid: bool)
    ```

Parameters
:   * `avoid`  
      Either true or false.

Description
:   By default, all actors avoid collisions (avoid\_collisions(true)), and a runtime mechanism for collision avoidance is activated for the modifier-specified drive() scenario — if such a mechanism exists.

When set to false, the actor moves regardless of surrounding traffic and may collide.

Example
:   Code 120. Avoid collisions modifier

    ```
    do serial:
        vehicle1.drive() with:
            avoid_collisions(false)
    ```

## 8.9.19 Enum at

Specify at which moments within the phase the constraint must hold.

Values
:   Table 147. Enum at


    | Value | Comment |
    | --- | --- |
    | start | This constraint holds [at](#sec-actions_movableobjects-enum-at) the start of the phase. |
    | end | This constraint holds [at](#sec-actions_movableobjects-enum-at) the end of the phase. |
    | all | This constraint holds throughout this phase (default). |

## 8.9.20 Enum movement\_mode

Values
:   Table 148. Enum movement\_mode


    | Value | Comment |
    | --- | --- |
    | monotonous | This movement mode adheres to the laws of physics. On top of that it limits the level of surprise that a movement may have. |
    | other | Not necessarily monotonous. This is the default. |

## 8.9.21 Enum track

Values
:   Table 149. Enum track


    | Value | Comment |
    | --- | --- |
    | actual | Track the actual movement of the reference vehicle. This is the default. |
    | projected | Track the "projected" movement of the reference vehicle, as it would have been if it kept the speed and direction [at](#sec-actions_movableobjects-enum-at) the start of the action. |

## 8.9.22 Enum lat\_measure\_by

Specify the start and end points for lateral distance measurement. For example, measuring the distance from the left side of the actor to the right side of the reference physical\_object.

Values
:   Table 150. Enum lat\_measure\_by


    | Value | Comment |
    | --- | --- |
    | left\_to\_left | From actor left to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) left. |
    | left\_to\_center | From actor left to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) center. |
    | left\_to\_right | From actor left to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) right. |
    | center\_to\_left | From actor center to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) left. |
    | center\_to\_center | From actor center to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) center. |
    | center\_to\_right | From actor center to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) right. |
    | right\_to\_left | From actor right to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) left. |
    | right\_to\_center | From actor right to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) center. |
    | right\_to\_right | From actor right to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) right. |
    | closest | Closest lateral distance between object and physical\_object. |

## 8.9.23 Enum yaw\_measure\_by

Specify how relative the yaw angle is measured. Defines from which reference line on the actor and to which reference line on the referenced physical\_object the yaw angle is measured.

Values
:   Table 151. Enum yaw\_measure\_by


    | Value | Comment |
    | --- | --- |
    | length\_to\_length | From actor length to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) length. |
    | length\_to\_width | From actor length to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) width. |
    | width\_to\_length | From actor width to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) length. |
    | width\_to\_width | From actor width to [physical\_object](entity.html#sec-trafficparticipant-abstract-physical_object) width. |
    | relative\_to\_north | Actor yaw relative to geographic North. |
    | relative\_to\_road | Actor yaw relative to [road](road_abstractions.html#sec-roads-class-road) s-axis. |

## 8.9.24 Enum orientation\_measured\_by

Specify how to measure the orientation.

Values
:   Table 152. Enum orientation\_measured\_by


    | Value | Comment |
    | --- | --- |
    | absolute | Measure orientation in world coordinates. |
    | relative\_to\_reference | Measure orientation relative to a reference physical\_object. |
    | relative\_to\_road | Measure orientation relative to [road](road_abstractions.html#sec-roads-class-road) coordinates. |

## 8.9.25 Enum movement\_options

Specify how actor movement should be implemented.

Values
:   Table 153. Enum movement\_options


    | Value | Comment |
    | --- | --- |
    | prefer\_physical | Perform the movement physical if possible. |
    | prefer\_non\_physical | Perform the non physical way if the implementation allows that. For example, a test [track](#sec-actions_movableobjects-enum-track) may ignore this request. |
    | must\_be\_physical | An error message is issued, if this action cannot be physically performed for any reason. |