# ASAM Opendrive v1.9.0 — 10.4 Road type

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/10_roads/10_04_road_type.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.4 Road type

The road type defines the main purpose of a road and the associated traffic rules.
Example road types are motorways and rural roads.
The road type is valid for the entire road cross section.

The road type may be changed as often as needed within a `<road>` element.
This may be done by defining different road types at given points along the road reference line.
One road type remains valid until another road type is defined.

**Elements in UML model**

**`<type>` element**

In ASAM OpenDRIVE, the road type is represented by the `<type>` element within the `<road>` element.

```
UML class: t_road_type
XML tag:   <type> (Multiplicity: 0..*)
```

A road type element is valid for the entire cross section of a road.
It is valid until a new road type element is provided or until the road ends.

Table 25. Attributes of the <type> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `country` | [e\_countryCode](../16_annexes/map_uml_data_types.html#top-EAID_7A0922E5_0B9A_4a52_8063_A2499579DB20) | optional |  | Country code of the road, see ISO 3166-1, alpha-2 codes. |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | s-coordinate of start position |
| `type` | [e\_roadType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_3A3FB3DD_D0CF_43a7_95D6_30D9D024D0D9) | required |  | Type of the road defined as enumeration |

**Rules**

The following rules apply to road types:

* [asam.net:xodr:1.4.0:road.type.create\_new\_type\_in\_parent](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-type-create-new-type-in-parent): When the type of road changes, a new `<type>` element shall be created within the parent `<road>` element.

* Country code and state identifier may be added to the `<type>` element to specify which national traffic rules apply to this road type.
  The according data is stored in the application and not in ASAM OpenDRIVE.

* [asam.net:xodr:1.7.0:road.type.only\_alpha\_2\_country\_codes](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-type-only-alpha-2-country-codes): There shall only be ALPHA-2 country codes in use, no ALPHA-3 country codes, because only ALPHA-2 country codes support state identifiers.

* [asam.net:xodr:1.4.0:road.type.lane\_type\_may\_differ\_from\_parent](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-type-lane-type-may-differ-from-parent): Single lanes may have another type than the road they belong to. Road type and lane type represent different properties and are both valid if specified.

* [asam.net:xodr:1.4.0:road.type.elem\_asc\_order](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-road-type-elem-asc-order): `<type>` elements shall be defined in ascending order according to the s-coordinate.

**Related topics**

* [Section 10.2, "Properties for road sections and cross section"](10_02_properties_for_road_sections.html#top-1323a74c-b102-4fdd-bc02-63265f034f45)
* [Section 11.8.1, "Lane type"](../11_lanes/11_08_lane_properties.html#sec-79c983d6-db57-41ad-85f7-4643c25910dc)

## 10.4.1 Speed limits for road types

A speed limit may be defined for a road type.
When the road type changes and a speed limit exists on that road section, a new `<speed>` element is required, because road types have no global valid speed limits unless provided by [`<defaultRegulations>`](../06_general_architecture/06_04_header.html#sec-27ad621f-1b2a-40d6-8723-b9f8aa00cb3f).
The speed limit shall be defined for each `<type>` element of a road separately.

**Elements in UML model**

**`<speed>` element**

In ASAM OpenDRIVE, the speed limit is represented by the `<speed>` element within the `<type>` element.

```
UML class: t_road_type_speed
XML tag:   <speed> (Multiplicity: 0..1)
```

Defines the default maximum speed allowed in conjunction with the specified road type.

Table 26. Attributes of the <speed> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `max` | [t\_maxSpeed](../16_annexes/map_uml_data_types.html#top-EAID_D2734936_A31D_4410_8CA6_F04AA0984531) | required | Maximum allowed speed. Given as string (only "no limit" / "undefined") or numerical value in the respective unit (see attribute unit). If the attribute unit is not specified, m/s is used as default. |
| `unit` | [e\_unitSpeed](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_491DC05E_01C6_49b3_83BE_A06DD81F9C35) | required | Unit of the attribute max. For values, see chapter “units”. |

**Rules**

The following rules apply to speed limits:

* A maximum speed may be defined as default value per `<type>` element of a road.
* Single lanes may have different speed limits than the road they belong to.
  They are defined as a lane `<speed>` element.
* Speed limits derived from signals shall always have preference.

**Related topics**

* [Section 10.2, "Properties for road sections and cross section"](10_02_properties_for_road_sections.html#top-1323a74c-b102-4fdd-bc02-63265f034f45)
* [Section 14.1, "Introduction to signals"](../14_signals/14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)
* [Section 11.8.1, "Lane speed limit"](../11_lanes/11_08_lane_properties.html#sec-866ad6d9-a026-4051-9a3a-5f94405a15f7)