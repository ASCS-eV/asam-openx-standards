# ASAM OpenDRIVE® v1.9.0 — 13.9 Object borders

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_09_object_borders.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.9 Object borders

In the current version of ASAM OpenDRIVE®, object borders are only allowed for Traffic Islands.
Objects of type "trafficIsland" may have a border, that is a frame of a defined width.
Different border types are available, currently concrete and curb.

The `<borders>` element serves as a wrapper for the `<border>` element, which itself contains further attributes to describe the borders.

**Elements in UML model**

**`<borders>` element**

In ASAM OpenDRIVE®, object borders are represented by the `<borders>` element within the `<object>` element.

```
UML class: t_road_objects_object_borders
XML tag:   <borders> (Multiplicity: 0..1)
```

Object borders are frames with a defined width, for example, to describe traffic islands.

Different border types are available.

**`<border>` element**

In ASAM OpenDRIVE®, object borders are represented by the `<border>` element within the `<borders>` element.

```
UML class: t_road_objects_object_borders_border
XML tag:   <border> (Multiplicity: 1..*)
```

Specifies a border along certain outline points.

Table 101. Attributes of the <border> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `outlineId` | nonNegativeInteger | required |  | ID of the outline to use |
| `type` | [e\_borderType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_2D816E93_925F_4971_9AA2_C88571AE7C5E) | required |  | Appearance of border |
| `useCompleteOutline` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional |  | Use all outline points for border. “true” is used as default. |
| `width` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Border width |

**Rules**

The following rules apply to object borders:

* [asam.net:xodr:1.7.0:road.object.borders.useCompleteOutline\_true](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-borders-usecompleteoutline-true): If @useCompleteOutline is true, the `<cornerReference>` element shall not be defined.

* If @useCompleteOutline is false, at least two `<cornerReference>` elements are mandatory.

* [asam.net:xodr:1.9.0:road.object.borders.different\_outlineids](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-borders-different-outlineids): All `<outline>` elements of an `<outlines>` element shall have different @outlineId values.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.2, "Object outline"](13_02_object_outline.html#top-67295042-9707-4ad5-9671-b80cde49bb3a)
* [Section 13.2.1, "Object marking on outlines"](13_02_object_outline.html#sec-c25542c0-f80d-4da9-a430-020474b58301)