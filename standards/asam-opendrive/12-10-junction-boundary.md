# ASAM OpenDRIVE® v1.9.0 — 12.10 Junction boundary

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_10_junction_boundary.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.10 Junction boundary

Junction boundaries define the outermost edge of the full area for common junctions, where the `<elevationGrid>` is applied to all points within this boundary.
A junction boundary consists of segments that run along the outmost edge of a given lane or perpendicular to lanes connected to the junction and should include all sidewalks or similar lanes.
Segments run counter clockwise around the junction and form a closed junction boundary.
The boundary can also specify a transition zone where local height is interpolated between road data and the `<elevationGrid>` in order to ensure a smooth transition from the roads outside of the junction onto the grid and vice versa.

For more information on `<elevationGrid>`, see  [Section 12.11, "Junction elevation grid"](12_11_junction_elevation_grid.html#top-26a9b5c3-a1f1-4958-b8da-4ce704ae96fc).

**Elements in UML model**

**`<boundary>` element**

In ASAM OpenDRIVE®, junction boundaries are represented by the `<boundary>` element within the `<junction>` element.

```
UML class:  t_junction_boundary
XML tag:    <boundary> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Junction boundaries enclose the area intended for traffic.
This also includes the sidewalks for pedestrians.

![img](../_images/uml_class_diagrams/EAID_4F7CBFCD_44AA_49be_9D85_6625376F773A.png)

Figure 98. UML class diagram of the JunctionBoundary class

[Figure 98](#fig-b10e5b4c-ec68-4b44-b4e7-dd5ccce00aca) shows the UML class diagram of the ASAM OpenDRIVE® JunctionBoundary class.

**`<segment type="lane">` element**

In ASAM OpenDRIVE®, segments along lanes are represented by `<segment>` elements with the value `lane` in the @type attribute within the `<boundary>` element.
The order of the `<segment>` elements represent the segments in counterclockwise order around the junction.

```
UML class:  t_junction_boundary_segment_lane
XML tag:    <segment type="lane"> (Multiplicity: 1..*)
Introduced: 1.8.0
```

A segment element with @type="lane" goes along @boundaryLane for the given s range.
It is the outmost edge of the lane relative to the center of the junction.

Table 77. Attributes of the <segment type="lane"> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `boundaryLane` | int | required |  | 1.8.0 | ID of the lane of which the outer edge is the segment |
| `roadId` | string | required |  | 1.8.0 | ID of the road used for the segment |
| `sEnd` | [t\_grEqZeroOrContactPoint](../16_annexes/map_uml_data_types.html#top-EAID_2467CAA3_B070_4f21_85B0_255F09E84E26) | required | m | 1.8.0 | End of the segment (s-coordinate, begin, end) |
| `sStart` | [t\_grEqZeroOrContactPoint](../16_annexes/map_uml_data_types.html#top-EAID_2467CAA3_B070_4f21_85B0_255F09E84E26) | required | m | 1.8.0 | Start of the segment (s-coordinate, begin, end) |
| `type` | [e\_junction\_segment\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_B80E83B2_0168_47c9_89E8_6F6B291D23B2) | required |  | 1.8.0 | Type of the segment |

**`<segment type="joint">` element**

In ASAM OpenDRIVE®, segments perpendicular to lanes are represented by `<segment>` elements with the value `joint` in the @type attribute within the `<boundary>` element.
The order of the `<segment>` elements represent the segments in counterclockwise order around the junction.

```
UML class:  t_junction_boundary_segment_joint
XML tag:    <segment type="joint"> (Multiplicity: 1..*)
Introduced: 1.8.0
```

A segment element with @type="joint" is perpendicular to the start or end of the given road.

Table 78. Attributes of the <segment type="joint"> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `contactPoint` | [t\_grEqZeroOrContactPoint](../16_annexes/map_uml_data_types.html#top-EAID_2467CAA3_B070_4f21_85B0_255F09E84E26) | required |  | 1.8.0 | Contact point on the road |
| `jointLaneEnd` | int | optional |  | 1.8.0 | ID of the lane crossed by the segment. If missing all lanes are crossed by the segment. |
| `jointLaneStart` | int | optional |  | 1.8.0 | ID of the lane crossed by the segment. If missing all lanes are crossed by the segment. |
| `roadId` | string | required |  | 1.8.0 | ID of the road used for the segment |
| `transitionLength` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m | 1.8.0 | Length of the transition area where local height is interpolated between road data and the `<elevationGrid>` in order to ensure a smooth transition. The default is 0. |
| `type` | [e\_junction\_segment\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_B80E83B2_0168_47c9_89E8_6F6B291D23B2) | required |  | 1.8.0 | Type of the segment |

**XML example**

```
<junction>
    <boundary>
        <segment type="lane" roadId="8" boundaryLane="-2" sStart="begin" sEnd="end"/>
        <segment type="joint" roadId="2" contactPoint="end" jointLaneStart="2" jointLaneEnd="-1"/>
        <segment type="lane" roadId="17" boundaryLane="-1" sStart="begin" sEnd="end"/>
        <segment type="joint" roadId="3" contactPoint="start"/>
        <segment type="lane" roadId="100" boundaryLane="0" sStart="begin" sEnd="end"/>
        <segment type="joint" roadId="60" contactPoint="start" jointLaneStart="0" jointLaneEnd="2"/>
        <segment type="lane" roadId="52" boundaryLane="0" sStart="end" sEnd="begin"/>
        <segment type="joint" roadId="4" contactPoint="end" jointLaneStart="1" jointLaneEnd="-2"/>
        <segment type="lane" roadId="32" boundaryLane="-2" sStart="begin" sEnd="42.0"/>
        <segment type="lane" roadId="32" boundaryLane="-1" sStart="42.0" sEnd="end"/>
        <segment type="joint" roadId="5" contactPoint="end" jointLaneStart="1" jointLaneEnd="-2"/>
        <segment type="lane" roadId="41" boundaryLane="-2" sStart="begin" sEnd="end"/>
        <segment type="joint" roadId="1" contactPoint="start" jointLaneStart="-2" jointLaneEnd="2"/>
    </boundary>
</junction>
```

![img](../_images/12_junctions/junction_boundary_segments.png)

Figure 99. Junction boundary formed by segments

[Figure 99](#fig-7b71d8b5-f9bd-4b6a-9abf-3cffaae82953) shows a junction boundary out of various segments along lanes or perpendicular to lanes. The road with @id="100" has the sole purpose to provide a lane segment that closes the junction boundary at the gap between the road with @id="60" and the road with @id="3".

**Rules**

The following rules apply to junction boundaries:

* [asam.net:xodr:1.8.0:junctions.boundary.only\_for\_common\_junctions](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-boundary-only-for-common-junctions): Junction boundaries are currently only valid for common junctions.

* [asam.net:xodr:1.8.0:junctions.boundary.segments\_counter\_clockwise\_order](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-boundary-segments-counter-clockwise-order): Segments shall be ordered counter clockwise.

* [asam.net:xodr:1.8.0:junctions.boundary.segments\_for\_each\_conn\_road](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-boundary-segments-for-each-conn-road): Segments shall be defined to reach the start or end of all roads connected to the junction.

* [asam.net:xodr:1.8.0:junctions.boundary.segments\_close\_boundry](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-boundary-segments-close-boundry): Segments shall close the entire junction boundary.

* [asam.net:xodr:1.8.0:junctions.boundary.close\_gap\_with\_new\_roads](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-boundary-close-gap-with-new-roads): If the existing roads are not sufficient to define a closed junction boundary, additional roads shall be defined for the missing segments.

These additional roads shall follow the rules of road linkage to the incoming roads, outgoing roads, or connecting roads (see  [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)),
but are not required to have any lanes or connections.
Start and end of an additional road shall point away from both incoming and/or outgoing roads to the inside of the junction.
The @junction attribute shall contain the id of the junction to which the road belongs.

**Related topics**

* [Section 12.9, "Junction reference line"](12_09_junction_reference_line.html#top-c53f51c5-e3c1-4c7e-bc61-efdf4f0bf54c)
* [Section 12.11, "Junction elevation grid"](12_11_junction_elevation_grid.html#top-26a9b5c3-a1f1-4958-b8da-4ce704ae96fc)