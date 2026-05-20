# ASAM Openscenario Dsl v2.2.0 — 8.14 Physical types and structs

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/physical_types.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.14 Physical types and structs

The following definitions constitute the types sub-module of the standard library.
They are reflected in `types.osc`, and are made available via either `import osc.standard.types`, `import osc.standard.all`, or `import osc.standard` statements, as defined in [Importing the standard library](../language-reference/Libraries.html#code-lc-libraries-file-import-standard-library).
They reside in the `stdtypes` namespace.

## 8.14.1 Scalar types

### 8.14.1.1 Type length

Physical type for length.

```
type length is SI(m: 1)
unit nanometer  of length is SI(m: 1, factor: 0.000000001)
unit nm         of length is SI(m: 1, factor: 0.000000001)
unit micrometer of length is SI(m: 1, factor: 0.000001)
unit millimeter of length is SI(m: 1, factor: 0.001)
unit mm         of length is SI(m: 1, factor: 0.001)
unit centimeter of length is SI(m: 1, factor: 0.01)
unit cm         of length is SI(m: 1, factor: 0.01)
unit meter      of length is SI(m: 1, factor: 1)
unit m          of length is SI(m: 1, factor: 1)
unit kilometer  of length is SI(m: 1, factor: 1000)
unit km         of length is SI(m: 1, factor: 1000)
unit inch       of length is SI(m: 1, factor: 0.0254)
unit feet       of length is SI(m: 1, factor: 0.3048)
unit mile       of length is SI(m: 1, factor: 1609.344)
unit mi         of length is SI(m: 1, factor: 1609.344)
```

### 8.14.1.2 Type time

Physical type for time.

```
type time is SI(s: 1)
unit millisecond of time is SI(s: 1, factor: 0.001)
unit ms          of time is SI(s: 1, factor: 0.001)
unit second      of time is SI(s: 1, factor: 1)
unit sec         of time is SI(s: 1, factor: 1)
unit s           of time is SI(s: 1, factor: 1)
unit minute      of time is SI(s: 1, factor: 60)
unit min         of time is SI(s: 1, factor: 60)
unit hour        of time is SI(s: 1, factor: 3600)
unit h           of time is SI(s: 1, factor: 3600)
```

### 8.14.1.3 Type speed

Physical type for speed.

```
type speed is SI(m: 1, s: -1)
unit meter_per_second    of speed is SI(m: 1, s: -1, factor: 1)
unit mps                 of speed is SI(m: 1, s: -1, factor: 1)
unit kilometer_per_hour  of speed is SI(m: 1, s: -1, factor: 0.277777778)
unit kmph                of speed is SI(m: 1, s: -1, factor: 0.277777778)
unit kph                 of speed is SI(m: 1, s: -1, factor: 0.277777778)
unit mile_per_hour       of speed is SI(m: 1, s: -1, factor: 0.447038889)
unit mph                 of speed is SI(m: 1, s: -1, factor: 0.447038889)
unit miph                of speed is SI(m: 1, s: -1, factor: 0.447038889)
unit mmph                of speed is SI(m: 1, s: -1, factor: 0.000000278)
unit millimeter_per_hour of speed is SI(m: 1, s: -1, factor: 0.000000278)
```

### 8.14.1.4 Type acceleration

Physical type for acceleration.

```
type acceleration is SI(m: 1, s: -2)
unit meter_per_sec_sqr          of acceleration is SI(m: 1, s: -2, factor: 1)
unit mpsps                      of acceleration is SI(m: 1, s: -2, factor: 1)
unit mpss                       of acceleration is SI(m: 1, s: -2, factor: 1)
unit kilometer_per_hour_per_sec of acceleration is SI(m: 1, s: -2, factor: 0.277777778)
unit kmphps                     of acceleration is SI(m: 1, s: -2, factor: 0.277777778)
unit mile_per_hour_per_sec      of acceleration is SI(m: 1, s: -2, factor: 0.447038889)
unit miphps                     of acceleration is SI(m: 1, s: -2, factor: 0.447038889)
```

### 8.14.1.5 Type jerk

Physical type for jerk.

```
type jerk is SI(m: 1, s: -3)
unit meter_per_sec_cubed of jerk is SI(m: 1, s: -3, factor: 1)
unit mpspsps             of jerk is SI(m: 1, s: -3, factor: 1)
unit mile_per_sec_cubed  of jerk is SI(m: 1, s: -3, factor: 1609.344)
unit mipspsps            of jerk is SI(m: 1, s: -3, factor: 1609.344)
```

### 8.14.1.6 Type angle

Physical type for angle.

```
type angle is SI(rad: 1)
unit degree of angle is SI(rad: 1, factor: 0.01745329252)
unit deg    of angle is SI(rad: 1, factor: 0.01745329252)
unit radian of angle is SI(rad: 1, factor: 1)
unit rad    of angle is SI(rad: 1, factor: 1)
```

### 8.14.1.7 Type angular\_rate

Physical type for angular\_rate.

```
type angular_rate is SI(rad: 1, s: -1)
unit degree_per_sec of angular_rate is SI(rad: 1, s: -1, factor: 0.01745329252)
unit degps          of angular_rate is SI(rad: 1, s: -1, factor: 0.01745329252)
unit radian_per_sec of angular_rate is SI(rad: 1, s: -1, factor: 1)
unit radps             of angular_rate is SI(rad: 1, s: -1, factor: 1)
```

### 8.14.1.8 Type angular\_acceleration

Physical type for angular\_acceleration.

```
type angular_acceleration is SI(rad: 1, s: -2)
unit degree_per_sec_sqr of angular_acceleration is SI(rad: 1, s: -2, factor: 0.01745329252)
unit degpsps            of angular_acceleration is SI(rad: 1, s: -2, factor: 0.01745329252)
unit radian_per_sec_sqr of angular_acceleration is SI(rad: 1, s: -2, factor: 1)
unit radpsps            of angular_acceleration is SI(rad: 1, s: -2, factor: 1)
```

### 8.14.1.9 Type mass

Physical type for mass.
The pound and lb units refer to pounds-mass.

```
type mass is SI(kg: 1)
unit gram     of mass is SI(kg: 1, factor: 0.001)
unit kilogram of mass is SI(kg: 1, factor: 1)
unit kg       of mass is SI(kg: 1, factor: 1)
unit ton      of mass is SI(kg: 1, factor: 1000)
unit pound    of mass is SI(kg: 1, factor: 0.45359237)
unit lb       of mass is SI(kg: 1, factor: 0.45359237)
```

### 8.14.1.10 Type temperature

Physical type for temperature.

```
type temperature is SI(K: 1)
unit K          of temperature is SI(K: 1, factor: 1)
unit kelvin     of temperature is SI(K: 1, factor: 1)
unit celsius    of temperature is SI(K: 1, factor: 1, offset: 273.15)
unit C          of temperature is SI(K: 1, factor: 1, offset: 273.15)
unit fahrenheit of temperature is SI(K: 1, factor: 0.555555556, offset: 255.372222222)
unit F          of temperature is SI(K: 1, factor: 0.555555556, offset: 255.372222222)
```

### 8.14.1.11 Type pressure

Physical type for pressure.

```
type pressure is SI(kg: 1, m: -1, s: -2)
unit newton_per_meter_sqr of pressure is SI(kg: 1, m: -1, s: -2, factor: 1)
unit Pa                   of pressure is SI(kg: 1, m: -1, s: -2, factor: 1)
unit pascal               of pressure is SI(kg: 1, m: -1, s: -2, factor: 1)
unit hPa                  of pressure is SI(kg: 1, m: -1, s: -2, factor: 100)
unit atm                  of pressure is SI(kg: 1, m: -1, s: -2, factor: 101325)
```

### 8.14.1.12 Type luminous\_intensity

Physical type for luminous\_intensity.

```
type luminous_intensity is SI(cd: 1)
unit cd      of luminous_intensity is SI(cd: 1, factor: 1)
unit candela of luminous_intensity is SI(cd: 1, factor: 1)
```

### 8.14.1.13 Type luminous\_flux

Physical type for luminous\_flux.

```
type luminous_flux is SI(cd: 1, rad: 2)
unit lm    of luminous_flux is SI(cd: 1, rad: 2, factor: 1)
unit lumen of luminous_flux is SI(cd: 1, rad: 2, factor: 1)
```

### 8.14.1.14 Type illuminance

Physical type for illuminance.

```
type illuminance is SI(cd: 1, rad: 2, m: -2)
unit lx  of illuminance is SI(cd: 1, rad: 2, m: -2, factor: 1)
unit lux of illuminance is SI(cd: 1, rad: 2, m: -2, factor: 1)
```

### 8.14.1.15 Type electrical\_current

Physical type for electrical\_current.

```
type electrical_current is SI(A: 1)
unit ampere of electrical_current is SI(A: 1, factor: 1)
unit A      of electrical_current is SI(A: 1, factor: 1)
```

### 8.14.1.16 Type amount\_of\_substance

Physical type for amount\_of\_substance.

```
type amount_of_substance is SI(mol: 1)
unit mole of amount_of_substance is SI(mol: 1, factor: 1)
unit mol  of amount_of_substance is SI(mol: 1, factor: 1)
```

## 8.14.2 Compound types

### 8.14.2.1 Struct position

Parent for position classes composed of physical types.

```
struct position
```

### 8.14.2.2 Struct position\_3d

Compound type for three-dimensional position in x-, y-, z-direction.
Inherited from generic position class.

```
struct position_3d inherits position:
    x: length
    y: length
    z: length
    def norm() -> length is undefined
```

### 8.14.2.3 Struct geodetic\_position\_2d

Compound type for geodetic position as latitude and longitude in a geographical coordinate system.
Positive latitude angles in North direction from equator.
Positive longitude angles in East direction from prime Meridian.
Inherited from generic position class.

```
struct geodetic_position_2d inherits position:
    latitude: angle
    longitude: angle
```

### 8.14.2.4 Struct celestial\_position\_2d

Compound type for celestial position in azimuth and elevation in a Horizontal Coordinate System, in which the y-axis-direction is 0 deg and the x-axis-direction is 90 deg.
As a result, North is 0 deg and East is 90 deg, if x-axis and y-axis are mapped to East and North respectively.
The origin of Horizontal Coordinate System equals the World Coordinate System origin.
Inherited from generic position class.

```
struct celestial_position_2d inherits position:
    azimuth: angle
    elevation: angle
```

### 8.14.2.5 Struct orientation\_3d

Compound type for three-dimensional orientation of objects using Tait-Bryan angles roll, pitch and yaw.
The rotations are to be performed yaw first (around the z-axis), pitch second (around the new y-axis) and roll third (around the new x-axis) to follow the definition according to ISO 8855.

```
struct orientation_3d:
    roll: angle
    pitch: angle
    yaw: angle
```

### 8.14.2.6 Struct pose\_3d

Compound type for pose in three-dimensional space, including compound types for three-dimensional position and orientation.

```
struct pose_3d:
    position: position_3d
    orientation: orientation_3d
```

### 8.14.2.7 Struct translational\_velocity\_3d

Compound type for three-dimensional translational velocity in x, y, z-direction.

```
struct translational_velocity_3d:
    x: speed
    y: speed
    z: speed
    def norm() -> speed is undefined
```

### 8.14.2.8 Struct orientation\_rate\_3d

Compound type for three-dimensional orientation rate of objects using Tait-Bryan angles roll, pitch and yaw.
The rotations are to be performed yaw first (around the z-axis), pitch second (around the new y-axis) and roll third (around the new x-axis) to follow the definition according to ISO 8855.

```
struct orientation_rate_3d:
    roll: angular_rate
    pitch: angular_rate
    yaw: angular_rate
```

### 8.14.2.9 Struct velocity\_6d

Compound type for velocity including compound types for three-dimensional translational velocity and orientation rate.

```
struct velocity_6d:
    translational: translational_velocity_3d
    angular: orientation_rate_3d
```

### 8.14.2.10 Struct translational\_acceleration\_3d

Compound type for three-dimensional translational acceleration in x, y, z-direction.

```
struct translational_acceleration_3d:
    x: acceleration
    y: acceleration
    z: acceleration
    def norm() -> acceleration is undefined
```

### 8.14.2.11 Struct orientation\_acceleration\_3d

Compound type for three-dimensional orientation acceleration of objects using Tait-Bryan angles roll, pitch and yaw.
The rotations are to be performed yaw first (around the z-axis), pitch second (around the new y-axis) and roll third (around the new x-axis) to follow the definition according to ISO 8855.

```
struct orientation_acceleration_3d:
    roll: angular_acceleration
    pitch: angular_acceleration
    yaw: angular_acceleration
```

### 8.14.2.12 Struct acceleration\_6d

Compound type for acceleration including compound types for three-dimensional translational and orientational acceleration.

```
struct acceleration_6d:
    translational: translational_acceleration_3d
    angular: orientation_acceleration_3d
```

### 8.14.2.13 Method norm()

The compound types position\_3d, translational\_velocity\_3d and translational\_acceleration\_3d provide the method norm(), which calculates the Euclidean norm, i.e. the scalar value.

Prototypes:

```
extend position_3d:
    def norm() -> length

extend translational_velocity_3d:
    def norm() -> speed

extend translational_acceleration_3d:
    def norm() -> acceleration
```

Example:

```
    pos: position_3d with:
        keep(it.x == 3m)
        keep(it.y == 4m)
        keep(it.z == 12m)

    distance: length = pos.norm() # result will be 13m
```