# ASAM OpenDRIVE® v1.9.0 — 15.4 Stations

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/15_railroads/15_04_stations.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 15.4 Stations

Rail-bound vehicles like trams need stations for people to get on and off.
Each station shall have at least one platform, which may be further divided into segments.
The platforms determine the physical extent of a station.

The `<station>` element may also be used for bus stations.

![img](../_images/15_railroads/railroads_3.png)

Figure 146. Railroad stations

[Figure 146](#fig-a1c9fc52-e344-4dad-8624-4dd99fdb5233) shows two scenarios for stations:

* In the first scenario, one platform is referenced by the roads `1` and `3`, running in different driving directions.
  The platform consists of one segment only.
* In the second scenario, platform `1` is referenced by road `5` only.
  Platform `2` is referenced by road `4` and `6`.
  Platform `2` is split into two segments.

**Elements in UML model**

**`<station>` element**

In ASAM OpenDRIVE®, stations are represented by the `<station>` element within the `<OpenDRIVE>` element.

```
UML class: t_station
XML tag:   <station> (Multiplicity: 0..*)
```

Stations are places on the rail network where passengers enter and leave rail-bound vehicles at platforms.

May refer to multiple tracks and is therefore defined on the same level as junctions.

Table 151. Attributes of the <station> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | Unique ID within database |
| `name` | string | required | Unique name of the station |
| `type` | [e\_station\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_45C714B7_9D7E_4e51_9516_36C51903358C) | optional | Type of station. Free text, depending on the application.  e.g.: small, medium, large |

![img](../_images/uml_class_diagrams/EAID_2C45CCE7_B666_43dd_B239_6E71586B04E1.png)

Figure 147. UML class diagram of the Station class

[Figure 147](#fig-cab6a3b8-a90a-4743-83f5-e6820f19ac01) shows the UML class diagram of the ASAM OpenDRIVE® Station class.

**XML example**

* [Ex\_Railway-Station.xodr](../_attachments/examples/Ex_Railway-Station/Ex_Railway-Station.xodr)

**Rules**

The following rules apply to stations:

* [asam.net:xodr:1.7.0:road.railroad.stations.one\_platform\_per\_station](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-stations-one-platform-per-station): A `<station>` element shall be followed by at least one `<platform>` element.

* The type of the station may be further specialized by the @type attribute.
  The values are stored in the used application.

**Related topics**

* [Section 15.1, "Introduction to railroads"](15_01_introduction.html#top-cc907730-d1cf-4775-8d97-1898f533257b)
* [Section 15.4.1, “Platforms”](#sec-9504c509-63ef-427a-a9b9-db307266e523)
* [Section 15.4.2, “Segments”](#sec-279fe10d-a645-4073-8950-02f81f8183f6)

## 15.4.1 Platforms

A station shall contain at least one platform.
A platform shall be referenced by one or more railroad tracks.
See picture in [Figure 146](#fig-a1c9fc52-e344-4dad-8624-4dd99fdb5233).

**Elements in UML model**

**`<platform>` element**

In ASAM OpenDRIVE®, platforms are represented by the `<platform>` element within the `<station>` element.

```
UML class: t_station_platform
XML tag:   <platform> (Multiplicity: 1..*)
```

Platforms are essential parts of stations for passengers to enter and leave rail-bound vehicles.
One or more railroad tracks reference one platform.

Table 152. Attributes of the <platform> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | Unique ID within database |
| `name` | string | optional | Name of the platform. May be chosen freely. |

**Rules**

The following rules apply to platforms:

* [asam.net:xodr:1.7.0:road.railroad.platforms.min\_amount](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-platforms-min-amount): There shall be at least one platform per station.

* [asam.net:xodr:1.7.0:road.railroad.platforms.min\_segments](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-platforms-min-segments): A platform shall contain at least one segment.

**Related topics**

* [Section 15.4.2, “Segments”](#sec-279fe10d-a645-4073-8950-02f81f8183f6)

## 15.4.2 Segments

Platforms may be further divided into segments.
This is useful if a bi-directional railroad track runs along the same platform.
A platform shall contain at least one segment.

**Elements in UML model**

**`<segment>` element**

In ASAM OpenDRIVE®, segments are represented by the `<segment>` element within the `<platform>` element.

```
UML class: t_station_platform_segment
XML tag:   <segment> (Multiplicity: 1..*)
```

Segments are parts of platforms.

Each `<platform>` element is valid on one or more track segments.
The `<segment>` element must be specified.

Table 153. Attributes of the <segment> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `roadId` | string | required |  | Unique ID of the `<road>` element (track) that accompanies the platform |
| `sEnd` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Maximum s-coordiante on `<road>` element that has an adjacent platform |
| `sStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Minimum s-coordinate on `<road>` element that has an adjacent platform |
| `side` | [e\_station\_platform\_segment\_side](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EA21D184_0B60_44d3_8288_0B9F483F72E9) | required |  | Side of track on which the platform is situated when going from sStart to sEnd |

**Rules**

The following rules apply to segments:

* [asam.net:xodr:1.7.0:road.railroad.segment.segments\_per\_platform\_min\_amount](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-segment-segments-per-platform-min-amount): There shall be at least one segment per platform.

**Related topics**

* [Section 15.4.1, “Platforms”](#sec-9504c509-63ef-427a-a9b9-db307266e523)