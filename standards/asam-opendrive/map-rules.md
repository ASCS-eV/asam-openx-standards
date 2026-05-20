# ASAM Opendrive v1.9.0 — Annex F: Checker rules (normative)

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/map_rules.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex F: Checker rules (normative)

**Checker rule concept**

Checker rules are semantic and syntactic requirements that shall be applied to a scenario.
ASAM OpenDRIVE defines a basic set of rules that enforce compliance with the standard, as well as additional rules with recommendations in accordance with ASAM OpenDRIVE.
Rules consist of a name, an UID (a unique identifier of the check), and a description that specifies the requirements for the scenario.

**Rule UID Concepts**

The UID is a string that encapsulates a sequence of **concepts** that allow to identify immediately a rule across the different domains. The concepts are ordered and separated via the separation character **`:`**.

The concepts for a rule UID are:

* **Emanating Entity**: a domain name for the entity (organization or company) that declares the rule UID
* **Standard**: a short string that represents the standard or the domain to which the rule is applied
* **Definition Setting**: the version of the standard or the domain to which the rule appears or is applied **for the first time**
* **Rule Full Name**: the full name of the rule, as dot-separated, snake\_lower\_case string. The full name of a rule is composed by the **rule set**, a categorization for the rule, and the rule **name**, a unique string inside the categorization. The rule set can be nested (meaning that it can be defined as an arbitrary sequence of dot-separated names, while the name is the snake\_case string after the last dot of the full name)

To provide a visual description for a rule UID:

```
<emanating-entity>:<standard>:x.y.z:rule_set.for_rules.rule_name
```

|  |  |
| --- | --- |
|  | Third party rule UID creators (i.e., emanating entities different than ASAM) should still fill all the concepts above. If that is not possible, concepts shall be left blank, but separation `:` is still required (i.e., `example.com:::rulename` is valid). |

UIDs are designed to be queried, e.g., implementations may use UNIX pattern matching.

|  |  |
| --- | --- |
|  | Visit the  [ASAM Quality Checker Framework](https://github.com/asam-ev/qc-framework) documentation to see detailed information on how and which checks are implemented. |

## F.1 defaultRegulations

### F.1.1 only\_speed\_priority

UID
:   asam.net:xodr:1.8.0:defaultRegulations.only\_speed\_priority

Description
:   Only `<speed>` and `<priority>` elements shall be used within the `<defaultRegulations>` element.

## F.2 header

### F.2.1 offset

#### F.2.1.1 centered\_coords

UID
:   asam.net:xodr:1.7.0:header.offset.centered\_coords

Description
:   The `<offset>` element should be such that the x and y coordinates of ASAM OpenDRIVE are approximately centered around (0;0). If the x and y coordinates are too large, applications using float coordinates internally might not be able to process them accurately enough due to the limited precision of IEEE 754 double precision floating point numbers.

### F.2.2 proj

#### F.2.2.1 max\_one\_proj

UID
:   asam.net:xodr:1.9.0:header.proj.max\_one\_proj

Description
:   There shall be no more than one definition of the projection. If the definition is missing, a local Cartesian coordinate system is assumed.

## F.3 ids

### F.3.1 id\_unique\_in\_class

UID
:   asam.net:xodr:1.4.0:ids.id\_unique\_in\_class

Description
:   IDs shall be unique within a class.

### F.3.2 id\_unique\_in\_lane\_section

UID
:   asam.net:xodr:1.4.0:ids.id\_unique\_in\_lane\_section

Description
:   Lane IDs shall be unique within a lane section.

### F.3.3 only\_ref\_defined\_ids

UID
:   asam.net:xodr:1.4.0:ids.only\_ref\_defined\_ids

Description
:   Only defined IDs may be referenced.

## F.4 junctions

### F.4.1 no\_overlap

UID
:   asam.net:xodr:1.4.0:junctions.no\_overlap

Description
:   No junctions of any type shall overlap each other.

### F.4.2 type\_default\_no\_linked\_road

UID
:   asam.net:xodr:1.7.0:junctions.type\_default\_no\_linked\_road

Description
:   The `<connection>` element of a junction of @type="default" or @type="virtual" shall not have the @linkedRoad attribute.

### F.4.3 type\_direct\_no\_conn\_road

UID
:   asam.net:xodr:1.7.0:junctions.type\_direct\_no\_conn\_road

Description
:   The `<connection>` element of a junction of @type="direct" shall not have the @connectingRoad attribute.

### F.4.4 boundary

#### F.4.4.1 close\_gap\_with\_new\_roads

UID
:   asam.net:xodr:1.8.0:junctions.boundary.close\_gap\_with\_new\_roads

Description
:   If the existing roads are not sufficient to define a closed junction boundary, additional roads shall be defined for the missing segments.

#### F.4.4.2 only\_for\_common\_junctions

UID
:   asam.net:xodr:1.8.0:junctions.boundary.only\_for\_common\_junctions

Description
:   Junction boundaries are currently only valid for common junctions.

#### F.4.4.3 segments\_close\_boundry

UID
:   asam.net:xodr:1.8.0:junctions.boundary.segments\_close\_boundry

Description
:   Segments shall close the entire junction boundary.

#### F.4.4.4 segments\_counter\_clockwise\_order

UID
:   asam.net:xodr:1.8.0:junctions.boundary.segments\_counter\_clockwise\_order

Description
:   Segments shall be ordered counter clockwise.

#### F.4.4.5 segments\_for\_each\_conn\_road

UID
:   asam.net:xodr:1.8.0:junctions.boundary.segments\_for\_each\_conn\_road

Description
:   Segments shall be defined to reach the start or end of all roads connected to the junction.

### F.4.5 common

#### F.4.5.1 direct\_junction\_attributes

UID
:   asam.net:xodr:1.8.0:junctions.common.direct\_junction\_attributes

Description
:   The @overlapZone attribute shall only be specified for direct junctions.

#### F.4.5.2 junctions\_no\_pred\_succ

UID
:   asam.net:xodr:1.4.0:junctions.common.junctions\_no\_pred\_succ

Description
:   Unlike roads, junctions do not have a predecessor or successor.

#### F.4.5.3 not\_only\_two

UID
:   asam.net:xodr:1.9.0:junctions.common.not\_only\_two

Description
:   Junctions should not be used when only two roads meet.

#### F.4.5.4 virtual\_junction\_attributes

UID
:   asam.net:xodr:1.5.0:junctions.common.virtual\_junction\_attributes

Description
:   The @mainRoad, @orientation, @sStart and @sEnd attributes shall only be specified for virtual junctions.

#### F.4.5.5 when\_to\_use

UID
:   asam.net:xodr:1.4.0:junctions.common.when\_to\_use

Description
:   Junctions shall only be used when roads cannot be linked directly. They clarify ambiguities for the linking. Ambiguities are caused when a road has two or more possible predecessor or successor roads.

### F.4.6 connection

#### F.4.6.1 connect\_road\_no\_incoming\_road

UID
:   asam.net:xodr:1.4.0:junctions.connection.connect\_road\_no\_incoming\_road

Description
:   Connecting roads shall not be incoming roads.

#### F.4.6.2 end\_opposite\_linkage

UID
:   asam.net:xodr:1.7.0:junctions.connection.end\_opposite\_linkage

Description
:   The value `end` shall be used to indicate that the connecting road runs along the opposite direction of the linkage indicated in the `<laneLink>` element

#### F.4.6.3 lane\_change\_one\_con\_road

UID
:   asam.net:xodr:1.7.0:junctions.connection.lane\_change\_one\_con\_road

Description
:   By one connecting road with multiple `<laneLink>` elements for the connections between the lanes.

#### F.4.6.4 connect\_road\_no\_incoming\_road

UID
:   asam.net:xodr:1.9.0:junctions.connection.no\_connecting\_road\_direct

Description
:   The @connectingRoad attribute shall not be used for junctions with @type="direct".

#### F.4.6.5 no\_lane\_change\_for\_mult\_con\_roads

UID
:   asam.net:xodr:1.7.0:junctions.connection.no\_lane\_change\_for\_mult\_con\_roads

Description
:   By multiple connecting roads, each with one `<laneLink>` element for the connection between two specific lanes. Lane changes within this junction are not possible.

#### F.4.6.6 one\_link\_to\_incoming

UID
:   asam.net:xodr:1.8.0:junctions.connection.one\_link\_to\_incoming

Description
:   There shall only be one `<connection>` for a specific combination of @incomingRoad and @connectingRoad.
    For each `<connection>`, its `<laneLink>` elements shall only be specified for the lanes that lead into the junction.

#### F.4.6.7 connect\_road\_no\_incoming\_road

UID
:   asam.net:xodr:1.9.0:junctions.connection.smooth\_fit

Description
:   The linked lanes shall fit smoothly as described for roads (see  [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)).

#### F.4.6.8 start\_along\_linkage

UID
:   asam.net:xodr:1.7.0:junctions.connection.start\_along\_linkage

Description
:   The value `start` shall be used to indicate that the connecting road runs along the linkage indicated in the `<laneLink>` element.

### F.4.7 crossing

#### F.4.7.1 only\_one\_high\_prio

UID
:   asam.net:xodr:1.8.0:junctions.crossing.only\_one\_high\_prio

Description
:   Only one road defined by the @roadId attributes of the `<roadSection>` elements shall have `high` priority.

#### F.4.7.2 only\_road\_sections

UID
:   asam.net:xodr:1.8.0:junctions.crossing.only\_road\_sections

Description
:   Junctions with @type="crossing" shall only have `<roadSection>` elements.

#### F.4.7.3 s\_start\_end\_coverage

UID
:   asam.net:xodr:1.8.0:junctions.crossing.s\_start\_end\_coverage

Description
:   The values for the @sStart and @sEnd attributes of the `<roadSection>` elements shall at least cover the area where the roads overlap.

### F.4.8 cross\_path

#### F.4.8.1 correct\_junction\_id

UID
:   asam.net:xodr:1.8.0:junctions.cross\_path.correct\_junction\_id

Description
:   The @junction attribute shall contain the id of the junction to which a road belongs.

#### F.4.8.2 disregard\_cross\_road\_evelation

UID
:   asam.net:xodr:1.8.0:junctions.cross\_path.disregard\_cross\_road\_evelation

Description
:   The elevations of the crossing road defined by the @crossingRoad attribute of the `<crossPath>` element are disregarded.

#### F.4.8.3 lane\_linkage

UID
:   asam.net:xodr:1.8.0:junctions.cross\_path.lane\_linkage

Description
:   Start and end of the crossing road shall reach the linked lanes specified by the `<startLaneLink>` and `<endLaneLink>` elements.

#### F.4.8.4 only\_connect\_correct\_type

UID
:   asam.net:xodr:1.8.0:junctions.cross\_path.only\_connect\_correct\_type

Description
:   Cross paths shall only connect lanes with @type="walking" or @type="biking".

#### F.4.8.5 start\_end\_contained

UID
:   asam.net:xodr:1.8.0:junctions.cross\_path.start\_end\_contained

Description
:   The start and end points of the crossing road and its lanes shall be fully contained within the linked lanes specified by the `<startLaneLink>` and `<endLaneLink>` elements.

#### F.4.8.6 within\_junction\_area

UID
:   asam.net:xodr:1.8.0:junctions.cross\_path.within\_junction\_area

Description
:   Cross paths shall be within the area of a common junction or a virtual junction.

### F.4.9 direct

#### F.4.9.1 connecting\_road\_attribute\_usage

UID
:   asam.net:xodr:1.7.0:junctions.direct.connecting\_road\_attribute\_usage

Description
:   The @connectingRoad attribute shall not be used for junctions with @type="direct".

#### F.4.9.2 correct\_type\_linked\_road\_usage

UID
:   asam.net:xodr:1.7.0:junctions.direct.correct\_type\_linked\_road\_usage

Description
:   The @linkedRoad attribute shall only be used for junctions with @type="direct".

#### F.4.9.3 flat\_exits\_entries

UID
:   asam.net:xodr:1.8.0:junctions.direct.flat\_exits\_entries

Description
:   Currently only flat entries and exits can be modeled by overlapping direct junctions.

#### F.4.9.4 linked\_lane\_smoothness

UID
:   asam.net:xodr:1.7.0:junctions.direct.linked\_lane\_smoothness

Description
:   The linked lanes shall fit smoothly as described for roads (see  [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)).

#### F.4.9.5 overlap\_zone\_coverage

UID
:   asam.net:xodr:1.8.0:junctions.direct.overlap\_zone\_coverage

Description
:   The value of the @overlapZone attribute shall cover at least the overlapping area, but may be larger.

#### F.4.9.6 overlap\_zone\_exclusivity

UID
:   asam.net:xodr:1.8.0:junctions.direct.overlap\_zone\_exclusivity

Description
:   Only one pair of `<laneLink>` elements shall have @overlapZone attributes to define the overlapping lanes.

#### F.4.9.7 road\_connectivity

UID
:   asam.net:xodr:1.8.0:junctions.direct.road\_connectivity

Description
:   Direct junctions shall connect one road on one side with multiple roads on the other side.

#### F.4.9.8 road\_ramp\_heading

UID
:   asam.net:xodr:1.7.0:junctions.direct.road\_ramp\_heading

Description
:   The junction shall be placed where the headings of road, ramp, or slip lane are identical.

#### F.4.9.9 split\_or\_merge

UID
:   asam.net:xodr:1.8.0:junctions.direct.split\_or\_merge

Description
:   Direct junctions shall only be used for splitting or merging roads without crossing traffic.

### F.4.10 elevation\_grid

#### F.4.10.1 entry\_exit\_smoothness

UID
:   asam.net:xodr:1.8.0:junctions.elevation\_grid.entry\_exit\_smoothness

Description
:   For junction entries and exits, a smooth transition should be assured.

#### F.4.10.2 only\_one\_elev\_grid

UID
:   asam.net:xodr:1.8.0:junctions.elevation\_grid.only\_one\_elev\_grid

Description
:   A junction shall have only one elevation grid.

#### F.4.10.3 perpendicular\_vectors

UID
:   asam.net:xodr:1.8.0:junctions.elevation\_grid.perpendicular\_vectors

Description
:   The elevation grid shall be defined with vectors perpendicular to the junction reference line.

#### F.4.10.4 polynome\_coefficient\_values

UID
:   asam.net:xodr:1.8.0:junctions.elevation\_grid.polynome\_coefficient\_values

Description
:   The coefficients \(c\) and \(d\) of the polynoms shall be `0` if there are not enough support points in the elevation grid to calculate them.

#### F.4.10.5 valid\_for\_entire\_boundry

UID
:   asam.net:xodr:1.8.0:junctions.elevation\_grid.valid\_for\_entire\_boundry

Description
:   If a junction boundary is defined, the elevation grid shall be valid for the area enclosed by the junction boundary.

### F.4.11 geometry

#### F.4.11.1 correct\_junction\_boundry

UID
:   asam.net:xodr:1.8.0:junctions.geometry.correct\_junction\_boundry

Description
:   If a junction boundary is specified, a junction reference line shall cross the junction boundary or be at least tangent to the junction boundary at one point.

#### F.4.11.2 only\_one\_line\_element

UID
:   asam.net:xodr:1.8.0:junctions.geometry.only\_one\_line\_element

Description
:   Junction reference lines shall be defined by one `<geometry>` element. This `<geometry>` element shall have only one `<line>` element.

#### F.4.11.3 ref\_line\_definition

UID
:   asam.net:xodr:1.8.0:junctions.geometry.ref\_line\_definition

Description
:   The `<geometry>` element of a junction reference line shall be defined in a way that every point of the junction can be reached with a perpendicular straight line.

### F.4.12 priority

#### F.4.12.1 high\_and\_low\_attr

UID
:   asam.net:xodr:1.8.0:junctions.priority.high\_and\_low\_attr

Description
:   `<priority>` elements shall be defined with a pair of one @high and one @low attribute.

#### F.4.12.2 no\_signals

UID
:   asam.net:xodr:1.7.0:junctions.priority.no\_signals

Description
:   `<priority>` elements should only be used if there are no signals defined.

### F.4.13 virtual

#### F.4.13.1 connecting\_roads\_start\_end

UID
:   asam.net:xodr:1.9.0:junctions.virtual.connecting\_roads\_start\_end

Description
:   All connecting roads within the virtual junction shall either start or end at @sStart or at @sEnd.

#### F.4.13.2 heading\_equal\_mainroad

UID
:   asam.net:xodr:1.9.0:junctions.virtual.heading\_equal\_mainroad

Description
:   The heading of the connecting roads and the @mainRoad shall be equal at @sStart and at @sEnd.

#### F.4.13.3 linked\_lanes\_smooth\_fit

UID
:   asam.net:xodr:1.9.0:junctions.virtual.linked\_lanes\_smooth\_fit

Description
:   The linked lanes shall fit smoothly (see  [Section 10.3, "Road linkage"](../10_roads/10_03_road_linkage.html#top-86fc414c-6211-4777-b40e-466d4551d23e)).

#### F.4.13.4 main\_road\_only

UID
:   asam.net:xodr:1.9.0:junctions.virtual.main\_road\_only

Description
:   Virtual junctions shall be used for branches off the main road only. The main road has priority if not specified otherwise.

#### F.4.13.5 no\_controllers

UID
:   asam.net:xodr:1.9.0:junctions.virtual.no\_controllers

Description
:   Virtual junctions shall not have controllers and therefore no traffic lights.

#### F.4.13.6 only\_one\_start\_end

UID
:   asam.net:xodr:1.9.0:junctions.virtual.only\_one\_start\_end

Description
:   There shall only be one @sStart and one @sEnd attribute for the virtual junction.

#### F.4.13.7 connections

##### only\_virtual\_junctions

UID
:   asam.net:xodr:1.9.0:junctions.virtual.connections.only\_virtual\_junctions

Description
:   Virtual connections shall only be defined in virtual junctions.

#### F.4.13.8 crossPath

##### cross\_road\_check\_s\_t

UID
:   asam.net:xodr:1.8.0:junctions.virtual.crossPath.cross\_road\_check\_s\_t

Description
:   The crossing road shall not exceed the values for s and t of the main road defined by the @roadAtStart and @roadAtEnd attributes.

## F.5 performance

### F.5.1 avoid\_redundant\_info

UID
:   asam.net:xodr:1.8.1:performance.avoid\_redundant\_info

Description
:   Redundant elements should be avoided, such as elevation or laneSection nodes for consecutive s-coordinates with identical attributes, or multiple geometry nodes for straight lines.

## F.6 road

### F.6.1 length\_sum\_geometries

UID
:   asam.net:xodr:1.9.0:road.length\_sum\_geometries

Description
:   The road length should be the sum of the lengths of all `<geometry>` elements

### F.6.2 no\_overlap\_outside\_junction

UID
:   asam.net:xodr:1.4.0:road.no\_overlap\_outside\_junction

Description
:   Roads outside a junction shall not overlap.

### F.6.3 no\_overlap\_self

UID
:   asam.net:xodr:1.4.0:road.no\_overlap\_self

Description
:   A road shall not overlap with itself.

### F.6.4 overlap\_inside\_junction

UID
:   asam.net:xodr:1.4.0:road.overlap\_inside\_junction

Description
:   Only roads with the same junction id may overlap on the same level. This does not include roads on different driving levels, for example, bridges.

### F.6.5 corner\_local

#### F.6.5.1 element\_min\_amount

UID
:   asam.net:xodr:1.7.0:road.corner\_local.element\_min\_amount

Description
:   There shall be at least two `<cornerLocal>` elements inside an `<outline>` element.

#### F.6.5.2 first\_id\_zero

UID
:   asam.net:xodr:1.9.0:road.corner\_local.first\_id\_zero

Description
:   The @id attribute of the first `<cornerLocal>` element of an object should be 0.

#### F.6.5.3 mandatory\_id\_with\_markings

UID
:   asam.net:xodr:1.9.0:road.corner\_local.mandatory\_id\_with\_markings

Description
:   The @id attribute of a `<cornerLocal>` element shall be mandatory when the parent also has a `<markings>` element.

#### F.6.5.4 no\_mixing\_road\_local

UID
:   asam.net:xodr:1.x.0:road.corner\_local.no\_mixing\_road\_local

Description
:   "There shall be no mixture of `<cornerRoad>` and `<cornerLocal>` elements inside the same `<outline>` element."

#### F.6.5.5 sequential\_id\_values

UID
:   asam.net:xodr:1.9.0:road.corner\_local.sequential\_id\_values

Description
:   The @id attribute should increase by 1 for each `<cornerLocal>` element in the order they are listed from top to bottom.

### F.6.6 corner\_road

#### F.6.6.1 corner\_road\_local\_exclusivity

UID
:   asam.net:xodr:1.9.0:road.corner\_road.corner\_road\_local\_exclusivity

Description
:   There shall be no mixture of `<cornerRoad>`, `<cornerLocal>`, and `<curveLocal>` elements inside the same `<outline>` element.

#### F.6.6.2 element\_min\_amount

UID
:   asam.net:xodr:1.7.0:road.corner\_road.element\_min\_amount

Description
:   There shall be at least two `<cornerRoad>` elements inside an `<outline>` element.

#### F.6.6.3 first\_id\_zero

UID
:   asam.net:xodr:1.9.0:road.corner\_road.first\_id\_zero

Description
:   The @id attribute of the first `<cornerRoad>` element of an object should be 0.

#### F.6.6.4 mandatory\_id\_with\_markings

UID
:   asam.net:xodr:1.9.0:road.corner\_road.mandatory\_id\_with\_markings

Description
:   The @id attribute of a `<cornerRoad>` element shall be mandatory when the parent also has a `<markings>` element.

#### F.6.6.5 sequential\_id\_values

UID
:   asam.net:xodr:1.9.0:road.corner\_road.sequential\_id\_values

Description
:   The @id attribute should increase by 1 for each `<cornerRoad>` element in the order they are listed from top to bottom.

### F.6.7 crg

#### F.6.7.1 attach\_vs\_friction

UID
:   asam.net:xodr:1.7.0:road.crg.attach\_vs\_friction

Description
:   `@mode=attached` shall not be used together with `@purpose=friction`.

#### F.6.7.2 friction\_no\_z\_offset\_scale

UID
:   asam.net:xodr:1.7.0:road.crg.friction\_no\_z\_offset\_scale

Description
:   `@zOffset` and `@zScale` shall not be set for friction values.

#### F.6.7.3 h\_offset\_only\_genuine

UID
:   asam.net:xodr:1.9.0:road.crg.h\_offset\_only\_genuine\_global

Description
:   @hOffset shall not be used for modes other than @mode=genuine and @mode=global.

#### F.6.7.4 junction

UID
:   asam.net:xodr:1.7.0:road.crg.junction

Description
:   If a `<junction>` element contains a `<CRG>` element, none of the connecting roads that belong to this junction shall have a `<CRG>` element.

#### F.6.7.5 no\_opposite

UID
:   asam.net:xodr:1.7.0:road.crg.no\_opposite

Description
:   @orientation=opposite shall not be used for modes other than @mode=attached and @mode=attached0.

#### F.6.7.6 only\_on\_per\_s

UID
:   asam.net:xodr:1.7.0:road.crg.only\_on\_per\_s

Description
:   In the future, multiple CRG files at one position may be combined. For compatibility with future versions, each road or junction should only contain one CRG file per `s`-position and @purpose.

#### F.6.7.7 s\_t\_offset\_no\_global

UID
:   asam.net:xodr:1.7.0:road.crg.s\_t\_offset\_no\_global

Description
:   @sOffset and @tOffset shall not be used with @mode=global.

#### F.6.7.8 use\_last\_entry

UID
:   asam.net:xodr:1.7.0:road.crg.use\_last\_entry

Description
:   If more than one CRG entry is given for the same physical property (attribute purpose) at a given location, then the last entry in the sequence of occurrence in the ASAM OpenDRIVE file shall be the relevant one. All others are ignored (but see the [note](../10_roads/10_06_road_surface.html#Note_CRG)).

### F.6.8 cross\_section\_surface

#### F.6.8.1 height

UID
:   asam.net:xodr:1.8.0:road.cross\_section\_surface.height

Description
:   The value of @height at `<lane>` elements is added to the cross section surface in z-direction.

#### F.6.8.2 lane\_def\_valid

UID
:   asam.net:xodr:1.8.0:road.cross\_section\_surface.lane\_def\_valid

Description
:   A cross section surface is only valid within the lane definition of the road.

#### F.6.8.3 no\_shape\_superelevation

UID
:   asam.net:xodr:1.8.0:road.cross\_section\_surface.no\_shape\_superelevation

Description
:   A cross section surface shall not be used in combination with road shape or superelevation.

#### F.6.8.4 start\_end\_match\_with\_refline

UID
:   asam.net:xodr:1.8.0:road.cross\_section\_surface.start\_end\_match\_with\_refline

Description
:   A cross section surface shall start and end at the start and end of the road reference line.

#### F.6.8.5 use\_strip

UID
:   asam.net:xodr:1.8.0:road.cross\_section\_surface.use\_strip

Description
:   If on a side only one strip is used, it is defined in a `<strip>` element with @id="1" or @id="-1" and a width shall not be specified.

#### F.6.8.6 use\_width

UID
:   asam.net:xodr:1.8.0:road.cross\_section\_surface.use\_width

Description
:   If on a side two strips are specified, a width for the inner strip shall be specified.

### F.6.9 curve\_local

#### F.6.9.1 continuous\_curve\_local

UID
:   asam.net:xodr:1.9.0:road.curve\_local.continuous\_curve\_local

Description
:   Outlines defined by `<curveLocal>` elements shall be continuous.

#### F.6.9.2 element\_min\_amount

UID
:   asam.net:xodr:1.9.0:road.curve\_local.element\_min\_amount

Description
:   There shall be at least one `<curveLocal>` element inside an `<outline>` element.

#### F.6.9.3 length\_match

UID
:   asam.net:xodr:1.9.0:road.curve\_local.length\_match

Description
:   The actual curve length, as determined by numerical integration over the parameter range, should match @length.

#### F.6.9.4 paramPoly3

##### arcLength\_range

UID
:   asam.net:xodr:1.9.0:road.curve\_local.paramPoly3.arcLength\_range

Description
:   For `<paramPoly3>` elements with @pRange="arcLength", p shall be chosen in [0, @length from `<curveLocal>`].

##### normalized\_range

UID
:   asam.net:xodr:1.9.0:road.curve\_local.paramPoly3.normalized\_range

Description
:   For `<paramPoly3>` elements with @pRange="normalized", p shall be chosen in [0, 1].

### F.6.10 elevation

#### F.6.10.1 elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.elevation.elem\_asc\_order

Description
:   `<elevation>` elements shall be defined in ascending order according to the s-coordinate.

#### F.6.10.2 elev\_along\_ref\_line

UID
:   asam.net:xodr:1.4.0:road.elevation.elev\_along\_ref\_line

Description
:   Roads shall be elevated along their road reference line.

### F.6.11 geometry

#### F.6.11.1 contact\_point

UID
:   asam.net:xodr:1.7.0:road.geometry.contact\_point

Description
:   If two roads are connected without a junction, the road reference line of a new road shall always begin at the `<contactPoint>` element of its successor or predecessor road. The road reference lines may be directed in opposite directions.

#### F.6.11.2 elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.geometry.elem\_asc\_order

Description
:   `<geometry>` elements shall be defined in ascending order along the road reference line according to the s-coordinate.

#### F.6.11.3 one\_geom\_elem\_per\_spec

UID
:   asam.net:xodr:1.4.0:road.geometry.one\_geom\_elem\_per\_spec

Description
:   One `<geometry>` element shall contain only one element that further specifies the geometry of the road.

#### F.6.11.4 only\_one\_refline

UID
:   asam.net:xodr:1.4.0:road.geometry.only\_one\_refline

Description
:   There shall be only one road reference line per road.

#### F.6.11.5 refline\_exists

UID
:   asam.net:xodr:1.4.0:road.geometry.refline\_exists

Description
:   Each road shall have a road reference line.

#### F.6.11.6 refline\_no\_gaps

UID
:   asam.net:xodr:1.4.0:road.geometry.refline\_no\_gaps

Description
:   A road reference line shall have no gaps.

#### F.6.11.7 refline\_no\_kinks

UID
:   asam.net:xodr:1.4.0:road.geometry.refline\_no\_kinks

Description
:   A road reference line should have no kinks.

#### F.6.11.8 s-value\_sum

UID
:   asam.net:xodr:1.9.0:road.geometry.s-value\_sum

Description
:   The s-value of each `<geometry>` shall be the sum of all `<geometry>` lengths prior

#### F.6.11.9 arc

##### no\_zero\_curvature

UID
:   asam.net:xodr:1.9.0:road.geometry.arc.no\_zero\_curvature

Description
:   @curvature should not be zero.

#### F.6.11.10 paramPoly3

##### arcLength\_range

UID
:   asam.net:xodr:1.7.0:road.geometry.paramPoly3.arcLength\_range

Description
:   If @pRange="arcLength", p shall be chosen in [0, @length from `<geometry>`].

##### length\_match

UID
:   asam.net:xodr:1.7.0:road.geometry.paramPoly3.length\_match

Description
:   The actual curve length, as determined by numerical integration over the parameter range, should match @length.

##### normalized\_range

UID
:   asam.net:xodr:1.7.0:road.geometry.paramPoly3.normalized\_range

Description
:   If @pRange="normalized", p shall be chosen in [0, 1].

##### valid\_parameters

UID
:   asam.net:xodr:1.7.0:road.geometry.paramPoly3.valid\_parameters

Description
:   The local u/v coordinate system should be aligned with the s/t coordinate system of the start point (meaning that the curve starts in the direction given by @hdg, and at the position given by @x and @y). To achieve this, the polynomial parameter coefficients have to be @aU=@aV=@bV=0, @bU>0.

#### F.6.11.11 spiral

##### curvature\_change

UID
:   asam.net:xodr:1.9.0:road.geometry.spiral.curvature\_change

Description
:   @curvStart and @curvEnd should not be the same.

### F.6.12 lane

#### F.6.12.1 center\_elem\_definition

UID
:   asam.net:xodr:1.4.0:road.lane.center\_elem\_definition

Description
:   One `<center>` element shall be defined for each s-coordinate.

#### F.6.12.2 center\_lane

UID
:   asam.net:xodr:1.9.0:road.lane.center\_lane

Description
:   Each road shall have at least one lane layer with a center lane.

#### F.6.12.3 center\_lane\_id

UID
:   asam.net:xodr:1.4.0:road.lane.center\_lane\_id

Description
:   The center lane shall have the lane id 0.

#### F.6.12.4 center\_lane\_no\_width

UID
:   asam.net:xodr:1.4.0:road.lane.center\_lane\_no\_width

Description
:   The center lane shall have no width, meaning that the `<width>` element shall not be used for the center lane.

#### F.6.12.5 center\_lane

UID
:   asam.net:xodr:1.9.0:road.lane.center\_lane\_singular

Description
:   There shall always be exactly one center lane at each s-position.

#### F.6.12.6 lanes\_numbered\_correctly

UID
:   asam.net:xodr:1.4.0:road.lane.lanes\_numbered\_correctly

Description
:   Lanes with positive ID run on the left side of the center lane, while lanes with negative ID run on the right side of the center lane.

#### F.6.12.7 lane\_id\_unique

UID
:   asam.net:xodr:1.9.0:road.lane.lane\_id\_unique

Description
:   Lane numbering shall be unique per lane section and layer.

#### F.6.12.8 lane\_listing

UID
:   asam.net:xodr:1.4.0:road.lane.lane\_listing

Description
:   For better orientation, lanes should be listed from left to right, that is with descending ID.

#### F.6.12.9 lane\_order

UID
:   asam.net:xodr:1.4.0:road.lane.lane\_order

Description
:   Lane numbering shall start with 1 next to the center lane in positive t-direction in ascending order and -1 next to the center lane in negative t-direction in descending order.

#### F.6.12.10 lane\_order\_no\_gaps

UID
:   asam.net:xodr:1.4.0:road.lane.lane\_order\_no\_gaps

Description
:   Lane numbering shall be consecutive without any gaps.

#### F.6.12.11 lane\_listing

UID
:   asam.net:xodr:1.4.0:road.lane.lane\_reverse\_left\_right

Description
:   @direction="reverse" shall not be used to change from right-hand traffic to left-hand traffic and vice versa.

#### F.6.12.12 lane\_listing

UID
:   asam.net:xodr:1.9.0:road.lane.lane\_section\_drivable

Description
:   In order to be drivable, each lane section should contain at least one `<right>` or `<left>` element that is valid for the whole length of that section.

#### F.6.12.13 lane\_sect\_min\_amount

UID
:   asam.net:xodr:1.9.0:road.lane.lane\_sect\_first

Description
:   The first lane section shall be defined with a value of 0.0 for the @s attribute.

#### F.6.12.14 lane\_sect\_min\_amount

UID
:   asam.net:xodr:1.4.0:road.lane.lane\_sect\_min\_amount

Description
:   Each `<lanes>` element shall contain at least one `<laneSection>` element.

#### F.6.12.15 level\_true\_one\_side

UID
:   asam.net:xodr:1.7.0:road.lane.level\_true\_one\_side

Description
:   If a lane has @level="true", then all further outward lanes shall be lanes with @level="true" until the edge of the road is reached.

#### F.6.12.16 s\_attr\_value

UID
:   asam.net:xodr:1.4.0:road.lane.s\_attr\_value

Description
:   All `<laneSection>` elements shall contain the @s attribute.

#### F.6.12.17 access

##### center\_lane\_no\_acc\_rule

UID
:   asam.net:xodr:1.4.0:road.lane.access.center\_lane\_no\_acc\_rule

Description
:   The center lane shall have no access rules.

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.access.elem\_asc\_order

Description
:   `<access>` elements shall be defined in ascending order according to the s-coordinate.

##### no\_mix\_of\_deny\_or\_allow

UID
:   asam.net:xodr:1.7.0:road.lane.access.no\_mix\_of\_deny\_or\_allow

Description
:   At a given s-position, either only deny or only allow values shall be given.

#### F.6.12.18 border

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.border.elem\_asc\_order

Description
:   `<border>` elements shall be defined in ascending order according to the s-coordinate.

##### exclusive\_offset\_border

UID
:   asam.net:xodr:1.4.0:road.lane.border.exclusive\_offset\_border

Description
:   `<border>` elements shall not be used together with `<laneOffset>`.

##### exclusive\_width\_border

UID
:   asam.net:xodr:1.4.0:road.lane.border.exclusive\_width\_border

Description
:   `<border>` elements shall not be used together with `<width>` elements in the same lane group.

##### overlap\_with\_inner\_lanes

UID
:   asam.net:xodr:1.4.0:road.lane.border.overlap\_with\_inner\_lanes

Description
:   Lane borders shall not intersect inner lanes.

#### F.6.12.19 height

##### center\_lane\_no\_height

UID
:   asam.net:xodr:1.4.0:road.lane.height.center\_lane\_no\_height

Description
:   The center lane shall not be elevated by lane height.

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.height.elem\_asc\_order

Description
:   `<height>` elements shall be defined in ascending order according to the s-coordinate.

#### F.6.12.20 lane\_properties

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.lane\_properties.elem\_asc\_order

Description
:   Lane geometries of identical types shall be defined in ascending order.

#### F.6.12.21 layer

##### center\_lane\_permanent

UID
:   asam.net:xodr:1.9.0:road.lane.layer.center\_lane\_permanent

Description
:   Each lane section in the permanent layer shall have a center lane.

##### lane\_group\_width\_temporary

UID
:   asam.net:xodr:1.9.0:road.lane.layer.lane\_group\_width\_temporary

Description
:   For each lane group, the sum of all lane widths and lane offsets on the temporary lane layer shall not be greater than the sum of lane widths and lane offsets on the permanent lane layer.

##### lane\_phys\_attr\_temporary

UID
:   asam.net:xodr:1.9.0:road.lane.layer.lane\_phys\_attr\_temporary

Description
:   Lanes in the "temporary" layer shall not contain `<height>` or `<material>` elements.
    The height and material is instead determined by the permanent layer.

##### layer\_limits

UID
:   asam.net:xodr:1.9.0:road.lane.layer.layer\_limits

Description
:   Each road shall have exactly one "permanent" and up to one "temporary" lane layer.

##### layer\_mandatory\_permanent

UID
:   asam.net:xodr:1.9.0:road.lane.layer.layer\_mandatory\_permanent

Description
:   There shall be at least one lane in the "permanent" layer at each s-coordinate of the road.

##### length\_only\_temporary

UID
:   asam.net:xodr:1.9.0:road.lane.layer.length\_only\_temporary

Description
:   Lanes in the permanent lane layer shall not use the attribute @length.

#### F.6.12.22 link

##### lanes\_across\_laneSections

UID
:   asam.net:xodr:1.4.0:road.lane.link.lanes\_across\_laneSections

Description
:   Lane that continues across the lane sections shall be connected in both directions.

##### multiple\_connections

UID
:   asam.net:xodr:1.4.0:road.lane.link.multiple\_connections

Description
:   Multiple predecessors and successors shall be used if a lane is split abruptly or several lanes are merged abruptly. All lanes that are connected shall have a non-zero width at the connection point.

##### new\_lane\_appear

UID
:   asam.net:xodr:1.4.0:road.lane.link.new\_lane\_appear

Description
:   If a new lane appears besides, only the continuing lane shall be connected to the original lane, not the appearing lane.

##### no\_link

UID
:   asam.net:xodr:1.4.0:road.lane.link.no\_link

Description
:   The `<link>` element shall be omitted if the lane starts or ends in a junction or has no link.

##### temporary\_layer\_section\_link\_permanent

UID
:   asam.net:xodr:1.9.0:road.lane.link.temporary\_layer\_section\_link\_permanent

Description
:   At the start and at the end of a temporary lane layer section, all drivable lanes with non-zero width on the temporary lane layer shall be linked to lanes on the permanent lane layer.

##### use\_junctions

UID
:   asam.net:xodr:1.4.0:road.lane.link.use\_junctions

Description
:   Two lanes shall only be linked if their linkage is clear. If the relationship to a predecessor or successor is ambiguous, junctions shall be used.

##### zero\_width\_at\_end

UID
:   asam.net:xodr:1.7.0:road.lane.link.zero\_width\_at\_end

Description
:   Lanes that have a width of zero at the end of the lane section shall have no `<successor>` element.

##### zero\_width\_at\_start

UID
:   asam.net:xodr:1.7.0:road.lane.link.zero\_width\_at\_start

Description
:   Lanes that have a width of zero at the beginning of the lane section shall have no `<predecessor>` element.

#### F.6.12.23 material

##### center\_lane\_no\_material

UID
:   asam.net:xodr:1.4.0:road.lane.material.center\_lane\_no\_material

Description
:   The center lane shall have no material elements.

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.material.elem\_asc\_order

Description
:   `<material>` elements shall be defined in ascending order according to the s-coordinate

#### F.6.12.24 road\_mark

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.road\_mark.elem\_asc\_order

Description
:   `<roadMark>` elements shall be defined in ascending order according to the s-coordinate.

##### only\_outer

UID
:   asam.net:xodr:1.9.0:road.lane.road\_mark.only\_outer

Description
:   `<roadMark>` elements shall only be used to describe the outer lane marking.

##### position\_outer\_half

UID
:   asam.net:xodr:1.9.0:road.lane.road\_mark.position\_outer\_half

Description
:   The center line of the lane marking shall be positioned on the lane’s outer border line in such a way that the outer half of the lane marking is physically placed on the next lane.

#### F.6.12.25 rule

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.rule.elem\_asc\_order

Description
:   `<rule>` elements shall be defined in ascending order according to the s-coordinate.

#### F.6.12.26 speed

##### center\_lane\_no\_spd\_lmt

UID
:   asam.net:xodr:1.4.0:road.lane.speed.center\_lane\_no\_spd\_lmt

Description
:   The center lane shall have no speed limit.

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.speed.elem\_asc\_order

Description
:   `<speed>` elements shall be defined in ascending order according to the s-coordinate.

#### F.6.12.27 width

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane.width.elem\_asc\_order

Description
:   `<width>` elements shall be defined in ascending order according to the s-coordinate.

##### lane\_width\_validity

UID
:   asam.net:xodr:1.4.0:road.lane.width.lane\_width\_validity

Description
:   Width (ds) shall be greater than or equal to zero.

##### no\_width\_with\_border

UID
:   asam.net:xodr:1.9.0:road.lane.width.no\_width\_with\_border

Description
:   `<width>` elements shall not be used together with `<border>` elements in the same lane group.

##### width\_defined\_whole\_section

UID
:   asam.net:xodr:1.7.0:road.lane.width.width\_defined\_whole\_section

Description
:   The width of the lane shall be defined for the full length of the lane section. This means that there must be a `<width>` element for @s="0".

### F.6.13 lanes

#### F.6.13.1 lane\_offset

##### elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lanes.lane\_offset.elem\_asc\_order

Description
:   `<laneOffset>` elements shall be defined in ascending order according to the s-coordinate.

##### no\_offset\_if\_border\_defined

UID
:   asam.net:xodr:1.4.0:road.lanes.lane\_offset.no\_offset\_if\_border\_defined

Description
:   There shall be no `<laneOffset>` if border definitions are present.

### F.6.14 lane\_section

#### F.6.14.1 elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.lane\_section.elem\_asc\_order

Description
:   `<laneSection>` elements shall be defined in ascending order according to the s-coordinate.

#### F.6.14.2 lanesec\_length\_limit\_road

UID
:   asam.net:xodr:1.9.0:road.lane\_section.lanesec\_length\_limit\_road

Description
:   A lane section with @length shall not extend beyond the end of the road.

#### F.6.14.3 lanesec\_usage\_lane\_num

UID
:   asam.net:xodr:1.4.0:road.lane\_section.lanesec\_usage\_lane\_num

Description
:   A new lane section shall be defined each time the number of lanes change.

#### F.6.14.4 lane\_sect\_req

UID
:   asam.net:xodr:1.9.0:road.lane\_section.lane\_long\_zero\_width

Description
:   Using lanes with a width of 0 for long distances should be avoided.

#### F.6.14.5 lane\_sect\_req

UID
:   asam.net:xodr:1.4.0:road.lane\_section.lane\_sect\_req

Description
:   Each road shall have at least one lane section.

#### F.6.14.6 new\_lanesec\_link\_temp\_to\_perm

UID
:   asam.net:xodr:1.9.0:road.lane\_section.new\_lanesec\_link\_temp\_to\_perm

Description
:   A new lane section on the permanent lane layer shall be defined each time lanes on the permanent layer are linked to lanes on the temporary layer.

#### F.6.14.7 valid\_length

UID
:   asam.net:xodr:1.4.0:road.lane\_section.valid\_length

Description
:   The length of lane sections shall be greater than zero.

### F.6.15 linkage

#### F.6.15.1 both\_sides\_consistency

UID
:   asam.net:xodr:1.9.0:road.linkage.both\_sides\_consistency

Description
:   `<predecessor>` and/or `<successor>` shall be defined at both sides of the road linkage and shall be consistent.

#### F.6.15.2 is\_junction\_needed

UID
:   asam.net:xodr:1.4.0:road.linkage.is\_junction\_needed

Description
:   Two roads shall only be linked directly if the linkage is clear. If the relationship to successor or predecessor is ambiguous, junctions shall be used.

#### F.6.15.3 junc\_link\_attribute\_usage

UID
:   asam.net:xodr:1.7.0:road.linkage.junc\_link\_attribute\_usage

Description
:   For a common junction and a direct junction as successor or predecessor the @elementType and @elementId attributes shall be used.

#### F.6.15.4 road\_link\_attribute\_usage

UID
:   asam.net:xodr:1.4.0:road.linkage.road\_link\_attribute\_usage

Description
:   For a road as successor or predecessor the @elementType, @elementId and @contactPoint attributes shall be used.

#### F.6.15.5 virtjunc\_link\_attribute\_usage

UID
:   asam.net:xodr:1.7.0:road.linkage.virtjunc\_link\_attribute\_usage

Description
:   For a virtual junction as successor or predecessor the @elementType, @elementId, @elementS and @elementDir attributes shall be used.

### F.6.16 object

#### F.6.16.1 circular\_vs\_angular

UID
:   asam.net:xodr:1.7.0:road.object.circular\_vs\_angular

Description
:   Objects may be of circular or angular shape. The possibilities are mutually exclusive. The shape is defined by the used attributes.

#### F.6.16.2 orientation

UID
:   asam.net:xodr:1.7.0:road.object.orientation

Description
:   The direction for which objects are valid shall be specified.

#### F.6.16.3 s\_t\_coords

UID
:   asam.net:xodr:1.7.0:road.object.s\_t\_coords

Description
:   The origin position of the object shall be described with s- and t-coordinates along the road surface.

#### F.6.16.4 type\_attr

UID
:   asam.net:xodr:1.7.0:road.object.type\_attr

Description
:   The type of an object shall be given by the @type attribute.

#### F.6.16.5 borders

##### different\_outlineids

UID
:   asam.net:xodr:1.9.0:road.object.borders.different\_outlineids

Description
:   All `<outline>` elements of an `<outlines>` element shall have different @outlineId values.

##### useCompleteOutline\_true

UID
:   asam.net:xodr:1.7.0:road.object.borders.useCompleteOutline\_true

Description
:   If @useCompleteOutline is true, the `<cornerReference>` element shall not be defined.

#### F.6.16.6 bridges

##### define\_type

UID
:   asam.net:xodr:1.7.0:road.object.bridges.define\_type

Description
:   Bridges may be restricted to certain lanes, using the `<laneValidity>` element.

##### from\_lower\_equal\_to

UID
:   asam.net:xodr:1.7.0:road.object.bridges.from\_lower\_equal\_to

Description
:   The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

##### type\_definition

UID
:   asam.net:xodr:1.7.0:road.object.bridges.type\_definition

Description
:   The @type of the bridges shall be specified.

#### F.6.16.7 marking

##### colour

UID
:   asam.net:xodr:1.7.0:road.object.marking.colour

Description
:   The color of the marking shall be defined.

##### complete\_or\_partial\_on\_outline

UID
:   asam.net:xodr:1.9.0:road.object.marking.complete\_or\_partial\_on\_outline

Description
:   The marking of an object with an `<outlines>` element shall either completely or partially be defined on one of its outlines.

##### markings\_with\_outline

UID
:   asam.net:xodr:1.9.0:road.object.marking.markings\_with\_outline

Description
:   If an outline is used, any `<markings>` element shall be inside an `<outline>` element.

##### markings\_without\_outline

UID
:   asam.net:xodr:1.9.0:road.object.marking.markings\_without\_outline

Description
:   If no outline is used, the `<markings>` element shall be inside the `<object>` element.

##### no\_cornerreference\_if\_no\_outline

UID
:   asam.net:xodr:1.7.0:road.object.marking.no\_cornerreference\_if\_no\_outline

Description
:   If no outline is used, the `<cornerReference>` element cannot be used.

##### no\_outline\_side\_attr

UID
:   asam.net:xodr:1.7.0:road.object.marking.no\_outline\_side\_attr

Description
:   If no outline is used, the @side attribute is mandatory.

##### outline\_corner\_reference\_count

UID
:   asam.net:xodr:1.7.0:road.object.marking.outline\_corner\_reference\_count

Description
:   If an outline is used, at least two `<cornerReference>` elements are mandatory.

#### F.6.16.8 material

##### materials\_may\_differ

UID
:   asam.net:xodr:1.7.0:road.object.material.materials\_may\_differ

Description
:   The material of objects may differ from the surrounding road.

#### F.6.16.9 object\_marking

##### colour

UID
:   asam.net:xodr:1.8.2:road.object.object\_marking.colour

Description
:   The color of the marking shall be defined.

##### enclosed\_outline\_marking

UID
:   asam.net:xodr:1.8.2:road.object.object\_marking.enclosed\_outline\_marking

Description
:   To specify a marking that fully encloses an object on a closed outline, the `<marking>` shall have two `<cornerReference>` elements with the same @id.

##### include\_points\_between\_cornerReferences

UID
:   asam.net:xodr:1.8.2:road.object.object\_marking.include\_points\_between\_cornerReferences

Description
:   For `<marking>` elements with `<cornerReference>` elements that are not directly subsequent on the outline, all points in between shall be included as well.

##### keep\_id\_ordered

UID
:   asam.net:xodr:1.8.2:road.object.object\_marking.keep\_id\_ordered

Description
:   `<cornerReference>` elements shall use the same order of @id attributes as the points of the outline they belong to.

##### outline\_corner\_reference\_count

UID
:   asam.net:xodr:1.8.2:road.object.object\_marking.outline\_corner\_reference\_count

Description
:   At least two `<cornerReference>` elements are mandatory.

#### F.6.16.10 outline

##### exactly\_one\_outer

UID
:   asam.net:xodr:1.9.0:road.object.outline.exactly\_one\_outer

Description
:   `<outlines>` elements shall have exactly one `<outline>` element with @outer=true.

##### inner\_outline\_touches\_outer

UID
:   asam.net:xodr:1.9.0:road.object.outline.inner\_outline\_touches\_outer

Description
:   If an inner outline touches the outer outline, the reference point shall be identical in both outlines.

##### outline\_followed\_by\_corner

UID
:   asam.net:xodr:1.7.0:road.object.outline.outline\_followed\_by\_corner

Description
:   An `<outline>` element shall be followed by two or more `<cornerRoad>` elements, by two or more `<cornerLocal>` elements, or by one or more `<cornerLocalParamPoly3>` elements.

##### points\_inside\_box

UID
:   asam.net:xodr:1.7.0:road.object.outline.points\_inside\_box

Description
:   All points of the `<outline>` element must be located inside the bounding volume.

#### F.6.16.11 reference

##### from\_lower\_equal\_to

UID
:   asam.net:xodr:1.7.0:road.object.reference.from\_lower\_equal\_to

Description
:   The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

#### F.6.16.12 repeating

##### attributes\_with\_outline\_skeleton

UID
:   asam.net:xodr:1.9.0:road.object.repeating.attributes\_with\_outline\_skeleton

Description
:   @lengthStart, @lengthEnd, @widthStart, @widthEnd, @heightStart, and @heightEnd shall not be applicable for objects with an `<outlines>`, an `<outline>`, or a `<skeleton>` element.

##### no\_widthstart\_end\_with\_radius

UID
:   asam.net:xodr:1.9.0:road.object.repeating.no\_widthstart\_end\_with\_radius

Description
:   @widthStart and @widthEnd shall not be applicable for objects where @radius is set.

##### outline\_use\_cornerlocal

UID
:   asam.net:xodr:1.9.0:road.object.repeating.outline\_use\_cornerlocal

Description
:   Repeated objects with an outline shall use `<cornerLocal>`

##### valid\_s\_length

UID
:   asam.net:xodr:1.9.0:road.object.repeating.valid\_s\_length

Description
:   Repeated objects shall have valid s-coordinates and lengths.

#### F.6.16.13 skeleton

##### points\_boundary\_inside\_box

UID
:   asam.net:xodr:1.9.0:road.object.skeleton.points\_boundary\_inside\_box

Description
:   The boundary, defined by either width and height or radius, of each point of an object’s skeleton shall at least partially be located inside the bounding volume.

##### points\_inside\_box

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.points\_inside\_box

Description
:   All points of the `<polyline>` element must be located inside the bounding volume.

##### points\_requirements

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.points\_requirements

Description
:   All points of the `<polyline>` element are connected with a straight line between the `<vertexRoad>` or `<vertexLocal>` elements and the specified @radius or @width and @height attributes of each point are perpendicular to this line.

##### polyline\_followed\_by\_vertex

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.polyline\_followed\_by\_vertex

Description
:   A `<polyline>` element shall be followed by either two or more `<vertexRoad>` elements or by two or more `<vertexLocal>` elements.

##### use\_radius\_or\_width\_length

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.use\_radius\_or\_width\_length

Description
:   Each `<polyline>` element shall either use @radius or @width and @length attributes for all of its vertex elements.

##### vertex\_local

###### element\_min\_amount

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.vertex\_local.element\_min\_amount

Description
:   There shall be at least two `<vertexLocal>` elements inside an `<polyline>` element.

###### linear\_interpolation

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.vertex\_local.linear\_interpolation

Description
:   Values of @radius or @width and @length attributes will be interpolated linearly between two `<vertexLocal>` points.

###### no\_mixing\_road\_local

UID
:   asam.net:xodr:1.9.0:road.object.skeleton.vertex\_local.no\_mixing\_road\_local

Description
:   There shall be no `<vertexRoad>` element next to a `<vertexLocal>` element inside the same `<polyline>` element.

###### vertex\_local\_elements

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.vertex\_local.vertex\_local\_elements

Description
:   `<vertexLocal>` elements shall not use @radius together with @width and @length attributes in one `<polyline>` element.

##### vertex\_road

###### element\_min\_amount

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.vertex\_road.element\_min\_amount

Description
:   There shall be at least two `<vertexRoad>` elements inside a `<polyline>` element.

###### linear\_interpolation

UID
:   asam.net:xodr:1.9.0:road.object.skeleton.vertex\_road.linear\_interpolation

Description
:   Values of @radius or @width and @length attributes shall be interpolated linearly between two `<vertexRoad>` points.

###### no\_radius\_with\_width\_length

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.vertex\_road.no\_radius\_with\_width\_length

Description
:   `<vertexRoad>` elements shall not use @radius together with @width and @length attributes in one `<polyline>` element.

###### polyline\_elements

UID
:   asam.net:xodr:1.8.0:road.object.skeleton.vertex\_road.polyline\_elements

Description
:   There shall be no `<vertexLocal>` element next to a `<vertexRoad>` element inside the same `<polyline>` element.

#### F.6.16.14 surface

##### avoid\_skewed\_crg\_surfacees

UID
:   asam.net:xodr:1.9.0:road.object.surface.avoid\_skewed\_crg\_surfacees

Description
:   To avoid skewed CRG surfaces, the @perpToRoad attribute should only be used for objects that are smaller than the local radius of the curvature of the road elevation.

##### calculate\_road\_height

UID
:   asam.net:xodr:1.7.0:road.object.surface.calculate\_road\_height

Description
:   If `crgEvaluv2z` returns NaN, then the road height at that position shall be the ASAM OpenDRIVE height in addition to the road surface CRG, if it is present. The value of @hideRoadSurfaceCRG attribute shall have no influence.The value of @hideRoadSurfaceCRG attribute shall have no influence.

##### crg\_hidden\_on\_object\_overlap

UID
:   asam.net:xodr:1.7.0:road.object.surface.crg\_hidden\_on\_object\_overlap

Description
:   If a road surface CRG is present, that is, the CRG area overlaps the bounding volume of the object and has any mode other than attached, then @hideRoadSurfaceCRG shall be false.

##### identical\_local\_coordinates

UID
:   asam.net:xodr:1.7.0:road.object.surface.identical\_local\_coordinates

Description
:   The local coordinate system of the CRG shall be identical to the local coordinate system of the object to which it belongs. The reference line, inertial position, curvature, and heading of the CRG file shall be ignored.

##### no\_bounding\_box\_overlap

UID
:   asam.net:xodr:1.7.0:road.object.surface.no\_bounding\_box\_overlap

Description
:   The bounding volumes of objects with `<surface>` elements shall not overlap.

##### object\_reference\_on\_overlap

UID
:   asam.net:xodr:1.7.0:road.object.surface.object\_reference\_on\_overlap

Description
:   An object with a `<surface>` element shall be referenced on all roads it overlaps, using `<object>` and `<objectReference>` elements.

##### only\_for\_angular\_boxes

UID
:   asam.net:xodr:1.7.0:road.object.surface.only\_for\_angular\_boxes

Description
:   Only objects with angular bounding volumes may contain `<surface>` elements. Circular objects or objects with `<outlines>` elements shall not contain `<surface>` elements.

##### only\_one\_crg\_file

UID
:   asam.net:xodr:1.7.0:road.object.surface.only\_one\_crg\_file

Description
:   An object shall not reference more than one CRG file.

##### repeat\_discretely\_not\_continously

UID
:   asam.net:xodr:1.7.0:road.object.surface.repeat\_discretely\_not\_continously

Description
:   Objects with `<surface>` elements may repeat discretely, but not continuously. See  [Section 13.4, "Repeating objects"](../13_objects/13_04_repeating_objects.html#top-fc693ed2-a38b-4cfc-a346-90c8a478bfd0).

#### F.6.16.15 tunnels

##### from\_lower\_equal\_to

UID
:   asam.net:xodr:1.7.0:road.object.tunnels.from\_lower\_equal\_to

Description
:   The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

##### type\_definition

UID
:   asam.net:xodr:1.7.0:road.object.tunnels.type\_definition

Description
:   The @type of the tunnel shall be specified.

#### F.6.16.16 validty

##### check\_parent\_orientation

UID
:   asam.net:xodr:1.7.0:road.object.validty.check\_parent\_orientation

Description
:   The range given by all `<validity>` elements shall be a subset of the parent’s @orientation attribute:

##### from\_lower\_equal\_to

UID
:   asam.net:xodr:1.7.0:road.object.validty.from\_lower\_equal\_to

Description
:   The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

##### left\_hand\_traffic\_lane\_ids

UID
:   asam.net:xodr:1.7.0:road.object.validty.left\_hand\_traffic\_lane\_ids

Description
:   For left-hand-traffic, @orientation="-" implies that the `<validity>` element shall only span negative lane ids, while @orientation="+" implies that the `<validity>` element shall only span positive lane ids.
    If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

##### right\_hand\_traffic\_lane\_ids

UID
:   asam.net:xodr:1.7.0:road.object.validty.right\_hand\_traffic\_lane\_ids

Description
:   For right-hand traffic, @orientation="+" implies that the `<validity>` element shall only span negative lane ids, while @orientation="-" implies that the `<validity>` element shall only span positive lane ids.
    If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

### F.6.17 railroad

#### F.6.17.1 one\_rail\_per\_road

UID
:   asam.net:xodr:1.7.0:road.railroad.one\_rail\_per\_road

Description
:   There shall only be one tram or one rail lane per road.

#### F.6.17.2 rail\_lane\_width\_validity

UID
:   asam.net:xodr:1.7.0:road.railroad.rail\_lane\_width\_validity

Description
:   The width of the lane shall be at least the width rail-bound vehicles.

#### F.6.17.3 rail\_refline\_centered

UID
:   asam.net:xodr:1.7.0:road.railroad.rail\_refline\_centered

Description
:   The road reference line shall be in the center of the pair of railroad tracks.

#### F.6.17.4 platforms

##### min\_amount

UID
:   asam.net:xodr:1.7.0:road.railroad.platforms.min\_amount

Description
:   There shall be at least one platform per station.

##### min\_segments

UID
:   asam.net:xodr:1.7.0:road.railroad.platforms.min\_segments

Description
:   A platform shall contain at least one segment.

#### F.6.17.5 segment

##### segments\_per\_platform\_min\_amount

UID
:   asam.net:xodr:1.7.0:road.railroad.segment.segments\_per\_platform\_min\_amount

Description
:   There shall be at least one segment per platform.

#### F.6.17.6 stations

##### one\_platform\_per\_station

UID
:   asam.net:xodr:1.7.0:road.railroad.stations.one\_platform\_per\_station

Description
:   A `<station>` element shall be followed by at least one `<platform>` element.

#### F.6.17.7 switch

##### check\_switch\_conn

UID
:   asam.net:xodr:1.7.0:road.railroad.switch.check\_switch\_conn

Description
:   Main tracks shall not be used to connect two switches.

##### single\_switch\_no\_partner

UID
:   asam.net:xodr:1.7.0:road.railroad.switch.single\_switch\_no\_partner

Description
:   Single switches do not have partner switches.

### F.6.18 shape

#### F.6.18.1 elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.shape.elem\_asc\_order

Description
:   `<shape>` elements shall be defined in ascending order, firstly according to the s-coordinate and secondly according to the t-coordinate.

#### F.6.18.2 t\_definition\_coverage

UID
:   asam.net:xodr:1.4.0:road.shape.t\_definition\_coverage

Description
:   At all s-positions the t-definition has to cover the maximum road width of the entire road.

### F.6.19 signal

#### F.6.19.1 priority

UID
:   asam.net:xodr:1.7.0:road.signal.priority

Description
:   If present, signals shall be used in priority to other traffic rules.

#### F.6.19.2 signal\_type

UID
:   asam.net:xodr:1.7.0:road.signal.signal\_type

Description
:   Signals shall have a specific type and subtype.

#### F.6.19.3 use\_country\_code

UID
:   asam.net:xodr:1.7.0:road.signal.use\_country\_code

Description
:   A country code shall be added to refer to country-specific rules using the @country attribute.

#### F.6.19.4 boards

##### multi\_board\_have\_sub\_boards

UID
:   asam.net:xodr:1.8.0:road.signal.boards.multi\_board\_have\_sub\_boards

Description
:   A multi board shall have at least one static signal board and at least one variable message board.

##### multi\_board\_use\_correct\_type

UID
:   asam.net:xodr:1.8.0:road.signal.boards.multi\_board\_use\_correct\_type

Description
:   Multi boards shall be specified to be @type="multiBoard".

##### multi\_board\_use\_dynamic\_true

UID
:   asam.net:xodr:1.8.0:road.signal.boards.multi\_board\_use\_dynamic\_true

Description
:   Multi boards shall be specified to be @dynamic="true".

##### static\_boards\_no\_single\_signal

UID
:   asam.net:xodr:1.9.0:road.signal.boards.static\_boards\_no\_single\_signal

Description
:   Static boards shall not be used for single signals, for example, a stop sign on a single sheet of metal.

##### static\_board\_use\_correct\_type

UID
:   asam.net:xodr:1.8.0:road.signal.boards.static\_board\_use\_correct\_type

Description
:   Static signal boards shall be specified to be @type="staticBoard".

#### F.6.19.5 controller

##### valid\_for\_signals

UID
:   asam.net:xodr:1.7.0:road.signal.controller.valid\_for\_signals

Description
:   Controllers shall be valid for one or more signals.

#### F.6.19.6 dependency

##### multiple\_dependency

UID
:   asam.net:xodr:1.7.0:road.signal.dependency.multiple\_dependency

Description
:   A signal may have multiple dependencies.

#### F.6.19.7 gantry

##### all\_variable\_boards\_same\_gantry

UID
:   asam.net:xodr:1.9.0:road.signal.gantry.all\_variable\_boards\_same\_gantry

Description
:   All variable message boards within a `<vmsGroup>` element shall belong to the same gantry.

##### vmsgroup\_at\_least\_one\_reference

UID
:   asam.net:xodr:1.9.0:road.signal.gantry.vmsgroup\_at\_least\_one\_reference

Description
:   Each gantry shall have one `<vmsGroup>` element with at least one `<vmsBoardReference>` element.

#### F.6.19.8 reference

##### from\_lower\_equal\_to

UID
:   asam.net:xodr:1.7.0:road.signal.reference.from\_lower\_equal\_to

Description
:   The value of the @fromLane attribute shall be lower than or equal to the value of the @toLane attribute.

##### left\_hand\_traffic\_lane\_ids

UID
:   asam.net:xodr:1.7.0:road.signal.reference.left\_hand\_traffic\_lane\_ids

Description
:   For left-hand-traffic, @orientation="-" implies that the `<validity>` element shall only span negative lane ids, while @orientation="+" implies that the `<validity>` element shall only span positive lane ids. If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

##### right\_hand\_traffic\_lane\_ids

UID
:   asam.net:xodr:1.7.0:road.signal.reference.right\_hand\_traffic\_lane\_ids

Description
:   For right-hand traffic, @orientation="+" implies that the `<validity>` element shall only span negative lane ids, while @orientation="-" implies that the `<validity>` element shall only span positive lane ids. If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used

##### specify\_direction

UID
:   asam.net:xodr:1.7.0:road.signal.reference.specify\_direction

Description
:   The direction on the road for which the referenced signal is valid shall be specified for every `<signalReference>` element using the @orientation attribute.

##### used\_for\_signals\_only

UID
:   asam.net:xodr:1.7.0:road.signal.reference.used\_for\_signals\_only

Description
:   Signal reference shall be used for signals only.

#### F.6.19.9 semantics

##### no\_semantics\_without\_category

UID
:   asam.net:xodr:1.9.0:road.signal.semantics.no\_semantics\_without\_category

Description
:   Signal semantics shall not be specified for signs if no category for the desired traffic behavior exists.

#### F.6.19.10 validity

##### left\_hand\_traffic\_lane\_ids

UID
:   asam.net:xodr:1.7.0:road.signal.validity.left\_hand\_traffic\_lane\_ids

Description
:   For left-hand-traffic, @orientation="-" implies that the `<validity>` element shall only span negative lane ids, while @orientation="+" implies that the `<validity>` element shall only span positive lane ids. If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

##### right\_hand\_traffic\_lane\_ids

UID
:   asam.net:xodr:1.7.0:road.signal.validity.right\_hand\_traffic\_lane\_ids

Description
:   For right-hand traffic, @orientation="+" implies that the `<validity>` element shall only span negative lane ids, while @orientation="-" implies that the `<validity>` element shall only span positive lane ids.
    If the given `<validity>` elements span both, positive and negative lane ids, @orientation="none" shall be used.

### F.6.20 superelevation

#### F.6.20.1 elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.superelevation.elem\_asc\_order

Description
:   `<superelevation>` elements shall be defined in ascending order according to the s-coordinate.

### F.6.21 type

#### F.6.21.1 create\_new\_type\_in\_parent

UID
:   asam.net:xodr:1.4.0:road.type.create\_new\_type\_in\_parent

Description
:   When the type of road changes, a new `<type>` element shall be created within the parent `<road>` element.

#### F.6.21.2 elem\_asc\_order

UID
:   asam.net:xodr:1.4.0:road.type.elem\_asc\_order

Description
:   `<type>` elements shall be defined in ascending order according to the s-coordinate.

#### F.6.21.3 lane\_type\_may\_differ\_from\_parent

UID
:   asam.net:xodr:1.4.0:road.type.lane\_type\_may\_differ\_from\_parent

Description
:   Single lanes may have another type than the road they belong to. Road type and lane type represent different properties and are both valid if specified.

#### F.6.21.4 only\_alpha\_2\_country\_codes

UID
:   asam.net:xodr:1.7.0:road.type.only\_alpha\_2\_country\_codes

Description
:   There shall only be ALPHA-2 country codes in use, no ALPHA-3 country codes, because only ALPHA-2 country codes support state identifiers.

### F.6.22 use\_cases

#### F.6.22.1 shape\_elements\_start\_right

UID
:   asam.net:xodr:1.9.0:road.use\_cases.shape\_elements\_start\_right

Description
:   To model road shapes, shape elements shall start at the right side of the road, that is in positive t-direction. That means the elements start with negative t-values.