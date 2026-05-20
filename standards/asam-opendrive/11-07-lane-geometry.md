# ASAM Opendrive v1.9.0 — 11.7 Lane geometry

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_07_lane_geometry.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.7 Lane geometry

Lane geometry are properties that describe the shape of lanes.
Lane geometries are defined per lane section but may change within that section.

![img](../_images/11_lanes/fig_uml_class_lanes_lane_properties.png)

Figure 70. UML model for lane geometry in the Lanes class

[Figure 70](#fig-24654426-8984-4a53-8627-3effc2b56faf) shows the UML model for lane geometry in the ASAM OpenDRIVE Lanes class.
Examples of lane geometry are lane width, lane border, and lane height.

**Rules**

The following rules apply to lane geometry:

* Lane geometries shall be defined relative to the start of the corresponding lane section.
* A specific lane geometry shall remain valid until another lane geometry of that type is defined or the lane section ends.

* [asam.net:xodr:1.4.0:road.lane.lane\_properties.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-lane-properties-elem-asc-order): Lane geometries of identical types shall be defined in ascending order.

## 11.7.1 Lane width

![img](../_images/11_lanes/lane_section_3.png)

Figure 71. Change of lane width per lane section

[Figure 71](#fig-e2eb6a19-8cf4-47ac-96ac-c124f42695b0) shows the change in lane width in positive s-direction, starting at different offset positions.

**Elements in UML model**

**`<width>` element**

In ASAM OpenDRIVE, lane width is represented by the `<width>` element within the `<lane>` element.

```
UML class: t_road_lanes_laneSection_lr_lane_width
XML tag:   <width> (Multiplicity: 1..*)
```

Lane widths widen or narrow lanes along the t-coordinate within lane sections.

Lane width and lane border elements are mutually exclusive within the same lane group.
If both width and lane border elements are present for a lane section in the ASAM OpenDRIVE file, the application must use the information from the `<width>` elements.

Table 41. Attributes of the <width> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `a` | double | required | m | Coefficient a, width at @s (ds=0) |
| `b` | double | required | 1 | Coefficient b |
| `c` | double | required | 1/m | Coefficient c |
| `d` | double | required | 1/m² | Coefficient d |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position of the `<width>` element, relative to the position of the preceding `<laneSection>` element |

**XML example**

* [Ex\_Lane-Width.xodr](../_attachments/examples/Ex_Lane-Width/Ex_Lane-Width.xodr)

**Calculation**

The width at a given point is calculated with the following polynomial function of the third order:

`width (ds) = a + b*ds + c*ds² + d*ds³`

where

|  |  |
| --- | --- |
| `width` | is the width at a given position |
| `a, b, c, d` | are the coefficients |
| `ds` | is the distance along the road reference line between the start of a new lane width element and the given position |

`ds` restarts at zero for each element.
The absolute position of a width value is calculated as follows:

`s = ssection + offsetstart + ds`

where

|  |  |
| --- | --- |
| `s` | is the absolute position in the road reference line coordinate system |
| `sSection` | is the start position of the preceding lane section element in the track coordinate system |
| `offsetStart` | is the offset of the element relative to the preceding lane section |

**Rules**

The following rules apply to lane width:

tag::Rules\_lane\_width[]

* [asam.net:xodr:1.7.0:road.lane.width.width\_defined\_whole\_section](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-lane-width-width-defined-whole-section): The width of the lane shall be defined for the full length of the lane section. This means that there must be a `<width>` element for @s="0".

* [asam.net:xodr:1.4.0:road.lane.center\_lane\_no\_width](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-center-lane-no-width): The center lane shall have no width, meaning that the `<width>` element shall not be used for the center lane.

* The width of a lane shall remain valid until a new `<width>` element is defined or the lane section ends.
* A new `<width>` element shall be defined when the variables of the polynomial function change.

* [asam.net:xodr:1.9.0:road.lane.width.no\_width\_with\_border](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-width-no-width-with-border): `<width>` elements shall not be used together with `<border>` elements in the same lane group.

* [asam.net:xodr:1.4.0:road.lane.width.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-width-elem-asc-order): `<width>` elements shall be defined in ascending order according to the s-coordinate.

* [asam.net:xodr:1.4.0:road.lane.width.lane\_width\_validity](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-width-lane-width-validity): Width (ds) shall be greater than or equal to zero.

**Related topics**

* [Section 10.5.1, "Superelevation"](../10_roads/10_05_elevation.html#sec-4abf7baf-fb2f-4263-8133-ad0f64f0feac)
* [Section 10.5.1, "Shape definition"](../10_roads/10_05_elevation.html#sec-66ac2b58-dc5e-4538-884d-204406ea53f2)
* [Section 11.3, "Lane groups"](11_03_lane_groups.html#top-3c24733f-35b5-43ae-b1da-60920f47ad47)
* [Section 11.4, "Lane sections"](11_04_lane_sections.html#top-e2c7cf98-db06-4a27-972a-0d165f87a867)

## 11.7.2 Lane borders

![img](../_images/11_lanes/lane_border.png)

Figure 72. Lane with varying border shape

[Figure 72](#fig-43e509c3-ff11-4aa4-ac98-c8bc58a8e34f) shows the convention for a lane with varying border shape over a given range.

**Elements in UML model**

**`<border>` element**

In ASAM OpenDRIVE, lane borders are represented by the `<border>` element within the `<lane>` element.

```
UML class: t_road_lanes_laneSection_lr_lane_border
XML tag:   <border> (Multiplicity: 1..*)
```

Lane borders set the width of lanes.
Lane borders describe the outer limits of lanes, independent of the parameters of their inner borders.
In this case, inner lanes are defined as lanes which have the same sign for their ID as the lane currently defined, but with a smaller absolute value for their ID.

Especially when road data is derived from automatic measurements, this type of definition is easier than specifying the lane width because it avoids creating many lane sections.

Lane width and lane border elements are mutually exclusive within the same lane group.
If both width and lane border elements are present for a lane section in the ASAM OpenDRIVE file, the application shall use the information from the `<width>` elements.

Table 42. Attributes of the <border> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `a` | double | required | m | Coefficient a, border position at @s (ds=0) |
| `b` | double | required | 1 | Coefficient b |
| `c` | double | required | 1/m | Coefficient c |
| `d` | double | required | 1/m² | Coefficient d |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position of the `<border>` element , relative to the position of the preceding `<laneSection>` element |

**XML example**

* [Ex\_Lane-Border.xodr](../_attachments/examples/Ex_Lane-Border/Ex_Lane-Border.xodr)

**Calculation**

The border position at a given point is calculated with the following polynomial function of the third order:

`tborder (ds) = a + b*ds + c*ds² + d*ds³`

where

|  |  |
| --- | --- |
| `tborder` | is the t-position of the border at a given ds-position |
| `a, b, c, d` | are the coefficients |
| `ds` | is the distance along the road reference line between the start of the element and the given position |

`ds` restarts at zero for each element.
The absolute position of a border offset value is calculated by

`s = sSection + offsetstart+ ds`

where

|  |  |
| --- | --- |
| `s` | is the absolute position in the road reference line coordinate system |
| `sSection` | is the start position of the preceding lane section element in the track coordinate system |
| `offsetStart` | is the offset of the element relative to the preceding lane section element |

**Rules**

The following rules apply to lane borders:

* [asam.net:xodr:1.4.0:road.lane.border.exclusive\_width\_border](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-border-exclusive-width-border): `<border>` elements shall not be used together with `<width>` elements in the same lane group.

* [asam.net:xodr:1.4.0:road.lane.border.exclusive\_offset\_border](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-border-exclusive-offset-border): `<border>` elements shall not be used together with `<laneOffset>`.

* A new `<border>` element shall be defined when the variables of the polynomial function change.

* [asam.net:xodr:1.4.0:road.lane.border.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-border-elem-asc-order): `<border>` elements shall be defined in ascending order according to the s-coordinate.

* [asam.net:xodr:1.4.0:road.lane.border.overlap\_with\_inner\_lanes](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-border-overlap-with-inner-lanes): Lane borders shall not intersect inner lanes.

**Related topics**

* [Section 11.3, "Lane groups"](11_03_lane_groups.html#top-3c24733f-35b5-43ae-b1da-60920f47ad47)
* [Section 11.4, "Lane sections"](11_04_lane_sections.html#top-e2c7cf98-db06-4a27-972a-0d165f87a867)

## 11.7.3 Lane height

Lane height shall be defined along the h-coordinate.
Lane height may be used to elevate a lane independent from the road elevation.

![img](../_images/11_lanes/lane_height_1.png)

Figure 73. Lane height

[Figure 73](#fig-b3c6653e-058b-426d-8640-795da6c2d318) shows that lane height is used to implement small-scale elevation, such as raising pedestrian walkways.
Lane height is specified as offset from the road (including elevation, superelevation, shape, cross section surface) in h-direction.

**Elements in UML model**

**`<height>` element**

In ASAM OpenDRIVE, lane height is represented by the `<height>` element within the `<lane>` element.

```
UML class: t_road_lanes_laneSection_lr_lane_height
XML tag:   <height> (Multiplicity: 0..*)
```

Lane heights elevate lanes along the h-coordinate within a lane section independent from the road elevation.

Lane height is used to implement small-scale elevation such as raising pedestrian walkways.
Lane height is specified as offset from the road (including elevation, superelevation, shape, cross section surface) in h-direction.

Table 43. Attributes of the <height> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `inner` | double | required | m | Inner offset from road level |
| `outer` | double | required | m | Outer offset from road level |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position, relative to the position of the preceding `<laneSection>` element |

**XML example**

```
<lane id="-2" type="walking" level="false">
    <link>
        <successor id="-3"/>
    </link>
    <width sOffset="0.0" a="2.0" b="0.0" c="0.0" d="0.0"/>
    <height sOffset="0.0" inner="0.12" outer="0.12"/>
</lane>
```

**Rules**

The following rules apply to lane height:

* To modify the lane height, for example for curbstones, the `<height>` element shall be used.

* [asam.net:xodr:1.4.0:road.lane.height.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-height-elem-asc-order): `<height>` elements shall be defined in ascending order according to the s-coordinate.

* [asam.net:xodr:1.4.0:road.lane.height.center\_lane\_no\_height](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-height-center-lane-no-height): The center lane shall not be elevated by lane height.

* Lane height shall not be used to define road elevation or superelevation.
* Lane height shall be used for small scale elevation only.

**Related topics**

* [Section 10.5.1, "Road elevation"](../10_roads/10_05_elevation.html#sec-1d876c00-d69e-46d9-bbcd-709ab48f14b1)
* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 11.3, "Lane groups"](11_03_lane_groups.html#top-3c24733f-35b5-43ae-b1da-60920f47ad47)

## 11.7.4 Excluding lanes from lateral profile

Single lanes may be excluded from lateral profile to cover use cases like roads with curbstones, borders, or sidewalks.

![img](../_images/11_lanes/lane_height_2.png)

Figure 74. Lanes excluded from road elevation

[Figure 74](#fig-3572c8fb-33ca-4f8e-88b9-15352209d4ea) shows the use of the @level attribute, which excludes the outermost lanes of a road from superelevation.

ASAM OpenDRIVE provides the @level attribute for excluding lanes from lateral profile.
When the attribute is set to `true` for a lane, then this lane is excluded from superelevation, road shape definition and cross section surface definitions of the road.
The elevation of the lane stays on the same height as the outer border of the inner connecting lane.
For lanes with @level="true" the projection does not change.
Changes between lane sections are not recommended.

There may be multiple outer lanes with @level="true", for example, for a bike lane followed by a sidewalk.

**Rules**

The following rules apply to excluding lanes from road elevation:

* [asam.net:xodr:1.7.0:road.lane.level\_true\_one\_side](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-lane-level-true-one-side): If a lane has @level="true", then all further outward lanes shall be lanes with @level="true" until the edge of the road is reached.

* There may be multiple outer lanes with @level="true".

**Related topics**

* [Section 10.5.1, "Superelevation"](../10_roads/10_05_elevation.html#sec-4abf7baf-fb2f-4263-8133-ad0f64f0feac)
* [Section 11.8.1, "Lane type"](11_08_lane_properties.html#sec-79c983d6-db57-41ad-85f7-4643c25910dc)