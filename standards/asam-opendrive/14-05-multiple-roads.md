# ASAM OpenDRIVE® v1.9.0 — 14.5 Signals that apply to multiple roads

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_05_multiple_roads.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.5 Signals that apply to multiple roads

ASAM OpenDRIVE® offers the possibility for one signal to apply to multiple roads.
This is achieved by defining the signal in one road using a `<signal>` element, and referencing it from one or more other roads using `<signalReference>` elements.
This is especially useful in junctions where many roads are close together and, for example, speed limit signs may need to apply to more than one of those close-together roads.

The `<signalReference>` element shall include the longitudinal, @s attribute, and lateral, @t attribute, position on the road where the referenced signal should take effect.
The `<signalReference>` element shall also include an @orientation attribute to specify whether the referenced signal applies to traffic flowing in the positive, negative, or both s-directions.
Similarly to `<signal>` elements themselves, `<signalReference>` elements may be supplemented with an `<validity>` element for lane validity.
This makes it possible to include or exclude certain lanes from the signal’s validity range.

**Elements in UML model**

**`<signalReference>` element**

In ASAM OpenDRIVE®, a referenced signal is represented by the `<signalReference>` element within the `<signals>` element.

```
UML class: t_road_signals_signalReference
XML tag:   <signalReference> (Multiplicity: 0..*)
```

Refers to the same, that is, identical signal from multiple roads.
The referenced signals require a unique ID.
The `<signalReference>` element consists of a main element and an optional lane validity element.

Table 126. Attributes of the <signalReference> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `id` | string | required |  | Unique ID of the referenced signal within the database |
| `orientation` | [e\_orientation](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D8972119_8CE4_407e_A4AD_3183B0B5C687) | required |  | "+" = valid in positive s-direction  "-" = valid in negative s-direction  "none" = valid in both directions |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate |
| `t` | double | required | m | t-coordinate |

![img](../_images/14_signals/fig_uml_class_signals_signalreference.png)

Figure 134. UML model of the t\_road\_signals\_signalReference element in the Signals class

[Figure 134](#fig-5135d59a-7c1f-44f2-98e2-06131929e846) shows the UML model of the t\_road\_signals\_signalReference element in the ASAM OpenDRIVE® Signals class.

**`<validity>` element**

In ASAM OpenDRIVE®, lane validity is represented by the `<validity>` element within the `<signal>` or `<signalReference>` element.

```
UML class: t_road_objects_object_laneValidity
XML tag:   <validity> (Multiplicity: 0..*)
```

Lane validities restrict signals and objects to specific lanes.

Table 127. Attributes of the <validity> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `fromLane` | integer | required |  | Minimum ID of the lanes for which the object is valid |
| `layer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional | 1.9.0 | Layer of the lanes for which the object is valid. |
| `toLane` | integer | required |  | Maximum ID of the lanes for which the object is valid |

**XML example**

* [UC\_X\_Junction.xodr](../_attachments/use_cases/UC_Junction/UC_X_Junction.xodr)

**Rules**

The following rules apply to referencing signals from multiple roads using the `<signalReference>` element:

* A lane `<validity>` element may be added for every `<signalReference>` element.

* [asam.net:xodr:1.7.0:road.signal.reference.used\_for\_signals\_only](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-reference-used-for-signals-only): Signal reference shall be used for signals only.

* [asam.net:xodr:1.7.0:road.signal.reference.specify\_direction](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-reference-specify-direction): The direction on the road for which the referenced signal is valid shall be specified for every `<signalReference>` element using the @orientation attribute.

* [asam.net:xodr:1.7.0:road.object.validty.check\_parent\_orientation](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-validty-check-parent-orientation): The range given by all `<validity>` elements shall be a subset of the parent’s @orientation attribute:

include::partial$rules/road/signal/reference/right\_hand\_traffic\_lane\_ids.adoc[].

* [asam.net:xodr:1.7.0:road.signal.reference.left\_hand\_traffic\_lane\_ids](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-reference-left-hand-traffic-lane-ids): For left-hand-traffic, @orientation="-" implies that the `<validity>` element shall only span negative lane ids, while @orientation="+" implies that the `<validity>` element shall only span positive lane ids. If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

* [asam.net:xodr:1.7.0:road.signal.reference.from\_lower\_equal\_to](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-reference-from-lower-equal-to): The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

**Related topics**

* [Section 14.1, "Introduction to signals"](14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)
* [Section 14.2, "Lane validity for signals"](14_02_lane_validity_signals.html#top-2aa0b17c-1b34-444c-9e00-fb51cc91c740)