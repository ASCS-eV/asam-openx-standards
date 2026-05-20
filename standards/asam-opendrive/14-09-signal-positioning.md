# ASAM OpenDRIVE® v1.9.0 — 14.9 Signal positioning (deprecated)

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_09_signal_positioning.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.9 Signal positioning (deprecated)

The current ASAM OpenDRIVE® only places signals at their physical location and uses signal `<reference>` and/or `<dependency>` elements to model, for example the concept of the interaction between stop lines and stop signs or traffic lights.

The ASAM OpenDRIVE® Junction guideline describes interactivity between traffic lights and stop lines.

In previous versions of ASAM OpenDRIVE®, a signal’s position was identical with its validity and, therefore, should have been placed next to the road which it is valid for, enabling the application to identify the signals validity.
This was called the logical position of a signal.
The s-position of the signal described the position on the road where the signal takes effect.

![img](../_images/14_signals/Signals_5.png)

Figure 141. Junction with signals at physical and logical positions

[Figure 141](#fig-32d49d5d-4112-45a4-ba51-c62373663edc) shows how the physical and logical position of a signal could have differed in certain situations.
ASAM OpenDRIVE® offered two possibilities to describe the physical deviation of a signal.
The possibilities were mutually exclusive.
The positioning of the signal had no influence on its content.

* A signal may have been positioned at another physical position that is described with a road reference line coordinate system.  
  A signal whose physical position deviated from its logical position was represented by the `<positionRoad>` element within the `<signal>` element.
  That means, the ID of the specified road was referenced, together with the s- and t-coordinates of the road.  
  Examples were different positions of stop signs and stop lines.
* A signal may have been positioned at another physical position that was described with an inertial coordinate system.
  A signal whose physical position deviates from its logical position and was positioned using inertial coordinates was represented by the `<positionInertial>` element within the `<signal>` element.  
  Inertial coordinates were used, for example, if the signal was not placed next to a road, but on the other side of the street or hanging over a junction.

**Elements in UML model**

![img](../_images/14_signals/fig_uml_class_signals_physicalposition.png)

Figure 142. UML class diagram of the t\_physicalPosition element in the Signals class

[Figure 142](#fig-a3fe59ba-6cb0-490d-a9d7-37f0a64b892c) shows the UML class diagram of the t\_physicalPosition element in the ASAM OpenDRIVE® Signals class.

**`<positionRoad>` element**

In ASAM OpenDRIVE®, a signal position using a referenced road is represented by the `<positionRoad>` element within the `<signal>` element.

```
UML class:  t_road_signals_signal_positionRoad
XML tag:    <positionRoad>
Deprecated: 1.8.0
```

Describes the reference point of the physical position road coordinates in cases where it deviates from the logical position.
Defines the position on the road.

Table 145. Attributes of the <positionRoad> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `hOffset` | double | required | rad | Heading offset of the signal (relative to @orientation) |
| `pitch` | double | optional | rad | Pitch angle of the signal after applying hOffset, relative to the inertial system (x’y’-plane) |
| `roadId` | string | required |  | Unique ID of the referenced road |
| `roll` | double | optional | rad | Roll angle of the signal after applying hOffset and pitch, relative to the inertial system (x’’y’’-plane) |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate |
| `t` | double | required | m | t-coordinate |
| `zOffset` | double | required | m | z offset from road level to bottom edge of the signal |

**`<positionInertial>` element**

In ASAM OpenDRIVE®, a signal position using inertial coordinates is represented by the `<positionInertial>` element within the `<signal>` element.

```
UML class: t_road_signals_signal_positionInertial
XML tag:   <positionInertial>
```

Describes the reference point of the physical position in inertial coordinates in cases where it deviates from the logical position.
Defines the inertial position.

Table 146. Attributes of the <positionInertial> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `hdg` | double | required | rad | Heading of the signal, relative to the inertial system |
| `pitch` | double | optional | rad | Pitch angle of the signal after applying heading, relative to the inertial system (x’y’-plane) |
| `roll` | double | optional | rad | Roll angle of the signal after applying heading and pitch, relative to the inertial system (x’’y’’-plane) |
| `x` | double | required | m | x-coordinate |
| `y` | double | required | m | y-coordinate |
| `z` | double | required | m | z-coordinate |

**XML example**

* [UC\_LHT\_Complex-TrafficLights.xodr](../_attachments/use_cases/UC_LHT_Complex-TrafficLights/UC_LHT_Complex-TrafficLights.xodr)

**Rules**

The following rules apply to signal positioning:

* Signals should be placed next to the road for which they are valid.
* The physical position of signals may deviate from their logical position.

**Related topics**

* [Section 14.1, "Introduction to signals"](14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)
* [Section 14.2, "Lane validity for signals"](14_02_lane_validity_signals.html#top-2aa0b17c-1b34-444c-9e00-fb51cc91c740)
* [Section 14.3, "Signal dependency"](14_03_signal_dependency.html#top-f4d8bdcc-3f58-454d-b14e-801a880d9c41)
* [Section 14.4, "Signal reference"](14_04_signal_reference.html#top-1030e9ff-6b75-4353-b2b4-043f08c02a2d)