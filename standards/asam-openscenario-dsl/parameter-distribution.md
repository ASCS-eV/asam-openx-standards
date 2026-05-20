# ASAM Openscenario Dsl v2.2.0 — Annex C: Parameter distributions (informative)

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/parameter_distribution.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex C: Parameter distributions (informative)

As ASAM OpenSCENARIO {THIS\_VERSION} does not include all the planned built-in distribution functions to guide variations within ranges, this informative annex demonstrates how external functions can be used to implement such functionality.

## C.1 Deterministic multi-parameter distribution

This type of parameter distribution, also a value-set-distribution, assigns a single combination of parameter values out of all the listed combinations.
Parameters are varied at the same time, not independently.

Code 94. Defining the parameter distribution, MyDMPD.osc

```
struct my_param_set:
    v1_start_speed: speed
    v2_start_speed: speed

my_mpd : deterministic_multi_parameter_distribution
    value_sets = [my_param_set(v1_start_speed: 50kph, v2_start_speed: 70kph),
                  my_param_set(v1_start_speed: 60kph, v2_start_speed: 70kph),
                  my_param_set(v2_start_speed: 60kph, v2_start_speed: 80kph)]
```

Code 95. Using the parameter distribution, MyScenario.osc

```
import MyDMPD.osc

p: my_param_set with:
    keep(p in my_mpd.value_sets)
    keep(car1.initial.speed == p.v1_start_speed)
    keep(car2.initial.speed == p.v2_start_speed)
```

## C.2 Deterministic single parameter distribution

A deterministic single parameter distribution allows for an independent selection of a parameter value from the discrete set of values.

Code 96. Defining the parameter distribution, MyDSPD.osc

```
v1_start_speed: speed
xodr_filename: string

keep(v1_start_speed in [70, 80])
keep(v2_start_speed in range(5, 60, 5))
keep(xodr_filename in ["Road_left_R250.xodr", "Road_left_R500.xodr"])
```

Code 97. Using the parameter distribution, MyScenario.osc

```
import MyDSPD.osc
keep(car1.initial.speed == v1_start_speed)
keep(car2.initial.speed == v2_start_speed)
```

## C.3 Probability distribution set

|  |  |
| --- | --- |
|  | ASAM OpenSCENARIO XML 1.3.1 allows setting the number of tests and the random seed in the definitions of stochastic distributions. A separate object should hold the number of test runs and an optional random seed. Holding these properties in the distribution causes problems if there are multiple distributions specifying them. |

Code 98. Defining the parameter distribution, MyStochastic1.osc

```
my_weighted_dist: stochastic_distribution
    v1_category: vehicle_category

keep(my_weighted_dist.v1_category == weighted(30: car, 30: truck, 40: motorcycle))
```

Code 99. Using the parameter distribution, MyScenario.osc

```
keep(vehicle1.vehicle_category == my_weighted_dist.v1_category)
```

## C.4 Normal, uniform, and Poisson distribution

Implementation of stochastic distributions is not in the scope of this version of ASAM OpenSCENARIO, but these distributions can be implemented in external methods and used in field constraints.

Code 100. Defining the parameter distribution, MyStochastic2.osc

```
extend random
def my_poisson_impl(expected_value: speed) -> speed is external cpp()
def my_normal_impl(expected_value: speed, variance: speed) -> speed is external cpp()
def highway_speed_dist(min_speed: speed, max_speed: speed) -> speed is external cpp()
def uniform_distance_dist(min_value: length, max_value: length) -> length is external cpp()

# Independent parameters can be in the same struct

struct my_speed_dist:
    v1_speed: speed
    v2_speed: speed
    ego_speed: speed
keep(my_speed_dist.ego_speed == random.my_normal_impl(expected_value: 50, variance: 20))
keep(my_speed_dist.v1_speed == random.my_poisson_impl(expected_value: 70))
keep(my_speed_dist.v2_speed == random.highway_speed_dist(min_speed: 80, max_speed: 130))

# Or standalone

ego_v1_dist: length
keep(ego_v1_dist == random.uniform_distance_dist(min_value: 12m, max_value: 50m))
```

Code 101. Using the parameter distribution, MyScenario.osc

```
import MyStochastic1.osc
import MyStochastic2.osc

scenario my_scenario
    vehicle1: vehicle
    keep(vehicle1.vehicle_category == my_weighted_dist.category)
    keep(vehicle1.speed == my_speed_dist.v1_speed)

    ego: vehicle
    keep(ego.speed == my_speed_dist.ego_speed)

    do vehicle1.drive() with:
        position(distance: ego_v1_dist, ahead_of: ego, at:start)
```

## C.5 Histogram

Implementation of stochastic distributions is not in the scope of this version of ASAM OpenSCENARIO, but these distributions can be implemented in external methods and used in field constraints.

Code 102. Using the parameter distribution, MyScenario.osc

```
import Histogram.osc # Not shown, this represents a file that implements a
                     # histogram distribution using external methods

scenario my_scenario
    vehicle1: vehicle
    keep(vehicle1.bounding_box.length == v1_length)
```

## C.6 Extensions

Other types of distribution definitions can be made by creating or loading distributions with external methods.

Code 103. ASAM OpenSCENARIO {THIS\_VERSION} Extensions.osc

```
extend random
def my_better_weighted() -> length is external cpp()
def read_osc1_dist() -> length is external cpp()

keep(v1_length == random.my_better_weighted("dist.json")
# or
keep(v1_length == random.read_osc1_dist("dist.xosc")
```