# ASAM OpenMATERIAL® 3D latest — 7.3.5 Other structure

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/07_geometry/object-other/other-index.html
> **Standard**: ASAM OpenMATERIAL® 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.3.5 Other structure

## 7.3.5.1 General

The other object class comprises all objects not yet specified by ASAM OpenMATERIAL® 3D.
It includes all objects that are not specified by type-specific object classes.
Definitions in type-specific object classes overwrite the specifications in the other object class.

For objects of class other, only the presence of the Grp\_Root node is mandatory.
All object components shall be children of Grp\_Root.
The associated coordinate system for Grp\_Root should have its origin in the geometric center of the object’s bounding box, projected to the ground.
The x-axis of the coordinate system should point to the front of the object (if applicable), the z-axis of the object should point vertically upwards and the y-axis should point sidewards to complete the right-hand coordinate system.

## 7.3.5.2 Model structure

### 7.3.5.2.1 Structure overview

Diagram

### 7.3.5.2.2 Grp\_Root

This group is the root node of the object.
All components of the object shall be children of this node.
The origin of the node is the center of the object’s bounding box projected to the ground, including all object parts in their default positions.

Table 105. Grp\_Root


| Grp\_Root | |
| --- | --- |
| **Origin** | Center of the object’s bounding box projected to the ground, including all object parts in their default positions |
| **x-axis** | Collinear with the object’s longitudinal axis, pointing forwards |
| **y-axis** | Completes the right-handed coordinate system |
| **z-axis** | Perpendicular to the x-axis, pointing vertically upwards |