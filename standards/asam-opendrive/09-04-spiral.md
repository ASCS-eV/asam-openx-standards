# ASAM Opendrive v1.9.0 — 9.4 Spiral

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/09_geometries/09_04_spiral.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.4 Spiral

A spiral is a clothoid that describes a changing curvature of the road reference line.

![img](../_images/09_geometry/spiral.png)

Figure 27. Road geometry described by a spiral

[Figure 27](#fig-6f6de31c-b273-410a-a245-5c3f40fd48ab) shows the concept of a spiral.
Spirals may be used to describe the transition from a `<line>` element to an `<arc>` element without causing leaps in the curvature.

A spiral is characterized by the curvature at its start position (@curvStart) and the curvature at its end position (@curvEnd).
Along the arc length of the spiral (see @length of the `<geometry>` element), the curvature is linear from the start to the end.

It is also possible to arrange several `<line>`, `<spiral>`, and `<arc>` elements in a sequence in order to describe complex curvatures.

**Elements in UML model**

**`<spiral>` element**

In ASAM OpenDRIVE, a spiral is represented by the `<spiral>` element within the `<geometry>` element.

```
UML class: t_road_planView_geometry_spiral
XML tag:   <spiral>
```

Spirals or more specifically Euler spirals also known as clothoids.
They describe road reference lines with constantly changing curvatures.

Table 19. Attributes of the <spiral> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `curvEnd` | double | required | 1/m | Curvature at the end of the element.  Positive curvature: left curve (counter-clockwise motion) Negative curvature: right curve (clockwise motion) |
| `curvStart` | double | required | 1/m | Curvature at the start of the element.   Positive curvature: left curve (counter-clockwise motion) Negative curvature: right curve (clockwise motion) |

**XML example**

```
<geometry s="100.0" x="38.00" y="-1.81" hdg="0.33" length="30.00">
    <spiral curvStart="0.0" curvEnd="0.013"/>
</geometry>
```

**Rules**

The following rules apply to spirals:

* [asam.net:xodr:1.9.0:road.geometry.spiral.curvature\_change](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-geometry-spiral-curvature-change): @curvStart and @curvEnd should not be the same.

**Related topics**

* [Section 9.1, "Introduction to geometries"](09_01_introduction.html#top-0631e31d-eb24-470d-b767-a22e21dac50d)
* [Section 9.2, "Road reference line"](09_02_road_reference_line.html#top-9cb15835-ff9e-4b51-9bc8-730a3695fde9)
* [Section 9.5, "Arc"](09_05_arc.html#top-0d75cff2-4103-401f-a802-b5868d15a4fe)
* [Section 10.1, "Introduction to roads"](../10_roads/10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)