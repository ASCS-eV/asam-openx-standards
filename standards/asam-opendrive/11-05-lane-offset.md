# ASAM OpenDRIVE® v1.9.0 — 11.5 Lane offset

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_05_lane_offset.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.5 Lane offset

A lane offset may be used to shift the center lane away from the road reference line.
This makes it easier to model local lateral shifts of lanes on roads, for example for left turn lanes.

A combination of lane offset and shape definition can lead to inconsistencies depending on the interpolation used for the lane offset.
Because linear interpolation is used for the road shape along the road reference line, linear interpolation should also be used for the offset definition to enable consistent combined use of both definitions.

![img](../_images/11_lanes/lanes_offset.png)

Figure 65. Lane offset

[Figure 65](#fig-7558b905-679d-4fb9-affa-3b3b72025a18) shows the offset of the center lane away from the road reference line.

|  |  |
| --- | --- |
|  | Lane layers are independent. If both the permanent and the temporary lane layer contain lanes, each require their own respective lane offset. The lane offset of the temporary lane layer does not need to be identical to that of the permanent lane layer. |

**Elements in UML model**

**`<laneOffset>` element**

In ASAM OpenDRIVE®, a lane offset is represented by a `<laneOffset>` element within the `<lanes>` element.

```
UML class: t_road_lanes_laneOffset
XML tag:   <laneOffset> (Multiplicity: 0..*)
```

Lane offsets shift the center lane away from the road reference line.

Table 38. Attributes of the <laneOffset> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `a` | double | required | m | Coefficient a, offset at @s (ds=0) |
| `b` | double | required | 1 | Coefficient b |
| `c` | double | required | 1/m | Coefficient c |
| `d` | double | required | 1/m² | Coefficient d |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position |

**XML example**

```
<lanes>
     <laneOffset s="25.0" a="0.0" b="0.0" c="3.9e-03" d="-5.2e-05"/>
     <laneOffset s="75.0" a="3.25" b="0.0" c="0.0" d="0.0"/>
     …
</lanes>
```

* [Ex\_Simple-LaneOffset.xodr](../_attachments/examples/Ex_Simple-LaneOffset/Ex_Simple-LaneOffset.xodr)

**Calculation**

The offset at a given point is calculated with the following polynomial function of the third order:

`offset (ds) = a + b*ds + c*ds² + d*ds³`

where

|  |  |
| --- | --- |
| `offset` | is the lateral offset at a given position |
| `a, b, c, d` | are the coefficients |
| `ds` | is the distance along the road reference line between the start of a new lane offset element and the given position |

`ds` restarts at zero for each element.
The absolute position of an offset value is calculated as follows:

`s = sstart + ds`

where

|  |  |
| --- | --- |
| `s` | is the absolute position in the road reference line coordinate system |
| `sstart` | is the start position of the element in the reference line coordinate system |

A new lane offset element is required each time the polynomial function changes.

**Rules**

The following rules apply to lane offsets:

* [asam.net:xodr:1.4.0:road.lanes.lane\_offset.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lanes-lane-offset-elem-asc-order): `<laneOffset>` elements shall be defined in ascending order according to the s-coordinate.

* A new lane offset shall start when the underlying polynomial function changes.

* [asam.net:xodr:1.4.0:road.lanes.lane\_offset.no\_offset\_if\_border\_defined](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lanes-lane-offset-no-offset-if-border-defined): There shall be no `<laneOffset>` if border definitions are present.

**Related topics**

* [Section 10.5.1, "Shape definition"](../10_roads/10_05_elevation.html#sec-66ac2b58-dc5e-4538-884d-204406ea53f2)
* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 11.7.1, "Lane borders"](11_07_lane_geometry.html#sec-1d7eba61-d3d2-440d-b822-55f0af8a1183)