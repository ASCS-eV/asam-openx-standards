# ASAM Opendrive v1.9.0 — 14.3 Signal dependency

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_03_signal_dependency.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.3 Signal dependency

Signal dependency means that one signal controls the output of another signal.

**Elements in UML model**

**`<dependency>` element**

In ASAM OpenDRIVE, signal dependency is represented by the `<dependency>` element within the `<signal>` element.

```
UML class: t_road_signals_signal_dependency
XML tag:   <dependency> (Multiplicity: 0..*)
```

Signal dependencies limit or extend the validity of one signal by an additional signal.
For example, a speed limit sign of 60 km/h that is only valid for trucks, specified by a supplementary sign.
One signal may have multiple dependencies.

Table 124. Attributes of the <dependency> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | ID of the controlling signal |
| `type` | string | optional | Type of the dependency,   Free text, depending on application |

**XML example**

![img](../_images/14_signals/Signals_4.png)

Figure 133. Lane and type specific speed limit

[Figure 133](#fig-1ad6881b-550a-4505-9ee1-52ae5fbcf7bb) shows the dependency between the speed limit signal and the signal to make the lane valid for specific traffic participants only.

```
<signals>
    <signal s="50.0"
            t="-4.0"
            id="1"
            name="SpeedLimit60"
            dynamic="no"
            orientation="+"
            zOffset="1.90"
            type="274"
            country="DE"
            countryRevision="2013"
            subtype="56"
            value="60.0"
            unit="km/h"
            hOffset="0.0 "
            pitch="0.0"
            roll="0.0"
            height="0.61"
            width="0.61">
        <dependency id="2"/>
    </signal>
    <signal s="50.0"
            t="-4.0"
            id="2"
            name="LorriesOnly"
            dynamic="no"
            orientation="+"
            zOffset="1.56"
            type="1048"
            country="DE"
            countryRevision="2013"
            subtype="12"
            hOffset="0.0"
            pitch="0.0"
            roll="0.0"
            height="0.33"
            width="0.60">
    </signal>
</signals>
```

**Rules**

The following rules apply to dependency elements:

* [asam.net:xodr:1.7.0:road.signal.dependency.multiple\_dependency](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-dependency-multiple-dependency): A signal may have multiple dependencies.

* The type of dependency is not specifically defined in ASAM OpenDRIVE and may be set in the application.

Rules regarding the type of dependency are defined in the application and are not stored in ASAM OpenDRIVE.

**Related topics**

* [Section 14.1, "Introduction to signals"](14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)
* [Section 14.4, "Signal reference"](14_04_signal_reference.html#top-1030e9ff-6b75-4353-b2b4-043f08c02a2d)