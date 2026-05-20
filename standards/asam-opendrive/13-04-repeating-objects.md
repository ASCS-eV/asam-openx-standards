# ASAM Opendrive v1.9.0 — 13.4 Repeating objects

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_04_repeating_objects.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.4 Repeating objects

To avoid lengthy XML code, objects of the same type may be repeated using one or more `<repeat>` elements.
This element is mainly used to describe railings, railing posts, and street lamps.

Each `<repeat>` element specifies a section of repetition that starts at a given position (using @s and @tStart) and ends after a specified length (at @s + @length and @tEnd).
Sections do not need to be adjacent and are independent of each other.  
The t-coordinate for each s-coordinate between tStart and tEnd is interpolated

* using a parametric cubic polynomial based on @tStart, @bT, @cT, and @dT if at least one of the coefficients bT, cT, and dT are provided
* using a linear interpolation based on @tStart and @tEnd if none of the coefficients are provided

Within each section, the distance attribute defines how the object is repeated:

* If @distance is greater than 0, an instance of the object is repeatedly placed along the specified path as many time as the specified parameters of @distance and @length allow, rounded down.
* If @distance is set to 0, the object’s profile is instead extruded from the start to the end point, creating one continuous shape within this section.
  This is also called a "continuous object".

For `<repeat>` elements with @distance greater than 0, it is not possible or allowed to create an "incomplete" instance at the end of the provided @length attribute of the `<repeat>` element.
The origin of each instance placed in a section of repetition must be inside that section (including its border).
The dimensions of each instance (e.g. its bounding volume) may extend beyond that section on either end and shall not be cut off at any of the borders of the section.

The attributes of the repeated object (e.g. length, width, and height) may change within and between each section.
These changes have both a "Start" and an "End" setting (hereinafter also referred to as \*Start and \*End).
For example, the object attribute @width can be overwritten using @widthStart and @widthEnd.
If the attributes of the object differ from the ones defined in a `<repeat>` element, the `<repeat>` element takes precedence.
If \*Start and \*End have different values, the respective attribute of the object is interpolated from the start to the end of the zone of repetition.
Unless coefficients for a parametric cubic polynomial are provided, the interpolation mode is linear.
For more information on interpolation, see [Calculation](#sec-5a29ecb1-9b5f-4302-acce-71517109e4ea).  
Objects with an outline or a skeleton, however, may not change their dimensions within or between sections.

By default, the repetition follows the curvature of the road reference line.
If @detachFromReferenceLine is set to true, each section of repetition will instead be applied in a straight line from its start to its end position.

![img](../_images/13_objects/object_2.png)

Figure 120. Large angular continuous object with changing shape using a single `<repeat>` element

[Figure 120](#fig-9e8f61d7-f480-48c1-b65a-415e36f24d32) shows top and side views of a large angular continuous object extruded (@distance set to 0) along the specified path using a single `<repeat>` element.
The repetition starts at position (@s, @tStart, @zOffsetStart) and continues for a @length to the point (@s+@length, @tEnd, @zOffsetEnd).
Its width changes from @widthStart to @widthEnd.
Its height changes from @heightStart to @heightEnd.
Since this is a continuous repetition, the @lengthStart and @lengthEnd is ignored.

![img](../_images/13_objects/object_3.png)

Figure 121. Repeated small angular objects with changing shape using a single `<repeat>` element

[Figure 121](#fig-270402d4-f2f1-41e8-835b-e4bde027137d) shows top and side views of several smaller angular objects that are repeated every @distance for the specified @length using a single `<repeat>` element.
In this example, @length divided by @distance is not an integer.
As a result, no repeated object is placed at the position at the end (@s+@length, @tEnd, @zOffsetEnd).

![img](../_images/13_objects/object_4.png)

Figure 122. Repeated small circular objects with changing shape using a single `<repeat>` element

[Figure 122](#fig-7c98e28c-5c09-4993-ad91-62c41d509c64) shows top and side views of several smaller circular objects that are repeated every @distance for the specified @length using a single `<repeat>` element.

**Elements in UML model**

**`<repeat>` element**

In ASAM OpenDRIVE, repeating objects are represented by the `<repeat>` element within the `<object>` element.

```
UML class: t_road_objects_object_repeat
XML tag:   <repeat> (Multiplicity: 0..*)
```

To avoid lengthy XML code, objects of the same type may be repeated.
Attributes of the repeated object shall overrule the attributes from the original object.
If attributes are omitted in the repeated objects, the attributes from the original object apply.

Table 95. Attributes of the <repeat> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `bT` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional |  | 1.9.0 | Coefficient b for t. |
| `cT` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional |  | 1.9.0 | Coefficient c for t. |
| `dT` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional |  | 1.9.0 | Coefficient d for t. |
| `detachFromReferenceLine` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional |  | 1.8.0 | If true, the start and end positions are connected as a straight line which does not follow the road reference line. The default is false |
| `distance` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m |  | Distance between two instances of the object;  If this value is zero, then the object is treated like a continuous feature, for example, a guard rail, a wall, etc. |
| `heightEnd` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Height of the object at @s + @length |
| `heightStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Height of the object at @s |
| `lengthEnd` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Length of the object at @s + @length |
| `lengthStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Length of the object at @s |
| `length` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required |  |  | Length of the repeat area, along the road reference line in s-direction. |
| `radiusEnd` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Radius of the object at @s + @length |
| `radiusStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Radius of the object at @s |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m |  | s-coordinate of start position, overrides the corresponding argument in the original `<object>` record |
| `tEnd` | double | required | m |  | Lateral offset of object’s reference point at @s + @length |
| `tStart` | double | required | m |  | Lateral offset of objects reference point at @s |
| `widthEnd` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Width of the object at @s + @length |
| `widthStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Width of the object at @s |
| `zOffsetEnd` | double | required | m |  | z-offset of the object at @s + @length, relative to the elevation of the road reference line |
| `zOffsetStart` | double | required | m |  | z-offset of the object at @s, relative to the elevation of the road reference line |

**XML example**

```
<objects>
    <object type="streetLamp"
            name="ExampleStreetLamp"
            id="2"
            s="15.00"
            t="5.0"
            zOffset="0.0"
            orientation="none"
            length="0.14"
            width="1.28"
            height="7.35"
            hdg="0.0"
            pitch="0.00"
            roll="0.0000">
        <repeat s="15.0"
                length="180.0"
                distance="60.00"
                tStart="5.0"
                tEnd="5.0"
                widthStart="1.28"
                widthEnd="1.28"
                heightStart="7.35"
                heightEnd="7.35"
                zOffsetStart="0.0"
                zOffsetEnd="0.0"/>
    </object>
</objects>
```

**Calculation**

The value of a linearly interpolated attribute \(a\) at a given point is calculated using the following linear function:

\[a(ds) = aStart + (aEnd - aStart) \cdot \frac{ds}{length}\]

where

|  |  |
| --- | --- |
| \(a(ds)\) | is the attribute value at a given ds-position |
| \(aStart\) | is the start value of the attribute in the zone of repetition |
| \(aEnd\) | is the end value of the attribute in the zone of repetition |
| \(ds\) | is the distance along the road reference line between the start of the element and the given position |
| \(length\) | is the length of the zone of repetition |

The t-coordinate at a given s-coordinate is calculated with the following function:

\[t(ds) =
\begin{cases}
\begin{align\*}
&tStart + (tEnd - tStart) \cdot \frac{ds}{length} \> &&\text{if no coefficients are specified} \\
&tStart + bT \cdot ds + cT \cdot ds^2 + dT \cdot ds^3 \> &&\text{otherwise}
\end{align\*}
\end{cases}\]

where

|  |  |
| --- | --- |
| \(t(ds)\) | is the t-coordinate at a given ds-position |
| \(tStart\) | is the t-coordinate at the start of the zone of repetition |
| \(tEnd\) | is the t-coordinate at the end of the zone of repetition |
| \(ds\) | is the distance along the road reference line between the start of the element and the given position |
| \(bT, cT, dT\) | are coefficients for the cubic polynomial |
| \(length\) | is the length of the zone of repetition |

If coefficients are specified, \(tEnd = t(length)\) shall be true.

**Rules**

The following rules apply to repeating objects:

* Parameters of the repeated object may differ from the original object.
* Applicable parameters of the repeated object shall overrule the parameters from the original object.

* [asam.net:xodr:1.9.0:road.object.repeating.valid\_s\_length](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-repeating-valid-s-length): Repeated objects shall have valid s-coordinates and lengths.

* [asam.net:xodr:1.9.0:road.object.repeating.outline\_use\_cornerlocal](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-repeating-outline-use-cornerlocal): Repeated objects with an outline shall use `<cornerLocal>`

* [asam.net:xodr:1.9.0:road.object.repeating.no\_widthstart\_end\_with\_radius](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-repeating-no-widthstart-end-with-radius): @widthStart and @widthEnd shall not be applicable for objects where @radius is set.

* [asam.net:xodr:1.9.0:road.object.repeating.attributes\_with\_outline\_skeleton](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-repeating-attributes-with-outline-skeleton): @lengthStart, @lengthEnd, @widthStart, @widthEnd, @heightStart, and @heightEnd shall not be applicable for objects with an `<outlines>`, an `<outline>`, or a `<skeleton>` element.

* If t is defined by a cubic polynomial, tEnd must be equal to t(length).
* Parameters @bT, @cT, and @dT shall be considered equal to 0.0 if not explicitly provided.

**Related topics**

* [Section 12.13, "Junction groups"](../12_junctions/12_13_junction_groups.html#top-99e6f0a6-ad6b-4c5e-bace-622208adfc2f)
* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.2, "Object outline"](13_02_object_outline.html#top-67295042-9707-4ad5-9671-b80cde49bb3a)
* [Section 13.3, "Object skeleton"](13_03_object_skeleton.html#top-4c99f00a-bb80-4aff-8c87-c90313ecb3d6)