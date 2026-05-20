# ASAM OpenMATERIAL® 3D latest — 7.2 General

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/07_geometry/general.html
> **Standard**: ASAM OpenMATERIAL® 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.2 General

## 7.2.1 Dimensions

Unless stated otherwise, all numeric values within ASAM OpenMATERIAL® 3D are in SI units. [Table 15](#tab-quantities-units) lists the units and dimensions:

Table 15. Quantities and units


| Name | Unit | Symbol |
| --- | --- | --- |
| acceleration | meters per second squared | m/s2 |
| plane angle | radians | rad |
| distance, dimension, length | meter | m |
| mass | kilogram | kg |
| time | second | s |
| speed | meters per second | m/s |

## 7.2.2 Coordinate systems

ASAM OpenMATERIAL® 3D uses the following types of coordinate systems:

* World coordinate system, see [Section 7.2.2.1, "World coordinate system"](#_world_coordinate_system)
* Local coordinate system, see [Section 7.2.2.2, "Local coordinate system"](#_local_coordinate_system)

Both coordinate systems consist of three orthogonal directions associated with
x-, y-, and z-axes, and a coordinate origin where axes meet. The coordinate
systems are right-handed Cartesian coordinate systems according to ISO 8855 [[7](../bibliography.html#bib-iso8855)]. For
a non-rotated coordinate system, the following applies:

* Forward matches x-axis
* Left matches y-axis
* Up matches z-axis

The positive rotation is assumed to be counter-clockwise ("right-hand rule").
Orientation of objects is expressed extrinsically by the yaw, pitch, and roll
angles derived from the Euler rotation sequence in the order z-axis, then
y-axis, then x-axis.

![img](../_images/fig_coordinate_system.svg)

Figure 3. Yaw, pitch, and roll angle in an ISO 8855:2011 compliant coordinate system

[Figure 3](#fig-coordinate-system) shows a right-handed coordinate system.

![img](../_images/fig_coo_sys_rotation.svg)

Figure 4. Coordinate system with defined rotations

[Figure 4](#fig-coo-sys-rotation) shows the positive axes and positive directions of the
corresponding angles.

![img](../_images/fig_coo_sys_example.svg)

Figure 5. Examples of rotations in coordinate system

[Figure 5](#fig-coo-sys-example) shows the different states of a coordinate
system with defined rotations. x’/y’/(z’=z) denotes the coordinate system after
rotating x/y/z with the heading angle around the z-axis. The coordinate system
x’’/(y’’=y’)/z’’ denotes the coordinate system after rotating x’/y’/z’ with the
pitch angle around the y’-axis. The final rotated coordinate system
(x’’’=x’’)/y’’’/z’’’ is obtained after rotating system x’’/y’’/z’’ with roll
angle.

Each *3D model* has an individual reference frame. Individual nodes of an
object may have local coordinate frames, for example, each wheel of a vehicle.

### 7.2.2.1 World coordinate system

A coordinate system of type (x, y, z) that is fixed in the inertial reference frame of
the simulation environment has the xw- and yw-axes parallel to the ground
plane and the zw-axis pointing upward.

Neither origin nor orientation of the world coordinate system are defined by the ASAM OpenMATERIAL® 3D standard. Nevertheless, the origin of the world coordinate system in an ASAM OpenMATERIAL® 3D environment should coincide with the origin of a corresponding ASAM OpenDRIVE® map (if available).
The origin of the world coordinate system in ASAM OSI should also be aligned with these two coordinate systems.

### 7.2.2.2 Local coordinate system

Top-most local coordinate frames of *3D assets* (so-called reference coordinate frames) in ASAM OpenMATERIAL® 3D are defined in the center of the bounding box of the corresponding asset, projected to the bottom of the bounding box.
By static transformations, these coordinate frames may be synchronized with reference coordinate frames in ASAM OpenSCENARIO XML and ASAM OSI.
[Table 16](#tab-local-coordinates) provides an overview of the translations between ASAM OpenMATERIAL® 3D asset reference coordinates and ASAM OpenSCENARIO XML and ASAM OSI reference coordinates.

Table 16. Transformation of asset coordinates to ASAM OpenSCENARIO XML and ASAM OSI


| Standard | Coordinate System | Transformation |
| --- | --- | --- |
| ASAM OpenSCNEARIO XML | Vehicle | The origin is the center of the rear axle projected to the ground. Add the x-coordinate of the [rear axle](asset-schema.html#_rearaxle) from the vehicle asset metadata to the ASAM OpenMATERIAL® 3D reference frame. |
| ASAM OSI | Moving or stationary object | The origin is in the center of the bounding box. Add half of the height of the asset defined as the maximum z-coordinate in the [bounding box](asset-schema.html#_boundingbox) to the ASAM OpenMATERIAL® 3D reference frame. |
| ASAM OSI | Host vehicle | The origin is the center of the rear axle. Add the x- and z-coordinate of the [rear axle](asset-schema.html#_rearaxle) from the vehicle asset metadata to the ASAM OpenMATERIAL® 3D reference frame. |

Besides reference coordinate frames, *3D assets* may incorporate other local coordinate frames, see [Section 7.3.1, "Object classes introduction"](object-classes-introduction.html).

## 7.2.3 Naming conventions

### 7.2.3.1 General

The following naming conventions apply to ASAM OpenMATERIAL® 3D geometry files:

* The *3D model* file and the related *3D asset* file shall have the same base name.
  Example: `Example.gltf`, `Example.xoma`
* The naming convention inside the *3D model* file (contains 3D information) must follow the capital Snake\_Case definition, to improve human readability and enable consistent parsing of the file structure.
* The naming convention inside the *3D asset* file (contains metadata) must follow the lowerCamelCase definition, to allow a consistent naming convention in all JSON files and consistent parsing.
* Keywords are predefined names for objects inside the node structure.

### 7.2.3.2 Node structure

Every node structure for a 3D object uses predefined keywords to allow a consistent naming convention and parsing.
Some keywords are already defined by the ASAM OpenMATERIAL® 3D standard and more could follow in future updates.
Users are free to add more keywords for themself, if they are needed. The following rules apply:

* All components shall be named according to capital snake case definition, starting with uppercase letters.
* Group nodes (also known as empty nodes or parent nodes) shall have "Grp\_" as a prefix.
* Iterators shall be added as suffixes.
  In the documentation, iterator names are written in angled brackets. Example: `<type_idx>`.
  In the node name itself, the iterator names are replaced by integer values, starting from 0.
* Sequence of suffixes:

  + 1: Iterator
  + 2: Type Enumerator
  + 3: Subtype Enumerator.
* The predefined keywords shall be used for the corresponding asset parts and can be found in the corresponding subchapters.

### 7.2.3.3 Metadata

The following rules for metadata apply:

* Fields shall be named according to the lowerCamelCase definition, starting with lowercase letters.
* Naming of custom properties shall follow the predefined keys.
* Objects, arrays (lists), and enums shall follow the notation in the corresponding JSON files.

## 7.2.4. *3D asset* file

The *3D asset* file provides metadata as well as a mapping table to ASAM OpenMATERIAL® 3D *material property* files.
This information extends the geometry of an asset given in standard *3D model* file formats, for example, glTF, FBX, or USD.
The *3D asset* file is in JSON format with the file extension .xoma.
The asset file has to have the same file name as the accompanying *3D model*.
The following is an example of a *3D model* file in glTF format with an accompanying *3D asset* file:

* `my-model.gltf`
* `my-model.xoma`

## 7.2.5 Asset Type

In the current specification of ASAM OpenMATERIAL® 3D, assets of type 'object' and 'scene' can be specified.
Since the concept of 'scene' has been replaced by the following concept of referencing external assets, it can be understood as deprecated.

## 7.2.6 References to external assets

To accommodate use cases in which 3D objects are not built from single assets but from (variable) compositions of assets
(e.g., vehicles with roof racks and bicycles, environments built up by separate layers or enhanced with additional objects),
ASAM OpenMATERIAL® 3D allows external assets to be referenced in the *3D asset* file.

To do this, the *3D asset* files of external assets must be associated with a node of an overarching asset in its *3D asset* file.
This node acts as parent to the external assets and determines their spatial placement and orientation.
The mapping is implemented as a list of key-value pairs of parent nodes and references to *3D asset* files.

Example:
A Grp\_Wheel\_Steering\_Rotating\_<axle\_idx>\_<wheel\_idx> node in a vehicle asset could be a parent node for interchangeable car wheels, which are individually referenced from external assets.

## 7.2.7 Requirements

* The geometry of the object shall be in real-word scale, using meters as the unit for measurement distances.
* The object’s origins and pivot points shall coincide with position and orientation of the origin of the object’s reference coordinate frame, unless otherwise specified.
* Meshes shall not contain problematic characteristics such as doubled, isolated, coincident, coplanar, degenerate, or primitives.
* Meshes shall have outside facing normals. Soft or hard edges shall be set correctly.
* Meshes shall not be empty or contain multiple level of details (LoDs).
* Meshes shall be triangulated. Potential normal maps shall match that triangulation.
* Rendering materials shall support physically based rendering (PBR) workflows and there shall not be geometry without assigned material.
* Additional requirements apply when ASAM OpenMATERIAL® 3D assignment textures are used:

  + UV channel 1 shall be used for assignment textures.
  + UV Islands shall have margins in between, so that assignment texture interpolation errors are avoided.
  + There shall not be any geometry without UV coverage.

## 7.2.8 Recommendations

* UVs should not overlap and be within 0-1 UV space.
* Elongated primitives should be avoided as they fit badly in acceleration structures.
* Alpha-textured meshes should be optimized to minimize the amount of alpha testing.
* Meshes should not have holes or gaps.
* Meshes should have a clean edgeflow.
* Usage of N-Gons is not recommended.
* Faces should be one-sided.
* An object’s shape should have the lowest possible number of polygons.
* Texel density should be homogeneous and as low as possible.
* UV stretching should be minimized.
* Naming of files, nodes, meshes, and materials should be meaningful.
* Usage of multiple PBR maps is encouraged, for example, albedo, roughness, metallic, normals.
* Smaller objects should have one *material* per object, for example, baked traffic cone. Larger objects should contain multiple seamless repeatable materials, for example, brick building.

## 7.2.9 Lighting

The lighting concept in ASAM OpenMATERIAL® 3D introduces a clear distinction between discrete light sources, e.g., point lights or spotlights) and emissive materials, enabling both physically simulated light sources and visually emissive elements to be defined in a standardized way.

### 7.2.9.1 Discrete light sources

Discrete light sources represent active light sources that emit light into the environment.
They are defined within the XOMA file format using the lightDefinitions property.

Each discrete light source is associated with a corresponding node in the 3D model file.
This node determines the spatial placement and orientation of the light within the asset.

If the associated node follows a predefined naming convention for lighting group nodes of a specific asset class, the lighting function is implicitly defined.
For example:
A node named Grp\_Light\_Low\_Beam\_Left\_0 in a vehicle asset indicates that the light represents the left low beam.
In a simulation, this light is activated when the corresponding vehicle function (low beam) is enabled.

If a generic node name is used, no standardized function can be derived.
In such cases, the simulator may assign a lighting function arbitrarily, resulting in non-standardized behavior.

Additional properties of discrete light sources, such as intensity, color and beam shape, can be configured in the XOMA file as defined in the corresponding schema.

### 7.2.9.2 Emissive materials

Emissive materials are defined in the 3D model file and mapped within the XOMA file format using the emissiveLightMapping property.

Similar to discrete light sources, emissive materials are associated with nodes in the 3D model file.
However, in this case, the node does not define spatial positioning but is used solely to determine the lighting function via its name.
For example:
A material associated with the node Grp\_Light\_Indicator\_Left\_0 corresponds to the left turn indicator.
In a simulation, the emissive effect of the indicator is activated by modification of parameters or activation of textures of the corresponding material.

As with discrete light sources, generic node names lead to undefined behavior, allowing the simulator to decide the mapping.

The visual appearance of emissive materials is defined by materials within the 3D model file.
These materials are referenced in the XOMA file.

Additionally, emissive textures can be specified in the XOMA file.
A masking texture may be used to selectively control emissive regions for specific lighting functions.