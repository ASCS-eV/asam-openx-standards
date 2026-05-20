# ASAM OpenSCENARIO® DSL v2.2.0 — 8.5 Abstract road network

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/dm_abstract_road_network.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.5 Abstract road network

The ASAM OpenSCENARIO language allows users to describe key aspects of the map in which the scenario shall take place.

This ASAM OpenSCENARIO description is not a replacement for a fully detailed geometric map.
Such descriptions can be found in a map file.
Rather, it is an abstract description of the features of the road network that influence the behavior of the actors during the scenario.

This section explains the main concepts of the ASAM OpenSCENARIO road abstraction and how road abstraction can be used for scenario description.

## 8.5.1 Roads, maps, and scenarios

This part of the ASAM OpenSCENARIO domain model is placed under the [`map`](road_abstractions.html#sec-roads-class-map) actor.
The classes and modifiers under the [`map`](road_abstractions.html#sec-roads-class-map) actor can be used to describe an abstract road network (ARN).

This abstract road network can then be used as a location proxy for the specification of actor behavior.
Consistent rules to define road-based coordinate systems within the abstract road network also enable the following tasks:

* Locating actors in the scenario
* Triggering the behavior of actors according to their location
* Constraining the behavior of actors according to their location

Furthermore, an abstract road network can be used to:

* Search for an existing road network that matches the abstract road network’s constraints.  
  This can be done, for example, within a specific map file, or in a map database.
* Create a synthetic map that satisfies the abstract road network constraints.  
  In this sense, users can think of this abstract road network as a "search space", rather than a geographic map or fixed geometry for the scenario.

This part of the domain model enables ASAM OpenSCENARIO users to describe *routes* within a *map*.
Such a map abstractly represents a desired environment to enable a behavior of a scenario.

The abstract road network was designed with the expressed intent to enable paths of behavior and routes that can be used to express both legal paths of behavior and illegal paths of behavior.

The main purposes of an abstract road network as part of the domain model are:

* Specifying constraints with respect to map, road, junction, and lane elements.
* Creating a map search space to either find a matching road network in a map or generate a synthetic one.
* Matching mapped entities for actor behavior.
* Creating paths of behavior called *routes*, so they can be used within behavior descriptions.
* Using s-t-coordinate systems when moving along a route.
* Enabling extension of the road’s domain model, either by users or by future releases of the standard.

## 8.5.2 Purposes of constraints

The main purposes of constraints of an abstract road network are:

* Limit the map search space.
* Describe a minimum environment that is necessary to allow paths of behavior through routes.
* Use modifiers to create routes or establish relationships between entities.
* Use the created routes to define *where* to `drive along()` within an action description.
  Here, [`along()`](movement-modifiers.html#sec-dm-actions-drive-modifiers-along) specifies the route that is traveled.

## 8.5.3 Key points

Key points when creating an abstract road network are:

* Describe only a minimum abstract road network that is necessary to support behavior.
  Do not re-create a map file.
* Let modifiers do the hard work.
* An abstract road network does not replace ASAM OpenDRIVE® or any other map supply.
* The goal of the abstract road network is to allow a user to outline just the details required for their use case so that suitable maps meeting these requirements can be selected.
* An abstract road network acts as a set of constraints needed to find and resolve options for behavior and the driving domain.
  In the driving domain, this is narrowed down to a specific set of maps, route points, or routes and sometimes even further using route anchors.

## 8.5.4 Maps

For the purposes of ASAM OpenSCENARIO, the `map` actor is a domain model representation of an abstract road network.
The `map` actor inherits from the `osc_actor` parent class, as is common for all actors in the standard library.
The `map` holds entities that are necessary for either the creation of maps, the restriction of a map search space, or both.

A `map_file` is a parameter representing a map file or concrete road network representation of road entities and road geometry.
In ASAM OpenSCENARIO, this is represented as a string, which can include both the file path and the file name of the map file.
A `map_file` is included in the `map` class so that the search space defined in an instance of `map` can be limited to one specific map file.
The map file for a scenario can be set using the `map.set_map_file()` modifier.

|  |  |
| --- | --- |
|  | In future versions of ASAM OpenSCENARIO the `map_file` parameter may be deprecated in favor of a more complete mechanism to bind external maps to the abstract road network description. |

The `map` is composed of instances of `route` and `junction`, which allow an abstract description of the road network to be matched to specific entities in a map file.

Constraints are the primary way that a map’s entities are used to restrict the map search space.
For the construction of routes constraints are used to both create and restrict the map search space.
Map methods such as `map.create_route()` gives users the flexibility to create routes either from a single `map_file` or from an external implementation.

|  |  |
| --- | --- |
|  | This also applies for the creation of compound routes, see [Section 8.5.7, “Creating compound routes”](#sec-dm-roads-creating-routes). |

Every scenario, no matter if abstract, logical, or concrete, must have a set of constraints that relate to the *map*.
Otherwise, actions cannot be rational to space and time.

An ASAM OpenSCENARIO map is composed of:

* Instances of `route`  
  A map can have zero routes, one route, or many routes.
  `route` is the parent class of map elements like `road` and `lane`, among others.
* Instances of `junction`  
  A map may have zero junctions, one, or many junctions.
  Junctions connect roads in the abstract road network.
* A setting for the `driving_rule`  
  A map may be for left-handed traffic or right-handed traffic.
* A `map_file` parameter  
  This allows users to bind the abstract road network to an external map file.
  This parameter can remain unspecified.

In the ASAM OpenSCENARIO domain model, the elements allowing users to describe an abstract road network for the scenario are under the parent-class `map`.

![Entity overview](_images/diag-7bbfe76ebb5c3467c2bc45e354a307f92e314446.png)

Figure 14. Entity overview

### 8.5.4.1 Map as an actor

For a *map* to act in a creation space, the map must be an actor that acts or has actions and modifiers like a typical actor does, meaning vehicle, person, animal, and so on.

A *map* represents the abstract road network and contains definitions of road abstraction related methods and modifiers.
A *map* is a subclass of an *actor* as only actors can contain modifiers.

|  |  |
| --- | --- |
|  | * A map has to be an actor because only actors contain modifiers. * A map replaces the `abstract_road_network` name because it is shorter: `map.routes_overlap()` rather than `road_network.routes_overlap()` |

### 8.5.4.2 Binding the map search space

|  |  |
| --- | --- |
|  | In future versions of ASAM OpenSCENARIO the `map_file` parameter may be deprecated in favor of a more complete mechanism to bind external maps to the abstract road network description. |

A `map_file` can be used with a constraint to restrict the map search space to a single map or within a list of map files.

`map_file` entities are specific to map\_file implementation and specific implementors and are not specific to ASAM OpenSCENARIO.

The `map_file` constraints can optionally be used to bind the abstract road network search space (map) to a concrete `map_file` or a set of map files to support both concrete scenarios and abstract scenarios.

For example, the benefit of assigning or creating a constraint to one `map_file` is like constraining a parameter to one value.
Given this constraint, scenario developers can ensure that the behaviors of the scenario attempt to secure a location somewhere within *this* `map_file` geometry.

Code 61. Setting a single map\_file

```
map.set_map_file('my_map.xodr')
```

Alternatively, you can use a `keep` constraint.

Code 62. Constraining a single map\_file

```
my_map: map
keep(my_map.map_file == 'my_map.xodr')
```

For logical scenarios, the benefit of creating a constraint with more than one map ensures that behaviors of the scenario attempt to secure a location somewhere within this list of map files.

Code 63. Assigning multiple map files for a logical scenario

```
 my_map: map
 keep(my_map.map_file in ['my_map1.xodr', 'my_map2.xodr', 'my_map3.xodr'])
```

If a `map_file` is not defined or constrained and is instead left to abstraction, any ASAM OpenSCENARIO implementation could use the map constraints to define a `map_file` that satisfies the constraints for the given application.

## 8.5.5 Routes

The class `route` is the common parent class for all children of `route_element` and `compound_route`.
It lets the user specify locations on the abstract road network (single or composed elements) where traffic participants can move.

The `along()` modifier enables usage of those routes inside scenarios and actions.

### 8.5.5.1 Route data structure

As shown in the following part of the domain model diagram, the class `route` inherits to several children.

![Entity overview](_images/diag-1f7d39bc4d41fa0b54fa50ef31315cb66b9619f1.png)

Figure 15. Entity overview

This chapter contains a short description of each class that inherits from `route` (see [Struct route](road_abstractions.html#sec-roads-class-route)).

* `route`  
  The parent class of [`route_element`](road_abstractions.html#sec-roads-abstract-route_element) and `compound_route`.
  An instance of `route` can refer to a single [`route_element`](road_abstractions.html#sec-roads-abstract-route_element), like a road or a lane, or to a sequence of elements (in the case of a `compound_route`).
  Having a single parent for these classes facilitates the use of the [`along()`](movement-modifiers.html#sec-dm-actions-drive-modifiers-along) modifier, and simplifies multiple other route- and map-related functionalities.
* [`route_element`](road_abstractions.html#sec-roads-abstract-route_element)  
  A basic, individual element used to build a route.
  Compound routes are composed of a list of individual route elements.
* `lane`  
  A pathway limited by two boundaries.
  Other elements of the road network are built out of lanes.
* `lane_section`  
  A group of adjacent lanes arranged side-by-side.
  Within a `lane_section`, the number, type, use, and directionality of lanes remain constant.
* `road`  
  A sequence of adjacent lane sections arranged end-to-end.
  A road can only connect to another road at a junction.
* `crossing`  
  A pathway similar to a lane, but overlaid on top of other lanes.
  Typically used for crosswalks, railroad crossings, or other situations with overlaying uses and directionalities.
* `path`  
  An ordered list of points in global world coordinates.
* `route_point`  
  A waypoint for a route expressed in s-t-coordinates.
* `xyz_point`  
  A waypoint for a route expressed in Cartesian coordinates.
* `odr_point`  
  A waypoint for a route expressed in ASAM OpenDRIVE® coordinates.
* `compound_route`  
  An ordered list of adjacent [`route_element`](road_abstractions.html#sec-roads-abstract-route_element) instances which are used to describe a potential course of movement.
  The members of the `compound_route` must be traversed in sequential order.
* `compound_lane`  
  An ordered list of adjacent lanes arranged end-to-end.

ASAM OpenSCENARIO also includes:

* `relative_path`
* `trajectory`
* `relative_trajectory`

However, these classes are not children of `route`.
The *relative\_path* and all trajectories have dependencies on time and are therefore not routable types.
The *relative\_path*, *trajectory*, and *relative\_trajectory* types can be used with their corresponding actions.

![Entity overview](_images/diag-a1e7778270766041a99411e8ec17640207e53053.png)

Figure 16. Entity overview

![Entity overview](_images/diag-98adf35f9d6d70d3ea0010985c83464a30d45f6c.png)

Figure 17. Entity overview

### 8.5.5.2 Route anchors

Map file constraints narrow the map search space.
But it is also possible to narrow the search space of route locations to specific location entities within a map file.

*Route anchors* are used to narrow this search.
Route anchors are string identifiers that allow one or more route entities of a map search space to be tied or bound to any map file entity.

* A typical use case for implementors is using an application that creates unique identifiers within the map file to pair with route elements, like `road`, `lane_section`, `lane`, and so on.

ASAM OpenDRIVE® examples:

* `<userData code="roadAnchor" value="myRoad">`  
  Used as an attribute of road.
* `<userData code="laneSectionAnchor" value="11111111-1234-5678-1234-567812345678">`  
  Used as an attribute of a lane section.
* `<userData code="laneAnchor" value="-1">`  
  Used as an attribute of lane.
* `<userData code="roadAnchor" value="net.asam.opendrive: roadId:165, laneId:-1">`  
  Used as an attribute of road that provides an anchor to the lane level.

When used as a search space, each route can be restricted to a single location entity (or a set of location entities) within a map file.
These location entities, which are found in a map file, are representative of the type of route entity that is being anchored.

* Example 1: The route anchors of a lane are matched with a lane that has an anchor in the map file.
* Example 2: A lane section is matched with a lane section that has an anchor in the map file.
* Example 3: A road is matched with a road that has an anchor in the map file.
* Example 4: A route point is matched with a point in the map file.

A single anchor or a set of anchors can be found in the map file.
This is up to the implementor.

Example: `map.map_file` has a relationship with `map.routes[i].anchors`.

A map anchor of a route is an entity that provides a pointer to a map file entity.
This clarifies or restricts a map-route entity to a map file entity.
The types depend on the implementation.

Given an instance of route:

* Binding of `route.anchors`  
  Route anchors are of the route class and can be used optionally to bind or allow for a narrowed set of matched location entities within a map file with the potential to satisfy a route within the *map search space* of a map.

|  |  |
| --- | --- |
|  | The matched entities depend on the map file implementation and are up to the implementor. |

Each route contains an optional ability to bind a given route to a set of *anchors*.
These anchors could be used within a defined `map.map_file` to allow an implementation to determine the location of a given route.

For a map file or a set of map files, the route anchors are defined as a list of strings to enable multiple choices found within.

```
struct lane:
    lane_type: lane_type
    lane_subtype: lane_subtype
    anchors: list of string
```

#### 8.5.5.2.1 Creating routes using anchors

Example 1. Assign anchors for a single map

```
my_map: map.map_file = ['my_map1.xodr']

anchored_lane_section: lane_section with:
    keep('11111111-1234-5678-1234-567812345678' in it.anchors)
    # shows an example of a uuid used as an anchor

anchored_lane1: lane with:
    keep('-1' in it.anchors)
```

Example 2. Assign anchors for longer route

```
my_map: map.map_file = ['my_map1.xodr']

anchored_lane_section1: lane_section with:
    keep('first_anchor_uuid1' in it.anchors)

anchored_lane1: lane with:
    keep('-1' in it.anchors)

anchored_lane_section2: lane_section with:
    keep('second_anchor_uuid2' in it.anchors)
```

Example 3. Assign anchors for multiple maps

```
my_map: map.map_file = ['my_map1.xodr', 'my_map2.xodr']
# each entry in the list is used sequentially but has unique ids.

ego_lane: lane with:
    keep('net.asam.opendrive: roadId:165, laneId:-1' in it.anchors or
         'net.asam.opendrive: roadId:257, laneId:-3' in it.anchors)

# Allows For Logical Scenario where the egoVehicle can start in a different lane given each map.
```

|  |  |
| --- | --- |
|  | Specific implementation is up to the implementor. This is just an example. |

Example 4. Assign anchors to route\_point

```
my_map: map.map_file = ['my_map1.xodr']

my_route_point: route_point with:
    keep('net.asam.opendrive: roadId165, laneId:-2, s:121, t:2.3' in it.anchors)
```

|  |  |
| --- | --- |
|  | Specific implementation is up to the implementor. This is just an example. |

Example 5. Anchoring two locations for two vehicles starting from different places on the same map

```
my_map: map.map_file = ['my_map1.xodr']

anchored_starting_location1: lane_section with:
    keep('location1_uuid' in it.anchors)

anchored_location1_lane: lane with:
    keep('-1' in it.anchors)

anchored_starting_location2: lane_section with:
    keep('location2_uuid' in it.anchors)

anchored_location2_lane: lane with:
    keep('-3' in it.anchors)
```

## 8.5.6 Junctions

### 8.5.6.1 Junction definition

|  |  |
| --- | --- |
|  | This definition of a junction is valid for this version of ASAM OpenSCENARIO and in the context of an *abstract road network*. |

A `junction` is a *connected search space*.
That search space is represented by a list of one or more roads that connect up to an area of intersection.

A `junction` is also an *area* where junction routes bind incoming routes (like roads and lanes) to outgoing routes, like spokes on a wheel.
*Roads* that connect to a junction, can be used as *routes*.

|  |  |
| --- | --- |
|  | A junction is *not* a route, but rather a separate object corresponding to a place where multiple routes meet. These routes are bound with connections to allow the flow of behavior. |

Each junction has a list of roads that define possible options to create junction routes or pathways through the junction.

Roads are used in several relations, like `roads_follow_in_junction()`. See [Section 8.5.7.1, “`roads_follow_in_junction()` modifier”](#sec-dm-roads-follow-in-junction).

The referenced roads follow in and out of the junction.

Key point
:   * The `junction` class has a list of one or more instances of `road`.

![Basic junction](_images/dm_junction_basic2_20211026.png)

Figure 18. Basic junction

#### 8.5.6.1.1 Junction routes within a junction

A junction route is a route within a junction.
Junction routes are formed through modifiers, like `roads_follow_in_junction()`.
A junction route completes connections between incoming roads and outgoing roads or incoming lanes and outgoing lanes.

Note that *junction route* is not a class.
Junction route is a term used to refer to instances of `route` that are inside of junctions.
A junction route can be any type of `route`, like a single `route_element` or a `compound_route`.

Key points
:   * A junction is a hub for road connections.
    * Therefore, the `junction` class contains a list of `road` elements that connect through the junction.
    * A junction is neither a `route` nor a `route_element`, and cannot be included in a `compound_route`.
    * However, there can be routes inside of a junction.
    * Instances of `route` that are inside of a junction are called junction routes.
    * A junction route is used to complete connections between route elements, for example, `road`, `lane`, and so on.
    * To make pathways from an incoming road to an outgoing road, a junction uses junction routes to close or complete a connection.

      + An `in_road` to an `out_road` is typically passed to modifiers like `roads_follow_in_junction` to create junction routes.
    * These junction routes provide connection pathways that allow for route transitions.
      The transitions can be:

      + From one route to another route
      + Used in an all-encompassing route
    * These junction routes can also act as virtual lanes inside the junction.
    * Junction routes allow for both legal pathways and illegal pathways, whereas ASAM OpenDRIVE® or a real road network typically only specifies legal pathways.

      + `roads_follow_in_junction()` only creates legal junction routes.
      + However, users can use junction routes to create routes (or compound routes) where actors could move against the legal traffic flow.
    * One junction can connect to many routes with junction routes, like spokes on a wheel.
      Each one of the outer roads can be connected through junction routes to another road (meaning another spoke of the same wheel).  
      Combining the `in_road` and the `out_road` with junction routes enables behavioral pathways.

|  |  |
| --- | --- |
|  | A junction route is not always used as a virtual lane. Sometimes a junction route is used as a virtual road connecting all the lanes of one road or route with all lanes of another road or route. |

![dm junction routes3 20211026](_images/dm_junction_routes3_20211026.png)

Figure 19. Junction routes

The following examples show how to create junction routes inside of a junction.

Example 6. Four-way junction with road junction routes

```
my_junction: junction
road_1, road_2, road_3, road_4: road
jr_12, jr_34: road

r1: map.roads_follow_in_junction(junction: my_junction, in_road: road_1, out_road: road_2, junction_route: jr_12)
r3: map.roads_follow_in_junction(junction: my_junction, in_road: road_3, out_road: road_4, junction_route: jr_34)

# Note: my_junction.roads is the list [road_1, road_2, road_3, road_4]
# Note: r1.resulting_route is a compound route composed of [road_1, jr_12, road_2]
# Note: r3.resulting_route is a compound route composed of [road_3, jr_34, road_4]
```

Example 7. Junction with lane junction routes

```
my_lane_junction: junction
lane_1, lane_2, jr_lane: lane

j1: map.roads_follow_in_junction(junction: my_lane_junction, in_lane: lane_1, out_lane: lane_2, junction_route: jr_lane)

# Note: lane_1 belongs to the in_road, accessed by j1.in_road
# Note: lane_2 belongs to the out_road, accessed by j1.out_road
# Note: j1.resulting_route is a compound route composed of [lane_1, jr_lane, lane_2]
```

#### 8.5.6.1.2 Road within a junction

It is possible, geometrically speaking, to have a road and a junction occupy the same space.
When this occurs, the junction type is a `junction_road`.

#### 8.5.6.1.3 Crossings over the top of a junction

A crossing may be overlaid anywhere where a lane is present.
The placement of a crossing allows the placement over the top of a junction where lanes of a road meet up to the junction.

#### 8.5.6.1.4 Geometric constraints of a junction

The geometric constraints of a junction may be included in future versions of ASAM OpenSCENARIO.
Currently, this is not implemented.

|  |  |
| --- | --- |
|  | Junctions may have an impact on s- and t-coordinates. This is not included in this version of ASAM OpenSCENARIO. |

## 8.5.7 Creating compound routes

The class `compound_route` inherits from the class `route`.
It has a field [`route_elements`](road_abstractions.html#sec-roads-abstract-route_element) holding an ordered list of route elements.
This list represents a spatially connected route on the abstract road network.

Instances of the class `compound_route` can be created with the following method, which needs to be externally implemented:

Code 64. Method declaration for creating routes

```
def map.create_route(routes: list of route, connect_points_by: connect_route_points, legal_route: bool) -> compound_route
```

When called the external method is expected to return a `compound_route` object with a field [`route_elements`](road_abstractions.html#sec-roads-abstract-route_element) by resolving the ordered argument list in the following way:

* If compound routes are part of the argument list, the method first splits those into their constituting route elements while retaining the order.
  This results in a list that only contains route elements.
* If the resulting list from the last step describes map patterns that are not spatially connected on the abstract road network, the gap(s) of the under-defined route must be filled in an implementation-specific way with any route elements resulting in a spatially connected route.

|  |  |
| --- | --- |
|  | * If the list of route elements describes patterns that spatially overlap, implementations are free to define further properties as extensions of compound\_route. |

The field [`route_elements`](road_abstractions.html#sec-roads-abstract-route_element) of the returned `compound_route` object gets the value of the (final) list of connecting route elements.

The other two optional parameters describe how route elements must be connected and if illegal routes may be used (this is `false` by default).

The following code snippets create routes.

Code 65. A route with a single type of route element

```
my_road_1, my_road_2, my_road_3: road
# Modifiers are used to connect the roads into a road network...

my_route: route = map.create_route([my_road_1, my_road_2, my_road_3])
```

In this example, the roads may have some relations specified by constraints or modifiers.
They may also be anchored on a real map.
If the route elements listed in the argument are not directly connected, the method implementation is expected to fill the gaps and return a continuous compound route.

Code 66. A route with different types of route elements

```
my_road_1, my_road_2: road
my_path: path
my_point: xyz_point
# Modifiers or methods are used to connect the roads and specify the path and point...

my_route : map.create_route([my_point, my_road_1, my_path, my_road_2], connect_points_by: lane)
```

In this example, the route elements are of different types, but they all are children of the [`route_element`](road_abstractions.html#sec-roads-abstract-route_element) class.
The `connect_points_by` argument specifies how to connect the routable point types to the rest of the route.
In this case, the second element of the route must be interpreted as the `lane` that contains `my_point`.
If the user does not specify this argument, the method uses the default value.

For the instantiation of routable points and paths there are dedicated method signatures:

* `create_route_point()`
* `create_xyz_point()`
* `create_odr_point()`
* `create_path()`
* `create_path_odr_points()`
* `create_path_route_points()`

For coordinate conversion between different routable point types there are also dedicated method signatures:

* `route_point_to_xyz()`
* `xyz_to_route_point()`
* `odr_to_route_point()`

### 8.5.7.1. `roads_follow_in_junction()` modifier

The modifier `map.roads_follow_in_junction()` is a modifier that specifies or constrains the connection between [`route_elements`](road_abstractions.html#sec-roads-abstract-route_element) into and out of a junction and optionally some further properties of the corresponding junction.

Code 67. Declaration of the `roads_follow_in_junction()` modifier

```
map.roads_follow_in_junction(junction: junction, in_road: road, out_road: road,
direction: junction_direction, clockwise_count: uint, number_of_roads: uint,
in_lane: lane, out_lane: lane,
junction_route: route, resulting_route: route)
```

The following code creates a four-way junction with a right-turn route through it.

Code 68. A four-way junction with a right-turn route

```
map: map
r1, r2: road
my_mod: map.roads_follow_in_junction(in_road: r1, out_road: r2, direction: right, number_of_roads: 4)
```

The resulting route of type `compound_route` can be accessed with `my_mod.resulting_route`, which has a list of the following [`route_elements`](road_abstractions.html#sec-roads-abstract-route_element) as a property: `[in_road, junction_route, out_road]`.

The `junction_route` (instantiated by the modifier) represents the spatial connection inside the junction between the inbound and outbound [`route_element`](road_abstractions.html#sec-roads-abstract-route_element).
It is accessible via `my_mod.junction_route`.

Note that the modifier can automatically instantiate road objects that connect to the junction.
Those objects are accessible by their symbolic names, using `my_mod.in_road` and `my_mod.out_road`.
The example illustrated this automatic instantiation.

It is also possible to have roads or lanes as parameters of the modifier, which may be constrained:

The following code creates a four-way junction with two-lane roads and a right-turn route through it.

Code 69. A four-way junction with two-lane roads and a right-turn route

```
map: map
r3, r4: road with:
    keep(number_of_lanes == 2)
my_mod2: map.roads_follow_in_junction(in_road: r3, out_road: r4, clockwise_count: 3, number_of_roads: 4)
```

This example specifies the same thing and additionally constrains the inbound and outbound roads to two lanes.

|  |  |
| --- | --- |
|  | By default the resulting route must be legal. If the inbound or the outbound [`route_element`](road_abstractions.html#sec-roads-abstract-route_element) binds to a [`route_element`](road_abstractions.html#sec-roads-abstract-route_element) where the respective movement is illegal, an error message must be raised. |

#### 8.5.7.1.1. Using the modifier `roads_follow_in_junction()`

The `resulting_route` parameter can be used as an input to the `create_route()` method or directly inside the `along()` modifier for movable objects to move along.

Code 70. Using resulting route with the modifier `along()`

```
scenario my_junction_scenario:
    map: map
    r1, r2: road
    my_mod: map.roads_follow_in_junction(in_road: r1, out_road: r2, direction: right, number_of_roads: 4)
    car_a: vehicle

    do parallel:
        car_a.drive() with:
            along(my_mod.resulting_route)
```

### 8.5.7.2 Customized abstract road networks

More complex custom modifiers defining compound topologies and potentially usable [`route_elements`](road_abstractions.html#sec-roads-abstract-route_element) inside of it can be built out of smaller modifiers to encapsulate a broader constraint set of the abstract road network.

An example follows, which is verbally described first:

* A vehicle `v1` moves on roads with at least two lanes each.
* Take the first exit to the right of the first junction, which is a four-way-junction.
* Cross an adjacent arbitrary second junction in an arbitrary way.
* A second vehicle `v2` initially moves along a second route that is included in the route of `v1`.

Code 71. Code for a customized abstract road network and its usage inside a scenario

```
# Define that abstract road network:
# Roads, junctions, routes covering several roads
modifier map.two_junction_network:
    r1, r2, r3: road with:
        keep(min_lanes >= 2)
    j1, j2: junction
    f1: roads_follow_in_junction(junction: j1, number_of_in_roads: 4,
        in_road: r1, out_road: r2, direction: right)
    f2: roads_follow_in_junction(junction: j2, in_road: r2,
        out_road: r3)

    route_a: route = create_route([r1, f1.junction_route, r2, f2.junction_road, r3])
    route_b: route = create_route([r1, f2.junction_route, r2])

# Use that modifier
scenario traffic.drive_along_two_junctions:
    map: map
    net: map.two_junction_network()
    v1, v2: vehicle
    do parallel:
        v1.drive() with:
            along(net.route_a)
        serial:
            v2.drive() with:  # Initially drive behind v1
                along(net.route_b)
                position([10m..50m], behind: v1, at: start)
        ...  # Then do something else
```

Encapsulating the routing constraints into the map actor via the method application is recommended to enable reusability (see [Method application](../language-reference/expressions_main.html#sec-lc-expressions-method-application)).
Note that other instances of modifiers like `road_follows_in_junction()` are nested inside.

### 8.5.7.3. `routes_overlap()` modifier

The modifier `map.routes_overlap()` makes it possible to specify two overlapping routes.
Where the route patterns must overlap, can be specified with the specific parameter `overlap_kind`.
This parameter can have one of the following values:

* `equal`
* `start`
* `end`
* `inside`

Code 72. Declaration of the `routes_overlap()` modifier

```
map.routes_overlap(route1: route, route2: route, overlap_kind: route_overlap_kind)
```

The following code creates a route that is longer than 1000 m, and has a tunnel inside of it.

Code 73. A road with a tunnel

```
r1: route with:
    keep(length > 1000m)
t: route_in_tunnel     # assuming a user-defined type route_in_tunnel exists.
map.routes_overlap(route1: r1, route2: t, overlap_kind: inside)
```

Note that the second route is in the first route.

A tunnel at the start of the (resulting) route can be specified by changing the *overlap\_kind* from `inside` to `start`.

### 8.5.7.4. `routes_are_opposite()` modifier

The modifier `map.routes_are_opposite()` makes it possible to specify two routes that are opposite to each other.

Code 74. Declaration of the `routes_are_opposite()` modifier

```
map.routes_are_opposite(route1: route, route2: route,
containing_road: road, lateral_overlap: lateral_overlap_kind)
```

The following code creates a two-way road r1 with opposing lanes that are located adjacent to each other, for example, a typical rural road.

Code 75. A two-way road with opposing lanes

```
map: map
r1: road
ls1: lane_section with:
    keep(it.max_lanes == 1)
ls2: lane_section with:
    keep(it.max_lanes == 1)
map.routes_are_opposite(route1: ls1, route2: ls2, containing_road: r1, lateral_overlap: never)
```

Only the following [`route_elements`](road_abstractions.html#sec-roads-abstract-route_element) can be arguments to the modifier:

* `lane_section`
* `lane`
* `compound_lane`

If a *road* is input to the modifier, an error must be raised.

For a bi-directional one-lane road use `lateral_overlap: always`.

## 8.5.8 Crossings

A crossing is an overlay or virtual path that acts as a route and has a direct relationship to lanes.

![A typical crossing](_images/dm_typical_crossing.png)

Figure 20. A typical crossing

A crossing can be used to represent:

1. A crosswalk within junctions crossing from one sidewalk to another sidewalk.
2. An independent crossing in the middle of the road.
3. A parking lot, overlaid on top of free space to give a directed path.
4. A railroad crossing.

A crossing has nearly the same characteristics as a lane but is not part of a `lane_section` or a road.
A crossing is simply layered on top of route entities if it is *"anchored to"* a crossing.

* A crossing is very similar to a lane, but is independent of road entities and relies on lane geometry.
* A crossing has a `start_lane` and `end_lane`.  
  The `start_lane` anchors the crossing at the centerline of the `start_lane`.
  The `start_lane` completes the crossing at the centerline of the `end_lane` where it completes the connection.
* The origin of a crossing for s-coordinates is determined from a lane centerline and s-position along that line.
* The `start_lane` assigns the lane that starts the crossing.
* The `end_lane` assigns the lane that completes the crossing.
* A crossing has a start angle of 90 degrees unless otherwise specified.
* A crossing is always a straight line.
* In the case of straight-line geometry, the crossing ends at the natural connection with `end_lane` centerline.
* A crossing does not need an angle for where it connects to the `end_lane`.
  If a single angle and one starting s-dimension are known, then the angle can be calculated, because of the rule of two relative points.
* A crossing does not need an s-dimension for where it connects at the `end_lane`.
  With the straight-line geometric requirements, the s-dimension can be calculated.

![dm crossing 20210926](_images/dm_crossing_20210926.png)

Figure 21. A crossing

When a crossing is a route, it can be used in the following way with other lanes or routes:

```
map: map
sidewalk1: lane
sidewalk2: lane
crossing1: crossing with:
    keep(it.width == 3.5m)

map.crossing_connects(crossing1,
                    start_lane: sidewalk1,
                    end_lane: sidewalk2,
                    start_s_coord: 5m,
                    start_angle: 90deg)

# may be used without 'start_angle' parameter
```

The origin of a crossing completely overlaps up to the centerline of the s-point of `start_lane` and is connected or anchored to this lane.

The centerline of a crossing is always perpendicular to the centerline of the start lane unless an angle is otherwise specified.

The end point of the crossing centerline must intersect at an s-point found on the centerline of the end lane.
This is satisfied, no matter what connected angle is possible.
This connection must ensure that the crossing is created using a straight line.

A crossing also has a width, which can be used with constraints to specify how big the crossing is.
The width allows for larger groups of pedestrians or animals to move in either direction.

## 8.5.9 s-t-coordinate system for routes

In the ASAM OpenSCENARIO abstract road network, lanes constitute the fundamental building block for other map elements.
The composition diagram below shows how lanes are central to the composition of routes.
Therefore, the lane is used to define a consistent set of rules to create s-t-coordinates on all the children of `route`.

Other details of s-t coordinate systems are found in the [coordinate systems](dm_coordinate_systems.html) section.

![Entity overview](_images/diag-d55968d7a30d44919ce08de28c927cd4e263ef23.png)

Figure 22. Entity overview

* Each `lane` has an s-t-coordinate system.

  + The s-axis runs along the centerline of the lane.
  + The t-axis runs perpendicular to the s-axis.
  + The s-t-coordinate system follows the right-hand rule.
  + By default, uni-directional lanes shall have legal traffic moving in the positive s-direction.
* Lanes are arranged side-by-side to make a `lane_section`.

  + The lane section also has an s-t-coordinate system.
  + The s-t-axes for the lane section coincide with s-t-axes of the lane chosen in the `lane_section.s_axis` field.
* Lane sections are arranged end-to-end to make a `road`.

  + The road also has an s-t-coordinate system.
  + The s-axis of the road is formed by the succession of the s-axes of the lane sections that compose the road.
  + The t-axis for the road runs perpendicular to the s-axis, following the right-hand rule.
* A `crossing` has an s-t-coordinate system, defined similarly to the s-t-coordinate system for the lane.
* Each `compound_route` has an s-t-coordinate system.
  This coordinate system is built following the same rules as for a `lane`.
* Routes that are inside of junctions (like the `junction_route` parameter in the `roads_follow_in_junction()` modifier) are instances of the route types mentioned above, and therefore follow the corresponding rules to establish their s-t coordinate system.