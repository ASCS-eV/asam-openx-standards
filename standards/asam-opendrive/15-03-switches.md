# ASAM Opendrive v1.9.0 — 15.3 Switches

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/15_railroads/15_03_switches.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 15.3 Switches

Rail-bound vehicles use switches to change their tracks.
In contrast to junctions, a switch can guide the vehicles into two directions only.

There are two different types of switches:

* Dynamic switches split the railroad track into two tracks leading in two directions.
  Dynamic switches can be changed during the simulation.
* Static switches split the railroad track into two tracks leading in two directions and have the two variants `straight` and `turn`.
  Static switches cannot be changed during the simulation.

Switches may be placed at an arbitrary position on a main track.

![img](../_images/15_railroads/railroads_2.png)

Figure 145. Railroad switches

[Figure 145](#fig-a2f03594-1b25-42ac-9afc-589bbc0fba12) shows the two partner switches `12` and `32`.
A side track `2` connects the two main tracks `1` and `3`.

**Elements in UML model**

**`<switch>` element**

In ASAM OpenDRIVE, switches are represented by the `<switch>` element within the `<railroad>` element.

```
UML class: t_road_railroad_switch
XML tag:   <switch> (Multiplicity: 0..*)
```

Switches change the tracks for rail-bound vehicles.
Switches guide the vehicles into two directions only.

Table 147. Attributes of the <switch> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | Unique ID of the switch; preferably an integer number, see uint32\_t |
| `name` | string | required | Unique name of the switch |
| `position` | [e\_road\_railroad\_switch\_position](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_7B38FC66_AE1D_46eb_977F_06C8C68493CD) | required | Either a switch can be operated (dynamic) or it is in a static position |

**XML example**

```
<railroad>
    <switch name="ExampleSwitch12" id="12" position="dynamic">
        <mainTrack id="1" s="1.0000000000000000e+01" dir="+"/>
        <sideTrack id="2" s="0.0000000000000000e+00" dir="+"/>
        <partner name="ExampleSwitch32" id="32"/>
    </switch>
</railroad>
```

**Rules**

The following rules apply to switches:

* A switch may be either dynamic or static.

**Related topics**

* [Section 15.2, "Railroad tracks"](15_02_railroad_tracks.html#top-bd13c77a-7b58-416c-9449-7c1dcf43497e)
* [Section 15.3.1, “Main track”](#sec-c2acd458-27c6-48bf-983b-6c91a9feb1bd)
* [Section 15.3.2, “Side track”](#sec-3c7e5de0-490c-4148-9ef1-10cbc2fd7516)
* [Section 15.3.3, “Partner switches”](#sec-22a79a45-79b1-4f2b-aba9-4fa65211bf21)

## 15.3.1 Main track

A main track represents the main course for rail bound traffic.
A main track has the same properties as a side track.
The two track types have been implemented as a convenience function to simplify the modeling of tracks entering and coming out of switches.
[Figure 145](#fig-a2f03594-1b25-42ac-9afc-589bbc0fba12) shows a main track.

**Elements in UML model**

**`<mainTrack>` element**

In ASAM OpenDRIVE, main tracks are represented by the `<mainTrack>` element within the `<switch>` element.

```
UML class: t_road_railroad_switch_mainTrack
XML tag:   <mainTrack>
```

Main tracks form the primary course for rail bound traffic.

Table 148. Attributes of the <mainTrack> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `dir` | [e\_elementDir](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D1E21B53_3817_4627_8EC7_24415D264892) | required |  | direction, relative to the s-direction, on the main track for entering the side track via the switch |
| `id` | string | required |  | Unique ID of the main track, that is, the `<road>` element. Must be consistent with parent containing this `<railroad>` element. |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of the switch, that is, the point where main track and side track meet |

**Rules**

The following rules apply to main tracks:

* [asam.net:xodr:1.7.0:road.railroad.switch.check\_switch\_conn](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-switch-check-switch-conn): Main tracks shall not be used to connect two switches.

**Related topics**

* [Section 15.3.2, “Side track”](#sec-3c7e5de0-490c-4148-9ef1-10cbc2fd7516)
* [Section 15.3.3, “Partner switches”](#sec-22a79a45-79b1-4f2b-aba9-4fa65211bf21)

## 15.3.2 Side track

A side track connects two switches that are placed on main tracks.
A side track has the same properties as a main track.
The two track types have been implemented as convenience function to simplify the modeling of tracks entering and coming out of switches.

[Figure 145](#fig-a2f03594-1b25-42ac-9afc-589bbc0fba12) shows a side track.

**Elements in UML model**

**`<sideTrack>` element**

In ASAM OpenDRIVE, side tracks are represented by the `<sideTrack>` element within the `<switch>` element.

```
UML class: t_road_railroad_switch_sideTrack
XML tag:   <sideTrack>
```

Side tracks connect two switches that are placed on main tracks.

Table 149. Attributes of the <sideTrack> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `dir` | [e\_elementDir](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D1E21B53_3817_4627_8EC7_24415D264892) | required |  | direction, relative to the s-direction, on the side track for after entering it via the switch |
| `id` | string | required |  | Unique ID of the side track, that is, the `<road>` element |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of the switch on the side track |

**Rules**

The following rules apply to side tracks:

* Side tracks shall be used to link two switches only.

**Related topics**

* [Section 15.3.1, “Main track”](#sec-c2acd458-27c6-48bf-983b-6c91a9feb1bd)
* [Section 15.3.3, “Partner switches”](#sec-22a79a45-79b1-4f2b-aba9-4fa65211bf21)

## 15.3.3 Partner switches

For convenience reasons, two switches may be declared partner switches.
This describes a connection between two switches that are linked by a side track.
These two switches need to be set consistently.
[Figure 145](#fig-a2f03594-1b25-42ac-9afc-589bbc0fba12) shows the partner switches `12` and `32`.

**Elements in UML model**

**`<partner>` element**

In ASAM OpenDRIVE, partner switches are represented by the `<partner>` element within the `<switch>` element.

```
UML class: t_road_railroad_switch_partner
XML tag:   <partner> (Multiplicity: 0..1)
```

Partner switches are two consistently set switches linked by a side track.

Table 150. Attributes of the <partner> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | Unique ID of the partner switch |
| `name` | string | optional | Unique name of the partner switch |

**Rules**

The following rules apply to partner switches:

* Partner switches shall be used to indicate that a side track links two switches.

* [asam.net:xodr:1.7.0:road.railroad.switch.single\_switch\_no\_partner](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-switch-single-switch-no-partner): Single switches do not have partner switches.

**Related topics**

* [Section 15.3.1, “Main track”](#sec-c2acd458-27c6-48bf-983b-6c91a9feb1bd)
* [Section 15.3.2, “Side track”](#sec-3c7e5de0-490c-4148-9ef1-10cbc2fd7516)