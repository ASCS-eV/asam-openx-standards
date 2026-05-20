# ASAM Openmaterial 3D latest — 7.3.2 Vehicle structure

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/07_geometry/object-vehicle/vehicle-index.html
> **Standard**: ASAM Openmaterial 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.3.2 Vehicle structure

## 7.3.2.1 General

A vehicle is any machine that moves on land and is either self-propelled or attached to a self-propelled machine.
Trailers or train wagons are considered separate vehicles.
However, permanently attached parts, such as the front and rear of an articulated bus, are considered parts of a single vehicle.
The vehicle class includes all land vehicles, whether wheeled or tracked.
In this version of the standard, only wheeled vehicles are considered.

The vehicle’s 3D geometry is structured according to the node structure defined in [Section 7.3.2.3, "Model structure"](#_model_structure).
The structure begins with a Root node, which is the parent of all other nodes.
The origin of the Root node is the center of the vehicle’s bounding box projected to the ground, including all vehicle parts in their default positions, meaning the vehicle is under neutral load conditions, the wheels are running straight, the doors are closed and the lights are off.
This origin can easily be transformed to coordinate frames from other ASAM standards, such as ASAM OpenSCENARIO XML vehicle coordinates as well as ASAM OSI object coordinates and host vehicle coordinates,
see [Section 7.2.2.2, "Local coordinate system"](../general.html#_local_coordinate_system).

Separating vehicle elements into different groups allows for the movement or animation of parts, such as wheels and doors, positioning external light sources in a simulation, and many other use cases.
Group nodes are empty nodes representing the coordinate origin of the contained geometry.
Meshes should be placed in the corresponding group node.
Not all nodes need to be present in every vehicle *3D model*, as not all vehicles have parts that fit all groups.
Additional group nodes may be added to support additional use cases, but they shall be integrated into the general structure of external or internal and static or dynamic groups and follow the naming convention.

Groups with a local transform are indicated in the structure by a (T).
This is only an indicator in the documentation and must not be contained in the actual node name.

## 7.3.2.2 Naming convention

Every mesh has a unique name and represents a part of the vehicle.
The different vehicle components can be identified by the keywords.
All included meshes use one or more keywords to indicate which kind of object it represents and where it is located:

* Count the axle index from front to rear starting with 0 (according to the [ASAM OSI definition](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/latest/gen/structosi3_1_1MovingObject_1_1VehicleAttributes_1_1WheelData.html#a094de989f5a2aab080f9a65f0feb3867)).
* Count the wheel index per axle from right to left (in positive y-direction and according to the [ASAM OSI definition](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/latest/gen/structosi3_1_1MovingObject_1_1VehicleAttributes_1_1WheelData.html#a094de989f5a2aab080f9a65f0feb3867)).
* Count the door index per side from front to rear and right to left (in positive y-direction).
* Count the seat index per level from first level front to rear, and right to left, to the next level from right to left and front to rear.

Note: A rear bench with 3 seats is considered as 3 seats, because 3 passengers could take a seat on it.

If needed, the user is free to add more groups and new keywords, which are not part of the standard.

## 7.3.2.3 Model structure

### 7.3.2.3.1 Structure overview

Diagram

### 7.3.2.3.2 Grp\_Root

This group is the root node of the entire vehicle.
All components of the vehicle shall be children of this node.
The origin of the Root node is the center of the vehicle’s bounding box projected to the ground, including all vehicle parts in their default positions, meaning the vehicle is under neutral load conditions, the wheels are running straight, the doors are closed, and the lights are off.

Table 17. Grp\_Root


| Grp\_Root | |
| --- | --- |
| **Origin** | Center of the vehicle’s bounding box projected to the ground, including all vehicle parts in their default positions |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.3 Grp\_Exterior

This group contains all parts of the vehicle’s exterior. It shares the coordinate system with Grp\_Root, see [Table 17](#tab-Vehicle-Grp-Root).

### 7.3.2.3.4 Grp\_Exterior\_Dynamic

This group contains all dynamic parts of the vehicle’s exterior. It shares the coordinate system with Grp\_Root, see [Table 17](#tab-Vehicle-Grp-Root).

Dynamic parts are geometric structures whose position and orientation relative to the vehicle’s origin may change throughout a simulation.
They may also change their state during the simulation, which is why lights are considered dynamic.

### 7.3.2.3.5 Grp\_Convertible\_Top

This group contains all parts of a vehicle’s convertible top. It shares the coordinate system with Grp\_Root, see [Table 17](#tab-Vehicle-Grp-Root).

### 7.3.2.3.6 Grp\_Door\_Bottom\_<door\_bottom\_idx> (T)

This group contains all parts of a door located at the bottom of the vehicle, including its interior parts, as they move together as a unit.

`<door_bottom_idx>` denotes the index of doors at the bottom. The index entries
are sorted from front to rear, starting with 0.

![Grp Door Bottom](../../_images/Grp_Door_Bottom.svg)

Figure 6. Grp\_Door\_Bottom\_<door\_bottom\_idx>

Table 18. Grp\_Door\_Bottom\_<door\_bottom\_idx>


| Grp\_Door\_Bottom\_<door\_bottom\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the virtual hinge axis |
| **x-axis** | Perpendicular to the z-axis, pointing along the closed door |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Concentric and coaxial to the virtual hinge axis, pointing in the direction that enables the door to open with a positive rotation around the z-axis |

### 7.3.2.3.7 Grp\_Door\_Front\_<door\_front\_idx> (T)

This group contains all parts of a door located at the front of the vehicle, such as the engine cover. It also includes the door’s interior parts, as they move together as a single unit.

`<door_front_idx>` denotes the index of front doors. The index entries are
sorted from right to left in positive y-direction, starting with 0.

![Grp Door Front](../../_images/Grp_Door_Front.svg)

Figure 7. Grp\_Door\_Front\_<door\_front\_idx>

Table 19. Grp\_Door\_Front\_<door\_front\_idx>


| Grp\_Door\_Front\_<door\_front\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the virtual hinge axis |
| **x-axis** | Perpendicular to the z-axis, pointing along the closed door |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Concentric and coaxial to the virtual hinge axis, pointing in the direction that enables the door to open with a positive rotation around the z-axis |

### 7.3.2.3.8 Grp\_Door\_Left\_<door\_left\_idx> (T)

This group contains all parts of a door located on the left side of the vehicle, including its interior parts, as they move together as a unit.

`<door_left_idx>` denotes the index of doors on the left side. The index entries
are sorted from front to rear, starting with 0.

![Grp Door Left](../../_images/Grp_Door_Left.svg)

Figure 8. Grp\_Door\_Left\_<door\_left\_idx>

Table 20. Grp\_Door\_Left\_<door\_left\_idx>


| Grp\_Door\_Left\_<door\_left\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the virtual hinge axis |
| **x-axis** | Perpendicular to the z-axis, pointing along the closed door |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Concentric and coaxial to the virtual hinge axis, pointing in the direction that enables the door to open with a positive rotation around the z-axis |

### 7.3.2.3.9 Grp\_Door\_Rear\_<door\_rear\_idx> (T)

This group contains all parts of a door located at the rear of the vehicle, such as the trunklid. It also includes the door’s interior parts, as they move together as a single unit.

`<door_rear_idx>` denotes the index of rear doors. The index entries are sorted
from right to left in positive y-direction, starting with 0.

![Grp Door Rear](../../_images/Grp_Door_Rear.svg)

Figure 9. Grp\_Door\_Rear\_<door\_rear\_idx>

Table 21. Grp\_Door\_Rear\_<door\_rear\_idx>


| Grp\_Door\_Rear\_<door\_rear\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the virtual hinge axis |
| **x-axis** | Perpendicular to the z-axis, pointing along the closed door |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Concentric and coaxial to the virtual hinge axis, pointing in the direction that enables the door to open with a positive rotation around the z-axis |

### 7.3.2.3.10 Grp\_Door\_Right\_<door\_right\_idx> (T)

This group contains all parts of a door located on the right side of the vehicle, including its interior parts, as they move together as a unit.

`<door_right_idx>` denotes the index of doors on the right side. The index entries
are sorted from front to rear, starting with 0.

![Grp Door Right](../../_images/Grp_Door_Right.svg)

Figure 10. Grp\_Door\_Right\_<door\_right\_idx>

Table 22. Grp\_Door\_Right\_<door\_right\_idx>


| Grp\_Door\_Right\_<door\_right\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the virtual hinge axis |
| **x-axis** | Perpendicular to the z-axis, pointing along the closed door |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Concentric and coaxial to the virtual hinge axis, pointing in the direction that enables the door to open with a positive rotation around the z-axis |

### 7.3.2.3.11 Grp\_Door\_Top\_<door\_top\_idx> (T)

This group contains all parts of a door located on the top of the vehicle, including its interior parts, as they move together as a unit.

`<door_top_idx>` denotes the index of doors on the top of the vehicle. The index entries
are sorted from front to rear, starting with 0.

![Grp Door Top](../../_images/Grp_Door_Top.svg)

Figure 11. Grp\_Door\_Top\_<door\_top\_idx>

Table 23. Grp\_Door\_Top\_<door\_top\_idx>


| Grp\_Door\_Top\_<door\_top\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the virtual hinge axis |
| **x-axis** | Perpendicular to the z-axis, pointing along the closed door |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Concentric and coaxial to the virtual hinge axis, pointing in the direction that enables the door to open with a positive rotation around the z-axis |

### 7.3.2.3.12 Grp\_Hitch\_Front (T)

This group contains all parts of a hitch at the front of the vehicle. It exists on some cars
and on most trailers.

![Grp Hitch Front](../../_images/Grp_Hitch_Front.svg)

Figure 12. Grp\_Hitch\_Front

Table 24. Grp\_Hitch\_Front


| Grp\_Hitch\_Front | |
| --- | --- |
| **Origin** | Mounting point between the hitch and the vehicle body |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.13 Grp\_Hitch\_Front\_Contact\_Point (T)

This group defines the contact point to attach another vehicle.

During simulation a vehicle’s Grp\_Hitch\_Rear\_Contact\_Point and another
vehicle’s Grp\_Hitch\_Front\_Contact\_Point are placed at the same position.

![Grp Hitch Front Contact Point](../../_images/Grp_Hitch_Front_Contact_Point.svg)

Figure 13. Grp\_Hitch\_Front\_Contact\_Point

Table 25. Grp\_Hitch\_Front\_Contact\_Point


| Grp\_Hitch\_Front\_Contact\_Point | |
| --- | --- |
| **Origin** | Point of contact to the hitch of another vehicle |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.14 Grp\_Hitch\_Rear (T)

This group contains all parts of a hitch on the rear of the vehicle. It exists on cars and
on some trailers for multi-trailer setups.

![Grp Hitch Rear](../../_images/Grp_Hitch_Rear.svg)

Figure 14. Grp\_Hitch\_Rear

Table 26. Grp\_Hitch\_Rear


| Grp\_Hitch\_Rear | |
| --- | --- |
| **Origin** | Mounting point between the hitch and the vehicle body |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.15 Grp\_Hitch\_Rear\_Contact\_Point (T)

This group defines the contact point to attach another vehicle.

During simulation a vehicle’s Grp\_Hitch\_Rear\_Contact\_Point and another
vehicle’s Grp\_Hitch\_Front\_Contact\_Point are placed at the same position.

![Grp Hitch Rear Contact Point](../../_images/Grp_Hitch_Rear_Contact_Point.svg)

Figure 15. Grp\_Hitch\_Rear\_Contact\_Point

Table 27. Grp\_Hitch\_Rear\_Contact\_Point


| Grp\_Hitch\_Rear\_Contact\_Point | |
| --- | --- |
| **Origin** | Point of contact to the hitch of another vehicle |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.16 Grp\_License\_Plate\_<license\_plate\_idx> (T)

This group contains all parts of the vehicle’s license plate.

`<license_plate_idx>` denotes the index of license plates. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

Table 28. Grp\_License\_Plate\_<license\_plate\_idx>


| Grp\_License\_Plate\_<license\_plate\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the plate’s surface |
| **x-axis** | Pointing outwards from the front of the license plate |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.17 Grp\_Light\_Brake\_Center\_<brake\_center\_idx> (T)

This group contains all parts of a brake light located at the center of the vehicle.

`<brake_center_idx>` denotes the index of brake lights in the center. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Brake Center](../../_images/Grp_Light_Brake_Center.svg)

Figure 16. Grp\_Light\_Brake\_Center\_<brake\_center\_idx>

Table 29. Grp\_Light\_Brake\_Center\_<brake\_center\_idx>


| Grp\_Light\_Brake\_Center\_<brake\_center\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.18 Grp\_Light\_Brake\_Left\_<brake\_left\_idx> (T)

This group contains all parts of a brake light located on the left side of the vehicle.

`<brake_left_idx>` denotes the index of brake lights on the left side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Tail Left](../../_images/Grp_Light_Tail_Left.svg)

Figure 17. Grp\_Light\_Brake\_Left\_<brake\_left\_idx>

Table 30. Grp\_Light\_Brake\_Left\_<brake\_left\_idx>


| Grp\_Light\_Brake\_Left\_<brake\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.19 Grp\_Light\_Brake\_Right\_<brake\_right\_idx> (T)

This group contains all parts of a brake light located on the right side of the vehicle.

`<brake_right_idx>` denotes the index of brake lights on the right side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Tail Right](../../_images/Grp_Light_Tail_Right.svg)

Figure 18. Grp\_Light\_Brake\_Right\_<brake\_right\_idx>

Table 31. Grp\_Light\_Brake\_Right\_<brake\_right\_idx>


| Grp\_Light\_Brake\_Right\_<brake\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.20 Grp\_Light\_Corner\_Left\_<corner\_left\_idx> (T)

This group contains all parts of a corner light on the vehicle’s left side.
A corner light is typically a white light that provides side illumination in the direction of a turn or lane change.

`<corner_left_idx>` denotes the index of corner lights on the left side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Day Left](../../_images/Grp_Light_Day_Left.svg)

Figure 19. Grp\_Light\_Corner\_Left\_<corner\_left\_idx>

Table 32. Grp\_Light\_Corner\_Left\_<corner\_left\_idx>


| Grp\_Light\_Corner\_Left\_<corner\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission in neutral position |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.21 Grp\_Light\_Corner\_Right\_<corner\_right\_idx> (T)

This group contains all parts of a corner light on the vehicle’s right side.
A corner light is typically a white light that provides side illumination in the direction of a turn or lane change.

`<corner_right_idx>` denotes the index of corner lights on the right side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Day Right](../../_images/Grp_Light_Day_Right.svg)

Figure 20. Grp\_Light\_Corner\_Right\_<corner\_right\_idx>

Table 33. Grp\_Light\_Corner\_Right\_<corner\_right\_idx>


| Grp\_Light\_Corner\_Right\_<corner\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission in neutral position |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.22 Grp\_Light\_Day\_Left\_<day\_left\_idx> (T)

This group contains all parts of the daytime running light on the vehicle’s left side.

`<day_left_idx>` denotes the index of daytime running lights on the left side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Day Left](../../_images/Grp_Light_Day_Left.svg)

Figure 21. Grp\_Light\_Day\_Left\_<day\_left\_idx>

Table 34. Grp\_Light\_Day\_Left\_<day\_left\_idx>


| Grp\_Light\_Day\_Left\_<day\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.23 Grp\_Light\_Day\_Right\_<day\_right\_idx> (T)

This group contains all parts of the daytime running light on the vehicle’s right side.

`<day_right_idx>` denotes the index of daytime running lights on the right side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Day Right](../../_images/Grp_Light_Day_Right.svg)

Figure 22. Grp\_Light\_Day\_Right\_<day\_right\_idx>

Table 35. Grp\_Light\_Day\_Right\_<day\_right\_idx>


| Grp\_Light\_Day\_Right\_<day\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.24 Grp\_Light\_Fog\_Left\_<fog\_left\_idx> (T)

This group contains all parts of a fog light on the vehicle’s left side.

`<fog_left_idx>` denotes the index of fog lights on the left side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Tail Left](../../_images/Grp_Light_Tail_Left.svg)

Figure 23. Grp\_Light\_Fog\_Left\_<fog\_left\_idx>

Table 36. Grp\_Light\_Fog\_Left\_<fog\_left\_idx>


| Grp\_Light\_Fog\_Left\_<fog\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.25 Grp\_Light\_Fog\_Right\_<fog\_right\_idx> (T)

This group contains all parts of a fog light on the vehicle’s right side.

`<fog_right_idx>` denotes the index of fog lights on the right side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Tail Right](../../_images/Grp_Light_Tail_Right.svg)

Figure 24. Grp\_Light\_Fog\_Right\_<fog\_right\_idx>

Table 37. Grp\_Light\_Fog\_Right\_<fog\_right\_idx>


| Grp\_Light\_Fog\_Right\_<fog\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.26 Grp\_Light\_High\_Beam\_Left\_<high\_beam\_left\_idx> (T)

This group contains all parts of a high beam light on the vehicle’s left side.

`<high_beam_left_idx>` denotes the index of high beam lights on the left side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Day Left](../../_images/Grp_Light_Day_Left.svg)

Figure 25. Grp\_Light\_High\_Beam\_Left\_<high\_beam\_left\_idx>

Table 38. Grp\_Light\_High\_Beam\_Left\_<high\_beam\_left\_idx>


| Grp\_Light\_High\_Beam\_Left\_<high\_beam\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.27 Grp\_Light\_High\_Beam\_Right\_<high\_beam\_right\_idx> (T)

This group contains all parts of a high beam light on the vehicle’s right side.

`<high_beam_right_idx>` denotes the index of high beam lights on the right side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Day Right](../../_images/Grp_Light_Day_Right.svg)

Figure 26. Grp\_Light\_High\_Beam\_Right\_<high\_beam\_right\_idx>

Table 39. Grp\_Light\_High\_Beam\_Right\_<high\_beam\_right\_idx>


| Grp\_Light\_High\_Beam\_Right\_<high\_beam\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.28 Grp\_Light\_Indicator\_Left\_<indicator\_left\_idx> (T)

This group contains all parts of an indicator light on the vehicle’s left side.

`<indicator_left_idx>` denotes the index of indicator lights on the left side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

Table 40. Grp\_Light\_Indicator\_Left\_<indicator\_left\_idx>


| Grp\_Light\_Indicator\_Left\_<indicator\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.29 Grp\_Light\_Indicator\_Right\_<indicator\_right\_idx> (T)

This group contains all parts of an indicator light on the vehicle’s right side.

`<indicator_right_idx>` denotes the index of indicator lights on the right side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

Table 41. Grp\_Light\_Indicator\_Right\_<indicator\_right\_idx>


| Grp\_Light\_Indicator\_Right\_<indicator\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.30 Grp\_Light\_License\_Plate\_<license\_plate\_light\_idx> (T)

This group contains all parts of the vehicle’s license plate light.

`<license_plate_light_idx>` denotes the index of license plate lights. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Light License Plate](../../_images/Grp_Light_License_Plate.svg)

Figure 27. Grp\_Light\_License\_Plate\_<license\_plate\_light\_idx>

Table 42. Grp\_Light\_License\_Plate\_<license\_plate\_light\_idx>


| Grp\_Light\_License\_Plate\_<license\_plate\_light\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.31 Grp\_Light\_Low\_Beam\_Left\_<low\_beam\_left\_idx> (T)

This group contains all parts of a low beam light on the vehicle’s left side.

`<low_beam_left_idx>` denotes the index of low beam lights on the left side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Day Left](../../_images/Grp_Light_Day_Left.svg)

Figure 28. Grp\_Light\_Low\_Beam\_Left\_<low\_beam\_left\_idx>

Table 43. Grp\_Light\_Low\_Beam\_Left\_<low\_beam\_left\_idx>


| Grp\_Light\_Low\_Beam\_Left\_<low\_beam\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.32 Grp\_Light\_Low\_Beam\_Right\_<low\_beam\_right\_idx> (T)

This group contains all parts of a low beam light on the vehicle’s right side.

`<low_beam_right_idx>` denotes the index of low beam lights on the right side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Day Right](../../_images/Grp_Light_Day_Right.svg)

Figure 29. Grp\_Light\_Low\_Beam\_Right\_<low\_beam\_right\_idx>

Table 44. Grp\_Light\_Low\_Beam\_Right\_<low\_beam\_right\_idx>


| Grp\_Light\_Low\_Beam\_Right\_<low\_beam\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.33 Grp\_Light\_Park\_Left\_<park\_left\_idx> (T)

This group contains all parts of a parking light on the vehicle’s left side.

`<park_left_idx>` denotes the index of parking lights on the left side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

Table 45. Grp\_Light\_Park\_Left\_<park\_left\_idx>


| Grp\_Light\_Park\_Left\_<park\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.34 Grp\_Light\_Park\_Right\_<park\_right\_idx> (T)

This group contains all parts of a parking light on the vehicle’s right side.

`<park_right_idx>` denotes the index of parking lights on the right side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

Table 46. Grp\_Light\_Park\_Right\_<park\_right\_idx>


| Grp\_Light\_Park\_Right\_<park\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.35 Grp\_Light\_Position\_Left\_<position\_left\_idx> (T)

This group contains all parts of a position light on the vehicle’s left side.
Position lights are usually small, low-intensity, and orange.

`<position_left_idx>` denotes the index of position lights on the left side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

Table 47. Grp\_Light\_Position\_Left\_<position\_left\_idx>


| Grp\_Light\_Position\_Left\_<position\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.36 Grp\_Light\_Position\_Right\_<position\_right\_idx> (T)

This group contains all parts of a position light on the vehicle’s right side.
Position lights are usually small, low-intensity, and orange.

`<position_right_idx>` denotes the index of position lights on the right side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

Table 48. Grp\_Light\_Position\_Right\_<position\_right\_idx>


| Grp\_Light\_Position\_Right\_<position\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.37 Grp\_Light\_Reverse\_Left\_<reverse\_left\_idx> (T)

This group contains all parts of a reverse light on the vehicle’s left side.

`<reverse_left_idx>` denotes the index of reverse lights on the left side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Tail Left](../../_images/Grp_Light_Tail_Left.svg)

Figure 30. Grp\_Light\_Reverse\_Left\_<reverse\_left\_idx>

Table 49. Grp\_Light\_Reverse\_Left\_<reverse\_left\_idx>


| Grp\_Light\_Reverse\_Left\_<reverse\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.38 Grp\_Light\_Reverse\_Right\_<reverse\_right\_idx> (T)

This group contains all parts of a reverse light on the vehicle’s right side.

`<reverse_right_idx>` denotes the index of reverse lights on the right side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Tail Right](../../_images/Grp_Light_Tail_Right.svg)

Figure 31. Grp\_Light\_Reverse\_Right\_<reverse\_right\_idx>

Table 50. Grp\_Light\_Reverse\_Right\_<reverse\_right\_idx>


| Grp\_Light\_Reverse\_Right\_<reverse\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.39 Grp\_Light\_Tail\_Left\_<tail\_left\_idx> (T)

This group contains all parts of a tail light on the vehicle’s left side.

`<tail_left_idx>` denotes the index of tail lights on the left side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Tail Left](../../_images/Grp_Light_Tail_Left.svg)

Figure 32. Grp\_Light\_Tail\_Left\_<tail\_left\_idx>

Table 51. Grp\_Light\_Tail\_Left\_<tail\_left\_idx>


| Grp\_Light\_Tail\_Left\_<tail\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.40 Grp\_Light\_Tail\_Right\_<tail\_right\_idx> (T)

This group contains all parts of a tail light on the vehicle’s right side.

`<tail_right_idx>` denotes the index of tail lights on the right side. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Light Tail Right](../../_images/Grp_Light_Tail_Right.svg)

Figure 33. Grp\_Light\_Tail\_Right\_<tail\_right\_idx>

Table 52. Grp\_Light\_Tail\_Right\_<tail\_right\_idx>


| Grp\_Light\_Tail\_Right\_<tail\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, usually backwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.41 Grp\_Light\_Warning\_<warning\_idx> (T)

This group contains all parts of the vehicle’s warning light.
Warning lights can include various emergency lights, hazard lights, and more.

`<warning_idx>` denotes the index of warning lights. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Light Warning](../../_images/Grp_Light_Warning.svg)

Figure 34. Grp\_Light\_Warning\_<warning\_idx>

Table 53. Grp\_Light\_Warning\_<warning\_idx>


| Grp\_Light\_Warning\_<warning\_idx> | |
| --- | --- |
| **Origin** | Center of the light element |
| **x-axis** | Pointing towards the main light emission, or forwards for rotating lights |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.42 Grp\_Mirror\_Blindspot\_Mounting\_<blindspot\_mirror\_mounting\_idx> (T)

This group contains all parts of the vehicle’s blindspot mirror mounting.

It is a child node of Grp\_Exterior\_Dynamic if mounted directly to the
vehicle body, or a child node of either Grp\_Door\_Left or Grp\_Door\_Right if
mounted to the door.

`<blindspot_mirror_mounting_idx>` denotes the index of blindspot mirror mountings.
The index entries are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

The index is used consistently, regardless of whether the mirror is mounted to
the door or to the vehicle body.

![Grp Mirror Blindspot Mounting](../../_images/Grp_Mirror_Blindspot_Mounting.svg)

Figure 35. Grp\_Mirror\_Blindspot\_Mounting\_<blindspot\_mirror\_mounting\_idx>

Table 54. Grp\_Mirror\_Blindspot\_Mounting\_<blindspot\_mirror\_mounting\_idx>


| Grp\_Mirror\_Blindspot\_Mounting\_<blindspot\_mirror\_mounting\_idx> | |
| --- | --- |
| **Origin** | Base of the mirror mounting |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.43 Grp\_Mirror\_Blindspot\_Joint\_<blindspot\_mirror\_joint\_idx> (T)

This group contains all parts of the movable structure that holds the blindspot mirror.
The blindspot mirror view automatically adjusts when the angle of the blindspot joint changes.

It is a child node of the corresponding mirror mounting group.

`<blindspot_mirror_joint_idx>` denotes the index of blindspot mirror joints. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Mirror Blindspot Joint](../../_images/Grp_Mirror_Blindspot_Joint.svg)

Figure 36. Grp\_Mirror\_Blindspot\_Joint\_<blindspot\_mirror\_joint\_idx>

Table 55. Grp\_Mirror\_Blindspot\_Joint\_<blindspot\_mirror\_joint\_idx>


| Grp\_Mirror\_Blindspot\_Joint\_<blindspot\_mirror\_joint\_idx> | |
| --- | --- |
| **Origin** | Joint of the movable structure of a mirror |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.44 Grp\_Mirror\_Blindspot\_View\_<blindspot\_mirror\_view\_idx> (T)

This group is an empty node that represents the view direction of the mirror
glass on a blindspot mirror.

It is a child node of the corresponding mirror joint group.

`<blindspot_mirror_view_idx>` denotes the index of blindspot mirrors. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Mirror Blindspot View](../../_images/Grp_Mirror_Blindspot_View.svg)

Figure 37. Grp\_Mirror\_Blindspot\_View\_<blindspot\_mirror\_view\_idx>

Table 56. Grp\_Mirror\_Blindspot\_View\_<blindspot\_mirror\_view\_idx>


| Grp\_Mirror\_Blindspot\_View\_<blindspot\_mirror\_view\_idx> | |
| --- | --- |
| **Origin** | Center of the mirror glass surface |
| **x-axis** | Pointing outwards from the mirror glass, aligned with the surface normal |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards along the face of the mirror glass |

### 7.3.2.3.45 Grp\_Mirror\_Side\_Mounting\_Left\_<side\_mirror\_mounting\_left\_idx> (T)

This group contains all parts of the side mirror on the vehicle’s left side.

It is a child node of Grp\_Exterior\_Dynamic if mounted directly to the
vehicle body, or a child node of either Grp\_Door\_Left or Grp\_Door\_Right if
mounted to the door.

`<side_mirror_mounting_left_idx>` denotes the index of side mirrors on the left side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

The index is used consistently, regardless of whether the mirror is mounted to
the door or to the vehicle body.

![Grp Mirror Side Mounting Left](../../_images/Grp_Mirror_Side_Mounting_Left.svg)

Figure 38. Grp\_Mirror\_Side\_Mounting\_Left\_<side\_mirror\_mounting\_left\_idx>

Table 57. Grp\_Mirror\_Side\_Mounting\_Left\_<side\_mirror\_mounting\_left\_idx>


| Grp\_Mirror\_Side\_Mounting\_Left\_<side\_mirror\_mounting\_left\_idx> | |
| --- | --- |
| **Origin** | Base of the mirror mounting |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.46 Grp\_Mirror\_Side\_Joint\_Left\_<side\_mirror\_joint\_left\_idx> (T)

This group contains all parts of the movable structure that holds the mirror on the vehicle’s left side.
The mirror view automatically adjusts when the angle of the joint changes.

It is a child node of the corresponding mirror mounting group.

`<side_mirror_joint_left_idx>` denotes the index of side mirror joints on the
left side. The index entries are sorted from right to left in positive
y-direction, and from front to rear, starting with 0.

![Grp Mirror Side Joint Left](../../_images/Grp_Mirror_Side_Joint_Left.svg)

Figure 39. Grp\_Mirror\_Side\_Joint\_Left\_<side\_mirror\_joint\_left\_idx>

Table 58. Grp\_Mirror\_Side\_Joint\_Left\_<side\_mirror\_joint\_left\_idx>


| Grp\_Mirror\_Side\_Joint\_Left\_<side\_mirror\_joint\_left\_idx> | |
| --- | --- |
| **Origin** | Joint of the movable structure of a mirror |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.47 Grp\_Mirror\_Side\_View\_Left\_<side\_mirror\_view\_left\_idx> (T)

This group is an empty node that represents the view direction of the mirror
glass on a side mirror on the left side of the vehicle.

It is a child node of the corresponding mirror joint group.

`<side_mirror_view_left_idx>` denotes the index of mirror glasses on the left side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Mirror Side View Left](../../_images/Grp_Mirror_Side_View_Left.svg)

Figure 40. Grp\_Mirror\_Side\_View\_Left\_<side\_mirror\_view\_left\_idx>

Table 59. Grp\_Mirror\_Side\_View\_Left\_<side\_mirror\_view\_left\_idx>


| Grp\_Mirror\_Side\_View\_Left\_<side\_mirror\_view\_left\_idx> | |
| --- | --- |
| **Origin** | Center of the mirror glass surface |
| **x-axis** | Pointing outwards from the mirror glass, aligned with the surface normal |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards along the face of the mirror glass |

### 7.3.2.3.48 Grp\_Mirror\_Side\_Mounting\_Right\_<side\_mirror\_mounting\_right\_idx> (T)

This group contains all parts of the side mirror on the vehicle’s right side.

It is a child node of Grp\_Exterior\_Dynamic if mounted directly to the
vehicle body, or a child node of either Grp\_Door\_Left or Grp\_Door\_Right if mounted
to the door.

`<side_mirror_mounting_right_idx>` denotes the index of side mirrors on the
right side. The index entries are sorted from right to left in positive
y-direction, and from front to rear, starting with 0.

The index is used consistently, regardless of whether the mirror is mounted to
the door or to the vehicle body.

![Grp Mirror Side Mounting Right](../../_images/Grp_Mirror_Side_Mounting_Right.svg)

Figure 41. Grp\_Mirror\_Side\_Mounting\_Right\_<side\_mirror\_mounting\_right\_idx>

Table 60. Grp\_Mirror\_Side\_Mounting\_Right\_<side\_mirror\_mounting\_right\_idx>


| Grp\_Mirror\_Side\_Mounting\_Right\_<side\_mirror\_mounting\_right\_idx> | |
| --- | --- |
| **Origin** | Base of the mirror mounting |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.49 Grp\_Mirror\_Side\_Joint\_Right\_<side\_mirror\_joint\_right\_idx> (T)

This group contains all parts of the movable structure that holds the mirror on the vehicle’s left side.
The mirror view automatically adjusts when the angle of the joint changes.

It is a child node of the corresponding mirror mounting group.

`<side_mirror_joint_right_idx>` denotes the index of side mirror joints on the
right side. The index entries are sorted from right to left in positive
y-direction, and from front to rear, starting with 0.

![Grp Mirror Side Joint Right](../../_images/Grp_Mirror_Side_Joint_Right.svg)

Figure 42. Grp\_Mirror\_Side\_Joint\_Right\_<side\_mirror\_joint\_right\_idx>

Table 61. Grp\_Mirror\_Side\_Joint\_Right\_<side\_mirror\_joint\_right\_idx>


| Grp\_Mirror\_Side\_Joint\_Right\_<side\_mirror\_joint\_right\_idx> | |
| --- | --- |
| **Origin** | Joint of the movable structure of a mirror |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.50 Grp\_Mirror\_Side\_View\_Right\_<side\_mirror\_view\_right\_idx> (T)

This group is an empty node that represents the view direction of the mirror
glass on a side mirror on the right side of the vehicle.

It is a child node of the corresponding mirror joint group.

`<side_mirror_view_right_idx>` denotes the index of mirror glasses on the right side. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Mirror Side View Right](../../_images/Grp_Mirror_Side_View_Right.svg)

Figure 43. Grp\_Mirror\_Side\_View\_Right\_<side\_mirror\_view\_right\_idx>

Table 62. Grp\_Mirror\_Side\_View\_Right\_<side\_mirror\_view\_right\_idx>


| Grp\_Mirror\_Side\_View\_Right\_<side\_mirror\_view\_right\_idx> | |
| --- | --- |
| **Origin** | Center of the mirror glass surface |
| **x-axis** | Pointing outwards from the mirror glass, aligned with the surface normal |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards along the face of the mirror glass |

### 7.3.2.3.51 Grp\_Rear\_Axle\_Center (T)

This group is an empty node in the center of the rear axle.

The coordinate origin of this group is aligned with the ASAM OSI host vehicle coordinate system and may be used as the reference frame for perception sensor data.

Table 63. Grp\_Rear\_Axle\_Center


| Grp\_Rear\_Axle\_Center | |
| --- | --- |
| **Origin** | Center of the rear axle of the vehicle |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.52 Grp\_Wheel\_<axle\_idx>\_<wheel\_idx> (T)

This group contains all parts of a wheel, which may consist of the tire, rim, brake caliper, and so on.

The groups' transform shall only be used to implement translational movement of the wheel.
Rotational movement of the wheel shall be applied simultaneously to the transforms of both groups'
child nodes, Grp\_Wheel\_Steering and Grp\_Wheel\_Steering\_Rotating, whereby the wheels' rolling movement
shall only be taken into account for the latter (see following sections for details).

Suspension deflection is represented by translation along the z-axis.
Zero translation around all axles is defined under neutral load conditions.

`<axle_idx>` denotes the index of the axle to which the wheel is mounted,
counting from front to rear, starting with 0.

`<wheel_idx>` denotes the index of the wheel on the specified axle, counting from right to left in positive y-direction, starting with 0.
For example, the wheel on the front left of a standard vehicle would be labeled 'Grp\_Wheel\_0\_1'.

![Grp Wheel](../../_images/Grp_Wheel.svg)

Figure 44. Grp\_Wheel\_<axle\_idx>\_<wheel\_idx>

Table 64. Grp\_Wheel\_<axle\_idx>\_<wheel\_idx>


| Grp\_Wheel\_<axle\_idx>\_<wheel\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the wheel |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.53 Grp\_Wheel\_Steering\_<axle\_idx>\_<wheel\_idx> (T)

This group contains all parts of a wheel that follow the steering motion but not the wheels' rolling movement, such as brake calipers.
Therefore, rotational movement due to wheel steering and wheel camber shall be applied to this group.

Wheel steering is represented by rotation around the z-axis.
Wheel camber is defined by a rotation around the x-axis.
Zero rotation around all axles is defined under neutral load conditions.

The indices are the same as in the parent group Grp\_Wheel.

Table 65. Grp\_Wheel\_Steering\_<axle\_idx>\_<wheel\_idx>


| Grp\_Wheel\_Steering\_<axle\_idx>\_<wheel\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the wheel |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.54 Grp\_Wheel\_Steering\_Rotating\_<axle\_idx>\_<wheel\_idx> (T)

This group contains all parts of a wheel that follow the steering motion as well as the rolling movement of the wheel, such as tire and rim.
Therefore, rotational movement due to wheel steering, wheel camber and the wheel rolling movement shall be applied to this group.

Wheel steering is represented by rotation around the z-axis.
Wheel camber is defined by a rotation around the x-axis.
The wheels' rolling movement is defined by a rotation around the y-axis.
Zero rotation around all axles is defined under neutral load conditions.

The indices are the same as in the parent group Grp\_Wheel.

Table 66. Grp\_Wheel\_Steering\_Rotating\_<axle\_idx>\_<wheel\_idx>


| Grp\_Wheel\_Steering\_Rotating\_<axle\_idx>\_<wheel\_idx> | |
| --- | --- |
| **Origin** | Geometric center of the wheel |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.55 Grp\_Exterior\_Static

This group contains all static parts of the vehicle’s exterior. It shares the coordinate system with Grp\_Root, see [Table 17](#tab-Vehicle-Grp-Root).
Static elements are geometric structures that have a fixed position and
orientation relative to the vehicle’s origin throughout the simulation.

In contrast to lights, which change their state depending on whether they are
switched on or off, static elements never change state during the simulation.

### 7.3.2.3.56 Grp\_Interior

This group contains all parts of the vehicle’s interior. It shares the coordinate system with Grp\_Root, see [Table 17](#tab-Vehicle-Grp-Root).
The interior is separated from the exterior to allow for disabling or exchanging it in the simulation.

### 7.3.2.3.57 Grp\_Interior\_Dynamic

This group contains all dynamic parts of the vehicle’s interior. It shares the coordinate system with Grp\_Root, see [Table 17](#tab-Vehicle-Grp-Root).
Dynamic elements are geometric structures whose position and orientation relative to the vehicle’s origin may change throughout the simulation.

They may also change their state during the simulation. Examples of dynamic elements are lights, which can be switched on and off.

### 7.3.2.3.58 Grp\_Eyepoint\_<eyepoint\_idx> (T)

This group is an empty node that represents the view direction of an average passenger in the vehicle.

`<eyepoint_idx>` denotes the index of eye points. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Eyepoint](../../_images/Grp_Eyepoint.svg)

Figure 45. Grp\_Eyepoint\_<eyepoint\_idx>

Table 67. Grp\_Eyepoint\_<eyepoint\_idx>


| Grp\_Eyepoint\_<eyepoint\_idx> | |
| --- | --- |
| **Origin** | Center of the eye view point |
| **x-axis** | Collinear with the view direction |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards in neutral position |

### 7.3.2.3.59 Grp\_Mirror\_Rearview\_Mounting\_<rearview\_mirror\_mounting\_idx> (T)

This group contains all parts of a vehicle’s rearview mirror mounting.

`<rearview_mirror_mounting_idx>` denotes the index of rearview mirror mountings. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

The index is used consistently, regardless of whether the mirror is mounted to
the door or to the vehicle body.

![Grp Mirror Rearview Mounting](../../_images/Grp_Mirror_Rearview_Mounting.svg)

Figure 46. Grp\_Mirror\_Rearview\_Mounting\_<rearview\_mirror\_mounting\_idx>

Table 68. Grp\_Mirror\_Rearview\_Mounting\_<rearview\_mirror\_mounting\_idx>


| Grp\_Mirror\_Rearview\_Mounting\_<rearview\_mirror\_mounting\_idx> | |
| --- | --- |
| **Origin** | Base of the mirror mounting |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.60 Grp\_Mirror\_Rearview\_Joint\_<rearview\_mirror\_joint\_idx> (T)

This group contains all parts of the movable structure that holds the rearview
mirror. The mirror view automatically adjusts when the angle of the joint changes.

`<rearview_mirror_joint_idx>` denotes the index of rearview mirror joints. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Mirror Rearview Joint](../../_images/Grp_Mirror_Rearview_Joint.svg)

Figure 47. Grp\_Mirror\_Rearview\_Joint\_<rearview\_mirror\_joint\_idx>

Table 69. Grp\_Mirror\_Rearview\_Joint\_<rearview\_mirror\_joint\_idx>


| Grp\_Mirror\_Rearview\_Joint\_<rearview\_mirror\_joint\_idx> | |
| --- | --- |
| **Origin** | Joint of the movable structure of a mirror |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.61 Grp\_Mirror\_Rearview\_View\_<rearview\_mirror\_view\_idx> (T)

This group is an empty node that represents the view direction of the mirror
glass on a rearview mirror.

It is a child node of the corresponding mirror joint group.

`<rearview_mirror_view_idx>` denotes the index of rearview mirrors. The index entries
are sorted from right to left in positive y-direction, and from front to rear, starting with 0.

![Grp Mirror Rearview View](../../_images/Grp_Mirror_Rearview_View.svg)

Figure 48. Grp\_Mirror\_Rearview\_View\_<rearview\_mirror\_view\_idx>

Table 70. Grp\_Mirror\_Rearview\_View\_<rearview\_mirror\_view\_idx>


| Grp\_Mirror\_Rearview\_View\_<rearview\_mirror\_view\_idx> | |
| --- | --- |
| **Origin** | Center of the mirror glass surface |
| **x-axis** | Pointing outwards from the mirror glass, aligned with the surface normal |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards along the face of the mirror glass |

### 7.3.2.3.62 Grp\_Seat\_<seat\_row>\_<seat\_idx> (T)

This group contains all parts of the vehicle’s seats.

The seat position can be used to place a human *3D model* as a passenger.
Therefore, a bench consists of multiple individual seats.

`<seat_row_idx>` denotes a row of seats, counted from the front to the rear, starting with 0.
`<seat_idx>` denotes the index of a seat per row. The index entries
are sorted from right to left in positive y-direction, starting with 0.

![Grp Seat](../../_images/Grp_Seat.svg)

Figure 49. Grp\_Seat\_<seat\_row>\_<seat\_idx>

Table 71. Grp\_Seat\_<seat\_row>\_<seat\_idx>


| Grp\_Seat\_<seat\_row>\_<seat\_idx> | |
| --- | --- |
| **Origin** | Center of the seat cushion |
| **x-axis** | Collinear with the vehicle’s longitudinal axis, pointing in the direction of the seat |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |

### 7.3.2.3.63 Grp\_Steering\_Wheel (T)

This group contains all elements of the vehicle’s steering wheel.

![Grp Steering Wheel](../../_images/Grp_Steering_Wheel.svg)

Figure 50. Grp\_Steering\_Wheel

Table 72. Grp\_Steering\_Wheel


| Grp\_Steering\_Wheel | |
| --- | --- |
| **Origin** | Center of the steering wheel |
| **x-axis** | Collinear with the steering column, pointing towards the axis |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards in neutral position |

### 7.3.2.3.64 Grp\_Interior\_Static

This group contains all static parts of the vehicle’s interior. It shares the coordinate system with Grp\_Root, see [Table 17](#tab-Vehicle-Grp-Root).
Static elements are geometric structures that have a fixed position and orientation relative to the vehicle’s origin throughout the simulation.

In contrast to lights, which change their state depending on whether they are
switched on or off, static elements never change state during the simulation.

### 7.3.2.3.65 Grp\_Vehicle\_Part (T)

One or more optional vehicle parts may be added to the main vehicle structure. This group contains all (sub-)parts of the vehicle part.

A vehicle part is a large component of a vehicle that can move in a
different direction than the rest of the vehicle, for example, the vehicle part follows an
individual path during turns.

A vehicle may have multiple vehicle parts at the same hierarchy level or in a parent-child relationship.
This typically applies to articulated vehicles, such as a front loader with a hinged axis or an articulated bus with a hinge in the middle, and may also apply to construction vehicles.
When a vehicle part can be detached, like a trailer, it is treated as a separate object, not as a vehicle part.

The child nodes of a vehicle part may follow the same structure as the main vehicle. For example, if a vehicle part has lights, they may use the same structure and naming conventions as those on the main vehicle.

Standard passenger vehicles do not have separate parts.

Table 73. Grp\_Vehicle\_Part


| Grp\_Vehicle\_Part | |
| --- | --- |
| **Origin** | Center of the joint to the main vehicle or the parent. |
| **x-axis** | Collinear with the part’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |