# ASAM OpenMATERIAL® 3D latest — 7.3.1 Introduction

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/07_geometry/object-classes-introduction.html
> **Standard**: ASAM OpenMATERIAL® 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.3.1 Introduction

In ASAM OpenMATERIAL® 3D, an object class is a collection of similar objects.
Examples of object classes are vehicles, humans, and environment.
Each instance of an object class is described by the same properties but has
individual property values.

The ASAM OpenMATERIAL® 3D standard supports the following object classes:

* Vehicle (see [Section 7.3.2, "Vehicle structure"](object-vehicle/vehicle-index.html))
* Human (see [Section 7.3.3, "Human structure"](object-human/human-index.html))
* Environment (see [Section 7.3.4, "Environment structure"](object-environment/environment-index.html))
* Other (see [Section 7.3.5, "Other structure"](object-other/other-index.html))

If a human is clearly distinguishable from a vehicle, then both the
human and the vehicle are represented by two different objects respectively.
Examples are bicycles, motorbikes, or scooters, where the human and the vehicle are
perceived as separate entities.
Stationary objects, for example, the road network, traffic infrastructure, vegetation, buildings, are part
of the environment object class.

The other object class comprises all objects not yet specified by ASAM OpenMATERIAL® 3D.
It includes all objects that are not specified by type-specific object classes.
Definitions in type-specific object classes overwrite the specifications in the other object class.