# ASAM OpenODD® v1.0.0 — C.2 (informative) Car-to-car front turn across path example

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_c_case_studies_02_ccftap.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# C.2 (informative) Car-to-car front turn across path example

## C.2.1 Introduction

This case study shows an example in YAML format.
The ODD is designed around an autonomous vehicle performing a Car-to-Car Front Turn-Across-Path (CCFtap) test case.
The COD file contains seven CODs, with time stamps about 1 minute apart.

## C.2.2 Taxonomy

Code 224. Example case study taxonomy (YAML) - file taxonomy.yml

```
TAXONOMY:
  # Taxonomy consisting of weather and atmospheric conditions (including satellite based global positioning).
  environmental_conditions:

    ambient_air_temperature: float ambient_temperature  # DegCelsius

    weather:
      wind:
        wind_speed: float velocity  # m/s
        wind_type:
          no_wind:
            wind_speed: "< 0.1 m/s"
          light_breeze:
            wind_speed: "[0.1 .. 3.3] m/s"
          strong_breeze:
            wind_speed: "[3.3 .. 13.8] m/s"
          gale:
            wind_speed: "[13.8 .. 20.7] m/s"
          storm:
            wind_speed: "> 20.7 m/s"

      rain:
        average_rainfall_per_hour: float precipitation_rate
        average_rainfall_per_area: float precipitation_rate
        rainfall_rate: float precipitation_rate # mm/h
        rain_type:
          no_rain:
            rainfall_rate: "< 0.1 mm/h"
          light_rain:
            rainfall_rate: "[0.1 .. 2.5] mm/h"
          moderate_rain:
            rainfall_rate: "[2.5 .. 7.6] mm/h"
          heavy_rain:
            rainfall_rate: "> 7.6 mm/h"

      snowfall:
        snowfall_visibility: float length # km
        is_snowing: boolean
        snowfall_type:
          light_snow:
            snowfall_visibility: "> 1 km"
          moderate_snow:
            snowfall_visibility: "[0.5 .. 1] km"
          heavy_snow:
            snowfall_visibility: "< 0.5 km"

      illumination:
        artificial_illuminance:
          - streetlights
          - oncoming_vehicle_lights
          - indoor_lights
        natural_illuminance: float illuminance # lux
          daylight:
            illuminance: ">= 2000 lux"
          low_ambient:
            illuminance: "[200 .. 2000] lux"
          night:
            illuminance: "< 200 lux"

      connectivity:
        positioning:
          satellite_based_global_positioning:
            - Global_Positioning_System
            - Galileo
            - GLONASS
            - RTK
```

## C.2.3 ODD

Code 225. Example case study ODD (YAML)

```
IMPORT:
  - taxonomy.yml
  - shapefile_astazero.shp   # Shapefile definition for AstaZero test site

ODD:
  main_module_ccftap:
    TITLE: ODD CCFtap case
    INCLUDE_AND:
      region: true
      module_drivable_area: true
      illumination: true
      connectivity: true
      direction_of_travel:
        - right-hand_travel
      speed: "< 50.0 km/h"
      ambient_air_temperature: "[5.0 .. 25.0] C"
      junction:
        - none
        - cross_road
    EXCLUDE_OR:
      excluded_traffic_agents: true
      bad_weather: true
      particulates: true

############# INCLUDED MODULES #############

MODULES:
  module_region:
    LABEL:
      region
    INCLUDE_AND:
      country:
        - Sweden
      service_area:
        - shapefile_astazero.shp

  module_drivable_area:
    LABEL:
      drivable_area
    INCLUDE_AND:
      drivable_area_type:
        - primary_roads
      drivable_area_type_classification:
        - with_active_traffic_management
        - without_active_traffic_management
      drivable_area_surface_type:
        - asphalt
      lane_marking:
        - clear_lane_marking
        - temporary_lane_marking
        - no_lane_marking
      lane_type:
        - traffic_lane
      number_of_lanes: "2"
      lane_dimensions:
        - lane_width: "[3.25 .. 3.5] m"
      drivable_area_edge:
        - solid_barriers
        - none
      drivable_area_shoulder:
        - paved
        - gravel
        - grass
      drivable_area_signs:
        - regulatory_signs
        - warning_signs
        - information_signs
        - none

  module_illumination:
    LABEL:
      illumination
    INCLUDE_AND:
      artificial_illuminance:
        - streetlights
        - oncoming_vehicle_lights
      illuminance: ">= 250.0 lux"

  module_connectivity:
    LABEL:
      connectivity
    INCLUDE_AND:
      positioning:
        - global_positioning_system
      connectivity_bandwidth: ">= 1.0 Mbps"
      latency: "< 10.0 ms"

############# EXCLUDED MODULES #############

  module_traffic_agents:
    LABEL:
      excluded_traffic_agents
    INCLUDE_OR:
      agent_type:
        - non_motor_vehicle
        - vulnerable_road_users
        - animals

  module_weather_conditions:
    LABEL:
      bad_weather
    INCLUDE_OR:
      wind_speed: "> 5.4 m/s"
      rainfall_rate: "> 7.6 mm/h"
      snowfall: True
      cloudiness_rate: "> 4.0 oktas"

  module_particulates:
    LABEL:
      particulates
    INCLUDE_OR:
      particulates_type:
        - sand
        - dust
        - smoke_and_pollution
        - fog
```

## C.2.4 COD

Code 226. Example case study COD (YAML)

```
COD:
    - TEMPORAL_EXTENT:                                            "2024-06-19 09:36:12.812"
      SPATIAL_EXTENT:                                             "57.772755 12.771464"
      RAINFALL_RATE;mm/hr:                                        0.000
      RAINFALL_LEVEL;categorical_literal:                         no_rain
      WIND_SPEED;m/s:                                             0.000
      IS_PEDESTRIANS;boolean:                                     false
      PEDESTRIAN.COUNT;count:                                     0
      IS_JUNCTION; boolean:                                       false
      IS_JUNCTION;categorical_literal:                            none
      DRIVABLE_AREA_TYPE;categorical_literal:                     primary_roads
      DRIVABLE_AREA_SURFACE_TYPE;categorical_literal:             asphalt
      LANE_TYPE;categorical_literal:                              traffic_lane
      LANE_TYPE.COUNT;count:                                      2
      LANE_TYPE.LANE_WIDTH;m:                                     3.5
      LANE_MARKING;categorical_literal:                           clear_lane_marking
      DRIVABLE_AREA_TYPE_CLASSIFICATION;categorical_literal:      without_activate_traffic_management
      DRIVABLE_AREA_SHOULDER;categorical_literal:                 paved
      DRIVABLE_AREA_SIGNS;categorical_literal:                    None
      ILLUMINATION.ILLUMINATION;lux:                              1000
      ILLUMINATION.ARTIFICIAL_ILLUMINANCE;lux:                    oncoming_vehicle_lights
      POSITIONING;categorical_literal:                            global_positioning_system

    - TEMPORAL_EXTENT:                                            "2023-06-19 09:37:45.142"
      SPATIAL_EXTENT:                                             "57.772783, 12.771306"
      RAINFALL_RATE;mm/hr:                                        0.000
      RAINFALL_LEVEL;categorical_literal:                         no_rain
      WIND_SPEED;m/s:                                             0.000
      IS_PEDESTRIANS;boolean:                                     false
      PEDESTRIAN.COUNT;count:                                     0
      IS_JUNCTION;boolean:                                        false
      IS_JUNCTION;categorical_literal:                            none
      DRIVABLE_AREA_TYPE;categorical_literal:                     primary_roads
      DRIVABLE_AREA_SURFACE_TYPE;categorical_literal:             asphalt
      LANE_TYPE;categorical_literal:                              traffic_lane
      LANE_TYPE.COUNT;count:                                      2
      LANE_TYPE.LANE_WIDTH;m:                                     3.5
      LANE_MARKING;categorical_literal:                           clear_lane_marking
      DRIVABLE_AREA_TYPE_CLASSIFICATION;categorical_literal:      without_activate_traffic_management
      DRIVABLE_AREA_SHOULDER;categorical_literal:                 paved
      DRIVABLE_AREA_SIGNS;categorical_literal:                    None
      ILLUMINATION.ILLUMINATION;lux:                              1000
      ILLUMINATION.ARTIFICIAL_ILLUMINANCE;lux:                    oncoming_vehicle_lights
      POSITIONING;categorical_literal:                            global_positioning_system

    - TEMPORAL_EXTENT:                                            "2024-06-19 09:39:26.291"
      SPATIAL_EXTENT:                                             "57.772801, 12.771170"
      RAINFALL_RATE;mm/hr:                                        0.000
      RAINFALL_LEVEL;categorical_literal:                         no_rain
      WIND_SPEED;m/s:                                             0.000
      IS_PEDESTRIANS;boolean:                                     false
      PEDESTRIAN.COUNT;count:                                     0
      IS_JUNCTION;boolean:                                        false
      IS_JUNCTION;categorical_literal:                            none
      DRIVABLE_AREA_TYPE;categorical_literal:                     primary_roads
      DRIVABLE_AREA_SURFACE_TYPE;categorical_literal:             asphalt
      LANE_TYPE;categorical_literal:                              traffic_lane
      LANE_TYPE.COUNT;count:                                      2
      LANE_TYPE.LANE_WIDTH;m:                                     3.5
      LANE_MARKING;categorical_literal:                           clear_lane_marking
      DRIVABLE_AREA_TYPE_CLASSIFICATION;categorical_literal:      without_activate_traffic_management
      DRIVABLE_AREA_SHOULDER;categorical_literal:                 paved
      DRIVABLE_AREA_SIGNS;categorical_literal:                    None
      ILLUMINATION.ILLUMINATION;lux:                              1000
      ILLUMINATION.ARTIFICIAL_ILLUMINANCE;lux:                    oncoming_vehicle_lights
      POSITIONING;categorical_literal:                            global_positioning_system

    - TEMPORAL_EXTENT:                                            "2024-06-19 09:41:06.725"
      SPATIAL_EXTENT:                                             "57.772785, 12.771297"
      RAINFALL_RATE;mm/hr:                                        0.000
      RAINFALL_LEVEL;categorical_literal:                         no_rain
      WIND_SPEED;m/s:                                             0.000
      IS_PEDESTRIANS;boolean:                                     false
      PEDESTRIAN.COUNT;count:                                     0
      IS_JUNCTION;boolean:                                        false
      IS_JUNCTION;categorical_literal:                            none
      DRIVABLE_AREA_TYPE;categorical_literal:                     primary_roads
      DRIVABLE_AREA_SURFACE_TYPE;categorical_literal:             asphalt
      LANE_TYPE;categorical_literal:                              traffic_lane
      LANE_TYPE.COUNT;count:                                      2
      LANE_TYPE.LANE_WIDTH;m:                                     3.5
      LANE_MARKING;categorical_literal:                           clear_lane_marking
      DRIVABLE_AREA_TYPE_CLASSIFICATION;categorical_literal:      without_activate_traffic_management
      DRIVABLE_AREA_SHOULDER;categorical_literal:                 paved
      DRIVABLE_AREA_SIGNS;categorical_literal:                    None
      ILLUMINATION.ILLUMINATION;lux:                              1000
      ILLUMINATION.ARTIFICIAL_ILLUMINANCE;lux:                    oncoming_vehicle_lights
      POSITIONING;categorical_literal:                            global_positioning_system

    - TEMPORAL_EXTENT:                                            "2024-06-19 09:42:47.186"
      SPATIAL_EXTENT:                                             "57.772814, 12.771070"
      RAINFALL_RATE mm/hr:                                        0.000
      RAINFALL_LEVEL;categorical_literal:                         no_rain
      WIND_SPEED;m/s:                                             0.000
      IS_PEDESTRIANS;boolean:                                     false
      PEDESTRIAN.COUNT;count:                                     0
      IS_JUNCTION;boolean:                                        true
      IS_JUNCTION;categorical_literal:                            cross_road
      DRIVABLE_AREA_TYPE;categorical_literal:                     primary_roads
      DRIVABLE_AREA_SURFACE_TYPE;categorical_literal:             asphalt
      LANE_TYPE;categorical_literal:                              traffic_lane
      LANE_TYPE.COUNT;count:                                      2
      LANE_TYPE.LANE_WIDTH;m:                                     3.5
      LANE_MARKING;categorical_literal:                           clear_lane_marking
      DRIVABLE_AREA_TYPE_CLASSIFICATION;categorical_literal:      without_activate_traffic_management
      DRIVABLE_AREA_SHOULDER;categorical_literal:                 paved
      DRIVABLE_AREA_SIGNS;categorical_literal:                    None
      ILLUMINATION.ILLUMINATION;lux:                              1000
      ILLUMINATION.ARTIFICIAL_ILLUMINANCE;lux:                    oncoming_vehicle_lights
      POSITIONING;categorical_literal:                            global_positioning_system

    - TEMPORAL_EXTENT:                                            "2024-06-19 09:44:27.881"
      SPATIAL_EXTENT:                                             "57.772835, 12.770925"
      RAINFALL_RATE mm/hr:                                        0.000
      RAINFALL_LEVEL;categorical_literal:                         no_rain
      WIND_SPEED;m/s:                                             0.000
      IS_PEDESTRIANS;boolean:                                     false
      PEDESTRIAN.COUNT;count:                                     0
      IS_JUNCTION; boolean:                                       true
      IS_JUNCTION; categorical_literal:                           cross_road
      DRIVABLE_AREA_TYPE;categorical_literal:                     primary_roads
      DRIVABLE_AREA_SURFACE_TYPE;categorical_literal:             asphalt
      LANE_TYPE;categorical_literal:                              traffic_lane
      LANE_TYPE.COUNT;count:                                      2
      LANE_TYPE.LANE_WIDTH;m:                                     3.5
      LANE_MARKING;categorical_literal:                           clear_lane_marking
      DRIVABLE_AREA_TYPE_CLASSIFICATION;categorical_literal:      without_activate_traffic_management
      DRIVABLE_AREA_SHOULDER;categorical_literal:                 paved
      DRIVABLE_AREA_SIGNS;categorical_literal:                    None
      ILLUMINATION.ILLUMINATION;lux:                              1000
      ILLUMINATION.ARTIFICIAL_ILLUMINANCE;lux:                    oncoming_vehicle_lights
      POSITIONING;categorical_literal:                            global_positioning_system

    - TEMPORAL_EXTENT:                                            "2024-06-19 09:46:08.172"
      SPATIAL_EXTENT:                                             "57.772693, 12.770763"
      RAINFALL_RATE;mm/hr:                                        0.000
      RAINFALL_LEVEL;categorical_literal:                         no_rain
      WIND_SPEED;m/s:                                             0.000
      IS_PEDESTRIANS;boolean:                                     false
      PEDESTRIAN.COUNT;count:                                     0
      IS_JUNCTION; boolean:                                       true
      IS_JUNCTION; categorical_literal:                           cross_road
      DRIVABLE_AREA_TYPE;categorical_literal:                     primary_roads
      DRIVABLE_AREA_SURFACE_TYPE;categorical_literal:             asphalt
      LANE_TYPE;categorical_literal:                              traffic_lane
      LANE_TYPE.COUNT;count:                                      2
      LANE_TYPE.LANE_WIDTH;m:                                     3.5
      LANE_MARKING;categorical_literal:                           clear_lane_marking
      DRIVABLE_AREA_TYPE_CLASSIFICATION;categorical_literal:      without_activate_traffic_management
      DRIVABLE_AREA_SHOULDER;categorical_literal:                 paved
      DRIVABLE_AREA_SIGNS;categorical_literal:                    None
      ILLUMINATION.ILLUMINATION;lux:                              1000
      ILLUMINATION.ARTIFICIAL_ILLUMINANCE;lux:                    oncoming_vehicle_lights
      POSITIONING;categorical_literal:                            global_positioning_system
```