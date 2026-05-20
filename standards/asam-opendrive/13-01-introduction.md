# ASAM Opendrive v1.9.0 — 13.1 Introduction to objects

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_01_introduction.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.1 Introduction to objects

Objects are items that influence a road by expanding, delimiting, or supplementing its course.
They are not mandatory to guide driver and traffic models, unlike signals.
However, signals may be linked to objects when the object directly relates to that signal.
An example would be the stop line (object) for a traffic light (signal).
For more on signal references, see  [Section 14.4, "Signal reference"](../14_signals/14_04_signal_reference.html#top-1030e9ff-6b75-4353-b2b4-043f08c02a2d).  
The most common examples are parking spaces, crosswalks, and traffic barriers.
Specific road markings for the control and regulation of road traffic are instead represented as signals.
For more on signals, see  [Section 14.1, "Introduction to signals"](../14_signals/14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a).

Every object is defined by a unique object id, the position of its origin point (in road reference line system coordinates), and a bounding volume.
The bounding volume of an object defines the object’s dimensions using simple geometric shapes.
In ASAM OpenDRIVE, this can either be a right rectangular prism (a box) or a cylinder.
In either case, no point of an object should be outside of that volume.
Conversely, each surface of the bounding volume should intersect with at least one point of the object.

Objects can be marked as "temporary".
Examples are temporary speed limit signs or traffic beacons for road works.
See also [Figure 60](../11_lanes/11_02_lane_layers.html#fig-8e54e01d-146a-4e0a-8e6c-f0ad6515b8c3) in  [Section 11.2, "Lane layers"](../11_lanes/11_02_lane_layers.html#top-709a1642-11e1-44bb-a26d-1de7478c23e3).

![img](../_images/13_objects/object_1.png)

Figure 111. Circular and angular object

[Figure 111](#fig-1c502436-9b71-49e2-b146-6658c7d081be) shows the bounding volume of an angular object using width, length, and height (bounding box) and the bounding volume of an circular object using radius and height (bounding cylinder).

Complex objects may be further described using `<outline>` or `<skeleton>` elements.
If an `<outline>` or `<skeleton>` element is defined, it supersedes the bounding volume.
However, every point of an `<outline>` or `<skeleton>` element of an object must be contained in its bounding volume.

Objects in ASAM OpenDRIVE do not change their position or orientation (heading, pitch, roll).

They may be declared dynamic or static:

* Dynamic objects are static but have one or more movable parts.
  Examples are fans in tunnels or windmills.
* Stationary objects are completely static without any movable parts.
  Examples are buildings or trees.

Objects are defined per `<road>` element.

![img](../_images/13_objects/object_18.png)

Figure 112. Placing objects on roads

[Figure 112](#fig-7ed192f9-7d81-4d9e-8b30-246cd9f36fd8) shows an object that is not properly placed on a road.
Objects that are placed on roads using the `<elevationProfile>` element or the `<lateralProfile>` element should be so small that these objects do not cut or float above the road surface significantly, nor cause skewed ASAM OpenCRG surfaces.

**Elements in UML model**

**`<objects>` element**

In ASAM OpenDRIVE, objects are represented by the `<objects>` element within the `<road>` element.

```
UML class: t_road_objects
XML tag:   <objects> (Multiplicity: 0..1)
```

Container for all objects along a road.

![img](../_images/uml_class_diagrams/EAID_981EF40C_984C_4522_BBD4_7466215BCDE0.png)

Figure 113. UML class diagram of the Objects class

[Figure 113](#fig-52ccdd39-1a3c-486c-a6d2-e6fff6202842) shows the UML class diagram of the ASAM OpenDRIVE Objects class.

**`<object>` element**

In ASAM OpenDRIVE, a single object is represented by the `<object>` element within the `<objects>` element.

```
UML class: t_road_objects_object
XML tag:   <object> (Multiplicity: 0..*)
```

Objects influence a road by expanding, delimiting, or supplementing its course.
Objects are elements that form the environment, for example, buildings, guard rails, poles, and trees.
Objects are not mandatory to guide driver and traffic models, unlike signals.

There are two ways to describe the bounding volume of objects.

* For an angular object: definition of the width, length and height.
* For a circular object: definition of the radius and height.

Table 85. Attributes of the <object> element


| Name | Type | Use | Unit | Introduced | Description |
| --- | --- | --- | --- | --- | --- |
| `dynamic` | [t\_yesNo](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_A171A2AA_DFE6_4b8b_BA5A_AD59E6334468) | optional |  |  | Indicates whether the object is dynamic or static, default value is “no” (static). Dynamic object cannot change its position. |
| `hdg` | double | optional | rad |  | Heading angle of the object relative to road direction |
| `height` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Height of the object’s bounding box.   @height is defined in the local coordinate system u/v along the z-axis |
| `id` | string | required |  |  | Unique ID within database |
| `invalidated` | boolean | optional |  | 1.9.0 | Indicates whether the object is currently invalidated. Example: crossed out traffic sign. |
| `length` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m |  | Length of the object’s bounding box, alternative to @radius.  @length is defined in the local coordinate system u/v along the u-axis |
| `name` | string | optional |  |  | Name of the object. May be chosen freely. |
| `orientation` | [e\_orientation](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_D8972119_8CE4_407e_A4AD_3183B0B5C687) | optional |  |  | "+" = valid in positive s-direction  "-" = valid in negative s-direction  "none" = valid in both directions  (does not affect the heading) |
| `perpToRoad` | [t\_bool](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_33A24631_A9D0_48ca_BB42_2B8417EDC05E) | optional |  | 1.7.0 | Alternative to @pitch and @roll. If true, the object is vertically perpendicular to the road surface at all points and @pitch and @roll are ignored. Default is false. |
| `pitch` | double | optional | rad |  | Pitch angle relative to the x/y-plane |
| `radius` | [t\_grZero](../16_annexes/map_uml_data_types.html#top-EAID_712BF396_F6CE_4c9f_861D_D959D28F0E13) | optional | m |  | radius of the circular object’s bounding box, alternative to @length and @width. @radius is defined in the local coordinate system u/v |
| `roll` | double | optional | rad |  | Roll angle relative to the x/y-plane |
| `s` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | required | m |  | s-coordinate of object’s origin |
| `subtype` | string | optional |  |  | Variant of a type |
| `t` | double | required | m |  | t-coordinate of object’s origin |
| `temporary` | boolean | optional |  | 1.9.0 | Indicates whether the object is temporary or permanent. Example: temporary speed limit sign in road works situation. |
| `type` | [e\_objectType](../16_annexes/enumerations/map_uml_enumerations.html#top-EAID_C47587D0_7173_42df_8BB7_36B2C598D95F) | optional |  |  | Type of object. For a parking space, the `<parkingSpace>` element may be used additionally. |
| `validLength` | [t\_grEqZero](../16_annexes/map_uml_data_types.html#top-EAID_77A53B88_22D3_4a7e_8C94_45AB3C7E221D) | optional | m |  | Validity of object along s-axis (0.0 for point object) |
| `width` | double | optional | m |  | Width of the object’s bounding box, alternative to @radius.  @width is defined in the local coordinate system u/v along the v-axis |
| `zOffset` | double | required | m |  | z-offset of object’s origin relative to the elevation of the road reference line |

For the different object types refer to [Combinations of elements and attributes for object types](13_14_object_examples.html#top-bd330b94-a6e3-42d9-a2b3-0bae5cb19e92).

**XML example**

```
<objects>
    <object type="building"
            name="ExampleBuilding"
            id="1"
            s="80.0"
            t="17.0"
            zOffset="0.0"
            orientation="none"
            length="12.15"
            width="22.415"
            height="11.84"
            hdg="1.44"
            pitch="0.0"
            roll="0.00">
    </object>
</objects>
```

**Rules**

The following rules apply to objects:

* [asam.net:xodr:1.7.0:road.object.type\_attr](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-type-attr): The type of an object shall be given by the @type attribute.

* An object may either be dynamic or static, but an object cannot change its position or its heading, pitch, or roll.
* Objects derived from ASAM OpenSCENARIO shall not be mixed with objects described in ASAM OpenDRIVE.

* [asam.net:xodr:1.7.0:road.object.orientation](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-orientation): The direction for which objects are valid shall be specified.

* [asam.net:xodr:1.7.0:road.object.s\_t\_coords](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-s-t-coords): The origin position of the object shall be described with s- and t-coordinates along the road surface.

* [asam.net:xodr:1.7.0:road.object.circular\_vs\_angular](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-object-circular-vs-angular): Objects may be of circular or angular shape. The possibilities are mutually exclusive. The shape is defined by the used attributes.

* An object’s placement may either be temporary or permanent, as indicated by @temporary.
* Omitting @temporary shall default to @temporary="false".
* Traffic actors should ignore objects with @invalidated="true".
* Omitting @invalidated shall default to @invalidated="false".

**Related topics**

* [Section 10.1, "Introduction to roads"](../10_roads/10_01_introduction.html#top-f0ae72f0-300e-4f8b-9c9b-7f68a467a9f7)
* [Section 13.2, "Object outline"](13_02_object_outline.html#top-67295042-9707-4ad5-9671-b80cde49bb3a)
* [Section 13.3, "Object skeleton"](13_03_object_skeleton.html#top-4c99f00a-bb80-4aff-8c87-c90313ecb3d6)
* [Section 13.4, "Repeating objects"](13_04_repeating_objects.html#top-fc693ed2-a38b-4cfc-a346-90c8a478bfd0)
* [Section 14.1, "Introduction to signals"](../14_signals/14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)
* [Section 14.4, "Signal reference"](../14_signals/14_04_signal_reference.html#top-1030e9ff-6b75-4353-b2b4-043f08c02a2d)