# ASAM OpenMATERIAL® 3D latest — 5 Terms and definitions

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/05_terms_and_definitions/terms-and-definitions.html
> **Standard**: ASAM OpenMATERIAL® 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 5 Terms and definitions

3D asset
:   The combination of an object’s 3D geometry, assigned material properties, and
    specific metadata.

3D data file
:   A standard 3D model file in glTF, FBX, or USD format.

3D environment
:   A 3D representation of a simulated sensor’s surroundings. It can consist of
    multiple 3D assets.

3D model
:   A mathematical coordinate-based representation of an object’s geometrical
    surface. Material properties used for rendering purposes can be part of the 3D model. This excludes physical material properties. For a combination of 3D
    geometry and physical material properties, see 3D asset.

Co-simulation
:   Simulation of multiple independent models connected with interfaces. A
    co-simulation platform handles the timing, synchronization, and data transfer between the
    individual models.

Electromagnetic property
:   Denotes a characteristic of an object or material when interacting with electric and magnetic fields.  
    **Examples**: conduction, magnetization, polarization.

Ground truth
:   Defines true static and dynamic states of objects. The true states are either
    determined by the content creator or defined by an omniscient observer, for
    example, a simulation platform.

Machine perception
:   The ability of systems to interpret sensory data and to reliably detect objects
    and other road users relevant to the operation of automated driving. The data is
    used to generate situational awareness of the vehicle environment [[10](../bibliography.html#bib-die)].

Material
:   A collection of material properties belonging to one entity.

Material assignment
:   A mapping of material IDs to meshes of 3D models, or pixels of textures mapped to these meshes. The material ID is a unique
    pointer to a set of material properties in separate material files.

Material classification
:   Standardized classification scheme that sorts materials into classes and groups
    of classes, for example, based on their physical properties.

Material parameter file
:   A file in JSON format containing defined material properties according to the
    ASAM OpenMATERIAL® 3D standard.

Material property
:   Denotes a physical, chemical, or geometric property of a material.

Multispectral or hyperspectral material
:   Material with wavelength-specific properties that are defined for multiple spectra.  
    Multispectral material shows up in imagery as 3-10 wider bands.  
    Hyperspectral material shows hundreds of narrow bands.

Object
:   A tangible thing with defined 3D boundaries and discrete meshes. An object ID can be assigned.
    In the JSON schemas, the term *object* also refers to the JSON data type.
    This is not to be confused with a 3D object, but it is clearly marked as type: `object` in the schemas.

Object part
:   A segment of an object that has distinct characteristics, for example, material,
    shape, or function.  
    **Example**: A car door differs from the rest of the vehicle due to its function
    to open and close.

Object type
:   Class of objects with the same set of properties. Each instance of the class is
    described by the same properties, but has individual property values.

Physical property
:   Denotes a characteristic of an object or material that can be measured.  
    **Examples**: permittivity, density, index of refraction.

Post rendering effect
:   Visual modification applied to graphics after initial rendering, enhancing
    appearance or realism without impairing performance.

Scenario
:   A description of the behavior or temporal evolution of physical objects and
    environmental conditions on the driving infrastructure over an interval of time,
    including the movement of traffic participants or the change of environmental
    conditions [[2](../bibliography.html#bib-osc)].

Signal energy propagation
:   The act of a signal traveling through the environment and potentially
    interacting with objects and particles [[11](../bibliography.html#bib-lin)].

Simulation platform
:   Application that orchestrates and runs the simulations. It can be either an
    all-in-one solution including the generation of the 3D environment or a
    co-simulation platform orchestrating a co-simulation of multiple sensor models, vehicle dynamics models, and so on.

Surface normal
:   A vector that is perpendicular to a given object, surface, or geometrical
    primitive. It can be used to determine the face direction for 2D and
    3D rendering.

Validation
:   A method for evaluating a simulation model’s performance and accuracy by
    comparing simulated data to measured data and quantifying the differences.

Vertex normal
:   A directional vector that is associated with a vertex. It represents the
    normalized average of the surrounding surface normals.