# ASAM OpenDRIVE® v1.9.0 — 11.8 Additional lane properties

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_08_lane_properties.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.8 Additional lane properties

Additional lane properties describe the use or other physical properties of lanes.
Lane properties are defined per lane section but may change within that section.
If a property is not specifically defined for a lane section, applications can apply default properties.

![img](../_images/uml_class_diagrams/EAID_CD586CD1_8333_46a3_A103_8F63F2BCE9C1.png)

Figure 75. UML class diagram of the Lanes class

[Figure 75](#fig-954a4511-24c8-44d7-a385-3ef579556e98) shows the UML class diagram of the ASAM OpenDRIVE® Lanes class.
Example for additional lane properties are lane type, lane speed limit or lane material.

## 11.8.1 Lane type

The lane type is defined per lane.
A lane type defines the main purpose of a lane and its corresponding traffic rules.

The available lane types are:

* `shoulder`: Soft border at the edge of the road.
* `border`: Hard border at the edge of the road.
  It has usually the same height as the drivable lane.
* `driving`: Normal drivable road that is not one of the other types.
* `stop`: Hard shoulder on motorways for emergency stops
* `restricted`: Lane on which cars should not drive. The lane has the same height as drivable lanes.
  Typically, the lane is separated with lines and often contains dotted lines as well.
* `parking`: Lane with parking spaces.
* `median`: Lane that sits between driving lanes that lead in opposite directions.
  It is typically used to separate traffic in towns on large roads.
* `biking`: Lane that is reserved for cyclists.
* `walking`: Lane on which pedestrians can walk.
* `curb`: Curb stones.
  Curb stones have usually a different height than the adjacent drivable lanes.
* `entry`: Lane that is used for sections that are parallel to the main road and merge into the main road.
  It is mainly used for acceleration lanes.
* `exit`: Lane that is used for sections that are parallel to the main road and lead to an exit from the main road.
  It is mainly used for deceleration lanes.
* `onRamp`: Ramp leading to a motorway from rural or urban roads.
* `offRamp`: Ramp leading away from a motorway and onto rural urban roads.
* `connectingRamp`: Ramp that connects two motorways, for example, motorway junctions.
* `slipLane`: Lane on which drivers change roads without driving into the main intersection.
* `none`: Space on the outermost edge of the road and does not have actual content.
  Its only purpose is for applications to register that ASAM OpenDRIVE® is still present in case the (human) driver leaves the road.

|  |  |
| --- | --- |
|  | The lane type `sidewalk` was deprecated, use `walking` instead. The lane type `bidirectional` was deprecated, use the @direction attribute instead. A full list including all deprecated lane types can be found at [e\_laneType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_9692E2F3_4895_4ce6_A84E_FB1297B0B58E). |

The following examples show typical use cases for lane types:

* Motorway, see [Figure 76](#fig-60a46e91-de14-47b0-b5c0-c899f8dfd0e5)
* Rural road, see [Figure 77](#fig-a1a80653-50b4-41a4-ab53-317ffc97204a)
* Urban road, see [Figure 78](#fig-0ddd6e1b-3b70-40cd-84ad-18356b4c1e75)
* Motorway exit and entry, see [Figure 79](#fig-535664ed-61f5-4eab-ac35-29bac123ffdc)
* A motorway connecting to another motorway, see [Figure 80](#fig-cf209a1d-15e8-4810-9605-1781844cde25)

![img](../_images/11_lanes/lane_type_64.png)

Figure 76. Lane types for a motorway

[Figure 76](#fig-60a46e91-de14-47b0-b5c0-c899f8dfd0e5) shows the lane types for a one-directional motorway.
There are three `driving` lanes and a `stop` lane.
The `border` lane is the border to the oncoming lanes.
The outer limits are `shoulder` lanes with a `none` lane indicating the end of the road.

![img](../_images/11_lanes/lane_type_65.png)

Figure 77. Lane types for a rural road

[Figure 77](#fig-a1a80653-50b4-41a4-ab53-317ffc97204a) shows a bi-directional rural road.
Two `driving` lanes are bordered by `shoulder` lanes.
`none` lanes indicate the end of the road.
A `restricted` lane in between the driving lanes is added.
This could be used, for example, for traffic islands.

![img](../_images/11_lanes/lane_type_66.png)

Figure 78. Lane types for an urban road

[Figure 78](#fig-0ddd6e1b-3b70-40cd-84ad-18356b4c1e75) shows the right side of a bi-directional urban road.
The two `driving` lanes in each direction are separated by a `median` lane.
Next to the driving lanes are a `walking` lane, a `biking` lane, and a `shoulder` lane.
The `shoulder` lane is interrupted by a `parking` lane.

![img](../_images/11_lanes/lane_type_67.png)

Figure 79. Lane types for motorway exit and entry

[Figure 79](#fig-535664ed-61f5-4eab-ac35-29bac123ffdc) shows lane types for a typical motorway exit and entry.
There are three `driving` lanes in each direction.
The direction where vehicles leave the motorway have an `exit` lane on their right, flowing in to an `offRamp` lane.
The `offRamp` lane runs parallel to the `driving` lanes at first, then describing a curve.
Vehicles entering the motorway drive on a curvy `onRamp` lane, flowing in to an `onRamp` lane parallel to the `driving` lanes flowing in to a `entry` lane.

![img](../_images/11_lanes/lane_type_68.png)

Figure 80. Lane types for motorway connecting to another motorway

[Figure 80](#fig-cf209a1d-15e8-4810-9605-1781844cde25) shows lane types for a motorway that is connected to another motorway.
There are three `driving` lanes in each direction.
The direction where vehicles leave the motorway have an `exit` lane on their right, flowing in to a `connectingRamp` lane.
The `connectingRamp` lane runs parallel to the `driving` lanes at first, then describing a curve.
Vehicles entering the motorway drive on a curvy `connectingRamp` lane, flowing in to a `connectingRamp` lane parallel to the `driving` lanes flowing in to an `entry` lane.

Lane types are set with the @type attribute of the `<lane>` element.

**Rules**

The following rules apply to lane types:

* The lane type may be changed as often as needed by using a new lane section.

**Related topics**

* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Annex A.4, "e\_laneType"](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_9692E2F3_4895_4ce6_A84E_FB1297B0B58E)

## 11.8.2 Lane material

ASAM OpenDRIVE® provides an element to store information on the material of lanes (apart from ASAM OpenCRG), meaning their surface, friction properties, and roughness.
If no material is defined, applications can apply default values.

**Elements in UML model**

**`<material>` element**

In ASAM OpenDRIVE®, lane material is represented by the `<material>` element within the `<lane>` element.

```
UML class: t_road_lanes_laneSection_lr_lane_material
XML tag:   <material> (Multiplicity: 0..*)
```

Stores information about the material of lanes.
Each element is valid until a new element is defined.
If multiple elements are defined, they must be listed in ascending order.

Table 44. Attributes of the <material> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `friction` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required |  | Friction coefficient |
| `roughness` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional |  | Roughness, for example, for sound and motion systems |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position, relative to the position of the preceding `<laneSection>` element |
| `surface` | string | optional |  | Surface material code, depending on application |

**Rules**

The following rules apply to lane material:

* [asam.net:xodr:1.4.0:road.lane.material.center\_lane\_no\_material](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-material-center-lane-no-material): The center lane shall have no material elements.

* The material elements of a lane shall remain valid until another material element starts or the lane section ends.

* [asam.net:xodr:1.4.0:road.lane.material.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-material-elem-asc-order): `<material>` elements shall be defined in ascending order according to the s-coordinate

**Related topics**

* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 11.3, "Lane groups"](11_03_lane_groups.html#top-3c24733f-35b5-43ae-b1da-60920f47ad47)
* [Section 11.4, "Lane sections"](11_04_lane_sections.html#top-e2c7cf98-db06-4a27-972a-0d165f87a867)

## 11.8.3 Lane speed limit

The maximum speed allowed on a lane may be defined. Lane speed limits override road speed limits.

![img](../_images/11_lanes/lane_speed_limit.png)

Figure 81. Lane-specific speed limits

[Figure 81](#fig-1fa47d97-5d89-4b29-8c89-ad2e6d407c08) shows how a speed limit is defined for single lanes.
The lanes `1` and `-1` have a speed limit of 80 km/h, while the lane `2` has a speed limit of 60 km/h.

**Elements in UML model**

**`<speed>` element**

In ASAM OpenDRIVE®, lane speed is represented by the `<speed>` element within the `<lane>` element.

```
UML class: t_road_lanes_laneSection_lr_lane_speed
XML tag:   <speed> (Multiplicity: 0..*)
```

Defines the maximum allowed speed on a given lane.
Each element is valid in direction of the increasing s-coordinate until a new element is defined.

Table 45. Attributes of the <speed> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `max` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required |  | Maximum allowed speed. If the attribute unit is not specified, m/s is used as default. |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position, relative to the position of the preceding `<laneSection>` element |
| `unit` | [e\_unitSpeed](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_491DC05E_01C6_49b3_83BE_A06DD81F9C35) | optional |  | Unit of the attribute max |

**XML example**

```
<lane id="-1" type="driving" level="false">
    <link>
        <successor id="-1"/>
    </link>
    <width sOffset="0.0" a="3.5" b="0.0" c="0.0" d="0.0"/>
    <speed sOffset="0.0" max="80.0" unit="km/h"/>
</lane>
```

**Rules**

The following rules apply to lane speed limits:

* [asam.net:xodr:1.4.0:road.lane.speed.center\_lane\_no\_spd\_lmt](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-speed-center-lane-no-spd-lmt): The center lane shall have no speed limit.

* The speed limit of a lane shall remain valid until another speed limit is defined or the lane section ends.

* [asam.net:xodr:1.4.0:road.lane.speed.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-speed-elem-asc-order): `<speed>` elements shall be defined in ascending order according to the s-coordinate.

* Speed limits derived from signals shall always have preference.

**Related topics**

* [Section 10.4.1, "Speed limits for road types"](../10_roads/10_04_road_type.html#sec-33dc6899-854e-4533-a3d9-76e9e1518ee7)
* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 14.1, "Introduction to signals"](../14_signals/14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)

## 11.8.4 Lane access

Lanes can be restricted to specific road users, such as trucks or buses.
Such restrictions may be defined in ASAM OpenDRIVE® in addition to restrictions described by signals.

![img](../_images/11_lanes/lane_access.png)

Figure 82. Lane access, bus lane

[Figure 82](#fig-4fa28ce3-f04f-4067-a6c6-3767d0687511) shows that the lane `2` is restricted to buses.

**Elements in UML model**

**`<access>` element**

In ASAM OpenDRIVE®, lane access is represented by the `<access>` element within the `<lane>` element.

```
UML class: t_road_lanes_laneSection_lr_lane_access
XML tag:   <access> (Multiplicity: 0..*)
```

Defines access restrictions for certain types of road users.

Each element is valid in direction of the increasing s coordinate until a new element is defined.
If multiple elements are defined, they shall be listed in ascending order.

Table 46. Attributes of the <access> element


| Name | Type | Use | Unit | Deprecated | Description |
| --- | --- | --- | --- | --- | --- |
| `restriction` | [e\_accessRestrictionType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_73EEA8EB_16E9_45ac_ADFF_97F4D36EE967) | optional |  | 1.8.0 | Identifier of the participant to whom the restriction applies |
| `rule` | [e\_road\_lanes\_laneSection\_lr\_lane\_access\_rule](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_79D165EB_5E05_4444_A0B0_95AC1EDB819E) | optional |  |  | Specifies whether the participant given in the attribute @restriction is allowed or denied access to the given lane |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m |  | s-coordinate of start position, relative to the position of the preceding `<laneSection>` element |

**`<restriction>` element**

In ASAM OpenDRIVE®, restrictions are represented by the `<restriction>` element within the `<access>` element.

```
UML class:  t_road_lanes_laneSection_lr_lane_access_restriction
XML tag:    <restriction> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Defines access restrictions for certain types of road users.

Each restriction element defines one type that is either allowed or denied according to the parent access element.

Table 47. Attributes of the <restriction> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `type` | [e\_accessRestrictionType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_73EEA8EB_16E9_45ac_ADFF_97F4D36EE967) | required | 1.8.0 | Identifier of the participant to whom the restriction applies |

**XML example**

```
<lane id="2" type="driving" level="false">
    <link>
        <successor id="2"/>
    </link>
    <width sOffset="0.0" a="2.0" b="0.0" c="0.0" d="0.0"/>
    <access sOffset="0.0" rule="allow">
        <restriction type="bus" />
    </access>
    <access sOffset="50.0" rule="allow">
        <restriction type="bicycle" />
        <restriction type="bus" />
    </access>
</lane>
```

**Rules**

The following rules apply to lane access rules:

* [asam.net:xodr:1.4.0:road.lane.access.center\_lane\_no\_acc\_rule](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-access-center-lane-no-acc-rule): The center lane shall have no access rules.

* The access rules of a lane shall remain valid until another access rule is defined or the lane section ends.

* [asam.net:xodr:1.4.0:road.lane.access.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-access-elem-asc-order): `<access>` elements shall be defined in ascending order according to the s-coordinate.

* If no `<access>` element is present within a lane element, then there are no restrictions.
* If a deny value is present in the @rule attribute, all other vehicles are still allowed.
* If an allow value is present in the @rule attribute, all other vehicles are banned.

* [asam.net:xodr:1.7.0:road.lane.access.no\_mix\_of\_deny\_or\_allow](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-lane-access-no-mix-of-deny-or-allow): At a given s-position, either only deny or only allow values shall be given.

* For a new s-position, all restrictions must be defined again, even if only a subset changes.
* The @rule="deny" with `<restriction type="none" />` is used to revert all previous restrictions.

|  |  |
| --- | --- |
|  | In previous versions of ASAM OpenDRIVE® each individual restriction was specified as one `<access>` element. This was problematic since it was unclear at what distance between two @sOffset attributes the entries would be considered as one access rule. Therefore, all applied restrictions are now a subset of one access element. |

**Related topics**

* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 11.4, "Lane sections"](11_04_lane_sections.html#top-e2c7cf98-db06-4a27-972a-0d165f87a867)