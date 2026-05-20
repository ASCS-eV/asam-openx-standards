# ASAM OpenSCENARIO® DSL v2.2.0 — 8.3 Coordinate systems

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/dm_coordinate_systems.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.3 Coordinate systems

In ASAM OpenSCENARIO, the following coordinate system types are defined:

* A coordinate system that consists of three orthogonal directions associated with X, Y, and Z axes and a coordinate origin where axes meet, defines the right-handed Cartesian coordinate system.
  It is compliant with the ISO 8855:2011 [[11](../bibliography.html#bib-iso8855)] definition.
  Orientation of road objects is expressed extrinsically by the yaw, pitch, and roll angles derived from the sequence of rotations in the order: Z-axis, then Y-axis, then X-axis.
  The positive rotation is assumed to be counter-clockwise ("right-hand rule", see [Figure 11](#fig-yaw-pitch-roll)):

  ![Orientation coordinates](_images/2.svg)

  Figure 11. Yaw, pitch, and roll angle in an ISO 8855:2011 compliant coordinate system
* A route-based coordinate system that consists of two coordinate axes associated with the reference line of the corresponding route (s-axis) and the direction orthogonal to it (t-axis) and pointing leftwards.
  The definition of the s- and t-axes depends on the reference part of the route in use (see [Figure 12](#fig-s-t)).
  Common route elements that use this coordinate system in ASAM OpenSCENARIO include lanes, lane sections, roads, crossings, and paths.

  ![Road coordinates](_images/3.drawio.svg)

  Figure 12. Route-based s/t-coordinate system with origin at the beginning of the route

## 8.3.1. World coordinate system (Xw, Yw, Zw)

Coordinate system of type (X, Y, Z) fixed in the inertial reference frame of the simulation environment, with Xw and Yw axes parallel to the ground plane and Zw axis pointing upward.

Neither origin nor orientation of the world coordinate system is defined by ASAM OpenSCENARIO.
If a road network is referenced from a scenario, the world coordinate system is aligned with the inertial coordinate system present in this description.
In particular, the Zw-coordinate is assumed to consider a road elevation, an entire road super-elevation, or a lateral road shape profile.

## 8.3.2. Vehicle coordinate system (Xv, Yv, Zv)

The vehicle axis system of type (X, Y, Z), as defined in ISO 8855:2011 [[11](../bibliography.html#bib-iso8855)], is fixed in the reference frame of the vehicle sprung mass. The Xv axis is horizontal and forwards with the vehicle at rest.
The Xv axis is parallel to the vehicle’s longitudinal plane of symmetry.
The Yv axis is perpendicular to the vehicle’s longitudinal plane of symmetry and points left.
The Zv axis points upward.

In ASAM OpenSCENARIO, the origin of this coordinate system is derived by projecting the center of the vehicle’s rear axis to the ground plane at neutral load conditions.
The origin remains fixed to the vehicle sprung mass, as illustrated in [Figure 13](#fig-vehicle-coords).

For vehicles with a single axle, this axle is used to determine the reference point.
In the case of multiple rear axles, the first rear axle with permanent regular contact with the road surface is used.

![Vehicle coordinates](_images/4.svg)

Figure 13. Vehicle coordinate system

## 8.3.3. Physical object coordinate system (Xp , Yp , Zp)

Except for the special case of the [vehicle coordinate system](#vehicle-coords), the axis system for all physical objects is fixed in the reference frame of the object’s bounding box.
Both, the X-axis and Y-axis are horizontal.
If an obvious object’s front plane can be identified, for example, for pedestrians, the X-axis is normal to the object’s front plane pointing forward.
The Y-axis is horizontal, perpendicular to X, and points to the left. The Z-axis points upward.

The origin of this coordinate system is derived from the geometrical center of the object’s bounding box under neutral load conditions (if applicable) projected onto the ground plane.

## 8.3.4 Lane coordinate System (s/t)

To every lane specified in a lane section of a road, there is a s/t-type coordinate system assigned.
It is assumed the lane geometry is specified in the world coordinate system in the detailed road network definition (external to ASAM OpenSCENARIO).

The lane centerline is defined as the s-axis on the (X,Y)-plane of the world coordinate system going in the middle between the lane’s left and right boundaries throughout the whole lane section.
The shape of the s-axis line is determined by the geometry of the lane projected on the (X,Y)-plane.
The s-coordinate is calculated along the s-axis without considering an elevation of the lane in the s-direction.

At each s-coordinate along the s-axis a new t-axis is defined.
Being located on the (X,Y)-plane, each t-axis points to the left orthogonally to the s-axis direction.
The t-coordinate is calculated without considering the lateral profile of the road.

The vertical position orthogonally to the local (s,t)-plane depends on the road elevation and lateral profile, and therefore it is derived from the respective detailed road network description (external to ASAM OpenSCENARIO).
Both s- and t-coordinate are relevant within the respective road boundaries.

The origin of the s-coordinate is fixed to the beginning of the lane centerline.
The origin of the t-coordinate resides on the lane s-axis at the respective s-coordinate.

## 8.3.5 Lane section coordinate system (s/t)

To every lane section specified within a road, there is a s/t-type coordinate system assigned.
It is assumed the lane section geometry is specified in the world coordinate system in the detailed road network definition (external to ASAM OpenSCENARIO).

The s-axis of the lane section coincides with the s-axis of one of the lanes that is contained within the lane section.
ASAM OpenSCENARIO allows users to indicate which lane should be chosen to define the s-axis of the lane section.

The t-axes of the lane section also coincide with the t-axes of the chosen lane at the respective s-coordinates.

The vertical position orthogonally to the local (s,t)-plane depends on the road elevation and lateral profile, and therefore it is derived from the respective detailed road network description (external to ASAM OpenSCENARIO).

In the case of multiple lane sections, each lane section defines its own set of lanes with their own s-axes.

## 8.3.6 Road coordinate system (s/t)

To every road specified in the ASAM OpenSCENARIO abstract road network definition, there is an s/t-type coordinate system assigned.
It is assumed the road geometry is specified in the world coordinate system in the detailed road network definition (external to ASAM OpenSCENARIO).

The road reference line is defined as the sequence of s-axes from the lane sections that compose the road.
The road t-axes coincide with the t-axes of the corresponding lane section at the respective s-coordinates.

The vertical position orthogonally to the local (s,t)-plane depends on the road elevation and lateral profile, and therefore it is derived from the respective detailed road network description (external to ASAM OpenSCENARIO).

## 8.3.7 Crossing coordinate system (s/t)

To every crossing specified within a road network, there is a s/t-type coordinate system assigned.
It is assumed the crossing geometry is specified in the world coordinate system in the detailed road network definition (external to ASAM OpenSCENARIO).

The crossing’s centerline is defined as the s-axis on the (X,Y)-plane of the world coordinate system going in the middle between the crossing’s left and right boundaries throughout the whole crossing.
The shape of the s-axis line is determined by the geometry of the crossing projected on the (X,Y)-plane.
The s-coordinate is calculated along the s-axis without considering an elevation of the crossing in the s-direction.

At each s-coordinate along the s-axis a new t-axis is defined.
Being located on the (X,Y)-plane, each t-axis points to the left orthogonally to the s-axis direction.
The t-coordinate is calculated without considering the lateral profile of the crossing.

The vertical position orthogonally to the local (s,t)-plane depends on the road elevation and lateral profile, and therefore it is derived from the respective detailed road network description (external to ASAM OpenSCENARIO).
Both s- and t-coordinate are relevant within the respective road boundaries.

The origin of the s-coordinate is fixed to the beginning of the crossing centerline.
The origin of the t-coordinate resides on the crossing s-axis at the respective s-coordinate.

## 8.3.8 Path coordinate system (s/t)

To every path specified within the scenario, there is a s/t-type coordinate system assigned.
The path is deemed as an imaginary spatial directed line ("path line") that expresses a movement path.
The s-axis line is defined as a projection of the path line on the (X,Y)-plane of the world coordinate system.
The s-coordinate is calculated along the path s-axis without taking into account an elevation of the path in the s-direction.

At each s-coordinate along the s-axis a new t-axis is defined.
Being located on the (X,Y)-plane, each t-axis points to the left orthogonally to the s-axis direction.

The vertical position orthogonally to the local (s,t)-plane depends on the road elevation and lateral profile, and therefore it is derived from the respective detailed road network description (external to ASAM OpenSCENARIO).

The origin of the s-coordinate is fixed to the beginning of the projected path line.
The origin of the t-coordinate resides on the path s-axis at the respective s-coordinate.

## 8.3.9 Geographic coordinate system (latitude, longitude, altitude)

ASAM OpenSCENARIO accepts position coordinates expressed in spherical geographic coordinate systems as longitude, latitude, and altitude.
Interpretation of geographic coordinates might depend on the reference geoid model (datum) used in the geographic coordinate system and is therefore external to ASAM OpenSCENARIO.

The world coordinate system is considered the projected coordinate system compatible with the ENU (East, North, Up) convention of the X/Y/Z-axis directions and is derived from the used geographic coordinate system that is based on the applied geoid model.
The (X,Y)-plane of the world coordinate system is assumed to be a local tangent plane in relation to the surface of the reference geoid model.

If coordinates of positions are derived from the geographic coordinate system, the road network definition shall specify the map projection system type involved and provide its mandatory parameters.