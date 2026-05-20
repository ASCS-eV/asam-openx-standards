# ASAM OpenDRIVE® v1.9.0 — 9.2 Road reference line

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/09_geometries/09_02_road_reference_line.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.2 Road reference line

The basic element of every road in ASAM OpenDRIVE® is the road reference line.
All geometry elements that describe the road shape and further properties of the road are defined along the road reference line.
These properties include lanes and signals.

By definition, the road reference line runs in s-direction, while the lateral deviation of objects from the road reference line runs in t-direction.
The direction of the road reference line does not indicate the driving direction.

![img](../_images/09_geometry/road_elements.png)

Figure 24. Individual parts of a road

[Figure 24](#fig-848bb044-6489-46f2-b236-009368db449a) shows the different parts of a road in ASAM OpenDRIVE®.

* The road reference line
* Individual lanes of a road
* Features like signals that are placed along the road

**Elements in UML model**

![img](../_images/uml_class_diagrams/EAID_8A007E88_354E_463e_9D40_944248350DFB.png)

Figure 25. UML class diagram of the RoadGeometry class, including the road reference line elements

[Figure 25](#fig-e050d43d-eba2-49d7-a75e-29ba31d301e8) shows the UML class diagram of the ASAM OpenDRIVE® RoadGeometry class.

**`<planView>` element**

In ASAM OpenDRIVE®, the plan view is represented by the `<planView>` element within the `<road>` element.
The `<planView>` element is a mandatory element in every `<road>` element.

```
UML class: t_road_planView
XML tag:   <planView> (Multiplicity: 1)
```

Contains geometry elements that define the layout of the road reference line in the x/y-plane (plan view).

**`<geometry>` element**

In ASAM OpenDRIVE®, the geometry of a road reference line is represented by the `<geometry>` element within the `<planView>` element.

```
UML class: t_road_planView_geometry
XML tag:   <geometry> (Multiplicity: 1..*)
```

Table 18. Attributes of the <geometry> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `hdg` | double | required | rad | Start orientation (inertial heading) |
| `length` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | required | m | Length of the element’s reference line |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position |
| `x` | double | required | m | Start position (x inertial) |
| `y` | double | required | m | Start position (y inertial) |

**Rules**

The following rules apply to road reference lines:

* [asam.net:xodr:1.4.0:road.geometry.refline\_exists](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-geometry-refline-exists): Each road shall have a road reference line.

* [asam.net:xodr:1.4.0:road.geometry.only\_one\_refline](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-geometry-only-one-refline): There shall be only one road reference line per road.

* The road reference line usually runs in the center of the road but may be laterally offset.

* [asam.net:xodr:1.4.0:road.geometry.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-geometry-elem-asc-order): `<geometry>` elements shall be defined in ascending order along the road reference line according to the s-coordinate.

* [asam.net:xodr:1.4.0:road.geometry.one\_geom\_elem\_per\_spec](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-geometry-one-geom-elem-per-spec): One `<geometry>` element shall contain only one element that further specifies the geometry of the road.

* [asam.net:xodr:1.7.0:road.geometry.contact\_point](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-geometry-contact-point): If two roads are connected without a junction, the road reference line of a new road shall always begin at the `<contactPoint>` element of its successor or predecessor road. The road reference lines may be directed in opposite directions.

* [asam.net:xodr:1.4.0:road.geometry.refline\_no\_gaps](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-geometry-refline-no-gaps): A road reference line shall have no gaps.

* [asam.net:xodr:1.4.0:road.geometry.refline\_no\_kinks](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-geometry-refline-no-kinks): A road reference line should have no kinks.

* [asam.net:xodr:1.9.0:road.geometry.s-value\_sum](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-geometry-s-value-sum): The s-value of each `<geometry>` shall be the sum of all `<geometry>` lengths prior

**Related topics**

* [Section 9.3, "Straight line"](09_03_straight_line.html#top-74c133a9-fc15-4a00-ae49-9a4cdc20b742)
* [Section 9.4, "Spiral"](09_04_spiral.html#top-9807cfa9-04f5-4eca-b468-d68b71486666)
* [Section 9.5, "Arc"](09_05_arc.html#top-0d75cff2-4103-401f-a802-b5868d15a4fe)
* [Section 10.1, "Introduction to roads"](../10_roads/10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)
* [Section 11.1, "Introduction to lanes"](../11_lanes/11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)