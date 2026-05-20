# ASAM Openmaterial 3D latest — 6 Use cases

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/06_use_cases/use-cases.html
> **Standard**: ASAM Openmaterial 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 6 Use cases

This section provides a comprehensive list of use cases.
These use cases are structured to demonstrate how various aspects of ASAM OpenMATERIAL 3D are applied.
They include the impact of technologies like 3D modeling tools and 3D engines, as well as specific *3D model* formats such as glTF and FBX.
This clear organization helps users understand the practical applications of ASAM OpenMATERIAL 3D and how it integrates into their workflows.

Table 5. Use case 1: Creating *3D assets*


|  |  |
| --- | --- |
| **Description** | As a content creator, I want to create *3D assets* for perception sensor simulation in a standardized format. The assets shall be linked to *material properties*. |
| **Relevant OpenMATERIAL 3D segments** | Geometry and Material |
| **Influencing standards** | OGC CDB [[9](../bibliography.html#bib-ogc)] |
| **Influencing technologies** | 3D Modeling (for example, 3dsMax and Maya), 3D Engine (for example, Unreal Engine) |
| **Relevant user** | Content creator |

Table 6. Use case 2: Creating material data


|  |  |
| --- | --- |
| **Description** | As a measurement engineer, I want to create material data for use in *3D asset* creation. The data shall consist of *physical or measured properties* of materials that can be assigned to 3D meshes. |
| **Relevant OpenMATERIAL 3D segments** | Material |
| **Influencing standards** | - |
| **Influencing technologies** | - |
| **Relevant user** | Measurement engineer |

Table 7. Use case 3: Validating *material properties* and 3D geometries


|  |  |
| --- | --- |
| **Description** | As a measurement engineer, I want to validate 3D geometries and *material properties*. This *validation* is performed as a comparison of the data, that is, *material properties* and defined points in the 3D geometry, against measurements from the real world. |
| **Relevant OpenMATERIAL 3D segments** | Geometry and Material |
| **Influencing standards** | - |
| **Influencing technologies** | - |
| **Relevant user** | Measurement engineer, regulator |

Table 8. Use case 4: Distributing and reusing material data and *3D assets*


|  |  |
| --- | --- |
| **Description** | As a content creation company, we want to distribute material data and *3D assets* under copyright and license considerations. To distribute material data and *3D assets* efficiently, it shall be possible to reuse the data and assets in different *simulation platforms* and sensor models with varying sensor technologies, for example, wavelengths. |
| **Relevant OpenMATERIAL 3D segments** | Geometry and Material |
| **Influencing standards** | - |
| **Influencing technologies** | - |
| **Relevant user** | Content creator |

Table 9. Use case 5: Importing *3D assets* linked to *material properties* into shared sensor simulation models (FMU)


|  |  |
| --- | --- |
| **Description** | As a sensor model developer, I want to import *3D assets* that are packaged as FMUs into sensor models. |
| **Relevant OpenMATERIAL 3D segments** | Geometry and Material |
| **Influencing standards** | FMI [[6](../bibliography.html#bib-fmi)], ASAM OSI (OSMP) [[5](../bibliography.html#bib-osi)], ASAM OpenLABEL [[3](../bibliography.html#bib-ola)], ASAM OpenDRIVE [[4](../bibliography.html#bib-odr)], ASAM OpenSCENARIO [[2](../bibliography.html#bib-osc)] |
| **Influencing technologies** | Unreal Engine, Unity, OptiX, CUDA |
| **Relevant user** | Sensor model developer |

Table 10. Use case 6: Importing *3D assets* linked to *material properties* into *simulation platform*


|  |  |
| --- | --- |
| **Description** | As a *simulation platform* developer, I want to import *3D assets* into a *simulation platform*. |
| **Relevant OpenMATERIAL 3D segments** | Geometry and Material |
| **Influencing standards** | - |
| **Influencing technologies** | Unreal Engine, Unity, Unigine, OptiX, CUDA |
| **Relevant user** | Simulation platform developer |

Table 11. Use case 7: Retrofitting or changing *material properties* independent of *3D assets*


|  |  |
| --- | --- |
| **Description** | As a simulation platform developer, I want to be able to add or change *material properties* independently of *3D assets* geometries in a *simulation platform*. |
| **Relevant OpenMATERIAL 3D segments** | Material |
| **Influencing standards** | ASAM OpenLABEL [[3](../bibliography.html#bib-ola)] |
| **Influencing technologies** | Unreal Engine, Unity, OptiX, CUDA |
| **Relevant user** | Simulation platform developer |

Table 12. Use case 8: Moving *object parts* in the environment simulation


|  |  |
| --- | --- |
| **Description** | As a *simulation platform* or sensor model developer, I want to move *objects* as well as individual parts of the *objects* during simulation runtime. These can be parts of a vehicle, for example, wheels and doors or the skeleton bones of a pedestrian. One option to manipulate the imported *3D assets* during simulation runtime is using ASAM OSI. In the [osi3::GroundTruth](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/V3.6.0/gen/structosi3_1_1GroundTruth.html) message, information about moving and stationary *objects* is provided from the *scenario* engine to the sensor model. This entails *object* positions, orientations, speeds and so on for every simulation time step, but also a so-called model reference. This reference is the path to a *3D asset* associated with the *object* or the stationary environment. Using the pose information together with the 3D mesh data, a *3D environment* is constructed and updated for every simulation time step. Further attributes, such as [wheel positions](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/V3.6.0/gen/structosi3_1_1MovingObject_1_1VehicleAttributes_1_1WheelData.html) for vehicles or [bone poses](https://opensimulationinterface.github.io/osi-antora-generator/asamosi/V3.6.0/gen/structosi3_1_1MovingObject_1_1PedestrianAttributes_1_1Bone.html) for pedestrians, enable a more refined movement of traffic participants in the *3D environment*. |
| **Relevant OpenMATERIAL 3D segments** | Geometry |
| **Influencing standards** | ASAM OSI [[5](../bibliography.html#bib-osi)] |
| **Influencing technologies** | - |
| **Relevant user** | Simulation platform developer |

Table 13. Use case 9: Simulating energy or *signal propagation* with *3D assets* linked to *material properties*


|  |  |
| --- | --- |
| **Description** | As a *simulation platform* or sensor model developer, I want to simulate the energy or *signal propagation* using imported *3D assets* with linked *material properties*. This is, for example, done with ray tracing. Rays are launched in a virtual 3D scene to simulate the propagation of light beams, radio waves, or ultrasonic waves. The interaction of the rays with the surfaces of the *objects* in the *3D environment* depends on the *material properties* of these surfaces. These properties are assigned to the 3D geometries of the *objects* and imported from a material database. The simulation shall be able to cope with different real-time requirements, for example, SiL, HiL, open-loop, closed-loop. |
| **Relevant OpenMATERIAL 3D segments** | Geometry and Material |
| **Influencing standards** | - |
| **Influencing technologies** | Nvidia OptiX |
| **Relevant user** | Simulation platform developer, sensor model developer, end user |

Table 14. Use case 10: Using sensor simulation to train perception algorithms


|  |  |
| --- | --- |
| **Description** | As a perception algorithm developer, I want to use simulated environments for model training and testing, as real-world information collection is too expensive and inconvenient. |
| **Relevant OpenMATERIAL 3D segments** | Geometry and Material |
| **Influencing standards** | ASAM OSI [[5](../bibliography.html#bib-osi)], ASAM OpenSCENARIO [[2](../bibliography.html#bib-osc)], ASAM OpenDRIVE [[4](../bibliography.html#bib-odr)] |
| **Influencing technologies** | Unity, OptiX, Regeneration AI |
| **Relevant user** | End user |