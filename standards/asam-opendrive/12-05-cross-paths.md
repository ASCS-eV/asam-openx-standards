# ASAM Opendrive v1.9.0 — 12.5 Cross paths

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_05_cross_paths.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.5 Cross paths

Cross paths are similar to crossings from the driving point of view, adding connections between specific lanes.
Cross paths are part of the junction similar to connecting roads.

![img](../_images/12_junctions/cross_path_common.png)

Figure 87. Example of a cross path with a pedestrian crossing in a common junction

[Figure 87](#fig-023ef463-f73a-495f-8a66-cddae8ae71ae) shows a part of a common junction where the road with @id="75" as cross path connects the sidewalks of the two connecting roads with @id="45" and @id="46". The @roadAtStart attribute of the `<crossPath>` element defines which road the `<startLaneLink>` element refers to with its s@ attribute. The @roadAtEnd attribute of the `<crossPath>` element defines which road the `<endLaneLink>` element refers to with its s@ attribute.

Cross paths are represented by `<crossPath>` elements within the `<junction>` element.
A `<crossPath>` element defines the crossing road with the value of the @crossingRoad attribute and the roads connected by the cross path with the values of the @roadAtStart and @roadAtEnd attributes.

**Elements in UML model**

**`<crossPath>` element**

In ASAM OpenDRIVE, cross paths are represented by `<crossPath>` elements within the `<junction>` element.

```
UML class:  t_junction_crossPath
XML tag:    <crossPath> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Cross paths are intended for pedestrian crossings and are junctions elements where traffic of a lane can cross other lanes and continue on a different lane of the same or a different road.
The cross path itself is a separate road.

Table 64. Attributes of the <crossPath> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `crossingRoad` | string | required | 1.8.0 | ID of road defining the cross path. |
| `id` | string | required | 1.8.0 | Unique ID within the junction |
| `roadAtEnd` | string | required | 1.8.0 | ID of road at end point of the crossing road |
| `roadAtStart` | string | required | 1.8.0 | ID of road at start point of the crossing road |

**`<startLaneLink>` and `<endLaneLink>` elements**

In ASAM OpenDRIVE, lane links of cross paths are represented by `<startLaneLink>` and `<endLaneLink>` elements within the `<crossPath>` element.

```
UML class:  t_junction_crossPath_laneLink
XML tag:    <endLaneLink> (Multiplicity: 1)
XML tag:    <startLaneLink> (Multiplicity: 1)
Introduced: 1.8.0
```

Define the links between the lanes of the `<crossPath>` to the lanes of other roads.

Table 65. Attributes of the <endLaneLink> and <startLaneLink> elements


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `from` | integer | required | 1.8.0 | Lane ID of either @roadAtEnd for `<endLaneLink>` or @roadAtStart for `<startLaneLink>` |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | 1.8.0 | s-coordinate of either start or end point in linked road. |
| `to` | integer | required | 1.8.0 | Lane ID of @crossingRoad |

**XML example**

```
<road name="" length="6.8257399999999990e+01" id="4" junction="-1" rule="RHT">
    <link>
        <successor elementType="junction" elementId="10"/>
    </link>
    ...
    <lanes>
        <laneSection s="0.0000000000000000e+00">
            <left>
                <lane id="3" type="walking" level="false">
                    <link/>
                    ...
                </lane>
                <lane id="2" type="curb" level="false">
                    <link/>
                    ...
                </lane>
                <lane id="1" type="driving" level="false">
                    <link/>
                    ...
                </lane>
            </left>
            <center>
                <lane id="0">
                    ...
                </lane>
            </center>
            <right>
                <lane id="-1" type="driving" level="false">
                    <link/>
                    ...
                </lane>
                <lane id="-2" type="curb" level="false">
                    <link/>
                    ...
                </lane>
                <lane id="-3" type="walking" level="false">
                    <link/>
                    ...
                </lane>
            </right>
        </laneSection>
    </lanes>
    ...
</road>
<road name="" length="3.9995576531488346e+01" id="46" junction="10" rule="RHT">
    <link>
        <predecessor elementType="road" elementId="4" contactPoint="end"/>
        <successor elementType="road" elementId="6" contactPoint="end"/>
    </link>
    <lanes>
        <laneSection s="0.0000000000000000e+00">
            <left>
                <lane id="3" type="walking" level="false">
                    <link>
                        <predecessor id="3"/>
                        <successor id="-3"/>
                    </link>
                    ...
                </lane>
                <lane id="2" type="curb" level="false">
                    <link>
                        <predecessor id="2"/>
                        <successor id="-2"/>
                    </link>
                    ...
                </lane>
                <lane id="1" type="driving" level="false">
                    <link>
                        <predecessor id="1"/>
                        <successor id="-1"/>
                    </link>
                    ...
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
                        <predecessor id="-1"/>
                        <successor id="1"/>
                    </link>
                    ...
                </lane>
            </right>
        </laneSection>
    </lanes>
</road>
<road name="" length="2.8900504898771064e+01" id="45" junction="10" rule="RHT">
    <link>
        <predecessor elementType="road" elementId="4" contactPoint="end"/>
        <successor elementType="road" elementId="5" contactPoint="start"/>
    </link>
    ...
    <lanes>
        <laneSection s="0.0000000000000000e+00">
            <left>
                <lane id="1" type="driving" level="false">
                    <link>
                        <predecessor id="1"/>
                        <successor id="1"/>
                    </link>
                    ...
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
                        <predecessor id="-1"/>
                        <successor id="-1"/>
                    </link>
                    ...
                </lane>
                <lane id="-2" type="curb" level="false">
                    <link>
                        <predecessor id="-2"/>
                        <successor id="-2"/>
                    </link>
                    ...
                </lane>
                <lane id="-3" type="walking" level="false">
                    <link>
                        <predecessor id="-3"/>
                        <successor id="-3"/>
                    </link>
                    ...
                </lane>
            </right>
        </laneSection>
    </lanes>
    ....
</road>
<road name="" length="9.4332512961489723e+00" id="75" junction="10" rule="RHT">
    <link/>
    ...
    <lanes>
        <laneSection s="0.0000000000000000e+00">
            <left>
                <lane id="1" type="walking" level="false">
                    <link/>
                    ...
                </lane>
            </left>
            <center>
                <lane id="0">
                    ...
                </lane>
            </center>
        </laneSection>
    </lanes>
    ...
</road>
<junction name="" id="10">
    <connection id="0" incomingRoad="4" connectingRoad="46" contactPoint="start">
        <laneLink from="-1" to="-1"/>
    </connection>
    <connection id="1" incomingRoad="4" connectingRoad="45" contactPoint="start">
        <laneLink from="-1" to="-1"/>
        <laneLink from="-2" to="-2"/>
        <laneLink from="-3" to="-3"/>
    </connection>
    ...
    <crossPath id="6" crossingRoad="75" roadAtStart="46" roadAtEnd="45">
        <startLaneLink s="5.0000000000000000e-01" from="3" to="1"/>
        <endLaneLink s="2.4841630000000000e-01" from="-3" to="1"/>
    </crossPath>
    ...
</junction>
```

**Rules**

The following rules apply to cross paths:

* [asam.net:xodr:1.8.0:junctions.cross\_path.within\_junction\_area](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-cross-path-within-junction-area): Cross paths shall be within the area of a common junction or a virtual junction.

* [asam.net:xodr:1.8.0:junctions.cross\_path.disregard\_cross\_road\_evelation](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-cross-path-disregard-cross-road-evelation): The elevations of the crossing road defined by the @crossingRoad attribute of the `<crossPath>` element are disregarded.

* [asam.net:xodr:1.8.0:junctions.cross\_path.lane\_linkage](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-cross-path-lane-linkage): Start and end of the crossing road shall reach the linked lanes specified by the `<startLaneLink>` and `<endLaneLink>` elements.

* [asam.net:xodr:1.8.0:junctions.cross\_path.start\_end\_contained](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-cross-path-start-end-contained): The start and end points of the crossing road and its lanes shall be fully contained within the linked lanes specified by the `<startLaneLink>` and `<endLaneLink>` elements.

* [asam.net:xodr:1.8.0:junctions.cross\_path.only\_connect\_correct\_type](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-cross-path-only-connect-correct-type): Cross paths shall only connect lanes with @type="walking" or @type="biking".

* [asam.net:xodr:1.8.0:junctions.cross\_path.correct\_junction\_id](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-cross-path-correct-junction-id): The @junction attribute shall contain the id of the junction to which a road belongs.

**Related topics**

* [Section 12.7.1, "Cross paths with virtual junctions"](12_07_virtual_junctions.html#sec-eaa19a5b-a1de-4002-bc9d-f9ac4d39f839)
* [Section 12.8, "Crossings"](12_08_crossings.html#top-910643c3-508f-48a9-91a4-dd180adbdb2d)