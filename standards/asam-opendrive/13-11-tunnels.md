# ASAM Opendrive v1.9.0 — 13.11 Tunnels

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_11_tunnels.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.11 Tunnels

Tunnels are modeled as objects in ASAM OpenDRIVE.
The road with the tunnel object defines the part of the road that is the tunnel or the underpass.
By definition, tunnels are valid for the complete cross section of a road.
Tunnels are described by a starting point, a length and a type, for example, if the tunnel represents an underpass and is open to daylight.
Additional properties may define the light conditions.

![img](../_images/13_objects/object_10.png)

Figure 125. Tunnel

[Figure 125](#fig-28dd5e95-118e-4567-b8e9-f8ad898fd79b) shows a tunnel that is valid for the whole cross section of the road and that defines the part that is the tunnel.

**Elements in UML model**

**`<tunnel>` element**

In ASAM OpenDRIVE, tunnels are represented by the `<tunnel>` element within the `<objects>` element.

```
UML class: t_road_objects_tunnel
XML tag:   <tunnel> (Multiplicity: 0..*)
```

Tunnels are modeled as objects in ASAM OpenDRIVE.
The road with the tunnel object defines the part of the road that is the tunnel or the underpass.

Tunnels are valid for the complete cross section of a road unless a lane validity element with further restrictions is provided as child element

Table 104. Attributes of the <tunnel> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `daylight` | [t\_zeroOne](../16_annexes/map_uml_data_types.html#top-EAID_AB1F001B_EB35_4c0d_84DF_A629F108D352) | optional |  | Degree of daylight intruding the tunnel. Depends on the application. |
| `id` | string | required |  | Unique ID within database |
| `length` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Length of the tunnel (in s-direction) |
| `lighting` | [t\_zeroOne](../16_annexes/map_uml_data_types.html#top-EAID_AB1F001B_EB35_4c0d_84DF_A629F108D352) | optional |  | Degree of artificial tunnel lighting. Depends on the application. |
| `name` | string | optional |  | Name of the tunnel. May be chosen freely. |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate |
| `type` | [e\_tunnelType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_0337D9C2_71FE_4896_9D80_BEF871FA0D8B) | required |  | Type of tunnel |

**`<validity>` element**

In ASAM OpenDRIVE, lane validity is represented by the `<validity>` element within the `<object>` element.

```
UML class: t_road_objects_object_laneValidity
XML tag:   <validity> (Multiplicity: 0..*)
```

Lane validities restrict signals and objects to specific lanes.

Table 105. Attributes of the <validity> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `fromLane` | integer | required |  | Minimum ID of the lanes for which the object is valid |
| `layer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional | 1.9.0 | Layer of the lanes for which the object is valid. |
| `toLane` | integer | required |  | Maximum ID of the lanes for which the object is valid |

**XML example**

```
<objects>
    <tunnel s="50.0"
            length="100.0"
            name="ExampleTunnel"
            id="1"
            type="standard"
            lighting="0.2"
            daylight="0.9"/>
</objects>
```

**Rules**

The following rules apply to tunnel elements:

* Tunnels may be restricted to certain lanes, using the `<laneValidity>` element.

* [asam.net:xodr:1.7.0:road.object.tunnels.type\_definition](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-tunnels-type-definition): The @type of the tunnel shall be specified.

* [asam.net:xodr:1.7.0:road.object.tunnels.from\_lower\_equal\_to](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-tunnels-from-lower-equal-to): The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

**Related topics**

* [Section 10.2, "Properties for road sections and cross section"](../10_roads/10_02_properties_for_road_sections.html#top-1323a74c-b102-4fdd-bc02-63265f034f45)
* [Section 13.6, "Lane validity for objects"](13_06_lane_validity_obj.html#top-4f4a9920-bb53-4f67-ac57-afe4b23c1775)
* [Section 13.12, "Bridges"](13_12_bridges.html#top-b65d5a80-f80f-415d-9188-349726023b4a)