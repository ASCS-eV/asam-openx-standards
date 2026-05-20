# ASAM OpenDRIVE® v1.9.0 — 12.9 Junction reference line

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_09_junction_reference_line.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.9 Junction reference line

Junction reference lines are geometric references related to junctions.
A junction reference line is defined in the reference line coordinate system.
A junction reference line attaches the `<elevationGrid>` element and other relevant objects to the junction, for example traffic islands or potholes.
A junction reference line has no lanes and no elevation or superelevation.

![img](../_images/12_junctions/junction_reference_line.png)

Figure 97. Junction reference line ~red arrow~

[Figure 97](#fig-298faa87-6415-4285-8c8f-8e9c10bb8c97) shows a junction and a junction reference line.

In ASAM OpenDRIVE®, junction reference lines are represented by the `<planView>` element within the `<junction>` element.

```
UML class: t_road_planView
XML tag:   <planView> (Multiplicity: 1)
```

Contains geometry elements that define the layout of the road reference line in the x/y-plane (plan view).

**`<geometry>` element**

In ASAM OpenDRIVE®, the geometry of a junction reference line is represented by the `<geometry>` element within the `<planView>` element.

```
UML class: t_road_planView_geometry
XML tag:   <geometry> (Multiplicity: 1..*)
```

Table 76. Attributes of the <geometry> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `hdg` | double | required | rad | Start orientation (inertial heading) |
| `length` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | required | m | Length of the element’s reference line |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position |
| `x` | double | required | m | Start position (x inertial) |
| `y` | double | required | m | Start position (y inertial) |

The `<planView>` element contains one `<geometry>` element with the `<line>` element.

**XML example**

```
<junction id="15">
    <planView>
        <geometry s="0.0000000000000000e+00"
                  x="3.0505642010572856e+01"
                  y="3.6353713565101820e+01"
                  hdg="2.9842438203363086e-01"
                  length="7.5257400000000004e+01">
            <line/>
        </geometry>
    </planView>
    <object type="roadSurface" subtype="pothole" name="" id="1" s="3.1064163564293011e+01" t="1.6886219784199805e+00" zOffset="0.0000000000000000e+00" validLength="0.0000000000000000e+00" orientation="none" length="0.3179999999999999e+00" width="0.4229999999999999e+00" height="0.0000000000000000e+00" hdg="5.7401170550235827e+00" pitch="0.0000000000000000e+00" roll="0.0000000000000000e+00">
        <surface>
          <CRG file="pothole.crg" hideRoadSurfaceCRG="true" zScale="1"/>
        </surface>
      </object>
</junction>
```

**Rules**

The following rules apply to junction reference lines:

* [asam.net:xodr:1.8.0:junctions.geometry.only\_one\_line\_element](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-geometry-only-one-line-element): Junction reference lines shall be defined by one `<geometry>` element. This `<geometry>` element shall have only one `<line>` element.

* [asam.net:xodr:1.8.0:junctions.geometry.ref\_line\_definition](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-geometry-ref-line-definition): The `<geometry>` element of a junction reference line shall be defined in a way that every point of the junction can be reached with a perpendicular straight line.

* [asam.net:xodr:1.8.0:junctions.geometry.correct\_junction\_boundry](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-junctions-geometry-correct-junction-boundry): If a junction boundary is specified, a junction reference line shall cross the junction boundary or be at least tangent to the junction boundary at one point.

**Related topics**

* [Section 12.11, "Junction elevation grid"](12_11_junction_elevation_grid.html#top-26a9b5c3-a1f1-4958-b8da-4ce704ae96fc)
* [Section 12.10, "Junction boundary"](12_10_junction_boundary.html#top-6d1f0b2f-282b-4d48-a920-be13f75706a3)