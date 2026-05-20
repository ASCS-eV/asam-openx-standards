# ASAM OpenDRIVE® v1.9.0 — 14.7 Signal boards

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_07_signal_boards.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.7 Signal boards

Signals are not always separate signs on a single sheet of metal.
Several signs can be coupled on one board.
They can be of the following types:

* static board of @type="staticBoard"
* variable message board of @type="vmsBoard"
* multi board with static and dynamic parts of @type="multiBoard"

## 14.7.1 Static boards

**Elements in UML model**

**`<staticBoard>` element**

```
UML class:  t_road_signals_staticBoard
XML tag:    <staticBoard> (Multiplicity: 0..*)
Introduced: 1.8.0
```

A `<signal>` element that contains a `<staticBoard>` element.
The signs that are displayed on a static board are defined as separate `<sign>` elements.

**`<sign>` element**

```
UML class:  t_road_signals_board_sign
XML tag:    <sign> (Multiplicity: 0..*)
Introduced: 1.8.0
```

A `<sign>` element on a static board defined in the local coordinate system of the `<signal>` element.
A `<sign>` element may have all attributes and child elements of a signal.

Table 130. Attributes of the <sign> element


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
| `subtype` | string | required |  |  | Subtype identifier according to country code or "-1" / "none" |
| `temporary` | boolean | optional |  | 1.9.0 | Indicates whether the signal is temporary or permanent. Example: temporary speed limit sign in road works situation. |
| `text` | string | optional |  |  | Additional text associated with the signal, for example, text on city limit "City\nBadAibling" |
| `type` | string | required |  |  | Type identifier according to country code   or "-1" / "none". See extra document. |
| `unit` | [e\_unit](../16_annexes/map_uml_data_types.html#top-EAID_34376D30_4A82_46e3_9ADC_BCD136B920FF) | optional |  |  | Unit of @value |
| `v` | double | required | m | 1.8.0 | Local v-coordinate of the sign on the board |
| `value` | double | optional |  |  | Value of the signal, if value is given, unit is mandatory |
| `width` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Width of the signal’s bounding box.  @width is defined in the local coordinate system u/v along the v-axis |
| `z` | double | required | m | 1.8.0 | Local z-coordinate of the sign on the board |

**XML example**

```
<signal s="4.0"
        t="1.0"
        id="534"
        name="board"
        dynamic="no"
        orientation="+"
        zOffset="5.00"
        country="OpenDRIVE"
        type="staticBoard"
        subtype="-1"
        hOffset="0"
        pitch="0"
        roll="0"
        height="2.0"
        width="1.5">
    <validity from="-2" to="-2"/>
    <staticBoard>
        <sign id="535" Country="DE" type="274" subtype="60" countryRevision="2017" v="-0.5" z="1.5" width="0.5" height="0.5" value="60" unit="km/h">
            <validity from="-2" to="-2"/>
            <signalDependency id ="536"/>
            <signalDependency id ="537"/>
        </sign>
        <sign id="536" Country="DE" type="1010" subtype="51" countryRevision="2017" v="-0.75" z="0.9" width="0.420" height="0.231"/>
        <sign id="537" Country="DE" type="1040" subtype="30" countryRevision="2017" v="-0.75" z="0.6" width="0.420" height="0.231" value="22000600"/>
        <sign id="538" Country="DE" type="1012" subtype="36" countryRevision="2017" v="-0.75" z="0.3" width="0.420" height="0.231"/>
        <sign id="539" Country="DE" type="274" subtype="80" countryRevision="2017" v="0.75" z="1.5" width="0.420" height="0.231" value="100" unit="km/h">
            <signalDependency id ="540" />
        </sign>
        <sign id="540" Country="DE" type="1040" subtype="30" countryRevision="2017" v="-0.75" z="0.6" width="0.420" height="0.231" value="22000600"/>
        <sign id="541" Country="DE" type="1012" subtype="36" countryRevision="2017" v="-0.75" z="0.3" width="0.420" height="0.231"/>
    </staticBoard>
 </signal>
```

![img](../_images/14_signals/fig_multistaticsign.png)

Figure 138. multiStaticSign from XML example above

**Rules**

* [asam.net:xodr:1.8.0:road.signal.boards.static\_board\_use\_correct\_type](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-signal-boards-static-board-use-correct-type): Static signal boards shall be specified to be @type="staticBoard".

* Static signal boards shall be specified to be @dynamic="false".
* The `<validity>` element of a `<sign>` element shall override the `<validity>` element of the parent `<signal>` element.
* The `<signalDependency>` element of a `<sign>` element shall override the `<signalDependency>` element of the parent `<signal>` element.

* [asam.net:xodr:1.9.0:road.signal.boards.static\_boards\_no\_single\_signal](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-signal-boards-static-boards-no-single-signal): Static boards shall not be used for single signals, for example, a stop sign on a single sheet of metal.

**Related topics**

* [Section 14.3, "Signal dependency"](14_03_signal_dependency.html#top-f4d8bdcc-3f58-454d-b14e-801a880d9c41)
* [Section 14.4, "Signal reference"](14_04_signal_reference.html#top-1030e9ff-6b75-4353-b2b4-043f08c02a2d)
* [Section 14.8, "Signal semantics"](14_08_signal_semantics.html#top-ac3b27c3-c3ac-49cf-bdaf-c52177f1dcee)
* [Section 14.7.2, “Variable message boards (VMS)”](#sec-cb990f03-1e06-4f31-a9df-6cb910f2376a)
* [Section 14.7.3, “Multi boards”](#sec-3a012f70-b671-4287-946c-f8caa3b58c3f)
* [Section 14.7.4, “Gantry”](#sec-6301c5c6-a389-4386-b227-06946186a29a)

## 14.7.2 Variable message boards (VMS)

**Elements in UML model**

**`<vmsBoard>` element**

```
UML class:  t_road_signals_vmsBoard
XML tag:    <vmsBoard> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Variable message boards can change their values during the simulation in ASAM OpenSCENARIO.

Variable message boards are switched off if they are not specified in ASAM OpenSCENARIO.

Table 131. Attributes of the <vmsBoard> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `displayHeight` | double | optional | m | 1.8.0 | Height of the display |
| `displayType` | [e\_road\_signals\_displayType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_0F33D4CC_5E43_48e1_BB2F_BCBB61F268A8) | required |  | 1.8.0 | Functional type of the display |
| `displayWidth` | double | optional | m | 1.8.0 | Width of the display |
| `v` | double | required | m | 1.8.0 | Local v-coordinate of the board |
| `z` | double | required | m | 1.8.0 | Local z-coordinate of the board |

**`<displayArea>` element**

```
UML class:  t_road_signals_displayArea
XML tag:    <displayArea> (Multiplicity: 0..*)
Introduced: 1.8.0
```

A display area is the recommended position of the signal to be visualized in the simulation.
A display area is specified in the `<displayArea>` element.
A `<displayArea>` element is defined in the local coordinate system of the `<signal>` element.
The @index attribute can be used in ASAM OpenSCENARIO to reference the display area.
In ASAM OpenSCENARIO a different local display area position may be specified.

Table 132. Attributes of the <displayArea> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `height` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | 1.8.0 | Height of the `<displayArea>` |
| `index` | int | required |  | 1.8.0 | Index of the `<displayArea>` |
| `v` | double | required | m | 1.8.0 | Local v-coordinate of the `<displayArea>` on the board |
| `width` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | 1.8.0 | Width of the `<displayArea>` |
| `z` | double | required | m | 1.8.0 | Local z-coordinate of the `<displayArea>` on the board |

**XML example**

```
<signal s="4.0"
        t="1.0"
        id="534"
        name="board"
        dynamic="yes"
        orientation="+"
        zOffset="5.00"
        country="OpenDRIVE"
        type="vmsBoard"
        subtype="-1"
        hOffset="0"
        pitch="0"
        roll="0"
        height="1.5"
        width="1.5">
    <vmsBoard displayHeight="1.5" displayWidth="1.5" material="colorGraphics">
        <displayArea index="1" v="7" z="3" width="1.4" height="1.4">
            <validity from="-2" to="-2" />
        </displayArea>
        <displayArea index="2" v="5.5" z="3" width="1.4" height="1.4">
            <validity from="-2" to="-3" />
        </displayArea>
        <displayArea index="3" v="5.5" z="0.5" width="1.4" height="0.4" >
            <validity from="-3" to="-3" />
        </displayArea>
    </vmsBoard>
</signal>
```

**Rules**

* Variable message boards shall be specified to be @type="vmsBoard".
* Variable message boards shall be specified to be @dynamic="true".
* The `<validity>` element of a `<displayArea>` element shall override the `<validity>` element of the parent `<signal>` element.
* The `<signalDependency>` of a `<displayArea>` element shall override the `<signalDependency>` element of the parent `<signal>` element.

**Related topics**

* [Section 14.7.1, “Static boards”](#sec-87f0973f-f66c-4dbf-a893-e4684e3dd765)
* [Section 14.7.3, “Multi boards”](#sec-3a012f70-b671-4287-946c-f8caa3b58c3f)
* [Section 14.7.4, “Gantry”](#sec-6301c5c6-a389-4386-b227-06946186a29a)

## 14.7.3 Multi boards

A multi board is a board that consists of static boards and variable message boards.
The size of the parent `<signal>` element covers all static and variable message boards.

**XML example**

```
<signal s="4.0"
        t="1.0"
        id="534"
        name="board"
        dynamic="yes"
        orientation="+"
        zOffset="5.00"
        country="OpenDRIVE"
        type="multiBoard"
        subtype="-1"
        hOffset="0"
        pitch="0"
        roll="0"
        height="3.0"
        width="7.5">
    <vmsBoard displayHeight="2.5" displayWidth="7.0" material="colorGraphics" v="0" z="0.5">
        <displayArea index="1" v="7" z="3" width="1.4" height="1.4">
            <validity from="-2" to="-2" />
        </displayArea>
        <displayArea index="2" v="5.5" z="3" width="1.5" height="1.5">
            <validity from="-2" to="-3" />
        </displayArea>
        <displayArea index="3" v="5.5" z="0.5" width="1.5" height="0.5">
            <validity from="-3" to="-3" />
        </displayArea>
    </vmsBoard>
    <staticBoard>
        <sign id="535" country="DE" type="386" subtype="32" countryRevision="2017" v="-7" z="0.2" width="0.5" height="0.2">
            <validity from="-2" to="-2" />
        </sign>
        <sign id="535" country="DE" type="405" subtype="-1" countryRevision="2017" v="-5" z="0.2" width="0.5" height="0.2" text="66">
            <validity from="-2" to="-3" />
        </sign>
        <sign id="535" country="DE" type="386" subtype="32" countryRevision="2017" v="-3.5" z="0.2" width="0.5" height="0.2">
            <validity from="-3" to="-3" />
        </sign>
    </staticBoard>
</signal>
```

**Rules**

* [asam.net:xodr:1.8.0:road.signal.boards.multi\_board\_have\_sub\_boards](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-signal-boards-multi-board-have-sub-boards): A multi board shall have at least one static signal board and at least one variable message board.

* [asam.net:xodr:1.8.0:road.signal.boards.multi\_board\_use\_correct\_type](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-signal-boards-multi-board-use-correct-type): Multi boards shall be specified to be @type="multiBoard".

* [asam.net:xodr:1.8.0:road.signal.boards.multi\_board\_use\_dynamic\_true](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-signal-boards-multi-board-use-dynamic-true): Multi boards shall be specified to be @dynamic="true".

**Related topics**

* [Section 14.7.1, “Static boards”](#sec-87f0973f-f66c-4dbf-a893-e4684e3dd765)
* [Section 14.7.2, “Variable message boards (VMS)”](#sec-cb990f03-1e06-4f31-a9df-6cb910f2376a)
* [Section 14.7.4, “Gantry”](#sec-6301c5c6-a389-4386-b227-06946186a29a)

## 14.7.4 Gantry

**Elements in UML model**

**`<vmsGroup>` element**

```
UML class:  t_signalGroup_vmsGroup
XML tag:    <vmsGroup> (Multiplicity: 0..*)
Introduced: 1.8.0
```

On a gantry there can be one large variable message board or several smaller variable message boards.
ASAM OpenSCENARIO requires to treat a gantry that has one large variable message board or several smaller variable message boards the same way.
Therefore variable message boards that are on the same gantry shall be grouped and their indexes shall be redefined if not unique.

Table 133. Attributes of the <vmsGroup> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `id` | string | required | 1.8.0 | Unique id of the `<vmsGroup>` |

![img](../_images/uml_class_diagrams/EAID_58914C14_7C50_4f5c_85C2_C0D20AA0A0B0.png)

Figure 139. UML class diagram of the SignalGroup class

[Figure 139](#fig-4f762530-d9dc-4be1-9181-beb86f9b3443) shows the UML class diagram of the ASAM OpenDRIVE® SignalGroup class.

**`<vmsBoardReference>` element**

```
UML class:  t_signalGroup_vmsBoardReference
XML tag:    <vmsBoardReference> (Multiplicity: 1..*)
Introduced: 1.8.0
```

Variable message board references list all variable message boards that belong to the same gantry.

Table 134. Attributes of the <vmsBoardReference> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `groupIndex` | int | required | 1.8.0 | groupIndex the index of the grouped boards shall be unique within the `<vmsGroup>` |
| `signalId` | string | required | 1.8.0 | Id of the signal that has a `<vmsBoard>` assigned |
| `vmsIndex` | int | required | 1.8.0 | vmsIndex, the index of the `<vmsBoard>` |

**XML example**

```
<vmsGroup id="27" >
    <vmsBoardReference signalId="501" vmsIndex="1" groupIndex="1" />
    <vmsBoardReference signalId="502" vmsIndex="1" groupIndex="2" />
    <vmsBoardReference signalId="503" vmsIndex="1" groupIndex="3" />
</vmsGroup>
```

**Rules**

* [asam.net:xodr:1.9.0:road.signal.gantry.vmsgroup\_at\_least\_one\_reference](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-signal-gantry-vmsgroup-at-least-one-reference): Each gantry shall have one `<vmsGroup>` element with at least one `<vmsBoardReference>` element.

* [asam.net:xodr:1.9.0:road.signal.gantry.all\_variable\_boards\_same\_gantry](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-signal-gantry-all-variable-boards-same-gantry): All variable message boards within a `<vmsGroup>` element shall belong to the same gantry.

**Related topics**

* [Section 14.7.1, “Static boards”](#sec-87f0973f-f66c-4dbf-a893-e4684e3dd765)
* [Section 14.7.2, “Variable message boards (VMS)”](#sec-cb990f03-1e06-4f31-a9df-6cb910f2376a)
* [Section 14.7.3, “Multi boards”](#sec-3a012f70-b671-4287-946c-f8caa3b58c3f)