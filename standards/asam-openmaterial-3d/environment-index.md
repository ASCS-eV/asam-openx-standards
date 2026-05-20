# ASAM OpenMATERIAL® 3D latest — 7.3.4 Environment structure

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/07_geometry/object-environment/environment-index.html
> **Standard**: ASAM OpenMATERIAL® 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.3.4 Environment structure

## 7.3.4.1 General

The environment consists of the terrain, buildings, objects, and traffic areas, for example roads. It also includes all stationary traffic items, such as traffic signals, signs or lights.

The environment’s 3D geometry is structured according to the node structure defined in [Section 7.3.4.3, "Model structure"](#_model_structure).
The structure begins with a root node, which is the parent of all other nodes. If applicable, the origin of the root node should match that of the corresponding OpenDRIVE map.
Children of the root node are terrain, environment objects, and the road network.
The latter is further detailed by its child nodes, the drivable area, sidewalks, roadmarks, road objects, and signals.

An [example environment asset](https://github.com/asam-ev/OpenMATERIAL-3D/tree/main/examples/environment_example) is provided in the examples folder.

Groups with a local transform are indicated in the structure by a (T).
This is only an indicator in the documentation and must not be contained in the actual node name.

## 7.3.4.2 Naming convention

Every object has a unique name and represents a part of the environment.
All included meshes are part of a group to indicate which kind of object type it represents.
All meshes should be named meaningful.

If needed, the user is free to add more groups and new keywords, which are not part of the standard, for himself.

## 7.3.4.3 Model structure

### 7.3.4.3.1 Structure overview

Diagram

### 7.3.4.3.2 Grp\_Root

The environment consists of the terrain, buildings, objects, and traffic areas, for example roads. It also includes all stationary traffic items, such as traffic signals, signs, or lights.

If applicable, the origin of the root should match the [inertial coordinate frame](https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/08_coordinate_systems/08_02_inertial_coordinate_system.html) of a corresponding ASAM OpenDRIVE® map.

Table 102. Grp\_Root


| Grp\_Root | |
| --- | --- |
| **Origin** | Origin matching the [inertial coordinate frame](https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/08_coordinate_systems/08_02_inertial_coordinate_system.html) of an associated ASAM OpenDRIVE® map (if available) |
| **x-axis** | Pointing to the right (east for maps with geographic reference) |
| **y-axis** | Pointing up (north for maps with geographic reference) |
| **z-axis** | Pointing out of the drawing plane (up for maps with geographic reference) |

### 7.3.4.3.3 Grp\_Terrain

The terrain is characterized by the environment’s ground structure, such as hills, mountains, or flat territory, meaning the landscape in general. It does not include local elevations like vegetation, buildings, or other human-made structures.

Grp\_Terrain is used as parent for all nodes defining the terrain of an environment. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Terrain](../../_images/Grp_Terrain.svg)

Figure 52. Grp\_Terrain

### 7.3.4.3.4 Grp\_Environment\_Objects

Environment objects include buildings, vegetation, and any other (stationary) objects in the environment. An environment object causes a local elevation or other addition to the terrain.

Grp\_Environment\_Objects is used as parent for all environment objects in an environment. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Environment Objects](../../_images/Grp_Environment_Objects.svg)

Figure 53. Grp\_Environment\_Objects

### 7.3.4.3.5 Grp\_Buildings

A building is a human-made structure and includes houses, towers, or skyscrapers.

Grp\_Buildings is used as parent for all buildings of a Grp\_Environment\_Objects. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Buildings](../../_images/Grp_Buildings.svg)

Figure 54. Grp\_Buildings

### 7.3.4.3.6 Grp\_Vegetation

Vegetation includes all organic growth or plants that are part of the landscape. Vegetation can grow on the terrain or on human-made structures, for example between roads and buildings.

Grp\_Vegetation is used as parent for all vegetation objects of a Grp\_Environment\_Objects. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Vegetation](../../_images/Grp_Vegetation.svg)

Figure 55. Grp\_Vegetation

### 7.3.4.3.7 Grp\_Road\_Network

The road network is the entirety of a road. It includes the drivable area, sidewalks, and any other traffic objects, such as traffic signals, signs, or traffic lights.

Grp\_Road\_Network is used as parent for all nodes defining the road network of an environment. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Road Network](../../_images/Grp_Road_Network.svg)

Figure 56. Grp\_Road\_Network

### 7.3.4.3.8 Grp\_Drivable\_Area

The drivable area is a traffic space that is dedicated to vehicles. It is the surface part of the road structure on which vehicles drive and includes lanes and parking areas. The drivable area for ASAM OpenMATERIAL® 3D is comparable to the scope of the ASAM OpenDRIVE® standard for on-road use cases.

Grp\_Drivable\_Area is used as parent for all nodes defining the drivable area of a road network. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Drivable Area](../../_images/Grp_Drivable_Area.svg)

Figure 57. Grp\_Drivable\_Area

### 7.3.4.3.9 Grp\_Sidewalks

A sidewalk is a traffic space that is dedicated to pedestrians and sometimes cyclists. Sidewalks are usually adjacent to the drivable area.

Grp\_Sidewalks is used as parent for all nodes defining the sidewalks of a road network. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Sidewalks](../../_images/Grp_Sidewalks.svg)

Figure 58. Grp\_Sidewalks

### 7.3.4.3.10 Grp\_Road\_Marks

Road marks include any markings on the road and traffic spaces.

Grp\_Road\_Marks is used as parent for all nodes defining the road marks of a road network. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Road Marks](../../_images/Grp_Road_Marks.svg)

Figure 59. Grp\_Road\_Marks

### 7.3.4.3.11 Grp\_Road\_Objects

Road objects include all other objects on or nearby the road, excluding signals.

Grp\_Road\_Objects is used as parent for all road objects of a road network. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Road Objects](../../_images/Grp_Road_Objects.svg)

Figure 60. Grp\_Road\_Objects

### 7.3.4.3.12 Grp\_Signals

A signal in the context of traffic is a visual sign used to control the flow of traffic. A traffic signal can be both a sign and a light. Signals describe the relevant area or volume of a traffic signal only. Posts and gantries are considered road objects.

Grp\_Signals is used as parent for all signals of a road network. It shares the coordinate system with Grp\_Root, see [Table 102](#tab-Environment-Grp-Root).

![Grp Signals](../../_images/Grp_Signals.svg)

Figure 61. Grp\_Signals

### 7.3.4.3.13 Grp\_Sign\_<signal\_idx> (T)

Traffic signs belong to traffic signals. They are indexed using a `<signal_index>`. The `<signal_index>` can be taken over from ASAM OpenDRIVE® or ASAM OSI. If no predefined indices exist, they can be generated by iterating over all signals from (0,…​,n). The indices are used for both traffic signs and traffic lights. A traffic sign cannot have the same index as a traffic light in a single environment.

![Grp Sign](../../_images/Grp_Sign.svg)

Figure 62. Grp\_Sign\_<signal\_idx>

Table 103. Grp\_Sign


| Grp\_Sign | |
| --- | --- |
| **Origin** | Geometric center of the signs face |
| **x-axis** | Concentric and coaxial to the surface normal of the sign face |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.4.3.14 Grp\_Traffic\_Light\_<signal\_idx> (T)

Traffic lights belong to traffic signals. They show temporary changes in illumination. The `<signal_index>` can be taken over from ASAM OpenDRIVE® or ASAM OSI. If no predefined indices exist, they can be generated by iterating over all signals from (0,…​,n). The indices are used for both traffic signs and traffic lights. A traffic light cannot have the same index as a traffic sign in a single environment.

![Grp Traffic Light](../../_images/Grp_Traffic_Light.svg)

Figure 63. Grp\_Traffic\_Light\_<signal\_idx>

Table 104. Grp\_Traffic\_Light


| Grp\_Traffic\_Light | |
| --- | --- |
| **Origin** | Geometric center of the traffic light signal area surface |
| **x-axis** | Concentric and coaxial to the surface normal of the signal area surface |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

If the index of a traffic light (`<signal_index>`) is aligned with an ASAM OpenDRIVE® map, lighting of individual bulbs can be implemented by corresponding child nodes implementing the ASAM OpenMATERIAL® 3D [lighting concept](../general.html#lighting).
To enable dynamic light state control by ASAM OpenSCENARIO scenarios and ASAM Open Simulation Interface messages, naming of these child nodes should follow the scheme `Grp_Bulb_<bulb_idx> (T)`.
Here, `<bulb_index>` should be counted from left to right (in positive y-direction) and from bottom to top (in positive z-direction) to align with [osi3::TrafficLight](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/latest/gen/structosi3_1_1TrafficLight.html).

Bulb-specific [semantic color](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/latest/gen/structosi3_1_1TrafficLight_1_1Classification.html#ade8af99e440cdd216d8294647d473114) defined by [osi3::TrafficLight::Classification](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/latest/gen/structosi3_1_1TrafficLight_1_1Classification.html) has to be implemented by RGB light `color` in ASAM OpenMATERIAL® 3D:

Table 105. Bulb\_Color


| Bulb Color | |
| --- | --- |
| **COLOR\_RED** | 255,0,0 |
| **COLOR\_YELLOW** | 255,255,0 |
| **COLOR\_GREEN** | 0,255,0 |
| **COLOR\_BLUE** | 0,0,255 |
| **COLOR\_WHITE** | 255,255,255 |

Bulb-specific [icons](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/latest/gen/structosi3_1_1TrafficLight_1_1Classification.html#ac69696ede6d67777aa87b9b290778515) can be implemented by emissive materials and `masking_textures` in ASAM OpenMATERIAL® 3D.
Here, naming of the `masking_textures` should correspond with the naming used in ASAM OpenSimulationInterface, e.g. "ICON\_ARROW\_STRAIGHT\_AHEAD.png".
Instead of masking textures, emissive textures that are already included in the 3D Data File can be used.

For the implementation of ASAM OpenSCENARIO [semantic traffic light states](https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_XML/latest/10_scenario_creation/10_10_traffic_signal.html), child nodes of bulbs can be grouped by parenting group nodes per traffic light, e.g. `Grp_Bulbs_Attention_Stop`/`Grp_Bulbs_Go`/`Grp_Bulbs_Stop`:

Diagram