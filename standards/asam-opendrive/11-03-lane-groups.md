# ASAM Opendrive v1.9.0 — 11.3 Lane groups

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_03_lane_groups.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.3 Lane groups

For easier navigation through an ASAM OpenDRIVE road description, the lanes within a lane section are grouped into left, center, and right lanes.

![img](../_images/11_lanes/lanes_group.png)

Figure 62. Lane grouping with left, center, right

[Figure 62](#fig-e2e5e357-03f8-46bc-a5c1-ab2aa53f0eaa) shows the lane grouping.
Within these groups, the lanes are described by `<lane>` elements.
Because lane numbers descend in a negative t-direction and ascend in a positive t-direction, applications can derive the direction of a lane from the lane id given in the @id attribute of a `<lane>` element, unless the lane is bi-directional (specified by @direction=both).

**Elements in UML model**

**`<left>` element**

In ASAM OpenDRIVE, left lane groups are represented by the `<left>` element within the `<laneSection>` element.

```
UML class: t_road_lanes_laneSection_left
XML tag:   <left> (Multiplicity: 0..1)
```

Contains all lanes left to the center lane.

**`<lane>` element**

In ASAM OpenDRIVE, lanes in the left lane group are represented by `<lane>` elements within the `<left>` element.

```
UML class: t_road_lanes_laneSection_left_lane
XML tag:   <lane> (Multiplicity: 1..*)
```

Left lanes numbered with positive IDs in ascending order from center lane to left border.

Table 34. Attributes of the <lane> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `advisory` | [e\_laneAdvisory](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_2F2EBD73_C3AB_4121_921A_DB492066027C) | optional | 1.8.0 | If true, lane can be used also by a neighboring lane. Advisory lane has priority, for example a bike lane, that can also be used by cars. If not specified, default value is none. |
| `direction` | [e\_lane\_direction](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_BDEEA32B_3F22_4f2c_A327_04437D41CC3D) | optional | 1.8.0 | If not specified, direction is determined by the combination of `<left>` or `<right>` lane grouping and the values LHT or RHT of the @rule attribute of a road. The standard direction can be overwritten with this attribute. |
| `dynamicLaneDirection` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | 1.8.0 | If true, lane direction can be changed dynamically by the scenario during the simulation. If not specified, default boolean value is false. |
| `dynamicLaneType` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | 1.8.0 | If true, lane type can be changed dynamically by the scenario during the simulation. Typical example is a stop lane that can be changed by VMS boards to a driving lane. If not specified, default boolean value is false. |
| `id` | positiveInteger | required |  | ID of the lane |
| `level` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional |  | "true" = keep lane on level, that is, do not apply superelevation;  "false" = apply superelevation to this lane (default, also used if attribute level is missing) |
| `roadWorks` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | 1.8.0 | If true, lane is under construction and access as well as the ability to drive on it are restricted. |
| `type` | [e\_laneType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_9692E2F3_4895_4ce6_A84E_FB1297B0B58E) | required |  | Type of the lane |

**`<center>` element**

In ASAM OpenDRIVE, center lane groups are represented by the `<center>` element within the `<laneSection>` element.

```
UML class: t_road_lanes_laneSection_center
XML tag:   <center> (Multiplicity: 1)
```

Contains the center lane, which must be defined for all roads.

**`<lane>` element**

In ASAM OpenDRIVE, lanes in the center lane group are represented by `<lane>` elements within the `<center>` element.

```
UML class: t_road_lanes_laneSection_center_lane
XML tag:   <lane> (Multiplicity: 1)
```

Center lane element with ID zero.
Has no width attribute.
Mainly used for road markings.

Table 35. Attributes of the <lane> element


| Name | Type | Use | Deprecated | Description |
| --- | --- | --- | --- | --- |
| `id` | integer | required |  | ID of the lane |
| `level` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | 1.8.0 |  |
| `type` | [e\_laneType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_9692E2F3_4895_4ce6_A84E_FB1297B0B58E) | optional | 1.8.0 |  |

**`<right>` element**

In ASAM OpenDRIVE, right lane groups are represented by the `<right>` element within the `<laneSection>` element.

```
UML class: t_road_lanes_laneSection_right
XML tag:   <right> (Multiplicity: 0..1)
```

Contains all lanes right to the center lane.

**`<lane>` element**

In ASAM OpenDRIVE, lanes in the right lane group are represented by `<lane>` elements within the `<right>` element.

```
UML class: t_road_lanes_laneSection_right_lane
XML tag:   <lane> (Multiplicity: 1..*)
```

Right lanes numbered with negative IDs in descending order from center lane to right border.

Table 36. Attributes of the <lane> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `advisory` | [e\_laneAdvisory](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_2F2EBD73_C3AB_4121_921A_DB492066027C) | optional | 1.8.0 | If true, lane can be used also by a neighboring lane. Advisory lane has priority, for example a bike lane, that can also be used by cars. If not specified, default value is none. |
| `direction` | [e\_lane\_direction](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_BDEEA32B_3F22_4f2c_A327_04437D41CC3D) | optional | 1.8.0 | If not specified, direction is determined by the combination of `<left>` or `<right>` lane grouping and the values LHT or RHT of the @rule attribute of a road. The standard direction can be overwritten with this attribute. |
| `dynamicLaneDirection` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | 1.8.0 | If true, lane direction can be changed dynamically by the scenario during the simulation. If not specified, default boolean value is false. |
| `dynamicLaneType` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | 1.8.0 | If true, lane type can be changed dynamically by the scenario during the simulation. Typical example is a stop lane that can be changed by VMS boards to a driving lane. If not specified, default boolean value is false. |
| `id` | negativeInteger | required |  | ID of the lane |
| `level` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional |  | "true" = keep lane on level, that is, do not apply superelevation;  "false" = apply superelevation to this lane (default, also used if attribute level is missing) |
| `roadWorks` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | 1.8.0 | If true, lane is under construction and access as well as the ability to drive on it are restricted. |
| `type` | [e\_laneType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_9692E2F3_4895_4ce6_A84E_FB1297B0B58E) | required |  | Type of the lane |

**Rules**

The following rules apply to lane grouping:

* [asam.net:xodr:1.4.0:road.lane.lanes\_numbered\_correctly](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-lanes-numbered-correctly): Lanes with positive ID run on the left side of the center lane, while lanes with negative ID run on the right side of the center lane.

* [asam.net:xodr:1.9.0:road.lane.lane\_section\_drivable](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-lane-section-drivable): In order to be drivable, each lane section should contain at least one `<right>` or `<left>` element that is valid for the whole length of that section.

* [asam.net:xodr:1.4.0:road.lane.center\_elem\_definition](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-center-elem-definition): One `<center>` element shall be defined for each s-coordinate.

* [asam.net:xodr:1.4.0:road.lane.lane\_listing](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-lane-listing): For better orientation, lanes should be listed from left to right, that is with descending ID.

* [asam.net:xodr:1.4.0:road.lane.lane\_reverse\_left\_right](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-lane-reverse-left-right): @direction="reverse" shall not be used to change from right-hand traffic to left-hand traffic and vice versa.

**Related topics**

* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 11.4, "Lane sections"](11_04_lane_sections.html#top-e2c7cf98-db06-4a27-972a-0d165f87a867)

## 11.3.1 Driving direction

In ASAM OpenDRIVE, the driving direction is specified by a combination of different elements and attributes.
For a road with the @rule="RHT" attribute, the default driving direction would be in positive direction of the road reference line for all `<right>` element lanes with negative @id attribute and against the road reference line for lanes in the `<left>` element with positive @id attribute.
If the road has the @rule="LHT" attribute, the default driving direction would be in positive direction of the road reference line for all `<left>` element lanes with positive @id attribute and against the road reference line for all `<right>` element lanes with negative @id attribute.
This can be influenced with the @direction attribute individually for each lane.
If the @direction attribute is not specified or has a value of @direction="standard", the default driving direction is not changed.
The @direction="reversed" attribute reverses the default driving direction.
The @direction="both" attribute replaces the deprecated lane @type="bidirectional" and allows both driving directions.

In addition, this can be changed during the simulation if @dynamicLaneDirection="true" attribute is set, for example by a VMS board.

**Related topics**

* [Section 10.1, "Introduction to roads"](../10_roads/10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)
* [Section 14.7, "Signal boards"](../14_signals/14_07_signal_boards.html#top-33be999b-2d06-4c74-a285-e662e0a0bb55)