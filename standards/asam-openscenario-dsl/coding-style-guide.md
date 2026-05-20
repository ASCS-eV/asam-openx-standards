# ASAM OpenSCENARIO® DSL v2.2.0 — 9.2 Formatting ASAM OpenSCENARIO code

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/user-guide/coding_style_guide.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.2 Formatting ASAM OpenSCENARIO code

## 9.2.1 Coding style guide

This coding style guide is intended to help you write source code in the ASAM OpenSCENARIO domain-specific language in a uniform way.

### 9.2.1.1 Introduction

This guide focuses on uniform formatting and naming for source code.
It does not contain best practices nor is it a reference for the language.

You should follow the recommendations in this document if you are a *scenario developer* writing scenarios for real use.

By following the recommendations in this guide the code becomes easy to understand for you and other users.

## 9.2.2 Formatting

### 9.2.2.1 Indentation

* Use **four space characters** per indentation level.
* Do *not* use tab characters.
* Use the following text editor settings:

  + **Tab size: 4**
  + **Insert spaces**

### 9.2.2.2 Encoding

* Use **UTF-8** as encoding.

### 9.2.2.3 Whitespace

Whitespace characters provide better readability when used in the correct places.

* Use only **space characters** as whitespace.
* Replace tabs with four spaces as described in [Section 9.2.2.1, “Indentation”](#sec-osc2-coding-style-guide-indentation).

The correct use of space characters within ASAM OpenSCENARIO source code is as follows:

* **One space** *after* a **comma** (in argument lists and other lists)
* **One space** *after* a **colon** (for example for inheritance)
* **One space** *before and after* a **keyword**
* **One space** *before and after* an **operator**
* **No spaces** *before and after* **brackets and braces** (for example, in function calls or for indexing)
* **No space** *between* **value and unit**

The following code snippet shows some examples of the correct use of space characters.

Code 84. Correct use of space characters

```
func(arg[1], arg2)
if x == 4: print x, y
foo == [x, y, z]
func(1)
abc[key] = lst[index]
i = i + 1
actor bus: car(category: bus):
   keep(width == 1.8m)
   keep(length == 4.5m)

swerve_story: serial:
    side_vehicle.drive() with:
        path(s_side_vehicle)
        keep_speed()
    with:
        until (top.time > 5sec)
```

### 9.2.2.4 Comments

* Single lines of comments and inline comments can be added using the **'pound' symbol (#)**.

  ```
  # This is a single line comment.
  ```

  ```
  i = i + 42  # This is an inline comment
  ```
* Blocks of comments can be simulated by using several single lines of comments.

  ```
  # This is a block of comments example.
  # The following call to foo is commented out
  # Reason: see issue xyz
  # More explanation here...
  #
  # foo()
  ```

### 9.2.2.5 Line breaks

* Consider breaking up statements that are too long to fit into one line.  
  Use the line continuation special character **'backslash' (\)** for marking the continuation.

  ```
  This is a line of text that is too long for a single \
  line, so continue after the backslash in a new line.
  ```

## 9.2.3 Naming

Naming conventions are a widely discussed topic with great influence on readability influenced by fashion changes, habit, and personal taste.

Here are the recommendations valid for naming conventions in ASAM OpenSCENARIO source code.

### 9.2.3.1. Use *snake\_case* only

* Use ***snake\_case*** (aka *lowercase\_with\_underscore*) for all source code elements that are not keywords.

Code 85. Example for correctly formatted code

```
# 1: Define an actor
actor car_group:
     average_distance: length
     number_of_cars: uint

# 2: Define a road element struct
struct geometric_road: road_element:
    min_radius: length
    max_radius: length
    side: av_side

# 3: Define a scenario
scenario dut.traverse_junction_at_yield:
    s: road_with_sign with(sign_type: yield)
    do dut.car.traverse_junction() with: ...

# 4: Define a containing scenario
scenario dut.mix_three_dangers:
     weather_kind: weather_kind
     keep(weather_kind != clear)
     do mix:
         cut_in_and_slow()
         traverse_junction_at_yield()
         weather(kind: weather_kind)
```

### 9.2.3.2 Single character names

Do not use the following characters as single character names because they can be easily misread as zero (0) or one (1):

* No single lowercase *'el'* (l)
* No single uppercase *'eye'* (I)
* No single lowercase *'oh'* (o)
* No single uppercase *'oh'* (O)

## 9.2.4 Example

Here is a more complex example showing all the rules.

Code 86. Example for correctly formatted code in ASAM OpenSCENARIO

```
# Create enums for vehicle color and model
enum vehicle_color: [black, white, silver, blue, red, yellow]
enum vehicle_model: [bluebird_vision_2014, oem_ego_vehicle]

# Extend basic vehicle actor with color and model fields
extend vehicle:
    color: vehicle_color
    model: vehicle_model

# Create a scenario with a slower large vehicle in an adjacent lane
scenario slower_large_vehicle_in_adjacent_lane:
    # Set the map file
    map: map
    map.set_map_file("/maps/example.xodr")

    # Create ego vehicle
    ego: vehicle with:
        # Set the model to oem_ego_vehicle
        keep(it.model == oem_ego_vehicle)

    # Create a slower large vehicle
    v1: vehicle with:
        # Set the vehicle category to bus
        keep(it.vehicle_category == bus)
        # Set the model to bluebird_vision_2014
        keep(it.model == bluebird_vision_2014)
        # Set the color to black
        keep(it.color == yellow)

    # Define a lane section with three lanes
    simple_three_lane_road: lane_section
    lane_left: lane
    lane_center: lane
    lane_right: lane
    keep(simple_three_lane_road.lanes == [lane_left, lane_center, lane_right])

    # Make sure lanes are ordered according to their names
    map.lane_side(lane_center, left, lane_right)
    map.lane_side(lane_left, left, lane_center)

    # Ego behavior parameters
    ego_start_speed: speed
    keep(ego_start_speed in [60..80]kph)
    ego_lane: lane
    keep(ego_lane in simple_three_lane_road.lanes)

    # Vehicle 1 behavior parameters
    v1_start_speed: speed
    keep(v1_start_speed in [40kph..60kph])

    v1_start_distance: length
    keep(v1_start_distance in [20..100]m)

    vehicle_1_side: side_left_right
    vehicle_1_lane: lane
    keep(vehicle_1_lane in simple_three_lane_road.lanes)

    # Choose ego_lane based on vehicle_1_side and vehicle_1_lane
    keep(vehicle_1_lane == lane_left and vehicle_1_side == left => ego_lane in [lane_center, lane_right])
    keep(vehicle_1_lane == lane_right and vehicle_1_side == right => ego_lane in [lane_center, lane_left])
    keep(vehicle_1_lane == lane_center and vehicle_1_side == left => ego_lane == lane_right)
    keep(vehicle_1_lane == lane_center and vehicle_1_side == right => ego_lane == lane_left)

    # Define thresholds for later use in events
    simulation_time_threshold: time
    ego_ttc_threshold: time
    ego_distance_threshold: length


    keep(simulation_time_threshold == 120s)
    keep(ego_ttc_threshold == 1s)
    keep(ego_distance_threshold == 0.3m)

    # External KPI functions
    def distance_between_vehicles(vehicle1: vehicle, vehicle2: vehicle) -> length is external python("distance_between_vehicles", "kpi.py")
    def get_ttc_between_vehicles(vehicle1: vehicle, vehicle2: vehicle) -> time is external python("get_ttc_between_vehicles", "kpi_ttc.py")

    # Sample variables
    var simulation_time: time = sample(simulation.time, @simulation_clock)
    var ego_ttc_to_v1: time = sample(get_ttc_between_vehicles(vehicle1: ego, vehicle2: v1), @simulation_clock)
    var ego_distance_to_v1: length = sample(distance_between_vehicles(vehicle1: ego, vehicle2: v1), @simulation_clock)

    # Events
    event ego_ttc_threshold_reached is ego_ttc_to_v1 < ego_ttc_threshold
    event ego_close_to_v1 is ego_distance_to_v1 < ego_distance_threshold
    event simulation_time_exceeded is simulation_time > simulation_time_threshold

    # Status bools set by events
    var ego_ttc_threshold_reached_bool: bool = false
    ego_ttc_threshold_reached_bool = sample(true, @ego_ttc_threshold_reached)

    var ego_close_to_v1_bool: bool = false
    ego_close_to_v1_bool = sample(true, @ego_close_to_v1)

    var simulation_time_exceeded_bool: bool = false
    simulation_time_exceeded_bool = sample(true, @simulation_time_exceeded)

    # End simulation if either simulation time exceeds the threshold or the ego vehicle is too close to vehicle 1 or the ego vehicle's TTC is too low
    event end_simulation is (ego_ttc_threshold_reached_bool or ego_close_to_v1_bool or simulation_time_exceeded_bool)

    do parallel(overlap: equal):
        # Ego starts in a specific lane, continues driving until simulation time exceeded or it gets too close to Vehicle 1 either in TTC or distance
        ego_drive: ego.drive() with:
            along(ego_lane, at: start)
            speed(speed: ego_start_speed, at: start)
            until @end_simulation

        # Vehicle 1 starts ahead of ego vehicle at a specific speed in an adjacent lane, keeps speed and lane throughout the scenario
        v1_drive: v1.drive() with:
            along(vehicle_1_lane, at: start)
            speed(speed: v1_start_speed, at: start)
            keep_speed()
            keep_lane()
            position(distance: v1_start_distance, ahead_of: ego, at: start)
```

## 9.2.5 Related topics

If you cannot find a recommendation for your source code formatting or naming problem in this chapter, follow the [Style Guide for Python Code (PEP 8)](https://www.python.org/dev/peps/pep-0008/).