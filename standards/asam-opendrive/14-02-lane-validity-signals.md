# ASAM Opendrive v1.9.0 — 14.2 Lane validity for signals

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_02_lane_validity_signals.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.2 Lane validity for signals

By default, signals are valid for all lanes of a road, for traffic traveling in the direction indicated by @orientation attribute of a `<signal>` element.
Lane validity offers the possibility to restrict the validity of a signal to specific lanes only by using a `<validity>` element.
If the road has multiple lane layers, the layer for which the lane validity applies can be defined explicitly.
If no layer is defined explicitly, it defaults to the permanent layer.
If the signal is valid for both the permanent and the temporary layer, two separate `<validity>` elements have to be used.

![img](../_images/14_signals/Signals_3.png)

Figure 132. Lanes with signals in the shape of road markings

[Figure 132](#fig-da6d3888-b77e-4fdc-a9ad-9e53f36eeb3c) shows how signals in the shape of a road marking specify the speed limit of different lanes.

|  |  |
| --- | --- |
|  | The @orientation attribute and `<validity>` element complement each other. The @orientation attribute and the `<validity>` element are not interchangeable. |

* The @orientation attribute defines the travel direction for which a signal is valid.
* The `<validity>` element defines the lanes for which a signal is valid.

As an example for the difference in using the attribute and the element, speed limits can be taken: if traveling in road reference line direction, with right-hand-traffic, then a speed limit signal with `orientation="+"` applies to a vehicle even if this vehicle is driving on an oncoming lane while overtaking.
If the validity is limited to all right lanes then the signal does not apply, however, to the vehicle while it is in an oncoming lane.
Therefore, the `<validity>` element should only be used to limit signals to specific lanes, for example for traffic lights which only apply to certain lanes.

**Elements in UML model**

**`<validity>` element**

In ASAM OpenDRIVE, lane validity is represented by the `<validity>` element within the `<signal>` or `<signalReference>` element.

```
UML class: t_road_objects_object_laneValidity
XML tag:   <validity> (Multiplicity: 0..*)
```

Lane validities restrict signals and objects to specific lanes.

Table 123. Attributes of the <validity> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `fromLane` | integer | required |  | Minimum ID of the lanes for which the object is valid |
| `layer` | [e\_layerType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_AD278949_5B78_140C_8285_9DC1E2DBC31E) | optional | 1.9.0 | Layer of the lanes for which the object is valid. |
| `toLane` | integer | required |  | Maximum ID of the lanes for which the object is valid |

**Rules**

The following rules apply to validity elements:

* A signal may be valid for one or more lanes.

* [asam.net:xodr:1.7.0:road.object.validty.check\_parent\_orientation](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-validty-check-parent-orientation): The range given by all `<validity>` elements shall be a subset of the parent’s @orientation attribute:

* Omitting @layer shall default to @layer="permanent".

* [asam.net:xodr:1.7.0:road.signal.validity.right\_hand\_traffic\_lane\_ids](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-validity-right-hand-traffic-lane-ids): For right-hand traffic, @orientation="+" implies that the `<validity>` element shall only span negative lane ids, while @orientation="-" implies that the `<validity>` element shall only span positive lane ids.
  If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

* [asam.net:xodr:1.7.0:road.signal.validity.left\_hand\_traffic\_lane\_ids](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-validity-left-hand-traffic-lane-ids): For left-hand-traffic, @orientation="-" implies that the `<validity>` element shall only span negative lane ids, while @orientation="+" implies that the `<validity>` element shall only span positive lane ids. If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

* [asam.net:xodr:1.7.0:road.object.bridges.from\_lower\_equal\_to](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-bridges-from-lower-equal-to): The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

**Related topics**

* [Section 14.1, "Introduction to signals"](14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)
* [Section 14.3, "Signal dependency"](14_03_signal_dependency.html#top-f4d8bdcc-3f58-454d-b14e-801a880d9c41)