# ASAM Opendrive v1.9.0 — 10.5 Road elevation methods

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/10_roads/10_05_elevation.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.5 Road elevation methods

There are several ways to elevate a road or parts of a road:

* Road elevation specifies the elevation along the road reference line, that is in s-direction.
* The lateral profile specifies the elevation orthogonally to the road reference line, that is in t-direction.
* Road CRG surface may influence the road height (see  [Section 10.6, "Road CRG surface"](10_06_road_surface.html#top-7a0a2c4b-41a6-46e6-845e-932f2a014730)).
* Objects may influence the road height (see  [Section 13.13, "Object CRG surface"](../13_objects/13_13_object_surface.html#top-b9a23d6c-0f67-4e9e-b146-8e26ce2f75f5)).

![img](../_images/10_roads/types_elevation.png)

Figure 42. Types of elevation

[Figure 42](#fig-93510ca3-fe7d-43ad-b849-addced1e4916) shows the types of road elevation.
The length s does not change with the elevation.

## 10.5.1 Road elevation

A road may be elevated along its road reference line.
Road elevation is defined per road cross section at a given position on the road reference line.
Elevation is specified in meters.
The default elevation of a road is zero.
In case georeferencing is used, the definition of zero depends on it.

**Elements in UML model**

**`<elevationProfile>` element**

In ASAM OpenDRIVE, the elevation profile is represented by the `<elevationProfile>` element within the `<road>` element.

```
UML class: t_road_elevationProfile
XML tag:   <elevationProfile> (Multiplicity: 0..1)
```

Road elevation specifies the elevation along the road reference line, that is in s-direction.

**`<elevation>` element**

In ASAM OpenDRIVE, elevation is represented by the `<elevation>` element within the `<elevationProfile>` element.

```
UML class: t_road_elevationProfile_elevation
XML tag:   <elevation> (Multiplicity: 0..*)
```

Defines an elevation element at a given position on the road reference line.
Elements shall be defined in ascending order along the reference line.
The s length does not change with the elevation.

Table 27. Attributes of the <elevation> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `a` | double | required | m | Coefficient a, elevation at @s (ds=0) |
| `b` | double | required | 1 | Coefficient b |
| `c` | double | required | 1/m | Coefficient c |
| `d` | double | required | 1/m² | Coefficient d |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position |

**Calculation**

Road elevation is calculated with the following polynomial function of the third order:

`elev(ds) = a + b*ds + c*ds² + d*ds³`

where

|  |  |
| --- | --- |
| `elev` | is the elevation (inertial z) at a given position |
| `a, b, c, d` | are the coefficients |
| `ds` | is the distance along the road reference line between the start of a new elevation element and the given position. |

`ds` restarts at zero for each element.
The absolute position of an elevation value is calculated as follows:

`s = sstart + ds`

where

|  |  |
| --- | --- |
| `s` | is the absolute position in the road reference line coordinate system |
| `sstart` | is the start position of the element in the road reference line coordinate system |

**Rules**

The following rules apply to road elevation:

* [asam.net:xodr:1.4.0:road.elevation.elev\_along\_ref\_line](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-elevation-elev-along-ref-line): Roads shall be elevated along their road reference line.

* Road elevation may be defined in combination with superelevation and road shape or standalone.

* [asam.net:xodr:1.4.0:road.elevation.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-elevation-elem-asc-order): `<elevation>` elements shall be defined in ascending order according to the s-coordinate.

* The definition of road elevation remains valid until the next element of this type is defined.

**Related topics**

* [Section 10.5.2, “Superelevation”](#sec-4abf7baf-fb2f-4263-8133-ad0f64f0feac)
* [Section 10.5.3, “Shape definition”](#sec-66ac2b58-dc5e-4538-884d-204406ea53f2)

## 10.5.2 Superelevation

Superelevation is part of the lateral profile and describes the cross slope of the road.
It may be used, for example, to incline the road to the inner side so that vehicles can drive through them more easily.

![img](../_images/10_roads/superelevation.png)

Figure 43. Superelevation

[Figure 43](#fig-4d4fa618-abfb-4df3-b4b1-a58dcda7c4d4) shows that for superelevated roads, the t-axis of a road is not parallel to the underlying terrain.
For this reason, a lateral profile is defined for the entire road cross section.
Superelevation does not change the actual width of a lane, but it affects the projected width.
The default value for superelevation is zero.
Mathematically, superelevation is defined as the roll angle of the road cross section around the road reference line.
That means, superelevation has positive values for roads falling to the right side and negative values for roads falling to the left side.
In the example in [Figure 43](#fig-4d4fa618-abfb-4df3-b4b1-a58dcda7c4d4), the road reference line is parallel to the y-axis, to simplify the given example.

**Elements in UML model**

**`<lateralProfile>` element**

In ASAM OpenDRIVE, the lateral profile is represented by the `<lateralProfile>` element within the `<road>` element.

```
UML class: t_road_lateralProfile
XML tag:   <lateralProfile> (Multiplicity: 0..1)
```

Contains a series of lateral elevation elements that define the characteristics of the road surfaces banking along the road reference line.
The lateral profile is defined relative to the elevation of the road reference line.

**`<superelevation>` element**

In ASAM OpenDRIVE, superelevation is represented by the `<superelevation>` element within the `<lateralProfile>` element.

```
UML class: t_road_lateralProfile_superelevation
XML tag:   <superelevation> (Multiplicity: 0..*)
```

Superelevation specifies the transverse slope along the road reference line.
Superelevation is constant in each cross section and can vary in road reference line direction.

Elements must be defined in ascending order along the reference line.
The parameters of an element are valid until the next element starts or the road reference line ends.
Per default, the superelevation of a road is zero.

Table 28. Attributes of the <superelevation> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `a` | double | required | rad | Coefficient a, superelevation at @s (ds=0). |
| `b` | double | required | rad/m | Coefficient b. |
| `c` | double | required | rad/m² | Coefficient c. |
| `d` | double | required | rad/m³ | Coefficient d. |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position |

**Calculation**

Superelevation is calculated using the following polynomial function of the third order:

`superelevation (ds) = a + b*ds + c*ds² + d*ds³`

where

|  |  |
| --- | --- |
| `superelevation` | is the superelevation at a given position |
| `a, b, c, d` | are the coefficients |
| `ds` | is the distance along the road reference line between the start of a superelevation element and the given position. |

`ds` restarts at zero for each element.
The absolute position of a superelevation value is calculated as follows:

`s = sstart + ds`

where

|  |  |
| --- | --- |
| `s` | is the absolute position in the road reference line coordinate system |
| `sstart` | is the start position of the element in the road reference line coordinate system |

**Rules**

The following rules apply to superelevation:

* When superelevation is defined, it shall apply to the entire road cross section.

* [asam.net:xodr:1.4.0:road.superelevation.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-superelevation-elem-asc-order): `<superelevation>` elements shall be defined in ascending order according to the s-coordinate.

* Single lanes of a road may be excluded from superelevation using the @level attribute.
* Road elevation may be defined in combination with superelevation.

**Related topics**

* [Section 10.5.1, “Road elevation”](#sec-1d876c00-d69e-46d9-bbcd-709ab48f14b1)
* [Section 10.5.3, “Shape definition”](#sec-66ac2b58-dc5e-4538-884d-204406ea53f2)
* [Section 11.7.1, "Excluding lanes from lateral profile"](../11_lanes/11_07_lane_geometry.html#sec-2b576dd1-12a6-4fe3-9345-d04a51c332c8)

## 10.5.3 Shape definition

Non-linear lateral road shapes can be described by `<shape>` elements.
Shapes describe the elevation of a road’s cross section at a given point on the road reference line in a more detailed way.
That means there may be several shape definitions at one s-coordinate that have different t-values, thereby describing the curvy shape of the road.

Shapes change the actual width of a lane due to its curvilinear shape.
The projected width with respect to the planview is not affected.

![img](../_images/10_roads/road_shape_min_t.png)

Figure 44. Minimum t-definition range for road shapes

[Figure 44](#fig-a81a5b93-5ea9-421b-9684-5b5f3e84757b) shows how to calculate the height information between two lateral profiles.
The lateral profile at sR1 has five polynomial definitions, while the lateral profile at sR2 has three polynomial definitions.
To calculate a point between two lateral profiles, interpolate linearly between those two profiles and use the formulas shown in [Figure 44](#fig-a81a5b93-5ea9-421b-9684-5b5f3e84757b).
For the calculation the entire required t-definition has to cover the maximum road width at all s-positions.

Typical use cases are curved road surfaces on high-speed test tracks and crossfalls.
The default value for the shape is zero.

|  |  |
| --- | --- |
|  | Lane offsets can be defined non-linear along s. Shapes are interpolated linear along s. Therefore shapes cannot always follow lane offsets. |

![img](../_images/10_roads/road_shape.png)

Figure 45. Road shape definition

[Figure 45](#fig-219ec364-6ee0-4f0f-917f-e2a7a598e933) shows how the defined t-range must at least cover the maximum t-expansion of the entire `<road>` element.

**Deprecated**

Shapes in combination with superelevation are deprecated.

![img](../_images/10_roads/combo_shape_superele.png)

Figure 46. Road shape definition in combination with superelevation

[Figure 46](#fig-4c530904-6f9f-4286-8525-505fe130547b) shows the deprecated combination of road shape and superelevation.
The shape is rotated using superelevation.

**Elements in UML model**

**`<lateralProfile>` element**

In ASAM OpenDRIVE, the lateral profile is represented by the `<lateralProfile>` element within the `<road>` element.

```
UML class: t_road_lateralProfile
XML tag:   <lateralProfile> (Multiplicity: 0..1)
```

Contains a series of lateral elevation elements that define the characteristics of the road surfaces banking along the road reference line.
The lateral profile is defined relative to the elevation of the road reference line.

**`<shape>` element**

In ASAM OpenDRIVE, the lateral profile is represented by the `<shape>` element within the `<lateralProfile>` element.

```
UML class: t_road_lateralProfile_shape
XML tag:   <shape> (Multiplicity: 0..*)
```

Defined as the road section’s surface relative to the reference plane.
There may be several shape definitions at one s-position that have different t-values, thereby describing the curvy shape of the road.

Table 29. Attributes of the <shape> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `a` | double | required | m | Coefficient a, relative height at @t (dt=0) |
| `b` | double | required | 1 | Coefficient b |
| `c` | double | required | 1/m | Coefficient c |
| `d` | double | required | 1/m² | Coefficient d |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position |
| `t` | double | required | m | t-coordinate of start position |

**Calculation**

The shape of the lateral profile is calculated with the following polynomial function:

`hShape (dt)= a + b*dt + c*dt² + d*dt³`

where

|  |  |
| --- | --- |
| `hShape` | is the height above the reference plane at a given position |
| `a, b, c, d` | are the coefficients |
| `dt` | is the distance perpendicular to the road reference line between the start of a shape element and the given position |

`dt` restarts at zero for each element.
The absolute position of a shape value is calculated as follows:

`t = tstart + dt`

where

|  |  |
| --- | --- |
| `t` | is the absolute position in the road reference line coordinate system |
| `tstart` | is the start position of the element in the road reference line coordinate system |

**Rules**

The following rules apply to shapes:

* Shapes may be defined in combination with road elevation.

* [asam.net:xodr:1.4.0:road.shape.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-shape-elem-asc-order): `<shape>` elements shall be defined in ascending order, firstly according to the s-coordinate and secondly according to the t-coordinate.

* [asam.net:xodr:1.4.0:road.shape.t\_definition\_coverage](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-shape-t-definition-coverage): At all s-positions the t-definition has to cover the maximum road width of the entire road.

**Related topics**

* [Section 10.2, "Properties for road sections and cross section"](10_02_properties_for_road_sections.html#top-1323a74c-b102-4fdd-bc02-63265f034f45)
* [Section 10.5.1, “Road elevation”](#sec-1d876c00-d69e-46d9-bbcd-709ab48f14b1)
* [Section 10.5.2, “Superelevation”](#sec-4abf7baf-fb2f-4263-8133-ad0f64f0feac)

## 10.5.4 Cross section surface

Cross section surfaces describe the road surface along the road reference line with strips.
A strip defines a start position in s-direction and parameters for polynomials in t-direction.
On each side of the road reference line there are up to two strips.
The inner strip to the right has @id="-1" and the inner strip to the left @id="1".
The outer strip to the right has @id="-2" and the outer strip to the left @id="2".

![img](../_images/10_roads/cross_section_surface_strips.png)

Figure 47. Cross section surface strips on a road

[Figure 47](#fig-b868a64e-b460-4408-925c-eb0a6826a120) shows a road with strips of a cross section surface.

The inner strips have a width and an offset in t-direction to define where the outer strips start in t-direction.
The outer strips are valid to the outer edge of the last defined lane on the given side.
If only one strip exists, it has no given width and is valid to the end of the lane definition.

The road surface of the outer strip can be calculated relative to or independent of the inner strip.

![img](../_images/10_roads/cross_section_surface.png)

Figure 48. Cross section surface

[Figure 48](#fig-e4eee75b-f906-45b7-8daa-02e94307779c) shows cross section surfaces on both sides of a road.

|  |  |
| --- | --- |
|  | In general strip ids and strip widths are independent of lane ids and lane widths. |

**Elements in UML model**

**`<lateralProfile>` element**

In ASAM OpenDRIVE, the lateral profile is represented by the `<lateralProfile>` element within the `<road>` element.

```
UML class: t_road_lateralProfile
XML tag:   <lateralProfile> (Multiplicity: 0..1)
```

Contains a series of lateral elevation elements that define the characteristics of the road surfaces banking along the road reference line.
The lateral profile is defined relative to the elevation of the road reference line.

**`<crossSectionSurface>` element**

In ASAM OpenDRIVE, cross section surfaces are represented by the `<crossSectionSurface>` element within the `<lateralProfile>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface
XML tag:    <crossSectionSurface> (Multiplicity: 0..1)
Introduced: 1.8.0
```

A cross section surface defines the lateral profile by means of constant, linear, quadratic, and cubic polynomials in t-direction.

A cross section surface is valid for the full length of the road.

**`<tOffset>` element**

In ASAM OpenDRIVE, a t-offset is represented by the `<tOffset>` element within the `<crossSectionSurface>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_tOffset
XML tag:    <tOffset> (Multiplicity: 0..1)
Introduced: 1.8.0
```

A t offset shifts all strips relative to the road reference line in t-direction.

**`<surfaceStrips>` element**

In ASAM OpenDRIVE, surfaces are represented by the `<surfaceStrips>` element within the `<crossSectionSurface>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_surfaceStrip
XML tag:    <surfaceStrips> (Multiplicity: 1)
Introduced: 1.8.0
```

Surface strips contains the strips.

**`<strip>` element**

In ASAM OpenDRIVE, surface definitions are represented by the `<strip>` element within the `<surfaceStrips>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_strip
XML tag:    <strip> (Multiplicity: 1..4)
Introduced: 1.8.0
```

A strip defines the lateral profile in t- and s-direction.

Table 30. Attributes of the <strip> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | int | required | 1 for the inner left strip, -1 for the inner right strip, 2 for the outer left strip, -2 for the outer right strip |
| `mode` | [e\_strip\_mode](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_54B8FC12_8EA8_4739_A7DE_1EE52DEA3389) | optional | Can only be defined for an outer strip. |

**`<width>` element**

In ASAM OpenDRIVE, definitions of the width are represented by the `<width>` element within the `<strip>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_strip_width
XML tag:    <width> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Defines the width of the inner strip.

**`<constant>` element**

In ASAM OpenDRIVE, constant parts are represented by the `<constant>` element within the `<strip>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_strip_constant
XML tag:    <constant> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Defines in t a constant height of the surface.

**`<linear>` element**

In ASAM OpenDRIVE, linear parts are represented by the `<linear>` element within the `<strip>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_strip_linear
XML tag:    <linear> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Defines in t a linear height of the surface.

**`<quadratic>` element**

In ASAM OpenDRIVE, quadratic parts are represented by the `<quadratic>` element within the `<strip>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_strip_quadratic
XML tag:    <quadratic> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Defines in t a quadratic height of the surface.

**`<cubic>` element**

In ASAM OpenDRIVE, cubic parts are represented by the `<cubic>` element within the `<strip>` element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_strip_cubic
XML tag:    <cubic> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Defines in t a cubic height of the surface.

**`<coefficients>` element**

In ASAM OpenDRIVE, the cross section surface polynomial coefficients are represented by the <coefficients> element within the <tOffset>, <width>, <constant>, <linear>, <quadratic>, or <cubic> element.

```
UML class:  t_road_lateralProfile_crossSectionSurface_coefficients
XML tag:    <coefficients> (Multiplicity: 1..*)
Introduced: 1.8.0
```

Defines the coefficients of a cubic polynomial in s-direction.

The first `<coefficients>` element shall start at the beginning of the road reference line with @s="0".

Table 31. Attributes of the <coefficients> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `a` | double | optional | m | 1.8.0 | Coefficient a. If the attribute is not specified, the value is 0. |
| `b` | double | optional | m/m | 1.8.0 | Coefficient b. If the attribute is not specified, the value is 0. |
| `c` | double | optional | m/m² | 1.8.0 | Coefficient c. If the attribute is not specified, the value is 0. |
| `d` | double | optional | m/m³ | 1.8.0 | Coefficient d. If the attribute is not specified, the value is 0. |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m |  | s-coordinate of start position |

**XML example**

Code 1. Solution in ASAM OpenDRIVE 1.9.0

```
<lateralProfile>
    <crossSectionSurface>
        <tOffset>
            <coefficients s="0.0"
                          a="0.0"
                          b="0.0"
                          c="0.0045000000000000005"
                          d="-5e-05"/>
            <coefficients s="50.0"
                          a="5.0"
                          b="0.075"
                          c="-0.003"
                          d="3e-05"/>
        </tOffset>
        <surfaceStrips>
            <strip id="1">
                <width>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="0.0"
                                  c="0.006000000000000001"
                                  d="-6.400000000000001e-05"/>
                    <coefficients s="50.0"
                                  a="7.0"
                                  b="0.12"
                                  c="-0.0036"
                                  d="3.2e-05"/>
                </width>
                <constant>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="1.942890293094024e-18"
                                  c="0.0011385321100917428"
                                  d="-3.192660550458715e-05"/>
                    <coefficients s="20.0"
                                  a="0.2"
                                  b="0.007229357798165137"
                                  c="-0.0007770642201834863"
                                  d="9.449541284403669e-06"/>
                    <coefficients s="70.0"
                                  a="-0.2"
                                  b="0.0003944954128440377"
                                  c="0.0006403669724770642"
                                  d="-1.437648657832144e-05"/>
                </constant>
                <linear>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="0.0"
                                  c="-0.0003285714285714286"
                                  d="6.507936507936508e-06"/>
                    <coefficients s="30.0"
                                  a="-0.12"
                                  b="-0.002142857142857143"
                                  c="0.00025714285714285715"
                                  d="-2.3032069970845484e-06"/>
                </linear>
                <quadratic>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="0.0"
                                  c="-2.1649831649831646e-06"
                                  d="3.713680009976306e-08"/>
                    <coefficients s="45.0"
                                  a="-0.001"
                                  b="3.0757575757575755e-05"
                                  c="2.848484848484849e-06"
                                  d="-3.7916353618832964e-08"/>
                </quadratic>
                <cubic>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="0.0"
                                  c="1.4840830449826988e-06"
                                  d="-1.5831467535110928e-08"/>
                    <coefficients s="85.0"
                                  a="0.001"
                                  b="-9.085294117647057e-05"
                                  c="-2.5529411764705903e-06"
                                  d="2.480610021786493e-07"/>
                </cubic>
            </strip>
            <strip id="2">
                <constant>
                    <coefficients s="0.0"
                                  a="0.2"
                                  b="0.0"
                                  c="-0.00031875"
                                  d="3.2031250000000004e-06"/>
                    <coefficients s="80.0"
                                  a="-0.2"
                                  b="0.0105"
                                  c="0.00045"
                                  d="-2.375e-05"/>
                </constant>
                <linear>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="8.673617379884036e-20"
                                  c="-8.437500000000002e-06"
                                  d="6.640625000000001e-08"/>
                    <coefficients s="80.0"
                                  a="-0.02"
                                  b="-7.500000000000001e-05"
                                  c="7.500000000000001e-06"
                                  d="-1.8750000000000003e-07"/>
                </linear>
                <quadratic>
                    <coefficients s="0.0"
                                  a="0.0001"
                                  b="-2.6201552501733024e-20"
                                  c="-4.856163886874543e-06"
                                  d="2.8561638868745455e-07"/>
                    <coefficients s="10.0"
                                  a="-0.0001"
                                  b="-1.1438361131254525e-05"
                                  c="3.712327773749093e-06"
                                  d="-1.3739209840732682e-07"/>
                    <coefficients s="25.0"
                                  a="0.0001"
                                  b="7.1918056562726596e-06"
                                  c="-2.4703166545806143e-06"
                                  d="4.0075537829344936e-08"/>
                    <coefficients s="65.0"
                                  a="-0.001"
                                  b="1.9290548706792377e-06"
                                  c="2.338747884940778e-06"
                                  d="-4.5072491650757476e-08"/>
                </quadratic>
                <cubic>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="0.0"
                                  c="3.1999999999999995e-07"
                                  d="-3.555555555555555e-09"/>
                    <coefficients s="75.0"
                                  a="0.0003"
                                  b="-1.1999999999999999e-05"
                                  c="-4.8e-07"
                                  d="1.92e-08"/>
                </cubic>
            </strip>
            <strip id="-1">
                <width>
                    <coefficients s="0.0"
                                  a="8.0"
                                  b="0.0"
                                  c="0.0"
                                  d="0.0"/>
                </width>
                <constant>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="1.942890293094024e-18"
                                  c="0.0011385321100917428"
                                  d="-3.192660550458715e-05"/>
                    <coefficients s="20.0"
                                  a="0.2"
                                  b="0.007229357798165137"
                                  c="-0.0007770642201834863"
                                  d="9.449541284403669e-06"/>
                    <coefficients s="70.0"
                                  a="-0.2"
                                  b="0.0003944954128440377"
                                  c="0.0006403669724770642"
                                  d="-1.437648657832144e-05"/>
                </constant>
                <linear>
                    <coefficients s="0.0"
                                  a="0.1"
                                  b="0.0"
                                  c="6.000000000000001e-05"
                                  d="-4.0000000000000003e-07"/>
                </linear>
            </strip>
            <strip id="-2">
                <linear>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="1.3183898417423733e-17"
                                  c="-0.0005797802197802213"
                                  d="2.9763125763125804e-05"/>
                    <coefficients s="15.0"
                                  a="-0.03"
                                  b="0.0026967032967032934"
                                  c="0.0007595604395604402"
                                  d="-5.2923076923076945e-05"/>
                    <coefficients s="25.0"
                                  a="0.02"
                                  b="0.002010989010989012"
                                  c="-0.0008281318681318682"
                                  d="3.270329670329671e-05"/>
                    <coefficients s="35.0"
                                  a="-0.01"
                                  b="-0.004740659340659341"
                                  c="0.00015296703296703297"
                                  d="-1.1948761297873725e-06"/>
                </linear>
                <quadratic>
                    <coefficients s="0.0"
                                  a="0.0"
                                  b="0.0"
                                  c="1.8518518518518523e-06"
                                  d="-1.920438957475995e-08"/>
                    <coefficients s="90.0"
                                  a="0.001"
                                  b="-0.00013333333333333337"
                                  c="-3.333333333333328e-06"
                                  d="6.666666666666664e-07"/>
                </quadratic>
                <cubic>
                    <coefficients s="0.0"
                                  a="-0.0002"
                                  b="2.7105054312137612e-21"
                                  c="9.583333333333325e-08"
                                  d="-6.712962962962956e-10"/>
                    <coefficients s="60.0"
                                  a="0.0"
                                  b="4.25e-06"
                                  c="-2.499999999999998e-08"
                                  d="-4.687500000000003e-10"/>
                </cubic>
            </strip>
        </surfaceStrips>
    </crossSectionSurface>
</lateralProfile>
```

**Calculation**

**Calculation of width**

The width is calculated with the following function:

\[\begin{align\*}
w\_{i}(ds) = a\_{i} + b\_{i}\*ds + c\_{i}\*ds^{2} + d\_{i}\*ds^{3}
\end{align\*}\]

where

|  |  |
| --- | --- |
| \(w\_{i}\) | is the width at a given position |
| \(a\_{i}, b\_{i}, c\_{i}, d\_{i}\) | are the coefficients stored in the `<width>` element |
| \(ds\) | is the distance along the road reference line between the start of a `<crossSectionSurface>` element and the given position |

For \(n\) entries with a width definition in s-direction define the following parameters:

\[\begin{align\*}
s\_{0..n}, a\_{0..n}, b\_{0..n}, c\_{0..n}, d\_{0..n}
\end{align\*}\]

\[\begin{align\*}
with: ds = s - s\_{0..n}
\end{align\*}\]

**Calculation of \(t\_{offset}\)**

The offset for t is calculated with the following function:

\[\begin{align\*}
t\_{offset,i}(ds) = a\_{i} + b\_{i}\*ds + c\_{i}\*ds^{2} + d\_{i}\*ds^{3}
\end{align\*}\]

where

|  |  |
| --- | --- |
| \(t\_{offset,i}\) | is the t-offset at a given position |
| \(a\_{i}, b\_{i}, c\_{i}, d\_{i}\) | are the coefficients stored in the `<tOffset>` element |
| \(ds\) | is the distance along the road reference line between the start of a `<crossSectionSurface>` element and the given position |

For \(m\) entries with a t-offset definition in s-direction define the following parameters:

\[\begin{align\*}
s\_{0..m}, a\_{0..m}, b\_{0..m}, c\_{0..m}, d\_{0..m}
\end{align\*}\]

\[\begin{align\*}
with: ds = s - s\_{0..m}
\end{align\*}\]

**Calculation of \(dt\)**

Since the width has always a positive value, the calculation of the distance along the t-axis, \(dt\), has to consider the side.

Subtract the \(t\_{offset}\) from \(t\) to get the effective \(t\_{effective}\):

\[\begin{align\*}
t\_{effective} = t - t\_{offset}
\end{align\*}\]

For the right side with \(t\_{effective} <= 0\) apply the following:

If \(-w\_{right} <= t\_{effective} <= 0\) calculate

\[\begin{align\*}
&dt = t\_{effective}\\
&dt = t - t\_{offset}
\end{align\*}\]

If \(t\_{effective} < -w\_{right}\) calculate

\[\begin{align\*}
&dt = t\_{effective} + w\_{right}\\
&dt = t - t\_{offset} + w\_{right} & w\_{right} > 0
\end{align\*}\]

For the left side with \(t\_{effective} > 0\) apply the following:

If \(0 <= t\_{effective} <= w\_{left}\) calculate

\[\begin{align\*}
&dt = t\_{effective}\\
&dt = t - t\_{offset}
\end{align\*}\]

If \(t\_{effective} < w\_{left}\) calculate

\[\begin{align\*}
&dt = t\_{effective} - w\_{left}\\
&dt = t - t\_{offset} - w\_{left} & w\_{left} > 0
\end{align\*}\]

**Calculation of the local height due to the cross section surface**

The height value is calculated with the following function:

\[\begin{align\*}
h\_{CrossSectionSurface}(s, t) = co(s) + li(s)\*dt + qu(s)\*dt^{2} + cu(s)\*dt^{3}
\end{align\*}\]

where

|  |  |
| --- | --- |
| \(s, t\) | are the positions given in s and t |
| \(co\_{s}, li\_{s}, qu\_{s}, cu\_{s}\) | are the constant, linear, quadratic, and cubic components depending on the s-position |
| \(dt\) | is the distance along the t-axis |

The constant, linear, quadratic, and cubic components are linearly independent and can be calculated separately.

The constant (\(co\)) component uses the following definitions:

\[\begin{align\*}
s\_{co,0..n\_{co}}, a\_{co,0..n\_{co}}, b\_{co,0..n\_{co}}, c\_{co,0..n\_{co}}, d\_{co,0..n\_{co}}
\end{align\*}\]

\[\begin{align\*}
with: &&i = 0..n\_{co}\\
&&s\_{co,i} <= s < s\_{co,i+1}\\
&&ds\_{co} = s - s\_{co,i}
\end{align\*}\]

\[\begin{align\*}
co(s) = a\_{co,i} + b\_{co,i}\*ds\_{co} + c\_{co,i}\*{ds\_{co}}^{2} + d\_{co,i}\*{ds\_{co}}^{3}
\end{align\*}\]

The same definitions apply to the linear (\(li\)), quadratic (\(qu\)) and cubic (\(cu\)) components.
The number \(n\) of the components, \(n\_{co}\), \(n\_{li}\), \(n\_{qu}\), and \(n\_{cu}\) can be different for each component.

**Calculation of height regarding the mode**

In the case of the inner two strips (\(-w\_{right} <= t\_{effective} <= w\_{left}\)), the mode does not matter:

\[\begin{align\*}
h\_{strip}(s, dt) = h\_{CrossSectionSurface}(s, dt)
\end{align\*}\]

In the case of the outer two strips (\(t\_{effective} < -w\_{right}\) or \(t\_{effective} > w\_{left}\)), the mode shall be taken into account.

@mode="independent"

The calculation of the polynomials for the height values is independent and based on the road reference line.

@mode="relative"

The calculation of the polynomials for the height values is relative to the outer edge of the inner strip.

Left side:

\[\begin{align\*}
h\_{CrossSectionSurface}(s, t) = h\_{strip,id=1}(s, dt = w\_{left,id=1}(s)) + h\_{strip,id=2}(s, dt)
\end{align\*}\]

Right side:

\[\begin{align\*}
h\_{CrossSectionSurface}(s, t) = h\_{strip,id=-1}(s, dt = -w\_{right,id=-1}(s)) + h\_{strip,id=-2}(s, dt)
\end{align\*}\]

**Rules**

* [asam.net:xodr:1.8.0:road.cross\_section\_surface.lane\_def\_valid](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-cross-section-surface-lane-def-valid): A cross section surface is only valid within the lane definition of the road.

* [asam.net:xodr:1.8.0:road.cross\_section\_surface.start\_end\_match\_with\_refline](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-cross-section-surface-start-end-match-with-refline): A cross section surface shall start and end at the start and end of the road reference line.

* [asam.net:xodr:1.8.0:road.cross\_section\_surface.use\_strip](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-cross-section-surface-use-strip): If on a side only one strip is used, it is defined in a `<strip>` element with @id="1" or @id="-1" and a width shall not be specified.

* [asam.net:xodr:1.8.0:road.cross\_section\_surface.use\_width](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-cross-section-surface-use-width): If on a side two strips are specified, a width for the inner strip shall be specified.

* [asam.net:xodr:1.8.0:road.cross\_section\_surface.height](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-cross-section-surface-height): The value of @height at `<lane>` elements is added to the cross section surface in z-direction.

* The @level attribute may be used to exclude outer lanes from the cross section surface definition.

* [asam.net:xodr:1.8.0:road.cross\_section\_surface.no\_shape\_superelevation](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-cross-section-surface-no-shape-superelevation): A cross section surface shall not be used in combination with road shape or superelevation.

**Related topics**

* [Section 10.5.1, “Road elevation”](#sec-1d876c00-d69e-46d9-bbcd-709ab48f14b1)
* [Section 11.7.1, "Excluding lanes from lateral profile"](../11_lanes/11_07_lane_geometry.html#sec-2b576dd1-12a6-4fe3-9345-d04a51c332c8)