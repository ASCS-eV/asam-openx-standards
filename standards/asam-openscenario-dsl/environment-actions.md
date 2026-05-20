# ASAM Openscenario Dsl v2.2.0 — 8.11 Environment actions

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/environment-actions.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.11 Environment actions

## 8.11.1 Actions for environment

These actions are executed by the `environment` actor.
They can be used to specify the environmental conditions for the scenario.

![Diagram](_images/diag-87a2fea6fce18433c2e56cab2a92999353713b0a.png)

## 8.11.2 Action air

Specify state changes that relate to the air.

Basic information
:   Table 172. Basic information of action air


    |  |  |
    | --- | --- |
    | **Parents** | action\_for\_environment |
    | **Controlled states** | States related to air. |
    | **Action ending** | The action ends when the action of the same type is invoked. |

Parameters
:   Table 173. Action air


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | temperature | [temperature](physical_types.html#sec-physical_types-class-temperature) | no | See definition of [air](environment-actors.html#sec-environment-class-air) struct. |
    | pressure | [pressure](physical_types.html#sec-physical_types-class-pressure) | no | See definition of [air](environment-actors.html#sec-environment-class-air) struct. |
    | relative\_humidity | float | no | See definition of [air](environment-actors.html#sec-environment-class-air) struct. |

### 8.11.2.1 Examples

Code 75. Usage of air action

```
environment.air(temperature: temperature [, pressure: pressure] [, relative_humidity: float] [, <inherited action parameters>])

environment.air(pressure: pressure [, temperature: temperature] [, relative_humidity: float] [, <inherited action parameters>])

environment.air(relative_humidity: float [, temperature: temperature] [, pressure: pressure] [, <inherited action parameters>])
```

Use one, two or all three action parameters.
The unused parameters mean that the action will not modify the corresponding variable.

Code 76. Examples for air action

```
# All three variables
environment.air(15.0celsius, 1050.0hPa, 0.65)
environment.air(temperature: 15.0celsius, pressure: 1050.0hPa, relative_humidity: 0.65)

# Only temperature and relative humidity (presure is not modified)
environment.air(15.0celsius, relative_humidity: 0.65)
environment.air(temperature: 15.0celsius, relative_humidity: 0.65)

# Only temperature
environment.air(15.0celsius)
environment.air(temperature: 15.0celsius)

# Only pressure
environment.air(pressure: 1050.0hPa)

# Only relative_humidity
environment.air(relative_humidity: 0.65)
```

## 8.11.3 Action rain

Specify state changes that relate to rain.

Basic information
:   Table 174. Basic information of action rain


    |  |  |
    | --- | --- |
    | **Parents** | action\_for\_environment |
    | **Controlled states** | States related to rain. |
    | **Action ending** | The action ends when the action of the same type is invoked. |

Parameters
:   Table 175. Action rain


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | intensity | [speed](physical_types.html#sec-physical_types-class-speed) | no | See definition of [precipitation](environment-actors.html#sec-environment-class-precipitation) struct. |

### 8.11.3.1 Examples

Code 77. Usage of rain action

```
environment.rain(intensity: speed [, <inherited action parameters>])
```

In the following example, the rainfall intensity should be 20 mmph.

Code 78. Examples for rain action

```
environment.rain(20.0mmph)
environment.rain(intensity: 20.0mmph)
```

## 8.11.4 Action snow

Specify state changes that relate to snow.

Basic information
:   Table 176. Basic information of action snow


    |  |  |
    | --- | --- |
    | **Parents** | action\_for\_environment |
    | **Controlled states** | States related to snow. |
    | **Action ending** | The action ends when the action of the same type is invoked. |

Parameters
:   Table 177. Action snow


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | intensity | [speed](physical_types.html#sec-physical_types-class-speed) | no | See definition of [precipitation](environment-actors.html#sec-environment-class-precipitation) struct. |

### 8.11.4.1 Examples

Code 79. Usage of snow action

```
environment.snow(intensity: speed [, <inherited action parameters>])
```

In the following example, the snowfall intensity should be 10 mmph (melted amount).

Code 80. Examples for snow action

```
environment.snow(10.0mmph)
environment.snow(intensity: 10.0mmph)
```

## 8.11.5 Action wind

Specify state changes related to wind.

Basic information
:   Table 178. Basic information of action wind


    |  |  |
    | --- | --- |
    | **Parents** | action\_for\_environment |
    | **Controlled states** | States related to wind. |
    | **Action ending** | The action ends when the action of the same type is invoked. |

Parameters
:   Table 179. Action wind


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | speed | [speed](physical_types.html#sec-physical_types-class-speed) | no | See definition of [wind](environment-actors.html#sec-environment-class-wind) struct. |
    | direction | [angle](physical_types.html#sec-physical_types-class-angle) | no | See definition of [wind](environment-actors.html#sec-environment-class-wind) struct. |

### 8.11.5.1 Examples

Code 81. Usage of wind action

```
environment.wind(speed: speed, direction: angle [, <inherited action parameters>])
environment.wind(speed: speed [, <inherited action parameters>])
environment.wind(direction: angle [, <inherited action parameters>])
```

In the following example, the wind speed should be 3 m/s with an angle of 45 degrees.

Code 82. Examples for wind action

```
# Both variables
environment.wind(3.0mps, 45deg)
environment.wind(speed: 3.0mps, direction: 45deg)

# Only wind speed
environment.wind(3.0mps)
environment.wind(speed: 3.0mps)

# Only wind direction
environment.wind(direction: 45deg)
```

## 8.11.6 Action fog

Specify state changes related to fog.

Basic information
:   Table 180. Basic information of action fog


    |  |  |
    | --- | --- |
    | **Parents** | action\_for\_environment |
    | **Controlled states** | States related to fog. |
    | **Action ending** | The action ends when the action of the same type is invoked. |

Parameters
:   Table 181. Action fog


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | visual\_range | [length](physical_types.html#sec-physical_types-class-length) | no | See definition of [fog](environment-actors.html#sec-environment-class-fog) struct. |

### 8.11.6.1 Examples

Code 83. Usage of fog action

```
environment.fog(visual_range: length [, <inherited action parameters>])
```

In the following example, the visual range due to fog should be within 0.2 km.

Code 84. Examples for fog action

```
environment.fog(0.2km)
environment.fog(visual_range: 0.2km)
```

## 8.11.7 Action clouds

Specify state changes related to clouds.

Basic information
:   Table 182. Basic information of action clouds


    |  |  |
    | --- | --- |
    | **Parents** | action\_for\_environment |
    | **Controlled states** | States related to clouds. |
    | **Action ending** | The action ends when the action of the same type is invoked. |

Parameters
:   Table 183. Action clouds


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | cloudiness | uint | no | See definition of [clouds](environment-actors.html#sec-environment-class-clouds) struct. |

### 8.11.7.1 Examples

Code 85. Usage of clouds action

```
environment.clouds(cloudiness: uint [, <inherited action parameters>])
```

In the following example, the cloudiness level should be 4 oktas.

Code 86. Examples for clouds action

```
environment.clouds(4)
environment.clouds(cloudiness: 4)
```

## 8.11.8 Action assign\_celestial\_position

This action assigns the position of a celestial\_light\_source such as sun or moon. This will override possibly calculated positions based on geographic location and time. Unless this action is invoked again, the position of the celestial\_light\_source will remain fixed throughout the scenario.

Basic information
:   Table 184. Basic information of action assign\_celestial\_position


    |  |  |
    | --- | --- |
    | **Parents** | action\_for\_environment |
    | **Controlled states** | Position of celestial\_light\_source. |
    | **Action ending** | The action ends when the position is reached. |

Parameters
:   Table 185. Action assign\_celestial\_position


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | light\_source | [celestial\_light\_source](environment-actors.html#sec-environment-class-celestial_light_source) | yes | Celestial light source whose position will be assigned. |
    | azimuth | [angle](physical_types.html#sec-physical_types-class-angle) | no | See definition of [celestial\_position\_2d](physical_types.html#sec-physical_types-class-celestial_position_2d) struct. |
    | elevation | [angle](physical_types.html#sec-physical_types-class-angle) | no | See definition of [celestial\_position\_2d](physical_types.html#sec-physical_types-class-celestial_position_2d) struct. |

### 8.11.8.1 Examples

Code 87. Usage of assign\_celestial\_position

```
environment.assign_celestial_position(light_source: celestial_light_source, azimuth: angle, elevation: angle
[, <inherited action parameters>])

environment.assign_celestial_position(light_source: celestial_light_source, azimuth: angle
[, <inherited action parameters>])

environment.assign_celestial_position(light_source: celestial_light_source, elevation: angle
[, <inherited action parameters>])
```

This action assigns the position of a celestial object such as the sun or the moon.
Using the action will override the celestial positions that would be calculated based on geographic location (`geodetic_position`) and calendar time (`datetime`).
Unless this action is invoked again, the celestial position will remain fixed throughout the scenario.

Code 88. Examples for assign\_celestial\_position

```
# For moon position
environment.assign_celestial_position(environment.moon, 270deg, 90deg)
environment.assign_celestial_position(environment.moon, azimuth: 270deg, elevation: 90deg)

# For sun position
environment.assign_celestial_position(environment.sun, 100deg, 40deg)
environment.assign_celestial_position(environment.sun, azimuth: 100deg, elevation: 40deg)

# For sun, assign only azimuth
environment.assign_celestial_position(environment.sun, azimuth: 100deg)

# For sun, assign only elevation
environment.assign_celestial_position(environment.sun, elevation: 40deg)
```