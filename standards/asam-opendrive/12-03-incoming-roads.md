# ASAM OpenDRIVE® v1.9.0 — 12.3 Incoming roads

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_03_incoming_roads.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.3 Incoming roads

Incoming roads contain lanes that lead into a junction.
Because outgoing roads are not specifically defined in ASAM OpenDRIVE®, incoming roads may also serve as outgoing roads, see [Figure 85](12_02_common_junctions.html#fig-eac389f6-e0bc-4dcc-acf5-04ebf90e7f21).

To specify a road as incoming road, its ID is referenced in the `<connection>` element using the @incomingRoad attribute.

**Elements in UML model**

**`<connection incomingRoad="…​">` element**

In ASAM OpenDRIVE®, incoming roads are represented by the @incomingRoad attribute of `<connection>` elements within the `<junction>` element.

```
UML class: t_junction_connection_common
XML tag:   <connection> (Multiplicity: 0..*)
```

Provides information about a single connection within a common junction.

Table 57. Attributes of the <connection> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `connectingRoad` | string | required | ID of the connecting road. Only to be used for junctions of @type="default". |
| `contactPoint` | [e\_contactPoint](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EF13C2F5_5229_46f8_983F_E8B6252DC5B7) | optional | Contact point on the @connectingRoad or @linkedRoad. Required for all junction types except virtual. |
| `id` | string | required | Unique ID within the junction |
| `incomingRoad` | string | optional | ID of the incoming road. Required for all junction types except virtual. |

**XML example**

```
<junction name="myJunction" id="555" >
    <connection id="0"
                incomingRoad="1"
                connectingRoad="2"
                contactPoint="start">
        <laneLink from="-2" to="-1"/>
    </connection>
</junction>
```

**Rules**

The following rules apply to incoming roads:

* [asam.net:xodr:1.4.0:junctions.connection.connect\_road\_no\_incoming\_road](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-junctions-connection-connect-road-no-incoming-road): Connecting roads shall not be incoming roads.

**Related topics**

* [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 12.1, "Introduction to junctions"](12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)
* [Section 12.4, "Connecting roads"](12_04_connecting_roads.html#top-3e9bb97e-f2ab-4751-906a-c25e9fb7ac4e)