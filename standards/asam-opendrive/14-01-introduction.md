# ASAM OpenDRIVE® v1.9.0 — 14.1 Introduction to signals

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_01_introduction.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.1 Introduction to signals

Signals are traffic signs, traffic lights, and specific road marking for the control and regulation of road traffic.
Items that do not influence the behavior of traffic models directly are modeled as objects.
For more on objects, see  [Section 13.1, "Introduction to objects"](../13_objects/13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a).

![img](../_images/14_signals/Signals_1.png)

Figure 128. Signals in ASAM OpenDRIVE®

[Figure 128](#fig-6c4bd93c-5103-4335-9005-24153acfb62d) shows exemplary signal definitions for ASAM OpenDRIVE®.

Signals have different functions and properties:

* They are used to control traffic behavior, for example, with speed limits and turn restrictions, and to alert road traffic about dangerous situations.
* They can be static or dynamic.
  Static signals, such as stop signs, do not change their meaning.
  Dynamic signals, like traffic lights or variable message boards, may change their meaning during the simulation.
  Their dynamic content may be defined in ASAM OpenSCENARIO.
* They can be valid or invalid.
  An invalid sign is a sign that has been physically invalidated, such as a crossed-out speed limit in a roadworks zone.
  A signal is valid unless explicitly stated otherwise.
* They can be permanent or temporary.
  Examples for temporary signals are speed limit signs or traffic lights for road works.
  See also [Figure 60](../11_lanes/11_02_lane_layers.html#fig-8e54e01d-146a-4e0a-8e6c-f0ad6515b8c3) in  [Section 11.2, "Lane layers"](../11_lanes/11_02_lane_layers.html#top-709a1642-11e1-44bb-a26d-1de7478c23e3).

Signals shall be placed in relation to a specific road.
The position of the signal is described relative to the road reference line, using the s- and t- coordinates.
Signals shall be positioned in such a way that it is clear to which road or lane they belong and where their validity starts.
Ambiguity about their interpretation shall be avoided.

Traffic rules are different for each country.
The country of the signal is specified in the @country attribute.
When placing signals in ASAM OpenDRIVE®, country-specific legislation and traffic rules should be considered.
Legislative changes are indicated by the year when the rules come into force.
Traffic rules for the entire ASAM OpenDRIVE® file can be defined in the `<defaultRegulations>` element in the `<header>` element.

The @height and @width attributes of a signal are not required but are recommended for proper representation of the signal.
The @length attribute can be used to specify a thickness of the signal.

In addition to the road markings defined in this section, ASAM OpenDRIVE® also supports the following use cases:

* For the outer marking lines of a lane, use lane road markings.
  See  [Section 11.9, "Lane road markings"](../11_lanes/11_09_lane_road_markings.html#top-fc59db56-70c8-4320-a8c7-213379f8c037).
* For road markings that are not mandatory for driver and traffic models, use objects.
  See  [Section 13.2, "Object outline"](../13_objects/13_02_object_outline.html#top-67295042-9707-4ad5-9671-b80cde49bb3a) and  [Section 13.8, "Object markings"](../13_objects/13_08_object_markings.html#top-c25542c0-f80d-4da9-a430-020474b58301).

A signal with the @type and @subtype attributes is only unique in combination with the @country and @countryRevision attributes.
Since some elements that are considered signals in ASAM OpenDRIVE®, for example traffic lights, do not have any official
@type and @subtype representation, these are specified in the
 [Signal reference 1.0.0](../../../../ASAM_OpenDRIVE_Signal_reference/latest/signal-catalog/index.html) .
They can be used with the appropriate @type, @subtype and the @country="OpenDRIVE".

![img](../_images/14_signals/Signals_2.png)

Figure 129. Width and height for signal

[Figure 129](#fig-b5c4caf3-1266-41c7-bb3b-ff746fb8295e) shows the attributes ASAM OpenDRIVE® provides for a speed regulation signal.
It is pointed out how height and width are measured.

A signal with an @orientation of `+` applies to traffic traveling in the positive road reference line direction.
This means the signal with an @hOffset of `0` faces to the drivers traveling in a positive road reference line direction.
Any @hOffset given to this signal is applied counter-clockwise from the negative road reference line direction.

A signal with an @orientation of `-` applies to traffic traveling in the negative road reference line direction.
This means the signal with an @hOffset of `0` faces to the drivers traveling in the negative road reference line direction.
Any @hOffset given to this signal is applied counter-clockwise from the positive road reference line direction.

![img](../_images/14_signals/Signals_7.png)

Figure 130. Orientation and hOffset for signal

[Figure 130](#fig-27a17ba9-f404-41e1-975b-bd7116d277c7) shows a signal which applies to traffic traveling in the positive road reference line direction and which is turned counter-clockwise from the negative road reference line direction.
For the `<signal>` element, the @orientation attribute and @hOffset attribute are defined.
To the @orientation attribute the `+` value is assigned and to the @hOffset attribute a value of `5.7595865` is assigned.

**Elements in UML model**

**`<signals>` element**

In ASAM OpenDRIVE®, signals are represented by the `<signals>` element within the `<road>` element.

```
UML class: t_road_signals
XML tag:   <signals> (Multiplicity: 0..1)
```

Signals are traffic signs, traffic lights, and specific road markings that guide driver and traffic models.

The `<signals>` element is the container for all signals along a road.

![img](../_images/uml_class_diagrams/EAID_811E8671_D70D_4491_BCD2_F2DC1CDF8E17.png)

Figure 131. UML class diagram of the Signals class

[Figure 131](#fig-d8de1313-7b9a-4fac-b76f-4a60c8194997) shows the UML class diagram of the ASAM OpenDRIVE® Signals class.

**`<signal>` element**

In ASAM OpenDRIVE®, a signal is represented by the `<signal>` element within the `<signals>` element.

```
UML class: t_road_signals_signal_road
XML tag:   <signal> (Multiplicity: 0..*)
```

Used to provide information about signals along a road.
Consists of a main element and an optional lane validity element.
The element for a signal is `<signal>`.

Table 122. Attributes of the <signal> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `countryRevision` | string | optional |  |  | Defines the year of the applied traffic rules |
| `country` | [e\_countryCode](../16_annexes/map_uml_data_types.html#top-EAID_7A0922E5_0B9A_4a52_8063_A2499579DB20) | optional |  |  | Country code of the road, see ISO 3166-1, alpha-2 codes. |
| `dynamic` | [t\_yesNo](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_A171A2AA_DFE6_4b8b_BA5A_AD59E6334468) | required |  |  | Indicates whether the signal is dynamic or static. Example: traffic light is dynamic |
| `hOffset` | double | optional | rad |  | Heading offset of the signal (relative to @orientation, if orientation is equal to “+” or “-“)  Heading offset of the signal (relative to road reference line, if orientation is equal to “none” ) |
| `height` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Height of the signal, measured from bottom edge of the signal. |
| `id` | string | required |  |  | Unique ID of the signal within the OpenDRIVE file |
| `invalidated` | boolean | optional |  | 1.9.0 | Indicates whether the signal is currently invalidated. Example: crossed out traffic sign. |
| `length` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m | 1.8.0 | Length of the signal’s bounding box.  @length is defined in the local coordinate system u/v along the u-axis |
| `name` | string | optional |  |  | Name of the signal. May be chosen freely. |
| `orientation` | [e\_orientation](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D8972119_8CE4_407e_A4AD_3183B0B5C687) | required |  |  | "+" = valid in positive s- direction  "-" = valid in negative s- direction  "none" = valid in both directions |
| `pitch` | double | optional | rad |  | Pitch angle of the signal, relative to the inertial system (xy-plane) |
| `roll` | double | optional | rad |  | Roll angle of the signal after applying pitch, relative to the inertial system (x’’y’’-plane) |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m |  | s-coordinate |
| `subtype` | string | required |  |  | Subtype identifier according to country code or "-1" / "none" |
| `t` | double | required | m |  | t-coordinate |
| `temporary` | boolean | optional |  | 1.9.0 | Indicates whether the signal is temporary or permanent. Example: temporary speed limit sign in road works situation. |
| `text` | string | optional |  |  | Additional text associated with the signal, for example, text on city limit "City\nBadAibling" |
| `type` | string | required |  |  | Type identifier according to country code   or "-1" / "none". See extra document. |
| `unit` | [e\_unit](../16_annexes/map_uml_data_types.html#top-EAID_34376D30_4A82_46e3_9ADC_BCD136B920FF) | optional |  |  | Unit of @value |
| `value` | double | optional |  |  | Value of the signal, if value is given, unit is mandatory |
| `width` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Width of the signal’s bounding box.  @width is defined in the local coordinate system u/v along the v-axis |
| `zOffset` | double | required | m |  | z-offset of signal’s origin relative to the elevation of the road reference line |

**XML example**

```
<signals>
    <signal s="3981.4158159146"
            t="-14.0503"
            id="5000162"
            name="Vorschriftzeichen"
            dynamic="no"
            orientation="+"
            zOffset="3.8835"
            country="DE"
            countryRevision="2017"
            type="274"
            subtype="100"
            value="100"
            unit="km/h"
            height="0.77"
            width="0.77"
            hOffset="5.7595865">
    </signal>
</signals>
```

**Rules**

The following rules apply to signals:

* [asam.net:xodr:1.7.0:road.signal.signal\_type](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-signal-type): Signals shall have a specific type and subtype.

* [asam.net:xodr:1.7.0:road.signal.priority](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-priority): If present, signals shall be used in priority to other traffic rules.

* [asam.net:xodr:1.7.0:road.signal.use\_country\_code](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-use-country-code): A country code shall be added to refer to country-specific rules using the @country attribute.

* The year the traffic rules come into force may be specified in the @countryRevision attribute.
* Signals may be valid for one direction or both directions.
* Signals may be dynamic or static.
* Signals without @invalidated shall default to @invalidated=false.
* A signal’s placement may either be temporary or permanent, as indicated by @temporary.
* Omitting @temporary shall default to @temporary="false".
* Traffic actors should ignore objects with @invalidated="true".
* Omitting @invalidated shall default to @temporary="false".

**Related topics**

* [Section 11.9, "Lane road markings"](../11_lanes/11_09_lane_road_markings.html#top-fc59db56-70c8-4320-a8c7-213379f8c037)
* [Section 13.1, "Introduction to objects"](../13_objects/13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.2.1, "Object marking on outlines"](../13_objects/13_02_object_outline.html#sec-c25542c0-f80d-4da9-a430-020474b58301)
* [Section 10.1, "Introduction to roads"](../10_roads/10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)
* [Section 14.6, "Signal Controllers"](14_06_controllers.html#top-bb3b8324-47ba-4c80-aee7-a4a443cd0ef3)