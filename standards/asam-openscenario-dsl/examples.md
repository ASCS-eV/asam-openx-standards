# ASAM Openscenario Dsl v2.2.0 — Annex A: Scenario examples (informative)

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/annexes/examples.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex A: Scenario examples (informative)

This section provides some examples that were developed during standard development using the ASAM OpenSCENARIO language to exemplify its usage for practical use-cases. The examples are not simulation ready and are included to demonstrate the use of various language features.

## A.1 Euro NCAP

This example is taken from the Euro NCAP test protocol - Lane Support Systems Version [[17](../bibliography.html#bib-encap)]

```
import osc.standard

scenario elk_overtaking:
    gvt: vehicle                # Target vehicle
    dut: vehicle                # Device under test
    routeToFollow: route with:  # Route to be followed
        keep(it.min_lanes == 2)
 
    do parallel:
            dut.drive(duration: 5s) with:
                along(route: routeToFollow)                                # VUT should drive along the route routeToFollow
                lane(side_of: gvt, side: right, at: start)                 # VUT is initially on the right lane
                lane(same_as: gvt, at: end)                                # VUT transitions to the same lane as the target vehicle during the scenario
                lateral(distance: 1m, measure_by: left_to_left, at: start) # VUT has an initial distance of 1m to the lane marking on its
                                                                           # left (between the cars) of the GVT match)
                position(distance: 10.0m, ahead_of: gvt, at: start)        # VUT is initially ahead of GVT
                position(distance: 1m, behind: gvt, at: end)               # At the end, VUT and GVT overlap (s.t. the rear axle of the
                                                                           # VUT and the front)

            gvt.drive() with:
                along(route: routeToFollow)                                    # GVT should drive along the route routeToFollow
                speed(speed: 80kph)                                            # GVT speed is 80 kph
                lateral(distance: 1.5m, measure_by: right_to_right, at: start) # GVT has a constant distance of 1.5m to the lane marking
                                                                               # on its right (between the cars)
```

## A.2. UN regulation No 157

The following example is inspired by the UN regulation No. 157 "Uniform provisions concerning the approval of vehicles with regard to Automated Lane Keeping Systems" [[18](../bibliography.html#bib-alks)]

This example is based on the test scenario in Section 4.1 of Annex 5. "Lane Keeping".

```
# Note: This is a snapshot of a sample scenario file developed as part
# of the OpenSCENARIO 2.x project. It is not intended to demonstrate
# actual UNECE ALKS scenarios, nor is necessarily up to date with final
# OpenSCENARIO 2.0 semantics or domain model usage.

# UNECE 157 ALKS P.60
# 4. Test scenarios to assess the performance of the system with regard to the dynamic driving task
#     4.1. Lane Keeping
#     4.1.1. The test shall demonstrate that the ALKS does not leave its lane and maintains a stable position inside its ego lane across the speed range and
#            different curvatures within its system boundaries.
#     4.1.2. The test shall be executed at least:
#     (a) With a minimum test duration of 5 minutes;
#     (b) With a passenger car target as well as a PTW target as the lead vehicle / other vehicle;
#     (c) With a lead vehicle swerving in the lane; and
#     (d) With another vehicle driving close beside in the adjacent lane.
#
# Addendum in previous chapter:
# The lateral wandering distance the vehicle will normally wander within the lane is 0.375m.

import osc.standard

actor car inherits vehicle(vehicle_category == vehicle_category!car)

scenario swerving_side_vehicle:

    map: map                                         # Map instance
    ego: car              # instantiate ego vehicle
    lead_vehicle: car     # instantiate traffic vehicle 1
    adjacent_vehicle: car # instantiate traffic vehicle 2
    min_dist: length
    max_dist: length

    # define a route for the vehicles
    # current definitions in domain model:
    #   route: ordered list of road elements (not ODR road sections!)
    #   path: Sequence of coordinates without any time constraints
    #   trajectory: Sequence of coordinates with time stamps

    # current answer, but may be different in future
    r1: road with: # instantiate the road section
        keep(it.min_lanes == 2) # Ensure we have at least 2 lanes
        # We need to additionally require lanes to be driving lanes => will be clarified soon

        # Different options
        # 1. specify adjacency of lanes in dynamical part


    # (a) With a minimum test duration of 5 minutes
    test_duration: time
    keep(test_duration >= 5min)

    do parallel(duration: test_duration):

        # 4.1.1. The test shall demonstrate that the ALKS does not leave its lane and maintains a stable position inside its ego lane across the speed range and
        #        different curvatures within its system boundaries.
        ego.drive() with:                                               # ego drives
            # lane(left_of: adjacent_vehicle)                           # one lane to the left of the adjacent_vehicle
            # lane(side_of: adjacent_vehicle, side: left)               # same as above
            lane(side_of: adjacent_vehicle, side: map.inner_side())     # "inner" means "left" or "right" depending on whether right-hand or left-hand driving
            along(r1)                                                   # on the road r1, which has been required to have at least 2 lanes above (may be omitted, but not clear)
            speed([0kph..60kph])                                        # 0 and 60 may be replaced by parameters like ego_init_speed and so on

        # (c) With a lead vehicle swerving in the lane
        lead_vehicle.drive() with:
            lane(same_as: ego)
            position([min_dist..max_dist], ahead_of: ego)                # distance is currently measured center to center(?). But will be adressed
                                                                         # Add parameter for minimum distance
                                                                         # Alternatives would be:
                                                                         # - Using serials with lateral modifier
                                                                         # - use path modifier with path defined somewhere else
                                                                         #   1. Define trajectory in some variable X
                                                                         #   2. Use sth like path(X) here
                                                                         # - using a profile with way points from real world data incl distr

        # (d) With another vehicle driving close beside in the adjacent lane
        parallel:
            adjacent_vehicle.follow_lane(offset: 0.375m)                # specialized action (short hand for drive) same as drive with keep_lane(lateral: 0.375)
                                                                        # adjacent vehicle should drive as close beside as allowed by the ALKS to be not
                                                                        # lane change intention (cut in)
            adjacent_vehicle.drive() with:
                position([-1m,1m], ahead_of: ego)
```