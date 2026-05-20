# ASAM OpenDRIVE® v1.9.0 — 12.12 Junction CRG surface

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_12_junction_crg_surface.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.12 Junction CRG surface

In order to describe complex elevations within a junction on a very detailed level, a surface description for junctions can be specified.
This is accomplished by describing the junction surface in correspondence with the descriptions used in ASAM OpenCRG.
For junctions that are not flat but without a very detailed surface description, the `<elevationGrid>` should be used.

The CRG data may be applied to a given junction in different modes similar to a road, using the junction reference line specified by the `<planview>` element.

Table 81. Modes of connecting ASAM OpenCRG to ASAM OpenDRIVE®


| Mode | ASAM OpenCRG reference line | Total height | Typical use case |
| --- | --- | --- | --- |
| attached | discarded | ASAM OpenDRIVE® height plus ASAM OpenCRG height | Relative road height to road surface (including elevation, lateral profile, interpolated elevation grid, and lane height) |
| attached0 | discarded | ASAM OpenCRG height only | Absolute height measurement |
| genuine | shifted and rotated so beginning of reference line matches position given in ASAM OpenDRIVE® | ASAM OpenCRG height only | Combining complete ASAM OpenCRG tracks (for example, racing tracks) with ASAM OpenDRIVE® data |
| global | shifted and rotated by xOffset, yOffset, zOffset and hOffset | ASAM OpenCRG height only | On junctions |

|  |  |
| --- | --- |
|  | For a detailed explanation of the different modes, see  [Section 10.6, "Road CRG surface"](../10_roads/10_06_road_surface.html#top-7a0a2c4b-41a6-46e6-845e-932f2a014730). Instead of a road reference line use the junction reference line to place CRG data on the junction surface. |

**Elements in UML model**

**`<surface>` element**

In ASAM OpenDRIVE®, surfaces in a junction are represented by the `<surface>` element within the `<junction>` element and use the same information as the `<road>` element.

```
UML class: t_road_surface
XML tag:   <surface> (Multiplicity: 0..1)
```

Contains a series of elements describing a surface.

**`<CRG>` element**

In ASAM OpenDRIVE®, ASAM OpenCRG data of road surfaces is represented by the `<CRG>` element within the `<surface>` element.

```
UML class: t_road_surface_CRG
XML tag:   <CRG> (Multiplicity: 0..*)
```

Links road surface data defined according to ASAM OpenCRG format.

Table 82. Attributes of the <CRG> element


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

**Rules**

The following rules apply to junction CRG surfaces:

* Junction CRG surfaces shall use the junction reference line.
* When a `<junction>` element contains a `<surface>` element, the `<surface>` element supersedes all elevation data for connecting roads.

**Related topics**

* [Section 10.6, "Road CRG surface"](../10_roads/10_06_road_surface.html#top-7a0a2c4b-41a6-46e6-845e-932f2a014730)
* [Section 12.9, "Junction reference line"](12_09_junction_reference_line.html#top-c53f51c5-e3c1-4c7e-bc61-efdf4f0bf54c)
* [Section 12.11, "Junction elevation grid"](12_11_junction_elevation_grid.html#top-26a9b5c3-a1f1-4958-b8da-4ce704ae96fc)