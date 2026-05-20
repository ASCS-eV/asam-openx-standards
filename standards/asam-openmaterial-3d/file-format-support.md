# ASAM OpenMATERIAL® 3D latest — 7.4 File format

> **Source**: https://asam-ev.github.io/OpenMATERIAL-3D/asamopenmaterial/latest/specification/07_geometry/file-format-support.html
> **Standard**: ASAM OpenMATERIAL® 3D latest, 2025-01-01
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.4 File format

ASAM OpenMATERIAL® 3D does not define its own *3D model* format.
However, the geometry specification defines coordinate systems, units, node hierarchies, and more, which can be applied across different *3D model* formats.

ASAM OpenMATERIAL® 3D supports the *3D model* file formats glTF, FBX, and USD with the following considerations:

glTF
:   *3D models* of ASAM OpenMATERIAL® 3D in glTF format shall comply with the official [glTF specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html).
    The glTF specification has two delivery options: glTF + bin + textures, and the container format glb.
    Both delivery options are supported in ASAM OpenMATERIAL® 3D.

    The glTF coordinate system is right-handed, with +Y as the up axis, +Z as forward, and -X as right. The front of a glTF asset faces +Z.

    This setup differs from how coordinate systems are defined in ASAM OpenMATERIAL® 3D, see [Section 7.2.2, "Coordinate systems"](general.html#_coordinate_systems).
    While modeling, the ASAM OpenMATERIAL® 3D coordinate definitions shall be used.
    During export to and import from glTF, a coordinate transformation shall be applied to conform with the glTF specification.
    Common modeling tools like Blender handle this conversion automatically.

FBX
:   Although FBX lacks a formal specification, *3D models* of ASAM OpenMATERIAL® 3D in FBX format shall be compatible with the official [AUTODESK FBX SDK](https://help.autodesk.com/view/FBX/2020/ENU/?guid=FBX_Developer_Help_welcome_to_the_fbx_sdk_html).

USD
:   *3D models* of ASAM OpenMATERIAL® 3D in USD format shall comply with the official [USD specification](https://openusd.org/release/index.html).

    The USD coordinate specification allows either +Y or +Z as the up axis, defined in the upAxis metadata.
    To adhere to the ASAM OpenMATERIAL® 3D geometry specification, +Z shall be used as the up axis.