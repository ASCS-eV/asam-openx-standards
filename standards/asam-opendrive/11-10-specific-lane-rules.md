# ASAM Opendrive v1.9.0 — 11.10 Specific lane rules

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_10_specific_lane_rules.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.10 Specific lane rules

It is possible to define special rules for certain lanes that are not specifically defined in the ASAM OpenDRIVE standard and which are stored in the used application.

**Elements in UML model**

**`<rule>` element**

In ASAM OpenDRIVE, a lane rule is represented by the `<rule>` element within the `<lane>` element.

```
UML class: t_road_lanes_laneSection_lr_lane_rule
XML tag:   <rule> (Multiplicity: 0..*)
```

Used to add rules that are not covered by any of the other lane attributes that are described in this specification.

Table 53. Attributes of the <rule> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `sOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position, relative to the position of the preceding `<laneSection>` element |
| `value` | string | required |  | Free text; currently recommended values are  "no stopping at any time"  "disabled parking"  "car pool" |

**Rules**

The following rules apply to lane rules:

* Applications may have specific lane rules that are only valid in the respective application, but not in ASAM OpenDRIVE.

* [asam.net:xodr:1.4.0:road.lane.rule.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-lane-rule-elem-asc-order): `<rule>` elements shall be defined in ascending order according to the s-coordinate.

**Related topics**

* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)