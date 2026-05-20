# ASAM Opendrive v1.9.0 — 8.5 Georeferencing

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/08_coordinate_systems/08_05_geo_referencing.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.5 Georeferencing

Spatial reference systems are standardized by the European Petroleum Survey Group Geodesy (EPSG:32632 WGS 84 / UTM zone 32N [[17](../bibliography.html#bib-epsg32632)]) and are defined by parameters describing the geodetic datum.
A geodetic datum is a coordinate reference system for a collection of positions that are relative to an ellipsoid model of the earth.

A geodetic datum is described by a projection string according to PROJ, that is, a format for the exchange of data between two coordinate systems.
This data shall be marked as CDATA, because it may contain characters that interfere with the XML syntax of an element’s attribute.

![img](../_images/08_coordinate_systems/geo_ref.png)

Figure 21. geoReference and offset

[Figure 21](#fig-575a3505-1d2b-4cbc-b940-c42454b4ff8e) shows the relation between ASAM OpenDRIVE coordinates and geo referenced data.
The used spatial reference system is defined by PROJ-strings.
For detailed information on PROJ-strings see the documentation of the *PROJ coordinate transformation software library* [[18](../bibliography.html#bib-PROJ_2023)].

It is highly recommended to use official parameter sets for PROJ-strings that can be found at *EPSG.io* [[19](../bibliography.html#bib-epsgio)].
Parameters should not be changed.
Some spatial reference systems, for example, UTM, have implicit false easting and northing that are defined using the parameters `+x_0` and `+y_0`.

To apply an offset, use the `<offset>` element instead of changing parameter values of a projection definition because overwriting existing definitions may lead to unexpected behavior.
Alternatively define a custom projection using Transverse Mercator (TM).

If an offset exists, always apply the offset on the local ASAM OpenDRIVE coordinates to get the world coordinates before converting the positions using PROJ.

The offset is applied on an ASAM OpenDRIVE instance using an Affine Transformation with rotation around z-axis:

xWorld = xODR \* cos(hdg) - yODR \* sin(hdg) + xOffset

yWorld = xODR \* sin(hdg) + yODR \* cos(hdg) + yOffset

zWorld = zODR + zOffset

If no heading is supplied (recommended), the formulas simplify to:

xWorld = xODR + xOffset

yWorld = yODR + yOffset

zWorld = zODR + zOffset

**Elements in UML model**

**`<geoReference>` element**

In ASAM OpenDRIVE, the information about the geographic reference of an ASAM OpenDRIVE dataset is represented by the `<geoReference>` element within the `<header>` element.

```
UML class: t_header_GeoReference
XML tag:   <geoReference> (Multiplicity: 0..1)
```

Spatial reference systems are standardized by the European Petroleum Survey Group Geodesy (EPSG) and are defined by parameters describing the geodetic datum.
A geodetic datum is a coordinate reference system for a collection of positions that are relative to an ellipsoid model of the earth.

A geodetic datum is described by a projection string according to PROJ, that is, a format for the exchange of data between two coordinate systems.
This data shall be marked as CDATA, because it may contain characters that interfere with the XML syntax of an element’s attribute.

**`<offset>` element**

In ASAM OpenDRIVE, the offset of a database is represented by the `<offset>` element within the `<header>` element.

```
UML class: t_header_Offset
XML tag:   <offset> (Multiplicity: 0..1)
```

To avoid large coordinates, an offset of the whole dataset may be applied using the `<offset>` element.
It enables inertial relocation and re-orientation of datasets.
The dataset is first translated by @x, @y, and @z.
Afterwards, it is rotated by @hdg around the new origin.
Rotation around the z-axis should be avoided.

Table 17. Attributes of the <offset> element


| Name | Type | Use | Unit | Description |
| --- | --- | --- | --- | --- |
| `hdg` | double | required | rad | Heading offset (rotation around resulting z-axis) |
| `x` | double | required | m | Inertial x offset |
| `y` | double | required | m | Inertial y offset |
| `z` | double | required | m | Inertial z offset |

**XML example**

```
<geoReference>
    <![CDATA[+proj=utm +zone=32 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs]]>
</geoReference>
```

**Rules**

* [asam.net:xodr:1.9.0:header.proj.max\_one\_proj](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-header-proj-max-one-proj): There shall be no more than one definition of the projection. If the definition is missing, a local Cartesian coordinate system is assumed.

* [asam.net:xodr:1.7.0:header.offset.centered\_coords](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-header-offset-centered-coords): The `<offset>` element should be such that the x and y coordinates of ASAM OpenDRIVE are approximately centered around (0;0). If the x and y coordinates are too large, applications using float coordinates internally might not be able to process them accurately enough due to the limited precision of IEEE 754 double precision floating point numbers.