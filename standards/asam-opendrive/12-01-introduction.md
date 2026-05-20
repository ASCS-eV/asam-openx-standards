# ASAM Opendrive v1.9.0 — 12.1 Introduction to junctions

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_01_introduction.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.1 Introduction to junctions

Junctions enable the connection of more than two roads.

Four types of junctions exist:

* Common junctions are junctions with drivable lanes that can overlap and where traffic can cross.
* Direct junctions are junctions where traffic can change roads but cannot cross other traffic.
* Virtual junctions are junctions where the main road is not interrupted.
* Crossings are junctions where traffic cannot change the roads.

Table 54. Usage of the different types of junctions


| Use case | Overlapping lanes | Crossing traffic | Changing roads | Junction type | Alternative junction type |
| --- | --- | --- | --- | --- | --- |
| ordinary junctions | yes | yes | yes | common | n/a |
| junctions with traffic lights | yes | yes | yes | common | n/a |
| entries and exits | no | no | yes | direct | common (not recommended) |
| yes | no | yes | if constant elevation: direct, otherwise: common | common |
| yes | yes | yes | common | n/a (direct not possible) |
| driveways to parking lots | yes | yes | yes | if constant elevation: virtual, otherwise: common | common |
| driveways to residential estates | yes | yes | yes | if constant elevation: virtual, otherwise: common | common |
| slip lanes | no | no | yes | combination of one common and many direct | common |
| yes | no | yes | if constant elevation: combination of one common and many direct, otherwise: many common | common |
| railway crossing | yes | yes | no | crossing | common |

![img](../_images/uml_class_diagrams/EAID_522853C6_A091_462c_9784_E01118BD53AB.png)

Figure 84. UML class diagram of the Junction class

[Figure 84](#fig-8b7e2624-7c2f-4771-9e00-284dc2067532) shows the UML class diagram of the ASAM OpenDRIVE Junction class.

**Rules**

The following rules apply to junctions:

* [asam.net:xodr:1.4.0:junctions.no\_overlap](../16_annexes/map_rules.html#asam-net-xodr-1-4-0-junctions-no-overlap): No junctions of any type shall overlap each other.

* [asam.net:xodr:1.7.0:junctions.type\_direct\_no\_conn\_road](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-type-direct-no-conn-road): The `<connection>` element of a junction of @type="direct" shall not have the @connectingRoad attribute.

* [asam.net:xodr:1.7.0:junctions.type\_default\_no\_linked\_road](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-junctions-type-default-no-linked-road): The `<connection>` element of a junction of @type="default" or @type="virtual" shall not have the @linkedRoad attribute.