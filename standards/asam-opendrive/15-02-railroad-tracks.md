# ASAM Opendrive v1.9.0 — 15.2 Railroad tracks

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/15_railroads/15_02_railroad_tracks.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 15.2 Railroad tracks

In ASAM OpenDRIVE, railroad tracks are always described in connection with the roads on which one pair of railroad track run.
It is not possible to define railroad tracks outside of roads.
Railroad tracks always need an own road.
They cannot share a road with other traffic elements.
Regardless of a tram or sharing the same space with non-railway traffic or separate of non-railway traffic, it always needs a separate road.

Railroad tracks are defined per lane using the @type attribute.
Because rail-based traffic differs from road traffic, the following recommendations apply to the modeling of railroads:

![img](../_images/15_railroads/railroads_1.png)

Figure 144. Road reference lines for roads and railroads

[Figure 144](#fig-b291ed3c-985a-4760-b514-46afde41fe9f) shows the difference between the use of the road reference line for roads and railroads.

In ASAM OpenDRIVE, railroad tracks are represented by the @type attribute within the `<lane>` element.
The values for railroad tracks are `tram` and `rail`.

**Rules**

The following rules apply to railroads:

* [asam.net:xodr:1.7.0:road.railroad.rail\_refline\_centered](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-rail-refline-centered): The road reference line shall be in the center of the pair of railroad tracks.

* [asam.net:xodr:1.7.0:road.railroad.one\_rail\_per\_road](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-one-rail-per-road): There shall only be one tram or one rail lane per road.

* [asam.net:xodr:1.7.0:road.railroad.rail\_lane\_width\_validity](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-railroad-rail-lane-width-validity): The width of the lane shall be at least the width rail-bound vehicles.

**Related topics**

* [Section 15.1, "Introduction to railroads"](15_01_introduction.html#top-cc907730-d1cf-4775-8d97-1898f533257b)
* [Section 15.3, "Switches"](15_03_switches.html#top-bc2ab6c7-071a-41b5-b183-c9dd80e372f4)