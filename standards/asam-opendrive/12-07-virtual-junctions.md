# ASAM Opendrive v1.9.0 — 12.7 Virtual junctions

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_07_virtual_junctions.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.7 Virtual junctions

Virtual junctions are junctions that describe connections within a road without the need to cut the main road.
They are intended as best practice, for example, for the following use cases:

* Modeling driveways
* Modeling entries and exits to parking lots
* Modeling entries and exits to farm roads

![img](../_images/12_junctions/junction_3.png)

Figure 93. Example of a virtual junction showing a parking lot entry and exit

[Figure 93](#fig-916edd72-61e8-4549-8268-b7b9437da858) shows a virtual junction with three connecting roads `2`, `4` and `5`.
The virtual junction connects road `1` with road `99`.
Road `1` serves as an incoming road for connecting road `2` at the @sStart position s=50m.
Road `99` serves as incoming road for road `4` and road `5`.
Road `1` is successor for the two connecting roads `4` and `5` at @sEnd s=70m.
The successor is specified in the road definition of the connecting roads.

Virtual junctions are modeled by `<junction>` elements with the @type attribute.

**Elements in UML model**

For elements in the UML model see [Figure 84](12_01_introduction.html#fig-8b7e2624-7c2f-4771-9e00-284dc2067532).

**`<junction type="virtual">` element**

In ASAM OpenDRIVE, virtual junctions are represented by `<junction>` elements with the value `virtual` in the @type attribute within the `<OpenDRIVE>` element.

```
UML class: t_junction_virtual
XML tag:   <junction type="virtual"> (Multiplicity: 0..*)
```

Virtual junctions manage connections within an uninterrupted road, for example, entries and exits to parking lots, and pedestrian crossings.

Table 69. Attributes of the <junction type="virtual"> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `id` | string | required |  | ID of the junction to which the road belongs, for example connecting roads, cross paths, and roads of a junction boundary. Use -1 for none. |
| `mainRoad` | string | required |  | The main road from which the connecting roads of the virtual junction branch off. This attribute is mandatory for virtual junctions and shall not be specified for other junction types. |
| `name` | string | optional |  | Name of the junction. May be chosen freely. |
| `orientation` | [e\_orientation](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D8972119_8CE4_407e_A4AD_3183B0B5C687) | required |  | Defines the relevance of the virtual junction according to the driving direction. This attribute is mandatory for virtual junctions and shall not be specified for other junction types. The enumerator "none" specifies that the virtual junction is valid in both directions. |
| `sEnd` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | End position of the virtual junction in the reference line coordinate system. This attribute is mandatory for virtual junctions. |
| `sStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Start position of the virtual junction in the reference line coordinate system. This attribute is mandatory for virtual junctions. |
| `type` | [e\_junction\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_40D9549F_DB59_4440_A889_A09659446ED6) | required |  | Virtual junctions must be of type "virtual". |

**`<connection type="default">` element**

In ASAM OpenDRIVE, the connections are represented by `<connection>` elements with the value `default` in the @type attribute within the `<junction>` element.

```
UML class: t_junction_connection_virtual_default
XML tag:   <connection type="default"> (Multiplicity: 0..*)
```

Provides information about a single connection within a virtual junction.

Table 70. Attributes of the <connection type="default"> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `connectingRoad` | string | required |  |
| `contactPoint` | [e\_contactPoint](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EF13C2F5_5229_46f8_983F_E8B6252DC5B7) | optional | Contact point on the @connectingRoad or @linkedRoad. Required for all junction types except virtual. |
| `id` | string | required | Unique ID within the junction |
| `incomingRoad` | string | optional | ID of the incoming road. Required for all junction types except virtual. |
| `type` | [e\_connection\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_F48B9907_F898_46fd_A4AC_01A14BC1B4AE) | optional | Type of the connection. Regular connections are @type=“default” . This attribute is mandatory for virtual connections. |

**`<laneLink>` element**

In ASAM OpenDRIVE, lane links in virtual junctions are represented by `<laneLink>` elements within the `<connection>` element.

```
UML class: t_junction_connection_laneLink
XML tag:   <laneLink> (Multiplicity: 0..*)
```

Provides information about the lanes that are linked between an incoming road and a connecting road.
It is strongly recommended to provide this element.
It is deprecated to omit the `<laneLink>` element.

Table 71. Attributes of the <laneLink> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `fromLayer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional |  |  | Layer of the incoming lane (permanent, temporary). |
| `from` | integer | required |  |  | ID of the incoming lane |
| `overlapZone` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m | 1.8.0 | Specifies the length of the area where traffic from both overlapping lanes shares the space. It is defined in s length relative to the position of the junction. Intended for direct junctions only. Default is 100. |
| `toLayer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional |  |  | Layer of the connection lane (permanent, temporary). |
| `to` | integer | required |  |  | ID of the connection lane |

**XML example**

```
<road name="ConnectingRoad2" length="20" id="2" junction="555">
    <link>
        <predecessor elementType="road" elementId="1" elementS="50.0" elementDir="+"/>
        <successor elementType="road" elementId="99" contactPoint="end"/>
    </link>
    <laneSection s="0.0000000000000000e+00">
        <left/>
        <center/>
        <right>
            <lane id="-1" type="driving" level="false">
                <link>
                    <predecessor id="-2"/>
                    <successor id="1"/>
                </link>
            </lane>
        </right>
    </laneSection>
</road>
<road name="ConnectingRoad4" length="23" id="4" junction="555">
    <link>
        <predecessor elementType="road" elementId="99" contactPoint="end"/>
        <successor elementType="road" elementId="1" elementS="70.0" elementDir="+"/>
    </link>
    <laneSection s="0.0000000000000000e+00">
        <left/>
        <center/>
        <right>
            <lane id="-1" type="driving" level="false">
                <link>
                    <predecessor id="-1"/>
                    <successor id="-1"/>
                </link>
            </lane>
        </right>
    </laneSection>
</road>
<road name="ConnectingRoad5" length="20" id="5" junction="555">
    <link>
        <predecessor elementType="road" elementId="99" contactPoint="end"/>
        <successor elementType="road" elementId="1" elementS="70.0" elementDir="+"/>
    </link>
    <laneSection s="0.0000000000000000e+00">
        <left/>
        <center/>
        <right>
            <lane id="-1" type="driving" level="false">
                <link>
                    <predecessor id="-1"/>
                    <successor id="-2"/>
                </link>
            </lane>
        </right>
    </laneSection>
</road>
...
<junction name="myJunction" type="virtual" id="555" mainRoad="1" sStart="50" sEnd="70" orientation="+">
    <connection id="0" incomingRoad="1" connectingRoad="2" contactPoint="start">
        <laneLink from="-2" to="-1"/>
    </connection>
    <connection id="1" incomingRoad="99" connectingRoad="4" contactPoint="start">
        <laneLink from="-1" to="-1"/>
    </connection>
    <connection id="2" incomingRoad="99" connectingRoad="5" contactPoint="start">
        <laneLink from="-1" to="-1"/>
    </connection>
</junction>
```

**Rules**

The following rules apply to virtual junctions:

* The main incoming road within a virtual junction does not need to end before the junction area.
* Virtual junctions shall not replace common junctions and crossings that connect multiple roads.

* [asam.net:xodr:1.9.0:junctions.virtual.main\_road\_only](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-virtual-main-road-only): Virtual junctions shall be used for branches off the main road only. The main road has priority if not specified otherwise.

* [asam.net:xodr:1.9.0:junctions.virtual.no\_controllers](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-virtual-no-controllers): Virtual junctions shall not have controllers and therefore no traffic lights.

* If no incoming road is defined the @incomingRoad attribute has the value `-1`.

* [asam.net:xodr:1.9.0:junctions.virtual.connecting\_roads\_start\_end](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-virtual-connecting-roads-start-end): All connecting roads within the virtual junction shall either start or end at @sStart or at @sEnd.

* [asam.net:xodr:1.9.0:junctions.virtual.only\_one\_start\_end](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-virtual-only-one-start-end): There shall only be one @sStart and one @sEnd attribute for the virtual junction.

* [asam.net:xodr:1.9.0:junctions.virtual.heading\_equal\_mainroad](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-virtual-heading-equal-mainroad): The heading of the connecting roads and the @mainRoad shall be equal at @sStart and at @sEnd.

* [asam.net:xodr:1.9.0:junctions.virtual.linked\_lanes\_smooth\_fit](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-virtual-linked-lanes-smooth-fit): The linked lanes shall fit smoothly (see  [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)).

* The @mainRoad, @sStart, @sEnd, @orientation attributes shall only be valid for junctions of type virtual.
* Currently only flat virtual junctions can be modeled.

* [asam.net:xodr:1.8.0:junctions.common.direct\_junction\_attributes](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-common-direct-junction-attributes): The @overlapZone attribute shall only be specified for direct junctions.

**Related topics**

* [Section 12.14, "Signal synchronization groups in junctions"](12_14_signal_synchronization_groups.html#top-add49732-8747-40b6-93b0-1b3ff20afeb9)
* [Section 12.1, "Introduction to junctions"](12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)
* [Section 12.3, "Incoming roads"](12_03_incoming_roads.html#top-c0d5f9a9-a73a-4bcc-9a8c-393f357a559c)
* [Section 12.4, "Connecting roads"](12_04_connecting_roads.html#top-3e9bb97e-f2ab-4751-906a-c25e9fb7ac4e)
* [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 11.6, "Lane linkage"](../11_lanes/11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd)

## 12.7.1 Cross paths with virtual junctions

Cross paths with virtual junctions are modeled within the `<junction>` element with @type="virtual".
The value of the @mainRoad attribute defines the crossed road and the values of the @sStart and @sEnd attributes define the section with the cross path.

![img](../_images/12_junctions/cross_path.png)

Figure 94. Example of a cross path with a pedestrian crossing

[Figure 94](#fig-5a5d68e9-1201-48c1-9caf-ebe950cb94de) shows the road with @id="2" as cross path to connect the lanes with @id="-2" and @id="3" of the road with @id="1".

**XML example**

```
<road name="drivingRoad" length="200" id="1" junction="-1">
    <link>...</link>
    <planView>
        <geometry>...
            <line/>
        </geometry>
    </planView>
    <lanes>
        <laneSection s="0.0000000000000000e+00">
            <left>
                <lane id="3" type="walking">
                    <link>...</link>
                </lane>
                <lane id="2" type="driving">
                    <link>...</link>
                </lane>
                <lane id="1" type="driving">
                    <link>...</link>
                </lane>
            </left>
            <center>...</center>
            <right>
                <lane id="-1" type="driving">
                    <link>...</link>
                </lane>
                <lane id="-2" type="walking">
                    <link>...</link>
                </lane>
            </right>
        </laneSection>
        <laneSection s="5.0000000000000000e+01">
            <left>
                <lane id="3" type="walking">
                    <link>...</link>
                </lane>
                <lane id="2" type="driving">
                    <link>...</link>
                </lane>
                <lane id="1" type="restricted">
                    <link>...</link>
                </lane>
            </left>
            <center>...</center>
            <right>
                <lane id="-1" type="driving" level="false">
                    <link>...</link>
                </lane>
                <lane id="-2" type="walking">
                    <link>...</link>
                </lane>
            </right>
        </laneSection>
        <laneSection s="6.0000000000000000e+01">
            <left>
                <lane id="3" type="walking">
                    <link>...</link>
                </lane>
                <lane id="2" type="driving">
                    <link>...</link>
                </lane>
                <lane id="1" type="driving">
                    <link>...</link>
                </lane>
            </left>
            <center>...</center>
            <right>
                <lane id="-1" type="driving" level="false">
                    <link>...</link>
                </lane>
                <lane id="-2" type="walking">
                    <link>...</link>
                </lane>
            </right>
        </laneSection>
    </lanes>
    ...
</road>
<road name="pedestrian" length="12" id="2" junction="555">
    <link>...</link>
    <lanes>
        <laneSection s="0.0000000000000000e+00">
            <left/>
            <center>...</center>
            <right>
                <lane id="-1" type="walking">
                    <link/>
                </lane>
            </right>
        </laneSection>
    </lanes>
</road>
...
<junction name="pedestrianCrossPath" type="virtual" id="555" mainRoad="1" sStart="52" sEnd="58">
    <priority high="1" low="2"/>
    <crossPath id="0" crossingRoad="2" roadAtStart="1" roadAtEnd="1">
        <startLaneLink s="5.40000000000000000e+01" from="-2" to="-1"/>
        <endLaneLink s="5.4000000000000000e+01" from="3" to="-1"/>
    </crossPath>
</junction>
```

**Rules**

The following rules apply to cross paths with virtual junctions:

* The elevations of the crossing road defined by the @crossingRoad attribute of the `<crossPath>` element are disregarded.

* [asam.net:xodr:1.8.0:junctions.virtual.crossPath.cross\_road\_check\_s\_t](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-virtual-crosspath-cross-road-check-s-t): The crossing road shall not exceed the values for s and t of the main road defined by the @roadAtStart and @roadAtEnd attributes.

* [asam.net:xodr:1.8.0:junctions.cross\_path.lane\_linkage](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-cross-path-lane-linkage): Start and end of the crossing road shall reach the linked lanes specified by the `<startLaneLink>` and `<endLaneLink>` elements.

* [asam.net:xodr:1.8.0:junctions.cross\_path.only\_connect\_correct\_type](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-cross-path-only-connect-correct-type): Cross paths shall only connect lanes with @type="walking" or @type="biking".

**Related topics**

* [Section 12.5, "Cross paths"](12_05_cross_paths.html#top-6ac8a5ea-45ca-4a28-97e3-711deec5c792)
* [Section 12.8, "Crossings"](12_08_crossings.html#top-910643c3-508f-48a9-91a4-dd180adbdb2d)

## 12.7.2 Virtual connections (deprecated)

Virtual connections are deprecated and indicate possible connections between two roads or one or more lanes of two roads.
Because the indicated connections are only virtual, no real path is defined.
That means that the course of the reference line is not changed.

Virtual connections describe topological connections between roads and lanes.
They do not need to be geometrically correct.

![img](../_images/12_junctions/junction_4.png)

Figure 95. Virtual junction with virtual connections

[Figure 95](#fig-c7e99704-3f7e-476e-8bf4-54e0836c670f) shows a virtual junction with virtual connections.

**Elements in UML model**

For elements in the UML model see [Figure 84](12_01_introduction.html#fig-8b7e2624-7c2f-4771-9e00-284dc2067532).

**`<connection type="virtual">` element**

In ASAM OpenDRIVE, virtual connections are represented by `<connection>` elements with the value `virtual` in the @type attribute within the `<junction>` element.

```
UML class:  t_junction_connection_virtual
XML tag:    <connection type="virtual"> (Multiplicity: 0..*)
Deprecated: 1.8.0
```

Virtual connections indicate possible connections between two roads or one or more lanes of two roads.
Virtual connections do not specify connecting roads.

Table 72. Attributes of the <connection type="virtual"> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `connectingRoad` | string | required |  |
| `contactPoint` | [e\_contactPoint](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EF13C2F5_5229_46f8_983F_E8B6252DC5B7) | optional | Contact point on the @connectingRoad or @linkedRoad. Required for all junction types except virtual. |
| `id` | string | required | Unique ID within the junction |
| `incomingRoad` | string | optional | ID of the incoming road. Required for all junction types except virtual. |
| `type` | [e\_connection\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_F48B9907_F898_46fd_A4AC_01A14BC1B4AE) | required | Type of the connection. Virtual connections are fixed to @type=“virtual”. This attribute is mandatory for virtual connections. |

**`<predecessor>` and `<successor>` element**

In ASAM OpenDRIVE, predecessors and successors of virtual connections are represented by `<predecessor>` and `<successor>` elements within the `<connection>` element.

```
UML class:  t_junction_predecessorSuccessor
XML tag:    <predecessor> (Multiplicity: 1)
XML tag:    <successor> (Multiplicity: 1)
Deprecated: 1.8.0
```

Provides detailed information about the predecessor / successor road of a virtual connection.
Currently, only the @elementType “road” is allowed.

Table 73. Attributes of the <predecessor> and <successor> elements


| Name | Type | Use | Deprecated | Description |
| --- | --- | --- | --- | --- |
| `elementDir` | [e\_elementDir](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D1E21B53_3817_4627_8EC7_24415D264892) | required | 1.8.0 | Direction, relative to the s-direction, of the connection on the preceding / succeeding road |
| `elementId` | string | required | 1.8.0 | ID of the linked element |
| `elementS` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | 1.8.0 | s-coordinate where the connection meets the preceding / succeeding road. |
| `elementType` | string | required | 1.8.0 | Type of the linked element. Currently only "road" is allowed. |

**XML example**

```
<junction name="myJunction" type="virtual" id="555" >
    <connection id="0" incomingRoad="1" connectingRoad="2" contactPoint="start">
        <laneLink from="-2" to="-1"/>
    </connection>
    <connection id="1" incomingRoad="99" connectingRoad="4" contactPoint="start">
        <laneLink from="-1" to="-1"/>
    </connection>
    <connection id="2" incomingRoad="99" connectingRoad="5" contactPoint="start">
        <laneLink from="-1" to="-2"/>
    </connection>
    <connection id="3" type="virtual">
        <predecessor elementType="road" elementId="99" contactPoint="end"/>
        <successor   elementType="road" elementId="1" elementS="60.0" elementDir="-"/>
        <laneLink from="-1" to="1"/>
    </connection>
    <connection id="4" type="virtual">
        <predecessor elementType="road" elementId="99" contactPoint="end"/>
        <successor elementType="road" elementId="1"  elementS="60.0" elementDir="-"/>
        <laneLink from="-1" to="2"/>
    </connection>
    <connection id="5" type="virtual">
        <predecessor elementType="road" elementId="1" elementS="70.0" elementDir="-"/>
        <successor elementType="road" elementId="99" contactPoint="end"/>
        <laneLink from="1" to="1"/>
    </connection>
</junction>
```

**Rules**

The following rules apply to virtual connections:

* Virtual connections shall not replace regular geometrical elements described by road linkage and lane linkage.

* [asam.net:xodr:1.9.0:junctions.virtual.connections.only\_virtual\_junctions](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-virtual-connections-only-virtual-junctions): Virtual connections shall only be defined in virtual junctions.

**Related topics**

* [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 11.6, "Lane linkage"](../11_lanes/11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd)