# ASAM Openscenario Dsl v2.2.0 — 8.12 Road abstraction classes

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/road_abstractions.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.12 Road abstraction classes

## 8.12.1 Class definitions

## 8.12.2 Actor map

A map is the top-level actor that contains the description of the abstract road network.

Basic information
:   Table 186. Basic information of actor map


    |  |  |
    | --- | --- |
    | **Parents** | [osc\_actor](entity.html#sec-environment-abstract-osc_actor) |
    | **Used by** | OpenSCENARIO |

Parameters
:   Table 187. Actor map


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | map\_file | string | no | Name of the external [map](#sec-roads-class-map) file |
    | routes | list of route | yes | The list of routes that are part of the abstract [road](#sec-roads-class-road) network |
    | junctions | list of junction | yes | The list of junctions that are part of the abstract [road](#sec-roads-class-road) network |
    | [driving\_rule](#sec-roads-enum-driving_rule) | [driving\_rule](#sec-roads-enum-driving_rule) | yes | Specify on which side of the [road](#sec-roads-class-road) the vehicles [drive](actions.html#sec-actions_vehicles-class-drive) |
    | traffic\_light\_groups | list of traffic\_light\_group | no | All the traffic lights in the [map](#sec-roads-class-map) |
    | traffic\_light\_control | list of traffic\_light\_cycle | no | The traffic light cycle for traffic light groups. It does not necessarily contain control plans for all elements in traffic light groups and may also be empty. |

### 8.12.2.1 Methods

#### 8.12.2.1.1 Method odr\_to\_route\_point()

Takes a position in ASAM OpenDRIVE coordinates and returns the corresponding ASAM OpenSCENARIO route-coordinates for the point.
The method returns an error if the point is not on a route.

Prototype
:   ```
    extend map:
        def odr_to_route_point(road_id: string, lane_id: string, s: length, t: length) -> route_point
    ```

Return value
:   Returns a *route\_point*.

Parameters
:   Table 188. Parameters for method odr\_to\_route\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | road\_id | string | ASAM OpenDRIVE roadId |
    | lane\_id | string | Optional. ASAM OpenDRIVE laneId.  If omitted, the t-coordinate is measured from the ASAM OpenDRIVE road reference line.  If included, the t-coordinate is measured from the ASAM OpenDRIVE lane centerline of the lane. |
    | s | [length](physical_types.html#sec-physical_types-class-length) | The s-coordinate in ASAM OpenDRIVE coordinates |
    | t | [length](physical_types.html#sec-physical_types-class-length) | The t-coordinate in ASAM OpenDRIVE coordinates |

#### 8.12.2.1.2 Method xyz\_to\_route\_point()

Takes a position in world coordinates and returns the corresponding ASAM OpenSCENARIO route-coordinates for the point.
If the point is not on a [`route`](#sec-roads-class-route), returns with an error.

Prototype
:   ```
    extend map:
        def xyz_to_route_point(x: length, y: length, z: length) -> route_point
    ```

Return value
:   Returns a *route\_point*.

Parameters
:   Table 189. Parameters for method xyz\_to\_route\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | x | [length](physical_types.html#sec-physical_types-class-length) | The x-coordinate in the world-coordinate system. |
    | y | [length](physical_types.html#sec-physical_types-class-length) | The y-coordinate in the world-coordinate system. |
    | z | [length](physical_types.html#sec-physical_types-class-length) | The z-coordinate in the world-coordinate system. |

#### 8.12.2.1.3 Method route\_point\_to\_xyz()

Converts the coordinates specified in route-coordinates into the corresponding world-coordinates.
Returns a route point in Cartesian (x, y, z) coordinates.

Prototype
:   ```
    extend map:
        def route_point_to_xyz(route_point: route_point) -> xyz_point
    ```

Return value
:   Returns an *xyz\_point*.

Parameters
:   Table 190. Parameters for method route\_point\_to\_xyz()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | route\_point | [route\_point](#sec-roads-class-route_point) | ASAM OpenSCENARIO route\_point to be converted. |

#### 8.12.2.1.4 Method outer\_side()

Farther from opposing traffic.

Prototype
:   ```
    extend map:
        def outer_side() -> side_left_right
    ```

Return value
:   Returns `right` if *map.driving\_rule* is *right\_hand\_traffic*, `left` otherwise.

#### 8.12.2.1.5 Method inner\_side()

Closer to opposing traffic.

Prototype
:   ```
    extend map:
        def inner_side() -> side_left_right
    ```

Return value
:   Returns `left` if *map.driving\_rule* is *right\_hand\_traffic*, `right` otherwise.

#### 8.12.2.1.6 Method create\_route()

Creates a *compound\_route* that contains all the provided route instances, in the same sequential order as the input list.
Routable point types are connected according to the *connect\_points\_by* argument.
If the *connect\_points\_by* field is empty, this method defaults to the option `waypoint`.

Prototype
:   ```
    extend map:
        def create_route(routes: list of route, connect_points_by: connect_route_points, legal_route: bool) -> compound_route
    ```

Return value
:   Returns a *compound\_route* that contains all the specified routes.

Parameters
:   Table 191. Parameters for method create\_route()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | routes | list of [route](#sec-roads-class-route) | The route instances to be combined to form the new *compound\_route*. |
    | connect\_points\_by | [connect\_route\_points](#sec-roads-enum-connect_route_points) | Defines how to connect the points in the list of route. Default: waypoint. |
    | legal\_route | bool | The compound route only contains legal route elements. Default: true. |

When actors are placed on lanes with no inherent traffic flow direction, like a sidewalk, the initial orientation of the actor within this lane might be ambiguous.
In this case, it is suggested to use two instances of `route_point` to disambiguate the preferred initial orientation of the actor.
The example below demonstrates a pedestrian walking across *sidewalk\_1* (in the positive t-direction) before taking the crosswalk towards *sidewalk\_2*.

Syntax
:   Code 75. Syntax example

    ```
    map: map
    my_cross: crossing
    sidewalk_1, sidewalk_2: lane
    map.crossing_connects(my_cross, sidewalk_1, sidewalk_2, start_s_coord: 5.0m)

    sw_pt_1: route_point with:
            keep(it.route == sidewalk_1)
            keep( it.s ==  5.0m)
            keep( it.t == -1.0m)

    sw_pt_2: route_point with:
            keep(it.route == sidewalk_1)
            keep( it.s == 5.0m) # same s-coordinate as sw_pt_1
            keep( it.t == 0.5m)  # t-coordinate to the left of sw_pt_1

    my_route: route = map.create_route([sw_pt_1, sw_pt_2, my_cross, sidewalk_2])
    ```

    The below example demonstrates a pedestrian walking along *sidewalk\_1* in negative s-direction before taking the crosswalk towards *sidewalk\_2*.

    Code 76. Syntax example

    ```
    map: map
    my_cross: crossing
    sidewalk_1, sidewalk_2: lane
    map.crossing_connects(my_cross, sidewalk_1, sidewalk_2, start_s_coord: 5.0m)

    sw_pt_1: route_point with:
        keep(it.route == sidewalk_1)
        keep(it.s == 10.0m)
        keep(it.t == 0.0m)

    sw_pt_2: route_point with:
        keep(it.route == sidewalk_1)
        keep(it.s == 5.0m) # s-coordinate smaller than sw_pt_1
        keep(it.t == 0.0m) # same t-coordinate as sw_pt_1

    my_route: route = map.create_route([sw_pt_1, sw_pt_2, my_cross, sidewalk_2])
    ```

#### 8.12.2.1.7 Method create\_route\_point()

Creates a *route\_point*.

Prototype
:   ```
    extend map:
        def create_route_point(route: route, s: length, t: length) -> route_point
    ```

Return value
:   Returns a *route\_point*.

Parameters
:   Table 192. Parameters for method create\_route\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | route | [route](#sec-roads-class-route) | The route where the point resides |
    | s | [length](physical_types.html#sec-physical_types-class-length) | s-coordinate in the route |
    | t | [length](physical_types.html#sec-physical_types-class-length) | t-coordinate in the route |

#### 8.12.2.1.8 Method create\_xyz\_point()

Creates an xyz\_point.

Prototype
:   ```
    extend map:
        def create_xyz_point(x: length, y: length, z: length) -> xyz_point
    ```

Return value
:   Returns an xyz\_point.

Parameters
:   Table 193. Parameters for method create\_xyz\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | x | [length](physical_types.html#sec-physical_types-class-length) | x-coordinate in world-coordinate system |
    | y | [length](physical_types.html#sec-physical_types-class-length) | y-coordinate in world-coordinate system |
    | z | [length](physical_types.html#sec-physical_types-class-length) | z-coordinate in world-coordinate system |

#### 8.12.2.1.9 Method create\_odr\_point()

Creates an *odr\_point*.

Prototype
:   ```
    extend map:
        def create_odr_point(road_id: string, lane_id: string, s: length, t: length) -> odr_point
    ```

Return value
:   Returns an *odr\_point*.

Parameters
:   Table 194. Parameters for method create\_odr\_point()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | road\_id | string | ASAM OpenDRIVE roadId |
    | lane\_id | string | Optional. ASAM OpenDRIVE laneId.  If omitted, the t-coordinate is measured from the ASAM OpenDRIVE road reference line.  If included, the t-coordinate is measured from the respective ASAM OpenDRIVE lane centerline. |
    | s | [length](physical_types.html#sec-physical_types-class-length) | s-coordinate in ASAM OpenDRIVE coordinates |
    | t | [length](physical_types.html#sec-physical_types-class-length) | t-coordinate in ASAM OpenDRIVE coordinates |

#### 8.12.2.1.10 Method create\_path()

Creates a `path` in world x-y-z-coordinates from a list of `pose_3d` points.

Prototype
:   ```
    extend map:
        def create_path(points: list of pose_3d, interpolation: path_interpolation) -> path
    ```

Return value
:   Returns a `path` in world x-y-z-coordinates.

Parameters
:   Table 195. Parameters for method create\_path()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | points | list of [pose\_3d](physical_types.html#sec-physical_types-class-pose_3d) | List of points in world x-y-z-coordinates. |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | Choose how to join the points of the path. |

Syntax
:   Code 77. Syntax example for create\_path()

    ```
    pose1, pose2, pose3: pose_3d
    keep(pose1.position.x == 23.423)
    keep(pose1.position.y == 3.43)
    # Repeat for pose2 and pose3

    my_path: path = create_path([pose1, pose2, pose3], smooth)
    ```

#### 8.12.2.1.11 Method create\_path\_odr\_points()

Creates a `path` in world x-y-z-coordinates from a list of `odr_point` points.

Prototype
:   ```
    extend map:
        def create_path_odr_points(points: list of odr_point, interpolation: path_interpolation, on_road_network: bool) -> path
    ```

Return value
:   Returns a `path` in world x-y-z-coordinates.

Parameters
:   Table 196. Parameters for method create\_path\_odr\_points()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | points | list of [odr\_point](#sec-roads-class-odr_point) | Sequence of `odr_point` that will be converted to world x-y-z-coordinates to create a `path`. |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | Choose how to join the points of the path. |
    | on\_road\_network | bool | If set to *true*, the points of the path must be joined while keeping the whole path on the road network. |

Syntax
:   Code 78. Syntax example for create\_path\_odr\_points()

    ```
    pt1: odr_point = map.create_odr_point(road_id: 12, lane_id: 1, s: 10m, t: 0.2m)
    pt2: odr_point = map.create_odr_point(road_id: 12, lane_id: 2, s: 25m, t: 0.0m)
    pt3: odr_point = map.create_odr_point(road_id: 13, lane_id: 1, s: 30m, t: 0.0m)

    my_path: path = map.create_path_odr_points([pt1, pt2, pt3], smooth, true)
    ```

#### 8.12.2.1.12 Method create\_path\_route\_points()

Creates a `path` in world x-y-z-coordinates from a list of `route_point` points.

Prototype
:   ```
    extend map:
        def create_path_route_points(points: list of route_point, interpolation: path_interpolation, on_road_network: bool) -> path
    ```

Return value
:   Returns a `path` in world x-y-z-coordinates.

Parameters
:   Table 197. Parameters for method create\_path\_route\_points()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | points | list of [route\_point](#sec-roads-class-route_point) | Sequence of route\_point that will be converted to world x-y-z-coordinates to create a `path`. |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | Choose how to join the points of the path. |
    | on\_road\_network | bool | If set to *true*, the points of the path must be joined while keeping the whole path on the road network. |

Syntax
:   Code 79. Syntax example for create\_path\_route\_points()

    ```
    pt1, pt2, pt3: route_point
    keep(pt1.route == my_road)
    keep(pt1.s == 120.0m)
    keep(pt1.t == 5.3m)
    # Add similar constraints for pt2 and pt3

    my_path: path = map.create_path_route_points([pt1, pt2, pt3], smooth, true)
    ```

#### 8.12.2.1.13 Method create\_trajectory()

Creates a `trajectory` in world x-y-z-coordinates from a list of `pose_3d` points and time stamps.

Prototype
:   ```
    extend map:
        def create_trajectory(points: list of pose_3d, time_stamps: list of time,interpolation: path_interpolation) -> trajectory
    ```

Return value
:   Returns a `trajectory` in world x-y-z-coordinates.

Parameters

Table 198. Parameters for method create\_trajectory()


| Parameter | Type | Description |
| --- | --- | --- |
| points | list of [pose\_3d](physical_types.html#sec-physical_types-class-pose_3d) | List of points in world x-y-z-coordinates. |
| time\_stamps | list of [time](physical_types.html#sec-physical_types-class-time) | Time stamps for each element in points. The lists *time\_stamps* and *points* must have the same length. |
| interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | Choose how to join the points of the trajectory. |

Code 80. Syntax example for create\_trajectory()

```
pose1, pose2, pose3: pose_3d
keep(pose1.position.x == 23.423)
keep(pose1.position.y == 3.43)
# Repeat for pose2 and pose3

time_stamps: list of time = [0s, 2s, 5s]

my_trajectory: trajectory = map.create_trajectory([pose1, pose2, pose3], time_stamps, smooth)
```

#### 8.12.2.1.14 Method create\_trajectory\_odr\_points()

Creates a `trajectory` in world x-y-z-coordinates from a list of `odr_point` points.

Prototype
:   ```
    extend map:
        def create_trajectory_odr_points(points: list of odr_point, time_stamps: list of time, interpolation: path_interpolation, on_road_network: bool) -> trajectory
    ```

Return value
:   Returns a `trajectory` in world x-y-z-coordinates.

Parameters
:   Table 199. Parameters for method create\_trajectory\_odr\_points()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | points | list of [odr\_point](#sec-roads-class-odr_point) | Sequence of `odr_point` that will be converted to world x-y-z-coordinates to create a `trajectory`. |
    | time\_stamps | list of [time](physical_types.html#sec-physical_types-class-time) | Time stamps for each element in points. The lists *time\_stamps* and *points* must have the same length. |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | Choose how to join the points of the trajectory. |
    | on\_road\_network | bool | If set to *true*, the points of the trajectory must be joined while keeping the whole trajectory on the road network. |

Syntax
:   Code 81. Syntax example for create\_trajectory\_odr\_points()

    ```
    pt1: odr_point = map.create_odr_point(road_id: 12, lane_id: 1, s: 10m, t: 0.2m)
    pt2: odr_point = map.create_odr_point(road_id: 12, lane_id: 2, s: 25m, t: 0.0m)
    pt3: odr_point = map.create_odr_point(road_id: 13, lane_id: 1, s: 30m, t: 0.0m)

    time_stamps: list of time = [0s, 2s, 5s]

    my_trajectory: trajectory = map.create_trajectory_odr_points([pt1, pt2, pt3], time_stamps, smooth, true)
    ```

#### 8.12.2.1.15 Method create\_trajectory\_route\_points()

Creates a `trajectory` in world x-y-z-coordinates from a list of `route_point` points.

Prototype
:   ```
    extend map:
        def create_trajectory_route_points(points: list of route_point, time_stamps: list of time, interpolation: path_interpolation, on_road_network: bool) -> trajectory
    ```

Return value
:   Returns a `trajectory` in world x-y-z-coordinates.

Parameters
:   Table 200. Parameters for method create\_trajectory\_route\_points()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | points | list of [route\_point](#sec-roads-class-route_point) | Sequence of `route_point` that will be converted to world x-y-z-coordinates to create a `trajectory`. |
    | time\_stamps | list of [time](physical_types.html#sec-physical_types-class-time) | Time stamps for each element in points. The lists *time\_stamps* and *points* must have the same length. |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | Choose how to join the points of the trajectory. |
    | on\_road\_network | bool | If set to *true*, the points of the trajectory must be joined while keeping the whole trajectory on the road network. |

Syntax
:   Code 82. Syntax example for create\_trajectory\_route\_points()

    ```
    pt1, pt2, pt3: route_point
    keep(pt1.route == my_road)
    keep(pt1.s == 120.0m)
    keep(pt1.t == 5.3m)
    # Add similar constraints for pt2 and pt3

    time_stamps: list of time = [0s, 2s, 5s]

    my_trajectory: trajectory = map.create_trajectory_route_points([pt1, pt2, pt3], time_stamps, smooth)
    ```

#### 8.12.2.1.16 Method resolve\_relative\_path()

Creates a `path` from a `relative_path` by implementing the following steps:

1. Sample the pose of the reference entity.
2. Use this pose as the origin to establish the appropriate coordinate system for the list of points that are provided in the `relative_path`.
3. Compute the world x-y-z-coordinates of the list of points.
4. Return this list of points in a `path`.

   Prototype
   :   ```
       extend map:
           def resolve_relative_path(relative_path: relative_path, reference: physical_object, transform: relative_transform) -> path
       ```

   Return value
   :   Returns a *path* in world x-y-z-coordinates.

   Parameters
   :   Table 201. Parameters for method map.resolve\_relative\_path()


       | Parameter | Type | Description |
       | --- | --- | --- |
       | relative\_path | [relative\_path](#sec-paths-abstract-relative_path) | The relative path to be resolved to absolute x-y-z-coordinates. |
       | reference | [physical\_object](entity.html#sec-dm-entities-physical-objects) | Reference entity that marks the origin to resolve the list of points. |
       | transform | [relative\_transform](#sec-roads-enum-relative_transform) | Type of transformation to resolve relative points into absolute coordinates |

#### 8.12.2.1.17 Method resolve\_relative\_trajectory()

Creates a `trajectory` from a `relative_trajectory` by implementing the following steps:

1. Sample the pose of the reference entity.
2. Use this pose as the origin to establish the appropriate coordinate system for the list of points provided in the `relative_trajectory`.
3. Compute the world x-y-z-coordinates of the list of points.
4. Return this list of points in a `trajectory`.
5. The time stamps remain unchanged.

   Prototype
   :   ```
       extend map:
           def resolve_relative_trajectory(relative_trajectory: relative_trajectory, reference: physical_object, transform: relative_transform) -> trajectory
       ```

   Return value
   :   Returns a *trajectory* in world x-y-z-coordinates.

   Parameters
   :   Table 202. Parameters for method resolve\_relative\_trajectory()


       | Parameter | Type | Description |
       | --- | --- | --- |
       | relative\_trajectory | [relative\_trajectory](#sec-trajectories-abstract-relative_trajectory) | The relative trajectory to be resolved to absolute x-y-z-coordinates. |
       | reference | [physical\_object](entity.html#sec-dm-entities-physical-objects) | Reference entity that marks the origin to resolve the list of points. |
       | transform | [relative\_transform](#sec-roads-enum-relative_transform) | Type of transformation to resolve relative points into absolute coordinates |

#### 8.12.2.1.18 Method get\_map\_file()

Prototype
:   ```
    extend map:
        def get_map_file() -> string
    ```

Return value
:   Returns a string with the path and file name of the map\_file.

### 8.12.2.2 Modifiers

#### 8.12.2.2.1 Modifier number\_of\_lanes()

Creates constraints for the number of lanes within a [`route`](#sec-roads-class-route) by lane type, lane use and/or lane directionality.

Parameters
:   Table 203. Parameters for modifier map.number\_of\_lanes()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | route | [route](#sec-roads-class-route) | Mandatory. The route that will have these constraints. |
    | num\_of\_lanes | uint | Mandatory. The desired number of lanes. |
    | lane\_type | [lane\_type](#sec-roads-enum-lane_type) | Optional. Apply the constraint to the number of lanes with this type. |
    | lane\_use | [lane\_use](#sec-roads-enum-lane_use) | Optional. Apply the constraint to the number of lanes with this use. |
    | directionality | [directionality](#sec-roads-enum-directionality) | Optional. Apply the constraint to the number of lanes with this directionality. |

Syntax
:   ```
    city_road: road
    map.number_of_lanes(city_road, 1, pedestrian)
    map.number_of_lanes(city_road, 2, driving, directionality: uni_direction)
    map.number_of_lanes(city_road, 1, lane_use: mixed_traffic_vru)
    ```

    ```
    highway_ls: lane_section
    num: int with:
        keep(it >= 3) # constrained number
    map.number_of_lanes(highway_ls, 0, pedestrian)
    map.number_of_lanes(highway_ls, num, driving, directionality: uni_direction)
    map.number_of_lanes(highway_ls, 2, non_driving, lane_use: stop)
    map.number_of_lanes(highway_ls, 1, non_driving, lane_use: median)
    ```

#### 8.12.2.2.2 Modifier routes\_are\_in\_sequence()

Specifies that one route follows another in successive order.

Parameters
:   Table 204. Parameters for modifier map.routes\_are\_in\_sequence()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | preceding | [route](#sec-roads-class-route) | The first route |
    | succeeding | [route](#sec-roads-class-route) | The second route, which follows after the first route. |
    | road | [road](#sec-roads-class-road) | Optional. The road that will contain this sequence of routes. |

Syntax
:   ```
    lane1, lane2: lane
    map.routes_are_in_sequence(preceding: lane1, succeeding: lane2)
    ```

    ```
    my_road: road
    ls_a, la_b: lane_section
    map.routes_are_in_sequence(preceding: ls_a, succeeding: ls_b, road: my_road)
    ```

#### 8.12.2.2.3 Modifier roads\_follow\_in\_junction()

Defines a legal `route` through a junction.

Table 205. Parameters for modifier map.roads\_follow\_in\_junction()


| Parameter | Type | Description |
| --- | --- | --- |
| junction | [junction](#sec-roads-class-junction) | The junction to be used. |
| in\_road | [road](#sec-roads-class-road) | The chosen road that leads into the junction. |
| out\_road | [road](#sec-roads-class-road) | The chosen road that leads away from the junction. |
| direction | [junction\_direction](#sec-roads-enum-junction_direction) | Indicates the direction of the *out\_road* relative to the *in\_road*. |
| clockwise\_count | uint | *out\_road* is *clockwise\_count* roads from *in\_road*, counting clockwise.  Values larger than *number\_of\_roads* are illegal.  Example: For a four-way junction, *clockwise\_count* can have the following values:  `1`: Left  `2`: Straight  `3`: Right  `4`: U-turn |
| number\_of\_roads | uint | Total number of *in\_roads* connected to the junction. |
| in\_lane | [lane](#sec-roads-class-lane) | The chosen lane within *in\_road*. |
| out\_lane | [lane](#sec-roads-class-lane) | The chosen lane within *out\_road*. |
| junction\_route | [route](#sec-roads-class-route) | The element(s) that connect the *in\_lane* or *in\_road* to the *out\_lane* or *out\_road* within the junction. |
| resulting\_route | [route](#sec-roads-class-route) | The route going from *in\_lane* or *in\_road* to the *out\_lane* or *out\_road*. |

#### 8.12.2.2.4 Modifier routes\_overlap()

Specifies that two routes overlap longitudinally, see [routes overlap](dm_abstract_road_network.html#sec-dm-roads-routes-overlap-modifier).
For example, two lanes in a lane section are considered to overlap.
Two parallel roads running in the opposite direction are also considered to overlap.

Table 206. Parameters for modifier map.routes\_overlap()


| Parameter | Type | Description |
| --- | --- | --- |
| route1 | [route](#sec-roads-class-route) | The first of the overlapping routes. |
| route2 | [route](#sec-roads-class-route) | The second of the overlapping routes. |
| overlap\_kind | [route\_overlap\_kind](#sec-roads-enum-route_overlap_kind) | The type of expected overlap.  Notice route1 is considered the first route to interpret the values of the enum. |

#### 8.12.2.2.5 Modifier lane\_side()

Specifies the side relation between two instances of lane.

Table 207. Parameters for modifier map.lane\_side()


| Parameter | Type | Description |
| --- | --- | --- |
| lane1 | [lane](#sec-roads-class-lane) | The first lane. |
| side | [side\_left\_right](#sec-roads-enum-side_left_right) | Locate lane1 on this side of lane2. |
| lane2 | [lane](#sec-roads-class-lane) | The second lane. |
| count | uint | For a count of n, there are n-1 lanes between the two instances. |
| lane\_section | [lane\_section](#sec-roads-class-lane_section) | Optional. The lane\_section where the lanes reside. |

Syntax example:

```
lane_a, lane_b: lane
map.lane_side(lane_a, left, lane_b)
```

```
my_ls: lane_section
lane_c, lane_d: lane
map.lane_side(lane_c, right, lane_d, 2, my_ls)
```

#### 8.12.2.2.6 Modifier compound\_lane\_side()

Specifies side relation between two instances of compound\_lane.

Table 208. Parameters for modifier map.compound\_lane\_side()


| Parameter | Type | Description |
| --- | --- | --- |
| lane1 | [compound\_lane](#sec-roads-class-compound_lane) | The first compound\_lane. |
| side | [side\_left\_right](#sec-roads-enum-side_left_right) | Locate lane1 on this side of lane2. |
| lane2 | [compound\_lane](#sec-roads-class-compound_lane) | The second compound\_lane. |
| count | uint | For a count of n, there are n-1 lanes between the two instances. |
| route | [route](#sec-roads-class-route) | Optional. The route where the compound lanes reside. |

#### 8.12.2.2.7 Modifier end\_lane()

The lane ends in its lane\_section and has no successor in the next lane\_section.

Parameters
:   Table 209. Parameters for modifier map.end\_lane()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | lane | [lane](#sec-roads-class-lane) | This lane ends in its current lane\_section. |

Syntax
:   ```
    ls_a, ls_b: lane_section
    my_road: road
    map.routes_are_in_sequence(preceeding: ls_a, succeeding: ls_b, road: my_road)

    my_ending_lane: lane with:
        keep(it.lane_section == ls_a)
    map.end_lane(my_ending_lane)
    ```

#### 8.12.2.2.8 Modifier start\_lane()

The lane starts in its lane\_section and has no predecessor in the previous lane\_section.

Parameters
:   Table 210. Parameters for modifier map.start\_lane()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | lane | [lane](#sec-roads-class-lane) | This lane starts in its current lane\_section. |

Syntax
:   ```
    ls_a, ls_b: lane_section
    my_road: road
    map.routes_are_in_sequence(preceding: ls_a, succeeding: ls_b, road: my_road)

    my_starting_lane: lane with:
        keep(it.lane_section == ls_b)
    map.start_lane(my_starting_lane)
    ```

#### 8.12.2.2.9 Modifier crossing\_connects()

Connect a crossing between two lanes.
The s-coordinate of the crossing increases from the start\_lane to end\_lane.
If the start\_angle argument is not specified, the default solves the connection with start\_angle of 90 deg and a straight line to the end\_lane.

Parameters
:   Table 211. Parameters for modifier map.crossing\_connects()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | crossing | [crossing](#sec-roads-class-crossing) | The crossing that will be connected to the specified lanes. |
    | start\_lane | [lane](#sec-roads-class-lane) | The lane where crossing starts (starting from the lane’s centerline). |
    | end\_lane | [lane](#sec-roads-class-lane) | The destination lane where the crossing ends (ending on the lane’s centerline). |
    | start\_s\_coord | [length](physical_types.html#sec-physical_types-class-length) | The crossing origin derived from a s-position along the centerline of start\_lane. |
    | start\_angle | [angle](physical_types.html#sec-physical_types-class-angle) | Optional. The angle at which the straight centerline of the crossing originates from the start lane. Default is perpendicular. |

Syntax
:   ```
    my_cross: crossing
    sidewalk_1, sidewalk_2: lane
    map.crossing_connects(my_cross, sidewalk_1, sidewalk_2, 5m)
    ```

```
my_cross: crossing
sidewalk_3, sidewalk_4: lane
map.crossing_connects(my_cross, sidewalk_3, sidewalk_4, 5m, 60deg)
```

|  |  |
| --- | --- |
|  | In the future geometric constraints could be used within this modifier if the approach to the end\_lane was an unusual shape rather than a straight line. |

#### 8.12.2.2.10 Modifier routes\_are\_opposite()

Specifies that two routes are in opposite directions.

Table 212. Parameters for modifier map.routes\_are\_opposite()


| Parameter | Type | Description |
| --- | --- | --- |
| route1 | [route](#sec-roads-class-route) | The first uni-directional route. |
| route2 | [route](#sec-roads-class-route) | The second uni-directional route.  If route1 has no opposite, then route2 is null. |
| containing\_road | [road](#sec-roads-class-road) | The road to which both routes belong. |
| lateral\_overlap | [lateral\_overlap\_kind](#sec-roads-enum-lateral_overlap_kind) | Specifies if the routes overlap lateral, meaning they become a single two-way lane. |

#### 8.12.2.2.11 Modifier set\_map\_file()

Setting a map file.

Parameters
:   Table 213. Parameters for modifier map.set\_map\_file()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | file | string | The path and file name for the map file. |

Syntax
:   ```
    map.set_map_file("path/to/map/my_odr_map.xodr")
    ```

#### 8.12.2.2.12 Modifier set\_traffic\_lights\_control\_file()

Specifies a file with traffic lights control cycles.
This file references traffic lights or control groups defined in the map file (specified by modifier modifier `map.set_map_file`).
Traffic light states that are not applicable to the referenced traffic lights may result in undefined behavior.
Calling this modifier results in population of `map.traffic_light_control`.

Parameters
:   Table 214. Parameters for modifier map.set\_traffic\_lights\_control\_file()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | file | string | The path and file name for the control file. |

Syntax
:   ```
    map.set_traffic_lights_control_file("path/to/traffic/lights/control.file")
    ```

    This specifies `map.traffic_light_control`.

## 8.12.3 Enum driving\_rule

Values
:   Table 215. Enum driving\_rule


    | Value | Comment |
    | --- | --- |
    | left\_hand\_traffic | Traffic drives on the left side of the [road](#sec-roads-class-road) |
    | right\_hand\_traffic | Traffic drives on the right side of the [road](#sec-roads-class-road) |

## 8.12.4 Struct junction

A junction connects roads.

Basic information
:   Table 216. Basic information of struct junction


    |  |  |
    | --- | --- |
    | **Used by** | [map](#sec-roads-class-map) |

Parameters
:   Table 217. Struct junction


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | roads | list of road | yes | List of [road](#sec-roads-class-road) elements that are connected to this [junction](#sec-roads-class-junction) |

## 8.12.5 Struct route

A route is a location where a movable\_object can move, creating a behavioral pathway for the actors in the scenario.
An instance of `route` can be a single *route\_element* (for example, lane), or it can be composed of a sequence with multiple instances of *route\_element*.

The s-t-coordinates in a route:

* Each route has an s-t-coordinate system.

  + The s-axis increases longitudinally along the route.
  + The t-axis is perpendicular to the s-axis, following the right-hand-rule, with positive values to the left side of the s-axis.
* In modifiers that specify movement relative to another reference entity, this implies using the s-t-coordinates of the lane where the reference vehicle is located.

  + Example: `car1.drive() with: position(100m, ahead_of: car2)` measures the 100 m relative to the lane that car2 is in.
* The result of requesting *drive()* along a split route or a bi-directional route is undefined.
  The request should result in an error, unless the direction is specified in some other way.

Basic information
:   Table 218. Basic information of struct route


    |  |  |
    | --- | --- |
    | **Children** | [compound\_lane](#sec-roads-class-compound_lane), [compound\_route](#sec-roads-class-compound_route), [route\_element](#sec-roads-abstract-route_element) |
    | **Used by** | [map](#sec-roads-class-map) |

Parameters
:   Table 219. Struct route


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | length | [length](physical_types.html#sec-physical_types-class-length) | no | Nominal length of the route, measured along the s-axis of the route. Does not apply to [route\_point](#sec-roads-class-route_point) |
    | [directionality](#sec-roads-enum-directionality) | [directionality](#sec-roads-enum-directionality) | yes | Directionality for movement of [traffic\_participant](entity.html#sec-trafficparticipant-abstract-traffic_participant) actors on the [route](#sec-roads-class-route) |
    | min\_lanes | uint | no | Minimum number of drivable lanes along this route. Applies only to these children: road, [lane\_section](#sec-roads-class-lane_section) |
    | max\_lanes | uint | no | Maximum number of drivable lanes along this route. Applies only to these children: road, [lane\_section](#sec-roads-class-lane_section) |
    | anchors | list of string | no | The strings in here can be matched to unique items in the [map](#sec-roads-class-map) files specified in file\_name |

### 8.12.5.1 Methods

#### 8.12.5.1.1 Method start\_point()

Returns the start point of the route, where the s-coordinate has its minimum value (typically zero).

Prototype
:   ```
    extend route:
        def start_point() -> route_point
    ```

Return value
:   Returns a *route\_point*.

#### 8.12.5.1.2 Method end\_point()

Returns the end point of the route, where the s-coordinate has its maximum value.
The difference between the maximum and minimum values of the s-coordinate on the route is equal to the length of the route measured along the s-axis of the route.

Prototype
:   ```
    extend route:
        def end_point() -> route_point
    ```

Return value
:   Returns a *route\_point*.

## 8.12.6 Enum directionality

Directionality of the route

Values
:   Table 220. Enum directionality


    | Value | Comment |
    | --- | --- |
    | uni\_direction | A [traffic\_participant](entity.html#sec-trafficparticipant-abstract-traffic_participant) can [move](actions.html#sec-actions_movableobjects-class-move) legally in only one direction along the longitudinal s-axis. Usually applies to [lane\_type](#sec-roads-enum-lane_type) driving and vru\_vehicles |
    | bi\_direction | A [traffic\_participant](entity.html#sec-trafficparticipant-abstract-traffic_participant) can [move](actions.html#sec-actions_movableobjects-class-move) legally in both directions along the longitudinal s-axis. Usually applies to [lane\_type](#sec-roads-enum-lane_type) driving and vru\_vehicles |
    | split | Applies for multi-lane elements: there are lanes with opposing uni\_direction traffic flow within the [route](#sec-roads-class-route) |
    | free | A [traffic\_participant](entity.html#sec-trafficparticipant-abstract-traffic_participant) can legally [move](actions.html#sec-actions_movableobjects-class-move) in any direction (longitudinal or lateral). Usually applies to [lane\_type](#sec-roads-enum-lane_type) pedestrian or [lane\_use](#sec-roads-enum-lane_use) mix\_traffic\_vru |
    | none | No expected traffic flow. Usually applies to [lane\_type](#sec-roads-enum-lane_type) non\_driving |
    | other | Other type of [directionality](#sec-roads-enum-directionality) |

## 8.12.7 Struct route\_element

A route\_element that is a lower-level route, which can be used individualy, or can be part of a compound\_route.

Basic information
:   Table 221. Basic information of struct route\_element


    |  |  |
    | --- | --- |
    | **Parents** | [route](#sec-roads-class-route) |
    | **Children** | [crossing](#sec-roads-class-crossing), [geodetic\_point](#sec-roads-class-geodetic_point), [lane](#sec-roads-class-lane), [lane\_section](#sec-roads-class-lane_section), [odr\_point](#sec-roads-class-odr_point), [path](#sec-paths-class-path), [road](#sec-roads-class-road), [route\_point](#sec-roads-class-route_point), [xyz\_point](#sec-roads-class-xyz_point) |

Inherited parameters and variables
:   Table 222. Inherited parameters and variables of struct route\_element


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.8 Struct road

A road is composed by ordered lists of lane\_section, organized end-to-end (longitudinal direction, or s-direction).

A `road` is composed of instances of `lane_section` arranged end-to-end.
A `road` can only be connected with another `road` in a `junction`.

A road has two separate ordered lists of `lane_section`:

1. The *s\_positive* (mandatory) list of *lane\_section* contains the uni-directional lanes flowing in the positive road-s-direction.
2. The *s\_negative* (optional) list of *lane\_section* contains the uni-directional lanes flowing in the negative road-s-direction.

   * Both lists can include lanes with other directionalities.
   * Successive lane\_section elements in the list can have different properties (number of lanes, lane types, lane use, directionality, and so on).
   * A road has an s-t-coordinate system.
   * The s-axis of the road coincides with the s-axis of *s\_positive*.
   * A road can only be connected with another road in a junction.

Basic information
:   Table 223. Basic information of struct road


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |
    | **Has connection to** | [junction](#sec-roads-class-junction) |

Parameters
:   Table 224. Struct road


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | s\_positive | list of lane\_section | yes | List of [lane\_section](#sec-roads-class-lane_section) elements that flow in the positive direction of the [road](#sec-roads-class-road) s-axis |
    | s\_negative | list of lane\_section | no | List of [lane\_section](#sec-roads-class-lane_section) elements that flow in the negative direction of the [road](#sec-roads-class-road) s-axis |

Inherited parameters and variables
:   Table 225. Inherited parameters and variables of struct road


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.9 Struct lane\_section

A block of one or more lanes, organized side-by-side (lateral direction, or T-direction).

A section composed of lanes arranged side-by-side.
A `road` can be composed of one or multiple instances of `lane_section` arranged end-to-end.
Lane sections are useful for these purposes:

* Change the *number* of lanes over the course of a single road.
* Change the *type* of lanes within a single road.
* Change the *use* of lanes within a single road.
* Change the *directionality* of lanes within a single road.

The representation of `lane_section` is similar to the implementation in ASAM OpenDRIVE.

* The number of lanes is constant in the whole lane section.
* Lanes cannot change `lane_type` or `lane_use` or `directionality` within the lane section.
* A lane section has an s-t-coordinate system.
* The s-axis of the lane section coincides with the s-axis of the lane chosen with the (mandatory) `s_axis` property.

Basic information
:   Table 226. Basic information of struct lane\_section


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |
    | **Used by** | [road](#sec-roads-class-road) |

Parameters
:   Table 227. Struct lane\_section


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [road](#sec-roads-class-road) | [road](#sec-roads-class-road) | yes | Where the [lane\_section](#sec-roads-class-lane_section) resides |
    | lanes | list of lane | yes | List of lanes that compose the [lane\_section](#sec-roads-class-lane_section) |
    | s\_axis | [lane](#sec-roads-class-lane) | yes | Choose, which [lane](#sec-roads-class-lane) is used to determine the s-axis of the lane\_section. Must be a member of it.lanes |

Inherited parameters and variables
:   Table 228. Inherited parameters and variables of struct lane\_section


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.10 Struct lane

A lane is pathway that has limits for movement.
These limits are typically indicated by lane lines providing an indication of boundaries to traffic participants.

* A lane has an s-t-coordinate system.
* The lane s-axis goes along the centerline of the lane.
* The lane t-axis is perpendicular to the s-axis, following the right-hand-rule.
* For a lane with `directionality == uni_directional`, the legal traffic always moves in the positive s-direction.
* One or multiple adjacent lanes arranged side-by-side compose a `lane_section`.

Basic information
:   Table 229. Basic information of struct lane


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |
    | **Used by** | [lane\_section](#sec-roads-class-lane_section) |

Parameters
:   Table 230. Struct lane


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [lane\_section](#sec-roads-class-lane_section) | [lane\_section](#sec-roads-class-lane_section) | yes | Where the [lane](#sec-roads-class-lane) resides |
    | [lane\_type](#sec-roads-enum-lane_type) | [lane\_type](#sec-roads-enum-lane_type) | yes | Type of [lane](#sec-roads-class-lane) |
    | [lane\_use](#sec-roads-enum-lane_use) | [lane\_use](#sec-roads-enum-lane_use) | yes | A subtype of the lane\_type. Use compatible pairs of [lane\_type](#sec-roads-enum-lane_type) and [lane\_use](#sec-roads-enum-lane_use) |
    | width | [length](physical_types.html#sec-physical_types-class-length) | no | Nominal width of the [lane](#sec-roads-class-lane) |

Inherited parameters and variables
:   Table 231. Inherited parameters and variables of struct lane


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.11 Struct crossing

A crossing is overlaid on existing lanes. It allows different types of usage to take place on the same surface. A typical example is a crosswalk overlaid on drivable lanes.

Basic information
:   Table 232. Basic information of struct crossing


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |

Parameters
:   Table 233. Struct crossing


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | start\_lane | [lane](#sec-roads-class-lane) | yes | Crossing starts on this [lane](#sec-roads-class-lane) |
    | end\_lane | [lane](#sec-roads-class-lane) | yes | Crossing ends on this [lane](#sec-roads-class-lane) |
    | start\_s\_coord | [length](physical_types.html#sec-physical_types-class-length) | yes | On the starts\_from lane, the [crossing](#sec-roads-class-crossing) connects [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) this point in the [lane](#sec-roads-class-lane) s-axis (and zero in the t-axis) |
    | end\_s\_coord | [length](physical_types.html#sec-physical_types-class-length) | yes | On the ends\_on lane, the [crossing](#sec-roads-class-crossing) connects [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) this point in the [lane](#sec-roads-class-lane) s-axis (and zero in the t-axis) |
    | width | [length](physical_types.html#sec-physical_types-class-length) | yes | Nominal width of the crossing, measured perpendicular to the [crossing](#sec-roads-class-crossing) s-axis |
    | [crossing\_type](#sec-roads-class-crossing_type) | [crossing\_type](#sec-roads-class-crossing_type) | yes | Type of [crossing](#sec-roads-class-crossing) |

Inherited parameters and variables
:   Table 234. Inherited parameters and variables of struct crossing


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.12 Enum lane\_type

Basic information
:   Table 235. Basic information of enum lane\_type


    |  |  |
    | --- | --- |
    | **Used by** | [lane](#sec-roads-class-lane) |

Values
:   Table 236. Enum lane\_type


    | Value | Comment |
    | --- | --- |
    | driving | Driving [lane](#sec-roads-class-lane) for [road](#sec-roads-class-road) vehicles. See the driving\_lane\_use subtype |
    | non\_driving | Non-driving lanes in [road](#sec-roads-class-road) vehicles infrastructure. See the non\_driving\_lane\_use subtype |
    | vru\_vehicles | Lanes designated for VRU vehicles. See the vru\_vehicles\_lane\_use subtype |
    | pedestrian | Lanes for pedestrians. See the pedestrian\_lane\_use subtype |
    | other | If the [lane](#sec-roads-class-lane) has another type |

## 8.12.13 Enum lane\_use

Subtype of the lane\_type enum. lane\_use contains all values from all use types

Basic information
:   Table 237. Basic information of enum lane\_use


    |  |  |
    | --- | --- |
    | **Used by** | [lane](#sec-roads-class-lane) |

Values
:   Table 238. Enum lane\_use


    | Value | Comment |
    | --- | --- |
    | normal | A normal driving [lane](#sec-roads-class-lane) for [road](#sec-roads-class-road) vehicles (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving. |
    | exit | A deceleration [lane](#sec-roads-class-lane) in parallel to the main [road](#sec-roads-class-road) (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving. |
    | entry | An acceleration [lane](#sec-roads-class-lane) in parallel to the main [road](#sec-roads-class-road) (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving. |
    | on\_ramp | A ramp from rural or urban roads joining a motorway (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving. |
    | off\_ramp | A ramp leading off a motorway onto rural or urban roads (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving. |
    | connecting\_ramp | A ramp that connects two motorways (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving. |
    | hov | A [lane](#sec-roads-class-lane) for High Occupancy Vehicles (HOV), usually in highways. Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving. |
    | bus | A [lane](#sec-roads-class-lane) restricted for use only by busses. Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving. |
    | mixed\_traffic\_vru | A [lane](#sec-roads-class-lane) for mixed car and vru (vehicle and pedestrian) traffic, normally in urban areas. Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == driving or vru\_vehicles. |
    | parking | A [lane](#sec-roads-class-lane) with parking spaces (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == non\_driving. |
    | stop | A hard shoulder on motorways for emergency stops (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == non\_driving. |
    | restricted | A [lane](#sec-roads-class-lane) on which [road](#sec-roads-class-road) vehicles should not [drive](actions.html#sec-actions_vehicles-class-drive) (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == non\_driving. |
    | border | A hard border on the edge of a [road](#sec-roads-class-road) (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == non\_driving. |
    | shoulder | A soft border on the edge of a [road](#sec-roads-class-road) (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == non\_driving. |
    | curb | An elevated surface with different height compared to the drivable lanes. Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == non\_driving. |
    | median | An inaccessible [lane](#sec-roads-class-lane) for [road](#sec-roads-class-road) vehicles and pedestrians. Typically used to separate the traffic. Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == non\_driving. |
    | bicycle | A [lane](#sec-roads-class-lane) that is designated for bicycles (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == vru\_vehicles. |
    | motorcycle | A [lane](#sec-roads-class-lane) that is designated for motorcycles. Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == vru\_vehicles. |
    | sidewalk | A [lane](#sec-roads-class-lane) that is designated for pedestrians (OSI). Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == pedestrian. |
    | protected\_sidewalk | A [lane](#sec-roads-class-lane) for pedestrians with a barrier to separate it from [road](#sec-roads-class-road) traffic. Should be used in combination with [lane\_type](#sec-roads-enum-lane_type) == pedestrian. |
    | none | The [lane](#sec-roads-class-lane) has no use. |
    | other | The [lane](#sec-roads-class-lane) has another use. |

## 8.12.14 Enum side\_left\_right

Values
:   Table 239. Enum side\_left\_right


    | Value | Comment |
    | --- | --- |
    | left | On the left side of the [lane](#sec-roads-class-lane) |
    | right | On the right side of the [lane](#sec-roads-class-lane) |

## 8.12.15 Enum lon\_lat

Values
:   Table 240. Enum lon\_lat


    | Value | Comment |
    | --- | --- |
    | longitudinal | Refers to longitudinal direction |
    | lateral | Refers to lateral direction |

## 8.12.16 Struct crossing\_type

Basic information
:   Table 241. Basic information of struct crossing\_type


    |  |  |
    | --- | --- |
    | **Used by** | [crossing](#sec-roads-class-crossing) |

Parameters
:   Table 242. Struct crossing\_type


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | marking | [crossing\_marking](#sec-roads-enum-crossing_marking) | no | Define the type of markings on the [crossing](#sec-roads-class-crossing) |
    | use | [crossing\_use](#sec-roads-enum-crossing_use) | no | Define the type of use for the [crossing](#sec-roads-class-crossing) |
    | elevation | [crossing\_elevation](#sec-roads-enum-crossing_elevation) | no | Define the type of elevation for the [crossing](#sec-roads-class-crossing) |

## 8.12.17 Enum crossing\_marking

Basic information
:   Table 243. Basic information of enum crossing\_marking


    |  |  |
    | --- | --- |
    | **Used by** | [crossing\_type](#sec-roads-class-crossing_type) |

Values
:   Table 244. Enum crossing\_marking


    | Value | Comment |
    | --- | --- |
    | unmarked | No crossing-markings on the [road](#sec-roads-class-road) |
    | marked | The [road](#sec-roads-class-road) or walking surface has markings that indicate a [crossing](#sec-roads-class-crossing) |
    | zebra | Common type of marked [crossing](#sec-roads-class-crossing) with thick zebra stripes |
    | other | Other type of markings for the [crossing](#sec-roads-class-crossing) |

## 8.12.18 Enum crossing\_use

Basic information
:   Table 245. Basic information of enum crossing\_use


    |  |  |
    | --- | --- |
    | **Used by** | [crossing\_type](#sec-roads-class-crossing_type) |

Values
:   Table 246. Enum crossing\_use


    | Value | Comment |
    | --- | --- |
    | pedestrian | Crossing is used by pedestrians (person, animal) and/or vehicles that usually [move](actions.html#sec-actions_movableobjects-class-move) on sidewalks (wheelchair, stroller) |
    | [animal](entity.html#sec-trafficparticipant-entity-animal) | Animal crossing. For example, on a rural [road](#sec-roads-class-road) or highway |
    | bicycle | Crossing for bicycles |
    | rail\_road | Crossing for rail vehicles (train, subway, tram, …​) |
    | other | Other use for [crossing](#sec-roads-class-crossing) |

## 8.12.19 Enum crossing\_elevation

Basic information
:   Table 247. Basic information of enum crossing\_elevation


    |  |  |
    | --- | --- |
    | **Used by** | [crossing\_type](#sec-roads-class-crossing_type) |

Values
:   Table 248. Enum crossing\_elevation


    | Value | Comment |
    | --- | --- |
    | road\_level | Crossing is [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) same level as driving surface |
    | curb\_level | Crossing is elevated from driving surface, often [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) the same level as a walking surface (sidewalk) or curb |
    | refuge\_island | Along the crossing, the elevation may change between [road](#sec-roads-class-road) and curb levels. For example, with refuge island(s) in the middle |
    | other | Another elevation type |

## 8.12.20 Struct compound\_route

A compound\_route is a connected sequence of route elements.

Basic information
:   Table 249. Basic information of struct compound\_route


    |  |  |
    | --- | --- |
    | **Parents** | [route](#sec-roads-class-route) |

Parameters
:   Table 250. Struct compound\_route


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | route\_elements | list of route\_element | yes | A list of route\_element. |

Inherited parameters and variables
:   Table 251. Inherited parameters and variables of struct compound\_route


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.21 Struct compound\_lane

A connected sequence of lanes.

Basic information
:   Table 252. Basic information of struct compound\_lane


    |  |  |
    | --- | --- |
    | **Parents** | [route](#sec-roads-class-route) |

Parameters
:   Table 253. Struct compound\_lane


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | lanes | list of lane | yes | A list of [lane](#sec-roads-class-lane) |

Inherited parameters and variables
:   Table 254. Inherited parameters and variables of struct compound\_lane


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.22 Enum junction\_direction

In a junction, indicate the direction of the out\_road relative to the in\_road, measuring the angle clockwise. All angles +/- 10 deg.

Values
:   Table 255. Enum junction\_direction


    | Value | Comment |
    | --- | --- |
    | straight | The out\_road is 0deg relative to the in\_road |
    | right | The out\_road is 90deg relative to the in\_road |
    | u\_turn | The out\_road is 180deg relative to the in\_road |
    | left | The out\_road is 270deg relative to the in\_road |
    | other | If none of the above apply |

## 8.12.23 Enum route\_overlap\_kind

What type of longitudinal overlap is expected for a pair of routes.

Values
:   Table 256. Enum route\_overlap\_kind


    | Value | Comment |
    | --- | --- |
    | equal | Both routes have the same length, and coincide [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) the start and end points |
    | start | Both routes coincide [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) their start points |
    | end | Both routes coincide [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) their end points |
    | inside | The first [route](#sec-roads-class-route) is fully inside the second route. Their start and end points do not have to coincide |
    | any | Any part of the first [route](#sec-roads-class-route) overlaps with any part of the second [route](#sec-roads-class-route) |
    | other | If none of the above apply |

## 8.12.24 Enum lateral\_overlap\_kind

Type of lateral overlap is expected for a pair of routes.

Values
:   Table 257. Enum lateral\_overlap\_kind


    | Value | Comment |
    | --- | --- |
    | never | The two routes never overlap laterally. They never share a common lane. |
    | sometimes | In some segments of the route, the two routes can share a common lane. |
    | always | The routes always share a common lane. |

## 8.12.25 Struct route\_point

A point on the route network specified in route s-t-coordinates.

Basic information
:   Table 258. Basic information of struct route\_point


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |
    | **Used by** | [relative\_path\_st](#sec-paths-class-relative_path_st), [relative\_trajectory\_st](#sec-trajectories-class-relative_trajectory_st) |

Parameters
:   Table 259. Struct route\_point


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [route](#sec-roads-class-route) | [route](#sec-roads-class-route) | Yes | [route](#sec-roads-class-route) in which this point is located |
    | s | [length](physical_types.html#sec-physical_types-class-length) | No | Coordinate along the s-axis of the corresponding [route](#sec-roads-class-route) |
    | t | [length](physical_types.html#sec-physical_types-class-length) | No | Coordinate along the t-axis of the corresponding [route](#sec-roads-class-route) |

Inherited parameters and variables
:   Table 260. Inherited parameters and variables of struct route\_point


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.26 Struct xyz\_point

A pose in space specified in Cartesian x-y-z-coordinates.

Basic information
:   Table 261. Basic information of struct xyz\_point


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |

Parameters
:   Table 262. Struct xyz\_point


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | position | [position\_3d](physical_types.html#sec-physical_types-class-position_3d) | No | Position in Cartesian x-y-z-coordinates |

Inherited parameters and variables
:   Table 263. Inherited parameters and variables of struct xyz\_point


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.27 Struct odr\_point

A point expressed in ASAM OpenDRIVE coordinates.

Basic information
:   Table 264. Basic information of struct odr\_point


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |
    | **Used by** | [relative\_path\_odr](#sec-paths-class-relative_path_odr), [relative\_trajectory\_odr](#sec-trajectories-class-relative_trajectory_odr) |

Parameters
:   Table 265. Struct odr\_point


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | road\_id | string | Yes | ASAM OpenDRIVE identifier for the [road](#sec-roads-class-road) |
    | lane\_id | string | No | ASAM OpenDRIVE identifier for the lane. If specified, the t-coordinate is measured from the [lane](#sec-roads-class-lane) centerline. If not specified, the t-coordinate is measured from the ASAM OpenDRIVE reference line |
    | s | [length](physical_types.html#sec-physical_types-class-length) | No | Coordinate along the ASAM OpenDRIVE s-axis |
    | t | [length](physical_types.html#sec-physical_types-class-length) | No | Coordinate along the ASAM OpenDRIVE t-axis |

Inherited parameters and variables
:   Table 266. Inherited parameters and variables of struct odr\_point


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.28 Struct geodetic\_point

A point in space specified in Geographic (latitude, longitude, altitude) coordinates.

Basic information
:   Table 267. Basic information of struct geodetic\_point


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |

Parameters
:   Table 268. Struct geodetic\_point


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | latitude | angle | yes | The latitude of a point on the surface of the earth is the angle between the equatorial plane and the straight line that passes through that point and through the center of the earth. Range: [-90deg..90deg] |
    | longitude | angle | yes | The longitude of a point on the surface of the earth is the angle east or west of a reference meridian to another meridian that passes through that point. Range: [-180deg..180deg] |
    | altitude | length | no | Altitude is the earth gravity-related vertical distance from the target position, specified horizontally by its Longitude/Latitude coordinates, to the closest point on the underlying [road](#sec-roads-class-road) surface. When calculating the closest point, it is accounted for an elevation of the road, an entire [road](#sec-roads-class-road) super-elevation, or, in more complex cases, a [road](#sec-roads-class-road) lateral shape profile that are specified in the [road](#sec-roads-class-road) network definition (external to the OpenSCENARIO). Missing value is interpreted as 0. Range: [0m..inf[ |

Inherited parameters and variables
:   Table 269. Inherited parameters and variables of struct geodetic\_point


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.29 Enum connect\_route\_points

When building a compound\_route, determine which route\_element shall be used to compose the compound\_route if routable point types (i.e. xyz\_point, route\_point or odr\_point) are part of the list.

Values
:   Table 270. Enum connect\_route\_points


    | Value | Comment |
    | --- | --- |
    | [road](#sec-roads-class-road) | Use the [road](#sec-roads-class-road) element that contains this point |
    | [lane\_section](#sec-roads-class-lane_section) | Use the [lane\_section](#sec-roads-class-lane_section) element that contains this point |
    | [lane](#sec-roads-class-lane) | Use the [lane](#sec-roads-class-lane) element that contains this point |
    | [crossing](#sec-roads-class-crossing) | Use the [crossing](#sec-roads-class-crossing) element that contains this point |
    | waypoint | Use the point itself. The [route](#sec-roads-class-route) must pass exactly through this point |

## 8.12.30 Struct path

An absolute path expressed in Cartesian x-y-z-coordinates, measured in the global world coordinate system.

Basic information
:   Table 271. Basic information of struct path


    |  |  |
    | --- | --- |
    | **Parents** | [route\_element](#sec-roads-abstract-route_element) |

Parameters
:   Table 272. Struct path


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | points | list of [pose\_3d](physical_types.html#sec-physical_types-class-pose_3d) | Yes | List of points in world x-y-z-coordinates. The individual pose\_3d elements can have unconstrained coordinates. |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | yes | Choose how to join the points of the path. |

Inherited parameters and variables
:   Table 273. Inherited parameters and variables of struct path


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](#sec-roads-class-route) | [length](#tab-roads-class-route-info), [directionality](#tab-roads-class-route-info), [min\_lanes](#tab-roads-class-route-info), [max\_lanes](#tab-roads-class-route-info), [anchors](#tab-roads-class-route-info) |

## 8.12.31 Struct relative\_path

A relative path is a sequence of points measured with respect to a reference entity. These points can be expressed in Cartesian x-y-z-coordinates, route s-t-coordinates or ASAM OpenDRIVE coordinates.

Basic information
:   Table 274. Basic information of struct relative\_path


    |  |  |
    | --- | --- |
    | **Children** | [relative\_path\_odr](#sec-paths-class-relative_path_odr), [relative\_path\_pose\_3d](#sec-paths-class-relative_path_pose_3d), [relative\_path\_st](#sec-paths-class-relative_path_st) |

Parameters
:   Table 275. Struct relative\_path


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | yes | Choose how to join the points of the path. |

## 8.12.32 Struct relative\_path\_pose\_3d

A relative path expressed in Cartesian x-y-z-coordinates, measured in the local coordinate frame of the reference entity.

Basic information
:   Table 276. Basic information of struct relative\_path\_pose\_3d


    |  |  |
    | --- | --- |
    | **Parents** | [relative\_path](#sec-paths-abstract-relative_path) |

Parameters
:   Table 277. Struct relative\_path\_pose\_3d


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | points | list of [pose\_3d](physical_types.html#sec-physical_types-class-pose_3d) | Yes | List of points in world x-y-z-coordinates. The individual pose\_3d elements can have unconstrained coordinates. |

Inherited parameters and variables
:   Table 278. Inherited parameters and variables of struct relative\_path\_pose\_3d


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [relative\_path](#sec-paths-abstract-relative_path) | [interpolation](#tab-paths-abstract-relative_path-info) |

## 8.12.33 Struct relative\_path\_st

A relative path expressed in route s-t-coordinates, measured with respect to a reference entity.

Basic information
:   Table 279. Basic information of struct relative\_path\_st


    |  |  |
    | --- | --- |
    | **Parents** | [relative\_path](#sec-paths-abstract-relative_path) |

Parameters
:   Table 280. Struct relative\_path\_st


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | points | list of [route\_point](#sec-roads-class-route_point) | Yes | Sequence of [route\_point](#sec-roads-class-route_point) that form the relative [path](#sec-paths-class-path) |

Inherited parameters and variables
:   Table 281. Inherited parameters and variables of struct relative\_path\_st


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [relative\_path](#sec-paths-abstract-relative_path) | [interpolation](#tab-paths-abstract-relative_path-info) |

## 8.12.34 Struct relative\_path\_odr

A relative path expressed in ASAM OpenDRIVE coordinates, measured with respect to a reference entity.

Basic information
:   Table 282. Basic information of struct relative\_path\_odr


    |  |  |
    | --- | --- |
    | **Parents** | [relative\_path](#sec-paths-abstract-relative_path) |

Parameters
:   Table 283. Struct relative\_path\_odr


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | points | list of odr\_point | Yes | Sequence of [odr\_point](#sec-roads-class-odr_point) that form the relative [path](#sec-paths-class-path) |

Inherited parameters and variables
:   Table 284. Inherited parameters and variables of struct relative\_path\_odr


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [relative\_path](#sec-paths-abstract-relative_path) | [interpolation](#tab-paths-abstract-relative_path-info) |

## 8.12.35 Enum path\_interpolation

Choose how to join the list of points in a path or trajectory

Values
:   Table 285. Enum path\_interpolation


    | Value | Comment |
    | --- | --- |
    | straight\_line | Join the points with straight lines |
    | smooth | Join the points with a smooth line |

## 8.12.36 Enum relative\_transform

Type of transformation to resolve relative points into absolute coordinates

Basic information
:   Table 286. Basic information of enum relative\_transform


    |  |  |
    | --- | --- |
    | **Used by** | [follow\_path](actions.html#sec-actions_movableobjects-class-follow_path), [follow\_trajectory](actions.html#sec-actions_movableobjects-class-follow_trajectory), [replay\_path](actions.html#sec-actions_movableobjects-class-replay_path), [replay\_trajectory](actions.html#sec-actions_movableobjects-class-replay_trajectory) |

Values
:   Table 287. Enum relative\_transform


    | Value | Comment |
    | --- | --- |
    | world\_relative | Use the global coordinate system axes |
    | object\_relative | Use the reference object local coordinate system axes |
    | road\_relative | Use the s-t coordinate system of the [road](#sec-roads-class-road) where the reference object is located |
    | lane\_relative | Use the s-t coordinate system of the [lane](#sec-roads-class-lane) where the reference object is located |

## 8.12.37 Struct trajectory

An absolute trajectory expressed in Cartesian x-y-z-coordinates, measured in the global world coordinate system.

Basic information
:   Table 288. Basic information of struct trajectory


    |  |  |
    | --- | --- |
    | **Used by** | hidden |

Parameters
:   Table 289. Struct trajectory


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | points | list of [pose\_3d](physical_types.html#sec-physical_types-class-pose_3d) | Yes | List of points in world x-y-z-coordinates. The individual pose\_3d elements can have unconstrained coordinates. |
    | time\_stamps | list of [time](physical_types.html#sec-physical_types-class-time) | Yes | Time stamps for each element in points. The lists time\_stamps and points must have the same length. |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | yes | Choose how to join the points of the trajectory. |

## 8.12.38 Struct relative\_trajectory

A relative trajectory is a sequence of points measured with respect to a reference entity, where the points must be traversed at specific moments in time. These points can be expressed in Cartesian x-y-z-coordinates, route s-t-coordinates or ASAM OpenDRIVE coordinates.

Basic information
:   Table 290. Basic information of struct relative\_trajectory


    |  |  |
    | --- | --- |
    | **Children** | [relative\_trajectory\_odr](#sec-trajectories-class-relative_trajectory_odr), [relative\_trajectory\_pose\_3d](#sec-trajectories-class-relative_trajectory_pose_3d), [relative\_trajectory\_st](#sec-trajectories-class-relative_trajectory_st) |

Parameters
:   Table 291. Struct relative\_trajectory


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | time\_stamps | list of [time](physical_types.html#sec-physical_types-class-time) | Yes | Time stamps for each element in points. The lists time\_stamps and points must have the same length |
    | interpolation | [path\_interpolation](#sec-paths-enum-path_interpolation) | yes | Choose how to join the points of the trajectory. |

## 8.12.39 Struct relative\_trajectory\_pose\_3d

A relative trajectory expressed in Cartesian x-y-z-coordinates, measured in the local coordinate frame of the reference entity.

Basic information
:   Table 292. Basic information of struct relative\_trajectory\_pose\_3d


    |  |  |
    | --- | --- |
    | **Parents** | [relative\_trajectory](#sec-trajectories-abstract-relative_trajectory) |

Parameters
:   Table 293. Struct relative\_trajectory\_pose\_3d


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | points | list of [pose\_3d](physical_types.html#sec-physical_types-class-pose_3d) | Yes | List of points in world x-y-z-coordinates. The individual pose\_3d elements can have some unspecified coordinates. |

Inherited parameters and variables
:   Table 294. Inherited parameters and variables of struct relative\_trajectory\_pose\_3d


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [relative\_trajectory](#sec-trajectories-abstract-relative_trajectory) | [time\_stamps](#tab-trajectories-abstract-relative_trajectory-info), [interpolation](#tab-trajectories-abstract-relative_trajectory-info) |

## 8.12.40 Struct relative\_trajectory\_st

A relative trajectory expressed in route s-t-coordinates, measured with respect to a reference entity.

Basic information
:   Table 295. Basic information of struct relative\_trajectory\_st


    |  |  |
    | --- | --- |
    | **Parents** | [relative\_trajectory](#sec-trajectories-abstract-relative_trajectory) |

Parameters
:   Table 296. Struct relative\_trajectory\_st


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | points | list of [route\_point](#sec-roads-class-route_point) | Yes | Sequence of [route\_point](#sec-roads-class-route_point) that form the relative [trajectory](#sec-trajectories-class-trajectory) |

Inherited parameters and variables
:   Table 297. Inherited parameters and variables of struct relative\_trajectory\_st


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [relative\_trajectory](#sec-trajectories-abstract-relative_trajectory) | [time\_stamps](#tab-trajectories-abstract-relative_trajectory-info), [interpolation](#tab-trajectories-abstract-relative_trajectory-info) |

## 8.12.41 Struct relative\_trajectory\_odr

A relative trajectory expressed in ASAM OpenDRIVE coordinates, measured with respect to a reference entity.

Basic information
:   Table 298. Basic information of struct relative\_trajectory\_odr


    |  |  |
    | --- | --- |
    | **Parents** | [relative\_trajectory](#sec-trajectories-abstract-relative_trajectory) |

Parameters
:   Table 299. Struct relative\_trajectory\_odr


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | points | list of odr\_point | Yes | Sequence of [odr\_point](#sec-roads-class-odr_point) that form the relative [trajectory](#sec-trajectories-class-trajectory) |

Inherited parameters and variables
:   Table 300. Inherited parameters and variables of struct relative\_trajectory\_odr


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [relative\_trajectory](#sec-trajectories-abstract-relative_trajectory) | [time\_stamps](#tab-trajectories-abstract-relative_trajectory-info), [interpolation](#tab-trajectories-abstract-relative_trajectory-info) |