# ASAM Opendrive v1.9.0 — 9.6 Parametric cubic curve

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/09_geometries/09_06_param_poly3.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.6 Parametric cubic curve

Parametric cubic curves are used for complex curves that are to be generated from measurement data.
Parametric cubic curves are more flexible and allow a greater variety of road courses than cubic polynomials.
In comparison to cubic polynomials that are defined in a x/y coordinate system or as local u/v coordinates, the coordinates x and y are interpolated separately by their own splines with respect to a common interpolation parameter p.

**Elements in UML model**

**`<paramPoly3>` element**

In ASAM OpenDRIVE, parametric cubic curves are represented by `<paramPoly3>` elements within the `<geometry>` element.

```
UML class: t_road_planView_geometry_paramPoly3
XML tag:   <paramPoly3>
```

A parametric cubic curve describing the road reference line.

Table 21. Attributes of the <paramPoly3> element


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
| `pRange` | [e\_paramPoly3\_pRange](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_22440E30_85F7_48d1_95DF_89D4972EA8BF) | required |  | Range of parameter p.  * Case arcLength: p in [0, @length of `<geometry>`] * Case normalized: p in [0, 1] (Values of coefficients have no unit) |

**XML example**

```
<planView>
    <geometry s="0.000000000000e+00"
              x="6.804539427645e+05"
              y="5.422483642942e+06"
              hdg="5.287405485081e+00"
              length="6.565893957370e+01">
        <paramPoly3 aU="0.000000000000e+00"
                    bU="1.000000000000e+00"
                    cU="-4.666602734948e-09"
                    dU="-2.629787927644e-08"
                    aV="0.000000000000e+00"
                    bV="1.665334536938e-16"
                    cV="-1.987729787588e-04"
                    dV="-1.317158625579e-09"
                    pRange="arcLength">
        </paramPoly3>
    </geometry>
</planView>
```

**Rules**

The following rules apply to parametric cubic curves:

* [asam.net:xodr:1.7.0:road.geometry.paramPoly3.valid\_parameters](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-geometry-parampoly3-valid-parameters): The local u/v coordinate system should be aligned with the s/t coordinate system of the start point (meaning that the curve starts in the direction given by @hdg, and at the position given by @x and @y). To achieve this, the polynomial parameter coefficients have to be @aU=@aV=@bV=0, @bU>0.

* [asam.net:xodr:1.7.0:road.geometry.paramPoly3.arcLength\_range](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-geometry-parampoly3-arclength-range): If @pRange="arcLength", p shall be chosen in [0, @length from `<geometry>`].

* [asam.net:xodr:1.7.0:road.geometry.paramPoly3.normalized\_range](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-geometry-parampoly3-normalized-range): If @pRange="normalized", p shall be chosen in [0, 1].

* [asam.net:xodr:1.7.0:road.geometry.paramPoly3.length\_match](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-geometry-parampoly3-length-match): The actual curve length, as determined by numerical integration over the parameter range, should match @length.

**Related topics**

* [Section 8.5, "Georeferencing"](../08_coordinate_systems/08_05_geo_referencing.html#top-3535a746-e0af-4020-b71c-3a94e7a855a1)
* [Section 9.1, "Introduction to geometries"](09_01_introduction.html#top-0631e31d-eb24-470d-b767-a22e21dac50d)
* [Section 9.7, "Cubic polynom (deprecated)"](09_07_poly3.html#top-2f3fb62e-d0be-4eb8-a0f6-8bc0d6f6d953)
* [Section 10.1, "Introduction to roads"](../10_roads/10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)

## 9.6.1 Generating roads using parametric cubic curves

Generating road courses with parametric cubic curves only require x- and y-coordinates.
For reasons of consistency to cubic polynomials, they may be calculated simultaneously to cubic polynomials using local u- and v-coordinates.

`u(p) = aU + bU*p + cU*p2 + dU*p³`  
`v(p) = aV + bV*p + cV*p2 + dV*p³`

The mandatory @pRange specifies whether the interpolation parameter p is in the range [0, 1] ("normalized") or, alternatively, in the range [0, @length of `<geometry>`] ("arcLength").
The local coordinate system with the variables u and v may be placed and oriented arbitrarily.

To simplify representation, the local coordinate system should be aligned with the s/t coordinate system at the start point (@x,@y) and start orientation @hdg:

* The u-axis points in local s-direction, meaning along the road reference line at the start point.
* The v-axis points in local t-direction, meaning in lateral deviation from the road reference line at the start point.
* The parameters @aU, @aV and @bV shall be zero, @bU shall be > 0.

Providing non-zero values for the parameters @aU, @aV and @bV leads to a shift and rotation of the s/t coordinates as shown [Figure 29](#fig-9a7c32eb-ea76-4f17-9d1e-8445ee53d91b), [Figure 30](#fig-4c29c6d1-e115-441e-8580-0e73a32059a1) and [Figure 31](#fig-6ddce25c-ac8f-408d-9ee9-5a22a24e0cd7).

After defining the points of the curve for a given parameter p, the u-values and v-values are transformed into values of the x/y coordinate system with regard to the shifts and orientation specified by the parameters @aU, @aV, @bU, @bV, the start coordinates (@x,@y) and the start orientation @hdg.

|  |  |
| --- | --- |
|  | There is a non-linear relation between the interpolation parameter p and the actual length of the arc between the start point (@x,@y) in the `<geometry>` element and the point (x(p),y(p)) associated with the parameter `p`. In general, only the startpoint and endpoint parameter p=0 and p=@length (for the option @pRange=arcLength) coincides with the actual length of the arc. |

Taking into account shift and rotation parameters @a and @b and the (@x,@y) and @hdg specified in the `<geometry>` element, the final x/y curve position is located at a given u-coordinate, as shown in [Figure 35](09_07_poly3.html#fig-4f08e8e2-e5e5-44df-9a2f-8dfde65f3881).

![img](../_images/09_geometry/param_poly_1.png)

Figure 29. A parametric cubic curve for interpolation of the u-coordinate

![img](../_images/09_geometry/param_poly_2.png)

Figure 30. A parametric cubic curve for interpolation of the v-coordinate

![img](../_images/09_geometry/param_poly_3.png)

Figure 31. A parametric cubic curve