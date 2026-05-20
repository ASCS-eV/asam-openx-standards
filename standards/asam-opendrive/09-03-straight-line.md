# ASAM Opendrive v1.9.0 — 9.3 Straight line

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/09_geometries/09_03_straight_line.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.3 Straight line

A straight line is the simplest geometry element.

![img](../_images/09_geometry/straight_line.png)

Figure 26. A straight line

[Figure 26](#fig-ad5e465b-d76c-4518-8a13-44e12ba0df64) shows the concept of a straight line.
A `<geometry>` element that forms a straight line contains the @s, @x, @y, @length, and @hdg attributes and one empty `<line>` element.

**Elements in UML model**

**`<line>` element**

In ASAM OpenDRIVE, a straight line is represented by the `<line>` element within the `<geometry>` element.

```
UML class: t_road_planView_geometry_line
XML tag:   <line>
```

A straight line is the simplest geometry element.
It contains no further attributes.

**XML example**

```
<planView>
    <geometry s="0.0000000000000000e+00"
              x="-4.7170752711170401e+01"
              y="7.2847983820912710e-01"
              hdg="6.5477882613167993e-01"
              length="5.7280000000000000e+01">
        <line/>
    </geometry>
</planView>
```

**Related topics**

* [Section 9.2, "Road reference line"](09_02_road_reference_line.html#top-9cb15835-ff9e-4b51-9bc8-730a3695fde9)
* [Section 10.1, "Introduction to roads"](../10_roads/10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)