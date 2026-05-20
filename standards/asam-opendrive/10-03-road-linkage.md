# ASAM OpenDRIVE® v1.9.0 — 10.3 Road linkage

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/10_roads/10_03_road_linkage.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.3 Road linkage

For applications to navigate through a road network, roads must be linked to each other.
Roads may be connected to another road or a junction.
Isolated roads are not connected to other roads or junctions.

![img](../_images/10_roads/allow_link_1.png)

Figure 38. Allowed, prohibited, and recommended road linkage

[Figure 38](#fig-38e28751-d2f4-48e8-b4fe-762df507b0af) shows cases of prohibited, allowed, and recommended road linkage.
It is important that the lanes and road reference lines of the roads to be linked have a direct linkage to its predecessor or successor.
Overlaps or leaps should be avoided but are not prohibited if the road reference lines are connected properly.

![img](../_images/10_roads/allow_link_2.png)

Figure 39. Allowed cases of road linkage

[Figure 39](#fig-c4600da4-6139-45b6-9de0-af56f6797cc0) shows the allowed cases for road linkage outside junctions, with two roads running in the same, opposite, or converging directions.
Road linkage is not possible, if the two road reference lines are not connected to each other.

![img](../_images/10_roads/allow_link_3.png)

Figure 40. Allowed case of road linkage within a junction

[Figure 40](#fig-e1bb1e1d-2952-42a4-a0e5-03cdb913f366) shows the allowed case for road linkage within a junction.

A successor of a given road is an element connected to the end of its road reference line.
A predecessor of a given road is an element connected to the start of its road reference line.
For junctions, different attribute sets shall be used for the `<predecessor>` and `<successor>` elements.

**Elements in UML model**

**`<link>` element**

In ASAM OpenDRIVE®, road linkage is represented by the `<link>` element within the `<road>` element.

```
UML class: t_road_link
XML tag:   <link> (Multiplicity: 0..1)
```

Follows the road header if the road is linked to a successor or a predecessor.
Isolated roads may omit this element.

![img](../_images/uml_class_diagrams/EAID_4C4C33F7_889B_4892_ACCF_0127F3BA1B7B.png)

Figure 41. UML class diagram of the Link class

[Figure 41](#fig-805c6a13-6e8a-4e6c-bde6-170ae7b09a6c) shows the UML class diagram of the ASAM OpenDRIVE® Link class.

**`<predecessor>` and `<successor>` elements**

In ASAM OpenDRIVE®, predecessors and successors are represented by the `<predecessor>` and `<successor>` elements within the `<link>` element.

```
UML class: t_road_link_predecessorSuccessor
XML tag:   <predecessor> (Multiplicity: 0..1)
XML tag:   <successor> (Multiplicity: 0..1)
```

Successors and predecessors can be junctions or roads.
For each, different attribute sets shall be used.

Table 24. Attributes of the <predecessor> and <successor> elements


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `contactPoint` | [e\_contactPoint](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EF13C2F5_5229_46f8_983F_E8B6252DC5B7) | optional |  | Contact point of link on the linked element |
| `elementDir` | [e\_elementDir](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D1E21B53_3817_4627_8EC7_24415D264892) | optional |  | To be provided when elementS is used for the connection definition. Indicates the direction on the predecessor from which the road is entered. |
| `elementId` | string | required |  | ID of the linked element |
| `elementS` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m | Alternative to contactPoint for virtual junctions. Indicates a connection within the predecessor, meaning not at the start or end of the predecessor. Shall only be used for elementType "road" |
| `elementType` | [e\_road\_link\_elementType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_0DE449D1_BB4F_4bbc_A0DD_3A4722246020) | required |  | Type of the linked element |

**Rules**

The following rules apply to road linkage:

* [asam.net:xodr:1.4.0:road.linkage.is\_junction\_needed](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-linkage-is-junction-needed): Two roads shall only be linked directly if the linkage is clear. If the relationship to successor or predecessor is ambiguous, junctions shall be used.

* A road may have another road or a junction as successor or predecessor.
  A road may also have no successor or predecessor.
* A road may serve as its own predecessor or successor.

* [asam.net:xodr:1.4.0:road.linkage.road\_link\_attribute\_usage](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-linkage-road-link-attribute-usage): For a road as successor or predecessor the @elementType, @elementId and @contactPoint attributes shall be used.

* [asam.net:xodr:1.7.0:road.linkage.junc\_link\_attribute\_usage](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-linkage-junc-link-attribute-usage): For a common junction and a direct junction as successor or predecessor the @elementType and @elementId attributes shall be used.

* [asam.net:xodr:1.7.0:road.linkage.virtjunc\_link\_attribute\_usage](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-linkage-virtjunc-link-attribute-usage): For a virtual junction as successor or predecessor the @elementType, @elementId, @elementS and @elementDir attributes shall be used.

* [asam.net:xodr:1.9.0:road.linkage.both\_sides\_consistency](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-linkage-both-sides-consistency): `<predecessor>` and/or `<successor>` shall be defined at both sides of the road linkage and shall be consistent.

**Related topics**

* [Section 9.2, "Road reference line"](../09_geometries/09_02_road_reference_line.html#top-9cb15835-ff9e-4b51-9bc8-730a3695fde9)
* [Section 11.6, "Lane linkage"](../11_lanes/11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd)
* [Section 12.1, "Introduction to junctions"](../12_junctions/12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)