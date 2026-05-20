# ASAM OpenODD® v1.0.0 — C.1 (informative) Hands free ADS example

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_c_case_studies_01_hands_free.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# C.1 (informative) Hands free ADS example

## C.1.1 Introduction

This case study shows the same example in various formats.

The feature is designed for a public road with uninterrupted traffic flow, controlled access and separation of traffic directions.
Safe operation should be possible for atmospheric condition with a visibility of 150 meters.

The ODD for “automated lane-change” will extend the conditions of “handsfree”.

## C.1.2 Taxonomy

### C.1.2.1 YAML

Code 218. Example case study taxonomy (YAML) as file handsfree\_taxonomy.yaml

```
root:
  _node_type: Container
  scenery:
    _node_type: Container
    Drivable_Area:
      _node_type: Record
      attributes:
        road_type:
          _abstract_attr_type: categorical
          _concrete_attr_type: RoadType
        opposite_traffic_present:
          _abstract_attr_type: primitive
          _concrete_attr_type: boolean
        traffic_separation:
          _abstract_attr_type: categorical
          _concrete_attr_type: TrafficSeparationType
        number_of_driving_lanes_the_ego_direction:
          _abstract_attr_type: primitive
          _concrete_attr_type: int
        ego_lane:
          _abstract_attr_type: record
          _concrete_attr_type: Lane
        adjacent_lane_left:
          _abstract_attr_type: record
          _concrete_attr_type: Lane
        adjacent_lane_right:
          _abstract_attr_type: record
          _concrete_attr_type: Lane
        road_boundary_right:
          _abstract_attr_type: categorical
          _concrete_attr_type: RoadBoundaryType
    Lane:
      _node_type: Record
      attributes:
        width:
          _abstract_attr_type: primitive
          _concrete_attr_type: float
        curvature:
          _abstract_attr_type: primitive
          _concrete_attr_type: float
        allowed_speed:
          _abstract_attr_type: primitive
          _concrete_attr_type: float
        lane_boundary_left:
          _abstract_attr_type: record
          _concrete_attr_type: LaneBoundary
        lane_boundary_right:
          _abstract_attr_type: record
          _concrete_attr_type: LaneBoundary
        lane_boundary_color:
          _abstract_attr_type: categorical
          _concrete_attr_type: LaneBoundaryColor
        split_merge_in_front_present:
          _abstract_attr_type: primitive
          _concrete_attr_type: boolean
    LaneBoundary:
      _node_type: Record
      attributes:
        lb_type:
          _abstract_attr_type: categorical
          _concrete_attr_type: LaneBoundaryType
        lb_color:
          _abstract_attr_type: categorical
          _concrete_attr_type: LaneBoundaryColor
    TrafficSeparationType:
      _node_type: Categorical
      _literals:
        - one_way_road
        - physical_barrier
        - solid_line
        - virtual
        - allowed_to_use_opposite_lane
    LaneBoundaryColor:
      _node_type: Categorical
      _literals:
        - not applicable
        - white
        - blue
        - yellow
    LaneBoundaryType:
      _node_type: Categorical
      _literals:
        - virtual
        - solid_line
        - solid_solid
        - solid_dashed
        - dashed
        - dashed_sold
        - botts_dot
        - other_longitudinal_marking
        - road_boundary
    RoadBoundaryType:
      _node_type: Categorical
      _literals:
        - guard_rail
        - curb
        - grass
        - other
        - unmarked
    RoadType:
      _node_type: Categorical
      _literals:
        - motorway
        - rural
        - highway

  environmental_conditions:
    _node_type: Container
    Visibility:
      _node_type: PrimitiveType
      _value_:
        _abstract_attr_type: primitive
        _concrete_attr_type: float

  generic_types:
    _node_type: Container
    boolean:
      _node_type: PrimitiveType
    int:
      _node_type: PrimitiveType
    float:
      _node_type: PrimitiveType
```

### C.1.2.2 XML

Code 219. Example case study taxonomy (XML)

```
<TAXONOMY>
    <CONCEPT id="id001" name="root">
        <CONCEPT id="id002" name="scenery" parent_id="id001">
            <CONCEPT id="id003" name="DrivableArea" parent_id="id002">
                <TAXONOMY_DEFINED_TYPE id="id009" name="roadType" type_id="id005"/>
                <BOOLEAN id="id_o_t_p" name="opposite_traffic_present"  parent_id="id003"/>
                <TAXONOMY_DEFINED_TYPE id="id_ts" name="traffic_separation" type_id="id_t_s"/>
                <NUMERIC id="id_nodled" name="number_of_driving_lanes_the_ego_direction" value_type="parent" unit_std="ASAM" unit_type="count"></NUMERIC>
                <TAXONOMY_DEFINED_TYPE id="id_ego_lane" name="ego_lane" type_id="id_lane"/>
                <TAXONOMY_DEFINED_TYPE id="id_adjacent_lane_right" name="adjacent_lane_right" type_id="id_lane"/>
                <TAXONOMY_DEFINED_TYPE id="id_adjacent_lane_left" name="adjacent_lane_left" type_id="id_lane"/>
                <TAXONOMY_DEFINED_TYPE id="id_road_boundary_right" name="road_boundary_right" type_id="id_rbt"/>
            </CONCEPT>
            <CONCEPT id="id005" name="road_type">
                <CATEGORICAL id="id006" name="motorway"/>
                <CATEGORICAL id="id007" name="rural"/>
                <CATEGORICAL id="id008" name="highway"/>
            </CONCEPT>
            <CONCEPT id="id_t_s" name="traffic_separation">
                <CATEGORICAL id="id_owr" name="one_way_road"/>
                <CATEGORICAL id="id_pb" name="physical_barrier"/>
                <CATEGORICAL id="id_sl" name="solid_line"/>
                <CATEGORICAL id="id_t_s_v" name="virtual"/>
                <CATEGORICAL id="id_atuol" name="allowed_to_use_opposite_lane"/>
            </CONCEPT>
            <CONCEPT id="id_lbc" name="LaneBoundaryColor">
                <CATEGORICAL id="id_lbc_na" name="not_applicable"/>
                <CATEGORICAL id="id_lbc_w" name="white"/>
                <CATEGORICAL id="id_lbc_b" name="blue"/>
                <CATEGORICAL id="id_lbc_y" name="yellow"/>
            </CONCEPT>
            <CONCEPT id="id_rbt" name="RoadBoundaryType">
                <CATEGORICAL id="id_rbt_gr" name="guard_rail"/>
                <CATEGORICAL id="id_rbt_c" name="curb"/>
                <CATEGORICAL id="id_rbt_g" name="grass"/>
                <CATEGORICAL id="id_rbt_o" name="other"/>
                <CATEGORICAL id="id_rbt_u" name="unmarked"/>
            </CONCEPT>
            <CONCEPT id="id_lbt" name="LaneBoundaryType">
                <CATEGORICAL id="id_virtual" name="virtual"/>
                <CATEGORICAL id="id_solid_line" name="solid_line"/>
                <CATEGORICAL id="id_solid_solid" name="solid_solid"/>
                <CATEGORICAL id="id_solid_dashed" name="solid_dashed"/>
                <CATEGORICAL id="id_dashed" name="dashed"/>
                <CATEGORICAL id="id_dashed_solid" name="dashed_solid"/>
                <CATEGORICAL id="id_botts_dot" name="botts_dot"/>
                <CATEGORICAL id="id_other_longitudinal_marking" name="other_longitudinal_marking"/>
                <CATEGORICAL id="id_road_boundary" name="road_boundary"/>
            </CONCEPT>
            <CONCEPT id="id_lane" name="Lane">
                <NUMERIC id="id_lane_width" name="lane_width" value_type="float" unit_std="ASAM" unit_type="length" parent_id="id_lane"/>
                <!-- unit="inverse radius" curvature k=1/R not yet introduced in OpenODD schema-->
                <NUMERIC id="id_curvature" name="lane_curvature" value_type="float" unit_std="WIKIPEDIA" unit_type="curvature" parent_id="id_lane" />
                <NUMERIC id="id_allowed_speed" name="allowed_speed" value_type="float" unit_std="ASAM" unit_type="velocity" parent_id="id_lane"/>
                <TAXONOMY_DEFINED_TYPE id="id_lbl" name="lane_boundary_left" type_id="id_lbt"/>
                <TAXONOMY_DEFINED_TYPE id="id_lbr" name="lane_boundary_right" type_id="id_lbt"/>
                <TAXONOMY_DEFINED_TYPE id="id_lb_c" name="lane_boundary_color" type_id="id_lbc"/>
                <BOOLEAN id="id_split_merge_in_front_present" name="split_merge_in_front_present" parent_id="id_lane"/>
            </CONCEPT>
        </CONCEPT>
        <CONCEPT id="id_environment" name="environmetal_condition">
            <NUMERIC id="id_visibility" name="visibility" value_type="float" unit_std="met_office" unit_type="length" parent_id="id_environment"/>
        </CONCEPT>
    </CONCEPT>
</TAXONOMY>
```

### C.1.2.3 ASAM OpenSCENARIO® DSL

Code 220. Example case study taxonomy (ASAM OpenSCENARIO® DSL)

```
# file handsfree_taxonomy.osc

# ========================================================================================
# ==== Operational Domain Concepts - RB Case Study Handsfree simplified in OSC format ====
# ========================================================================================

# root container
# OSC syntax for Container unclear: namespace within separate osc files and import operator in ODD_Module definition?
# versus "struct" construct in OSC (slightly different semantic) ?

struct root:
    scenery : Scenery
    environmental_conditions : Environmental_Conditions

struct Scenery:
    drivable_area : Drivable_Area

struct Drivable_Area:
    road_type: RoadType
    opposite_traffic_present: bool
    traffic_separation: TrafficSeparationType
    number_of_driving_lanes_the_ego_direction: int
    ego_lane: Lane
    adjacent_lane_left: Lane
    adjacent_lane_right: Lane
    road_boundary_right: RoadBoundaryType

struct Lane:
    width:  Length
    curvature: Curvature
    allowed_speed: Speed
    lane_boundary_left: LaneBoundary
    lane_boundary_right: LaneBoundary
    lane_boundary_color: LaneBoundaryColor
    split_merge_in_front_present: bool

type Curvature is SI (m:-1)
unit inverse_meters of Curvature is SI (m:-1)

type Speed is SI(m: 1, s: -1)
unit kmph of Speed is SI(m: 1, s: -1, factor: 0.277777778)
unit mmph of Speed is SI(m: 1, s: -1, factor: 0.000277778)

type Length is SI(m: 1)
unit meters of Length is SI(m: 1)
unit mm of Length is SI(m: 1, factor: 0.001)

struct LaneBoundary:
    lb_type: LaneBoundaryType
    lb_color: LaneBoundaryColor

enum TrafficSeparationType: [one_way_road, physical_barrier, solid_line, virtual, allowed_to_use_opposite_lane]
enum RoadType : [motorway, rural, highway]
enum LaneBoundaryColor : [not_applicable, white, blue, yellow]
enum LaneBoundaryType : [virtual, solid_line, solid_solid, solid_dashed, dashed, dashed_sold, botts_dot, other_longitudinal_marking, road_boundary]
enum RoadBoundaryType: [guard_rail, curb, grass, other, unmarked]

# environmental_conditions container, child of root

struct Environmental_Conditions:
    visibility: Length

# alternative not compliant with OSC syntax validator, several types with the same unit seems to be not allowed (for example, length and visibility in meters)
# type Visibility is SI(m: 1)
# unit meters of Visibility is SI(m: 1)
# struct Environmental_Conditions:
#   visibility: Visibility
```

### C.1.2.4 Tabular

Table 150. Example case study taxonomy in tabular form - taxonomy root


| CONCEPT\_ID (node name) | PARENT\_ID | Node\_TYPE |
| --- | --- | --- |
| root | NULL | Container |
| scenery | root | Container |
| Drivable\_Area | scenery | Record |
| Lane | scenery | Record |
| LaneBoundary | scenery | Record |
| TrafficSeparationType | scenery | Categorical |
| LaneBoundaryColor | scenery | Categorical |
| LaneBoundaryType | scenery | Categorical |
| RoadBoundaryType | scenery | Categorical |
| RoadType | scenery | Categorical |
| environmental\_condition | root | Container |
| Visibility | environmental\_condition | PrimitiveType |
| generic\_types | root | Container |
| boolean | generic\_types | PrimitiveType |
| int | generic\_types | PrimitiveType |
| float | generic\_types | PrimitiveType |

Table 151. Example case study taxonomy in tabular form - record types


| Record\_Type (concept\_name) | Attribute (name) | Attr\_Type\_Abstract | Attr\_Type\_Concrete |
| --- | --- | --- | --- |
| Drivable\_Area | road\_type | categorical | RoadType |
| Drivable\_Area | opposite\_traffic\_present | primitive | boolean |
| Drivable\_Area | traffic\_separation | categorical | TrafficSeparationType |
| Drivable\_Area | number\_of\_driving\_lanes\_the\_ego\_direction | primitive | int |
| Drivable\_Area | ego\_lane | record | Lane |
| Drivable\_Area | adjacent\_lane\_left | record | Lane |
| Drivable\_Area | adjacent\_lane\_right | record | Lane |
| Drivable\_Area | road\_boundary\_right | categorical | RoadBoundaryType |
| Lane | width | primitive | float |
| Lane | curvature | primitive | float |
| Lane | allowed\_speed | primitive | int |
| Lane | lane\_boundary\_left | record | LaneBoundary |
| Lane | lane\_boundary\_right | record | LaneBoundary |
| Lane | lane\_boundary\_color | categorical | LaneBoundaryColor |
| Lane | split\_merge\_in\_front\_present | primitive | boolean |
| LaneBoundary | lb\_type | categorical | LaneBoundaryType |
| LaneBoundary | lb\_color | categorical | LaneBoundaryColor |
| LaneBoundary | width | primitive | float |
| Visibility | value | primitive | float |

Table 152. Example case study taxonomy in tabular form - categorical types


| Categorical\_Type (enumType) | Categorical\_literal (enum\_Value) |
| --- | --- |
| RoadType | motorway |
| RoadType | rural |
| RoadType | highway |
| TrafficSeparationType | one\_way\_road |
| TrafficSeparationType | physical\_barrier |
| TrafficSeparationType | solid\_line |
| TrafficSeparationType | vegetation |
| TrafficSeparationType | allowed\_to\_use\_opposite\_lane |
| LaneBoundaryType | virtual |
| LaneBoundaryType | solid\_line |
| LaneBoundaryType | solid\_solid |
| LaneBoundaryType | solid\_dashed |
| LaneBoundaryType | dashed |
| LaneBoundaryType | dashed\_sold |
| LaneBoundaryType | botts\_dot |
| LaneBoundaryType | other\_longitudinal\_marking |
| LaneBoundaryType | road\_boundary |
| LaneBoundaryColor | not applicable |
| LaneBoundaryColor | white |
| LaneBoundaryColor | blue |
| LaneBoundaryColor | yellow |
| LaneBoundaryColor | other |
| RoadBoundaryType | guard\_rail |
| RoadBoundaryType | curb |
| RoadBoundaryType | grass |
| RoadBoundaryType | unmarked |
| RoadBoundaryType | other |

## C.1.3 ODD

### C.1.3.1 YAML

Code 221. Example case study ODD (YAML)

```
IMPORT:
  - handsfree_taxonomy.yaml

MODULE:
  odd_HF_1:
    TITLE: ODD for Handsfree-Feature  v0.1
    DESCRIPTION: this module is the ODD description for L2+ Handsfree Feature
    INCLUDE_AND:
      Visibility: "> 100 m"
      regular_lane_marking_present: true # this is label of module below
      OR:
        Drivable_Area.road_type: ["motorway", "highway"]
        Drivable_Area.traffic_separation: ["one_way_road", "physical_barrier"]
    EXCLUDE_OR:
      Drivable_Area.ego_lane.width: "< 3.5 m"
      Drivable_Area.ego_lane.curvature: "[-0.0625 .. 0.0625] 1/m" # unit = m^-1, radius = 16 m
      Drivable_Area.ego_lane.split_merge_in_front_present: true # if lane change feature not available, then deactivate handsfree before passing lane_split/lane_merge
  regular_lane_marking_present:
    TITLE: regular_lane_marking
    DESCRIPTION: this module defines conditions on lane delimitation required for L2+ Handsfree Feature
    LABELS:
      - lane_marking
    INCLUDE_OR:
      - AND:
          Drivable_Area.traffic_separation: "one_way_road"
          Drivable_Area.traffic_separation.number_of_driving_lanes_the_ego_direction: "= 1"
      - AND:
          Drivable_Area.ego_lane.lane_boundary_left.lb_type: ["solid_line","solid_solid","solid_dashed","dashed","dashed_sold","botts_dot","other_longitudinal_marking","road_boundary"]
          Drivable_Area.ego_lane.lane_boundary_right.lb_type: ["solid_line","solid_solid","solid_dashed","dashed","dashed_sold","botts_dot","other_longitudinal_marking","road_boundary"]
    EXCLUDE_OR:
      Drivable_Area.ego_lane.lane_boundary_left.lb_type: "virtual"
      Lane.lane_boundary_color: "yellow" # valid for all Lanes (instances in COD) in vicinity of ego
      Drivable_Area.road_boundary_right: "unmarked"
```

### C.1.3.2 XML

Code 222. Example case study ODD (XML)

```
<MODULES>
    <MODULE id="id_root_module" handle="odd_HF_1">
        <INCLUDE_AND>
            <MODULE_REF id="id_regular_lane_marking"/>
            <GREATER_THAN_NUMBER_TERM field="id_visibility" min="100" unit="meters"/>
            <OR>
                <SET field="id009">
                    <CATEGORICAL_REF id="id006"/>
                    <CATEGORICAL_REF id="id008"/>
                </SET>
                <SET field="id_ts">
                    <CATEGORICAL_REF id="id_owr"/>
                    <CATEGORICAL_REF id="id_pb"/>
                </SET>
            </OR>
        </INCLUDE_AND>
        <EXCLUDE_OR>
             <!--  instance ego_lane:Lane and its lane_width in context (named attr) of DrivableArea referenced -->
             <!-- relative_addressed_field using xpath assuming instantiated DrivableArea -->
             <!-- field ="lane_width" corresponds to value of attr lane_width:float within instance egoLane:lane, which is instantiated within the instance of DriveableArea -->
            <GREATER_THAN_NUMBER_TERM min="3.5" rel_xpath="/ODD/Taxonomy/CONCEPT[@name='DrivableArea']/TAXONOMY_DEFINED_TYPE@name=egoLane/NUMERIC@name='lane_width'" unit="meters" />
            <RANGE_TWO_NUMBERS_TERM  min="-0.0625" max="0.0625" unit="inverse_meters" rel_xpath="/ODD/Taxonomy/CONCEPT[@name='DrivableArea']/TAXONOMY_DEFINED_TYPE@name=egoLane/NUMERIC@name='lane_curvature'" />
            <BOOLEAN_REF rel_xpath="/ODD/Taxonomy/CONCEPT[@name='DrivableArea']/TAXONOMY_DEFINED_TYPE@name=egoLane/BOOLEAN@name='split_merge_in_front_present'"/>
        </EXCLUDE_OR>
    </MODULE>
    <MODULE id="id_regular_lane_marking">
        <INCLUDE_OR>
            <AND>
                <SET field="id_ts">
                    <CATEGORICAL_REF id="id_owr"/>
                </SET>
                <EQUAL_TO_NUMBER_TERM field="id_nodled" value="1" unit="count"></EQUAL_TO_NUMBER_TERM>
            </AND>
            <AND>
                <SET rel_xpath="/ODD/Taxonomy/CONCEPT[@name='DrivableArea']/TAXONOMY_DEFINED_TYPE@name=egoLane/TAXONOMY_DEFINED_TYPE@name='lane_boundary_left'">
                    <CATEGORICAL_REF id="id_solid_line"/>
                    <CATEGORICAL_REF id="id_solid_solid"/>
                    <CATEGORICAL_REF id="id_solid_dashed"/>
                    <CATEGORICAL_REF id="id_dashed"/>
                    <CATEGORICAL_REF id="id_dashed_solid"/>
                    <CATEGORICAL_REF id="id_botts_dot"/>
                    <CATEGORICAL_REF id="id_road_boundary"/>
                </SET>
                <SET rel_xpath="/ODD/Taxonomy/CONCEPT[@name='DrivableArea']/TAXONOMY_DEFINED_TYPE@name=egoLane/TAXONOMY_DEFINED_TYPE@name='lane_boundary_right'">
                    <CATEGORICAL_REF id="id_solid_line"/>
                    <CATEGORICAL_REF id="id_solid_solid"/>
                    <CATEGORICAL_REF id="id_solid_dashed"/>
                    <CATEGORICAL_REF id="id_dashed"/>
                    <CATEGORICAL_REF id="id_dashed_solid"/>
                    <CATEGORICAL_REF id="id_botts_dot"/>
                    <CATEGORICAL_REF id="id_road_boundary"/>
                </SET>
            </AND>
        </INCLUDE_OR>
        <EXCLUDE_OR>
            <SET rel_xpath="/ODD/Taxonomy/CONCEPT[@name='DrivableArea']/TAXONOMY_DEFINED_TYPE@name=egoLane/TAXONOMY_DEFINED_TYPE@name='lane_boundary_right'">
                <CATEGORICAL_REF id="id_virtual"/>
            </SET>
            <SET rel_xpath="/ODD/Taxonomy/CONCEPT[@name='DrivableArea']/TAXONOMY_DEFINED_TYPE@name=egoLane/TAXONOMY_DEFINED_TYPE@name='road_boundary_right'">
                <CATEGORICAL_REF id="id_rbt_u"/>
            </SET>
        </EXCLUDE_OR>
    </MODULE>
</MODULES>
```

### C.1.3.3 ASAM OpenSCENARIO® DSL

Code 223. Example case study ODD (ASAM OpenSCENARIO® DSL)

```
# file handsfree_feature_ODD.osc
# ==================================================================================================
# ==== Operational Design Domain Definition - RB Case Study Handsfree simplified in OSC format  ====
# ==================================================================================================
import handsfree_taxonomy

# module ood_HF_1

extend Environmental_Conditions :
    keep (visibility > 100 meters )
extend Drivable_Area :
    keep(road_type in [motorway, highway] or
         traffic_separation in [one_way_road, physical_barrier])
    keep( not (
                ego_lane.width < 3.5 meters or
                (ego_lane.curvature in [-0.0625 inverse_meters .. 0.0625 inverse_meters]  ) or
                ego_lane.split_merge_in_front_present ))

# module regular_lane_marking_present
extend Drivable_Area :
    keep(
            (  traffic_separation == one_way_road
                and
               traffic_separation.number_of_driving_lanes_the_ego_direction == 1
            )
            or (
                ego_lane.lane_boundary_left.lb_type in [ solid_line , solid_solid , solid_dashed , dashed , dashed_sold , botts_dot , other_longitudinal_marking , road_boundary ]
                and
                ego_lane.lane_boundary_right.lb_type in [ solid_line , solid_solid , solid_dashed , dashed , dashed_sold , botts_dot , other_longitudinal_marking , road_boundary ]
            )
    )
    keep( not (ego_lane.boundary == virtual or
               ego_lane.color == yellow or
               road_boundary_right == unmarked )
    )
```

### C.1.3.4 Tabular

Table 153. Example case study ODD in tabular form


| MODULE\_ID | ROLE | CONTENT\_OR\_CONDITION |
| --- | --- | --- |
| 1 | handle | odd\_HF\_1 |
| 1 | type | odd |
| 1 | export | file\_hf\_1.yaml |
| 1 | references | taxonomy.yaml |
| 1 | title-EN | ODD for Handsfree-Feature v0.1 |
| 1 | include\_AND | Visibility: > 100 m |
| 1 | include\_AND | Drivable\_Area.road\_type: "motorway" OR Drivable\_Area.road\_type: "highway" OR Drivable\_Area.traffic\_separation: "one\_way\_road" OR Drivable\_Area.traffic\_separation: "physical\_barrier" |
| 1 | include\_AND | regular\_lane\_marking\_present: true |
| 1 | exclude\_OR | Drivable\_Area.ego\_lane.width: < 3.5 m |
| 1 | exclude\_OR | Drivable\_Area.ego\_lane.curvature: [-0.0625 .. 0.0625] 1/m |
| 1 | exclude\_OR | Drivable\_Area.ego\_lane.split\_merge\_in\_front\_present: true |
| 2 | handle | regular\_lane\_marking\_present |
| 2 | labels | lane\_marking |
| 2 | include\_OR | Drivable\_Area.traffic\_separation: "one\_way\_road" AND number\_of\_driving\_lanes\_the\_ego\_direction: 1 |
| 2 | include\_OR | Drivable\_Area.ego\_lane.lane\_boundary\_left: ["solid\_line","solid\_solid","solid\_dashed","dashed","dashed\_sold","botts\_dot","other\_longitudinal\_marking","road\_boundary"] AND Drivable\_Area.ego\_lane.lane\_boundary\_right: "solid\_line","solid\_solid","solid\_dashed","dashed","dashed\_sold","botts\_dot","other\_longitudinal\_marking","road\_boundary"] |
| 2 | exclude\_OR | Drivable\_Area.ego\_lane.lane\_boundary\_left: "virtual" |
| 2 | exclude\_OR | Lane.lane\_boundary\_color: "yellow" |
| 2 | exclude\_OR | Drivable\_Area.road\_boundary\_right: "virtual" |

## C.1.4 COD

Table 154. Example case study COD in tabular form


| # | TEMPORAL\_EXTENT | SPATIAL\_EXTENT | road\_type | opposite\_traffic\_present | traffic\_separation | number\_of\_driving\_lanes\_the\_ego\_direction | ego\_lane | adjacent\_lane\_left | adjacent\_lane\_right | boundary\_right | Visibility |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | dummy\_TE\_1 | dummy\_SE\_1 | motorway | FALSE | physical\_barrier | 3 | {  "width": 3,  "curvature": 1/500,  "allowed\_speed": 130,  "lane\_boundary\_left": {  "lb\_color": "white",  "lb\_width": 0.3,  "lb\_type": "dashed"  },  "lane\_boundary\_right": {  "lb\_color": "white",  "lb\_width": 0.4,  "lb\_type": "solid\_dashed"  },  "split\_merge\_in\_front\_present": true  } | {  "width": 3,  "curvature": 1/496.7,  "allowed\_speed": 130,  "lane\_boundary\_left": {  "lb\_color": "white",  "lb\_width": 0.3,  "lb\_type": "road\_boundary"  },  "lane\_boundary\_right": {  "lb\_color": "white",  "lb\_width": 0.3,  "lb\_type": "dashed"  },  "split\_merge\_in\_front\_present": false  } | {  "width": 3.7,  "curvature": 1/503.75,  "allowed\_speed": 80,  "lane\_boundary\_left": {  "lb\_color": "white",  "lb\_width": 0.3,  "lb\_type": "dashed"  },  "lane\_boundary\_right": {  "lb\_color": "white",  "lb\_width": 0.4,  "lb\_type": "dashed\_solid"  },  "split\_merge\_in\_front\_present": true  } | guard\_rail | 200 |
| 2 | dummy\_TE\_2 | dummy\_SE\_2 | motorway | FALSE | physical\_barrier | 2 | {  "width": 3,  "curvature": 1/500,  "allowed\_speed": 130,  "lane\_boundary\_left": {  "lb\_color": "white",  "lb\_width": 0.3,  "lb\_type": "dashed"  },  "lane\_boundary\_right": {  "lb\_color": "white",  "lb\_width": 0.4,  "lb\_type": "solid"  },  "split\_merge\_in\_front\_present": false  } | {  "width": 3,  "curvature": 1/496.7,  "allowed\_speed": 130,  "lane\_boundary\_left": {  "lb\_color": "white",  "lb\_width": 0.3,  "lb\_type": "road\_boundary"  },  "lane\_boundary\_right": {  "lb\_color": "white",  "lb\_width": 0.3,  "lb\_type": "solid"  },  "split\_merge\_in\_front\_present": false  } | {  "width": 2.7,  "curvature": 1/503.25,  "allowed\_speed": 0,  "lane\_type": "shoulder"  "lane\_boundary\_left": {  "lb\_color": "white",  "lb\_width": 0.4,  "lb\_type": "solid"  },  "lane\_boundary\_right": {  "lb\_color": "not\_applicable",  "lb\_width": null,  "lb\_type": "road\_boundary"  },  "split\_merge\_in\_front\_present": false  } | guard\_rail | 1000 |
| 3 | dummy\_TE\_3 | dummy\_SE\_3 | motorway | FALSE | physical\_barrier | 2 | { "width": 3, "curvature": 1/1500, "allowed\_speed": 130, "lane\_boundary\_left": { "lb\_color": "white", "lb\_width": 0.3, "lb\_type": "dashed" }, "lane\_boundary\_right": { "lb\_color": "white", "lb\_width": 0.4, "lb\_type": "solid" }, "split\_merge\_in\_front\_present": false } | { "width": 3, "curvature": 1/1496.7, "allowed\_speed": 130, "lane\_boundary\_left": { "lb\_color": "white", "lb\_width": 0.3, "lb\_type": "road\_boundary" }, "lane\_boundary\_right": { "lb\_color": "white", "lb\_width": 0.3, "lb\_type": "solid" }, "split\_merge\_in\_front\_present": false } | { "width": 2.7, "curvature": 1/1503.25, "allowed\_speed": 0, "lane\_type": "shoulder" "lane\_boundary\_left": { "lb\_color": "white", "lb\_width": 0.4, "lb\_type": "solid" }, "lane\_boundary\_right": { "lb\_color": "not\_applicable", "lb\_width": null, "lb\_type": "road\_boundary" }, "split\_merge\_in\_front\_present": false } | other | 1000 |