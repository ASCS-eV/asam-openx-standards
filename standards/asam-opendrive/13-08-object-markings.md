# ASAM OpenDRIVE® v1.9.0 — 13.8 Object markings

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_08_object_markings.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.8 Object markings

Object marking describes the line-based road markings of any objects like crosswalks and parking spaces.

Object-based road markings can be defined by:

* using closed outlines with @fillType = "paint" to create filled-in areas
* using outlines with a `<markings>` element to create lines without fill.

See  [Section 13.2, "Object outline"](13_02_object_outline.html#top-67295042-9707-4ad5-9671-b80cde49bb3a) for more information on object outlines.

An object marking is defined either in accordance to the bounding volume of the element or by referencing outline points of the object.
When referencing outline points, use the `<markings>` element inside one of the object’s `<outline>` elements.
Otherwise, use the `<markings>` element inside `<object>` element.

The `<markings>` element serves as a wrapper for the `<marking>` element, which contains further information about the marking.

In addition to the road markings defined in this section, ASAM OpenDRIVE® also supports the following use cases:

* For the outer marking lines of a lane, use lane road markings.
  See  [Section 11.9, "Lane road markings"](../11_lanes/11_09_lane_road_markings.html#top-fc59db56-70c8-4320-a8c7-213379f8c037).
* Road markings that do not represent the line at the outer border of a lane but guide driver and traffic models are defined as signals.
  These may optionally be accompanied by objects, for example in the case of stop lines related to a traffic light.
  See  [Section 14.1, "Introduction to signals"](../14_signals/14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a).

## 13.8.1 Elements in UML model

### 13.8.1.1. `<markings>` element

In ASAM OpenDRIVE®, the markings of objects are represented by the `<marking>` object:

* within the `<object>` element when using the object’s bounding volume
* within the related `<outline>` element when referencing outline points

```
UML class: t_road_objects_object_markings
XML tag:   <markings> (Multiplicity: 0..1)
```

Object markings are road markings of any objects, for example, crosswalks and parking spaces.

### 13.8.1.2. `<marking>` element

In ASAM OpenDRIVE®, a single marking is represented by the `<marking>` element within the `<markings>` element.

```
UML class: t_road_objects_object_markings_marking
XML tag:   <marking> (Multiplicity: 1..*)
```

Specifies a marking that is either attached to one side of the object bounding volume or referencing outline points.

Table 99. Attributes of the <marking> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `color` | [e\_roadMarkColor](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_B67AEB84_154B_4c53_979E_7F1EA9751C9E) | required |  | Color of the marking |
| `lineLength` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | required | m | Length of the visible part |
| `side` | [e\_sideType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_41CC10F3_DCBB_4d99_A542_421B9C6015D5) | optional |  | Side of the bounding volume described in `<object>` element in the local coordinate system u/v. For example, used for objects with @type = parkingSpace. |
| `spaceLength` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Length of the gap between the visible parts |
| `startOffset` | double | required | m | Lateral offset in u-direction from start of bounding box side where the first marking starts |
| `stopOffset` | double | required | m | Lateral offset in u-direction from end of bounding box side where the marking ends |
| `weight` | [e\_roadMarkWeight](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_239940A3_B976_4a17_BD54_8252EACCC1FD) | optional |  | Optical "weight" of the marking |
| `width` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m | Width of the marking |
| `zOffset` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m | Height of road marking above the road, i.e. thickness of the road marking |

### 13.8.1.3. `<cornerReference>` element

In ASAM OpenDRIVE®, a corner reference is represented by the `<cornerReference>` element within the `<marking>` element.

```
UML class: t_road_objects_object_markings_marking_cornerReference
XML tag:   <cornerReference> (Multiplicity: 0..*)
```

Specifies a point by referencing an existing outline point.

Table 100. Attributes of the <cornerReference> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | nonNegativeInteger | required | Identifier of the referenced outline point |

## 13.8.2 Example using the bounding volume

The marking may be defined for a straight line on two sides of the object’s bounding volume.
For this purpose, the @side attribute of the `<marking>` element is used.

**XML example**

```
<objects>
  <object type="parkingSpace" subtype="closed" id="0" s="10.0" t="-5.5" zOffset="0.0" orientation="none" length="5.0" width="2.5" height="4.0" hdg="1.57" pitch="0.0" roll="0.0">
    <parkingSpace access="all"/>
    <markings>
      <marking side="left" width="0.1" color="white" zOffset="0.005" spaceLength="0.0" lineLength="1.0" startOffset="0.0" stopOffset="0.0"/>
      <marking side="right" width="0.1" color="white" zOffset="0.005" spaceLength="0.0" lineLength="1.0" startOffset="0.0" stopOffset="0.0"/>
    </markings>
  </object>
  <!-- [...] -->
</objects>
```

## 13.8.3 Example referencing outline points

![img](../_images/13_objects/object_9.png)

Figure 124. Crosswalk in ASAM OpenDRIVE®

[Figure 124](#fig-3df4f0dc-d06a-4a7e-80e6-d4c1e0028349) shows how a crosswalk with exemplary size is modeled.

The marking may be defined for a straight line from one outline point to another by referencing the ID of the respective outline points.
For this purpose, the `<cornerReference>` element inside the `<marking>` element is used.

**XML example**

```
<objects>
    <object type="crosswalk"
            id="10"
            s="10.0"
            t="0.0"
            zOffset="0.0"
            orientation="none"
            length="10.0"
            width="7.0"
            hdg="0.0"
            pitch="0.0"
            roll="0.0">
        <outlines>
            <outline id="0">
                <cornerRoad s="5.0" t="3.5" dz="0.0" height="4.0" id="0"/>
                <cornerRoad s="8.0" t="-3.5" dz="0.0" height="4.0" id="1"/>
                <cornerRoad s="12.0" t="-3.5" dz="0.0" height="4.0" id="2"/>
                <cornerRoad s="15.0" t="3.5" dz="0.0" height="4.0" id="3"/>
                <markings>
                    <marking width="0.1"
                            color="white"
                            zOffset="0.005"
                            spaceLength ="0.05"
                            lineLength ="0.2"
                            startOffset="0.0"
                            stopOffset="0.0">
                        <cornerReference id="0"/>
                        <cornerReference id="1"/>
                    </marking>
                    <marking width="0.1"
                            color="white"
                            zOffset="0.005"
                            spaceLength ="0.05"
                            lineLength ="0.2"
                            startOffset="0.0"
                            stopOffset="0.0">
                        <cornerReference id="2"/>
                        <cornerReference id="3"/>
                    </marking>
                </markings>
            </outline>
        </outlines>
    </object>
</objects>
```

**Rules**

The following rules apply to object marking elements:

* [asam.net:xodr:1.7.0:road.object.marking.colour](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-marking-colour): The color of the marking shall be defined.

* [asam.net:xodr:1.9.0:road.object.marking.markings\_without\_outline](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-marking-markings-without-outline): If no outline is used, the `<markings>` element shall be inside the `<object>` element.

* [asam.net:xodr:1.7.0:road.object.marking.no\_outline\_side\_attr](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-marking-no-outline-side-attr): If no outline is used, the @side attribute is mandatory.

* [asam.net:xodr:1.7.0:road.object.marking.no\_cornerreference\_if\_no\_outline](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-marking-no-cornerreference-if-no-outline): If no outline is used, the `<cornerReference>` element cannot be used.

* [asam.net:xodr:1.9.0:road.object.marking.markings\_with\_outline](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-marking-markings-with-outline): If an outline is used, any `<markings>` element shall be inside an `<outline>` element.

* [asam.net:xodr:1.9.0:road.object.marking.complete\_or\_partial\_on\_outline](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-marking-complete-or-partial-on-outline): The marking of an object with an `<outlines>` element shall either completely or partially be defined on one of its outlines.

* [asam.net:xodr:1.7.0:road.object.marking.outline\_corner\_reference\_count](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-marking-outline-corner-reference-count): If an outline is used, at least two `<cornerReference>` elements are mandatory.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.2, "Object outline"](13_02_object_outline.html#top-67295042-9707-4ad5-9671-b80cde49bb3a)
* [Section 13.9, "Object borders"](13_09_object_borders.html#top-f4d6c702-996e-4344-8e80-e580ea6ca767)