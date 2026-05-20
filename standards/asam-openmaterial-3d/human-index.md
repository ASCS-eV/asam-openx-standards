# ASAM Openmaterial 3D latest — 7.3.3 Human structure

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/07_geometry/object-human/human-index.html
> **Standard**: ASAM Openmaterial 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.3.3 Human structure

## 7.3.3.1 General

A human is a bipedal being that can be represented by an object in 3D geometry.

The human 3D geometry is generically structured into the node structure and skeleton (also often called armature) defined in [Section 7.3.3.3, "Model structure"](#_model_structure).
The structure starts with a Root node as a parent group for all other nodes in the structure.

Splitting the object into different parts, such as clothing, hair, and accessories, enables animation and exchange of parts. If a piece of equipment or accessory is specific to a human, rather small, and not self-contained or animated, it can be part of the human asset itself.
For example: Backpacks, sunglasses, and jewelry can be part of the human asset. Bicycles, scooters, and skateboards are separate objects and not part of the human asset.
Not all nodes have to be present in every human *3D model*.
Custom *object parts* may be added to facilitate and better visualize additional use cases, but all custom parts shall adhere to the specified structure principle.

In the coordinate system for human 3D geometry, the x-axis points forwards, the y-axis points sidewards, and the z-axis points upwards.
The default pose is the A-pose.
The naming convention makes it possible to mirror one side of the skeleton to the other.
The bones follow a specific bone orientation: The y-axis of a bone always follows the bone direction, regardless of whether it points sidewards, upwards, or forwards. The x-axis usually faces forwards accordingly.
A bone’s name, position, and orientation is defined by the end-point closer in the hierarchy to the root.
For example, the "Lower\_Arm\_Left" defines the point in the left elbow of the model.

The skeleton starts with a root bone positioned at the origin of the asset, the center of the bounding box projected to the ground.
This position is static and does not change relative to the asset during simulation.
When using an ASAM OpenMATERIAL 3D human asset in combination with ASAM OSI, the OSI field [bbcenter\_to\_root](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/latest/gen/structosi3_1_1MovingObject_1_1PedestrianAttributes.html#a75db7466abca2d283c8d64d424385c0a) must be set to the vector from the center of the bounding box to the center of the ground projection of the bounding box.
This specifically means: x=0, y=0, z=-half of the bounding box height.

[Figure 51](#fig-human-structure) shows the orientation of the coordinate system of a human skeleton.

![fig human structure](../../_images/fig_human-structure.svg)

Figure 51. Human bone structure

Bones with a local transform are indicated in the structure by a (T).
This is only an indicator in the documentation and must not be contained in the actual node name.

## 7.3.3.2 Naming convention

Every bone has a unique name and represents a part of the human body.
The left and right side of the armature are indicated with the keywords "Left" and "Right" as a suffix.
All included meshes use a keyword as a prefix to indicate which kind of object it represents.
They shall be named meaningful.

If needed, the user is free to add more prefixes or bones, which are not part of the standard, for himself.

## 7.3.3.3 Model structure

### 7.3.3.3.1 Structure overview

Diagram

### 7.3.3.3.2 Grp\_Root

This group is used as a parent for all following nodes. It can be used to place the whole asset and select the complete node hierarchy at once. The transformation is set to 0 for all axes.

Table 74. Grp\_Root


| Grp\_Root | |
| --- | --- |
| **Origin** | Center of the bounding box on the ground |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing sidewards |
| **z-axis** | Pointing upwards |

### 7.3.3.3.3 Armature\_<Name>

This object or group represents the armature (skeleton) of the object and contains all bones. It is needed to ensure that the bone hierarchy can be exported and imported correctly.
Depending on the 3D software, the armature is a separate *object type* (for example in Blender) or represented by a group (for example in Maya).
The postfix `_<Name>` is optional, but is recommended to use, if you prepare multiple human assets in one file of an 3D application to keep the names unique and within the naming convention.
The armature shares the coordinate system with Grp\_Root.

### 7.3.3.3.4 Root

The Root bone is the parent bone for all other bones. It can be used to control the whole skeleton. It shares the coordinate system with Grp\_Root, see [Table 74](#tab-human-Grp_Root).

### 7.3.3.3.5 Hip (T)

The Hip bone represents the lowest parts and bones of the spine, that is, the Hip, Coccyx, and Sacrum spine bones of the human skeleton.

Table 75. Hip bone


| Hip | |
| --- | --- |
| **Origin** | At the height of the Coccyx bone and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.6 Lower\_Spine (T)

The Lower\_Spine bone represents the middle parts und bones of the spine, that is, the Lumbar spine bones of the human skeleton.

Table 76. Lower\_Spine bone


| Lower\_Spine | |
| --- | --- |
| **Origin** | At the height of the first Lumbar spine bone and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.7 Upper\_Spine (T)

The Upper\_Spine bone represents the upper parts und bones of the spine, that is, the Thoracic spine bones of the human skeleton.

Table 77. Upper\_Spine bone


| Upper\_Spine | |
| --- | --- |
| **Origin** | At the height of the lowest Thoracic spine bone and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.8 Neck (T)

The Neck bone represents the most upper parts und bones of the spine, that is, the Cervical spine bones of the human skeleton.

Table 78. Neck bone


| Neck | |
| --- | --- |
| **Origin** | At the height of the lowest Cervical spine bone and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.9 Head (T)

The Head bone represents the head, that is, the skull of the human skeleton.

Table 79. Head bone


| Head | |
| --- | --- |
| **Origin** | At the height of the first Cervical spine bone and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.10 Eye\_Left (T)

The Eye\_Left bone represents the left eye of the human body. It is used to calculate the eye level.

Table 80. Eye\_Left bone


| Eye\_Left | |
| --- | --- |
| **Origin** | At the middle of the (eyeball) geometry |
| **x-axis** | Pointing upwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.11 Eye\_Right (T)

The Eye\_Right bone represents the right eye of the human body. It is used to calculate the eye level.

Table 81. Eye\_Right bone


| Eye\_Right | |
| --- | --- |
| **Origin** | At the middle of the (eyeball) geometry |
| **x-axis** | Pointing upwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.12 Shoulder\_Left (T)

The Shoulder\_Left bone represents the upper part of the left shoulder, that is, the interaction between the Clavicle bone and the Humerus head of the human skeleton.

Table 82. Shoulder\_Left bone


| Shoulder\_Left | |
| --- | --- |
| **Origin** | At the height of the Clavicle bone and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.13 Upper\_Arm\_Left (T)

The Upper\_Arm\_Left bone represents the upper part of the left arm, that is, the Humerus head of the human skeleton.

Table 83. Upper\_Arm\_Left bone


| Upper\_Arm\_Left | |
| --- | --- |
| **Origin** | At the height of the Humerus head and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.14 Lower\_Arm\_Left (T)

The Lower\_Arm\_Left bone represents the lower part of the left arm, that is, the left elbow and Radius and Ulna of the human skeleton.

Table 84. Lower\_Arm\_Left bone


| Lower\_Arm\_Left | |
| --- | --- |
| **Origin** | At the height of the elbow and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.15 Hand\_Left (T)

The Hand\_Left bone represents the left hand, that is, the left carpal bones of the human skeleton.

Table 85. Hand\_Left bone


| Hand\_Left | |
| --- | --- |
| **Origin** | At the height of the beginning carpal bones and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.16 Full\_Thumb\_Left (T)

The Full\_Thumb\_Left bone represents the thumb of the left hand, that is, the full thumb of the human skeleton.

Table 86. Full\_Thumb\_Left bone


| Full\_Thumb\_Left | |
| --- | --- |
| **Origin** | At the height of the beginning carpal bones and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.17 Full\_Fingers\_Left (T)

The Full\_Fingers\_Left bone represents all other fingers of the left hand, that is, the full index finger, middle finger, ring finger, and pinkie finger of the human skeleton. The middle finger position and length are used to place the bone correctly.

Table 87. Full\_Fingers\_Left bone


| Full\_Fingers\_Left | |
| --- | --- |
| **Origin** | At the height of the beginning carpal bones and in the middle of the hand geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.18 Shoulder\_Right (T)

The Shoulder\_Right bone represents the upper part of the right shoulder, that is, the interaction between the Clavicle bone and the Humerus head of the human skeleton.

Table 88. Shoulder\_Right bone


| Shoulder\_Right | |
| --- | --- |
| **Origin** | At the height of the Clavicle bone and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.19 Upper\_Arm\_Right (T)

The Upper\_Arm\_Right bone represents the upper part of the right arm, that is, the Humerus head of the human skeleton.

Table 89. Upper\_Arm\_Right bone


| Upper\_Arm\_Right | |
| --- | --- |
| **Origin** | At the height of the Humerus head and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.20 Lower\_Arm\_Right (T)

The Lower\_Arm\_Right bone represents the lower part of the right arm, that is, the right elbow and Radius and Ulna of the human skeleton.

Table 90. Lower\_Arm\_Right bone


| Lower\_Arm\_Right | |
| --- | --- |
| **Origin** | At the height of the elbow and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.21 Hand\_Right (T)

The Hand\_Right bone represents the right hand, that is, the right carpal bones of the human skeleton.

Table 91. Hand\_Right bone


| Hand\_Right | |
| --- | --- |
| **Origin** | At the height of the beginning carpal bones and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.22 Full\_Thumb\_Right (T)

The Full\_Thumb\_Right bone represents the thumb of the right hand, that is, the full thumb of the human skeleton.

Table 92. Full\_Thumb\_Right bone


| Full\_Thumb\_Right | |
| --- | --- |
| **Origin** | At the height of the beginning carpal bones and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.23 Full\_Fingers\_Right (T)

The Full\_Fingers\_Right bone represents all other fingers of the right hand, that is, the full index finger, middle finger, ring finger, and pinkie finger. The middle finger position and length are used to place the bone correctly.

Table 93. Full\_Fingers\_Right bone


| Full\_Fingers\_Right | |
| --- | --- |
| **Origin** | At the height of the beginning carpal bones and in the middle of the hand geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.24 Upper\_Leg\_Left (T)

The Upper\_Leg\_Left bone represents the upper part of the left leg, that is, the thigh of the human skeleton. It controls the hip joint.

Table 94. Upper\_Leg\_Left bone


| Upper\_Leg\_Left (T) | |
| --- | --- |
| **Origin** | At the height of the hip joint and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.25 Lower\_Leg\_Left (T)

The Lower\_Leg\_Left bone represents the lower part of the left leg, that is, the Tibia and Fibula of the human skeleton. It controls the knee.

Table 95. Lower\_Leg\_Left bone


| Lower\_Leg\_Left | |
| --- | --- |
| **Origin** | At the height of the knee and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.26 Foot\_Left (T)

The Foot\_Left bone represents the left foot of the human skeleton without the toes. It controls the ankle.

Table 96. Foot\_Left bone


| Foot\_Left | |
| --- | --- |
| **Origin** | At the height of the ankle and in the middle of the geometry |
| **x-axis** | Pointing upwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.27 Full\_Toes\_Left (T)

The Full\_Toes\_Left bone represents all toes of the left foot of the human skeleton.

Table 97. Full\_Toes\_Left bone


| Full\_Toes\_Left | |
| --- | --- |
| **Origin** | At the height of the phalanges and in the middle of the geometry |
| **x-axis** | Pointing upwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.28 Upper\_Leg\_Right (T)

The Upper\_Leg\_Right bone represents the upper part of the right leg, that is, the thigh of the human skeleton. It controls the hip joint.

Table 98. Upper\_Leg\_Right bone


| Upper\_Leg\_Right | |
| --- | --- |
| **Origin** | At the height of the hip joint and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.29 Lower\_Leg\_Right (T)

The Lower\_Leg\_Right bone represents the lower part of the right leg, that is, the Tibia and Fibula of the human skeleton. It controls the knee.

Table 99. Lower\_Leg\_Right bone


| Lower\_Leg\_Right | |
| --- | --- |
| **Origin** | At the height of the knee and in the middle of the geometry |
| **x-axis** | Pointing forwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.30 Foot\_Right (T)

The Foot\_Right bone represents the right foot of the human skeleton without the toes. It controls the ankle.

Table 100. Foot\_Right bone


| Foot\_Right | |
| --- | --- |
| **Origin** | At the height of the ankle and in the middle of the geometry |
| **x-axis** | Pointing upwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.31 Full\_Toes\_Right (T)

The Full\_Toes\_Right bone in a human skeleton represents all toes of the right foot of the human skeleton.

Table 101. Full\_Toes\_Right bone


| Full\_Toes\_Right | |
| --- | --- |
| **Origin** | At the height of the phalanges and in the middle of the geometry |
| **x-axis** | Pointing upwards |
| **y-axis** | Pointing along the bone direction |
| **z-axis** | Pointing sidewards |

### 7.3.3.3.32 Accessories\_<Name>

This object represents an additional or exchangeable accessory of the human. It shares the coordinate system with Grp\_Root, see [Table 74](#tab-human-Grp_Root).

### 7.3.3.3.33 Body\_<Name>

This object represents the body of the human. It shares the coordinate system with Grp\_Root, see [Table 74](#tab-human-Grp_Root).

### 7.3.3.3.34 Clothing\_<Name>

This object represents an additional or exchangeable clothing part of the human. It shares the coordinate system with Grp\_Root, see [Table 74](#tab-human-Grp_Root).

### 7.3.3.3.35 Hair\_<Name>

This object represents an additional or exchangeable hair part of the human. It shares the coordinate system with Grp\_Root, see [Table 74](#tab-human-Grp_Root).