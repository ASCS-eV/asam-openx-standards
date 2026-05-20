# ASAM Opendrive v1.9.0 — 10.2 Properties for road sections and cross section

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/10_roads/10_02_properties_for_road_sections.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 10.2 Properties for road sections and cross section

Some properties of roads are described based on the cross section of the road.
The road cross section is the orthogonal view of the road at a given point on the road reference line.
An example of a property that refers to the road cross section is superelevation.
Elements that are valid for a road cross section are valid for the whole width of the road at a given point on the road reference line.

Other road properties are described based on the plan view of the road.
This includes lanes and road elevation.
For these properties, the term road section is used.
Road sections describe parts of roads and their specific properties along the s-coordinate of the road reference line.
Properties that are valid for a road section may not be valid for the whole width of the road, but for specific lanes only.

That means it is possible to create sections for different properties like road type or lane sections.
Sections are created by an additional element within the `<road>` element, using new start s-coordinates.
The length of a section is implicitly given by the difference between two given s-start positions.
Sections shall be stored in ascending order of s-coordinates.