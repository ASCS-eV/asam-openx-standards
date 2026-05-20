# ASAM Opendrive v1.9.0 — 14.8 Signal semantics

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_08_signal_semantics.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.8 Signal semantics

Signals are uniquely defined by the @country, @year, @type, and @subtype attributes.
These attributes specify the visualization of the signals because the visualization is different for each country.
However, the behavior of the traffic participant is often identical independent of the country, for example, for a stop sign.
A simulation engine requires rules specified for all signs for all countries.

## 14.8.1 Possible semantics

The introduction of signal semantics reduces the effort to specify the rules for all signs for all countries.
For signal semantics, the focus is on the behavior of traffic.
Functionality for signal semantics cannot be used for visualization.
This means, the signal semantics and its visual representation need not be identical.
As an example, a street sign may depict a car on white background within a red circle but apply to all motorized vehicles, not just cars.

As traffic behavior is very complex and also depending on other ASAM OpenDRIVE definitions, for example, the lane width, junctions, and road marking, signal semantics are reduced to a very limited scope.
The scope of signal semantics in ASAM OpenDRIVE is limited to traffic behavior that is specified just by signals in ASAM OpenDRIVE.
Each traffic behavior is specified by a specific element, for example, by the `<priority>` element that specifies priority regulations.

Table 135. Possible Semantics


| Traffic behavior | Description | Example | Link to attribute | Usage in/for `<defaultRegulations>` in `<header>` | Usage in/for `<signal>` or `<sign>` |
| --- | --- | --- | --- | --- | --- |
| <lane> | Specifies lane regulations. | Sign that defines cars are not allowed to overtake. | [`<lane>`](#sec-65079286-756b-4880-aa27-25b6358c4a71) | not recommended | recommended |
| <parking> | Specifies parking regulations. | Sign that defines that parking is forbidden. | no attributes | not allowed | recommended |
| <priority> | Specifies priority regulations. | Stop sign | [`<priority>`](#sec-672e879a-6d23-4cdf-9ef4-4bdba193313b) | recommend for default junction priority | recommended |
| <prohibited> | Specifies that certain types of traffic participants are not allowed to enter. Traffic participants are defined in [Section 14.8.2, “Traffic participants”](#sec-37cb97d2-633b-4228-ae29-caaee0853a24). | No pedestrians sign | no attributes | recommend for default junction priority | recommended |
| <routing> | Specifies routing information. | London | no attributes | not allowed | recommended |
| <speed> | Specifies speed regulations. | Speed limit sign | [`<speed>`](#sec-8398f7c9-c4d5-44e7-8f4e-90a89170ee43) | recommended | recommended |
| <streetname> | Specifies the name of a street. | High street | no attributes | not allowed | recommended |
| <tourist> | Specifies tourist information. | Science museum | no attributes | not allowed | recommended |
| <warning> | Specifies warnings for a type of traffic participant. | Deer might cross the road | no attributes | not allowed | recommended |
| <supplementaryAllows> | This signal semantic has no meaning on its own. It specifies the type of the traffic participant an exception is made for. Traffic participants are defined in [Section 14.8.2, “Traffic participants”](#sec-37cb97d2-633b-4228-ae29-caaee0853a24). | Except bicycles sign | no attributes | not allowed | recommended |
| <supplementaryDistance> | This signal semantic has no meaning on its own. It specifies the distance after a sign becomes valid or the range in which the sign is valid. | 200m sign | [`<supplementaryDistance>`](#sec-9d843dc7-7377-495a-bd64-b9d911638192) | not allowed | recommended |
| <supplementaryEnvironment> | This signal semantic has no meaning on its own. It specifies under which environmental conditions a sign is valid. | Rain sign | [`<supplementaryEnvironment>`](#sec-17488a44-da60-48ec-b8f3-e58209f56afd) | not allowed | recommended |
| <supplementaryExplanatory> | This signal semantic has no meaning on its own. It specifies explanations for a sign. | Emission reduction | no attributes | not allowed | recommended |
| <supplementaryProhibits> | This signal semantic has no meaning on its own. It specifies the type of the traffic participant a restriction is made for. Traffic participants are defined in [Section 14.8.2, “Traffic participants”](#sec-37cb97d2-633b-4228-ae29-caaee0853a24). | Truck Symbol | no attributes | not allowed | recommended |
| <supplementaryTime> | This signal semantic has no meaning on its own. It specifies the time or date a sign is valid. | 9:00 - 18:00 | [`<supplementaryTime>`](#sec-ac1528f5-8442-4801-b771-23a0e2368363) | not allowed | recommended |

**Elements in UML model**

**`<semantics>` element**

```
UML class:  t_signals_semantics
XML tag:    <semantics> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Semantics are limited to traffic behavior that is specified just by signals in ASAM OpenDRIVE.
Each traffic behavior is specified by a specific element.

![img](../_images/uml_class_diagrams/EAID_CA805EC8_2A9C_434e_91E8_E81321F9441F.png)

Figure 140. UML class diagram of the Semantics class

[Figure 140](#fig-2be31cc7-2652-4e1d-8530-a27baaeb2513) shows the UML class diagram of the ASAM OpenDRIVE Semantics class.

**`<lane>` element**

```
UML class:  t_signals_semantics_lane
XML tag:    <lane> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies lane regulations.

Table 136. Attributes of the <lane> element


| Name | Type | Use | Introduced |
| --- | --- | --- | --- |
| `type` | [e\_signals\_semantics\_lane](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_867E0EB2_99DA_4750_A148_B608A11DA73A) | required | 1.8.0 |

**`<parking>` element**

```
UML class:  t_signals_semantics_parking
XML tag:    <parking> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies parking regulations.

**`<priority>` element**

```
UML class:  t_signals_semantics_priority
XML tag:    <priority> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies priority regulations.

Table 137. Attributes of the <priority> element


| Name | Type | Use | Introduced |
| --- | --- | --- | --- |
| `type` | [e\_signals\_semantics\_priority](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_6C1E90A5_2BD7_4a01_B744_A04A326D29C6) | required | 1.8.0 |

**`<prohibited>` element**

```
UML class:  t_signals_semantics_prohibited
XML tag:    <prohibited> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies that certain types of traffic participants are not allowed to enter.
See Section 14.8.2, “Traffic participants” for details.

**`<routing>` element**

```
UML class:  t_signals_semantics_routing
XML tag:    <routing> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies routing information.

**`<speed>` element**

```
UML class:  t_signals_semantics_speed
XML tag:    <speed> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies speed regulations.

Table 138. Attributes of the <speed> element


| Name | Type | Use | Introduced |
| --- | --- | --- | --- |
| `type` | [e\_signals\_semantics\_speed](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_B7F9C248_F576_458b_8AE4_2BA4A71BBBDA) | required | 1.8.0 |
| `unit` | [e\_unitSpeed](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_491DC05E_01C6_49b3_83BE_A06DD81F9C35) | required |  |
| `value` | double | required |  |

**`<streetname>` element**

```
UML class:  t_signals_semantics_streetname
XML tag:    <streetname> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies the name of a street.

**`<tourist>` element**

```
UML class:  t_signals_semantics_tourist
XML tag:    <tourist> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies tourist information.

**`<warning>` element**

```
UML class:  t_signals_semantics_warning
XML tag:    <warning> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Specifies warnings for traffic participant.

**`<supplementaryAllows>` element**

```
UML class:  t_signals_semantics_supplementaryAllows
XML tag:    <supplementaryAllows> (Multiplicity: 0..*)
Introduced: 1.8.0
```

This signal semantic has no meaning on its own.
It specifies the type of the traffic participant an exception is made for.
See Section 14.8.2, “Traffic participants” for details.

**`<supplementaryDistance>` element**

```
UML class:  t_signals_semantics_supplementaryDistance
XML tag:    <supplementaryDistance> (Multiplicity: 0..*)
Introduced: 1.8.0
```

This signal semantic has no meaning on its own.
It specifies the distance after a sign becomes valid or the range in which the sign is valid.

Table 139. Attributes of the <supplementaryDistance> element


| Name | Type | Use | Introduced |
| --- | --- | --- | --- |
| `type` | [e\_signals\_semantics\_supplementaryDistance](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_CA994A8F_BDFF_432e_91D1_9162031C921E) | required | 1.8.0 |
| `unit` | [e\_unitDistance](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_00C01E54_46BF_4ad3_879B_3D03570EA74D) | required | 1.8.0 |
| `value` | double | required | 1.8.0 |

**`<supplementaryEnvironment>` element**

```
UML class:  t_signals_semantics_supplementaryEnvironment
XML tag:    <supplementaryEnvironment> (Multiplicity: 0..*)
Introduced: 1.8.0
```

This signal semantic has no meaning on its own.
It specifies under which environmental conditions a sign is valid.

Table 140. Attributes of the <supplementaryEnvironment> element


| Name | Type | Use | Introduced |
| --- | --- | --- | --- |
| `type` | [e\_signals\_semantics\_supplementaryEnvironment](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_B688C467_1003_4fd9_A272_CD13943176CE) | required | 1.8.0 |

**`<supplementaryExplanatory>` element**

```
UML class:  t_signals_semantics_supplementaryExplanatory
XML tag:    <supplementaryExplanatory> (Multiplicity: 0..*)
Introduced: 1.8.0
```

This signal semantic has no meaning on its own.
It specifies explanations for a sign.

**`<supplementaryProhibits>` element**

```
UML class:  t_signals_semantics_supplementaryProhibits
XML tag:    <supplementaryProhibits> (Multiplicity: 0..*)
Introduced: 1.8.0
```

This signal semantic has no meaning on its own.
It specifies the type of the traffic participant a restriction is made for.
See Section 14.8.2, “Traffic participants” for details.

**`<supplementaryTime>` element**

```
UML class:  t_signals_semantics_supplementaryTime
XML tag:    <supplementaryTime> (Multiplicity: 0..*)
Introduced: 1.8.0
```

This signal semantic has no meaning on its own.
It specifies the time or date a sign is valid.

Table 141. Attributes of the <supplementaryTime> element


| Name | Type | Use | Introduced |
| --- | --- | --- | --- |
| `type` | [e\_signals\_semantics\_supplementaryTime](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_2A1E7C8B_8ED8_4590_950F_23EDFF618584) | required | 1.8.0 |
| `value` | double | required | 1.8.0 |

**XML example**

```
<signal s="4.0"
        t="1.0"
        id="1"
        name="SpeedLimit60"
        dynamic="no"
        orientation="+"
        zOffset="2.00"
        country="DE"
        countryRevision="2013"
        type="274"
        subtype="56"
        value="60"
        unit="km/h"
        hOffset="0"
        pitch="0"
        roll="0"
        height="0.76"
        width="0.76">
    <semantics>
        <speed type="maximum" value="60" unit="km/h"/>
    </semantics>
</signal>
```

**Rules**

* Each `<signal>` element may have one or more semantic elements.

* [asam.net:xodr:1.9.0:road.signal.semantics.no\_semantics\_without\_category](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-signal-semantics-no-semantics-without-category): Signal semantics shall not be specified for signs if no category for the desired traffic behavior exists.

**Related topics**

* [Section 6.4.3, "`<defaultRegulations>` element"](../06_general_architecture/06_04_header.html#sec-27ad621f-1b2a-40d6-8723-b9f8aa00cb3f)
* [Section 14.8.2, “Traffic participants”](#sec-37cb97d2-633b-4228-ae29-caaee0853a24)
* [Annex E, *Categories for signal semantics (informative)*](../16_annexes/signal_semantics_categories/top_signal_semantics_categories.html#top-signal-semantics-categories)

## 14.8.2 Traffic participants

Signals semantics using `<prohibited>`, `<supplementaryAllows>`, or `<supplementaryProhibits>` can specify traffic participants.
These define particular types of traffic participants the signal either explicitly applies to (using `<prohibited>` or `<supplementaryProhibits>`) or which are exempt from it (using `<supplementaryAllows>`).
A traffic participant is either a `<vehicle>`, `<person>`, or `<animal>` element.
A sign may apply to more than one traffic participant.

|  |  |
| --- | --- |
|  | The enum literals have been harmonized between ASAM OpenX standards. The latest details about the harmonization can be found in the [ASAM TrafficParticipants Specification](https://publications.pages.asam.net/standards/ASAM_TrafficParticipants_Specification/ASAM_TrafficParticipants_Specification/latest/specification/index.html). |

Table 142. Traffic participants


| Traffic participant | Description | Example | Link to attribute | Usage in/for `<defaultRegulations>` in `<header>` | Usage in/for `<signal>` or `<sign>` |
| --- | --- | --- | --- | --- | --- |
| <vehicle> | Specifies a vehicular traffic participant. Vehicles are machines for transportation of humans, animals, or goods. They include motorized vehicles such as 'car', but also non-motorized vehicles like 'bicycle' or a wheelchair. To specify custom groups of vehicular traffic participants, use `<signalRegulations>` (see [Section 6.4.3.2, "`<signalRegulations>` element"](../06_general_architecture/06_04_header.html#sec-87debc1f-2e7b-4398-870c-38f620d783ab)). | No motorcycles | [`<vehicle>`](#sec-43a75a12-a74b-4a53-b2e2-e38fab35b127) | not allowed | recommended |
| <person> | Specifies a human traffic participant. In OpenDRIVE 1.9.0, this is restricted to pedestrians. | A pedestrian crossing the road. | [`<person>`](#sec-71480ebd-5c9e-4c7b-9e27-3eaaa7c0b61d) | not allowed | recommended |
| <animal> | Specifies an animal traffic participant. In OpenDRIVE 1.9.0, the type of animal cannot be specified. | Migratory toad crossing | no attributes | not allowed | recommended |

**`<vehicle>` element**

```
UML class:  t_signals_semantics_vehicle
XML tag:    <vehicle> (Multiplicity: 0..*)
Introduced: 1.9.0
```

Specifies a vehicular traffic participant.

Table 143. Attributes of the <vehicle> element


| Name | Type | Use |
| --- | --- | --- |
| `type` | [e\_vehicleCategory](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_A07A1644_B892_9BE8_96EE_83BA7D34121F) | required |

**`<person>` element**

```
UML class:  t_signals_semantics_person
XML tag:    <person> (Multiplicity: 0..*)
Introduced: 1.9.0
```

Specifies a human traffic participant.

Table 144. Attributes of the <person> element


| Name | Type | Use |
| --- | --- | --- |
| `type` | [e\_personCategory](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_8C99A5C4_2CF8_4407_AF46_1CF8873A6CD6) | required |

**`<animal>` element**

```
UML class:  t_signals_semantics_animal
XML tag:    <animal> (Multiplicity: 0..*)
Introduced: 1.9.0
```

Specifies an animal traffic participant.

**Rules**

* The enum literal "other" shall only be used if no other option fits.

**Related topics**

* [Section 6.4.3, "`<defaultRegulations>` element"](../06_general_architecture/06_04_header.html#sec-27ad621f-1b2a-40d6-8723-b9f8aa00cb3f)
* [Section 14.8.1, “Possible semantics”](#sec-ef42d3fd-8647-4d6a-9de5-6617346f27b5)
* [Annex E, *Categories for signal semantics (informative)*](../16_annexes/signal_semantics_categories/top_signal_semantics_categories.html#top-signal-semantics-categories)