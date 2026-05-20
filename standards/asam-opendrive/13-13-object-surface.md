# ASAM Opendrive v1.9.0 — 13.13 Object CRG surface

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_13_object_surface.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.13 Object CRG surface

In driving simulators, the driver should be able to feel both the general road surface and specific, visible features on the road.
This includes manhole covers, cracks, and patches.
However, these require different resolutions, and it is impractical to model the entire road surface with a fine grid.

To support high-resolution surface features on a low-resolution road, the `<surface>` element may be included within the `<object>` element.

Objects with a defined `<surface>` element influence the height of the road, including elevation, lateral profile, interpolated elevation grid, and lane height.
The object’s surface height is added to the road height.
In the other direction, it is subtracted if the object’s surface height is negative.

Because CRG data may only cover parts of a road’s surface, it must be made sure that the elevation information derived from ASAM OpenDRIVE data can still be used outside of the valid CRG area.
Because the reference line of the CRG file for an object is ignored, a CRG file may be referenced multiple times in different parts of the map.
The local coordinate system of an object is rotated with the object.
The object surface is thus also rotated.

![img](../_images/13_objects/object_12.png)

Figure 127. CRG for objects

[Figure 127](#fig-bfdad4a4-9b91-4142-9e3f-1693c7512443) shows how CRG for objects is applied.
s/t is the road reference line coordinate system.
u/v is the CRG coordinate system.
The object’s center point is defined as the origin of the CRG coordinate system, which results in positive and negative u/v values.

**Elements in UML model**

**`<surface>` element**

In ASAM OpenDRIVE, object surfaces are represented by the `<surface>` element within the `<object>` element.

```
UML class:  t_road_objects_object_surface
XML tag:    <surface> (Multiplicity: 0..1)
Introduced: 1.7.0
```

Used to describe the road surface elevation of an object.

**`<CRG>` element**

In ASAM OpenDRIVE, ASAM OpenCRG data of object surfaces is represented by the <CRG> element within the <surface> element.

```
UML class:  t_road_objects_object_surface_CRG
XML tag:    <CRG> (Multiplicity: 0..1)
Introduced: 1.7.0
```

Elevation data described in ASAM OpenCRG are represented by the `<CRG>` element within the `<surface>` element.

Table 108. Attributes of the <CRG> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `file` | string | required | 1.7.0 | Name of the file containing the CRG data. |
| `hideRoadSurfaceCRG` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | required | 1.7.0 | Determines if the object CRG hides the road surface CRG. Default is true. |
| `zScale` | double | required | 1.7.0 | z-scale factor for the surface description (default = 1.0). |

**XML example**

```
<surface>
    <CRG file="manhole_cover.crg" hideRoadSurfaceCRG="true" zScale="1"></CRG>
</surface>
```

**Calculation**

If an ASAM OpenCRG file is referenced, the u/v coordinates of the object are used directly as u/v coordinates of the ASAM OpenCRG file.
The reference line of the CRG file is unused.

Thus, the surface height of an object is calculated as follows, using the `crgEvaluv2z` function from the ASAM OpenCRG C-API:

\[\operatorname{objectSurfaceHeight}(object, u, v) = \operatorname{crgEvaluv2z}(crg, u, v) \* z\_{Scale}\]

The total height at the point of an object CRG depends on the attachment mode of the underlying road surface CRG (`t_road_surface_CRG`), provided there is one.

Table 109. Total height calculation by attachment mode


| Road surface CRG attachment mode | hideRoadSurfaceCRG = true (default) | hideRoadSurfaceCRG = false |
| --- | --- | --- |
| attached | OpenDRIVE height + object CRG  400 | OpenDRIVE height + road surface CRG + object CRG  400 |
| attached0, genuine, global | not allowed  400 | road surface CRG + object CRG 400 |
| no road surface CRG | OpenDRIVE height + object CRG  400 | OpenDRIVE height + object CRG  400 |

[Table 110](#tab-bea7d535-f628-4299-a083-8fee726cea2) summarizes the calculations for the different combinations.
For a review of attachment modes, see [Table 32](../10_roads/10_06_road_surface.html#tab-8dd4bfa6-b06a-48be-8044-07887e2e811a), "Modes of connecting ASAM OpenCRG to ASAM OpenDRIVE" in  [Section 10.6, "Road CRG surface"](../10_roads/10_06_road_surface.html#top-7a0a2c4b-41a6-46e6-845e-932f2a014730).

If `crgEvaluv2z` returns NaN, then the object has no defined height at that position.
This is allowed in ASAM OpenCRG.
In this case, the height of the road at that position shall be identical to the height defined in the rest of this standard, as if the object CRG were not present.
The @hideRoadSurfaceCRG attribute has no effect at positions where `crgEvaluv2z` returns NaN.
This enables the use of non-rectangular objects together with the @hideRoadSurfaceCRG attribute, for example, manhole covers.

**Rules**

The following rules apply to the use of CRG data in objects:

* [asam.net:xodr:1.7.0:road.object.surface.only\_for\_angular\_boxes](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-surface-only-for-angular-boxes): Only objects with angular bounding volumes may contain `<surface>` elements. Circular objects or objects with `<outlines>` elements shall not contain `<surface>` elements.

* Outside the bounding volume, CRG data from the object shall be ignored.

* [asam.net:xodr:1.7.0:road.object.surface.no\_bounding\_box\_overlap](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-surface-no-bounding-box-overlap): The bounding volumes of objects with `<surface>` elements shall not overlap.

* [asam.net:xodr:1.7.0:road.object.surface.identical\_local\_coordinates](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-surface-identical-local-coordinates): The local coordinate system of the CRG shall be identical to the local coordinate system of the object to which it belongs. The reference line, inertial position, curvature, and heading of the CRG file shall be ignored.

* [asam.net:xodr:1.7.0:road.object.surface.object\_reference\_on\_overlap](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-surface-object-reference-on-overlap): An object with a `<surface>` element shall be referenced on all roads it overlaps, using `<object>` and `<objectReference>` elements.

* [asam.net:xodr:1.7.0:road.object.surface.only\_one\_crg\_file](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-surface-only-one-crg-file): An object shall not reference more than one CRG file.

* [asam.net:xodr:1.7.0:road.object.surface.repeat\_discretely\_not\_continously](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-surface-repeat-discretely-not-continously): Objects with `<surface>` elements may repeat discretely, but not continuously. See  [Section 13.4, "Repeating objects"](13_04_repeating_objects.html#top-fc693ed2-a38b-4cfc-a346-90c8a478bfd0).

* [asam.net:xodr:1.9.0:road.object.surface.avoid\_skewed\_crg\_surfacees](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-surface-avoid-skewed-crg-surfacees): To avoid skewed CRG surfaces, the @perpToRoad attribute should only be used for objects that are smaller than the local radius of the curvature of the road elevation.

* The @height and @zOffset attributes of an object with a `<surface>` element shall be ignored when calculating the surface elevation.

* [asam.net:xodr:1.7.0:road.object.surface.crg\_hidden\_on\_object\_overlap](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-surface-crg-hidden-on-object-overlap): If a road surface CRG is present, that is, the CRG area overlaps the bounding volume of the object and has any mode other than attached, then @hideRoadSurfaceCRG shall be false.

* [asam.net:xodr:1.7.0:road.object.surface.calculate\_road\_height](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-surface-calculate-road-height): If `crgEvaluv2z` returns NaN, then the road height at that position shall be the ASAM OpenDRIVE height in addition to the road surface CRG, if it is present. The value of @hideRoadSurfaceCRG attribute shall have no influence.The value of @hideRoadSurfaceCRG attribute shall have no influence.

**Related topics**

* [Section 10.6, "Road CRG surface"](../10_roads/10_06_road_surface.html#top-7a0a2c4b-41a6-46e6-845e-932f2a014730)
* [Section 12.12, "Junction CRG surface"](../12_junctions/12_12_junction_crg_surface.html#top-9c1db57b-4325-472d-9c29-14e4872aa123)