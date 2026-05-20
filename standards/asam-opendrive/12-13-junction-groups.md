# ASAM OpenDRIVE® v1.9.0 — 12.13 Junction groups

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_13_junction_groups.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.13 Junction groups

Two or more junctions may be grouped in junction groups to indicate that these junctions belong to the same roundabout.

![img](../_images/12_junctions/junction_5.png)

Figure 108. Junction group with three junctions

[Figure 108](#fig-7046a7a4-6998-4cee-a8f6-02af371b9b23) shows how the junctions `1`, `2` and `3` are aggregated in junction group `A`.

Junction groups are described by `<junctionGroup>` elements.
The junctions that belong to the junction group are specified by `<junctionReference>` elements.

**Elements in UML model**

**`<junctionGroup>` element**

In ASAM OpenDRIVE®, junction groups are represented by the `<junctionGroup>` element within the `<OpenDRIVE>` element.

```
UML class: t_junctionGroup
XML tag:   <junctionGroup> (Multiplicity: 0..*)
```

Junction groups indicate for routing that the grouped junctions belong to the same node and are commonly seen as one big junction, for example roundabouts or highway interchanges.

The `<junctionGroup>` element is split into a header element and a series of member elements.

Table 82. Attributes of the <junctionGroup> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | Unique ID within database |
| `name` | string | optional | Name of the junction group. May be chosen freely. |
| `type` | [e\_junctionGroup\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_CE087C97_2B93_4646_83F9_DF84FE2DBE8C) | required | Type of junction group |

![img](../_images/uml_class_diagrams/EAID_C4CFB1D1_8463_420e_BB7B_BBC1449CFAB7.png)

Figure 109. UML class diagram of the JunctionGroup class

[Figure 109](#fig-31ea1f61-71ea-4db1-abc3-6bc684537a29) shows the UML class diagram of the ASAM OpenDRIVE® JunctionGroup class.

**`<junctionReference>` element**

In ASAM OpenDRIVE®, references to junctions are represented by the `<junctionReference>` element within the `<junctionGroup>` element.

```
UML class: t_junctionGroup_junctionReference
XML tag:   <junctionReference> (Multiplicity: 1..*)
```

References to existing `<junction>` elements.

Table 83. Attributes of the <junctionReference> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `junction` | string | required | ID of the junction |

**XML example**

* [UC\_2Lane-RoundAbout-3Arms.xodr](../_attachments/use_cases/UC_2Lane-RoundAbout-3Arms/UC_2Lane-RoundAbout-3Arms.xodr)

**Related topics**

* [Section 12.1, "Introduction to junctions"](12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)
* [Section 12.14, "Signal synchronization groups in junctions"](12_14_signal_synchronization_groups.html#top-add49732-8747-40b6-93b0-1b3ff20afeb9)