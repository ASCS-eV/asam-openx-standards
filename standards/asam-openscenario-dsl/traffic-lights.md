# ASAM Openscenario Dsl v2.2.0 — 8.15 Traffic lights

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/traffic_lights.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.15 Traffic lights

## 8.15.1 Overview

This chapter explains the implementation of traffic lights and how it enables the manipulation of traffic signals in ASAM OpenSCENARIO.
The concept allows for the management of traffic lights within the map file, using semantic states and or bulb states.

## 8.15.2 Traffic light bulbs

ASAM OpenSCENARIO provides enumeration types for icon shape, color, and state to manage and define traffic light bulbs.
The structure `traffic_light_bulb` encapsulates the properties of an individual traffic light bulb.

### 8.15.2.1 Enum bulb\_icon

Available icons for traffic lights. Note that this enum only describes the icons, with the actual colors being irrelevant. For visual representations of the icons, refer to the OpenDRIVE traffic signal code number and table found in OpenDRIVE traffic signal files. Images of the icons can be found at [usepastel.com/link/omxxxgy3/#/opendrive-group/opendrive-antora-gen/ASAM\_OpenDRIVE\_Signal\_reference/latest/signal-catalog/01\_road\_signals/road\_signals.html](https://usepastel.com/link/omxxxgy3/#/opendrive-group/opendrive-antora-gen/ASAM_OpenDRIVE_Signal_reference/latest/signal-catalog/01_road_signals/road_signals.html).

Basic information
:   Table 301. Basic information of enum bulb\_icon


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Values
:   Table 302. Enum bulb\_icon


    | Value | Comment |
    | --- | --- |
    | unknown | Unknown icon |
    | circle | OpenDRIVE Type 1000020, 1000001, 1000008, 1000012 |
    | pedestrian\_walking | OpenDRIVE Type 1000002-20 (a walking pedestrian) |
    | pedestrian\_standing | OpenDRIVE Type 1000002-10 (a pedestrian in standing position) |
    | tram | OpenDRIVE Type 1000014 (tram) |
    | bus | OpenDRIVE Type 1000015 (bus) |
    | bicycle | OpenDRIVE Type 1000013-20 (bicycle) |
    | horse\_rider | OpenDRIVE Type 1000015 (a [person](entity.html#sec-trafficparticipant-entity-person) riding a horse) |
    | person\_bicycle | OpenDRIVE Type 1000015 (a [person](entity.html#sec-trafficparticipant-entity-person) riding a bicylce) |
    | bicycle\_left | OpenDRIVE Type 1000013-50 (a bicycle as seen driving to the left) |
    | bicycle\_right | OpenDRIVE Type 1000013-80 (a bicycle as seen driving to the right) |
    | arrow\_left | OpenDRIVE Type 1000020-10 (an arrow pointing left) |
    | arrow\_right | OpenDRIVE Type 1000020-20 (an arrow pointing right) |
    | arrow\_straight | OpenDRIVE Type 1000020-30 (an arrow pointing straight ahead) |
    | arrow\_left\_straight | OpenDRIVE Type 1000020-40 |
    | arrow\_right\_straight | OpenDRIVE Type 1000020-50 |
    | arrow\_diagonal\_left | OpenDRIVE Type 1000020-60 |
    | arrow\_diagonal\_right | OpenDRIVE Type 1000020-70 |
    | arrow\_u\_turn\_left | OpenDRIVE Type 1000008-80 (an arrow indicating a u-turn to the left) |
    | arrow\_u\_turn\_right | OpenDRIVE Type 1000008-90 (an arrow indicating a u-turn to the left) |
    | arrow\_left\_right | OpenDRIVE Type 1000012-100 |
    | lane\_arrow\_down | OpenDRIVE Type 1000021 |
    | lane\_arrow\_down\_right | OpenDRIVE Type 1000022-10 |
    | lane\_arrow\_down\_left | OpenDRIVE Type 1000022-20 |
    | lane\_cross | OpenDRIVE Type 1000022-23 |
    | txt\_walk | A textual description meaning "walk" |
    | txt\_dont\_walk | A textual description meaning "do not walk" |
    | countdown | Numbers for counting down |
    | pt\_horizontal\_bar | Public transportation OpenDRIVE Type F-0 |
    | pt\_vertical\_bar | Public transportation OpenDRIVE Type F-1 |
    | pt\_slash\_bar | Public transportation OpenDRIVE Type F-2 |
    | pt\_backslash\_bar | Public transportation OpenDRIVE Type F-3 |
    | pt\_small\_circle | Public transportation OpenDRIVE Type F-4 |
    | pt\_triangle | Public transportation OpenDRIVE Type F-5 |
    | switch\_x | Public transportation OpenDRIVE Type W-0 |
    | switch\_v\_flipped | Public transportation OpenDRIVE Type W-1 |
    | switch\_v\_left | Public transportation OpenDRIVE Type W-2 |
    | switch\_v\_right | Public transportation OpenDRIVE Type W-3 |
    | switch\_t | Public transportation OpenDRIVE Type A-1 |
    | switch\_a | Public transportation OpenDRIVE Type A-X |
    | switch\_bar\_v | Public transportation OpenDRIVE Type W-14 |
    | switch\_bar\_v\_flipped | Public transportation OpenDRIVE Type W-11 |
    | switch\_bar\_v\_right | Public transportation OpenDRIVE Type W-12 |
    | switch\_bar\_v\_left | Public transportation OpenDRIVE Type W-13 |
    | switch\_dotted\_circle | Public transportation OpenDRIVE Type A-2B |

### 8.15.2.2 Enum bulb\_color

The color of a traffic light bulb.

Basic information
:   Table 303. Basic information of enum bulb\_color


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Values
:   Table 304. Enum bulb\_color


    | Value | Comment |
    | --- | --- |
    | unknown | Unknown [color](entity.html#sec-trafficparticipant-enum-color) |
    | red | Red [color](entity.html#sec-trafficparticipant-enum-color) |
    | yellow | Yellow [color](entity.html#sec-trafficparticipant-enum-color) |
    | green | Green [color](entity.html#sec-trafficparticipant-enum-color) |
    | blue | Blue [color](entity.html#sec-trafficparticipant-enum-color) |
    | white | White [color](entity.html#sec-trafficparticipant-enum-color) |

### 8.15.2.3 Enum bulb\_state

The state of a traffic light bulb.

Basic information
:   Table 305. Basic information of enum bulb\_state


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Values
:   Table 306. Enum bulb\_state


    | Value | Comment |
    | --- | --- |
    | unknown | Unknown state |
    | is\_off | Bulb is off |
    | is\_on | Bulb is on |
    | is\_flashing | Bulb is flashing |

### 8.15.2.4 Struct traffic\_light\_bulb

A traffic light bulb.

Basic information
:   Table 307. Basic information of struct traffic\_light\_bulb


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 308. Struct traffic\_light\_bulb


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | map\_id | string | no | Unique identifier of the traffic light bulb in the context of the [map](road_abstractions.html#sec-roads-class-map) actor |
    | icon | [bulb\_icon](#sec-traffic_lights-enum-bulb_icon) | yes | The type of traffic light bulb icon |
    | [color](entity.html#sec-trafficparticipant-enum-color) | [bulb\_color](#sec-traffic_lights-enum-bulb_color) | yes | The [color](entity.html#sec-trafficparticipant-enum-color) of the traffic light bulb |
    | icon\_positive | bool | yes | True if icon is illuminated (and background is dark), false if icon is dark (and background is illuminated). |

State variables
:   Table 309. State variables of struct traffic\_light\_bulb


    | Variable | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | state | [bulb\_state](#sec-traffic_lights-enum-bulb_state) | yes | State of the traffic light bulb |

![Example of icon_positive==false (left) and icon_positive==true (right)](_images/positive_negative_traffic_lights_example.png)

Figure 26. Example of icon\_positive==false (left) and icon\_positive==true (right)

## 8.15.3 Semantic states

The semantic state of a signal belongs to the rules governing traffic behavior in relation to the signal at a specific point in time.
For instance, a signal might be in a semantic stop state, indicating that compliant traffic must not cross a designated stop line associated with the signal.
Alternatively, it could be in a semantic caution state, allowing compliant traffic to proceed past the signal but requiring it to yield to other traffic and pedestrians.

### 8.15.3.1 Enum semantic\_traffic\_light\_state

Rules imposed on traffic obeying the signal at a given point in time.

Basic information
:   Table 310. Basic information of enum semantic\_traffic\_light\_state


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Values
:   Table 311. Enum semantic\_traffic\_light\_state


    | Value | Comment |
    | --- | --- |
    | off | Traffic light is turned off |
    | stop | Stop motion |
    | attention | Traffic signal is going to change to go |
    | caution | Obeying traffic may pass the signal but must yield to other traffic |
    | stop\_attention | Traffic signal is going to switch to stop |
    | go | Obeying traffic is allowed to [drive](actions.html#sec-actions_vehicles-class-drive) |
    | go\_exclusive | Obeying traffic has exclusive rights to pass. Other [crossing](road_abstractions.html#sec-roads-class-crossing) traffic members have semantic state stop. |
    | non\_functional | Non-functional traffic light. Can be used when a traffic light is in an unrecognizable state (for example, when red and green lights are on together). |

The mapping between semantic and physical (bulb) states can vary, especially across regional standards.
The `traffic_light` struct uses the `semantic_state_to_state` and `state_to_semantic_state` methods to enable conversion between these representations.
The specific conversion mapping can be defined in a separate file, such as 'xxx\_regional\_settings.osc'.

## 8.15.4 Traffic light

The `traffic_light` struct represents a singular traffic light box, such as one with red, yellow, and green bulbs.
The order of the bulbs reflects the arrangement of the traffic light.
For vertically oriented traffic light boxes the order is from top to bottom.
For horizontally oriented traffic light boxes the order is from left to right.

### 8.15.4.1 Struct traffic\_light

A single traffic light box.

Basic information
:   Table 312. Basic information of struct traffic\_light


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 313. Struct traffic\_light


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | map\_id | string | no | Unique identifier of the traffic light box in the context of the [map](road_abstractions.html#sec-roads-class-map) actor |
    | bulbs | list of traffic\_light\_bulb | yes | List of traffic light bulbs that are contained in the traffic light box |
    | pose | pose\_3d | yes | The physical position and orientation of the traffic light box |
    | height | length | yes | Height of the traffic light box |
    | width | length | yes | Width of the traffic light box |
    | group | [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) | yes | The traffic light group the traffic light box belongs to |

#### 8.15.4.1.1 Methods

##### Method state\_equal()

Checks whether the current bulb states of the traffic light bulbs of this traffic light are equal to the bulb states of the traffic light bulbs in `bulbs`.

Prototype
:   ```
    extend traffic_light:
        def state_equal(bulbs: list of traffic_light_bulb)-> bool
    ```

Return value
:   True if the current traffic light bulb states of the traffic light are equal to the bulb states of the bulbs in `bulbs`, otherwise false.

Parameters
:   Table 314. Parameter for method state\_equal()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | bulbs | list of traffic\_light\_bulb | List of traffic light bulbs to be compared to the bulbs of the current traffic light in regard to their state. |

##### Method semantic\_state\_to\_state()

Converts the semantic state to a list of traffic light bulbs with the correct bulb icons, colors and states.

Prototype
:   ```
    extend traffic_light:
        def semantic_state_to_state(state: semantic_traffic_light_state)-> list of traffic_light_bulb
    ```

Return value
:   A list of elements of type `traffic_light_bulb`, ordered according to the position of the bulbs in the traffic light.

Parameters
:   Table 315. Parameter for method semantic\_state\_to\_state()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | state | semantic\_traffic\_light\_state | state of the traffic light in semantic representation |

##### Method state\_to\_semantic\_state()

Converts a list of traffic light bulbs to a semantic state of a traffic light by evaluating their icons, colors, and states.

Prototype
:   ```
    extend traffic_light:
        def state_to_semantic_state(bulbs: list of traffic_light_bulb)-> semantic_traffic_light_state
    ```

Return value
:   The semantic state of the traffic light.

Parameters
:   Table 316. Parameter for method state\_state\_to\_semantic\_stateequal()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | bulbs | list of traffic\_light\_bulb | A list of traffic light bulbs, ordered according to the position of the bulbs in the traffic light. |

The struct `traffic_light_group` describes a set of traffic light boxes that control the same element of the road.
This can either be a single traffic light, or multiple traffic lights that duplicate each other.
An example are multiple traffic light boxes facing the same segment of the road, but hanging at different positions.
All traffic lights in the traffic light group must have exactly the same state at any given moment of time, unless there is a malfunction or one of the bulbs is burned.

### 8.15.4.2 Struct traffic\_light\_group

A set of traffic light boxes that control the same incoming lanes.

Basic information
:   Table 317. Basic information of struct traffic\_light\_group


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 318. Struct traffic\_light\_group


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | map\_id | string | no | Unique identifier of the traffic light group in the context of the [map](road_abstractions.html#sec-roads-class-map) actor |
    | bulbs | list of traffic\_light\_bulb | yes | Union of all traffic light bulbs that are contained in all traffic light boxes of the group |
    | traffic\_lights | list of traffic\_light | yes | List of traffic lights in the traffic light group |
    | cycle | [traffic\_light\_cycle](#sec-traffic_lights-class-traffic_light_cycle) | yes | Activation\_cycle may be null if not specified by the provided control plan (see map.set\_traffic\_lights\_control\_file) |

#### 8.15.4.2.1 Methods

##### Method state\_equal()

Checks whether the current bulb states of the traffic light bulbs of this traffic light group are equal to the bulb states of the traffic light bulbs in `bulbs`.

Prototype
:   ```
    extend traffic_light:
        def state_equal(bulbs: list of traffic_light_bulb)-> bool
    ```

Return value
:   True if the current traffic light bulb states of the traffic light group are equal to the bulb states of the bulbs in `bulbs`, otherwise false.

Parameters
:   Table 319. Parameter for method state\_equal()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | bulbs | list of traffic\_light\_bulb | List of traffic light bulbs to be compared to the bulbs of the current traffic light group in regard to their state. |

## 8.15.5 Stop-line

A stop line, whether imaginary or real, indicates the position at which traffic is required to halt when the traffic light is in the semantic stop state.
The marking of the stop line is defined by the following enumeration type.

### 8.15.5.1 Enum stop\_line\_marking

Type of imaginary or real line that describes the position where the traffic shall stop if the traffic light is in the semantic state `stop`.

Basic information
:   Table 320. Basic information of enum stop\_line\_marking


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Values
:   Table 321. Enum stop\_line\_marking


    | Value | Comment |
    | --- | --- |
    | none | No line drawn on the ground. |
    | solid | Stop line is a solid line. |
    | broken | Stop line is a broken (dashed) line. |

The following structure represents the `stop_line` of a `traffic_light_group`.

### 8.15.5.2 Struct traffic\_light\_stop\_line

The `stop_line` of a `traffic_light_group`.

Basic information
:   Table 322. Basic information of struct traffic\_light\_stop\_line


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [route\_element](road_abstractions.html#sec-roads-abstract-route_element) |

Parameters
:   Table 323. Struct traffic\_light\_stop\_line


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) | [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) | yes | Group of traffic lights that is related to the stop line |
    | [route](road_abstractions.html#sec-roads-class-route) | [route](road_abstractions.html#sec-roads-class-route) | yes | Route on which the stop line is located |
    | rightmost\_lane | uint | yes | The [lane](road_abstractions.html#sec-roads-class-lane) index for the rightmost relevant [lane](road_abstractions.html#sec-roads-class-lane) controlled by `traffic_light_group` |
    | leftmost\_lane | uint | yes | The [lane](road_abstractions.html#sec-roads-class-lane) index for the leftmost relevant [lane](road_abstractions.html#sec-roads-class-lane) controlled by the `traffic_light_group` |
    | offset | length | yes | The position of the stop line in s-coordinates along the [route](road_abstractions.html#sec-roads-class-route) |
    | secondary\_stop\_offset | length | yes | The position of the secondary stop line in s-coordinates along the route. By default, only one stop line per [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) exists, and `secondary_stop_offset` == `offset` |
    | primary\_stop\_line\_marking | [stop\_line\_marking](#sec-traffic_lights-enum-stop_line_marking) | yes | Type of stop line marking |
    | secondary\_stop\_line\_marking | [stop\_line\_marking](#sec-traffic_lights-enum-stop_line_marking) | yes | Type of stop line marking for secondary stop line. By default, only one stop line per [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) exists, and `secondary_stop_line_marking` == `primary_stop_line_marking` |

Inherited parameters and variables
:   Table 324. Inherited parameters and variables of struct traffic\_light\_stop\_line


    | Parent | Inherited parameters and variables |
    | --- | --- |
    | [route](road_abstractions.html#sec-roads-class-route) | [length](road_abstractions.html#tab-roads-class-route-info), [directionality](road_abstractions.html#tab-roads-class-route-info), [min\_lanes](road_abstractions.html#tab-roads-class-route-info), [max\_lanes](road_abstractions.html#tab-roads-class-route-info), [anchors](road_abstractions.html#tab-roads-class-route-info) |

## 8.15.6 Traffic light phase

A phase of a traffic light is its state for a certain duration.

### 8.15.6.1 Struct traffic\_light\_phase

Definition of the states of a list of traffic light bulbs of a specific traffic light group for a defined time span.

Basic information
:   Table 325. Basic information of struct traffic\_light\_phase


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 326. Struct traffic\_light\_phase


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | group | [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) | yes | Traffic light group that is addressed by the phase |
    | bulbs\_state | list of traffic\_light\_bulb | yes | List of traffic light bulbs that should be set for the specific group |
    | duration | time | yes | Duration of the phase in seconds |

A list of `traffic_light_phase` elements arranged in chronological order form the struct `traffic_light_cycle`.

### 8.15.6.2 Struct traffic\_light\_cycle

Different possible phases of type `traffic_light_phase` arranged in chronological order.

Basic information
:   Table 327. Basic information of struct traffic\_light\_cycle


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

Parameters
:   Table 328. Struct traffic\_light\_cycle


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | phases | list of traffic\_light\_phase | yes | The different phases of the cycle in chronological order |
    | synchronization\_group\_id | uint | yes | Identifier used to synchronize different traffic light groups. All traffic light groups with the same `synchronization_group_id` shall be synchronized, for example in a crossing: If traffic in one direction has a green light, the traffic in the perpendicular direction must have a red light |
    | start\_offset | time | yes | Temporal offset of the start of the cycle |

## 8.15.7 Interaction with the map

The traffic lights are located in the map.
The map itself is described by the map file.

```
extend map:
    traffic_light_groups: list of traffic_light_group
    traffic_light_control: list of traffic_light_cycle
```

Here, the `traffic_light_groups` is a list of all `traffic_light_group` defined in the map file.
In case the map file or any other source contains information about the corresponding entities of `traffic_light_cycle`, these shall be kept in the `traffic_light_control` list.
Note that `traffic_light_control` does not necessarily contain control plans for all `traffic_light_groups` and can also be empty.

The `set_traffic_lights_control_file` modifier is used to specify traffic light control cycles with an external file.
See [map modifier set\_traffic\_lights\_control\_file](road_abstractions.html#_modifier_set_traffic_lights_control_file) for details.

## 8.15.8 Actor for controlling traffic\_lights

Traffic lights are controlled by an actor `traffic_light_controller`, which inherits from `osc_actor`.

### 8.15.8.1 Actor traffic\_light\_controller

Actor for controlling traffic lights and traffic light groups

Basic information
:   Table 329. Basic information of actor traffic\_light\_controller


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [osc\_actor](entity.html#sec-environment-abstract-osc_actor) |

## 8.15.9 Actions for controlling traffic lights

### 8.15.9.1 Setting traffic light bulb states

The `set_bulb_state` action sets the state of a bulb of a single traffic light.

#### 8.15.9.1.1 Action set\_bulb\_state

Set the state of a single traffic light bulb.

Basic information
:   Table 330. Basic information of action set\_bulb\_state


    |  |  |
    | --- | --- |
    | **Action ending** | The action is instantaneous. |

Parameters
:   Table 331. Action set\_bulb\_state


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [traffic\_light](#sec-traffic_lights-class-traffic_light) | [traffic\_light](#sec-traffic_lights-class-traffic_light) | no | The traffic light to which the bulb belongs. Some bulbs can be independent of traffic lights |
    | [bulb\_color](#sec-traffic_lights-enum-bulb_color) | [bulb\_color](#sec-traffic_lights-enum-bulb_color) | yes | Color of the bulb |
    | bulb\_kind | [bulb\_icon](#sec-traffic_lights-enum-bulb_icon) | yes | Icon type of the bulb |
    | [bulb\_state](#sec-traffic_lights-enum-bulb_state) | [bulb\_state](#sec-traffic_lights-enum-bulb_state) | yes | Bulb state to be set |
    | sync | bool | yes | If true, bulb states of all traffic lights in the same synchronization group are set to a bulb state that is consistent according to map.traffic\_light\_control |

This action is instantaneous, meaning that the state change is immediate and permanent unless another `set` action is executed.
Here `sync==true` implies that all bulbs in the synchronization group will be set to a state that is consistent according to `map.traffic_light_control` cycles.

### 8.15.9.2. Setting traffic light states with a list of `bulb_states`

The `set_state` action sets the state of a single traffic light.

#### 8.15.9.2.1 Action set\_state

Set the state of a single traffic light.

Basic information
:   Table 332. Basic information of action set\_state


    |  |  |
    | --- | --- |
    | **Action ending** | The action is instantaneous. |

Parameters
:   Table 333. Action set\_state


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [traffic\_light](#sec-traffic_lights-class-traffic_light) | [traffic\_light](#sec-traffic_lights-class-traffic_light) | yes | The traffic light affected by the action |
    | state | list of bulb\_state | yes | List of bulb states to be set by the action |
    | sync | bool | yes | If true, states of all traffic lights in the same synchronization group are set to a state that is consistent according to map.traffic\_light\_control |

This action is instantaneous, meaning that the state change is immediate and permanent unless another `set` action is executed.
Here `sync==true` implies that all bulbs in the synchronization group will be set to a state that is consistent according to `map.traffic_light_control` cycles.

### 8.15.9.3. Setting `semantic_state` of a traffic\_light

The `set_semantic_state` action sets the semantic state of a single traffic light.

#### 8.15.9.3.1 Action set\_semantic\_state

Set the semantic-state of a single traffic light. If the state is not applicable to the given traffic light, then its state is left unchanged.

Basic information
:   Table 334. Basic information of action set\_semantic\_state


    |  |  |
    | --- | --- |
    | **Action ending** | The action is instantaneous. |

Parameters
:   Table 335. Action set\_semantic\_state


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [traffic\_light](#sec-traffic_lights-class-traffic_light) | [traffic\_light](#sec-traffic_lights-class-traffic_light) | yes | The traffic light affected by the action |
    | state | [semantic\_traffic\_light\_state](#sec-traffic_lights-enum-semantic_traffic_light_state) | yes | Semantic state to be set by the action |
    | sync | bool | yes | If true, states of all traffic lights in the same synchronization group are set to a state that is consistent according to map.traffic\_light\_control |

This action is instantaneous, meaning that the state change is immediate and permanent unless another `set` action is executed.
Here `sync==true` implies that all bulbs in the synchronization group will be set to a state that is consistent according to `map.traffic_light_control` cycles.
If the state is not applicable to the `traffic_light` then its state will remain unchanged.

### 8.15.9.4. Setting state of a single bulb in a `traffic_light_group`

The `set_group_bulb_state` action sets the state of a bulb for all traffic lights of a traffic light group.

#### 8.15.9.4.1 Action set\_group\_bulb\_state

Set state of a single bulb for all traffic lights of a traffic light group.

Basic information
:   Table 336. Basic information of action set\_group\_bulb\_state


    |  |  |
    | --- | --- |
    | **Action ending** | The action is instantaneous. |

Parameters
:   Table 337. Action set\_group\_bulb\_state


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [traffic\_light](#sec-traffic_lights-class-traffic_light) | [traffic\_light](#sec-traffic_lights-class-traffic_light) | yes | The traffic light group affected by the action |
    | [bulb\_color](#sec-traffic_lights-enum-bulb_color) | [bulb\_color](#sec-traffic_lights-enum-bulb_color) | yes | Color of the bulb |
    | bulb\_kind | [bulb\_icon](#sec-traffic_lights-enum-bulb_icon) | yes | Icon type of the bulb |
    | [bulb\_state](#sec-traffic_lights-enum-bulb_state) | [bulb\_state](#sec-traffic_lights-enum-bulb_state) | yes | Bulb state to be set |
    | sync | bool | yes | If true, states of all traffic lights in the same synchronization group are set to a state that is consistent according to map.traffic\_light\_control |

This action is instantaneous, meaning that the state change is immediate and permanent unless another `set` action is executed.
Here `sync==true` implies that all bulbs in the synchronization group will be set to a state that is consistent according to `map.traffic_light_control` cycles.
If the state is not applicable to the `traffic_light_group` then its state will remain unchanged.

### 8.15.9.5. Setting state of a `traffic_light_group` with a list of `bulb_states`

The `set_group_state` action sets the state of all traffic lights of a traffic light group.

#### 8.15.9.5.1 Action set\_group\_state

Set the state for all traffic lights in a traffic light group. If the state is not applicable to the given traffic light, then its state is left unchanged.

Basic information
:   Table 338. Basic information of action set\_group\_state


    |  |  |
    | --- | --- |
    | **Action ending** | The action is instantaneous. |

Parameters
:   Table 339. Action set\_group\_state


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | group | [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) | yes | The traffic light group affected by the action |
    | state | list of bulb\_state | yes | List of bulb states to be set by the action |
    | sync | bool | yes | If true, states of all traffic lights in the same synchronization group are set to a state that is consistent according to map.traffic\_light\_control |

This action is instantaneous, meaning that the state change is immediate and permanent unless another `set` action is executed.
Here `sync==true` implies that all bulbs in the synchronization group will be set to a state that is consistent according to `map.traffic_light_control` cycles.
If the state is not applicable to the `traffic_light_group` then its state will remain unchanged.

### 8.15.9.6. Setting semantic state of a `traffic_light_group`

The `set_group_semantic_state` action sets the semantic state of all traffic lights of a traffic light group.

#### 8.15.9.6.1 Action set\_group\_semantic\_state

Set the semantic state for all traffic lights of a traffic light group.

Basic information
:   Table 340. Basic information of action set\_group\_semantic\_state


    |  |  |
    | --- | --- |
    | **Action ending** | The action is instantaneous. |

Parameters
:   Table 341. Action set\_group\_semantic\_state


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) | [traffic\_light\_group](#sec-traffic_lights-class-traffic_light_group) | yes | The traffic light group affected by the action |
    | state | [semantic\_traffic\_light\_state](#sec-traffic_lights-enum-semantic_traffic_light_state) | yes | List of semantic states to be set by the action |
    | sync | bool | yes | If true, states of all traffic lights in the same synchronization group are set to a state that is consistent according to map.traffic\_light\_control |

This action is instantaneous, meaning that the state change is immediate and permanent unless another `set` action is executed.
Here `sync==true` implies that all bulbs in the synchronization group will be set to a state that is consistent according to `map.traffic_light_control` cycles.
If the state is not applicable to the `traffic_light` then its state will remain unchanged.

### 8.15.9.7 Setting activation cycles

The following action can be used to start the execution of traffic light cycles of any number of `traffic_light_group`.

#### 8.15.9.7.1 Action play\_cycles

This action receives a list of traffic light cycles to control the temporal sequence of the traffic light states of any number of traffic light groups. For each traffic light group the shall be only one cycle.

Basic information
:   Table 342. Basic information of action play\_cycles


    |  |  |
    | --- | --- |
    | **Action ending** | The action ends when another action that affects the state of any traffic light that is controlled by the current cycles is invoked. |

Parameters
:   Table 343. Action play\_cycles


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | cycles | list of traffic\_light\_cycle | yes | list of traffic light cycles to be executed |

The states of the `traffic_lights` in the groups will be changed according to the specified cycles.

## 8.15.10 Examples

### 8.15.10.1 Example 1

The following example shows how to control a traffic light by setting its `bulb_states`.

Code 75. Control a traffic light by its bulb states

```
scenario sut.traffic_light_bulb_state_control:
    # traffic light with 4 bulbs, 2 red, 1 yellow and 1 green.
    # This can be either 1 OpenDrive dynamic signal with with 4 bulbs in one line or 3 vertical and one on a side.
    # This can also be 4 separated OpenDrive traffic light signals with one bulb each.

    # define my_traffic_light, constrain it to be any traffic light on the map that has 4 bulbs,
    # with the first two being red, the third yellow and the fourth green
    my_traffic_light: traffic_light with:
        keep(it.bulbs.size() == 4)
        keep(it.bulbs[0].color == red)
        keep(it.bulbs[1].color == red)
        keep(it.bulbs[2].color == yellow)
        keep(it.bulbs[3].color == green)

    # define stop_line, constrain it to be the stop line of the traffic light group that my_traffic_light belongs to
    stop_line: traffic_light_stop_line with:
        keep(it.traffic_light_group == my_traffic_light.group)

    # define a traffic light controller
    my_traffic_light_controller: traffic_light_controller

    # define two times, yellow_time and red_time
    red_time: time with:
        keep(it in [5s..20s])

    yellow_time: time with:
        keep(it in [1s..3s])

    do parallel():
        # let sut travel the whole length of the road that stop_line is located on
        sut_drive: sut.car.drive() with:
            along(stop_line.road, start_offset: 0m, at: start)
            along(stop_line.road, end_offset: 0m, at: end)

        traffic_light_change: serial():
            # Start traffic light with the red bulb turned on
            set_red: my_traffic_light_controller.set_state(my_traffic_light, [is_on ,is_on, is_off, is_off])

            wait elapsed(red_time)

            # Turn off red bulb and turn on yellow bulb, then wait for 2s
            set_yellow: my_traffic_light_controller.set_state(my_traffic_light, [is_off, is_off, is_on, is_off])

            wait elapsed(yellow_time)

            # Turn off yellow bulb and turn on green bulb
            my_traffic_light_controller.set_state(my_traffic_light, [is_off, is_off, is_off, is_on])
```

### 8.15.10.2 Example 2

The following example shows how to control a traffic light by setting its semantic state.

Code 76. Control a traffic light by its semantic state

```
scenario sut.traffic_light_semantic_state_control:
    # define my_traffic_light, constrain it to be any traffic light on the map that has at least 3 bulbs
    my_traffic_light: traffic_light with:
        keep(it.bulbs.size() >= 3)

    # define stop_line, constrain it to be the stop line of the traffic light group that my_traffic_light belongs to
    stop_line: traffic_light_stop_line with:
        keep(it.traffic_light_group == my_traffic_light.group)

    # define a traffic light controller
    my_traffic_light_controller: traffic_light_controller

    # define a time stop_time
    stop_time: time with:
        keep(it in [5s..20s])

    do parallel():
        # let sut travel the whole length of the road that stop_line is located on
        sut_drive: sut.car.drive() with:
            along(stop_line.road, start_offset: 0m, at: start)
            along(stop_line.road, end_offset: 0m, at: end)

        traffic_light_change: serial():
            # Start traffic light in semantic state stop
            set_stop: my_traffic_light_controller.set_semantic_state(my_traffic_light, stop)

            wait elapsed(stop_time)

            # Change traffic_light to semantic state go_exclusive
            set_go_exclusive: my_traffic_light_controller.set_semantic_state(my_traffic_light, go_exclusive)
```

### 8.15.10.3 Example 3

This example demonstrates event-based triggering of traffic light states.

Code 77. Trigger traffic light states based on events

```
scenario sut.go_to_stop_by_event:
    # define my_traffic_light to be any traffic light on the map
    my_traffic_light: traffic_light

    # define stop_line, constrain it to be the stop line of the traffic light group that my_traffic_light belongs to
    stop_line: traffic_light_stop_line with:
        keep(it.traffic_light_group == my_traffic_light.group)

    # define a traffic light controller
    my_traffic_light_controller: traffic_light_controller

    # trigger event 'sut_at_my_traffic_light' when sut distance to stop_line is 10 m and semantic state of my_traffic_light is still go
    event sut_at_my_traffic_light is (sut.car.distance_along_route(stop_line.road, from: from_start) > (stop_line.offset - 10m)) and my_traffic_light.state_equal(my_traffic_light.semantic_state_to_state(go))

    do parallel():
        # let sut travel the whole length of the road that stop_line is located on
        sut_drive: sut.car.drive() with:
            along(stop_line.road, start_offset: 0m, at: start)
            along(stop_line.road, end_offset: 0m, at: end)

        traffic_light_change: serial():
            # Start traffic light in semantic state go
            set_go: my_traffic_light_controller.set_semantic_state(my_traffic_light, go)

            wait @sut_at_my_traffic_light

            # Change traffic_light to semantic state go_exclusive
            set_stop: my_traffic_light_controller.set_semantic_state(my_traffic_light, stop)
```

### 8.15.10.4 Example 4

This example shows how to let the traffic light controller play the traffic light control plan defined by the map.

Code 78. Execute the traffic light control plan of a map

```
scenario sut.drive_with_traffic_lights:

    # define my_traffic_light to be any traffic light on the map
    my_traffic_light: traffic_light

    # define stop_line, constrain it to be the stop line of the traffic light group that my_traffic_light belongs to
    stop_line: traffic_light_stop_line with:
        keep(it.traffic_light_group == my_traffic_light.group)

    # define a traffic light controller
    my_traffic_light_controller: traffic_light_controller

    do parallel():
        # play traffic light control plan for all traffic lights
        play_traffic_light_cycles: my_traffic_light_controller.play_cycles(map.traffic_light_control)
        # let sut travel the whole length of the road that stop_line is located on
        sut_drive: sut.car.drive() with:
            along(stop_line.road, start_offset: 0m, at: start)
            along(stop_line.road, end_offset: 0m, at: end)
```

### 8.15.10.5 Example 5

This example illustrates how to create a traffic light control plan for a map.

Code 79. Set up a traffic light control plan for a map

```
extend top.main:
    # cycles for traffic_light_group 42
    group42_cycle_phase1: traffic_light_phase with:
        # red for 30 seconds
        keep(it.group.map_id == "42")
        keep(it.bulbs_state == [is_on, is_off, is_off])
        keep(it.duration == 19s)
    group42_cycle_phase2: traffic_light_phase with:
        # yellow for 2 seconds
        keep(it.group.map_id == "42")
        keep(it.bulbs_state == [is_off, is_on, is_off])
        keep(it.duration == 2s)
    group42_cycle_phase3: traffic_light_phase with:
        # green for 30 seconds
        keep(it.group.map_id == "42")
        keep(it.bulbs_state == [is_off, is_off, is_on])
        keep(it.duration == 30s)

    group42_cycle: traffic_light_cycle with:
        keep(it.phases == [group42_cycle_phase1, group42_cycle_phase2, group42_cycle_phase3])

    # cycles for traffic_light_group 43
    group43_cycle_phase1: traffic_light_phase with:
        # green for 30 seconds
        keep(it.group.map_id == "43")
        keep(it.bulbs_state == [is_off, is_off, is_on])
        keep(it.duration == 19s)
    group43_cycle_phase2: traffic_light_phase with:
        # yellow for 2 seconds
        keep(it.group.map_id == "43")
        keep(it.bulbs_state == [is_off, is_on, is_off])
        keep(it.duration == 2s)
    group43_cycle_phase3: traffic_light_phase with:
        # red for 30 seconds
        keep(it.group.map_id == "43")
        keep(it.bulbs_state == [is_on, is_off, is_off])
        keep(it.duration == 30s)

    group43_cycle: traffic_light_cycle with:
        keep(it.phases == [group43_cycle_phase1, group43_cycle_phase2, group43_cycle_phase3])

    keep(map.traffic_light_control == [group42_cycle, group43_cycle])
```