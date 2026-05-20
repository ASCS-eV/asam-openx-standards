# ASAM Opendrive v1.9.0 — 12.4 Connecting roads

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_04_connecting_roads.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.4 Connecting roads

Connecting roads link the roads that meet in a junction.
They describe the paths that a vehicle can travel across a junction.
Connecting roads are modeled in the same way as standard roads.

The paths described by a connecting road is based on its lanes.
The connecting road specifies the connections between the lanes of an incoming road and the lanes of an outgoing road of the same junction.
If the lanes of an incoming and outgoing road are not linked, this means that there is no traversable path between these lanes.

![img](../_images/12_junctions/junction_2.png)

Figure 86. Connecting roads of junction with id 1 (left hand traffic)

[Figure 85](12_02_common_junctions.html#fig-eac389f6-e0bc-4dcc-acf5-04ebf90e7f21) and [Figure 86](#fig-32710c64-58e4-4133-b300-7be76f475326) show the connecting roads inside the junction area that connect the incoming and outgoing roads.

|  |  |
| --- | --- |
|  | The example in [Table 59](#tab-1f8ca32d-cf77-46db-bd6f-ee9ecb026e42), [Table 60](#tab-5f69947c-02c1-477c-94ab-60bcb734470f), and [Table 61](#tab-729a1f45-253e-40a0-9271-d512ae037c33) only considers how to cross the junction from the road with id="4". |

Table 58. Junction with id 1


| Connection id | Incoming road | Connecting road | Contact point | Lane link from | Lane link to |
| --- | --- | --- | --- | --- | --- |
| 9 | 4 | 28 | start |  |  |
|  |  |  |  | -3 | 1 |
| 10 | 4 | 61 | start |  |  |
|  |  |  |  | -2 | 1 |
|  |  |  |  | -3 | 2 |
| 11 | 4 | 64 | start |  |  |
|  |  |  |  | -1 | 1 |

Table 59. Roads


| Road id | Predecessor | Contact predecessor | Successor | Contact successor | Junction |
| --- | --- | --- | --- | --- | --- |
| 1 | junction with id 1 |  |  |  | -1 |
| 2 | junction with id 1 |  |  |  | -1 |
| 3 |  |  | junction with id 1 |  | -1 |
| 4 | junction with id 1 |  |  |  | -1 |
| 28 | road with id 4 | start | road with id 2 | start | 1 |
| 61 | road with id 4 | start | road with id 3 | end | 1 |
| 64 | road with id 4 | start | road with id 1 | start | 1 |

Table 60. Lane links


| Road id | Lane id | Predecessor’s lane id | Predecessor’s lane layer | Successor’s lane id | Successor’s lane layer |
| --- | --- | --- | --- | --- | --- |
| 28 | 1 | -3 | permanent | 3 | permanent |
| 61 | 1 | -2 | permanent | -2 | permanent |
| 61 | 2 | -3 | permanent | -3 | permanent |
| 64 | 1 | -1 | permanent | 1 | permanent |
| 4 | -3 | no lane link | permanent |  | permanent |
| 4 | -2 | no lane link | permanent |  | permanent |
| 4 | -1 | no lane link | permanent |  | permanent |
| 1 | 1 | no lane link | permanent |  | permanent |
| 3 | -2 |  | permanent | no lane link | permanent |
| 3 | -3 |  | permanent | no lane link | permanent |
| 2 | 3 | no lane link | permanent |  | permanent |

**Elements in UML model**

**`<connection connectingRoad="…​">` element**

In ASAM OpenDRIVE, connecting roads are represented by the @connectingRoad attribute of `<connection>` elements within the `<junction>` element.

```
UML class: t_junction_connection_common
XML tag:   <connection> (Multiplicity: 0..*)
```

Provides information about a single connection within a common junction.

Table 61. Attributes of the <connection> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `connectingRoad` | string | required | ID of the connecting road. Only to be used for junctions of @type="default". |
| `contactPoint` | [e\_contactPoint](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EF13C2F5_5229_46f8_983F_E8B6252DC5B7) | optional | Contact point on the @connectingRoad or @linkedRoad. Required for all junction types except virtual. |
| `id` | string | required | Unique ID within the junction |
| `incomingRoad` | string | optional | ID of the incoming road. Required for all junction types except virtual. |

**`<laneLink>` element**

In ASAM OpenDRIVE, lane links are represented by `<laneLink>` elements within the `<connection>` element.

```
UML class: t_junction_connection_laneLink
XML tag:   <laneLink> (Multiplicity: 0..*)
```

Provides information about the lanes that are linked between an incoming road and a connecting road.
It is strongly recommended to provide this element.
It is deprecated to omit the `<laneLink>` element.

Table 62. Attributes of the <laneLink> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `fromLayer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional |  |  | Layer of the incoming lane (permanent, temporary). |
| `from` | integer | required |  |  | ID of the incoming lane |
| `overlapZone` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m | 1.8.0 | Specifies the length of the area where traffic from both overlapping lanes shares the space. It is defined in s length relative to the position of the junction. Intended for direct junctions only. Default is 100. |
| `toLayer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional |  |  | Layer of the connection lane (permanent, temporary). |
| `to` | integer | required |  |  | ID of the connection lane |

**XML example**

* [Ex\_LHT-Complex-X-Junction.xodr](../_attachments/examples/Ex_LHT-Complex-X-Junction/Ex_LHT-Complex-X-Junction.xodr) (left-hand traffic)
* [UC\_Simple-X-Junction.xodr](../_attachments/use_cases/UC_Simple-X-Junction/UC_Simple-X-Junction.xodr) (right-hand traffic)

**Rules**

The following rules apply to connecting roads:

* [asam.net:xodr:1.8.0:junctions.connection.one\_link\_to\_incoming](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-connection-one-link-to-incoming): There shall only be one `<connection>` for a specific combination of @incomingRoad and @connectingRoad.
  For each `<connection>`, its `<laneLink>` elements shall only be specified for the lanes that lead into the junction.

* A connecting road may have both right and left lanes.
* An incoming road with multiple lanes may be connected to the lanes of the road leading out off the junction in different ways:

* [asam.net:xodr:1.7.0:junctions.connection.no\_lane\_change\_for\_mult\_con\_roads](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-connection-no-lane-change-for-mult-con-roads): By multiple connecting roads, each with one `<laneLink>` element for the connection between two specific lanes. Lane changes within this junction are not possible.

* [asam.net:xodr:1.7.0:junctions.connection.lane\_change\_one\_con\_road](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-connection-lane-change-one-con-road): By one connecting road with multiple `<laneLink>` elements for the connections between the lanes.

* [asam.net:xodr:1.9.0:junctions.connection.smooth\_fit](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-connection-smooth-fit): The linked lanes shall fit smoothly as described for roads (see  [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)).

* [asam.net:xodr:1.9.0:junctions.connection.no\_connecting\_road\_direct](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-connection-no-connecting-road-direct): The @connectingRoad attribute shall not be used for junctions with @type="direct".

* Omitting @layer shall default to @layer="permanent".

**Related topics**

* [Section 12.3, "Incoming roads"](12_03_incoming_roads.html#top-c0d5f9a9-a73a-4bcc-9a8c-393f357a559c)
* [Section 12.1, "Introduction to junctions"](12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)
* [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 11.6, "Lane linkage"](../11_lanes/11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd)
* [Section 12.4.1, “Priorities of connecting roads within a junction”](#sec-f60730d7-4192-440e-a6ba-8082288a1115)
* [Section 11.8.1, "Lane access"](../11_lanes/11_08_lane_properties.html#sec-38bbc30a-8f0f-4387-8a87-0ddd34563404)

## 12.4.1 Priorities of connecting roads within a junction

The `<priority>` element within the `<junction>` element defines the priority of a road over another road as a pair with the ID of the road with higher priority in the @high attribute and the ID of the road with lower priority in the @low attribute.

**Elements in UML model**

**`<priority>` element**

In ASAM OpenDRIVE, the priority of roads is represented by `<priority>` elements within the `<junction>` element.

```
UML class: t_junction_priority
XML tag:   <priority> (Multiplicity: 0..*)
```

The junction priority record provides information about the priority of one road over another road that are part of this junction.
It is only required if priorities cannot be derived from signs or signals in a junction or on tracks leading to a junction.

Table 63. Attributes of the <priority> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `high` | string | required | ID of the prioritized road |
| `low` | string | required | ID of the road with lower priority |

**Rules**

The following rules apply to priorities of roads within a junction:

* [asam.net:xodr:1.7.0:junctions.priority.no\_signals](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-priority-no-signals): `<priority>` elements should only be used if there are no signals defined.

* [asam.net:xodr:1.8.0:junctions.priority.high\_and\_low\_attr](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-priority-high-and-low-attr): `<priority>` elements shall be defined with a pair of one @high and one @low attribute.

**Related topics**

* [Section 12.1, "Introduction to junctions"](12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)

## 12.4.2 Direction of connecting roads

Connecting roads inside a junction may have different directions.
For ease of use, the road reference line of the connecting roads should be placed in driving direction if the driving direction is unique.

The @contactPoint attribute inside the `<connection>` element is used to specify the direction of a connecting road.

**Rules**

The following rules apply to the direction of connecting roads:

* [asam.net:xodr:1.7.0:junctions.connection.start\_along\_linkage](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-connection-start-along-linkage): The value `start` shall be used to indicate that the connecting road runs along the linkage indicated in the `<laneLink>` element.

* [asam.net:xodr:1.7.0:junctions.connection.end\_opposite\_linkage](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-connection-end-opposite-linkage): The value `end` shall be used to indicate that the connecting road runs along the opposite direction of the linkage indicated in the `<laneLink>` element

**Related topics**

* [Section 10.4, "Road type"](../10_roads/10_04_road_type.html#top-ca0f8ace-54c0-4f4b-8977-0098d74b3e19)