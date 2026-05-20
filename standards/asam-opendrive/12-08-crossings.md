# ASAM OpenDRIVE® v1.9.0 — 12.8 Crossings

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_08_crossings.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.8 Crossings

Crossings are junctions where traffic of two or more different roads crosses at the same level, but the traffic cannot change the roads at crossings.

Crossings are intended as best practice, for example, for the following use cases:

* Railroad crossings
* Pedestrian crossings
* Bicycle crossings

Crossings are similar to virtual junctions from the driving point of view, but without any connections.
Elevation definitions via CRG or elevation grid are possible.

**Elements in UML model**

**`<junction type="crossing">` element**

In ASAM OpenDRIVE®, crossings are represented by `<junction>` elements with the value `crossing` in the @type attribute within the `<OpenDRIVE>` element.

```
UML class:  t_junction_crossing
XML tag:    <junction type="crossing"> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Crossings are junctions without connecting roads.
They define sections where crossing traffic can appear.
Traffic does not change roads at crossings, for example, at railway crossings.

Table 74. Attributes of the <junction type="crossing"> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | ID of the junction to which the road belongs, for example connecting roads, cross paths, and roads of a junction boundary. Use -1 for none. |
| `name` | string | optional | Name of the junction. May be chosen freely. |
| `type` | [e\_junction\_type](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_40D9549F_DB59_4440_A889_A09659446ED6) | required | Crossings must be of type "crossing". |

**`<roadSection>` element**

In ASAM OpenDRIVE®, the ranges with possible crossing traffic at crossings are represented by `<roadSection>` elements within the `<junction>` element.

```
UML class:  t_junction_roadSection
XML tag:    <roadSection> (Multiplicity: 1..*)
Introduced: 1.8.0
```

Define the s range of the crossing roads with possible crossing traffic.

Table 75. Attributes of the <roadSection> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `id` | string | required | 1.8.0 | Unique ID within the junction |
| `roadId` | string | required | 1.8.0 | ID of the road of this roadSection element |
| `sEnd` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | 1.8.0 | End position of the crossing junction in the road reference line coordinate system. This attribute is mandatory for crossing junctions. |
| `sStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | 1.8.0 | Start position of the crossing junction in the road reference line coordinate system. This attribute is mandatory for crossing junctions. |

**XML example**

![img](../_images/12_junctions/crossing_rail.png)

Figure 96. Example of a crossing with a railroad track

[Figure 96](#fig-9d5b81e2-9636-493e-a6ac-8548c2dcbf58) shows a crossing of the roads with @id="1" and @id="2".
The road with @id="1" is for normal traffic and uses lanes with @type="driving".
The road with @id="2" is a railroad track and uses a lane with @type="rail".
Traffic on the road with @id="2" has priority.
For both roads `<roadSection>` elements define with the values of the @sStart and @sEnd attributes the section where traffic crosses.

```
<road name="DrivingRoad1" length="200" id="1" junction="-1">
    <laneSection s="0.0000000000000000e+00">
        <left>
            <lane id="1" type="driving"/>
        </left>
        <center/>
        <right>
            <lane id="-1" type="driving"/>
        </right>
    </laneSection>
</road>
<road name="RAILRoad" length="2300" id="2" junction="-1">
    <laneSection s="0.0000000000000000e+00">
        <left/>
        <center/>
        <right>
            <lane id="-1" type="rail"/>
        </right>
    </laneSection>
</road>
...
<junction name="myRailCrossing" type="crossing" id="555">
    <priority high="2" low="1"/>
    <roadSection id="0" roadId="1" sStart="50" sEnd="60"/>
    <roadSection id="1" roadId="2" sStart="150" sEnd="160"/>
</junction>
```

**Rules**

The following rules apply to crossings:

* [asam.net:xodr:1.8.0:junctions.crossing.only\_road\_sections](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-crossing-only-road-sections): Junctions with @type="crossing" shall only have `<roadSection>` elements.

* [asam.net:xodr:1.8.0:junctions.crossing.only\_one\_high\_prio](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-crossing-only-one-high-prio): Only one road defined by the @roadId attributes of the `<roadSection>` elements shall have `high` priority.

* [asam.net:xodr:1.8.0:junctions.crossing.s\_start\_end\_coverage](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-crossing-s-start-end-coverage): The values for the @sStart and @sEnd attributes of the `<roadSection>` elements shall at least cover the area where the roads overlap.

* Currently only flat crossings can be modeled.

**Related topics**

* [Section 12.5, "Cross paths"](12_05_cross_paths.html#top-6ac8a5ea-45ca-4a28-97e3-711deec5c792)
* [Section 12.7.1, "Cross paths with virtual junctions"](12_07_virtual_junctions.html#sec-eaa19a5b-a1de-4002-bc9d-f9ac4d39f839)