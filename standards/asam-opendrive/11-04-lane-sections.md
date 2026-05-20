# ASAM OpenDRIVE® v1.9.0 — 11.4 Lane sections

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_04_lane_sections.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.4 Lane sections

Lanes may be split into multiple lane sections.
Each lane section contains a fixed number of lanes.
The permanent lane layer needs to be specified for the complete length of the road without gaps.
Lane sections on the temporary layer may specify an explicit length.
A lane section with an explicit length may end before the end of the road or the beginning of the next lane section.

![img](../_images/11_lanes/lane_section_1.png)

Figure 63. Road section with lane sections

[Figure 63](#fig-459a1b0f-94d0-4712-8f23-45845d5f4998) shows that every time the number of lanes changes, a new lane section is required.
Lane sections are defined in ascending order along the road reference line.

![img](../_images/11_lanes/lane_section_2.png)

Figure 64. Lane sections defined separately for both sides of the road

[Figure 64](#fig-fbf7c6d2-a397-4833-be55-96347c71b5a7) shows how lane sections for complex roads may be defined for one side of the road only, using the @singleSide attribute.

**Elements in UML model**

**`<laneSection>` element**

In ASAM OpenDRIVE®, lane sections are represented by `<laneSection>` elements within the `<lanes>` element.

```
UML class: t_road_lanes_laneSection
XML tag:   <laneSection> (Multiplicity: 1..*)
```

A lane section splits a road into multiple parts whenever the number of lanes or their function changes.

The distance between two succeeding lane sections shall not be zero.

For easier navigation through an ASAM OpenDRIVE® road description, the lanes within a lane section are grouped into left, center, and right lanes.
Each lane section shall contain one `<center>` element and at least one `<right>` or `<left>` element.

Table 37. Attributes of the <laneSection> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `length` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional |  | Length of the lane section |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position |
| `singleSide` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional |  | Lane section element is valid for one side only (left, center, or right), depending on the child elements. |

For the child elements of the `<laneSection>` element refer to [Lane groups](11_03_lane_groups.html#top-3c24733f-35b5-43ae-b1da-60920f47ad47).

**Rules**

The following rules apply to lane sections:

* [asam.net:xodr:1.4.0:road.lane\_section.lane\_sect\_req](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-section-lane-sect-req): Each road shall have at least one lane section.

* [asam.net:xodr:1.4.0:road.lane\_section.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-section-elem-asc-order): `<laneSection>` elements shall be defined in ascending order according to the s-coordinate.

* [asam.net:xodr:1.9.0:road.lane.layer.length\_only\_temporary](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-layer-length-only-temporary): Lanes in the permanent lane layer shall not use the attribute @length.

* [asam.net:xodr:1.4.0:road.lane\_section.valid\_length](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-section-valid-length): The length of lane sections shall be greater than zero.

* [asam.net:xodr:1.9.0:road.lane.center\_lane\_singular](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-center-lane-singular): There shall always be exactly one center lane at each s-position.

* [asam.net:xodr:1.9.0:road.lane\_section.lane\_long\_zero\_width](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-section-lane-long-zero-width): Using lanes with a width of 0 for long distances should be avoided.

* [asam.net:xodr:1.4.0:road.lane\_section.lanesec\_usage\_lane\_num](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-section-lanesec-usage-lane-num): A new lane section shall be defined each time the number of lanes change.

* A lane section without @length shall remain valid until either a new lane section is defined or the road ends.
* A lane section with @length shall remain valid until @length is reached.

* [asam.net:xodr:1.9.0:road.lane\_section.lanesec\_length\_limit\_road](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-section-lanesec-length-limit-road): A lane section with @length shall not extend beyond the end of the road.

* The properties of lanes inside a lane section may be changed as often as needed.
* Lane sections may be defined for one side of the road only using the @singleSide attribute.

* [asam.net:xodr:1.9.0:road.lane\_section.new\_lanesec\_link\_temp\_to\_perm](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-section-new-lanesec-link-temp-to-perm): A new lane section on the permanent lane layer shall be defined each time lanes on the permanent layer are linked to lanes on the temporary layer.

**Related topics**

* [Section 9.2, "Road reference line"](../09_geometries/09_02_road_reference_line.html#top-9cb15835-ff9e-4b51-9bc8-730a3695fde9)
* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 11.3, "Lane groups"](11_03_lane_groups.html#top-3c24733f-35b5-43ae-b1da-60920f47ad47)
* [Section 11.6, "Lane linkage"](11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd)