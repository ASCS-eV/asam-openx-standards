# ASAM Opendrive v1.9.0 — 13.6 Lane validity for objects

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_06_lane_validity_obj.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.6 Lane validity for objects

By default, objects are valid for all lanes of a road.
Lane validity offers the possibility to restrict the validity of an object to specific lanes only.
If the road has multiple lane layers, the layer can also be defined explicitly.

In ASAM OpenDRIVE, lane validity is represented by the `<validity>` element within the `<object>` element.

|  |  |
| --- | --- |
|  | The @orientation attribute and the `<validity>` element complement each other. The @orientation attribute and the `<validity>` element are not interchangeable. |

* @orientation defines the travel direction for which an object is valid.
  @orientation="+" or @orientation="-" should only be used if the object impacts traffic rules.
  Otherwise, @orientation="none" should be used.
* The `<validity>` element defines specific lanes for which an object is valid.
  It should only be used for objects which are relevant for traffic rules, for example outlines of stop lines.

**Elements in UML model**

**`<validity>` element**

```
UML class: t_road_objects_object_laneValidity
XML tag:   <validity> (Multiplicity: 0..*)
```

Lane validities restrict signals and objects to specific lanes.

Table 97. Attributes of the <validity> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `fromLane` | integer | required |  | Minimum ID of the lanes for which the object is valid |
| `layer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional | 1.9.0 | Layer of the lanes for which the object is valid. |
| `toLane` | integer | required |  | Maximum ID of the lanes for which the object is valid |

**Rules**

The following rules apply to validity elements:

* An object may be valid for specified lanes.
* An object may be valid for one lane only.
* Omitting @layer shall default to @layer="permanent".

* [asam.net:xodr:1.7.0:road.object.validty.check\_parent\_orientation](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-validty-check-parent-orientation): The range given by all `<validity>` elements shall be a subset of the parent’s @orientation attribute:

* [asam.net:xodr:1.7.0:road.object.validty.right\_hand\_traffic\_lane\_ids](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-validty-right-hand-traffic-lane-ids): For right-hand traffic, @orientation="+" implies that the `<validity>` element shall only span negative lane ids, while @orientation="-" implies that the `<validity>` element shall only span positive lane ids.
  If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

* [asam.net:xodr:1.7.0:road.object.validty.left\_hand\_traffic\_lane\_ids](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-validty-left-hand-traffic-lane-ids): For left-hand-traffic, @orientation="-" implies that the `<validity>` element shall only span negative lane ids, while @orientation="+" implies that the `<validity>` element shall only span positive lane ids.
  If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

* [asam.net:xodr:1.7.0:road.object.validty.from\_lower\_equal\_to](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-validty-from-lower-equal-to): The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.10, "Object reference"](13_10_object_reference.html#top-d3896352-d768-418d-9ca7-12aadc2e2d32)