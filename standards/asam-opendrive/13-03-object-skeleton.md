# ASAM Opendrive v1.9.0 — 13.3 Object skeleton

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_03_object_skeleton.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.3 Object skeleton

An object may use a skeleton polyline to describe its shape more closely where all its vertices lie inside the object’s bounding volume.
This skeleton can define the appropriate parts of an object by a series of points with either a radius or a width and height.
This effectively approximates the shape of an object using boxes, cylinders, and frustums.
It also adds the possibility to define an @intersectionPoint attribute in order to describe where that object touches the road or ground surface.
These intersection points have to be determined based on the object’s origin and rotation as well as those of the road or ground surface.

Only objects of certain values of the @type attribute shall be described with these skeleton polylines.

The `<skeleton>` element serves as a wrapper for the `<polyline>` element that contains further elements to describe the different points of that polyline.

**Elements in UML model**

**`<skeleton>` element**

In ASAM OpenDRIVE, the skeleton of objects is represented by the `<skeleton>` element within the `<object>` element.

```
UML class:  t_road_objects_object_skeleton
XML tag:    <skeleton> (Multiplicity: 0..1)
Introduced: 1.8.0
```

Wrapper for the object polylines, that can be used to describe the actual shape inside the bounding volume more closely.

**`<polyline>` element**

In ASAM OpenDRIVE, the polyline of a skeleton is represented by the `<polyline>` element within the `<skeleton>` element.

```
UML class:  t_road_objects_object_skeleton_polyline
XML tag:    <polyline> (Multiplicity: 1..*)
Introduced: 1.8.0
```

Defines a series of points relative to the road reference line.

An `<polyline>` element shall be followed by either two or more `<vertexRoad>` elements or by two or more `<vertexLocal>` elements.

Table 92. Attributes of the <polyline> element


| Name | Type | Use | Introduced | Description |
| --- | --- | --- | --- | --- |
| `id` | positiveInteger | optional | 1.8.0 | ID of the polyline. Must be unique within one object. |

**Rules**

The following rules apply to `<skeleton>` elements:

* [asam.net:xodr:1.8.0:road.object.skeleton.polyline\_followed\_by\_vertex](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-polyline-followed-by-vertex): A `<polyline>` element shall be followed by either two or more `<vertexRoad>` elements or by two or more `<vertexLocal>` elements.

* The `<polyline>` element may use the @intersectionPoint attribute set to "true" for its point to specify where that object intersects with the ground.

* [asam.net:xodr:1.8.0:road.object.skeleton.points\_inside\_box](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-points-inside-box): All points of the `<polyline>` element must be located inside the bounding volume.

* [asam.net:xodr:1.9.0:road.object.skeleton.points\_boundary\_inside\_box](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-skeleton-points-boundary-inside-box): The boundary, defined by either width and height or radius, of each point of an object’s skeleton shall at least partially be located inside the bounding volume.

* The boundary of each point should be defined such that it stays within the object’s bounding volume as much as possible.

* [asam.net:xodr:1.8.0:road.object.skeleton.points\_requirements](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-points-requirements): All points of the `<polyline>` element are connected with a straight line between the `<vertexRoad>` or `<vertexLocal>` elements and the specified @radius or @width and @height attributes of each point are perpendicular to this line.

* Changes in @radius or @width and @height attributes between points of the `<polyline>` element shall be interpolated linearly.

* [asam.net:xodr:1.8.0:road.object.skeleton.use\_radius\_or\_width\_length](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-use-radius-or-width-length): Each `<polyline>` element shall either use @radius or @width and @length attributes for all of its vertex elements.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.3.1, “`<vertexRoad>` element”](#sec-898f3cd1-0313-4df7-921e-7f99415d2918)
* [Section 13.3.2, “`<vertexLocal>` element”](#sec-63c9f5b5-63d3-46ba-86fc-1a9a3f4317e8)

## 13.3.1. `<vertexRoad>` element

`<vertexRoad>` elements are mandatory elements inside a `<polyline>` element.
They are used to describe a more detailed form of objects.
Each `<vertexRoad>` element must lie inside the object’s bounding volume.
They are mutually exclusive with `<vertexLocal>` elements.
`<vertexRoad>` elements describe a skeleton polyline of objects relative to the road reference line with their s- and t-coordinates.

The shape of a polyline may be described by the object’s local width and length or radius at each `<vertexRoad>` point and the `<vertexRoad>` point’s difference in height @dz relative to the road reference line (parallel to z in the inertial coordinate system).

**Elements in UML model**

**`<vertexRoad>` element**

In ASAM OpenDRIVE, polyline points that use s- and t-coordinates are represented by the `<vertexRoad>` element within the `<polyline>` element.

```
UML class:  t_road_objects_object_skeleton_polyline_vertexRoad
XML tag:    <vertexRoad> (Multiplicity: 2..*)
Introduced: 1.8.0
```

Defines a point on the object’s polyline in road coordinates.
`<vertexRoad>` can use either radius or length/width within one `<polyline>` element.

Table 93. Attributes of the <vertexRoad> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `dz` | double | required | m | 1.8.0 | Offset of the polyline point relative to the road reference line parallel to z in the inertial coordinate system. |
| `id` | positiveInteger | optional |  | 1.8.0 | ID of the vertex point. Must be unique within one polyline. |
| `intersectionPoint` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional |  | 1.8.0 | Vertex point is intersecting the ground. "false" is used as default. |
| `radius` | double | optional | m | 1.8.0 | Local radius of the object at this vertex point, along the polyline |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m | 1.8.0 | s-coordinate of the corner |
| `t` | double | required | m | 1.8.0 | t-coordinate of the corner |

**XML example**

![img](../_images/13_objects/object_skeleton_pole.png)

Figure 118. Example of the bounding volume and skeleton of a traffic light pole

[Figure 118](#fig-b2b29a46-5e48-47d9-8eb7-029031c97bb9) shows a traffic light pole with an extension arm that spans over the street which can be described with two separate polylines, one for the main pole that defines an intersection point and one for the extension arm.

```
<object type="pole"
        subtype="trafficLight"
        name=""
        id="4000002"
        s="25.0"
        t="1.5"
        zOffset="0.00"
        roll="0"
        pitch="0"
        validLength="0"
        orientation="none"
        height="4"
        length="0.3"
        width="3"
        dynamic="no"
        hdg="0">
    <skeleton>
        <polyline id="1">
            <vertexRoad s="25.0" t="2.8" dz="0.0" radius="0.15" id="0" intersectionPoint="true"/>
            <vertexRoad s="25.0" t="2.8" dz="4.0" radius="0.10" id="1"/>
        </polyline>
        <polyline id="2">
            <vertexRoad s="25.0" t="2.8" dz="3.0" radius="0.15" id="0"/>
            <vertexRoad s="25.0" t="2.15" dz="3.25" radius="0.15" id="1"/>
            <vertexRoad s="25.0" t="0.0" dz="3.25" radius="0.15" id="2"/>
        </polyline>
    </skeleton>
</object>
```

**Rules**

The following rules apply to `<vertexRoad>` elements:

* [asam.net:xodr:1.8.0:road.object.skeleton.vertex\_road.element\_min\_amount](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-vertex-road-element-min-amount): There shall be at least two `<vertexRoad>` elements inside a `<polyline>` element.

* [asam.net:xodr:1.8.0:road.object.skeleton.vertex\_road.polyline\_elements](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-vertex-road-polyline-elements): There shall be no `<vertexLocal>` element next to a `<vertexRoad>` element inside the same `<polyline>` element.

* [asam.net:xodr:1.8.0:road.object.skeleton.vertex\_road.no\_radius\_with\_width\_length](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-vertex-road-no-radius-with-width-length): `<vertexRoad>` elements shall not use @radius together with @width and @length attributes in one `<polyline>` element.

* [asam.net:xodr:1.9.0:road.object.skeleton.vertex\_road.linear\_interpolation](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-skeleton-vertex-road-linear-interpolation): Values of @radius or @width and @length attributes shall be interpolated linearly between two `<vertexRoad>` points.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.3.2, “`<vertexLocal>` element”](#sec-63c9f5b5-63d3-46ba-86fc-1a9a3f4317e8)

## 13.3.2. `<vertexLocal>` element

`<vertexLocal>` elements are mandatory elements inside an `<polyline>` element.
They are used to describe a more detailed form of objects.
Each `<vertexLocal>` element must lie inside the object’s bounding volume.
They are mutually exclusive with `<vertexRoad>` elements.
`<vertexLocal>` describe a skeleton polyline of objects within a local u/v coordinate system.

The polyline shape of an object may be described by the object’s local width and length or radius at each `<vertexLocal>` point.

**Elements in UML model**

**`<vertexLocal>` element**

In ASAM OpenDRIVE, polyline points that use local u- and v-coordinates are represented by the `<vertexLocal>` element within the `<polyline>` element.

```
UML class:  t_road_objects_object_skeleton_polyline_vertexLocal
XML tag:    <vertexLocal> (Multiplicity: 2..*)
Introduced: 1.8.0
```

Defines a vertex point on the object polyline relative to the object’s origin in local u/v-coordinates.
The origin and the orientation of the object are given by the @s, @t, @zOffset and @hdg attributes of the element.
`<vertexLocal>` can use either radius or length/width within one `<polyline>` element.

Table 94. Attributes of the <vertexLocal> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `id` | positiveInteger | optional |  | 1.8.0 | ID of the vertex point. Must be unique within one polyline. |
| `intersectionPoint` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional |  | 1.8.0 | Vertex point is intersecting the ground. "false" is used as default. |
| `radius` | double | optional | m | 1.8.0 | Local radius of the object at this vertex point, along the polyline |
| `u` | double | required | m | 1.8.0 | Local u-coordinate of the vertex point |
| `v` | double | required | m | 1.8.0 | Local v-coordinate of the vertex point |
| `z` | double | required | m | 1.8.0 | Local z-coordinate of the vertex point |

**XML example**

![img](../_images/13_objects/object_skeleton_tree.png)

Figure 119. Example of the skeleton of a tree

[Figure 119](#fig-7b220bcb-ef7f-40b9-ad93-66d63333b886) shows a leaf tree which can be described with two separate polylines, one for the trunk that defines an intersection point and one for the crown.

```
<object type="tree"
        subtype="leaf"
        name="leafTree"
        id="6"
        s="9"
        t="-5"
        zOffset="-1.00"
        roll="0"
        pitch="0"
        validLength=""
        orientation="none"
        height="7.50"
        length="4.00"
        width="4.00"
        dynamic="no"
        hdg="0">
    <skeleton>
        <polyline id="1">
            <vertexLocal u="-0.2" v="1.0" z="0" radius="0.15" id="0"/>
            <vertexLocal u="-0.2" v="1.0" z="1.000" radius="0.15" id="1" intersectionPoint="true"/>
            <vertexLocal u="-0.2" v="1.0" z="4.500" radius="0.12" id="2"/>
        </polyline>
        <polyline id="2">
            <vertexLocal u="0.0" v="0.0" z="4.0" radius="2.0" id="0"/>
            <vertexLocal u="0.0" v="0.0" z="7.5" radius="2.0" id="1"/>
        </polyline>
    </skeleton>
</object>
```

**Rules**

The following rules apply to `<vertexLocal>` elements:

* [asam.net:xodr:1.8.0:road.object.skeleton.vertex\_local.element\_min\_amount](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-vertex-local-element-min-amount): There shall be at least two `<vertexLocal>` elements inside an `<polyline>` element.

* [asam.net:xodr:1.9.0:road.object.skeleton.vertex\_local.no\_mixing\_road\_local](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-object-skeleton-vertex-local-no-mixing-road-local): There shall be no `<vertexRoad>` element next to a `<vertexLocal>` element inside the same `<polyline>` element.

* [asam.net:xodr:1.8.0:road.object.skeleton.vertex\_local.vertex\_local\_elements](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-vertex-local-vertex-local-elements): `<vertexLocal>` elements shall not use @radius together with @width and @length attributes in one `<polyline>` element.

* [asam.net:xodr:1.8.0:road.object.skeleton.vertex\_local.linear\_interpolation](../16_annexes/map_rules.html#asam-net-xodr-1-8-0-road-object-skeleton-vertex-local-linear-interpolation): Values of @radius or @width and @length attributes will be interpolated linearly between two `<vertexLocal>` points.

**Related topics**

* [Section 13.1, "Introduction to objects"](13_01_introduction.html#top-e2ec908d-ae0b-4f5c-99f5-2b12761a368a)
* [Section 13.3.1, “`<vertexRoad>` element”](#sec-898f3cd1-0313-4df7-921e-7f99415d2918)