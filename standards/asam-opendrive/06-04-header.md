# ASAM OpenDRIVE® v1.9.0 — 6.4 Header

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/06_general_architecture/06_04_header.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 6.4 Header

## 6.4.1. `<header>` element

The header is the very first element within the `<OpenDRIVE>` element.
It is a mandatory element and contains general information about the ASAM OpenDRIVE® file, for example version of the ASAM OpenDRIVE® or default regulations.

![img](../_images/uml_class_diagrams/EAID_8ED3471B_7252_4771_ADDB_FFD1ACE9AA18.png)

Figure 5. UML class diagram of the Header class

[Figure 5](#fig-b002bcdd-898e-4534-9268-19b7c8ace791) shows the UML class diagram of the ASAM OpenDRIVE® Header class.

In ASAM OpenDRIVE®, the general information is represented by the `<header>` element.

```
UML class: t_header
XML tag:   <header>
```

Contains general information about the ASAM OpenDRIVE® file

Table 8. Attributes of the <header> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `date` | string | optional |  | Time/date of database creation according to ISO 8601 (preference: YYYY-MM-DDThh:mm:ss) |
| `east` | double | optional | m | Maximum inertial x value |
| `name` | string | optional |  | Database name |
| `north` | double | optional | m | Maximum inertial y value |
| `revMajor` | integer | required |  | Major revision number of OpenDRIVE format |
| `revMinor` | integer | required |  | Minor revision number of OpenDRIVE format; 6 for OpenDrive 1.6 |
| `south` | double | optional | m | Minimum inertial y value |
| `vendor` | string | optional |  | Vendor name |
| `version` | string | optional |  | Version of this road network |
| `west` | double | optional | m | Minimum inertial x value |

|  |  |
| --- | --- |
|  | The `<geoReference>` and `<offset>` elements are explained in  [Section 8.5, "Georeferencing"](../08_coordinate_systems/08_05_geo_referencing.html#top-3535a746-e0af-4020-b71c-3a94e7a855a1). |

## 6.4.2. `<license>` element

```
UML class:  t_license
XML tag:    <license> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Licensing information about the OpenDRIVE file.

Table 9. Attributes of the <license> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `name` | string | required | 1.8.0 | The full name of the license. Informational only. |
| `resource` | string | optional | 1.8.0 | Link to an URL where the full license text can be found. |
| `spdxid` | string | optional | 1.8.0 | The identifier of the license from the [SPDX license list](https://spdx.org/licenses/). Can also be an SPDX License Expression, which is also applicable to custom licenses (LicenseRef-…​). |
| `text` | string | optional | 1.8.0 | The full license text. |

## 6.4.3. `<defaultRegulations>` element

```
UML class:  t_header_defaultRegulations
XML tag:    <defaultRegulations> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Defines the default regulations.
In each country there are different speed limits to a rural road.
For example a rural road has a speed limit of 100km/h in Germany and 80km/h in the Netherlands.

In some countries, one is allowed to turn right at a red traffic light; in others, one is not.
Instead of writing this for each road or each signal, the default regulations can be specified once in the header for the entire ASAM OpenDRIVE® file.
The default driving regulations can be overwritten with road, lane, or signal definitions.

### 6.4.3.1. `<roadRegulations>` element

```
UML class:  t_header_roadRegulation
XML tag:    <roadRegulations> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Defines the default regulations for different road types.

Table 10. Attributes of the <roadRegulations> element


| Name | Type | Use | Introduced |
| --- | --- | --- | --- |
| `type` | [e\_roadType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_3A3FB3DD_D0CF_43a7_95D6_30D9D024D0D9) | required | 1.8.0 |

### 6.4.3.2. `<signalRegulations>` element

```
UML class:  t_header_signalRegulation
XML tag:    <signalRegulations> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Defines the default regulations for signs in different countries, for example, if it is allowed to turn right when a red traffic light appears.

Table 11. Attributes of the <signalRegulations> element


| Name | Type | Use | Introduced |
| --- | --- | --- | --- |
| `subtype` | string | required | 1.8.0 |
| `type` | string | required | 1.8.0 |

|  |  |
| --- | --- |
|  | The `<semantics>` element is explained in  [Section 14.8, "Signal semantics"](../14_signals/14_08_signal_semantics.html#top-ac3b27c3-c3ac-49cf-bdaf-c52177f1dcee). |

**XML example**

```
<OpenDRIVE>
    <header revMajor="1"
            revMinor="5"
            name=""
            version="1.00"
            date="Mon Nov 29 12:59:50 2021"
            north="0.0000000000000000e+00"
            south="0.0000000000000000e+00"
            east="0.0000000000000000e+00"
            west="0.0000000000000000e+00">
        <defaultRegulations>
            <roadRegulations type="motorway">
                <semantics>
                    <speed type="maximum" value="120" unit="km/h"/>
                </semantics>
            </roadRegulations>
            <roadRegulations type="rural">
                <semantics>
                    <speed type="maximum" value="50" unit="km/h"/>
                </semantics>
            </roadRegulations>
            <roadRegulations type="town">
                <semantics>
                    <speed type="maximum" value="30" unit="km/h"/>
                </semantics>
            </roadRegulations>
            <roadRegulations type="livingStreet">
                <semantics>
                    <speed type="maximum" value="5" unit="km/h"/>
                </semantics>
            </roadRegulations>
            <signalRegulations type="1000001" subType="-1">
                <semantics>
                    <priority type="turnOnRedAllowed" />
                </semantics>
            </signalRegulations>
        </defaultRegulations>
    </header>
</OpenDRIVE>
```

**Rules**

* [asam.net:xodr:1.8.0:defaultRegulations.only\_speed\_priority](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-defaultRegulations-only-speed-priority): Only `<speed>` and `<priority>` elements shall be used within the `<defaultRegulations>` element.

* The `<signalRegulations>` element shall be used for signs that result in different driving rules.
* `<signalRegulations>` elements shall not be used as a signal catalogue.