# ASAM Opendrive v1.9.0 — 14.4 Signal reference

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_04_signal_reference.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.4 Signal reference

Signal reference means that there is some kind of link between two signals or objects.
A signal reference is valid for one specific signal only.

**Elements in UML model**

**`<reference>` element**

In ASAM OpenDRIVE, a signal reference is represented by the `<reference>` element within the `<signal>` element.

```
UML class: t_road_signals_signal_reference
XML tag:   <reference> (Multiplicity: 0..*)
```

Signal references link a signal to another signal or object.
One signal may have multiple signal references.
The signal reference term should not to be confused with the `<signalReference>` element that is used to link a signal to multiple roads.

Table 125. Attributes of the <reference> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `elementId` | string | required | Unique ID of the linked element |
| `elementType` | [e\_road\_signals\_signal\_reference\_elementType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_719D83FA_FFE4_42e5_A475_7D5EEE7035BC) | required | Type of the linked element |
| `type` | string | optional | Type of the linkage   Free text, depending on application |

**XML example**

An example would be a traffic light which uses a `<reference>` to a stop line in order to specify where traffic participants have to stop on red.
The stop line in turn has a `<dependency>` on the traffic light, since traffic should stop there only if the traffic light is red.

```
<signals>
    <signal s="1.0e+00"
            t="-1.0e-01"
            id="5"
            name="pedestrian_trafficlight"
            dynamic="yes"
            orientation="+"
            zOffset="3.03"
            type="1000002"
            subtype="-1"
            country="OpenDRIVE"
            countryRevision="2023"
            hOffset="0.0"
            pitch="0.0"
            roll="0.0"
            height="0.53"
            width="0.27">
        <validity fromLane="-1" toLane="-1"/>
        <reference elementId="7" elementType="signal" type="stopline"/>
    </signal>
    <signal s="1.31e+01"
            t="0.0"
            id="7"
            name="InvisibleStopLine"
            dynamic="no"
            orientation="-"
            zOffset="0.0"
            type="1100001"
            subtype="-1"
            country="OpenDRIVE"
            countryRevision="2023"
            hOffset="0.0"
            pitch="0.0"
            roll="0.0"
            height="0.03"
            width="3.75">
        <validity fromLane="-1" toLane="-1"/>
        <dependency id="5" type="pedestrian_trafficlight"/>
    </signal>
</signals>
```

**Rules**

The following rules apply to signal reference elements:

* A signal may have multiple references.
* The type of reference is not specifically defined in ASAM OpenDRIVE and may be set in the application.

Rules regarding the type of reference are defined in the application and are not stored in ASAM OpenDRIVE.

**Related topics**

* [Section 13.1, "Introduction to objects"](../13_objects/13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 14.1, "Introduction to signals"](14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)
* [Section 14.3, "Signal dependency"](14_03_signal_dependency.html#top-f4d8bdcc-3f58-454d-b14e-801a880d9c41)