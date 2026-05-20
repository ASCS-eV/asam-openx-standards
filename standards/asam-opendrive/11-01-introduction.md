# ASAM Opendrive v1.9.0 — 11.1 Introduction to lanes

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_01_introduction.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.1 Introduction to lanes

In ASAM OpenDRIVE, lanes are an essential part of all roads.
Lanes are assigned to a lane layer, which is attached to the road reference line of the road.
In each lane layer, lanes are defined from inside to outside.
A minimum road definition requires a lane layer with a center lane and an additional lane with a defined width.
The number of lanes per road and layer is not limited.

The center lane has no width and serves as reference for lane numbering.
Furthermore, it contains the innermost road markings.
The center lane itself has the lane id 0.
The numbering of the other lanes in each layer starts at the center lane: Lane numbers descend to the right, meaning a negative t-direction, and ascend to the left, meaning a positive t-direction.

Individual lanes can be marked as inaccessible due to roadworks with the @roadworks attribute.
Access to and driving on a lane where @roadworks is set to true is restricted for traffic.

![img](../_images/11_lanes/lanes_overview.png)

Figure 57. Center lane for road with lanes of different driving directions

[Figure 57](#fig-305e76a9-2210-4dd7-acfd-bfedb3b95037) shows the center lane for a road with multiple traffic lanes and different driving directions.
In this case, the center lane separates the driving directions, depending on left- and right-hand traffic, specified in Road type.
Because no lane offset is used, the center lane is identical to the road reference line.

![img](../_images/11_lanes/lanes_oneway.png)

Figure 58. Center lane for road with lanes of identical driving direction

[Figure 58](#fig-ec1f8b0b-0f8c-41df-ab9c-f8193b870c11) shows the center lane for a road with lanes that have the same driving direction, meaning a one-way road.

**Elements in UML model**

**`<lanes>` element**

In ASAM OpenDRIVE, lanes are represented by `<lanes>` elements within the `<road>` element.

```
UML class: t_road_lanes
XML tag:   <lanes> (Multiplicity: 1..2)
```

Lanes are an essential part of all roads.
Lanes are attached to the road reference line and are defined from inside to outside.

Lanes contain a series of lane section elements that define the characteristics of the road cross sections with respect to the lanes along the road reference line.

Table 34. Attributes of the <lanes> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `layer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional | Layer the lanes are assigned to (permanent, temporary). |

![img](../_images/uml_class_diagrams/EAID_CD586CD1_8333_46a3_A103_8F63F2BCE9C1.png)

Figure 59. UML class diagram of the Lanes class

[Figure 59](#fig-d9d918ab-493f-456c-b212-78cde856ccf8) shows the UML class diagram of the ASAM OpenDRIVE Lanes class.

**XML example**

```
<lanes>
    <laneSection s="0.0">
        <left>
            <lane id="2" type="border" level="false">
                <link>
                </link>
                <width sOffset="0.0" a="1.0" b="0.0" c="0.0" d="0.0"/>
            </lane>
            <lane id="1" type="driving" level="false">
                <link>
                </link>
                <width sOffset="0.0" a="4.0" b="0.0" c="0.0" d="0.0"/>
            </lane>
        </left>
        <center>
            <lane id="0">
                ...
            </lane>
        </center>
        <right>
            <lane id="-1" type="driving" level="false">
                <link>
                </link>
                <width sOffset="0.0" a="4.0" b="0.0" c="0.0" d="0.0"/>
            </lane>
            <lane id="-2" type="border" level="false">
                <link>
                </link>
                <width sOffset="0.0" a="1.0" b="0.0" c="0.0" d="0.0"/>
            </lane>
        </right>
    </laneSection>
</lanes>
```

**Rules**

The following rules apply to the use of lanes:

* [asam.net:xodr:1.9.0:road.lane.center\_lane](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-center-lane): Each road shall have at least one lane layer with a center lane.

* Lane layers may have as many lanes as needed.

* [asam.net:xodr:1.4.0:road.lane.center\_lane\_no\_width](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-center-lane-no-width): The center lane shall have no width, meaning that the `<width>` element shall not be used for the center lane.

* [asam.net:xodr:1.4.0:road.lane.center\_lane\_id](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-center-lane-id): The center lane shall have the lane id 0.

* [asam.net:xodr:1.4.0:road.lane.lane\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-lane-order): Lane numbering shall start with 1 next to the center lane in positive t-direction in ascending order and -1 next to the center lane in negative t-direction in descending order.

* [asam.net:xodr:1.4.0:road.lane.lane\_order\_no\_gaps](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-lane-order-no-gaps): Lane numbering shall be consecutive without any gaps.

* [asam.net:xodr:1.9.0:road.lane.lane\_id\_unique](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-lane-id-unique): Lane numbering shall be unique per lane section and layer.

* There may be bidirectional lanes.
  This is specified using the @direction attribute of the `<lane>` element.

* [asam.net:xodr:1.4.0:road.lane.lane\_sect\_min\_amount](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-lane-sect-min-amount): Each `<lanes>` element shall contain at least one `<laneSection>` element.

* [asam.net:xodr:1.4.0:road.lane.s\_attr\_value](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-s-attr-value): All `<laneSection>` elements shall contain the @s attribute.

* All drivable lanes must be continuous and smooth, with no gaps, and must account for the plan view, profiles, and lane properties during design and implementation.

* [asam.net:xodr:1.9.0:road.lane.lane\_sect\_first](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-lane-sect-first): The first lane section shall be defined with a value of 0.0 for the @s attribute.

|  |  |
| --- | --- |
|  | In older ASAM OpenDRIVE versions a road required at least one lane with a width greater zero. As roads can now be used for junction boundaries and do not need an extra lane, this rule has been removed. |

**Related topics**

* [Section 11.2, "Lane layers"](11_02_lane_layers.html#top-709a1642-11e1-44bb-a26d-1de7478c23e3)
* [Section 11.3, "Lane groups"](11_03_lane_groups.html#top-3c24733f-35b5-43ae-b1da-60920f47ad47)