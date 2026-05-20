# ASAM OpenDRIVE® v1.9.0 — 8.2 Inertial coordinate systems

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/08_coordinate_systems/08_02_inertial_coordinate_system.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.2 Inertial coordinate systems

The inertial system is a right-handed coordinate system according to ISO 8855 [[9](../bibliography.html#bib-iso8855)] with the axes pointing to the following directions (see [Figure 11](#fig-6f953b3f-be4e-41cc-b7c0-6cf0f8937967)):

* x ⇒ right
* y ⇒ up
* z ⇒ coming out of drawing plane

For geographic reference, the following convention applies:

* x ⇒ east
* y ⇒ north
* z ⇒ up

Elements like objects and signals can be placed within the inertial coordinate system by applying a heading, followed by pitch, followed by roll:

![img](../_images/08_coordinate_systems/coo_sys_inertial.png)

Figure 11. Inertial coordinate system with defined rotations

[Figure 11](#fig-6f953b3f-be4e-41cc-b7c0-6cf0f8937967) shows the positive axes and positive directions of the corresponding angles.

|  |  |
| --- | --- |
| heading  heading = 0.0:  heading = +π/2: | around z-axis, where  x’ points into direction of x-axis / east  x’ points into direction of y-axis / north |
| pitch  pitch = 0.0:  pitch = +π/2: | around y’-axis, where  x’’/y’’ plane = x’/y’ plane  direction x’’ = - z’ = -z |
| roll   roll = 0.0:  roll = +π/2: | around x’’-axis, where  x’’’/y’’’ plane = x’’/y’’ plane  direction z’’’ = - y’’ |

![img](../_images/08_coordinate_systems/coo_sys_inertial_example.png)

Figure 12. Inertial coordinate system with defined rotations

[Figure 12](#fig-5d482d32-897e-4755-9439-f4740961192a) shows the different states of an inertial coordinate system with defined rotations.
x’/y’/(z’=z) denotes the coordinate system after rotating x/y/z with the heading angle around the z-axis.
The coordinate system x’’/(y’’=y’)/z’’ denotes the coordinate system after rotating x’/y’/z’ with the pitch angle around the y’-axis.
The final rotated coordinate system (x’’’=x’’)/y’’’/z’’’ is obtained after rotating system x’’/y’’/z’’ with roll angle.