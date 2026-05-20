# ASAM OpenDRIVE® v1.9.0 — 12.6 Direct junctions

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_06_direct_junctions.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.6 Direct junctions

Direct junctions are intended to model entries and exits without adding additional connecting roads.
This approach reduces the number of roads required to model entries and exits in comparison with the common junction modeling approach in  [Section 12.4, "Connecting roads"](12_04_connecting_roads.html#top-3e9bb97e-f2ab-4751-906a-c25e9fb7ac4e).

**Elements in UML model**

For elements in the UML model see [Figure 84](12_01_introduction.html#fig-8b7e2624-7c2f-4771-9e00-284dc2067532).

**`<junction type="direct">` element**

In ASAM OpenDRIVE®, direct junctions are represented by `<junction>` elements with the value `direct` in the @type attribute within the `<junction>` element.

```
UML class:  t_junction_direct
XML tag:    <junction type="direct"> (Multiplicity: 0..*)
Introduced: 1.7.0
```

Direct junctions are intended to model entries and exits where drivable lanes may overlap to split or merge, but traffic does not cross.

Table 66. Attributes of the <junction type="direct"> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | ID of the junction to which the road belongs, for example connecting roads, cross paths, and roads of a junction boundary. Use -1 for none. |
| `name` | string | optional | Name of the junction. May be chosen freely. |
| `type` | [e\_junction\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_40D9549F_DB59_4440_A889_A09659446ED6) | required | Direct junctions must be of type "direct". |

**`<connection>` element**

In ASAM OpenDRIVE®, connections in direct junctions are represented by `<connection>` elements within the `<junction>` element.

```
UML class: t_junction_connection_direct
XML tag:   <connection> (Multiplicity: 1..*)
```

Provides information about a single connection within a direct junction.

Table 67. Attributes of the <connection> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `contactPoint` | [e\_contactPoint](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EF13C2F5_5229_46f8_983F_E8B6252DC5B7) | optional |  | Contact point on the @connectingRoad or @linkedRoad. Required for all junction types except virtual. |
| `id` | string | required |  | Unique ID within the junction |
| `incomingRoad` | string | optional |  | ID of the incoming road. Required for all junction types except virtual. |
| `linkedRoad` | string | required | 1.7.0 | ID of the directly linked road. Only to be used for junctions of @type="direct". |

**`<laneLink>` element**

In ASAM OpenDRIVE®, lane links in direct junctions are represented by `<laneLink>` elements within the `<connection>` element.

```
UML class: t_junction_connection_laneLink
XML tag:   <laneLink> (Multiplicity: 0..*)
```

Provides information about the lanes that are linked between an incoming road and a connecting road.
It is strongly recommended to provide this element.
It is deprecated to omit the `<laneLink>` element.

Table 68. Attributes of the <laneLink> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `fromLayer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional |  |  | Layer of the incoming lane (permanent, temporary). |
| `from` | integer | required |  |  | ID of the incoming lane |
| `overlapZone` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m | 1.8.0 | Specifies the length of the area where traffic from both overlapping lanes shares the space. It is defined in s length relative to the position of the junction. Intended for direct junctions only. Default is 100. |
| `toLayer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional |  |  | Layer of the connection lane (permanent, temporary). |
| `to` | integer | required |  |  | ID of the connection lane |

**Rules**

* [asam.net:xodr:1.8.0:junctions.direct.road\_connectivity](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-direct-road-connectivity): Direct junctions shall connect one road on one side with multiple roads on the other side.

* [asam.net:xodr:1.8.0:junctions.direct.split\_or\_merge](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-direct-split-or-merge): Direct junctions shall only be used for splitting or merging roads without crossing traffic.

* [asam.net:xodr:1.7.0:junctions.direct.correct\_type\_linked\_road\_usage](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-direct-correct-type-linked-road-usage): The @linkedRoad attribute shall only be used for junctions with @type="direct".

* [asam.net:xodr:1.7.0:junctions.direct.connecting\_road\_attribute\_usage](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-direct-connecting-road-attribute-usage): The @connectingRoad attribute shall not be used for junctions with @type="direct".

* [asam.net:xodr:1.7.0:junctions.direct.linked\_lane\_smoothness](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-direct-linked-lane-smoothness): The linked lanes shall fit smoothly as described for roads (see  [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)).

* [asam.net:xodr:1.7.0:junctions.direct.road\_ramp\_heading](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-direct-road-ramp-heading): The junction shall be placed where the headings of road, ramp, or slip lane are identical.

* [asam.net:xodr:1.8.0:junctions.direct.overlap\_zone\_exclusivity](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-direct-overlap-zone-exclusivity): Only one pair of `<laneLink>` elements shall have @overlapZone attributes to define the overlapping lanes.

* [asam.net:xodr:1.8.0:junctions.direct.overlap\_zone\_coverage](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-direct-overlap-zone-coverage): The value of the @overlapZone attribute shall cover at least the overlapping area, but may be larger.

* [asam.net:xodr:1.8.0:junctions.direct.flat\_exits\_entries](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-direct-flat-exits-entries): Currently only flat entries and exits can be modeled by overlapping direct junctions.

**Related topics**

* [Section 12.3, "Incoming roads"](12_03_incoming_roads.html#top-c0d5f9a9-a73a-4bcc-9a8c-393f357a559c)
* [Section 12.4, "Connecting roads"](12_04_connecting_roads.html#top-3e9bb97e-f2ab-4751-906a-c25e9fb7ac4e)
* [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 11.6, "Lane linkage"](../11_lanes/11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd)

## 12.6.1 Simple direct junction

![img](../_images/12_junctions/direct_junction_1.png)

Figure 88. Direct junction

[Figure 88](#fig-4172ceb7-d8ed-48f1-8139-ed8120ac1515) shows a road connected to two linked roads.
Road `1` is directly linked to roads `2` and `3`.

**XML example**

The XML example shows the model that is displayed in [Figure 88](#fig-4172ceb7-d8ed-48f1-8139-ed8120ac1515).

```
<road name="" length="50" id="1" junction="-1">
    <link>
        <successor elementType="junction" elementId="111"/>
    </link>
</road>
<road name="" length="50" id="2" junction="-1">
    <link>
        <predecessor elementType="junction" elementId="111" />
    </link>
</road>
<road name="" length="50" id="3" junction="-1">
    <link>
        <predecessor elementType="junction" elementId="111" />
    </link>
</road>
<junction name="" type="direct" id="111">
    <connection id="0" incomingRoad="1" linkedRoad="3" contactPoint="start">
        <laneLink from="-4" to="-1"/>
    </connection>
    <connection id="1" incomingRoad="1" linkedRoad="2" contactPoint="start">
        <laneLink from="1" to="1"/>
        <laneLink from="-1" to="-1"/>
        <laneLink from="-2" to="-2"/>
        <laneLink from="-3" to="-3"/>
    </connection>
</junction>
```

## 12.6.2 Direct junction with overlapping lanes

![img](../_images/12_junctions/direct_junction_2.png)

Figure 89. Direct junction with overlapping lanes

[Figure 89](#fig-b70fa351-1697-411e-a028-b300c25b5cf8) shows one road connected to two following roads with overlapping lanes.
Traffic from lane `-3` of road `1` may continue in lane `-3` of road `2` or change to lane `-1` of road `3`.
Traffic from lane `-4` of road `1` changes to lane `-2` of road `3`.
The @overlapZone attribute specifies at least the length of the area where the traffic of the two overlapping lanes shares the space.

**XML example**

The XML example shows the model that is displayed in [Figure 89](#fig-b70fa351-1697-411e-a028-b300c25b5cf8).

```
<road name="" length="50" id="1" junction="-1">
    <link>
        <successor elementType="junction" elementId="111"/>
    </link>
</road>
<road name="" length="50" id="2" junction="-1">
    <link>
        <predecessor elementType="junction" elementId="111" />
    </link>
</road>
<road name="" length="50" id="3" junction="-1">
    <link>
        <predecessor elementType="junction" elementId="111" />
    </link>
</road>
<junction name="" type="direct" id="111">
    <connection id="0" incomingRoad="1" linkedRoad="3" contactPoint="start">
        <laneLink from="-3" to="-1" overlapZone="41"/>
        <laneLink from="-4" to="-2"/>
    </connection>
    <connection id="1" incomingRoad="1" linkedRoad="2" contactPoint="start">
        <laneLink from="1" to="1"/>
        <laneLink from="-1" to="-1"/>
        <laneLink from="-2" to="-2"/>
        <laneLink from="-3" to="-3" overlapZone="40"/>
    </connection>
</junction>
```

|  |  |
| --- | --- |
|  | *Determining which lanes overlap by reading the XML*  Entries (slip lanes):  Find `<laneLink>` elements with identical values of the @to attribute. The lanes of the two incoming roads overlap.  Exits:  Find `<laneLink>` elements with identical values of the @from attribute. The lanes of the two linked roads overlap. |

## 12.6.3 Unsolvable cases for direct junctions

![img](../_images/12_junctions/direct_junction_3.png)

Figure 90. Junction with multiple overlapping lanes on two roads

[Figure 90](#fig-24f9581b-5153-46c4-b3db-1712d4aa46d7) shows one road connected to two following roads with multiple overlapping lanes.
Lane `-1` of road `3` overlaps lanes `-3` and `-4` of road `2`.
Lane `-2` of road `3` overlaps lane `-4` of road `2`.
Direct junctions cannot be used if multiple lanes overlap.
In this case common junctions shall be used (see  [Section 12.2, "Common junctions"](12_02_common_junctions.html#top-79fcd58e-0434-4188-a508-20effff8986e)).

![img](../_images/12_junctions/direct_junction_4.png)

Figure 91. Junction with multiple overlapping lanes on multiple roads

[Figure 91](#fig-d6f158a8-5cf7-43f9-8189-88e462f0d5eb) shows one road connected to three following roads with overlapping lanes.
Lane `-1` of road `2` overlaps lane `-1` of road `3`.
Lane `-1` of road `4` overlaps lane `-3` of road `3`.
Direct junctions cannot be used if multiple lanes overlap.
In this case common junctions shall be used (see  [Section 12.2, "Common junctions"](12_02_common_junctions.html#top-79fcd58e-0434-4188-a508-20effff8986e)).

![img](../_images/12_junctions/direct_junction_5.png)

Figure 92. Junction with crossing traffic and multiple overlapping lanes on multiple roads

[Figure 92](#fig-74b2fe27-8545-4030-a2d6-4e3206410b65) shows two roads connected to two following roads with crossing traffic.
Traffic from lane `-3` of road `1` to lane `-1` of road `4` crosses traffic from lane `-1` of road `3` to lane `-3` of road `2`.
Direct junctions cannot be used if traffic crosses.
In addition to the crossing traffic this junction also has multiple overlapping lanes and more than one road on both sides.
In this case common junctions shall be used (see  [Section 12.2, "Common junctions"](12_02_common_junctions.html#top-79fcd58e-0434-4188-a508-20effff8986e)).