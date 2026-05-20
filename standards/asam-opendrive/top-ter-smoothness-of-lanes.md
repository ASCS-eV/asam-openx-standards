# ASAM Opendrive v1.9.0 — Annex D: Additional rules (normative)

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/smoothness_of_lanes/top_ter_smoothness_of_lanes.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex D: Additional rules (normative)

Some Rules can not be defined in a chapter, as they cover multiple chapters.

## D.1 Smoothness of lanes (normative)

This chapter contains rules regarding lane smoothness.

For vehicles to be able to drive along OpenDRIVE files, the lanes should be smooth.
There should be no gaps or kinks.
Therefore, this chapter applies only to drivable lanes.

The following `@type` of `<lanes>` are drivable lanes:

* driving
* entry
* exit
* onRamp
* offRamp
* connectingRamp
* slipLane
* biking, only advisory lanes are seen as drivable lanes.
* border
* stop
* restricted

Drivable lanes that are marked as deprecated:

* HOV
* bidirectional
* bus
* mwyEntry
* mwyExit
* roadWorks
* taxi

|  |  |
| --- | --- |
|  | These lane types may be configurable in the Checker Tool in the future. These are checked within the  [ASAM Quality Checker Framework](https://github.com/asam-ev/qc-framework). |

To determine the smoothness of lanes, several different ASAM OpenDRIVE contents needs to be considered.
The following elements are relevant, including their respective contents:

* `<planView>`
* `<elevationProfile>`
* `<lateralProfile>`
* `<lanes>` with `<laneOffset>`, `<width>` or `<border>`, `<height>`
* `@level` attribute
* `<elevationGrid>`

As critical transitions, all lane sections need to be taken into account.
Also relevant are the linkages of roads, lanes and junctions.

### D.1.1 Touching Points

In order to determine if a lane is smooth, its touching points needs to be found.

The touching points of a lane are the starting and end positions of the lane at its inner and outer edges.
A touching point has a position in x, y, z and a heading, pitch and roll.

Example of touching points.

![img](../../_images/Annex/SoL_RoadLinkage.png)

Figure 148. Touching Points between 2 logically connected roads

![img](../../_images/Annex/SoL_LaneSections.png)

Figure 149. Touching Points within laneSections

![img](../../_images/Annex/SoL_JunctionLinkage.png)

Figure 150. Touching Points for connecting roads

![img](../../_images/Annex/SoL_Multiple_Successors.png)

Figure 151. Touching Points for multiple lane linkage

The yellow point can not have a horizontal gap by definition, as in ASAM OpenDRIVE there are no gaps between lanes horizontally.
Also for vertical gaps the yellow point makes no difference for the vertical gap calculations.

In the text below the word 'match' is used.
If two touching points 'match', they are not mathematically identical.
There will likely be small differences mathematically due to floating points or different formulas used within ASAM OpenDRIVE.

### D.1.2 Horizontal gaps

#### D.1.2.1 s-direction

* Two connected drivable lanes shall have no horizontal gaps.
* There is no gap between two connected lanes in s-direction if the x,y values of the touching points of the two connected lanes match.
* There shall be no plan view gaps in its reference line geometry definition.

#### D.1.2.2 t-direction

* By definition of ASAM OpenDRIVE there can be no horizontal gaps in t-direction.

### D.1.3 Horizontal kinks

#### D.1.3.1 s-direction

* Two connected drivable lanes shall have no horizontal kinks.
* There is a kink between two connected lanes in s-direction if the x,y of the touching points of the two connected lanes match, but the headings of the connected lanes do not match.
* There shall be no kinks in its reference line geometry definition.
* The reference line direction needs to be taken into account here.

#### D.1.3.2 t-direction

* By definition of ASAM OpenDRIVE there can be no horizontal kinks in t-direction.

### D.1.4 Vertical gaps

#### D.1.4.1 s-direction

* Two connected drivable lanes shall have no vertical gaps.
* There is a gap between two connected lanes in s-direction if the z and/or roll values of the touching points of the two connected lanes do not match.
* There shall be no vertical gaps in the elevation definition and lateral profile definition of the road.

#### D.1.4.2 t-direction

* With `<lateralProfile>` vertical gaps can be defined.
* There should be no jumps of drivable lanes in the t direction.

### D.1.5 Vertical kinks

#### D.1.5.1 s-direction

* Two connected drivable lanes should have no vertical kinks.
* There is a kink between two connected lanes in s-direction, if the z values of the touching points of the two connected lanes match, but the pitch values of the touching points of the connected lanes do not match.

#### D.1.5.2 t-direction

With `<lateralProfile>` vertical kinks can be defined.
\* There may be kinks of drivable lanes in t direction.

\*Related topics

* [Section 10.3, "Road linkage"](../../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)
* [Section 10.5, "Road elevation methods"](../../10_roads/10_05_elevation.html#top-1d8329bd-9550-4482-9e04-6c75bb5b492a)
* [Section 11.6, "Lane linkage"](../../11_lanes/11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd)
* [Section 11.8.1, "Lane type"](../../11_lanes/11_08_lane_properties.html#sec-79c983d6-db57-41ad-85f7-4643c25910dc)
* [Section 12.1, "Introduction to junctions"](../../12_junctions/12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)

## D.2 Performance

**Rules**

* [asam.net:xodr:1.8.1:performance.avoid\_redundant\_info](../map_rules.html#asam-net-xodr-1-8-1-performance-avoid-redundant-info): Redundant elements should be avoided, such as elevation or laneSection nodes for consecutive s-coordinates with identical attributes, or multiple geometry nodes for straight lines.

**Related topics**

* [Section 9.1, "Introduction to geometries"](../../09_geometries/09_01_introduction.html#top-0631e31d-eb24-470d-b767-a22e21dac50d)
* [Section 10.1, "Introduction to roads"](../../10_roads/10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)
* [Section 11.1, "Introduction to lanes"](../../11_lanes/11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)