# ASAM Opendrive v1.9.0 — 12.2 Common junctions

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_02_common_junctions.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.2 Common junctions

Common junctions are junctions with drivable lanes that can overlap.

![img](../_images/12_junctions/junction_1.png)

Figure 85. Types of roads in a junction (right-hand traffic)

[Figure 85](#fig-eac389f6-e0bc-4dcc-acf5-04ebf90e7f21) shows two different kinds of roads with relation to junctions.

* Incoming roads: These roads contain lanes that lead into a junction.
* Connecting roads: These roads represent the paths through a junction.

Outgoing roads are not specifically defined as an element or attribute in ASAM OpenDRIVE.
Incoming roads serve as outgoing roads.
These roads are implicitly defined as outgoing by the connecting roads that lead into them.

**Elements in UML model**

For elements in the UML model see [Figure 84](12_01_introduction.html#fig-8b7e2624-7c2f-4771-9e00-284dc2067532).

**`<junction>` element**

In ASAM OpenDRIVE, junctions are represented by `<junction>` elements within the `<OpenDRIVE>` element.

```
UML class: t_junction_common
XML tag:   <junction type="default"> (Multiplicity: 0..*)
```

Common junctions are the default type of junction in ASAM OpenDRIVE and specify areas where drivable lanes may overlap and traffic may cross.

Table 55. Attributes of the <junction type="default"> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | ID of the junction to which the road belongs, for example connecting roads, cross paths, and roads of a junction boundary. Use -1 for none. |
| `name` | string | optional | Name of the junction. May be chosen freely. |
| `type` | [e\_junction\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_40D9549F_DB59_4440_A889_A09659446ED6) | optional | Common junctions are of type "default". If the attribute is not specified, the junction type is "default". This attribute is mandatory for all other junction types. |

**`<connection>` element**

In ASAM OpenDRIVE, connections in a junction are represented by `<connection>` elements within the `<junction>` element.

```
UML class: t_junction_connection_common
XML tag:   <connection> (Multiplicity: 0..*)
```

Provides information about a single connection within a common junction.

Table 56. Attributes of the <connection> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `connectingRoad` | string | required | ID of the connecting road. Only to be used for junctions of @type="default". |
| `contactPoint` | [e\_contactPoint](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EF13C2F5_5229_46f8_983F_E8B6252DC5B7) | optional | Contact point on the @connectingRoad or @linkedRoad. Required for all junction types except virtual. |
| `id` | string | required | Unique ID within the junction |
| `incomingRoad` | string | optional | ID of the incoming road. Required for all junction types except virtual. |

**Rules**

The following rules apply to common junctions:

* [asam.net:xodr:1.4.0:junctions.common.when\_to\_use](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-junctions-common-when-to-use): Junctions shall only be used when roads cannot be linked directly. They clarify ambiguities for the linking. Ambiguities are caused when a road has two or more possible predecessor or successor roads.

* [asam.net:xodr:1.4.0:junctions.common.junctions\_no\_pred\_succ](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-junctions-common-junctions-no-pred-succ): Unlike roads, junctions do not have a predecessor or successor.

* A junction may have an own name to distinguish it from other junctions.

* [asam.net:xodr:1.9.0:junctions.common.not\_only\_two](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-junctions-common-not-only-two): Junctions should not be used when only two roads meet.

* [asam.net:xodr:1.5.0:junctions.common.virtual\_junction\_attributes](../16_annexes/map_rules.html#asam-net-xodr-1-5-0-junctions-common-virtual-junction-attributes): The @mainRoad, @orientation, @sStart and @sEnd attributes shall only be specified for virtual junctions.

* [asam.net:xodr:1.8.0:junctions.common.direct\_junction\_attributes](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-common-direct-junction-attributes): The @overlapZone attribute shall only be specified for direct junctions.

**Related topics**

* [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 11.6, "Lane linkage"](../11_lanes/11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd)
* [Section 12.3, "Incoming roads"](12_03_incoming_roads.html#top-c0d5f9a9-a73a-4bcc-9a8c-393f357a559c)
* [Section 12.4, "Connecting roads"](12_04_connecting_roads.html#top-3e9bb97e-f2ab-4751-906a-c25e9fb7ac4e)