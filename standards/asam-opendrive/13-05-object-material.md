# ASAM OpenDRIVE® v1.9.0 — 13.5 Object material

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_05_object_material.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.5 Object material

Objects placed on a road, such as patches, may consist of a different material than the surrounding road.
Therefore, the material of the object may be defined separately.
In ASAM OpenDRIVE®, it is possible to describe the surface, roughness, and friction.
The values depend on the application and are not defined in ASAM OpenDRIVE®.

**Elements in UML model**

**`<material>` element**

In ASAM OpenDRIVE®, the outlines of objects are represented by the `<material>` element within the `<object>` element.

```
UML class: t_road_objects_object_material
XML tag:   <material> (Multiplicity: 0..*)
```

Describes the material properties of objects, for example, patches that are part of the road surface but deviate from the standard road material.
Supersedes the material specified in the `<road material>` element and is valid only within the outline of the parent road object.

Table 96. Attributes of the <material> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `friction` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional |  | Friction value, depending on application |
| `roadMarkColor` | [e\_roadMarkColor](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_B67AEB84_154B_4c53_979E_7F1EA9751C9E) | optional | 1.8.0 | Color of the painted road marking. |
| `roughness` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional |  | Roughness, for example, for sound and motion systems, depending on application |
| `surface` | string | optional |  | Surface material code, depending on application |

**Rules**

The following rules apply to material for objects:

* [asam.net:xodr:1.7.0:road.object.material.materials\_may\_differ](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-material-materials-may-differ): The material of objects may differ from the surrounding road.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)