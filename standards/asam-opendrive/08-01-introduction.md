# ASAM OpenDRIVE® v1.9.0 — 8.1 Introduction to coordinate systems

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/08_coordinate_systems/08_01_introduction.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.1 Introduction to coordinate systems

ASAM OpenDRIVE® uses three types of coordinate systems:

* The inertial x/y/z coordinate system
* The road reference line s/t/h coordinate system
* The local u/v/z coordinate system

![img](../_images/08_coordinate_systems/coo_sys_overview.png)

Figure 7. Available coordinate systems in ASAM OpenDRIVE®

[Figure 7](#fig-67a7a638-8746-44f4-a574-e05908306350) shows the three coordinate systems.

These coordinate systems may interact with each other, if present.

![img](../_images/08_coordinate_systems/coo_sys_interact.png)

Figure 8. Coordinate systems in ASAM OpenDRIVE® interacting with another

[Figure 8](#fig-ecaff823-8bfa-4c03-b660-f7cc5873e843) shows how the three coordinate systems interact with each other and with respect to the road reference line.
If not indicated otherwise, the local coordinate system is located and oriented relative to the road reference line coordinate system.
The road reference line coordinate system is located and oriented relative to the inertial coordinate system by specifying the origin, as well as the heading, roll, and pitch rotation angles of the origins with respect to each other.

![img](../_images/08_coordinate_systems/coo_sys_all_2.png)

Figure 9. Summary of coordinate system in ASAM OpenDRIVE®

[Figure 9](#fig-9e277ae1-6e3d-4c60-b06e-839d1a0b2d75) shows an example for positioning and orientation of the different coordinate systems relative to each other from another perspective.

|  |  |
| --- | --- |
|  | Note that the local u/v/z coordinate system’s origin is located at the elevation at this position. |

![image](../_images/08_coordinate_systems/coo_sys_s-t-road-based.drawio.svg)

Figure 10. Reference-line-based s/t-coordinate system with origin at the beginning of the road

[Figure 10](#fig-c28e3855-aebe-46c3-92df-f9e40a4bf616) shows the road-based coordinate system that consists of two coordinate axes associated with the reference line of the corresponding road (s-axis) and the direction orthogonal to it (t-axis) and pointing leftwards.