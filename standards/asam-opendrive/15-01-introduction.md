# ASAM Opendrive v1.9.0 — 15.1 Introduction to railroads

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/15_railroads/15_01_introduction.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 15.1 Introduction to railroads

In addition to roads, ASAM OpenDRIVE offers the possibility to model rail-based transport systems, that is, trams, and streetcars.
ASAM OpenDRIVE cannot be used for complex railway networks and railway signals.
ASAM OpenDRIVE describes rail networks only where roads and railroad tracks meet.

**Elements in UML model**

**`<railroad>` element**

In ASAM OpenDRIVE, railroads are represented by the `<railroad>` element within the `<road>` element.

```
UML class: t_road_railroad
XML tag:   <railroad> (Multiplicity: 0..1)
```

Container for all railroad definitions that shall be applied along a road.

The available set of railroad elements is currently limited to the definition of switches.
All other entries shall be covered with the existing elements, for example, track definition by `<road>`, signal definition by `<signal>`, etc.
Railroad-specific elements are defined against the background of streetcar applications.

![img](../_images/uml_class_diagrams/EAID_6B1CED55_51A4_4c21_978B_35F9092CC559.png)

Figure 143. UML class diagram of the Railroad class

[Figure 143](#fig-cb539359-0b87-4ef7-a951-621b77da3bb4) shows the UML class diagram of the ASAM OpenDRIVE Railroad class.

**Rules**

The following rules apply to railroads:

* Each railroad track requires one road.

**Related topics**

* [Section 15.2, "Railroad tracks"](15_02_railroad_tracks.html#top-bd13c77a-7b58-416c-9449-7c1dcf43497e)
* [Section 15.3, "Switches"](15_03_switches.html#top-bc2ab6c7-071a-41b5-b183-c9dd80e372f4)
* [Section 15.4, "Stations"](15_04_stations.html#top-049863be-26b9-4c34-9991-ac8ad690c8be)