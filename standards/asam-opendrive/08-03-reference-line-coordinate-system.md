# ASAM OpenDRIVE® v1.9.0 — 8.3 Road reference line coordinate systems

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/08_coordinate_systems/08_03_reference_line_coordinate_system.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.3 Road reference line coordinate systems

The road reference line is always located within the x/y plane defined by the inertial coordinate system.
A road reference line coordinate system runs along the road reference line.
It is a right-handed coordinate system.
The s-axis follows the tangent of the road reference line.
The t-axis is orthogonal to the s-axis and may be rotated around the s-axis by superelevation.
The right-handed coordinate system is completed by defining the up-direction `h` orthogonal to s-axis and t-axis.

![img](../_images/08_coordinate_systems/ref_line_sys.png)

Figure 13. Road reference line coordinate system

[Figure 13](#fig-eb7c93c8-4980-4c6a-ac98-f6c8734c56a6) shows the degrees of freedom defined for the road reference line coordinate system.

The following degrees of freedom are defined:

|  |  |
| --- | --- |
| s | coordinate along road reference line, measured in [m] from the beginning of the road reference line, calculated in the x/y plane (that is, not taking into account the elevation profile of the road) |
| t | lateral position, perpendicular to the road reference line and angled relative to the x/y plane according to the road superelevation. Positive to the left of the road reference line. |
| h | orthogonal to s/t plane in a right-handed coordinate system |
| heading | rotation around h-axis |
| superelevation | rotation around s-axis |

![img](../_images/08_coordinate_systems/ref_line_sys_rot.png)

Figure 14. Road reference line coordinate system with defined rotations

[Figure 14](#fig-cb64f5fc-c581-4868-81f6-de9a964893a6) shows the different states of a road reference line coordinate system with defined rotations.

Similar to the inertial coordinate system, the s’/t’/h’ and ssuperelevation/tsuperelevation/hsuperelevation denote the rotated coordinate systems around heading and superelevation angle.

![img](../_images/08_coordinate_systems/ref_line_sys_heading.png)

Figure 15. Heading in road reference line

[Figure 15](#fig-fdc5b5f7-13f2-4063-b3eb-eaa8c36e79f9) shows how the road reference line coordinate system can be positioned in the inertial space by providing the origin’s coordinates and the orientation (heading) of the origin with respect to the inertial coordinate system.

![img](../_images/08_coordinate_systems/ref_line_sys_superele.png)

Figure 16. Roll in road reference line by superelevation

[Figure 16](#fig-5ba9fa4a-ae86-4bd0-a566-ec4336bc21a5) shows how superelevation causes a roll in the road reference line.
Values of t are measured in the superelevated lane.
The value of the @width attribute of the lane does not change if superelevation is applied.
The projected width in the x/y plane is different to the width of the superelevated lane.

![img](../_images/08_coordinate_systems/ref_line_sys_ele.png)

Figure 17. Elevation in road reference line

[Figure 17](#fig-92f8e3fe-a832-4696-a0cf-5de31cc54dfa) shows the elevation for road reference line coordinate systems.
For the s/t/h coordinate system no pitch is possible.
Elevation has no effect on the length of s.

|  |  |
| --- | --- |
|  | In ASAM OpenDRIVE®, objects and signals are placed in their own s/t-coordinate system and are not rotated by superelevation, they specify their position relative to the road reference line and then can be rotated individually. Their @t attribute is rotated with the lane affected only by superelevation, so an object or signal placed at the border of a lane stays at this border regardless of superelevation or not. Their @zOffset attribute is calculated in z-direction, a value of `0` means the object or signal is placed at the local elevation at this s-position. In order to place the object or signal on the road surface and take the superelevation into account, the @zOffset attribute has to match the height offset caused by the superelevation at this position. |