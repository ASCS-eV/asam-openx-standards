# ASAM Opendrive v1.9.0 — 11.6 Lane linkage

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_06_lane_link.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.6 Lane linkage

To enable lane navigation, linkage information for lanes may be stored in ASAM OpenDRIVE.
Linkage is described by means of `<predecessor>` and `<successor>` elements for each lane.
Lanes may be linked to lanes on the same or another road.
Furthermore, lane links may be used to connect the permanent and the temporary layer.
Multiple lane links are permitted.
A `<predecessor>` of a given lane is a lane connected to the start of its lane section in its road reference line direction.
A `<successor>` of a given lane is a lane connected to the end of its lane section in road reference line direction.
A lane linkage by a `<predecessor>` and a `<successor>` is independent of the driving direction.

![img](../_images/11_lanes/lane_links.png)

Figure 66. Lane links for road with id 10

[Figure 66](#fig-1f3b2b07-6e8c-4d1a-8d95-6635da9a279e) shows an example for lane linkage.
The considered roads and their predecessor and successor are described in [Table 40](#tab-403158f8-3f09-4d1c-a513-50814a9b219c).

Table 39. Lane predecessors and successors for road with id 10


| Considered road | Lane predecessor | Lane successor |
| --- | --- | --- |
| Road 10 with lane id 1 | Lane id 1 (Road 30) | Lane id -1 (Road 20) |
| Road 10 with lane id -1 | Lane id -1 (Road 30) | Lane id 1 (Road 20) |
| Road 10 with lane id -2 | Lane id -2 (Road 30) | Lane id 2 (Road 20) |

The temporary lane layer does not need to be continuous over the whole length of a road.
A continuous set of one or more lane sections on the temporary lane layer is called a "temporary lane layer section" in ASAM OpenDRIVE.
An example for a temporary lane layer section is a roadworks section that applies to a section of a road.
To allow entering and exiting the lanes on the temporary lane layer at the start and end of that temporary lane layer section, a transition from the permanent to the temporary lane layer or vice versa must be provided for each lane on the temporary lane layer.
This leads to the lanes on the permanent layer having more than one predecessor or successor.

Lane predecessors and successors shall only be used to connect lanes if a physical connection at the beginning or end of both lanes exist.
Both lanes have a non-zero width at the connection point and are semantically connected.

Examples where lane linkage should be used:

* [asam.net:xodr:1.4.0:road.lane.link.lanes\_across\_laneSections](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-link-lanes-across-lanesections): Lane that continues across the lane sections shall be connected in both directions.

* Lane changes its type on a highway from `exit` to `offRamp`.
* Parking lane at the roadside ends, the road starts, and a vehicle can continue driving from the parking lane on the driving lane.
* Temporary lane of roadworks connects to the permanent lane.

Example where lane linkage should not be used:

* Parking lane at the roadside ends and a grass strip begins.

Examples where multiple predecessors and successors shall be used:

![img](../_images/11_lanes/lane_linkage_01.png)

Figure 67. Example of an ending bikeway

[Figure 67](#fig-d45dc8a4-fb40-4f14-b844-23f7100d7da3) shows an example where a bikeway ends and bicycles are expected to continue driving on the driving lane.

![img](../_images/11_lanes/lane_linkage_02.png)

Figure 68. Example of a splitting driving lane

[Figure 68](#fig-cb314ee4-8195-4c99-8b04-d7f8d8a797d6) shows an example where a driving lane splits into two or more driving lanes abruptly.
The width is non-zero.

Example where multiple predecessors and successors shall not be used:

* [asam.net:xodr:1.4.0:road.lane.link.new\_lane\_appear](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-link-new-lane-appear): If a new lane appears besides, only the continuing lane shall be connected to the original lane, not the appearing lane.

**Elements in UML model**

**`<link>` element**

In ASAM OpenDRIVE, lane linkage is represented by the `<link>` element within the `<lane>` element.

```
UML class: t_road_lanes_laneSection_lcr_lane_link
XML tag:   <link> (Multiplicity: 0..1)
```

For links between lanes with an identical road reference line, the lane predecessor and successor information provide the IDs of lanes on the preceding or following lane section.

For links between lanes with different road reference line, the lane predecessor and successor information provide the IDs of lanes on the first or last lane section of the other road reference line depending on the contact point of the road linkage.

This element may only be omitted, if lanes end at a junction or have no physical link.

![img](../_images/11_lanes/fig_uml_class_lanes_lanesection_lr_lane.png)

Figure 69. UML class diagram of the t\_road\_lanes\_laneSection\_lcr\_lane\_link element in the Lanes class

[Figure 69](#fig-74955d07-7be3-4527-9d4a-ea2fbbda6a1e) shows the UML class diagram of the t\_road\_lanes\_laneSection\_lcr\_lane\_link element in the ASAM OpenDRIVE Lanes class.

**`<predecessor>` and `<successor>` elements**

In ASAM OpenDRIVE, predecessors and successors are represented by the `<predecessor>` and `<successor>` elements within the `<link>` element.

```
UML class: t_road_lanes_laneSection_lcr_lane_link_predecessorSuccessor
XML tag:   <predecessor> (Multiplicity: 0..*)
XML tag:   <successor> (Multiplicity: 0..*)
```

Table 40. Attributes of the <predecessor> and <successor> elements


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | integer | required | ID of the preceding / succeeding linked lane. |
| `layer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional | Layer of the preceding / succeeding linked lane (permanent, temporary). |

**Rules**

The following rules apply to lane linkage:

* A lane may have another lane as predecessor or successor.
* The lane layer of a lane may be different from its predecessor or successor.
* Omitting @layer shall default to @layer="permanent".

* [asam.net:xodr:1.4.0:road.lane.link.use\_junctions](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-link-use-junctions): Two lanes shall only be linked if their linkage is clear. If the relationship to a predecessor or successor is ambiguous, junctions shall be used.

* [asam.net:xodr:1.4.0:road.lane.link.multiple\_connections](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-link-multiple-connections): Multiple predecessors and successors shall be used if a lane is split abruptly or several lanes are merged abruptly. All lanes that are connected shall have a non-zero width at the connection point.

* [asam.net:xodr:1.7.0:road.lane.link.zero\_width\_at\_start](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-lane-link-zero-width-at-start): Lanes that have a width of zero at the beginning of the lane section shall have no `<predecessor>` element.

* [asam.net:xodr:1.7.0:road.lane.link.zero\_width\_at\_end](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-lane-link-zero-width-at-end): Lanes that have a width of zero at the end of the lane section shall have no `<successor>` element.

* [asam.net:xodr:1.4.0:road.lane.link.no\_link](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-link-no-link): The `<link>` element shall be omitted if the lane starts or ends in a junction or has no link.

* [asam.net:xodr:1.9.0:road.lane.link.temporary\_layer\_section\_link\_permanent](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-link-temporary-layer-section-link-permanent): At the start and at the end of a temporary lane layer section, all drivable lanes with non-zero width on the temporary lane layer shall be linked to lanes on the permanent lane layer.

* [asam.net:xodr:1.9.0:road.lane\_section.new\_lanesec\_link\_temp\_to\_perm](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-section-new-lanesec-link-temp-to-perm): A new lane section on the permanent lane layer shall be defined each time lanes on the permanent layer are linked to lanes on the temporary layer.

**Related topics**

* [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 12.1, "Introduction to junctions"](../12_junctions/12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)