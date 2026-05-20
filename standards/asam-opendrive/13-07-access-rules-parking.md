# ASAM OpenDRIVE® v1.9.0 — 13.7 Access rules to parking spaces

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_07_access_rules_parking.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.7 Access rules to parking spaces

Objects of type parking space are defined as all other object types using the @type=parkingSpace within the `<object>` element.

![img](../_images/13_objects/object_8.png)

Figure 123. Parking spaces rectangular (left figure) and rhomboid (right figure)

[Figure 123](#fig-45a862d8-0673-4c69-bf01-bc2dff99b38d) shows how the outline of the parking space is described by `<cornerRoad>` or `<cornerLocal>` elements.
The access to a specified parking space may be restricted to a certain group, for example handicapped persons or residents, or a certain group of vehicles, for example buses.
Further restrictions depend on the application and are user defined text.

**Elements in UML model**

**`<parkingSpace>` element**

In ASAM OpenDRIVE®, access rules for parking spaces are represented by the `<parkingSpace>` element within the `<object>` element.

```
UML class: t_road_objects_object_parkingSpace
XML tag:   <parkingSpace> (Multiplicity: 0..1)
```

Details for a parking space may be added to the `<object>` element.

Table 98. Attributes of the <parkingSpace> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `access` | [e\_road\_objects\_object\_parkingSpace\_access](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_F7BE74C8_0856_4f3c_AF5B_E66FADE0EF06) | required | Access definitions for the parking space. Parking spaces tagged with "women" and "handicapped" are vehicles of type car. |
| `restrictions` | string | optional | Free text, depending on application |

**XML example**

* [Ex\_Parkingspace\_Rectangular.xodr](../_attachments/examples/Ex_Parkingspace/Ex_Parkingspace_Rectangular.xodr)
* [Ex\_Parkingspace\_rhomboid.xodr](../_attachments/examples/Ex_Parkingspace/Ex_Parkingspace_rhomboid.xodr)

**Rules**

The following rules apply to parkingSpace elements:

* The access to a specified parking space may be limited to a specified group of people or vehicles.
* Further access restrictions may be defined, but are not part of ASAM OpenDRIVE®.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.2.1, "`<curveLocal>` element"](13_02_object_outline.html#sec-faf3fe4b-e0a6-4aaa-aec5-75f71224e503)
* [Section 13.2.1, "`<cornerRoad>` element"](13_02_object_outline.html#sec-4bfef803-e146-4f6d-86b3-533540f56b51)
* [Section 13.2.1, "`<cornerLocal>` element"](13_02_object_outline.html#sec-cc00c8a6-eea6-49e6-b90c-37b21524c748)