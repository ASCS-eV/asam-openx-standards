# ASAM OpenDRIVE® v1.9.0 — 9.1 Introduction to geometries

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/09_geometries/09_01_introduction.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.1 Introduction to geometries

Road courses can have many different shapes.
There are long, straight roads on open ground, elongated curves on motorways, or narrow turns in the mountains.
In order to model all these road courses in a mathematically correct way, ASAM OpenDRIVE® provides a variety of geometry elements:

* Straight lines
* Spirals or clothoids with a linearly changing curvature
* Arcs with a constant curvature
* Parametric cubic polynomials
* Cubic polynomials (deprecated)

![img](../_images/09_geometry/geom_overview.png)

Figure 22. Geometry elements in ASAM OpenDRIVE®

[Figure 22](#fig-c2164748-80cf-4567-8d85-0c0b39f57429) shows the five possible ways to define the geometry of a road reference line.

The combination of all geometry elements available in ASAM OpenDRIVE® allows for the creation of a great variety of road courses.

**XML example**

![img](../_images/09_geometry/adding_primitives.png)

Figure 23. Example for creating a road reference line from geometry elements

[Figure 23](#fig-1cc37e26-9f90-48c9-9081-fcddc9395512) shows the example of a road reference line consisting of one line, two arcs, and two spiral elements.

|  |  |
| --- | --- |
|  | To avoid leaps in the curvature, spirals should be used to connect line elements with arc elements. |

* [Ex\_Line-Spiral-Arc.xodr](../_attachments/examples/Ex_Line-Spiral-Arc/Ex_Line-Spiral-Arc.xodr)