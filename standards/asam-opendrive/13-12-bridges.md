# ASAM OpenDRIVE® v1.9.0 — 13.12 Bridges

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_12_bridges.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.12 Bridges

Bridges are modeled as objects in ASAM OpenDRIVE®.
The road with the bridge object leads over a bridge.
By definition, bridges are valid for the complete cross section of a road.
Bridges are described by a starting point, a length, and a type, such as concrete, steel, wood, or brick.

![img](../_images/13_objects/object_11.png)

Figure 126. Bridge

[Figure 126](#fig-b1cce70a-c3fd-4b87-be73-4d60ba0f997d) shows a bridge that is valid for the whole cross section of the road and that defines the part that is the bridge.

**Elements in UML model**

**`<bridge>` element**

In ASAM OpenDRIVE®, bridges are represented by the `<bridge>` element within the `<objects>` element.

```
UML class: t_road_objects_bridge
XML tag:   <bridge> (Multiplicity: 0..*)
```

Bridges are modeled as objects in ASAM OpenDRIVE®.
The road with the bridge object leads over a bridge.
Bridges are valid for a road’s complete cross section unless a lane validity record with further restrictions is provided as child element.

Table 106. Attributes of the <bridge> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `id` | string | required |  | Unique ID within database |
| `length` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Length of the bridge (in s-direction) |
| `name` | string | optional |  | Name of the bridge. May be chosen freely. |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate |
| `type` | [e\_bridgeType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_C4877BA5_2D1C_4d4a_A8AF_70B59039EBDA) | required |  | Type of bridge |

**`<validity>` element**

In ASAM OpenDRIVE®, lane validity is represented by the `<validity>` element within the `<object>` element.

```
UML class: t_road_objects_object_laneValidity
XML tag:   <validity> (Multiplicity: 0..*)
```

Lane validities restrict signals and objects to specific lanes.

Table 107. Attributes of the <validity> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `fromLane` | integer | required |  | Minimum ID of the lanes for which the object is valid |
| `layer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional | 1.9.0 | Layer of the lanes for which the object is valid. |
| `toLane` | integer | required |  | Maximum ID of the lanes for which the object is valid |

**XML example**

```
<objects>
    <bridge s="50.0 "
            length="100.0"
            name="ExampleBridge"
            id="1"
            type="concrete"/>
</objects>
```

**Rules**

The following rules apply to bridge elements:

* [asam.net:xodr:1.7.0:road.object.bridges.define\_type](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-bridges-define-type): Bridges may be restricted to certain lanes, using the `<laneValidity>` element.

* [asam.net:xodr:1.7.0:road.object.bridges.type\_definition](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-bridges-type-definition): The @type of the bridges shall be specified.

* [asam.net:xodr:1.7.0:road.object.bridges.from\_lower\_equal\_to](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-bridges-from-lower-equal-to): The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

**Related topics**

* [Section 10.2, "Properties for road sections and cross section"](../10_roads/10_02_properties_for_road_sections.html#top-1323a74c-b102-4fdd-bc02-63265f034f45)
* [Section 13.6, "Lane validity for objects"](13_06_lane_validity_obj.html#top-4f4a9920-bb53-4f67-ac57-afe4b23c1775)