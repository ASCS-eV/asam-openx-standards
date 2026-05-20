# ASAM Opendrive v1.9.0 — 11.9 Lane road markings

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_09_lane_road_markings.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.9 Lane road markings

Lanes on roads can have different lane markings, for example lines of different colors and styles.
ASAM OpenDRIVE provides the `<roadMark>` element for these road markings.  
The road marking information defines the style of the line at the lane’s outer border.
For left lanes, this is the left border, for right lanes the right one.
The style of the center line that separates left and right lanes is determined by the `<roadMark>` element for the center lane.  
For each lane within a road cross section, multiple `<roadMark>` elements may be defined.
Several attributes may be used to describe the properties of the lane markings, for example @type, @weight, and @width.

There are two ways to specify the type of lane road marking:

* The @type attribute within the `<roadMark>` element makes it possible to enter keywords that are stored in the application. They are used to describe simplified road marking types like solid, broken, or grass.
* The `<type>` element contains further `<line>` elements making it possible to describe the road marking in a more detailed way.

In addition to the road markings defined in this section, ASAM OpenDRIVE also supports the following use cases:

* Road markings that do not represent the line at the outer border of a lane but guide driver and traffic models are defined as signals.
  These may optionally be accompanied by objects, for example in the case of stop lines related to a traffic light.
  See  [Section 14.1, "Introduction to signals"](../14_signals/14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a).
* For road markings that are not mandatory for driver and traffic models, use objects.
  See  [Section 13.2, "Object outline"](../13_objects/13_02_object_outline.html#top-67295042-9707-4ad5-9671-b80cde49bb3a) and  [Section 13.8, "Object markings"](../13_objects/13_08_object_markings.html#top-c25542c0-f80d-4da9-a430-020474b58301).

**Elements in UML model**

**`<roadMark>` element**

In ASAM OpenDRIVE, road markings are represented by `<roadMark>` elements within `<lane>` elements.

```
UML class: t_road_lanes_laneSection_lcr_lane_roadMark
XML tag:   <roadMark> (Multiplicity: 0..*)
```

Defines the style of the line at the outer border of a lane.
The style of the center line that separates left and right lanes is determined by the road mark element for the center lane.

Table 48. Attributes of the <roadMark> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `color` | [e\_roadMarkColor](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_B67AEB84_154B_4c53_979E_7F1EA9751C9E) | required |  | Color of the road marking |
| `height` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m | Height of road marking above the road, i.e. thickness of the road marking |
| `laneChange` | [e\_road\_lanes\_laneSection\_lcr\_lane\_roadMark\_laneChange](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_ACEEA5DD_8A5C_4c13_B5B7_9233272A914D) | optional |  | Allows a lane change in the indicated direction, taking into account that lanes are numbered in ascending order from right to left. If the attribute is missing, “both” is used as default. |
| `material` | string | optional |  | Material of the road marking. Identifiers to be defined by the user, use "standard" as default value. |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position of the `<roadMark>` element, relative to the position of the preceding `<laneSection>` element |
| `type` | [e\_roadMarkType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_4D56116F_9736_432e_844E_64F55EAE99F7) | required |  | Type of the road marking |
| `weight` | [e\_roadMarkWeight](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_239940A3_B976_4a17_BD54_8252EACCC1FD) | optional |  | Weight of the road marking. This attribute is optional if detailed definition is given below. |
| `width` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m | Width of the road marking. This attribute is optional if detailed definition is given by `<line>` element. |

![img](../_images/uml_class_diagrams/EAID_D2700AD5_7968_4435_AD3F_B177C0D1C1AD.png)

Figure 83. UML class diagram of the RoadMark class

[Figure 83](#fig-2640be87-3139-4601-8202-18b81bfd5607) shows the UML class diagram of the ASAM OpenDRIVE RoadMark class.

**Rules**

The following rules apply to road markings:

* [asam.net:xodr:1.9.0:road.lane.road\_mark.only\_outer](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-road-mark-only-outer): `<roadMark>` elements shall only be used to describe the outer lane marking.

* [asam.net:xodr:1.4.0:road.lane.road\_mark.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-road-mark-elem-asc-order): `<roadMark>` elements shall be defined in ascending order according to the s-coordinate.

* [asam.net:xodr:1.9.0:road.lane.road\_mark.position\_outer\_half](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-road-mark-position-outer-half): The center line of the lane marking shall be positioned on the lane’s outer border line in such a way that the outer half of the lane marking is physically placed on the next lane.

* The `<roadMark>` elements of a lane shall remain valid until another `<roadMark>` element starts or the lane section ends.

**Related topics**

* [Section 11.9.1, “Road marking types and lines”](#sec-1540a1cc-8824-480d-a1af-c20ab0bd6e34)
* [Section 11.9.2, “Explicit road marking types and lines”](#sec-108966cb-ecfd-4c0c-b8d9-2e4f95b10210)
* [Section 11.9.3, “Offset in road markings”](#sec-52e18ce8-c575-4918-ba4b-40da1afd60d8)
* [Section 13.2.1, "Object marking on outlines"](../13_objects/13_02_object_outline.html#sec-c25542c0-f80d-4da9-a430-020474b58301)
* [Section 14.1, "Introduction to signals"](../14_signals/14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)

## 11.9.1 Road marking types and lines

Detailed information about road marking types and lines may be defined in `<type>` elements within the `<roadMark>` element.
Each `<type>` element definition contains one or more `<line>` element definitions with additional information about the lines of the road marking.

Road marking information in the `<type>` element is more specific than the information given in the @type attribute within the `<roadMark>` element.

The outline of the road marking is described by the attributes @length and @space:

* @length represents the visible part of the line.
* @space describes the non-visible part.

The position of the road marking in relation to the road reference line may be described by defining the lateral offset.
A line definition is valid for a given length of the lane and is repeated automatically.
The optional @rule attribute for lines defines the traffic rule for passing the lane from the inside.

**Elements in UML model**

**`<type>` element**

In ASAM OpenDRIVE, road marking types are represented by `<type>` elements within `<roadMark>` elements.

```
UML class: t_road_lanes_laneSection_lcr_lane_roadMark_type
XML tag:   <type> (Multiplicity: 0..1)
```

Each type definition shall contain one or more line definitions with additional information about the lines that the road marking is composed of.

Table 49. Attributes of the <type> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `name` | string | required |  | Name of the road marking type. May be chosen freely. |
| `width` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | required | m | Accumulated width of the road marking. In case of several `<line>` elements this @width is the sum of all @width of `<line>` elements and spaces in between, necessary to form the road marking. This attribute supersedes the definition in the `<roadMark>` element. |

**`<line>` element**

In ASAM OpenDRIVE, road marking lines are represented by `<line>` elements within `<type>` elements.

```
UML class: t_road_lanes_laneSection_lcr_lane_roadMark_type_line
XML tag:   <line> (Multiplicity: 1..*)
```

A road marking may consist of one or more elements.
Multiple elements are usually positioned side-by-side.
A line definition is valid for a given length of the lane and will be repeated automatically.

Table 50. Attributes of the <line> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `color` | [e\_roadMarkColor](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_B67AEB84_154B_4c53_979E_7F1EA9751C9E) | optional |  | Line color. If given, this attribute supersedes the definition in the `<roadMark>` element. |
| `length` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Length of the visible part |
| `rule` | [e\_roadMarkRule](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EC1E052F_B2C5_4767_9317_0E54B7A08615) | optional |  | Rule that must be observed when passing the line from inside, for example, from the lane with the lower absolute ID to the lane with the higher absolute ID |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Initial longitudinal offset of the line definition from the start of the road marking definition |
| `space` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Length of the gap between the visible parts |
| `tOffset` | double | required | m | Lateral offset from the lane border.  If `<sway>` element is present, the lateral offset follows the sway. |
| `width` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m | Line width |

**Related topics**

* [Section 11.9.2, “Explicit road marking types and lines”](#sec-108966cb-ecfd-4c0c-b8d9-2e4f95b10210)
* [Section 11.9.3, “Offset in road markings”](#sec-52e18ce8-c575-4918-ba4b-40da1afd60d8)

## 11.9.2 Explicit road marking types and lines

**Elements in UML model**

**`<explicit>` element**

In ASAM OpenDRIVE, irregular road marking types are represented by `<explicit>` elements within `<roadMark>` elements.

```
UML class: t_road_lanes_laneSection_lcr_lane_roadMark_explicit
XML tag:   <explicit> (Multiplicity: 0..1)
```

Irregular road markings that cannot be described by repetitive line patterns may be described by individual road marking elements.
These explicit definitions also contain `<line>` elements for the line definition, however, these lines will not be repeated automatically as in repetitive road marking types.
In ASAM OpenDRIVE, irregular road marking types and lines are represented by `<explicit>` elements within elements.
The line definitions are contained in `<line>` elements within the `<explicit>` element.

The `<explicit>` element should specifically be used for measurement data.

**`<line>` element**

In ASAM OpenDRIVE, irregular road marking lines are represented by `<line>` elements within `<explicit>` elements.

```
UML class: t_road_lanes_laneSection_lcr_lane_roadMark_explicit_line
XML tag:   <line> (Multiplicity: 1..*)
```

Specifies a single line in an explicit road marking definition.

Table 51. Attributes of the <line> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `length` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | required | m | Length of the visible line |
| `rule` | [e\_roadMarkRule](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EC1E052F_B2C5_4767_9317_0E54B7A08615) | optional |  | Rule that must be observed when passing the line from inside, that is, from the lane with the lower absolute ID to the lane with the higher absolute ID |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Offset of start position of the `<line>` element, relative to the @*sOffset* given in the `<roadMark>` element |
| `tOffset` | double | required | m | Lateral offset from the lane border.  If `<sway>` element is present, the lateral offset follows the sway. |
| `width` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m | Line width. This attribute supersedes the definition in the `<roadMark>` element. |

**Related topics**

* [Section 11.9.1, “Road marking types and lines”](#sec-1540a1cc-8824-480d-a1af-c20ab0bd6e34)
* [Section 11.9.3, “Offset in road markings”](#sec-52e18ce8-c575-4918-ba4b-40da1afd60d8)

## 11.9.3 Offset in road markings

To describe lane markings that are not straight but have sideway curves, `<sway>` elements may be used.
A `<sway>` element relocates the lateral reference position for the following (explicit) type definition and thus defines an offset.
The sway offset is relative to the nominal reference position of the lane marking, meaning the lane border.

Offsets from the lateral reference position are defined by `<sway>` elements within the `<roadMark>` element.

**Elements in UML model**

**`<sway>` element**

In ASAM OpenDRIVE, offsets are represented by `<sway>` elements within `<roadMark>` elements.

```
UML class: t_road_lanes_laneSection_lcr_lane_roadMark_sway
XML tag:   <sway> (Multiplicity: 0..*)
```

Relocates the lateral reference position for the following (explicit) type definition and thus defines an offset.
The sway offset is relative to the nominal reference position of the lane marking, meaning the lane border.

Table 52. Attributes of the <sway> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `a` | double | required | m | Coefficient a, sway value at @s (ds=0) |
| `b` | double | required | 1 | Coefficient b |
| `c` | double | required | 1/m | Coefficient c |
| `d` | double | required | 1/m² | Coefficient d |
| `ds` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position of the `<sway>` element, relative to the @*sOffset* given in the `<roadMark>` element |

**Calculation**

For the definition of sways, the lateral reference position at a given point is calculated with the following polynomial function of the third order:

`tOffset (ds) = a + b*ds + c*ds² + d*ds³`

where

|  |  |
| --- | --- |
| `tOffset` | is the lateral offset of the lateral reference position from the lane border at a given ds position |
| `a, b, c, d` | are the coefficients |
| `ds` | is the distance along the road reference line between the start of the element and the given position. |

`ds` starts at zero for each element and is relative to the `sOffset` value given in the `<roadMark>` element.

**Related topics**

* [Section 11.9.1, “Road marking types and lines”](#sec-1540a1cc-8824-480d-a1af-c20ab0bd6e34)
* [Section 11.9.2, “Explicit road marking types and lines”](#sec-108966cb-ecfd-4c0c-b8d9-2e4f95b10210)