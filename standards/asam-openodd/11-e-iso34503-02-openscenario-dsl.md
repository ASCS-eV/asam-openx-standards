# ASAM OpenODD® v1.0.0 — B.2 ASAM OpenSCENARIO® DSL ISO 34503

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_e_iso34503_02_openscenario_dsl.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.2 ASAM OpenSCENARIO® DSL ISO 34503

The listing in [Code 215](#code-taxonomy-osc) shows an ASAM OpenSCENARIO® DSL representation of the taxonomy defined in ISO 34503 [[4](../bibliography.html#bib-iso34503)].

Code 215. Definition of a taxonomy (ASAM OpenSCENARIO® DSL)

```
# file domain_concepts_definition_iso_34503

# =======================================
# ==== ODD Domain Concepts ISO 34503 ====
# =======================================

type speed is SI(m: 1, s: -1)
unit kmph of speed is SI(m: 1, s: -1, factor: 0.277777778)
unit mmph of speed is SI(m: 1, s: -1, factor: 0.000277778)

type distance is SI(m: 1)
unit meters of length is SI(m: 1)
unit mm of length is SI(m: 1, factor: 0.001)

type temperature is SI(K:1)
unit C of temperature is SI(K:1, offset: 273)

type particles_per_volume is SI(m : -3)
unit ppm3 of particles_per_volume is SI(m: -3)

type angle is SI(rad: 1)
unit rad of angle is SI (rad: 1, factor: 1.0)
unit deg of angle is SI (rad: 1, factor: 0.01745329251) # pi/180

type time is SI(s: 1)  # Base SI unit: second
unit s of time is SI(s: 1)  # Seconds
unit ms of time is SI(s: 1, factor: 0.001)  # Milliseconds
unit min of time is SI(s: 1, factor: 60)  # Minutes
unit h of time is SI(s: 1, factor: 3600)  # Hours

enum definition_mode : [default, permissive, restrictive]


struct odd_element: # ‘abstract’ superclass of all structs that represent ‘taxonomy’ concepts
    definition_mode : definition_mode = default
    def current_zone() -> zone # returns the current zone of the subject vehicle, to be implemented based on detailed vehicle position in current world state (real or simulated)


struct odd inherits odd_element:
    environmental_conditions : environmental_conditions
    scenery : scenery
    dynamic_elements : dynamic_elements
    sampling_metadata : sampling_metadata


struct sampling_metadata:
    sampling_time : date_time
    sampling_location : geo_location_3D


struct geo_location_3D:
    latitude: angle  # Valid range: -90 to 90 degrees
    longitude: angle  # Valid range: -180 to 180 degrees
    altitude: length  # Typically no less than -400 meters (below sea level)


struct date_time:
    year: int  # calendar year, four-digit value, based on Gregorian calendar
    month: int  # calendar month, Valid range: 1 to 12
    day: int  # calendar day, valid range: 1 to 31
    hour: time  # use unit h, valid range: 0 to 23 h
    minute: time  # use unit min, valid range: 0 to 59 min
    second: time  # use unit s, valid range: 0 to 59 s
    millisecond: time  # use unit ms, valid range: 0 to 999 ms


# scenery.zones (9.2)
enum zone: [ zone_undefined ] # to be extended in odd definitions via 'extends'


# ----------
#  scenery
# ----------

struct scenery inherits odd_element:
    zones : zones
    drivable_area : drivable_area
    junctions : junctions
    basic_structures : basic_structures
    special_structures : special_structures
    fixed_road_structure : fixed_road_structures
    temporary_road_structure : temporary_road_structures


# scenery.drivable_area (9.3)
struct drivable_area inherits odd_element:
    drivable_area_type : drivable_area_type
    drivable_area_geometry : drivable_area_geometry
    drivable_area_lane_specification : drivable_area_lane_specification
    drivable_area_signs : drivable_area_signs
    drivable_area_edge : drivable_area_edge
    drivable_area_surface : drivable_area_surface


# scenery.drivable_area.drivable_area_type (9.3.2)
enum drivable_area_type: [motorways_or_highways_or_interstates, primary_roads, radial_roads, distributor_roads, minor_or_local_roads, slip_roads_or_off_ramps, parking_space, shared_space]


# scenery.drivable_area.drivable_area_geometry (9.3.3)
struct drivable_area_geometry inherits odd_element:
    horizontal_plane : horizontal_plane
    transverse_plane : transverse_plane
    longitudinal_plane : longitudinal_plane


# From ISO 34503, Sect. 9.3.3 "Drivable area geometry"
# In a horizontal plane, two main attributes should be included:
# 1) straight lines; and
# 2) curves.
struct horizontal_plane inherits odd_element:
    curvature_radius : length # Curvature radius of the road. Positive values for curves; infinity or a very high value for straight lines. The exact threshold value is not specified by ISO 34503 nor ASAM OpenODD®.
    straight_line : bool # if true, it means there is no curvature


# scenery.drivable_area.drivable_area_geometry.transverse_plane
# From ISO 34503, Sect. 9.3.3 "Drivable area geometry"
# In a transverse plane, the main attributes should at least be classified into
# the following attributes or have additional attributes:
# i) type: divided, undivided, pavement
# ii) barriers on road edges;
# v) types of lanes together;
# vi) superelevation / banking.
# -> what does "types of lanes together" mean, and what would be values for this attribute?
struct transverse_plane inherits odd_element:
    transverse_plane_type : transverse_plane_type
    barriers_on_road_edges : bool
    types_of_lanes_together : list of lane_type # Values are different combinations of lanes that occur alongside each other, e.g. driving lane plus bike lane.
    superelevation_banking: angle # the angle at which the road surface is tilted relative to the horizontal plane. This tilt, also called the bank angle, is used on curved sections of the road to help counteract the lateral forces that act on a vehicle when it is turning.


enum transverse_plane_type : [divided, undivided, pavement]


# scenery.drivable_area.drivable_area_geometry.longitudinal_plane
struct longitudinal_plane inherits odd_element:
    up_slope : angle
    down_slope : angle
    level_plane : boolean # if true, this implies a level plane and up- and down slope have very small values. The exact threshold value is not specified by ISO 345ß3 nor OpenODD.


# scenery.drivable_area.drivable_area_lane_specification (9.3.4)
struct drivable_area_lane_specification inherits odd_element:
    lane_dimensions : lane_dimensions
    lane_markings : lane_marking
    lane_type : lane_type
       number_of_lanes : int
    direction_of_travel : direction_of_travel
    speed_limit : speed


# scenery.drivable_area.drivable_area_lane_specification.lane_dimensions (9.3.4)
struct lane_dimensions inherits odd_element:
    width: length
    height: length


# scenery.drivable_area.drivable_area_lane_specification.lane_marking (9.3.4)
enum lane_marking: [clear_lane_marking, blurred_lane_marking, no_lane_marking, temporary_lane_marking]


# scenery.drivable_area.drivable_area_lane_specification.lane_type (9.3.4)
enum lane_type: [bus_lane, traffic_lane, cycle_lane, tram_lane, emergency_lane, shared_lane, other_special_purpose_lanes]


# scenery.drivable_area.drivable_area_lane_specification.direction_of_travel (9.3.4)
enum direction_of_travel : [right_hand_travel, left_hand_travel]


# scenery.drivable_area.drivable_area_signs (9.3.5), may be detailed further
struct drivable_area_signs inherits odd_element:
    sign_type : sign_type
    sign_feature : sign_feature


# sign type: regulatory signs (e.g. traffic lights), warning signs, information signs;
enum sign_type : [regulatory_sign, warning_signs, information_signs]


# b) sign feature: movable signs, fixed signs.
enum sign_feature :  [movable_sign, fixed_sign]


# scenery.drivable_area.drivable_area_edge (9.3.6)
struct drivable_area_edge inherits odd_element:
    line_markers : bool
    shoulder_type : shoulder_type
    showbanks : bool
    solid_barriers : solid_barriers_type
    temporary_line_markers : bool


enum shoulder_type : [paved, gravel, grass]


enum solid_barriers_type : [grating, rails, curb, cones]


# scenery.drivable_area.drivable_area_surface (9.3.7)
struct drivable_area_surface inherits odd_element:
    drivable_area_surface_type : drivable_area_surface_type
    drivable_area_surface_features : drivable_area_surface_features
    drivable_area_induced_surface_condition : drivable_area_induced_surface_condition


enum drivable_area_surface_type : [asphalt, cement_concrete, pavers, cobblestone, granite_setts, gravel]


enum drivable_area_surface_features : [cracks, potholes, ruts, swells, speed_bumpers, intentional_speed_reduction_obstacles]


enum drivable_area_induced_surface_condition : [icy, flooded, standing_water, snow_on_surface, wet, surface_contamination]


# scenery.junctions (9.4)
struct junctions inherits odd_element:
    roundabouts : roundabouts
    intersections : intersections


# scenery.junctions.roundabouts (9.4.2)
struct roundabouts inherits odd_element:
    roundabout_type : roundabout_type
    signalised : bool


enum roundabout_type : [none, mini, compact, normal, large, double, multiple]


# scenery.junctions.intersections (9.4.3)
struct intersections inherits odd_element:
    intersection_type : intersection_type
    signalised : bool


enum intersection_type : [none, t_junction, y_junction, cross_road, staggered, grade_separated]


# scenery.basic_structures (9.5) -- Naming inconsistency basic structures vs fixed structures?
# May need to be detailed with further attributes
enum basic_structures    : [buildings, streetlights, street_furniture, vegetation]


# scenery.special_structures (9.6)
# This modeling differs from the previous schema, since the different special structures each have individual attributes for width, height, usage.
struct special_structures inherits odd_element:
    # the field special_structure_types models what types of special structures are
    # present in the COD. This can be any subset of elements in special_structures_type,
    # i.e., there can be a predestrian crossing next to a bridge.
    # ODD specificaitons can use keep statements to constrain the allowed subset,
    # for example keep(special_structure_types in [bridge,tunnel] if only bridges and
    # tunnels are allowed).
    special_structure_types : list of special_structures_type
    # the fields below are used to contain further information about special structures
    # present in the vehcile's COD.
    automatic_access_control_barrier: automatic_access_control_barrier
    bridge : bridge
    pedestrian_crossing : pedestrian_crossing
    rail_crossing : rail_crossing
    tunnel : tunnel
    toll_plaza : toll_plaza


struct abstract_special_structure inherits odd_element:
    width : length
    height : length

enum special_structures_type: [automatic_access_control_barrier, bridge, pedestrian_crossing, rail_crossing, tunnel, toll_plaza]


struct automatic_access_control_barrier inherits abstract_special_structure


struct bridge inherits abstract_special_structure


struct pedestrian_crossing inherits abstract_special_structure


struct rail_crossing inherits abstract_special_structure


struct tunnel inherits abstract_special_structure


struct toll_plaza inherits abstract_special_structure


# scenery.temporary_road_structures (9.7)
enum temporary_road_structures: [construction_site_detour, refuse_collection, road_work, signage]


# -------------------------------
#  environmental_conditions (10)
# -------------------------------

struct environmental_conditions inherits odd_element:
    weather : weather
    particulates : particulates
    illumination : illumination
    connectivity : connectivity


# environmental_conditions.weather (10.2)
struct weather inherits odd_element:
    ambient_air_temperature : temperature # (10.2.2)
    wind : wind_kind # (10.2.3)
    rainfall : rainfall
    snowfall : snow_kind


# environmental_conditions.weather.wind_kind (10.2.3)
enum wind_kind: [no_wind, calm, light_air, light_breeze, gentle_breeze, moderate_breeze, fresh_breeze, strong_breeze, near_gale, gale, strong_gale, storm, violent_storm, hurricane]


# environmental_conditions.weather.rainfall (10.2.3)
struct rainfall inherits odd_element:
    rainfall_intensity : speed
    rainfall_type : rainfall_type
    rainfall_intensity_kind : rainfall_intensity_kind
    # Intra-taxonomy consistency constraints between RainfallIntensityKind and rainfall_intensity expressed as a numeric value with unit mmph
    keep((rainfall_intensity_kind == no_rain => rainfall_intensity == 0.0 mmph) and (rainfall_intensity == 0.0 mmph => rainfall_intensity_kind == no_rain))
    keep((rainfall_intensity_kind == light_rain => rainfall_intensity > 0.0 mmph and rainfall_intensity <= 2.5 mmph) and (rainfall_intensity > 0.0 mmph and rainfall_intensity <= 2.5 mmph => rainfall_intensity_kind == light_rain))
    keep((rainfall_intensity_kind == moderate_rain => rainfall_intensity > 2.5 mmph and rainfall_intensity <= 7.6 mmph) and (rainfall_intensity > 2.5 mmph and rainfall_intensity <= 7.6 mmph => rainfall_intensity_kind == moderate_rain ))
    keep((rainfall_intensity_kind == heavy_rain => rainfall_intensity > 7.6 mmph and rainfall_intensity <= 50 mmph) and (rainfall_intensity > 7.6 mmph and rainfall_intensity <= 50 mmph => rainfall_intensity_kind == heavy_rain))
    keep((rainfall_intensity_kind == violent_rain => rainfall_intensity > 50 mmph and rainfall_intensity <= 100 mmph) and (rainfall_intensity > 50 mmph and rainfall_intensity <= 100 mmph => rainfall_intensity_kind == violent_rain))
    keep((rainfall_intensity_kind == cloudburst => rainfall_intensity > 100 mmph) and (rainfall_intensity > 100 mmph => rainfall_intensity_kind == cloudburst))


enum rainfall_type : [dynamic, convective, orographic]


enum rainfall_intensity_kind: [no_rain, light_rain, moderate_rain, heavy_rain, violent_rain, cloudburst]


# environmental_conditions.weather.snow_kind (10.2.5)
enum snow_kind: [no_snow, light_snow, moderate_snow, heavy_snow]


# environmental_conditions.particulates (10.2.5)
struct particulates inherits odd_element:
    intensity : particles_per_volume
    size : length
    particulates_types : list of particulates_type


# can be refined to sub-structs with individual specification of intensity, size.
# For example, smoke concentration may be measured in how many nanograms per cubic meter of particles up to which size are present.
enum particulates_type : [dust, smoke_and_pollution, volcanic_ash, water_spray, non_precipitating_water, droplets, blowing_debris]


struct illumination inherits odd_element:
    illumination_type : illumination_type
    cloudiness_type : cloudiness_type


# 10.6
# Which kinds of connectivity and positioning does exist?
struct connectivity
    v2v_type : list of connectivity_type
    v2i_type : list of connectivity_type
    v2p_type : list of connectivity_type
    v2n_type : list of connectivity_type
    positioning_type : list of positioning_type


enum connectivity_type: [none, 2G, 2.5G, 3G, 4G, 5G, Satellite, Wifi, short_range_communications_DSRC, TS-G5, sidelink_PC5]


enum positioning_type: [none, GPS, Galileo, GLONASS, RTK, GLONASS, BeiDou]


# ----------------------
#  dynamic_elements (11)
# ----------------------

struct dynamic_elements inherits odd_element:
    traffic_agents : traffic_agents
    subject_vehicle : subject_vehicle


# dynamic_elements.traffic_agents (11.1)
struct traffic_agents inherits odd_element:
    agent_types : list of agent_type
    special_vehicles : list of special_vehicle_type
    ambulance : ambulance


struct ambulance:
    speed : speed


enum agent_type : [motor_vehicle, non_motor_vehicle, vulnerable_road_users, animals, horse_riders]


enum special_vehicle_type : [ambulance, police_vehicle, work_vehicle, traffic_management_vehicle, fire_engine_or_appliance_vehicle]


struct subject_vehicle inherits odd_element:
    maximum_allowed_speed : speed # represents the current legal allowed speed for the subject vehicle


struct route:
    waypoints : list of location


struct location:
    latitude : float
    longitude : float
```