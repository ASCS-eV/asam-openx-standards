# ASAM Opendrive v1.9.0 — 10.1 Introduction to roads

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/10_roads/10_01_introduction.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.1 Introduction to roads

**Elements in UML model**

**`<road>` element**

In ASAM OpenDRIVE, roads are represented by `<road>` elements within the `<OpenDRIVE>` element.

```
UML class: t_road
XML tag:   <road> (Multiplicity: 1..*)
```

Roads are the core elements for any road network in ASAM OpenDRIVE.
Each road runs along one road reference line.

A road shall have at least the center lane.
Vehicles may drive in both directions of the road reference line.
The standard driving direction is defined by the value which is assigned to the @rule attribute (RHT=right-hand traffic, LHT=left-han traffic).

ASAM OpenDRIVE roads may be roads in the real road network or artificial road network created for application use.
Each road is described by one or more `<road>` elements.
One `<road>` element may cover a long stretch of a road, shorter stretches between junctions, or even several roads.
A new `<road>` element should only start if the properties of the road cannot be described within the previous `<road>` element or if a junction is required.d

Table 23. Attributes of the <road> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `id` | string | required |  | Unique ID within the database. If it represents an integer number, it should comply to uint32\_t and stay within the given range. |
| `junction` | string | required |  | ID of the junction to which the road belongs, for example connecting roads, cross paths, and roads of a junction boundary. Use -1 for none. |
| `length` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | required | m | Total length of the reference line in the xy-plane. Change in length due to elevation is not considered |
| `name` | string | optional |  | Name of the road. May be chosen freely. |
| `rule` | [e\_trafficRule](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_E5B4C9F4_52A5_4673_9790_6A042A3E3CB0) | optional |  | Basic rule for using the road; RHT=right-hand traffic, LHT=left-hand traffic. When this attribute is missing, RHT is assumed. |

![img](../_images/uml_class_diagrams/EAID_E70C4B2B_6DDE_4179_A15E_75EF81E5C66F.png)

Figure 36. UML class diagram of the Road class

[Figure 36](#fig-85a83e7b-6dd1-4948-8a78-28d7a66907a0) shows the UML class diagram of the ASAM OpenDRIVE Road class.

![img](../_images/uml_class_diagrams/EAID_8A007E88_354E_463e_9D40_944248350DFB.png)

Figure 37. UML class diagram of the RoadGeometry class

[Figure 37](#fig-1a0ac60d-0a79-4724-b78f-eab7e6b4992b) shows the UML class diagram of the ASAM OpenDRIVE RoadGeometry class.

**Rules**

The following rules apply to roads:

* [asam.net:xodr:1.4.0:road.overlap\_inside\_junction](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-overlap-inside-junction): Only roads with the same junction id may overlap on the same level. This does not include roads on different driving levels, for example, bridges.

* [asam.net:xodr:1.4.0:road.no\_overlap\_outside\_junction](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-no-overlap-outside-junction): Roads outside a junction shall not overlap.

* [asam.net:xodr:1.4.0:road.no\_overlap\_self](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-no-overlap-self): A road shall not overlap with itself.

* [asam.net:xodr:1.9.0:road.length\_sum\_geometries](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-length-sum-geometries): The road length should be the sum of the lengths of all `<geometry>` elements

**Related topics**

* [Section 9.2, "Road reference line"](../09_geometries/09_02_road_reference_line.html#top-9cb15835-ff9e-4b51-9bc8-730a3695fde9)
* [Section 10.3, "Road linkage"](10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 11.1, "Introduction to lanes"](../11_lanes/11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)