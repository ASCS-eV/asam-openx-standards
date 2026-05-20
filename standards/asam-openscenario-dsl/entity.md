# ASAM Openscenario Dsl v2.2.0 — 8.7 Physical object actors

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/entity.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.7 Physical object actors

## 8.7.1 Physical objects

![Diagram](_images/diag-60f844ee2e0e0bf1436d138e3b4968c616f2d593.png)

## 8.7.2 Actor osc\_actor

Parent of all actors in the standard library.

|  |  |  |  |
| --- | --- | --- | --- |
|  | |  |  | | --- | --- | |  | Child `traffic_participant_group` is an actor that is defined in the informative part for [groups of traffic participants](#sec-dm-entities-traffic-participants-groups) and therefore not part of the normative domain model. | |

Basic information
:   Table 17. Basic information of actor osc\_actor


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Children** | [environment](environment-actors.html#sec-environment-class-environment), [map](road_abstractions.html#sec-roads-class-map), [physical\_object](#sec-trafficparticipant-abstract-physical_object), [traffic\_light\_controller](traffic_lights.html#sec-traffic_lights-entity-traffic_light_controller), traffic\_participant\_group |

## 8.7.3 Actor physical\_object

All tangible objects close to earth, excluding celestial objects such as sun or moon.

Basic information
:   Table 18. Basic information of actor physical\_object


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Parents** | [osc\_actor](#sec-environment-abstract-osc_actor) |
    | **Children** | [movable\_object](#sec-trafficparticipant-entity-movable_object), [stationary\_object](#sec-trafficparticipant-entity-stationary_object) |

Parameters
:   Table 19. Actor physical\_object


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [bounding\_box](#sec-trafficparticipant-class-bounding_box) | [bounding\_box](#sec-trafficparticipant-class-bounding_box) | yes | See [bounding\_box](#sec-trafficparticipant-class-bounding_box) |
    | [color](#sec-trafficparticipant-enum-color) | [color](#sec-trafficparticipant-enum-color) | no | See [color](#sec-trafficparticipant-enum-color) |
    | geometry\_reference | string | no | Opaque reference of an associated 3D geometry model of the physical object. It is implementation-specific how model references are resolved to 3D models. |
    | center\_of\_gravity | [position\_3d](physical_types.html#sec-physical_types-class-position_3d) | yes | Center of gravity of the object. If unknown, the center of the bounding box may be used instead. |

State variables
:   Table 20. State variables of actor physical\_object


    | Variable | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | pose | [pose\_3d](physical_types.html#sec-physical_types-class-pose_3d) | yes | Position and orientation measured in world coordinates with world system as reference. |

### 8.7.3.1 Methods

#### 8.7.3.1.1 Method object\_distance()

Returns the relative distance between the [`physical_object`](#sec-dm-entities-physical-objects) that calls the method and a reference entity.

The distance is computed as the position of the `reference` entity, measured in the coordinate system of the `physical_object` that calls the method.
This calculation is performed either in the longitudinal direction (x-axis), lateral direction (y-axis), vertical direction (z-axis), or as a+ Euclidean distance (length of a straight line).

By default, the distance is measured between the reference points of the respective entities.
Optionally, the distance between the bounding boxes can be computed instead.

Prototype
:   ```
    extend physical_object:
        def object_distance(reference: physical_object, direction: distance_direction, mode: distance_mode = reference_points) -> length
    ```

Return value
:   The relative distance between the `physical_object` that calls the method and the reference entity.

Parameters
:   Table 21. Parameters for method object\_distance()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | reference | [physical\_object](#sec-dm-entities-physical-objects) | The reference entity. |
    | direction | [distance\_direction](#sec-trafficparticipant-enum-distance_direction) | * Use `longitudinal` to measure the distance in the x-coordinate. * Use `lateral` to measure the distance in the y-coordinate. * Use `vertical` to measure the distance in the z-coordinate. * Use `euclidean` to measure the Euclidean distance (length of a straight line). |
    | mode | [distance\_mode](#sec-trafficparticipant-enum-distance_mode) | * Use `reference_points` to measure the distance between the reference points. (Default) * Use `bounding_boxes` to measure the distance between the bounding boxes. |

#### 8.7.3.1.2 Method road\_distance()

Returns the relative road distance between the [`physical_object`](#sec-dm-entities-physical-objects) that calls the method and a reference entity.

The distance is computed as the difference between the s-t-coordinates of the reference entity and the s-t-coordinates of the `physical_object` that calls the method.
This calculation is performed either in the longitudinal direction (s-axis) or the lateral direction (t-axis).

By default, the distance is measured between the reference points of the respective entities.
Optionally, the distance between the bounding boxes can be computed.

Prototype
:   ```
    extend physical_object:
        def road_distance(reference: physical_object, direction: road_distance_direction, mode: distance_mode = reference_points, route_type: on_route_type = on_road) -> length
    ```

Return value
:   The relative distance between the `physical_object` that calls the method and the reference entity.

Parameters
:   Table 22. Parameters for method road\_distance()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | reference | [physical\_object](#sec-dm-entities-physical-objects) | The reference entity. |
    | direction | [road\_distance\_direction](#sec-trafficparticipant-enum-road_distance_direction) | * Use `longitudinal` to measure the distance in the s-coordinate. * Use `lateral` to measure the distance in the t-coordinate. |
    | mode | [distance\_mode](#sec-trafficparticipant-enum-distance_mode) | * Use `reference_points` to measure the distance between the reference points. (Default) * Use `bounding_boxes` to measure the distance between the bounding boxes. |
    | route\_type | [on\_route\_type](#sec-trafficparticipant-enum-on_route_type) | Select the type of route that will be used to compute the s-coordinate. (Default is `on_road`.) |

#### 8.7.3.1.3 Method distance\_to\_xyz\_point()

Returns the relative distance between the [`physical_object`](#sec-dm-entities-physical-objects) that calls the method and an `xyz_point`.

The distance is computed as the position of the `xyz_point`, measured in the coordinate system of the `physical_object` that calls the method.
This calculation is performed either in the longitudinal direction (x-axis), lateral direction (y-axis), vertical direction (z-axis), or as a Euclidean distance (length of a straight line).

By default, the distance is measured from the reference point of the `physical_object`.
Optionally, the distance from the bounding box can be computed.

Prototype
:   ```
    extend physical_object:
        def distance_to_xyz_point(point: xyz_point, direction: distance_direction, mode: distance_mode = reference_points) -> length
    ```

Return value
:   The relative distance between the `physical_object` that calls the method and the reference point.

Parameters
:   Table 23. Parameters for method distance\_to\_xyz\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | point | [xyz\_point](road_abstractions.html#sec-roads-class-xyz_point) | The reference point. |
    | direction | [distance\_direction](#sec-trafficparticipant-enum-distance_direction) | * Use `longitudinal` to measure the distance in the x-coordinate. * Use `lateral` to measure the distance in the y-coordinate. * Use `vertical` to measure the distance in the z-coordinate. * Use `euclidean` to measure the Euclidean distance (length of a straight line). |
    | mode | [distance\_mode](#sec-trafficparticipant-enum-distance_mode) | * Use `reference_points` to measure the distance from the reference point of the actor. (Default) * Use `bounding_boxes` to measure the distance from the bounding box of the actor. |

#### 8.7.3.1.4 Method distance\_to\_route\_point()

Returns the relative distance between the [`physical_object`](#sec-dm-entities-physical-objects) that calls the method and a `route_point`.

The distance is computed as the difference between the s-t-coordinates of the `route_point` and the s-t-coordinates of the `physical_object` that calls the method.
This calculation is performed either in the longitudinal direction (s-axis) or the lateral direction (t-axis).

By default, the distance is measured from the reference point of the `physical_object`.
Optionally, the distance from the bounding box can be computed.

Prototype
:   ```
    extend physical_object:
        def distance_to_route_point(point: route_point, direction: road_distance_direction, mode: distance_mode = reference_points, route_type: on_route_type = on_road) -> length
    ```

Return value
:   The relative distance between the `physical_object` that calls the method and the reference point.

Parameters
:   Table 24. Parameters for method distance\_to\_route\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | point | [route\_point](road_abstractions.html#sec-roads-class-route_point) | The reference point. |
    | direction | [road\_distance\_direction](#sec-trafficparticipant-enum-road_distance_direction) | * Use `longitudinal` to measure the distance in the s-coordinate. * Use `lateral` to measure the distance in the t-coordinate. |
    | mode | [distance\_mode](#sec-trafficparticipant-enum-distance_mode) | * Use `reference_points` to measure the distance from the reference point of the actor. (Default) * Use `bounding_boxes` to measure the distance from the bounding box of the actor. |
    | route\_type | [on\_route\_type](#sec-trafficparticipant-enum-on_route_type) | Select the type of route that will be used to compute the s-coordinate. (Default is `on_road`.) |

#### 8.7.3.1.5 Method distance\_to\_odr\_point()

Returns the relative distance between the [`physical_object`](#sec-dm-entities-physical-objects) that calls the method and an `odr_point`.

The distance is computed as the difference between the s-t-coordinates of the `odr_point` and the s-t-coordinates of the `physical_object` that calls the method.
This calculation is performed either in the longitudinal direction (s-axis) or the lateral direction (t-axis).

By default, the distance is measured from the reference point of the `physical_object`.
Optionally, the distance from the bounding box can be computed.

Prototype
:   ```
    extend physical_object:
        def distance_to_odr_point(point: odr_point, direction: road_distance_direction, mode: distance_mode = reference_points, route_type: on_route_type = on_road) -> length
    ```

Return value
:   The relative distance between the `physical_object` that calls the method and the reference point.

Parameters
:   Table 25. Parameters for method distance\_to\_odr\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | point | [odr\_point](road_abstractions.html#sec-roads-class-odr_point) | The reference point. |
    | direction | [road\_distance\_direction](#sec-trafficparticipant-enum-road_distance_direction) | * Use `longitudinal` to measure the distance in the s-coordinate. * Use `lateral` to measure the distance in the t-coordinate. |
    | mode | [distance\_mode](#sec-trafficparticipant-enum-distance_mode) | * Use `reference_points` to measure the distance from the reference point of the actor. (Default) * Use `bounding_boxes` to measure the distance from the bounding box of the actor. |
    | route\_type | [on\_route\_type](#sec-trafficparticipant-enum-on_route_type) | Select the type of route that will be used to compute the s-coordinate. (Default is `on_road`.) |

#### 8.7.3.1.6 Method get\_s\_coord()

Returns the s-coordinate of the `physical_object`.

By default, the method uses the s-axis of the road where the `physical_object` is located, but the user can select other route element types.
If the `physical_object` is not on a route the method returns an error.

Prototype
:   ```
    extend physical_object:
        def get_s_coord(route_type: on_route_type = on_road) -> length
    ```

Return value
:   Returns a length with the s-coordinate.

Parameters
:   Table 26. Parameters for method get\_s\_coord()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | route\_type | [on\_route\_type](#sec-trafficparticipant-enum-on_route_type) | Select the type of route that will be used to compute the s-coordinate:  * `on_road` (default)    Use the s-axis of the `road` where the actor is located.   If the actor is not on a road the method returns an error. * `on_lane_section`    Use the s-axis of the `lane_section` where the actor is located.   If the actor is not on a lane section the method returns an error. * `on_lane`    Use the s-axis of the `lane` where the actor is located.   If the actor is not on a lane the method returns an error. * `on_crossing`    Use the s-axis of the `crossing` where the actor is located.   If the actor is not on a crossing the method returns an error. |

#### 8.7.3.1.7 Method get\_t\_coord()

Returns the t-coordinate of the `physical_object`.

By default, the method uses the t-axis of the road where the `physical_object` is located, but the user can select other route element types.
If the `physical_object` is not on a route the method returns an error.

Prototype
:   ```
    extend physical_object:
        def get_t_coord(route_type: on_route_type = on_road) -> length
    ```

Return value
:   Returns a length with the t-coordinate.

Parameters
:   Table 27. Parameters for method get\_t\_coord()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | route\_type | [on\_route\_type](#sec-trafficparticipant-enum-on_route_type) | Select the type of route that will be used to compute the t-coordinate:  * `on_road` (default)    Use the t-axis of the `road` where the actor is located.   If the actor is not on a road the method returns an error. * `on_lane_section`    Use the t-axis of the `lane_section` where the actor is located.   If the actor is not on a lane section the method returns an error. * `on_lane`    Use the t-axis of the `lane` where the actor is located.   If the actor is not on a lane the method returns an error. * `on_crossing`    Use the t-axis of the `crossing` where the actor is located.   If the actor is not on a crossing the method returns an error. |

#### 8.7.3.1.8 Method get\_route\_point()

Returns the `route_point` where the `physical_object` is located.

By default, the method uses the road where the `physical_object` is located, but the user can select other route element types.
If the `physical_object` is not on a route the method returns an error.

Prototype
:   ```
    extend physical_object:
        def get_route_point(route_type: on_route_type = on_road) -> route_point
    ```

Return value
:   Returns a `route_point`.

Parameters
:   Table 28. Parameters for method get\_route\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | route\_type | [on\_route\_type](#sec-trafficparticipant-enum-on_route_type) | Select the type of route that will be used to compute the route\_point:  * `on_road` (default)    Use the t-axis of the `road` where the actor is located.   If the actor is not on a road the method returns an error. * `on_lane_section`    Use the t-axis of the `lane_section` where the actor is located.   If the actor is not on a lane section the method returns an error. * `on_lane`    Use the t-axis of the `lane` where the actor is located.   If the actor is not on a lane the method returns an error. * `on_crossing`    Use the t-axis of the `crossing` where the actor is located.   If the actor is not on a crossing the method returns an error. |

#### 8.7.3.1.9 Method set\_bm()

Sets the behavioral model of a physical\_object.

Prototype
:   ```
    extend physical_object:
        def set_bm(behavioral_model : behavioral_model)
    ```

Return value
:   None

Parameters
:   Table 29. Parameter for method set\_bm()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | behavioral\_model | [behavioral\_model](#sec-dm-entities-physical-objects) | The behavioral model to set. |

### 8.7.3.2 Examples

Code 72. Syntax examples for physical\_object

```
# Constrain vehicle to be a wide car
my_wide_car: vehicle
keep(my_wide_car.vehicle_category == car)
keep(my_wide_car.bounding_box.width >= 1.95m)
keep(my_wide_car.color == maroon)
keep(my_wide_car.axles.size() == 2)
keep(my_wide_car.axles[0].number_of_wheels == 2)
keep(my_wide_car.axles[1].number_of_wheels == 2)
keep(my_wide_car.intended_infrastructure[0] == driving)

# Constrain vehicle to be a motorcycle
my_motorcycle: vehicle
keep(my_motorcycle.vehicle_category == vru_vehicle)
keep(my_motorcycle.axles.size() == 2)
keep(my_motorcycle.axles[0].number_of_wheels == 1)
keep(my_motorcycle.axles[1].number_of_wheels == 1)
keep(my_motorcycle.intended_infrastructure[0] == driving)

# Constrain vehicle to be a bicycle
my_bicycle: vehicle
keep(my_bicycle.vehicle_category == vru_vehicle)
keep(my_bicycle.axles.size() == 2)
keep(my_bicycle.axles[0].number_of_wheels == 1)
keep(my_bicycle.axles[1].number_of_wheels == 1)
keep(my_bicycle.intended_infrastructure[0] == biking)
```

## 8.7.4 Actor stationary\_object

A stationary\_object is a physical\_object that is anchored and whose bounding box cannot change its position or speed like a tree or a building.

Basic information
:   Table 30. Basic information of actor stationary\_object


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [physical\_object](#sec-trafficparticipant-abstract-physical_object) |

Inherited parameters and variables
:   Table 31. Inherited parameters and variables of actor stationary\_object


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [physical\_object](#sec-trafficparticipant-abstract-physical_object) | [pose](#tab-trafficparticipant-abstract-physical_object-states), [bounding\_box](#tab-trafficparticipant-abstract-physical_object-info), [color](#tab-trafficparticipant-abstract-physical_object-info), [geometry\_reference](#tab-trafficparticipant-abstract-physical_object-info), [center\_of\_gravity](#tab-trafficparticipant-abstract-physical_object-info) |

### 8.7.4.1 Modifiers

#### 8.7.4.1.1 Modifier location()

Specifies the location of a `stationary_object`.
Shall be invoked before the `do` section, as the location cannot be time-dependent.

Parameters
:   Table 32. Parameters for modifier stationary\_object.location()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | pose | [pose\_3d](physical_types.html#sec-physical_types-class-pose_3d) | Location of the stationary object for the whole scenario. |

Syntax
:   Code 73. Syntax examples for stationary\_object.location()

    ```
    my_pose: pose_3d
    # Add constraints for fields of my_pose
    my_building: stationary_object
    my_building.location(my_pose)

    do: ...
    ```

## 8.7.5 Actor movable\_object

A movable\_object is a physical\_object that is not anchored and can, therefore, be moved and change its position and speed like a rock or a ball.

Basic information
:   Table 33. Basic information of actor movable\_object


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [physical\_object](#sec-trafficparticipant-abstract-physical_object) |
    | **Children** | [traffic\_participant](#sec-trafficparticipant-abstract-traffic_participant) |

State variables
:   Table 34. State variables of actor movable\_object


    | Variable | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | velocity | [velocity\_6d](physical_types.html#sec-physical_types-class-velocity_6d) | yes | Translational and rotational velocity measured in object coordinates with world system as reference. |
    | acceleration | [acceleration\_6d](physical_types.html#sec-physical_types-class-acceleration_6d) | yes | Translational and rotational acceleration measured in object coordinates with world system as reference. |
    | speed | [speed](physical_types.html#sec-physical_types-class-speed) | yes | Speed in center\_of\_gravity defined as sqrt(velocity.translational.x² + velocity.translational.y²) \* sign(velocity.translational.x) |

Inherited parameters and variables
:   Table 35. Inherited parameters and variables of actor movable\_object


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [physical\_object](#sec-trafficparticipant-abstract-physical_object) | [pose](#tab-trafficparticipant-abstract-physical_object-states), [bounding\_box](#tab-trafficparticipant-abstract-physical_object-info), [color](#tab-trafficparticipant-abstract-physical_object-info), [geometry\_reference](#tab-trafficparticipant-abstract-physical_object-info), [center\_of\_gravity](#tab-trafficparticipant-abstract-physical_object-info) |

### 8.7.5.1 Methods

#### 8.7.5.1.1 Method distance\_along\_route()

Returns the distance between an actor and the start or end of a route, measured along the s-axis of the route.
User can pass either a route\_element or a compound\_route.

Prototype
:   ```
    extend traffic_participant:
        def distance_along_route(route: route, from: route_distance_enum = from_start) -> length
    ```

Return value
:   Returns a length measured along the s-axis of the route.

Parameters
:   Table 36. Parameters for method distance\_along\_route()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | route | [route](road_abstractions.html#sec-roads-class-route) | The route along which the distance should be measured.  If the actor calling the method is not on the given route the method returns an error. |
    | from | [route\_distance\_enum](#sec-trafficparticipant-enum-route_distance_enum) | Reference point from which the distance is measured.  * `from_start` (default)    Method returns the relative s-coordinate from route.start\_point() to the actor.    Positive means that the traffic participant is ahead of the start point. * `from_end`    Method returns the relative s-coordinate from the actor to the route.end\_point().    Positive means that the traffic participant is behind of the end point. |

## 8.7.6 Actor traffic\_participant

A traffic\_participant is a physical\_object that is relevant within traffic and may perform traffic-related actions (see traffic\_participant actions) such as following a route. A traffic\_participant includes both, objects that do participate in traffic actively like a driven vehicle and objects that do not move throughout the scenario like a parked vehicle.

Basic information
:   Table 37. Basic information of actor traffic\_participant


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Parents** | [movable\_object](#sec-trafficparticipant-entity-movable_object) |
    | **Children** | [animal](#sec-trafficparticipant-entity-animal), [person](#sec-trafficparticipant-entity-person), [vehicle](#sec-trafficparticipant-entity-vehicle) |

Parameters
:   Table 38. Actor traffic\_participant


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [intended\_infrastructure](#sec-trafficparticipant-enum-intended_infrastructure) | list of intended\_infrastructure | yes | See [intended\_infrastructure](#sec-trafficparticipant-enum-intended_infrastructure) for definition. Intended usage is for further specification of an entity. For example, together with [vehicle\_category](#sec-trafficparticipant-enum-vehicle_category) or to provide hints for implemenations where to spawn and / or auto-route entities. Note that multiple types of infrastructure can be assigned because of the list character of this type. |
    | role | [traffic\_participant\_role](#sec-trafficparticipant-enum-traffic_participant_role) | no | See [traffic\_participant\_role](#sec-trafficparticipant-enum-traffic_participant_role) enum. Role for the traffic participant. |

Inherited parameters and variables
:   Table 39. Inherited parameters and variables of actor traffic\_participant


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [movable\_object](#sec-trafficparticipant-entity-movable_object) | [velocity](#tab-trafficparticipant-entity-movable_object-states), [acceleration](#tab-trafficparticipant-entity-movable_object-states), [speed](#tab-trafficparticipant-entity-movable_object-states) |
    | [physical\_object](#sec-trafficparticipant-abstract-physical_object) | [pose](#tab-trafficparticipant-abstract-physical_object-states), [bounding\_box](#tab-trafficparticipant-abstract-physical_object-info), [color](#tab-trafficparticipant-abstract-physical_object-info), [geometry\_reference](#tab-trafficparticipant-abstract-physical_object-info), [center\_of\_gravity](#tab-trafficparticipant-abstract-physical_object-info) |

### 8.7.6.1 Methods

#### 8.7.6.1.1 Method time\_to\_collision()

Returns the time that is left until a possible collision between a traffic\_participant and a reference physical\_object takes place.

Prototype
:   ```
    extend traffic_participant:
        def time_to_collision(reference: physical_object) -> time
    ```

Return value
:   Returns the time until the bounding\_box of traffic\_participant would collide with the bounding box of the reference physical\_object, assuming both keep moving with their current velocity.

Parameters
:   Table 40. Parameter for method time\_to\_collision()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | reference | [physical\_object](#sec-dm-entities-physical-objects) | The reference physical\_object. |

Syntax
:   Code 74. Syntax example for method time\_to\_collision()

    ```
    scenario prevent_collision:
        ego: vehicle
        other_car: vehicle

        var collision_time: time = sample(ego.time_to_collision(reference: other_car), every(2s))

        do parallel:
            other_car.drive() with:
                speed(50kph)

            ego.drive() with:
                position(behind: other_car)
                until rise(collision_time < 10s)
    ```

#### 8.7.6.1.2 Method time\_headway()

Measure the time headway between the `traffic_participant` that calls the method and a reference `physical_object`.
Time headway is defined as the time it will take the trailing actor to reach the current position of the leading actor.

The `traffic_participant` and the reference `physical_object` are assumed to be moving in a common direction.

* The distance between the objects is measured from the front of the leading object to the front of the trailing object.

  + For example, for two vehicles heading in the same direction, from front bumper to front bumper.
* A positive value means that the `traffic_participant` is trailing behind the reference `physical_object`.
* A negative value means that the `traffic_participant` is leading ahead of the reference `physical_object`.
* This distance is divided by the speed of the trailing object.

The result of this division is the time headway.

Prototype
:   ```
    extend vehicle:
        def time_headway(reference: physical_object) -> time
    ```

Return value
:   Returns the time headway according to the above definition.

Parameters
:   Table 41. Parameter for method time\_headway()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | reference | [physical\_object](#sec-dm-entities-physical-objects) | The reference physical\_object. |

#### 8.7.6.1.3 Method time\_gap()

Returns the time distance between a `traffic_participant` and a reference `physical_object`.

For example, assume two vehicles (a traffic participant and a reference physical object) moving along a road in a common direction.

If `direction` is set to `longitudinal`, calculate the return value in the following way:

1. Measure the distance from the rear bumper of the leading vehicle to the front bumper of the trailing vehicle.
2. Divide this distance by the speed of the trailing vehicle.
3. The result is the longitudinal time gap.

For two vehicles traveling in the same lane the lateral time gap is not defined.

Now consider the two vehicles traveling in the same way but in different lanes.

If `direction` is set to `lateral`, calculate the return value in the following way:

1. Measure the distance from the right side of the vehicle on the left to the left side of the vehicle on the right.
2. Divide by the lateral velocity of the `traffic_participant` in the direction of the reference `physical_object`.
3. The result is the lateral time gap.

If the bounding boxes of `traffic_participant` and the reference `physical_object` are overlapping in the desired direction, the method shall return zero.

For two vehicles traveling in different lanes the longitudinal time gap is not defined.

Prototype
:   ```
    extend traffic_participant:
        def time_gap(reference: physical_object, direction: road_distance_direction) -> time
    ```

Return value
:   Returns the time gap according to the definition above.

Parameters
:   Table 42. Parameters for method time\_gap()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | reference | [physical\_object](#sec-dm-entities-physical-objects) | The reference entity. |
    | direction | [road\_distance\_direction](#sec-trafficparticipant-enum-road_distance_direction) | * `longitudinal`    The relative s-coordinate.    Positive means that the traffic participant is ahead of the reference. * `lateral`    The relative t-coordinate.    Positive means that the traffic participant is left of the reference. |

#### 8.7.6.1.4 Method space\_gap()

Returns the space distance between a `traffic_participant` and a reference `physical_object`.
The space gap distance is defined as the distance one object would need to travel to touch another object, in a given direction.

For example, assume two vehicles (a traffic participant and a reference physical object) moving along a road in a common direction.
If `direction` is set to `longitudinal`, then the space gap should be measured as the distance from the rear bumper of the leading vehicle to the front bumper of the trailing vehicle.

For two vehicles traveling in the same lane the space time gap is not defined.

Now consider the two vehicles traveling in the same way but in different lanes.
If `direction` is set to `lateral`, then the space gap should be measured as the distance from the right side of the vehicle on the left to the left side of the vehicle on the right.

For two vehicles traveling in different lanes the longitudinal space gap is not defined.

If the bounding boxes of the two vehicles are overlapping in the desired direction, the method shall return zero.

Prototype
:   ```
    extend traffic_participant:
        def space_gap(reference: physical_object, direction: road_distance_direction) -> length
    ```

Return value
:   Returns the space gap distance according to the definition above.

Parameters
:   Table 43. Parameters for method space\_gap()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | reference | [physical\_object](#sec-dm-entities-physical-objects) | The reference entity. |
    | direction | [road\_distance\_direction](#sec-trafficparticipant-enum-road_distance_direction) | * `longitudinal`    The relative s-coordinate.    Positive means that the traffic participant is ahead of the reference. * `lateral`    The relative t-coordinate.    Positive means that the traffic participant is left of the reference. |

#### 8.7.6.1.5 Method space\_headway()

Measure the space headway between the `traffic_participant` that calls the method and a reference `physical_object`.
Space headway is defined as the distance that the trailing actor needs to travel to reach the current position of the leading actor.

The `traffic_participant` and the reference `physical_object` are assumed to be moving in a common direction.

* The space headway is measured as the distance from the front of the leading object to the front of the trailing object.

  + For example, for two vehicles heading in the same direction, from front bumper to front bumper.
* A positive value means that the `traffic_participant` is trailing behind the reference `physical_object`.
* A negative value means that the `traffic_participant` is leading ahead of the reference `physical_object`.

This distance is the space headway.

Prototype
:   ```
    extend vehicle:
        def space_headway(reference: physical_object) -> length
    ```

Return value
:   Returns the space headway according to the description above.

Parameters
:   Table 44. Parameter for method space\_headway()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | reference | [physical\_object](#sec-dm-entities-physical-objects) | The reference physical\_object. |

## 8.7.7 Actor vehicle

A device intended for transport of people or cargo. Here restricted to land vehicles, meaning vehicles that move on a land surface such as a road or sidewalk.

Basic information
:   Table 45. Basic information of actor vehicle


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [traffic\_participant](#sec-trafficparticipant-abstract-traffic_participant) |
    | **Children** | [trailer](#sec-trafficparticipant-entity-trailer) |

Parameters
:   Table 46. Actor vehicle


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [vehicle\_category](#sec-trafficparticipant-enum-vehicle_category) | [vehicle\_category](#sec-trafficparticipant-enum-vehicle_category) | yes | See [vehicle\_category](#sec-trafficparticipant-enum-vehicle_category) |
    | axles | list of axle | yes | See [axle](#sec-trafficparticipant-class-axle) |
    | rear\_overhang | [length](physical_types.html#sec-physical_types-class-length) | yes | Rear overhang of the [vehicle](#sec-trafficparticipant-entity-vehicle) or more explicitly the horizontal distance between the end of the [bounding\_box](#sec-trafficparticipant-class-bounding_box) and the center of the rear axle. |
    | trailer\_receiver | [hitch\_receiver](#sec-trafficparticipant-class-hitch_receiver) | no | Receiver part of the hitch that acts as mounting point for connecting a trailer. If not specified, the [vehicle](#sec-trafficparticipant-entity-vehicle) does not have a receiver hitching device for trailers. |

Inherited parameters and variables
:   Table 47. Inherited parameters and variables of actor vehicle


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [movable\_object](#sec-trafficparticipant-entity-movable_object) | [velocity](#tab-trafficparticipant-entity-movable_object-states), [acceleration](#tab-trafficparticipant-entity-movable_object-states), [speed](#tab-trafficparticipant-entity-movable_object-states) |
    | [physical\_object](#sec-trafficparticipant-abstract-physical_object) | [pose](#tab-trafficparticipant-abstract-physical_object-states), [bounding\_box](#tab-trafficparticipant-abstract-physical_object-info), [color](#tab-trafficparticipant-abstract-physical_object-info), [geometry\_reference](#tab-trafficparticipant-abstract-physical_object-info), [center\_of\_gravity](#tab-trafficparticipant-abstract-physical_object-info) |
    | [traffic\_participant](#sec-trafficparticipant-abstract-traffic_participant) | [intended\_infrastructure](#tab-trafficparticipant-abstract-traffic_participant-info), [role](#tab-trafficparticipant-abstract-traffic_participant-info) |

### 8.7.7.1 Modifiers

#### 8.7.7.1.1 Modifier tow\_trailer()

Specifies that the vehicle is towing a trailer.
This means that the trailer receiver of the vehicle must be connected to the coupler of the trailer.
Relevant state variables shall be updated to specify the connection between tow vehicle and trailer.

Parameters
:   Table 48. Parameters for modifier vehicle.tow\_trailer()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | trailer | trailer | Trailer to be towed. |

Syntax
:   Code 75. Syntax examples for vehicle.tow\_trailer()

    ```
    my_car: vehicle
    my_trailer: trailer

    my_car.tow_trailer(my_trailer)

    do: ...
    ```

## 8.7.8 Actor trailer

A trailer is any non-self-propelled vehicle that is constructed to be towed by a power-driven vehicle. This also includes semi–trailers. (According to ECE/TRANS/WP.29/78/Rev.4)

Basic information
:   Table 49. Basic information of actor trailer


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [vehicle](#sec-trafficparticipant-entity-vehicle) |

Parameters
:   Table 50. Actor trailer


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [trailer\_category](#sec-trafficparticipant-enum-trailer_category) | [trailer\_category](#sec-trafficparticipant-enum-trailer_category) | yes | Specify [trailer](#sec-trafficparticipant-entity-trailer) category. |
    | coupler | [hitch\_coupler](#sec-trafficparticipant-class-hitch_coupler) | yes | Coupler part of the hitch that acts as mounting point to connect this [trailer](#sec-trafficparticipant-entity-trailer) to the tow vehicle. |

State variables
:   Table 51. State variables of actor trailer


    | Variable | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | tow\_vehicle | [vehicle](#sec-trafficparticipant-entity-vehicle) | yes | Reference to the [vehicle](#sec-trafficparticipant-entity-vehicle) that is towing this trailer. The tow [vehicle](#sec-trafficparticipant-entity-vehicle) can also be another trailer. If not specified, the [trailer](#sec-trafficparticipant-entity-trailer) is not towable. |

Inherited parameters and variables
:   Table 52. Inherited parameters and variables of actor trailer


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [movable\_object](#sec-trafficparticipant-entity-movable_object) | [velocity](#tab-trafficparticipant-entity-movable_object-states), [acceleration](#tab-trafficparticipant-entity-movable_object-states), [speed](#tab-trafficparticipant-entity-movable_object-states) |
    | [physical\_object](#sec-trafficparticipant-abstract-physical_object) | [pose](#tab-trafficparticipant-abstract-physical_object-states), [bounding\_box](#tab-trafficparticipant-abstract-physical_object-info), [color](#tab-trafficparticipant-abstract-physical_object-info), [geometry\_reference](#tab-trafficparticipant-abstract-physical_object-info), [center\_of\_gravity](#tab-trafficparticipant-abstract-physical_object-info) |
    | [traffic\_participant](#sec-trafficparticipant-abstract-traffic_participant) | [intended\_infrastructure](#tab-trafficparticipant-abstract-traffic_participant-info), [role](#tab-trafficparticipant-abstract-traffic_participant-info) |
    | [vehicle](#sec-trafficparticipant-entity-vehicle) | [vehicle\_category](#tab-trafficparticipant-entity-vehicle-info), [axles](#tab-trafficparticipant-entity-vehicle-info), [rear\_overhang](#tab-trafficparticipant-entity-vehicle-info), [trailer\_receiver](#tab-trafficparticipant-entity-vehicle-info) |

### 8.7.8.1 Examples

Code 76. Example 1: A vehicle with a trailer attached

```
my_towing_truck: vehicle
keep(my_towing_truck.vehicle_category == truck)

my_receiver: hitch_receiver
keep(my_receiver.trailer_category == fifth_wheel)
keep(my_receiver.position_x == -1.2)
keep(my_receiver.position_z == 0.5)

# Specify hitch receiver characteristics on tow vehicle:
keep(my_towing_truck.trailer_receiver == my_receiver)

my_trailer: trailer
keep(my_trailer.trailer_category == full_trailer)

my_coupler: coupler_hitch
keep(my_coupler.position_x == 2.5)
keep(my_coupler.position_z == 0.5)

# Specify hitch coupler characteristics on trailer:
keep(my_trailer.coupler == my_coupler)

# The truck is towing a trailer:
my_towing_truck.tow_trailer(my_trailer)
```

Add the following lines to attach a second trailer to the combination in [Code 73, "Example 1: A vehicle with a trailer attached"](#code-dm-trailer-example1):

Code 77. Example 2: Attach a second trailer

```
my_trailer_also_has_a_receiver: hitch_receiver
keep(my_trailer_also_has_a_receiver.trailer_category == ball)
keep(my_trailer_also_has_a_receiver.position_x == -1.6)
keep(my_trailer_also_has_a_receiver.position_z == 0.5)

# Specify the hitch receiver on the first trailer:
keep(my_trailer.trailer_receiver == my_trailer_also_has_a_receiver)

my_second_trailer: trailer
keep(my_second_trailer.trailer_category == full_trailer)

second_trailer_coupler: hitch_coupler
keep(second_trailer_coupler.position_x == 2.5)
keep(second_trailer_coupler.position_z == 0.5)

# Specify the hitch coupler on the second trailer
keep(my_second_trailer.coupler == second_trailer_coupler)

# The second trailer is towed by the first trailer
my_trailer.tow_trailer(my_second_trailer)
```

When viewed driving to the left, the combination is now `<my_towing_truck|--<my_trailer|--<my_second_trailer|`

## 8.7.9 Actor person

A person represents a human being. A person may act in different and changing modalitites throughout a scenario. For example, walking or being in a car.

Basic information
:   Table 53. Basic information of actor person


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [traffic\_participant](#sec-trafficparticipant-abstract-traffic_participant) |

Inherited parameters and variables
:   Table 54. Inherited parameters and variables of actor person


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [movable\_object](#sec-trafficparticipant-entity-movable_object) | [velocity](#tab-trafficparticipant-entity-movable_object-states), [acceleration](#tab-trafficparticipant-entity-movable_object-states), [speed](#tab-trafficparticipant-entity-movable_object-states) |
    | [physical\_object](#sec-trafficparticipant-abstract-physical_object) | [pose](#tab-trafficparticipant-abstract-physical_object-states), [bounding\_box](#tab-trafficparticipant-abstract-physical_object-info), [color](#tab-trafficparticipant-abstract-physical_object-info), [geometry\_reference](#tab-trafficparticipant-abstract-physical_object-info), [center\_of\_gravity](#tab-trafficparticipant-abstract-physical_object-info) |
    | [traffic\_participant](#sec-trafficparticipant-abstract-traffic_participant) | [intended\_infrastructure](#tab-trafficparticipant-abstract-traffic_participant-info), [role](#tab-trafficparticipant-abstract-traffic_participant-info) |

## 8.7.10 Actor animal

An animal represents a living being which is not a human. An animal may act in different and changing modalitites throughout a scenario. For example, running or being in a car.

Basic information
:   Table 55. Basic information of actor animal


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [traffic\_participant](#sec-trafficparticipant-abstract-traffic_participant) |

Inherited parameters and variables
:   Table 56. Inherited parameters and variables of actor animal


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [movable\_object](#sec-trafficparticipant-entity-movable_object) | [velocity](#tab-trafficparticipant-entity-movable_object-states), [acceleration](#tab-trafficparticipant-entity-movable_object-states), [speed](#tab-trafficparticipant-entity-movable_object-states) |
    | [physical\_object](#sec-trafficparticipant-abstract-physical_object) | [pose](#tab-trafficparticipant-abstract-physical_object-states), [bounding\_box](#tab-trafficparticipant-abstract-physical_object-info), [color](#tab-trafficparticipant-abstract-physical_object-info), [geometry\_reference](#tab-trafficparticipant-abstract-physical_object-info), [center\_of\_gravity](#tab-trafficparticipant-abstract-physical_object-info) |
    | [traffic\_participant](#sec-trafficparticipant-abstract-traffic_participant) | [intended\_infrastructure](#tab-trafficparticipant-abstract-traffic_participant-info), [role](#tab-trafficparticipant-abstract-traffic_participant-info) |

## 8.7.11 Struct bounding\_box

Simplified three dimensional shape enclosing the physical\_object. The bounding box does NOT include side mirrors for vehicles. The height includes the ground\_clearance, therefore it always goes from the top to the ground.

Basic information
:   Table 57. Basic information of struct bounding\_box


    |  |  |
    | --- | --- |
    | **Instantiable** | no |

Parameters
:   Table 58. Struct bounding\_box


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | center | [position\_3d](physical_types.html#sec-physical_types-class-position_3d) | yes | Represents the geometrical center of the bounding box expressed in coordinates that refer to the coordinate system of the [physical\_object](#sec-trafficparticipant-abstract-physical_object) |
    | length | [length](physical_types.html#sec-physical_types-class-length) | yes | Dimension in x-direction of the coordinate system of the [physical\_object](#sec-trafficparticipant-abstract-physical_object) |
    | width | [length](physical_types.html#sec-physical_types-class-length) | yes | Dimension in y-direction of the coordinate system of the [physical\_object](#sec-trafficparticipant-abstract-physical_object) |
    | height | [length](physical_types.html#sec-physical_types-class-length) | yes | Dimension in z-direction of the coordinate system of the [physical\_object](#sec-trafficparticipant-abstract-physical_object) |

## 8.7.12 Struct axle

Taken from ASAM OpenSCENARIO 1.x plus number of wheels to avoid ambiguities (for example, twin tires). Check definitions there for now.

Basic information
:   Table 59. Basic information of struct axle


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Used by** | [vehicle](#sec-trafficparticipant-entity-vehicle) |

Parameters
:   Table 60. Struct axle


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | max\_steering | [angle](physical_types.html#sec-physical_types-class-angle) | yes | Maximum steering angle for the wheels on the [axle](#sec-trafficparticipant-class-axle) |
    | wheel\_diameter | [length](physical_types.html#sec-physical_types-class-length) | yes | Diameter for the wheels on this [axle](#sec-trafficparticipant-class-axle) |
    | track\_width | [length](physical_types.html#sec-physical_types-class-length) | yes | Distance between the centerline of the outer wheels on opposing sides of the [axle](#sec-trafficparticipant-class-axle) |
    | position\_x | [length](physical_types.html#sec-physical_types-class-length) | yes | Longitudinal position of the [axle](#sec-trafficparticipant-class-axle) in the x-axis of the vehicle. For a 2-axle vehicle, the rear [axle](#sec-trafficparticipant-class-axle) must have position\_x = 0m |
    | position\_z | [length](physical_types.html#sec-physical_types-class-length) | yes | Vertical position of the [axle](#sec-trafficparticipant-class-axle) in the z-axis of the [vehicle](#sec-trafficparticipant-entity-vehicle) |
    | number\_of\_wheels | uint | yes | Number of wheels on the [axle](#sec-trafficparticipant-class-axle) |

## 8.7.13 Struct hitch\_receiver

A hitch is a device that connects a trailer to a towing vehicle. The `hitch_receiver` is on the tow vehicle. For a successful connection between tow vehicle and trailer, the `hitch_type` between receiver and coupler must match.

Basic information
:   Table 61. Basic information of struct hitch\_receiver


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Used by** | [vehicle](#sec-trafficparticipant-entity-vehicle) |

Parameters
:   Table 62. Struct hitch\_receiver


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [hitch\_type](#sec-trafficparticipant-enum-hitch_type) | [hitch\_type](#sec-trafficparticipant-enum-hitch_type) | yes | Type of hitch connector. Default: none, for vehicles that do not have a hitch receiver. |
    | position\_x | [length](physical_types.html#sec-physical_types-class-length) | yes | Position of the `hitch_receiver` on the x-axis of the tow vehicle. |
    | position\_z | [length](physical_types.html#sec-physical_types-class-length) | yes | Position of the `hitch_receiver` on the z-axis of the tow vehicle. |
    | max\_rotation | [angle](physical_types.html#sec-physical_types-class-angle) | no | Maximum relative rotation between the tow [vehicle](#sec-trafficparticipant-entity-vehicle) and the trailer. |
    | max\_tilt | [angle](physical_types.html#sec-physical_types-class-angle) | no | Maximum relative tilt (pitch, roll) between the towing [vehicle](#sec-trafficparticipant-entity-vehicle) and the trailer. |

State variables
:   Table 63. State variables of struct hitch\_receiver


    | Variable | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | is\_towing | bool | yes | Indicates if tow [vehicle](#sec-trafficparticipant-entity-vehicle) and [trailer](#sec-trafficparticipant-entity-trailer) are connected (true) or disconnected (false). |

## 8.7.14 Struct hitch\_coupler

A hitch is a device that connects a trailer to a towing vehicle. The `hitch_coupler` is on the trailer. For a successful connection between tow vehicle and trailer, the `hitch_type` between receiver and coupler must match.

Basic information
:   Table 64. Basic information of struct hitch\_coupler


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Used by** | [trailer](#sec-trafficparticipant-entity-trailer) |

Parameters
:   Table 65. Struct hitch\_coupler


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [hitch\_type](#sec-trafficparticipant-enum-hitch_type) | [hitch\_type](#sec-trafficparticipant-enum-hitch_type) | yes | Type of hitch connector. There is no default type for the hitch coupler. |
    | position\_x | [length](physical_types.html#sec-physical_types-class-length) | yes | Position of the `hitch_coupler` on the x-axis of the trailer. |
    | position\_z | [length](physical_types.html#sec-physical_types-class-length) | yes | Position of the `hitch_coupler` on the z-axis of the trailer. |

State variables
:   Table 66. State variables of struct hitch\_coupler


    | Variable | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | is\_towed | bool | yes | Indicates if tow [vehicle](#sec-trafficparticipant-entity-vehicle) and [trailer](#sec-trafficparticipant-entity-trailer) are connected (true) or disconnected (false). |

## 8.7.15 Enum color

Description of the color of a physical\_object. Specifies the color of a physical object. Not intended to replace more detailed material properties, but rather for debugging purposes. For a vehicle this should affect the vehicle body, for pedestrians it may affect the main piece of clothing. Based on the set defined by W3C for HTML\_ "basic colors".

Basic information
:   Table 67. Basic information of enum color


    |  |  |
    | --- | --- |
    | **Instantiable** | no |

Values
:   Table 68. Enum color


    | Value | Comment |
    | --- | --- |
    | white | RGB(255,255,255) |
    | silver | RGB(192,192,192) |
    | gray | RGB(128,128,128) |
    | black | RGB(0,0,0) |
    | red | RGB(255,0,0) |
    | maroon | RGB(128,0,0) |
    | yellow | RGB(255,255,0) |
    | olive | RGB(128,128,0) |
    | lime | RGB(0,255,0) |
    | green | RGB(0,128,0) |
    | aqua | RGB(0,255,255) |
    | teal | RGB(0,128,128) |
    | blue | RGB(0,0,255) |
    | navy | RGB(0,0,128) |
    | fuchsia | RGB(255,0,255) |
    | purple | RGB(128,0,128) |
    | violet | RGB(238,130,238) |
    | orange | RGB(255,165,0) |
    | brown | RGB(165,42,42) |
    | other | Other (unspecified but known) [color](#sec-trafficparticipant-enum-color) |

## 8.7.16 Enum vehicle\_category

Vehicle category based on UN ECE/TRANS/WP.29/78/Rev.6 extended by non-self-propelled vehicles.

Basic information
:   Table 69. Basic information of enum vehicle\_category


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Used by** | [vehicle](#sec-trafficparticipant-entity-vehicle) |

Values
:   Table 70. Enum vehicle\_category


    | Value | Comment |
    | --- | --- |
    | car | A car is a motorized [vehicle](#sec-trafficparticipant-entity-vehicle) designed primarily for passenger transportation. A car typically has four wheels. (UNECE category M1, G and L7) |
    | bus | A bus is a motorized [vehicle](#sec-trafficparticipant-entity-vehicle) designed to carry multiple passengers. (UNECE category M3 classes I, II, III) |
    | heavy\_truck | A heavy truck is a large commercial [vehicle](#sec-trafficparticipant-entity-vehicle) designed for transporting heavy loads. The cargo area is rigidly fixed to the [vehicle](#sec-trafficparticipant-entity-vehicle) itself. (UNECE category N2) |
    | truck = heavy\_truck | This category is provided for backwards compatibility and should not be used. Use heavy\_truck instead. The value is equal to heavy\_truck, which is the value this enum had in earlier releases. |
    | [trailer](#sec-trafficparticipant-entity-trailer) | A [trailer](#sec-trafficparticipant-entity-trailer) is a non-motorized [vehicle](#sec-trafficparticipant-entity-vehicle) designed for being towed by a motorized [vehicle](#sec-trafficparticipant-entity-vehicle) to carry goods, animals, or people. (UNECE category O1 to O3) |
    | micro\_mobility\_device | A micro-mobility device is a small, lightweight [vehicle](#sec-trafficparticipant-entity-vehicle) for short-distance travel, like hoverboards or roller skates. While bicycles, stand-up scooters, and wheelchairs may technically fall into this category, the respective detailed categories shall be used instead. |
    | vru\_vehicle = micro\_mobility\_device | This category is provided for backwards compatibility and should not be used. Use micro\_mobility\_device or one of the more specific VRU categories (bicycle, stand\_up\_scooter, wheelchair) instead. This value is equal to micro\_mobility\_device, which is the value this enum had in earlier releases. |
    | other | Unspecified but known type of [vehicle](#sec-trafficparticipant-entity-vehicle) |
    | van | A van is a motorized [vehicle](#sec-trafficparticipant-entity-vehicle) with a larger cargo area than a car, used for transporting goods or people. This category is not intended for mini vans, which shall rather be categorized as cars. (UNECE categories M2 and N1.) |
    | semi\_tractor | A semi-tractor is a [vehicle](#sec-trafficparticipant-entity-vehicle) designed for towing semi-trailers for the transportation of heavy loads. (UNECE category N3) |
    | semi\_trailer | A semi-trailer is a [vehicle](#sec-trafficparticipant-entity-vehicle) designed for being towed by a semi-tractor. Characteristics compared to a regular [trailer](#sec-trafficparticipant-entity-trailer) are the large size, the fact that a large portion of the weight is supported [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) the hitch, and a large overlap with the towing vehicle, i.e. the semi-tractor. (UNECE category O4). |
    | motorcycle | A motorcycle is a motorized [vehicle](#sec-trafficparticipant-entity-vehicle) designed primarily for passenger transportation. Compared to a car, fewer passive safety features, such as a full passenger cell, are typically present. This category includes both two-wheeled motorcycles and three-wheeled vehicles like motorcycles with side-cars or trikes. (UNECE categories L1 to L5) |
    | bicycle | A bicycle is a human-powered or motor-assisted, pedal-driven vehicle. This category includes typical two-wheeled bicycles as well as cargo-bikes and other pedal-driven vehicles with more than two wheels. |
    | stand\_up\_scooter | A stand-up scooter is a compact, typically two-wheeled device. It is operated with the rider standing on a deck between the wheels. It may be propelled by a motor or the rider making a kicking movement. |
    | wheelchair | A wheelchair is a manually or electrically powered mobility device with a seat mounted on a wheeled frame. Manual propulsion may be provided by the seated [person](#sec-trafficparticipant-entity-person) or a [person](#sec-trafficparticipant-entity-person) pushing the wheelchair. |
    | work\_machine | A work-machine is a [vehicle](#sec-trafficparticipant-entity-vehicle) designed for specific tasks (e.g., construction equipment, agricultural tractors, forklifts). |
    | train | A train is a [vehicle](#sec-trafficparticipant-entity-vehicle) designed for the transport of passengers and freight on rail infrastructure. The rail infrastructure for trains is mostly grade-separated from the public [road](road_abstractions.html#sec-roads-class-road) infrastructure as trains have exclusive right-of-way. Therefore, in case crossings with the [road](road_abstractions.html#sec-roads-class-road) infrastructure occur, the exclusive right-of-way is ensured, e.g. by railway barriers. A train often acts as a series of connected vehicles. |
    | tram | A tram is a [vehicle](#sec-trafficparticipant-entity-vehicle) designed for using rail infrastructure for the transport of passengers on rail infrastructure. The rail infrastructure may fully or partially overlap with public [road](road_abstractions.html#sec-roads-class-road) infrastructure. In contrast to trains, trams do not have exclusive right-of-way. A tram often acts as a series of connected vehicles. |
    | watercraft | A watercraft is a [vehicle](#sec-trafficparticipant-entity-vehicle) designed for travel on water (boats, ships, etc.). This category is deliberately generic and may be refined in future versions as needed. |
    | aircraft | An aircraft is a [vehicle](#sec-trafficparticipant-entity-vehicle) designed for flight through the [air](environment-actors.html#sec-environment-class-air) (airplanes, helicopters, etc.). This category is deliberately generic and may be refined in future versions as needed. |
    | land\_vehicle | A land [vehicle](#sec-trafficparticipant-entity-vehicle) is a [vehicle](#sec-trafficparticipant-entity-vehicle) designed for travel on land. This category is intentionally unspecific to include land vehicles that do not fall into ther categories and may be detailed out in future versions if use-cases require so. |

## 8.7.17 Enum trailer\_category

Trailer categories according to ECE/TRANS/WP.29/78/Rev.4

Basic information
:   Table 71. Basic information of enum trailer\_category


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Used by** | [trailer](#sec-trafficparticipant-entity-trailer) |

Values
:   Table 72. Enum trailer\_category


    | Value | Comment |
    | --- | --- |
    | semi\_trailer | A towed [vehicle](#sec-trafficparticipant-entity-vehicle) in which the axle(s) is (are) positioned behind the centre of gravity of the [vehicle](#sec-trafficparticipant-entity-vehicle) (when uniformly loaded), and which is equipped with a connecting device permitting horizontal and vertical forces to be transmitted to the towing vehicle. One or more of the axles may be driven by the towing vehicle. |
    | full\_trailer | A towed [vehicle](#sec-trafficparticipant-entity-vehicle) that has [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) least two axles and is equipped with a towing device that can [move](actions.html#sec-actions_movableobjects-class-move) vertically (in relation to the trailer) and controls the direction of the front axle(s), but that transmits no significant static load to the towing vehicle. One or more of the axles may be driven by the towing vehicle. |
    | central\_axle\_trailer | A towed vehicle, equipped with a towing device that cannot [move](actions.html#sec-actions_movableobjects-class-move) vertically (in relation to the trailer) and in which the axle(s) is (are) positioned close to the centre of gravity of the [vehicle](#sec-trafficparticipant-entity-vehicle) (when uniformly loaded) such that only a small static vertical load - not exceeding 10 percent of that corresponding to the maximum mass of the [trailer](#sec-trafficparticipant-entity-trailer) or a load of 1,000 daN (whichever is the lesser) - is transmitted to the towing vehicle. One or more of the axles may be driven by the towing vehicle. |

## 8.7.18 Enum hitch\_type

Types of trailer hitches

Basic information
:   Table 73. Basic information of enum hitch\_type


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Used by** | [hitch\_receiver](#sec-trafficparticipant-class-hitch_receiver) |

Values
:   Table 74. Enum hitch\_type


    | Value | Comment |
    | --- | --- |
    | ball | Standard ball and coupler (including gooseneck) connector. |
    | pintle | Pintle and hook connector. |
    | fifth\_wheel | Fifth wheel connector with jaws and kingpin. |
    | other | Other type. |
    | none | There is no hitch connector. Default value for all vehicles. |

## 8.7.19 Enum intended\_infrastructure

Infrastructure that is typically used by a traffic participant. Can be used to further specify an entity. For example, together with vehicle\_category or to provide hints for simulators where to spawn entities. Each entity can be assigned multiple values. Note that this needs to be aligned with road abstraction feature.

Basic information
:   Table 75. Basic information of enum intended\_infrastructure


    |  |  |
    | --- | --- |
    | **Instantiable** | no |

Values
:   Table 76. Enum intended\_infrastructure


    | Value | Comment |
    | --- | --- |
    | driving | Taken from ASAM OpenDRIVE: "Normal" drivable [road](road_abstractions.html#sec-roads-class-road) that is not one of the other types |
    | sidewalk | Taken from ASAM OpenDRIVE: Lane reserved for pedestrians |
    | biking | Taken from ASAM OpenDRIVE: Lane reserved for cyclists |
    | rail | Taken from ASAM OpenDRIVE: Lane reserved for trains |
    | tram | Taken from ASAM OpenDRIVE: Lane reserved for trams |
    | bus | Taken from ASAM OpenDRIVE: Lane reserved for buses |
    | taxi | Taken from ASAM OpenDRIVE: Lane reserved for taxis |
    | hov | Taken from ASAM OpenDRIVE: Lane reserved for High Occupancy Vehicles (HOVs) |

## 8.7.20 Enum traffic\_participant\_role

The role specifies the perceivable role of a traffic participant, as that might influence the behavior in traffic of surrounding traffic participants. The majority of traffic participants are civil, representing normal traffic participants. Whether a role is active (for example, in the sense of an ambulance flashing its emergency vehicle lighting) is independent of the role of the traffic participant.

Basic information
:   Table 77. Basic information of enum traffic\_participant\_role


    |  |  |
    | --- | --- |
    | **Instantiable** | no |

Values
:   Table 78. Enum traffic\_participant\_role


    | Value | Comment |
    | --- | --- |
    | civil | Traffic participant that can be perceived as regular civilian and does not perceivably indicate any other role. |
    | ambulance | Traffic participant that can be perceived as belonging to a medical emergency service. |
    | fire\_brigade | Traffic participant that can be perceived as belonging to the fire brigade. |
    | fire = fire\_brigade | This role is provided for backwards compatibility and should not be used. Use fire\_brigade instead. The value is equal to fire\_brigade, which is the value this enum had in earlier releases. |
    | military | Traffic participant that can be perceived as belonging to a military force. |
    | police | Traffic participant that can be perceived as belonging to a law enforcement agency. |
    | public\_transport | Traffic participant that can be perceived as a form of mass passenger transportation mode (e.g. public transport bus, rental passenger bus, tram) or clearly recognizable passenger transportation mode (e.g. taxi). |
    | roadside\_assistance | Traffic participant that can be perceived as belonging to a roadside/breakdown assistance service, e.g. towing vehicle. |
    | road\_assistance = roadside\_assistance | This role is provided for backwards compatibility and should not be used. Use roadside\_assistance instead. The value is equal to roadside\_assistance, which is the value this enum had in earlier releases. |
    | garbage\_collection | Traffic participant that can be perceived as belonging to a garbage collection service. |
    | construction | Traffic participant that can be perceived as construction vehicle/construction worker (e.g. [road](road_abstractions.html#sec-roads-class-road) construction, rail construction). |
    | road\_construction = construction | This role is provided for backwards compatibility and should not be used. Use construction instead. The value is equal to construction, which is the value this enum had in earlier releases. |
    | other | The entity has another unspecified but known role. |
    | freight\_transport | Traffic participant that can be perceived as freight transport, e.g. freight truck, delivery van, delivery bike, postman. |
    | special\_transport | Traffic participant that can be perceived as part of special transport (e.g. heavy or oversized load). |
    | dangerous\_goods\_transport | Traffic participant that can be perceived as part of dangerous goods/hazardous materials transport. |
    | agriculture | Traffic participant that can be perceived as agricultural machinery. |
    | traffic\_control | Traffic participant that can be perceived as an obligated traffic control unit (e.g. railroad flagman, [person](#sec-trafficparticipant-entity-person) responsible for traffic control [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) construction site, support [vehicle](#sec-trafficparticipant-entity-vehicle) for dangerous goods transport). |

## 8.7.21 Enum distance\_direction

Basic information
:   Table 79. Basic information of enum distance\_direction


    |  |  |
    | --- | --- |
    | **Used by** | [keep\_space\_gap](actions.html#sec-actions_vehicles-class-keep_space_gap) |

Values
:   Table 80. Enum distance\_direction


    | Value | Comment |
    | --- | --- |
    | longitudinal | Measure distance in the x-coordinate. Positive means that the `reference` is in front of the `physical_object` that calls the method. |
    | lateral | Measure distance in the y-coordinate. Positive means that the `reference` is to the left of the `physical_object` that calls the method. |
    | vertical | Measure distance in the z-coordinate. Positive means that the `reference` is to the above the `physical_object` that calls the method. |
    | euclidean | Measure distance in a Eucledian (or straight-line) way. Result is always positive. |

## 8.7.22 Enum road\_distance\_direction

Values
:   Table 81. Enum road\_distance\_direction


    | Value | Comment |
    | --- | --- |
    | longitudinal | Measure distance in the s-coordinate. Positive means that the `reference` is in front of the `physical_object` that calls the method. |
    | lateral | Measure distance in the t-coordinate. Positive means that the `reference` is to the left of the `physical_object` that calls the method. |

## 8.7.23 Enum distance\_mode

Values
:   Table 82. Enum distance\_mode


    | Value | Comment |
    | --- | --- |
    | reference\_points | Measures the distance between the reference points. |
    | bounding\_boxes | Measures the distance between the bounding boxes. |

## 8.7.24 Enum on\_route\_type

Select which s/t coordinate system is used to obtain the coordinates

Values
:   Table 83. Enum on\_route\_type


    | Value | Comment |
    | --- | --- |
    | on\_road | Use the `road` s/t coordinates |
    | on\_lane\_section | Use the `lane_section` s/t coordinates |
    | on\_lane | Use the `lane` s/t coordinates |
    | on\_crossing | Use the `crossing` s/t coordinates |

## 8.7.25 Enum route\_distance\_enum

Reference point from which the distance is measured.

Values
:   Table 84. Enum route\_distance\_enum


    | Value | Comment |
    | --- | --- |
    | from\_start | Measure distance from the start of the route. |
    | from\_end | Measure distance from the end of the route. |

## 8.7.26 Groups of traffic participants

|  |  |
| --- | --- |
|  | Please note that the following section and its sub-sections are non-normative. |

Many implementations for the creation and the handling of groups of traffic participants exist.
Some traffic flow simulators use stochastic traffic flow models and others use deterministic modeling approaches.

The following content is an example on how to build groups using only generic ASAM OpenSCENARIO language features.
A standard group model may be included in future versions of the standard.

|  |  |
| --- | --- |
|  | Groups represent multiple actor instances with multiple definitions and states. It is assumed that scenario authors will likely define groups at the top level and not under lower levels in the domain model hierarchy such as `physical_actor`. |

![Diagram](_images/diag-beea350b6e1531ab08951dc1702e8cbc8906d894.png)

### 8.7.26.1 Actor vehicle\_group

A traffic\_participant\_group serves as a collection of traffic\_participant actors. A group represents multiple actor instances with multiple definitions and states.

There are two main use cases for vehicle groups:

1. Adding entities to a scenario to have more participants in the scenario.
   By generating multiple vehicles in the surrounding environment of the scenario these vehicles act as 'noise' in the scenario.
2. Creating multiple vehicles with predefined initial conditions.  
   For example, creating a single-lane or convoy formation of vehicles, or both.

Initial conditions of actors and the actual behavior of actors throughout the scenarios differ:

* The ***group*** defines the *initial conditions* of actors in the scenario, meaning their creation and destruction.
* The ***behavioral model*** assigned to each vehicle defines the *actual behavior* of the vehicle within the group.

Basic information
:   Table 85. Basic information of actor vehicle\_group


    |  |  |
    | --- | --- |
    | **Instantiable** | no |
    | **Parents** | traffic\_participant\_group |
    | **Children** | common\_route\_vehicle\_group, random\_traffic\_vehicle\_group |

Parameters
:   Table 86. Actor vehicle\_group


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | vehicles | list of vehicle | yes | List of vehicles being part of this group. |

#### 8.7.26.1.1 Examples

Code 78. Example for vehicle\_group

```
scenario dut.driving_alongside_group:
    # Defining a group with a common route and
    # a single-lane formation
    g: single_lane_vehicle_group

    # Using 'for' constraint to control vehicles
    # parameters
    for v in g.vehicles:
        keep(v.category in [bus, truck])

    r: route

    do parallel:
        g.drive() with:
            along(r)
            lane(side_of: dut.vehicle, at: start)
        dut.vehicle.drive() with:
            along(r)
```