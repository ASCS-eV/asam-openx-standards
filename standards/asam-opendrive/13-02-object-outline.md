# ASAM OpenDRIVE® v1.9.0 — 13.2 Object outline

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_02_object_outline.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.2 Object outline

Objects may have an outline that is too complex to be described by parameters for angular and circular objects alone.
Therefore, the outline of polygonal objects or non-rectangular objects may be described in a more detailed way.

An outline defines a series of corner points, including the height of the object relative to the road reference line.
Outlines may be closed or open.
In a closed outline, the last corner point is connected to the first.
The inner area of the described outline may be filled with a filling type, for example, grass, concrete, asphalt, or pavement.
The definition of the outline of objects is mainly used for traffic islands and object-based road markings, such as parking spaces and arrows painted on the road surface.

Object-based road markings can be defined by:

* using closed outlines with @fillType = "paint" to create filled-in areas
* using outlines with a `<markings>` element to create lines without fill.

See  [Section 13.8, "Object markings"](13_08_object_markings.html#top-c25542c0-f80d-4da9-a430-020474b58301) for more information on the `<markings>` element.

For cross-walks and regularly shaped parking spaces, use object markings as described in  [Section 13.8, "Object markings"](13_08_object_markings.html#top-c25542c0-f80d-4da9-a430-020474b58301).

An object with more than one `<outline>` element must have exactly one outer outline.
This outer outline defines the overall shape of the object.
All inner outlines must be located fully inside the outer outline.
Inner outlines allow the definition of objects composed of multiple areas with different fill types or lane types as well as those with additional details inside their base shape.

Defining multiple outlines for one object is useful in several cases.
For example, a tree has a narrow trunk and a wide crown.
A driving simulation application might conclude that a vehicle cannot pass the tree if it only just recognized a bounding volume representing the tree.
Two outlines could be defined, one for the narrow trunk and one for the wide crown of the tree.
A driving simulation application in this case could conclude that the vehicle can drive underneath the tree.
Another example is a street light that consist of a pole and a light.
Traffic islands often require more than one outline because the outlines represent logical information, for example, an area where pedestrians can stay.
See example `UC_2Lane-RoundAbout-3Arms.xodr` in [Section 13.2.2, “`<cornerLocal>` element”](#sec-cc00c8a6-eea6-49e6-b90c-37b21524c748).

If an outline is referenced by a `<border>` element and @fillType is set, the fill area is reduced by the border frame.

![img](../_images/13_objects/object_5.png)

Figure 114. Traffic island as object

[Figure 114](#fig-50439882-7c73-4e96-94ac-2b50a31311a0) shows a traffic island which is placed in the middle of a road as non-rectangular object.

**Elements in UML model**

**`<outlines>` element**

In ASAM OpenDRIVE®, the outlines of objects are represented by the `<outlines>` element within the `<object>` element.

The `<outlines>` element serves as a wrapper for the `<outline>` element, which itself contains further elements to describe, for example, corner roads, bridges, and borders.

```
UML class: t_road_objects_object_outlines
XML tag:   <outlines> (Multiplicity: 0..1)
```

Wrapper for the different outline entries of an object, that can contain multiple outline definitions.
If `<outlines>` is not used, an object can have only a single `<outline>` entry.

**`<outline>` element**

In ASAM OpenDRIVE®, a single outline is represented by the `<outline>` element within the `<outlines>` element.

|  |  |
| --- | --- |
|  | If the optional attribute @closed is absent, the default value depends on the object type. See  [Section 13.14, "Combinations of elements and attributes for object types"](13_14_object_examples.html#top-bd330b94-a6e3-42d9-a2b3-0bae5cb19e92) for more details. |

```
UML class: t_road_objects_object_outlines_outline
XML tag:   <outline> (Multiplicity: 1..*)
```

Defines a series of corner points, including the height of the object relative to the road reference line.
For areas, the points should be listed in counter-clockwise order.
The inner area of the described outline may be filled with a filling type, such as grass, concrete, asphalt, or pavement.

An element shall be followed by two or more `<cornerRoad>` elements, by two or more `<cornerLocal>` elements, or by one or more `<curveLocal>` elements.

ASAM OpenDRIVE® 1.4 outline definitions (without `<outlines>` parent element) shall still be supported.

Table 86. Attributes of the <outline> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `closed` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | If true, the outline describes an area, not a linear feature |
| `fillType` | [e\_outlineFillType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_7449C6EF_EFB3_4eb9_9715_762FE63ED2C4) | optional | Type used to fill the area inside the outline |
| `id` | nonNegativeInteger | optional | ID of the outline. Must be unique within one object. |
| `laneType` | [e\_laneType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_9692E2F3_4895_4ce6_A84E_FB1297B0B58E) | optional | Describes the lane type of the outline |
| `outer` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional | Defines if outline is an outer outline of the object. Defaults to "true" |

**XML example**

* [Ex\_TrafficIsland-CornerRoad.xodr](../_attachments/examples/Ex_TrafficIsland-CornerRoad/Ex_TrafficIsland-CornerRoad.xodr)

**Rules**

The following rules apply to outline elements:

* [asam.net:xodr:1.7.0:road.object.outline.outline\_followed\_by\_corner](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-outline-outline-followed-by-corner): An `<outline>` element shall be followed by two or more `<cornerRoad>` elements, by two or more `<cornerLocal>` elements, or by one or more `<cornerLocalParamPoly3>` elements.

* The `<outline>` element may represent an area or a line feature.
* The inner area of the described outline may be filled with a filling type.
* An outline may be specified as an objects outer or inner outline.
  It may be specified if the described outline is located at the outer border of the object.

* [asam.net:xodr:1.9.0:road.object.outline.exactly\_one\_outer](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-outline-exactly-one-outer): `<outlines>` elements shall have exactly one `<outline>` element with @outer=true.

* Omitting @outer shall default to @outer=true.
* It may be specified as which lane type the object is treated by the application.

* [asam.net:xodr:1.7.0:road.object.outline.points\_inside\_box](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-outline-points-inside-box): All points of the `<outline>` element must be located inside the bounding volume.

* Outlines with @closed=true shall connect the last point in the outline to the first as if it was the next point in the sequence

* [asam.net:xodr:1.9.0:road.object.outline.inner\_outline\_touches\_outer](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-outline-inner-outline-touches-outer): If an inner outline touches the outer outline, the reference point shall be identical in both outlines.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.2.1, “`<cornerRoad>` element”](#sec-4bfef803-e146-4f6d-86b3-533540f56b51)
* [Section 13.2.2, “`<cornerLocal>` element”](#sec-cc00c8a6-eea6-49e6-b90c-37b21524c748)
* [Section 13.2.3, “`<curveLocal>` element”](#sec-faf3fe4b-e0a6-4aaa-aec5-75f71224e503)
* [Section 13.9, "Object borders"](13_09_object_borders.html#top-f4d6c702-996e-4344-8e80-e580ea6ca767)

## 13.2.1. `<cornerRoad>` element

`<cornerRoad>` elements are mandatory elements inside an `<outline>` element.
They are used to describe non-linear forms of objects.
They are mutually exclusive with `<cornerLocal>` and `<curveLocal>` elements.
`<cornerRoad>` elements describe the outline of objects relative to the road reference line with their s- and t-coordinates, using line connections between each element which are straight in the inertial coordinates systems.

The shape of an object may be described by the object’s height at a `<cornerRoad>` point and the difference in height relative to the road reference line.

![img](../_images/13_objects/object_6.png)

Figure 115. Object described by corner road coordinates

[Figure 115](#fig-ed2f8ade-8aa9-4dec-9af7-0d9163d293a9) shows a non-linear object with several corner points that is described by the s- and t-coordinates along the road reference line.
Each point is connected to the next with a straight line.
The corner road helps to position objects along a road, for example concrete barriers.
Corner points are connected using linear interpolation.

**Elements in UML model**

**`<cornerRoad>` element**

In ASAM OpenDRIVE®, corner points of an object that use s- and t-coordinates are represented by the `<cornerRoad>` element within the `<outline>` element.

```
UML class: t_road_objects_object_outlines_outline_cornerRoad
XML tag:   <cornerRoad> (Multiplicity: 2..*)
```

Defines a corner point on the object’s outline in road coordinates.

Table 87. Attributes of the <cornerRoad> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `dz` | double | required | m | dz of the corner relative to road reference line |
| `height` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Height of the object at this corner, along the z-axis |
| `id` | nonNegativeInteger | optional |  | ID of the outline point. Must be unique within one outline |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of the corner |
| `t` | double | required | m | t-coordinate of the corner |

**XML example**

* [Ex\_TrafficIsland-CornerRoad.xodr](../_attachments/examples/Ex_TrafficIsland-CornerRoad/Ex_TrafficIsland-CornerRoad.xodr)

**Calculation**

The outline \(\mathbf{e}\) between two given neighboring `<cornerRoad>` elements i and i+1 is calculated with the following linear function with respect to a common normalized interpolation parameter \(p\).
Note that the interpolation is done in the inertial coordinate system.
The s and t coordinates have to be transformed before interpolation.

\[\begin{align}
\mathbf{e\_{i \rightarrow i+1}}(p) &= \left[\begin{array}{@{}c@{}}
x(p) \\
y(p) \\
z(p)
\end{array} \right] \\
x(p) &= x\_i + (x\_{i+1} - x\_{i}) \cdot p \\
y(p) &= y\_i + (y\_{i+1} - y\_{i}) \cdot p \\
z(p) &= z\_i + (z\_{i+1} - z\_{i}) \cdot p
\end{align}\]

where

|  |  |
| --- | --- |
| \(\mathbf{e\_{i \rightarrow i+1}}(p)\) | is the outline between two neighboring corners i and i+1 |
| \(x\_i\), \(y\_{i+1}\), \(y\_i\), \(x\_{i+1}\), \(z\_i\), \(z\_{i+1}\) | are the coordinates x, y, and z of the corners i and i+1 respectively |
| \(p\) | is the normalized parameter to interpolate between 0 (corner i) and 1 (corner i+1) |

**Rules**

The following rules apply to `<cornerRoad>` elements:

* [asam.net:xodr:1.7.0:road.corner\_road.element\_min\_amount](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-corner-road-element-min-amount): There shall be at least two `<cornerRoad>` elements inside an `<outline>` element.

* [asam.net:xodr:1.9.0:road.corner\_road.corner\_road\_local\_exclusivity](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-road-corner-road-local-exclusivity): There shall be no mixture of `<cornerRoad>`, `<cornerLocal>`, and `<curveLocal>` elements inside the same `<outline>` element.

* [asam.net:xodr:1.9.0:road.corner\_road.mandatory\_id\_with\_markings](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-road-mandatory-id-with-markings): The @id attribute of a `<cornerRoad>` element shall be mandatory when the parent also has a `<markings>` element.

* [asam.net:xodr:1.9.0:road.corner\_road.first\_id\_zero](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-road-first-id-zero): The @id attribute of the first `<cornerRoad>` element of an object should be 0.

* [asam.net:xodr:1.9.0:road.corner\_road.sequential\_id\_values](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-road-sequential-id-values): The @id attribute should increase by 1 for each `<cornerRoad>` element in the order they are listed from top to bottom.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 10.5.1, "Superelevation"](../10_roads/10_05_elevation.html#sec-4abf7baf-fb2f-4263-8133-ad0f64f0feac)
* [Section 13.2.2, “`<cornerLocal>` element”](#sec-cc00c8a6-eea6-49e6-b90c-37b21524c748)
* [Section 13.2.3, “`<curveLocal>` element”](#sec-faf3fe4b-e0a6-4aaa-aec5-75f71224e503)

## 13.2.2. `<cornerLocal>` element

`<cornerLocal>` elements are mandatory elements inside an `<outline>` element.
They are used to describe non-linear forms of objects.
They are mutually exclusive with `<cornerRoad>` and `<curveLocal>` elements.
`<cornerLocal>` elements describe the outline of objects within their local u- and v-coordinates with straight connections between each element.

![img](../_images/13_objects/object_7.png)

Figure 116. An object described by `<cornerLocal>` coordinates

[Figure 116](#fig-9e094cdb-4cf5-4bee-a67b-d98530bb6ecc) shows a non-linear object with several corner points that is described within a local coordinate system.
Each point is connected to the next with a straight line.
The corner local helps to position objects beyond a road and relative to a single point, for example buildings or traffic islands.

**Elements in UML model**

**`<cornerLocal>` element**

In ASAM OpenDRIVE®, corner points of an object that use local u- and v-coordinates are represented by the `<cornerLocal>` element within the `<outline>` element.

```
UML class: t_road_objects_object_outlines_outline_cornerLocal
XML tag:   <cornerLocal> (Multiplicity: 2..*)
```

Defines a corner point on the object’s outline relative to the object’s origin in local u/v-coordinates.

Table 88. Attributes of the <cornerLocal> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `height` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Height of the object at this corner, along the z-axis |
| `id` | nonNegativeInteger | optional |  | ID of the outline point. Shall be unique within one outline. |
| `u` | double | required | m | Local u-coordinate of the corner |
| `v` | double | required | m | Local v-coordinate of the corner |
| `z` | double | required | m | Local z-coordinate of the corner |

**XML example**

* [UC\_2Lane-RoundAbout-3Arms.xodr](../_attachments/use_cases/UC_2Lane-RoundAbout-3Arms/UC_2Lane-RoundAbout-3Arms.xodr)

**Calculation**

The outline \(\mathbf{e}\) between two given neighboring `<cornerLocal>` elements i and i+1 is calculated with the following linear function with respect to a common normalized interpolation parameter \(p\):

\[\begin{align}
\mathbf{e\_{i \rightarrow i+1}}(p) &= \left[\begin{array}{@{}c@{}}
u(p) \\
v(p) \\
z(p)
\end{array} \right] \\
u(p) &= u\_i + (u\_{i+1} - u\_{i}) \cdot p \\
v(p) &= v\_i + (v\_{i+1} - v\_{i}) \cdot p \\
z(p) &= z\_i + (z\_{i+1} - z\_{i}) \cdot p
\end{align}\]

where

|  |  |
| --- | --- |
| \(\mathbf{e\_{i \rightarrow i+1}}(p)\) | is the outline between two neighboring corners i and i+1 |
| \(u\_i\), \(u\_{i+1}\), \(v\_i\), \(v\_{i+1}\), \(z\_i\), \(z\_{i+1}\) | are the coordinates u, v, and z of the corners i and i+1 respectively |
| \(p\) | is the normalized parameter to interpolate between 0 (corner i) and 1 (corner i+1) |

**Rules**

The following rules apply to `<cornerLocal>` elements:

* [asam.net:xodr:1.7.0:road.corner\_local.element\_min\_amount](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-corner-local-element-min-amount): There shall be at least two `<cornerLocal>` elements inside an `<outline>` element.

* [asam.net:xodr:1.9.0:road.corner\_road.corner\_road\_local\_exclusivity](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-road-corner-road-local-exclusivity): There shall be no mixture of `<cornerRoad>`, `<cornerLocal>`, and `<curveLocal>` elements inside the same `<outline>` element.

* [asam.net:xodr:1.9.0:road.corner\_local.mandatory\_id\_with\_markings](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-local-mandatory-id-with-markings): The @id attribute of a `<cornerLocal>` element shall be mandatory when the parent also has a `<markings>` element.

* [asam.net:xodr:1.9.0:road.corner\_local.first\_id\_zero](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-local-first-id-zero): The @id attribute of the first `<cornerLocal>` element of an object should be 0.

* [asam.net:xodr:1.9.0:road.corner\_local.sequential\_id\_values](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-local-sequential-id-values): The @id attribute should increase by 1 for each `<cornerLocal>` element in the order they are listed from top to bottom.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.2.1, “`<cornerRoad>` element”](#sec-4bfef803-e146-4f6d-86b3-533540f56b51)
* [Section 13.2.3, “`<curveLocal>` element”](#sec-faf3fe4b-e0a6-4aaa-aec5-75f71224e503)

## 13.2.3. `<curveLocal>` element

`<curveLocal>` elements are mandatory elements inside an `<outline>` element.
They are used to describe non-linear forms of objects.
They are mutually exclusive with `<cornerRoad>` and `<cornerLocal>` elements.

![img](../_images/13_objects/object_19.png)

Figure 117. An object described by `<curveLocal>` coordinates using `<paramPoly3>` elements

[Figure 117](#fig-faf3fe4b-e0a6-4aaa-aec5-75f71224e503) shows a non-linear object with several parametric cubic curves that is described within a local coordinate system.
Each vertex is connected to the next one using its curve, forming a smooth object outline.
Corner local curve helps to model objects with a smooth geometry such as traffic islands or additional road markings which cannot be modeled as lane boundaries.

**Elements in UML model**

**`<curveLocal>` element**

In ASAM OpenDRIVE®, object outlines that use local u- and v-coordinates can be defined using `<curveLocal>` elements.
The following shapes are available:

* Straight lines
* Arcs with a constant curvature
* Parametric cubic polynomials

```
UML class:  t_road_objects_object_outlines_outline_curveLocal
XML tag:    <curveLocal> (Multiplicity: 1..*)
Introduced: 1.9.0
```

Used to describe complex forms of objects.

Can be one of `<line>`, `<arc>`, or `<paramPoly3>`

Table 89. Attributes of the <curveLocal> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `hdg` | double | optional | rad | Start orientation (inertial heading) |
| `height` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | Height of the object at this corner, along the z-axis |
| `id` | nonNegativeInteger | optional |  | ID of the outline point. Shall be unique within one outline. |
| `length` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m | Length of the element’s reference line |
| `u` | double | required | m | Local u-coordinate of the corner |
| `v` | double | required | m | Local v-coordinate of the corner |
| `z` | double | required | m | Local z-coordinate of the corner |

**`<line>` element**

In ASAM OpenDRIVE®, a straight line is represented by the `<line>` element within the `<curveLocal>` element.

A straight line is the simplest corner local curve element.

```
UML class:  t_road_objects_object_outlines_outline_curveLocal_line
XML tag:    <line> (Multiplicity: 1)
Introduced: 1.9.0
```

A straight line is the simplest element.
It contains no further attributes.

**`<arc>` element**

In ASAM OpenDRIVE®, an arc is represented by the `<arc>` element within the `<curveLocal>` element.

An arc describes an object outline with constant curvature.

```
UML class:  t_road_objects_object_outlines_outline_curveLocal_arc
XML tag:    <arc> (Multiplicity: 1)
Introduced: 1.9.0
```

Arcs describe curves with constant curvature.

Table 90. Attributes of the <arc> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `curvature` | double | required | 1/m | Constant curvature throughout the element.  Positive curvature: left curve (counter-clockwise motion) Negative curvature: right curve (clockwise motion) |

**`<paramPoly3> element`**

In ASAM OpenDRIVE®, parametric cubic curves are represented by `<paramPoly3>` elements within the `<curveLocal>` element.

Parametric cubic curves are typically used to represent measurement data.

Unless otherwise stated, the variable p is in the range [0;1].
Alternatively, it may be given in the range [0; @length of parent `<curveLocal>`].

```
UML class:  t_road_objects_object_outlines_outline_curveLocal_paramPoly3
XML tag:    <paramPoly3> (Multiplicity: 1)
Introduced: 1.9.0
```

A parametric cubic curve describing the curve.

Table 91. Attributes of the <paramPoly3> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `aU` | double | required | m | Coefficient a for u. |
| `aV` | double | required | m | Coefficient a for v. |
| `bU` | double | required | 1 | Coefficient b for u. |
| `bV` | double | required | 1 | Coefficient b for v. |
| `cU` | double | required | 1/m | Coefficient c for u. |
| `cV` | double | required | 1/m | Coefficient c for v. |
| `dU` | double | required | 1/m² | Coefficient d for u. |
| `dV` | double | required | 1/m² | Coefficient d for v. |
| `pRange` | [e\_paramPoly3\_pRange](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_22440E30_85F7_48d1_95DF_89D4972EA8BF) | required |  | Range of parameter p.  * Case arcLength: p in [0, @length of parent `<curveLocal>`] * Case normalized: p in [0, 1] (Values of coefficients have no unit) |

**XML example**

* [Ex\_SmoothObjectOutline\_traffic\_island.xodr](../_attachments/examples/Ex_SmoothObjectOutline/Ex_SmoothObjectOutline_traffic_island.xodr)

```
<objects>
    <object type="trafficIsland" subtype="island" id="0" s="20.0" t="0.0" zOffset="0.0" orientation="none" length="32.566370964050293" width="4.0" height="0.3" hdg="0.0" pitch="0.0" roll="0.0">
        <outlines>
            <outline id="0" outer="true">
                <curveLocal u="0.0" v="0.0" z="0.0" height="0.3" hdg="0.0" length="10.0">
                    <line/>
                </curveLocal>
                <curveLocal u="10.0" v="0.0" z="0.0" height="0.3" hdg="0.0" length="6.2831854820251465">
                    <arc curvature="0.5"/>
                </curveLocal>
                <curveLocal u="10.0" v="4.0" z="0.0" height="0.3" hdg="-1.5707963267948966" length="10.0">
                    <line/>
                </curveLocal>
                <curveLocal u="0.0" v="4.0" z="0.0" height="0.3" hdg="-1.5707963267948966" length="6.2831854820251465">
                    <arc curvature="0.5"/>
                </curveLocal>
            </outline>
        </outlines>
    </object>
</objects>
```

**Rules**

The following rules apply to `<curveLocal>` elements:

* [asam.net:xodr:1.9.0:road.curve\_local.element\_min\_amount](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-curve-local-element-min-amount): There shall be at least one `<curveLocal>` element inside an `<outline>` element.

* [asam.net:xodr:1.9.0:road.corner\_road.corner\_road\_local\_exclusivity](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-corner-road-corner-road-local-exclusivity): There shall be no mixture of `<cornerRoad>`, `<cornerLocal>`, and `<curveLocal>` elements inside the same `<outline>` element.

* [asam.net:xodr:1.9.0:road.curve\_local.continuous\_curve\_local](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-curve_local-continuous-curve-local): Outlines defined by `<curveLocal>` elements shall be continuous.

Continuity is achieved when each point with a predecessor lies at the end of that predecessors curve.

* If no @length is provided, the curve shall extend up to the next `<curveLocal>` element.

* [asam.net:xodr:1.9.0:road.curve\_local.length\_match](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-curve-local-length-match): The actual curve length, as determined by numerical integration over the parameter range, should match @length.

* [asam.net:xodr:1.9.0:road.curve\_local.paramPoly3.arcLength\_range](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-curve-local-parampoly3-arclength-range): For `<paramPoly3>` elements with @pRange="arcLength", p shall be chosen in [0, @length from `<curveLocal>`].

* [asam.net:xodr:1.9.0:road.curve\_local.paramPoly3.normalized\_range](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-curve-local-parampoly3-normalized-range): For `<paramPoly3>` elements with @pRange="normalized", p shall be chosen in [0, 1].

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.2.1, “`<cornerRoad>` element”](#sec-4bfef803-e146-4f6d-86b3-533540f56b51)
* [Section 13.2.2, “`<cornerLocal>` element”](#sec-cc00c8a6-eea6-49e6-b90c-37b21524c748)

## 13.2.4 Object marking on outlines

An object’s outline may have markings.
This is done using an `<markings>` element inside the `<outline>` element.
See  [Section 13.8, "Object markings"](13_08_object_markings.html#top-c25542c0-f80d-4da9-a430-020474b58301).