# ASAM OpenDRIVE® v1.9.0 — 8.4 Local coordinate systems

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/08_coordinate_systems/08_04_local_coordinate_system.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.4 Local coordinate systems

The local coordinate system is a right-handed coordinate system according to ISO 8855 with the axes pointing to the following directions.
For a non-rotated coordinate system the following applies:

|  |  |
| --- | --- |
| u | Forward matches s |
| v | Left matches t |
| z | Up matches h |

![img](../_images/08_coordinate_systems/coo_sys_local.png)

Figure 18. Local coordinate system with defined rotations

[Figure 18](#fig-3ce150eb-1dee-4380-94ac-e9021e56f35b) shows the positive axes and positive directions of the corresponding angles and how elements, such as objects, can be placed within the local coordinate system by applying a heading, followed by pitch, followed by roll.

Within the local coordinate system, the following angles are defined:

|  |  |
| --- | --- |
| heading | around z-axis, 0.0 = east |
| heading = 0.0: | u’ is directed forward along u-direction |
| heading = +π/2: | u’ is directed to t |
|  |  |
| pitch | around v’-axis, where |
| pitch = 0.0: | u’’/v’’ plane = u’/v’ plane |
|  |  |
| roll | around u’’-axis, where |
| roll = 0.0: | u’’’/v’’’ plane = u’’/v’’ plane |

![img](../_images/08_coordinate_systems/coo_sys_local_example.png)

Figure 19. Local coordinate systems with heading, pitch, roll

[Figure 19](#fig-70e4801c-e784-460a-87f6-4633bca1efd8) shows how heading, pitch, and roll are applied to the local coordinate system.

![img](../_images/08_coordinate_systems/coo_sys_all_1.png)

Figure 20. Local coordinate system with respect to road reference line coordinate system

[Figure 20](#fig-fa173c34-aff9-4df6-944a-16cfdfa5a567) shows how the local coordinate system can only be positioned in road reference line space by providing the origin of the local coordinate system within the road reference line coordinate system and the orientation (heading) of the local coordinate system with respect to the road reference line coordinate system.