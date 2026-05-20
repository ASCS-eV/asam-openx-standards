# ASAM Opendrive v1.9.0 — 10.6 Road CRG surface

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/10_roads/10_06_road_surface.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.6 Road CRG surface

The description of the surface of a road is part of ASAM OpenCRG, not ASAM OpenDRIVE.
It is possible to reference data created by ASAM OpenCRG in ASAM OpenDRIVE.
In ASAM OpenDRIVE, the road surface is represented by the `<surface>` element within the `<road>` element.
Data described in ASAM OpenCRG is represented by the `<CRG>` element within the `<surface>` element.

Neither ASAM OpenDRIVE nor ASAM OpenCRG contain data regarding the visual representation of the road surface.

![img](../_images/10_roads/road_surface.png)

Figure 49. Road surface as defined in a CRG file

[Figure 49](#fig-6d43db11-7e41-4663-b542-f9503789f937) shows how it is possible with ASAM OpenCRG to model detailed road surface attributes, for example cobble stone or pot holes.

Besides modeling of elevation, CRG data can also be used to model detailed friction values of the road (see [Section 10.6.5, “Defining friction using ASAM OpenCRG”](#sec-78c54dc8-77a5-4f62-bc2f-42c0e71e2723)).

As the name indicates, CRG (Curved Regular Grid) data is organized in a regular grid which is laid out along a reference line, which is comparable to ASAM OpenDRIVE’s road reference line.
At each grid position, it contains the absolute elevation measured along a real road and some additional data which allows for the computation of the delta elevation relative to the reference line.

![img](../_images/10_roads/opencrg_introductory_example.png)

Figure 50. ASAM OpenCRG road surface description using u/v coordinates and x/y coordinates

[Figure 50](#fig-ec62cd75-b6c7-4c7c-bc61-c9fa776ad049) shows the reference line and different coordinate systems of ASAM OpenCRG.

The key to combining ASAM OpenDRIVE and CRG data is to define a correlation between the two reference lines and a rule for using the elevation data of both descriptions.

![img](../_images/10_roads/crg_position_1.png)

Figure 51. Positioning of an ASAM OpenCRG file along the reference line

[Figure 51](#fig-686a36a5-5331-46a1-851a-59809f5d1baa) shows CRG data that may be offset from the ASAM OpenDRIVE road reference line using @tOffset and it may be oriented in the same or opposite direction as the layout direction of the road (see [Section 10.6.2, “Switching orientation”](#sec-58890351-a29c-49b3-9fe4-6178bb2a0a5a)).

## 10.6.1 Modes of combining ASAM OpenDRIVE and ASAM OpenCRG

The CRG data may be applied to a given ASAM OpenDRIVE road in different modes:

Table 32. Modes of connecting ASAM OpenCRG to ASAM OpenDRIVE


| Mode | ASAM OpenCRG reference line | Total height | Typical use case |
| --- | --- | --- | --- |
| attached | discarded | ASAM OpenDRIVE height plus ASAM OpenCRG height | Relative road height to road surface (including elevation, lateral profile, interpolated elevation grid, and lane height) |
| attached0 | discarded | ASAM OpenCRG height only | Absolute height measurement |
| genuine | shifted and rotated so beginning of reference line matches position given in ASAM OpenDRIVE | ASAM OpenCRG height only | Combining complete ASAM OpenCRG tracks (for example, racing tracks) with ASAM OpenDRIVE data |
| global | shifted and rotated by xOffset, yOffset, zOffset and hOffset | ASAM OpenCRG height only | On junctions |

### 10.6.1.1 @mode = attached

![img](../_images/10_roads/crg_attached.png)

Figure 52. ASAM OpenCRG attachment mode, attached

[Figure 52](#fig-510aa072-bc73-4ccd-8d47-2cbbccfd43db) shows the attachment mode `attached`.
The reference line of the CRG data set is replaced with the ASAM OpenDRIVE road reference line, taking into account the @tOffset and the @sOffset parameters.
The local CRG elevation values, which are calculated by evaluating the CRG grid and applying @zOffset and @zScale, are added to the surface elevation data of the ASAM OpenDRIVE road, which are derived from the combination of elevation, superelevation and crossfall.
With this mode, the surface information relative to the original CRG data reference line is transferred from an arbitrary CRG road to an ASAM OpenDRIVE road without having to make sure that the overall geometries of the road match.
The original position, heading, curvature, elevation and superelevation of the CRG road are disregarded.
The CRG grid is evaluated along the ASAM OpenDRIVE reference line instead of the CRG reference line.

![img](../_images/10_roads/crg_attached_2.png)

Figure 53. ASAM OpenCRG attached mode with elevation

[Figure 53](#fig-e5b6ab89-52bb-48fd-8f64-1eeed087b0d1) shows the calculation of the height.

The calculation looks as follows, assuming @orientation=same, and using the `crgEvaluv2z` function from the ASAM OpenCRG C-API and a hypothetical `laneHeightNoCRG` function, which returns what the lane height would be if the CRG file was not present:

\[\begin{align\*}
& \left( \begin{array}{rrr}
u \\
v \\
\end{array}\right)\_{CRG} =
\left( \begin{array}{rrr}
s - s\_{Offset} \\
t - t\_{Offset} \\
\end{array}\right)\_{OpenDRIVE}
\\
& \operatorname{totalHeight}(road, s, t) = \operatorname{crgEvaluv2z}(crg, u, v) \* z\_{Scale} + z\_{Offset} + \operatorname{laneHeightNoCRG}(road, s, t)
\end{align\*}\]

### 10.6.1.2 @mode = attached0

This mode is the same as the attached mode, with the exception that only the CRG data elevation value is considered (that is, the ASAM OpenDRIVE elevation is set to zero).

![img](../_images/10_roads/crg_attached0.png)

Figure 54. ASAM OpenCRG attached0 mode with elevated reference line

To avoid problems, set @sStart and @sEnd exactly to the CRG data boundaries.
[Figure 54](#fig-022bce88-4812-4317-a0e9-43484592d2c0) shows the case when the @sStart or the @sEnd attributes are not set to the exact boundaries and therefore do not cover the CRG data boundaries.
Otherwise this results in inconsistencies in the road surface.

The height calculation is very similar to `attached`, again assuming @orientation=same:

Formula for mode attached0

\[\begin{align\*}
& \left( \begin{array}{rrr}
u \\
v \\
\end{array}\right)\_{CRG} =
\left( \begin{array}{rrr}
s - s\_{Offset} \\
t - t\_{Offset} \\
\end{array}\right)\_{OpenDRIVE}
\\
& \operatorname{totalHeight}(road, s, t) = \operatorname{crgEvaluv2z}(crg, u, v) \* z\_{Scale} + z\_{Offset}
\end{align\*}\]

### 10.6.1.3 @mode = genuine

![img](../_images/10_roads/crg_genuine.png)

Figure 55. ASAM OpenCRG attachment mode, genuine

[Figure 55](#fig-fb28ac87-b3b6-4ec1-ac44-88d29be95045) shows the attachment mode `genuine`.
The start point of the CRG data set reference line is positioned relative to the point on the ASAM OpenDRIVE road reference line at the position defined by @sStart, @sOffset and @tOffset.
By providing offset values for the longitudinal (@sOffset) and lateral (@tOffset) displacement, the heading (@hOffset) and the elevation (@zOffset), the correlation between the two descriptions reference lines is clear.
In genuine mode, the CRG data replace the ASAM OpenDRIVE elevation data, that is, the absolute elevation of a given point of the road surface is directly computed from the CRG data.
When using this method, it must be assured that the geometry of the CRG data matches – within certain tolerance – the geometry of the underlying ASAM OpenDRIVE road.

The height of a given `(x,y)` position on the lane is calculated as displayed below.

The calculation uses the following helper functions:

* `st2xyh` takes a `x/y`-coordinate on the road, and returns the world `x/y`-coordinate, in addition to the heading angle of the reference line at the given `s`-position.
* `crgEvalxy2z` is the function from the ASAM OpenCRG C API.
* `REFERENCE_LINE_START_X`, `REFERENCE_LINE_START_Y` and `REFERENCE_LINE_START_PHI` are road parameters from the CRG file.
* `sOffset`, `tOffset`, `hOffset`, `zOffset` and `zScale` are attributes from the `<CRG>` element.

\[\begin{align\*}
& (x\_{StartCRG}, y\_{StartCRG}, h\_{StartCRG}) = \operatorname{st2xyh}(road, s\_{Offset}, t\_{Offset})
\\
& h\_{RotAngle} = h\_{StartCRG} + h\_{Offset} - REFERENCE\\_LINE\\_START\\_PHI
\\
& \left( \begin{array}{rrr}
x\_{CRG} \\
y\_{CRG} \\ \end{array}\right) =
\left( \begin{matrix}{}
\cos(h\_{RotAngle}) & \sin(h\_{RotAngle}) \\
-\sin(h\_{RotAngle}) & \cos(h\_{RotAngle}) \\
\end{matrix}\right)
\left( \begin{array}{rrr}
x\_{OpenDRIVE} - x\_{StartCRG} \\
y\_{OpenDRIVE} - y\_{StartCRG} \\
\end{array}\right) + \left( \begin{array}{rrr}
REFERENCE\\_LINE\\_START\\_X \\
REFERENCE\\_LINE\\_START\\_Y \\ \end{array}\right)
\\
& \operatorname{totalHeight}(x\_{OpenDRIVE}, y\_{OpenDRIVE}) = \operatorname{crgEvalxy2z}(crg, x\_{CRG}, y\_{CRG}) \* z\_{Scale} + z\_{Offset}
\end{align\*}\]

### 10.6.1.4 @mode = global

The CRG data set is referenced from a given track or a junction record but no translatory or rotatory transformation is applied, except for the xyz and heading offsets defined by the @xOffset, @yOffset, @zOffset and @hOffset attributes.
All data in the CRG file remains in its native coordinate system.
Elevation data is interpreted as inertial data, that is, AS IS.
The ASAM OpenDRIVE height is ignored.
This can be used to define heights for junctions.
This is also the only mode that can be applied directly to `<junction>` elements without a junction reference line.

The height of a given `(x,y)` position on the lane is calculated as follows:

Formula for global mode

\[\begin{align\*}
& \left( \begin{array}{rrr}
x\_{CRG} \\
y\_{CRG} \\ \end{array}\right) =
\left( \begin{matrix}{}
\cos(h\_{Offset}) & \sin(h\_{Offset}) \\
-\sin(h\_{Offset}) & \cos(h\_{Offset}) \\
\end{matrix}\right)
\left( \begin{array}{rrr}
x\_{OpenDRIVE} - x\_{Offset} \\
y\_{OpenDRIVE} - y\_{Offset} \\
\end{array}\right)
\\
& \operatorname{totalHeight}(x\_{OpenDRIVE}, y\_{OpenDRIVE}) = \operatorname{crgEvalxy2z}(crg, x\_{CRG}, y\_{CRG}) \* z\_{Scale} + z\_{Offset}
\end{align\*}\]

## 10.6.2 Switching orientation

In modes `attached` and `attached0`, ASAM OpenCRG files can be rotated by 180 degrees, via the @orientation attribute:

![img](../_images/10_roads/crg_orientation.png)

Figure 56. ASAM OpenCRG orientation

[Figure 56](#fig-4fe3d8f0-6e5d-4b72-a641-18e1f16d27a3) shows the switching orientation states.

It is calculated as follows:

\[\left( \begin{array}{rrr}
u \\
v \\
\end{array}\right)\_{CRG} =
\left( \begin{matrix}
0 & -1 \\
-1 & 0 \\
\end{matrix}\right)
\left( \begin{array}{rrr}
s - s\_{Offset} \\
t - t\_{Offset} \\
\end{array}\right)\_{OpenDRIVE}\]

The @orientation attribute rotates the CRG file at the origin of the u/v coordinate system of the ASAM OpenCRG.
The value `same` has a rotation angle of 0° and the value `opposite` has a value of 180°.
The t-offset is not affected by the @orientation attribute.

## 10.6.3 Combining ASAM OpenCRG with superelevation

When using modes `attached0`, `genuine` or `global`, the height of the road is determined purely based on the CRG file.
It can still be useful (and is allowed by this standard) to add `<elevation>`, `<superelevation>`, `<height>` elements and similar to the road, to approximate the road height for tools not supporting ASAM OpenCRG.

|  |  |
| --- | --- |
|  | Elements, such as `<superelevation>`, do not influence the road height in modes `attached0`, `genuine` or `global`, but they still influence other parts of the road, for example, `<superelevation>` tilt the `t`-axis, and change the projected width of the lane on the ground (see [Section 10.5.1, "Superelevation"](10_05_elevation.html#sec-4abf7baf-fb2f-4263-8133-ad0f64f0feac)). The calculation for mode `attached0` uses the s/t coordinates as input (see the [Formula for mode attached0](#crg-mode-attached0-formula)). The conversion from x/y coordinates to s/t coordinates always takes `<superelevation>` and similar elements into account. |

## 10.6.4 Using ASAM OpenCRG on junctions

In principle, ASAM OpenCRG files can be added to junctions the same way they can be added to other roads with the help of a junction reference line or, depending on the mode, by attaching it directly to the `<junction>` element, see  [Section 12.12, "Junction CRG surface"](../12_junctions/12_12_junction_crg_surface.html#top-9c1db57b-4325-472d-9c29-14e4872aa123).

|  |  |
| --- | --- |
|  | `@mode=global` was invented for junctions, but may also be used outside of junctions. |

## 10.6.5 Defining friction using ASAM OpenCRG

CRG files can also be used to define friction values for the roads.
To do this, set @purpose to `friction`.

Friction values are calculated similarly to elevation values (see formulas above).

**Rules**

The following additional rules apply:

* [asam.net:xodr:1.7.0:road.crg.attach\_vs\_friction](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-crg-attach-vs-friction): `@mode=attached` shall not be used together with `@purpose=friction`.

* [asam.net:xodr:1.7.0:road.crg.friction\_no\_z\_offset\_scale](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-crg-friction-no-z-offset-scale): `@zOffset` and `@zScale` shall not be set for friction values.

The formulas are calculated as if `@zOffset=0` and `@zScale=1`.

That means, if a CRG file with @purpose=friction is added to a road, the values from the CRG file directly replace the friction value set via the `<material>` element, see [Section 11.8.2, "Lane material"](../11_lanes/11_08_lane_properties.html#sec-8345bf25-d584-4a5b-8fa7-e15c920ab219).

## 10.6.6 List of attributes and rules

**Elements in UML model**

**`<surface>` element**

In ASAM OpenDRIVE, the road surface is represented by the `<surface>` element within the `<road>` element.

```
UML class: t_road_surface
XML tag:   <surface> (Multiplicity: 0..1)
```

Contains a series of elements describing a surface.

**`<CRG>` element**

In ASAM OpenDRIVE, the CRG data is represented by the `<CRG>` element within the `<surface>` element.

```
UML class: t_road_surface_CRG
XML tag:   <CRG> (Multiplicity: 0..*)
```

Links road surface data defined according to ASAM OpenCRG format.

Table 33. Attributes of the <CRG> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `file` | string | required |  |  | Name of the file containing the CRG data |
| `hOffset` | double | optional | rad |  | Heading offset between CRG center line and reference line of the road (for mode genuine) or global coordinate system (for mode global). Not allowed in other modes. (default = 0.0). |
| `mode` | [e\_road\_surface\_CRG\_mode](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_A6071BD4_9A19_4bd9_9DCA_2EF127ED6D8F) | required |  |  | Attachment mode for the surface data, see specification. |
| `orientation` | [e\_direction](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_EE7BA5A8_72F5_411a_AD27_89495B78140C) | required |  |  | Orientation of the CRG data set relative to the parent `<road>` element. Only allowed for mode attached and attached0. |
| `purpose` | [e\_road\_surface\_CRG\_purpose](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_4555C4E5_3092_4672_9948_5E3A41CB86DD) | optional |  |  | Physical purpose of the data contained in the CRG file; if the attribute is missing, data will be interpreted as elevation data. |
| `sEnd` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m |  | End of the application of CRG  (s-coordinate) |
| `sOffset` | double | optional | m |  | s-offset between CRG center line and reference line of the road   (default = 0.0) |
| `sStart` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m |  | Start of the application of CRG data  (s-coordinate) |
| `tOffset` | double | optional | m |  | t-offset between CRG center line and reference line of the road  (default = 0.0) |
| `xOffset` | double | optional | m | 1.9.0 | x-offset for translating the CRG center line (default = 0.0). Only allowed for mode global. |
| `yOffset` | double | optional | m | 1.9.0 | y-offset for translating the CRG center line (default = 0.0). Only allowed for mode global. |
| `zOffset` | double | optional | m |  | z-offset between CRG center line and reference line of the road or the global coordinate system (for mode global) (default = 0.0). Only allowed for purpose elevation. |
| `zScale` | double | optional |  |  | z-scale factor for the surface description (default = 1.0). Only allowed for purpose elevation. |

**XML example**

```
<surface>
    <CRG file="fancyData.crg"
         sStart="0.0"
         sEnd="100.0"
         orientation="same"
         mode="attached"
         tOffset="0.0" />
</surface>
```

|  |  |
| --- | --- |
|  | * Because CRG data may only cover parts of a road’s surface, it must be made sure that outside the valid CRG area, the elevation information derived from ASAM OpenDRIVE data can still be used.  * [asam.net:xodr:1.7.0:road.crg.only\_on\_per\_s](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-crg-only-on-per-s): In the future, multiple CRG files at one position may be combined. For compatibility with future versions, each road or junction should only contain one CRG file per `s`-position and @purpose.  * ASAM OpenCRG files only have an effect on those roads or junctions from which they are referenced (and only between `sStart` and `sEnd` on that road).   Example: if one road references a CRG file in global mode, then only this road is influenced by the CRG file.   Other roads are not affected, even if the CRG file overlapped the road. * If the calculations of the CRG u/v coordinates or x/y coordinates lead to coordinates outside of the defined area of the CRG file, then the normal CRG mechanisms, for example, `BORDER_MODE_U` and `BORDER_MODE_V`, applies and decide which value is returned. * CRG files may be referenced multiple times with different parameters.   For example, CRG file may be placed in mode genuine multiple times, with different `zScale` values.   This should be considered in the implementation, for example, by NOT applying the `SCALE_Z_GRID` upon loading the CRG file, but by doing the calculation outside the CRG library so that multiple instantiations of the same file can share the data in the CRG library. |

**Rules**

The following rules apply to the use of CRG data in ASAM OpenDRIVE:

* [asam.net:xodr:1.7.0:road.crg.use\_last\_entry](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-crg-use-last-entry): If more than one CRG entry is given for the same physical property (attribute purpose) at a given location, then the last entry in the sequence of occurrence in the ASAM OpenDRIVE file shall be the relevant one. All others are ignored (but see the [note](#Note_CRG)).

* [asam.net:xodr:1.7.0:road.crg.junction](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-crg-junction): If a `<junction>` element contains a `<CRG>` element, none of the connecting roads that belong to this junction shall have a `<CRG>` element.

* [asam.net:xodr:1.7.0:road.crg.no\_opposite](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-crg-no-opposite): @orientation=opposite shall not be used for modes other than @mode=attached and @mode=attached0.

* [asam.net:xodr:1.9.0:road.crg.h\_offset\_only\_genuine\_global](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-crg-h-offset-only-genuine-global): @hOffset shall not be used for modes other than @mode=genuine and @mode=global.

* [asam.net:xodr:1.7.0:road.crg.s\_t\_offset\_no\_global](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-crg-s-t-offset-no-global): @sOffset and @tOffset shall not be used with @mode=global.

**Related topics**

* [Section 10.1, "Introduction to roads"](10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)