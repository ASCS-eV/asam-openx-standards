# ASAM Opendrive v1.9.0 — 13.10 Object reference

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_10_object_reference.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.10 Object reference

It is possible to link an object with one or more roads, signals, or other objects.
These links represent a logical connection between the two elements.

An object reference is used, for example, if a pedestrian crossing crosses several roads.
In this case, the pedestrian crossing is defined for one road only, and then referenced by the other roads that it crosses.
Objects that apply to multiple roads within a junction can alternatively be attached to the junction reference line.

The lane validity element may be used to indicate for which lane the object reference is valid.

**Elements in UML model**

**`<objectReference>` element**

In ASAM OpenDRIVE, the object reference is represented by the `<objectReference>` element within the `<objects>` element.

```
UML class: t_road_objects_objectReference
XML tag:   <objectReference> (Multiplicity: 0..*)
```

An object reference refers to one identical object from multiple roads.
The referenced objects require a unique ID.
The `<objectReference>` element consists of a main element and an optional lane validity element.

Table 102. Attributes of the <objectReference> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `id` | string | required |  | Unique ID of the referred object within the database |
| `orientation` | [e\_orientation](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D8972119_8CE4_407e_A4AD_3183B0B5C687) | required |  | "+" = valid in positive s-direction  "-" = valid in negative s-direction  "none" = valid in both directions |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate |
| `t` | double | required | m | t-coordinate |
| `validLength` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m | Validity of the object along s-axis  (0.0 for point object) |
| `zOffset` | double | optional | m | z offset relative to the elevation of the road reference line |

**`<validity>` element**

In ASAM OpenDRIVE, lane validity is represented by the `<validity>` element within the `<object>` element or the `<objectReference>` element.

```
UML class: t_road_objects_object_laneValidity
XML tag:   <validity> (Multiplicity: 0..*)
```

Lane validities restrict signals and objects to specific lanes.

Table 103. Attributes of the <validity> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `fromLane` | integer | required |  | Minimum ID of the lanes for which the object is valid |
| `layer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional | 1.9.0 | Layer of the lanes for which the object is valid. |
| `toLane` | integer | required |  | Maximum ID of the lanes for which the object is valid |

**Rules**

The following rules apply for the purpose of reusing object information:

* [asam.net:xodr:1.7.0:road.object.reference.from\_lower\_equal\_to](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-reference-from-lower-equal-to): The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.6, "Lane validity for objects"](13_06_lane_validity_obj.html#top-4f4a9920-bb53-4f67-ac57-afe4b23c1775)
* [Section 14.4, "Signal reference"](../14_signals/14_04_signal_reference.html#top-1030e9ff-6b75-4353-b2b4-043f08c02a2d)