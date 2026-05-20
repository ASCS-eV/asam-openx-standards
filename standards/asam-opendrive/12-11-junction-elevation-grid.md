# ASAM Opendrive v1.9.0 — 12.11 Junction elevation grid

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_11_junction_elevation_grid.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.11 Junction elevation grid

Elevation grids provide and overwrite elevation definitions for every point inside the junction boundary.
Elevation grids solve the issue of connecting roads with different z-values and gaps.
If a lane height (see [Section 11.7.1, "Lane height"](../11_lanes/11_07_lane_geometry.html#sec-d30c9ef9-cb82-4683-9fb6-6487e9dffd2f)) is present, the values are superimposed onto the grid values in order to model sidewalks etc.

An elevation grid is a coarse square grid with z-values at evenly spaced points.
Elevation grids do not replace ASAM OpenCRG.

An elevation grid requires the definition of complete squares outside the junction boundary in each direction.

The minimal elevation grid consists of four points with a z-value forming a square bounding box around the junction boundary.
This minimal elevation grid provides a plane with constant height, if the four points have the same z-value.

![img](../_images/12_junctions/elevation_grid_minimal_points.png)

Figure 100. Example of a minimal elevation grid attached to a junction reference line

[Figure 100](#fig-0a196cca-883a-45aa-bae0-20cd277e1dce) shows a junction reference line and an elevation grid with the center points C0,0 and C1,0 on the junction reference line and the points R0,0 and R1,0 right to it.

An elevation grid consisting of more smaller squares has a higher resolution and can define more complex elevation profiles.

![img](../_images/12_junctions/elevation_grid_points.png)

Figure 101. Example of an elevation grid with more points

[Figure 101](#fig-ad06ec7e-589d-490f-82de-3a84de96960c) shows a junction reference line and an elevation grid with points to the left and right of the junction reference line.

**Elements in UML model**

**`<elevationGrid>` element**

In ASAM OpenDRIVE, elevation grids are represented by the `<elevationGrid>` element within the `<junction>` element.

```
UML class:  t_junction_elevationGrid
XML tag:    <elevationGrid> (Multiplicity: 0..1)
Introduced: 1.8.0
```

An elevation grid is a coarse square grid with z-values at evenly spaced points.
Elevation grids do not replace OpenCRG.

Table 79. Attributes of the <elevationGrid> element


| Name | Type | Use | Unit | Introduced |
| --- | --- | --- | --- | --- |
| `gridSpacing` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | 1.8.0 |
| `sStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | 1.8.0 |

![img](../_images/uml_class_diagrams/EAID_B37C31C9_20D3_450d_9BA3_A32B2F47FA82.png)

Figure 102. UML class diagram of the ElevationGrid class

[Figure 102](#fig-aa1298c9-f078-4f90-addb-2d28de614923) shows the UML class diagram of the ASAM OpenDRIVE ElevationGrid class.

**`<elevation>` element**

In ASAM OpenDRIVE, z-values at distinct points to the left or the right of the junction reference line or directly on the junction reference line are represented by `<elevation>` elements within the `<elevationGrid>` element.

```
UML class:  t_junction_elevationGrid_elevation
XML tag:    <elevation> (Multiplicity: 0..*)
Introduced: 1.8.0
```

Defines the z-values at the regular grid points along the junction reference line.

Table 80. Attributes of the <elevation> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `center` | t\_junction\_grid\_position\_list | required | m | 1.8.0 | List of defined z-values. |
| `left` | t\_junction\_grid\_position\_list | optional | m | 1.8.0 | List of defined z-values from inside to outside. |
| `right` | t\_junction\_grid\_position\_list | optional | m | 1.8.0 | List of defined z-values from inside to outside. |

**XML example**

```
<junction>
    <elevationGrid sStart="1.35191514000e+00" gridSpacing="4.000000000e+00">
        <elevation left="5.0" center="5.0" right="5.0 5.0"/>
        <elevation left="5.0 5.0" center="5.0" right="5.0 5.0"/>
        <elevation left="5.0 5.0" center="5.0" right="5.0 5.0 5.0"/>
        <elevation left="5.0 5.0" center="5.0" right="5.0 5.0 5.0"/>
        <elevation left="5.05 5.0" center="5.1" right="5.05 5.0 5.0"/>
        <elevation left="5.1 5.0" center="5.2" right="5.1 5.0 5.0"/>
        <elevation left="5.05 5.0" center="5.1" right="5.05 5.0 5.0"/>
        <elevation left="5.0 5.0" center="5.0" right="5.0 5.0 5.0"/>
        <elevation center="5.0" right="5.0 5.0 5.0"/>
    </elevationGrid>
</junction>
```

**Rules**

The following rules apply to elevation grids:

* Elevation grids are currently only valid for common junctions.

* [asam.net:xodr:1.8.0:junctions.elevation\_grid.only\_one\_elev\_grid](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-elevation-grid-only-one-elev-grid): A junction shall have only one elevation grid.

* [asam.net:xodr:1.8.0:junctions.elevation\_grid.valid\_for\_entire\_boundry](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-elevation-grid-valid-for-entire-boundry): If a junction boundary is defined, the elevation grid shall be valid for the area enclosed by the junction boundary.

* [asam.net:xodr:1.8.0:junctions.elevation\_grid.perpendicular\_vectors](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-elevation-grid-perpendicular-vectors): The elevation grid shall be defined with vectors perpendicular to the junction reference line.

* The elevation grid shall be valid from the point where a traffic participant enters the junction boundary until it leaves the junction boundary on an outgoing road.
* The elevation grid outside the junction boundary is overwritten by a road passing the elevation grid.
  This does not apply to connecting roads, because they are inside the junction boundary.
* If an elevation grid is present, it shall override any elevation values derived from any roads that are part of the junction or its boundary.
* If a lane height is present, the values are superimposed onto the grid values.

* [asam.net:xodr:1.8.0:junctions.elevation\_grid.entry\_exit\_smoothness](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-elevation-grid-entry-exit-smoothness): For junction entries and exits, a smooth transition should be assured.

**Related topics**

* [Section 12.10, "Junction boundary"](12_10_junction_boundary.html#top-6d1f0b2f-282b-4d48-a920-be13f75706a3)
* [Section 12.9, "Junction reference line"](12_09_junction_reference_line.html#top-c53f51c5-e3c1-4c7e-bc61-efdf4f0bf54c)

## 12.11.1 Interpolation in the elevation grid

The z-values inside the junction boundary are calculated by bicubic interpolation.

![img](../_images/12_junctions/elevation_grid_interpolation_point.png)

Figure 103. Point P in the elevation grid

[Figure 101](#fig-ad06ec7e-589d-490f-82de-3a84de96960c) shows an elevation grid with point P.

1. Identify the corner points of the square around P and the points around these corner points.  
   Square around P: C3,0, R3,0, R4,0, C4,0.  
   Points around the square: L2,0, C2,0, R2,0, R2,1, R3,1, R4,1, R5,1, R5,0, C5,0, L5,0, L4,0, L3,0.

   ![img](../_images/12_junctions/elevation_grid_interpolation_points.png)

   Figure 104. Points around P relevant for interpolations
2. Calculate the cubic polynomial \(f(x) = dx^{3} + cx^{2} + bx + a\) through the points along each edge.

   Use the value `0` for the coefficients \(c\) and \(d\) of the polynomials if there are not enough support points in the elevation grid to calculate them.

   ![img](../_images/12_junctions/elevation_grid_interpolation_curves.png)

   Figure 105. Tangents and cubic splines relevant for interpolation
3. Calculate the (mixed) partial derivative of the cubic polynomials at each point in s-, t-, and st-direction.
4. Apply a bicubic interpolation using the tangents and the cubic polynomials to calculate the z-value of P.

**Calculation**

Scale and shift the points C3,0, C4,0, R3,0, R4,0 to get the normalized points \((0,0,z\_{C\_{3,0}}), (1,0,z\_{C\_{4,0}}), (0,1,z\_{R\_{3,0}}), (1,1,z\_{R\_{4,0}})\) for the calculation.

The calculation of the z-value at P uses the following parts:

1. The matrix \(Z\)

   \[\begin{align\*}
   Z=\begin{bmatrix}
   z\_{C\_{3,0}} & z\_{C\_{4,0}}\\
   z\_{R\_{3,0}} & z\_{R\_{4,0}}
   \end{bmatrix}
   \end{align\*}\]

   where

   |  |  |
   | --- | --- |
   | \(z\_{C\_{3,0}}\) | is the z-value at C3,0 |
   | \(z\_{C\_{4,0}}\) | is the z-value at C4,0 |
   | \(z\_{R\_{3,0}}\) | is the z-value at R3,0 |
   | \(z\_{R\_{4,0}}\) | is the z-value at R4,0 |
2. The matrix \(T\_{t}\) of the tangents in t-direction:

   \[\begin{align\*}
   T\_{t}=\begin{bmatrix}
   T\_{t}(C\_{3,0}) & T\_{t}(C\_{4,0})\\
   T\_{t}(R\_{3,0}) & T\_{t}(R\_{4,0})
   \end{bmatrix}
   \end{align\*}\]
3. The matrix \(T\_{s}\) of the tangents in s-direction:

   \[\begin{align\*}
   T\_{s}=\begin{bmatrix}
   T\_{s}(C\_{3,0}) & T\_{s}(C\_{4,0})\\
   T\_{s}(R\_{3,0}) & T\_{s}(R\_{4,0})
   \end{bmatrix}
   \end{align\*}\]
4. The matrix \(T\_{st}\) of the tangents in st-direction:

   \[\begin{align\*}
   T\_{st}=\begin{bmatrix}
   T\_{st}(C\_{3,0}) & T\_{st}(C\_{4,0})\\
   T\_{st}(R\_{3,0}) & T\_{st}(R\_{4,0})
   \end{bmatrix}
   \end{align\*}\]
5. The constant matrix \(A\):

   \[\begin{align\*}
   A=\begin{bmatrix}
   1 & 0 & 0 & 0\\
   0 & 0 & 1 & 0\\
   -3 & 3 & -2 & -1\\
   2 & -2 & 1 & 1\\
   \end{bmatrix}
   \end{align\*}\]
6. The constant \(\alpha\) for the interpolation inside the same square:

   \[\begin{align\*}
   \alpha = A⋅
   \begin{bmatrix}
   Z & T\_{t}\\
   T\_{s} & T\_{st}\\
   \end{bmatrix}
   ⋅ A^{T}
   \end{align\*}\]

Scale and shift s/t coordinates of point P according to the scale and shift used for the square.

The z-value at scaled and shifted s/t coordinates calculates as:

\[\begin{align\*}
z(s,t) =
\begin{bmatrix}
1 & s & s^{2} & s^{3}
\end{bmatrix}
⋅
\alpha
⋅
\begin{bmatrix}
1 & t & t^{2} & t^{3}
\end{bmatrix}^{T}
\end{align\*}\]

**Rules**

* [asam.net:xodr:1.8.0:junctions.elevation\_grid.polynome\_coefficient\_values](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-elevation-grid-polynome-coefficient-values): The coefficients \(c\) and \(d\) of the polynoms shall be `0` if there are not enough support points in the elevation grid to calculate them.

## 12.11.2 Interpolation between incoming road and elevation grid

In order to get the smoothest possible transition from an incoming road to the elevation grid of a junction, a four-sided polygon serves as transition area wherein a cubic interpolation defines the elevation values.

The four sides of the polygon are derived from the segment element with @type="joint" of the junction boundary at the incoming road and the two segment elements with @type="lane" next to it.

![img](../_images/12_junctions/elevation_grid_transitionLength_points.png)

Figure 106. Three segments of a junction boundary and the corner points P0, P1, P2, and P3 of the polygon at an incoming road

The first side of the polygon corresponds to a line along the segment element with @type="joint": P0 to P1.
The second and third side of the polygon corresponds to the line between an endpoint of the first side and the point on the segment element with @type="lane" in the distance of the @transitionLength attribute of the segment element with @type="joint" along the corresponding segment element with @type="lane": P1 to P2 and P0 to P3.
The fourth side of the polygon is the line between the endpoints of the second and third sides: P2 to P3.

![img](../_images/12_junctions/elevation_grid_transitionLength_polygon.png)

Figure 107. Polygon and the lines AB and CD through the point P

1. Solve the following equations to calculate \(k\) and \(l\) and finally the points \(A\) and \(B\).

   \[\begin{align\*}
   A= P\_{0} + k ⋅ (P\_{1} - P\_{0})
   \end{align\*}\]

   \[\begin{align\*}
   B= P\_{3} + k ⋅ (P\_{2} - P\_{3})
   \end{align\*}\]

   \[\begin{align\*}
   P= A + l ⋅ (B - A)
   \end{align\*}\]
2. Replace \(A\) and \(B\).

   \[\begin{align\*}
   P= P\_{0} + k ⋅ (P\_{1} - P\_{0}) + l ⋅ (P\_{3} + k ⋅ (P\_{2} - P\_{3}) - (P\_{0} + k ⋅ (P\_{1} - P\_{0})))
   \end{align\*}\]

   \[\begin{align\*}
   P= P\_{0} + k ⋅ (P\_{1} - P\_{0}) + l ⋅ (P\_{3} - P\_{0}) + k ⋅ l ⋅ (P\_{2} - P\_{3} - P\_{1} + P\_{0})
   \end{align\*}\]
3. Rearrange the equation to set one side to `0`.

   \[\begin{align\*}
   k ⋅ l ⋅ (P\_{2} - P\_{3} - P\_{1} + P\_{0}) + k ⋅ (P\_{1} - P\_{0}) + l ⋅ (P\_{3} - P\_{0}) + (P\_{0} - P) = 0
   \end{align\*}\]
4. Make the following replacements to get two equations for x and y coordinates.

   \[\begin{align\*}
   \begin{matrix}
   with: & m = px\_{2} - px\_{3} - px\_{1} + px\_{0} & n = px\_{1} - px\_{0} & o = px\_{3} - px\_{0} & p = px\_{0} - px\\
   & q = py\_{2} - py\_{3} - py\_{1} + py\_{0} & r = py\_{1} - py\_{0} & s = py\_{3} - py\_{0} & t = py\_{0} - py
   \end{matrix}
   \end{align\*}\]

   Result:

   \[\begin{align\*}
   \begin{matrix}
   f\_{x}(k, l) & := & m ⋅ k ⋅ l & + & n ⋅ k & + & o ⋅ l & + & p & = & 0\\
   f\_{y}(k, l) & := & q ⋅ k ⋅ l & + & r ⋅ k & + & s ⋅ l & + & t & = & 0
   \end{matrix}
   \end{align\*}\]
5. Solve the equations for the variables \(k\) and \(l\).
6. Calculate the points \(A\) and \(B\).
   For point \(A\), the \(z\_{A}\) value and the gradient \(m\_{A}\) are calculated at the end of the incoming road.
   For point \(B\), the \(z\_{B}\) value and the gradient \(m\_{A}\) in the direction of vector \(AB\) are calculated from the elevation grid.
7. Normalize the gradients \(m\_{A}\) and \(m\_{B}\) by dividing them by the length of vector \(AB\).
8. Calculate the coefficients for a cubic interpolation.

   \[\begin{align\*}
   \begin{matrix}
   a = & z\_{A}\\
   b = & & & & & m\_{A}\\
   c = & -3 ⋅ z\_{A} & + & 3 ⋅ z\_{B} & - & 2 ⋅ m\_{A} & - & m\_{B}\\
   d = & 2 ⋅ z\_{A} & - & 2 ⋅ z\_{B} & + & m\_{A} & + & m\_{B}
   \end{matrix}
   \end{align\*}\]
9. Calculate \(z\) at point \(P\).

   \[\begin{align\*}
   \begin{matrix}
   z\_{P} (l) = a + b ⋅ l + c ⋅ l^{2} + d ⋅ l^{3} & with & l = [0..1]
   \end{matrix}
   \end{align\*}\]