# ASAM Openscenario Dsl v2.2.0 — 8.10 Environment actors

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/environment-actors.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.10 Environment actors

## 8.10.1 Environment

In ASAM OpenSCENARIO, all settings or changes to the environment are conducted through the `environment` actor.
For a detailed definition of the actions that can be executed by the `environment` actor, see [Section 8.11.1, "Actions for environment"](environment-actions.html#sec-dm-actions-action-environment).

![Diagram](_images/diag-08096048882bb62d994707cdc9a66c9eacc7f938.png)

## 8.10.2 Actor environment

The environment actor executes all environment actions.

Note that the environment model is partitioned in a way that facilitates custom extensions and extensions for future versions of ASAM OpenSCENARIO.
Therefore, some classes may carry only one member variable for the time being.
For example, instead of adding 'fog\_visual\_range' as a direct property of the 'environment' actor, the class 'fog' contains visual\_range as a property.
In that way, an extension like adding properties like 'bounding\_box' and 'position' to the class 'fog' is easier and readibility is improved at the same time.

Note that when defining 'geodetic\_position' and 'datetime', the position of instances of 'celestial\_light\_source' (like 'sun' or 'moon') shall be calculated with underlying models resulting also in a change of their position with elapsing simulation time.
For fixed positions of instances of 'celestial\_light\_source', their 'celestial\_position' shall be set using the assign\_celestial\_postion action instead.
Setting this state shall override calculated positions in case 'geodetic\_position' and 'datetime' are specified as well.

Basic information
:   Table 154. Basic information of actor environment


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Parents** | [osc\_actor](entity.html#sec-environment-abstract-osc_actor) |

Parameters
:   Table 155. Actor environment


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | geodetic\_position | [geodetic\_position\_2d](physical_types.html#sec-physical_types-class-geodetic_position_2d) | no | Geodetic position of world coordinate frame regarding WGS84. Regarding usage for determination of angle of celestial light sources see remark above. |
    | datetime | [time](physical_types.html#sec-physical_types-class-time) | no | Date and time [at](movement-modifiers.html#sec-actions_movableobjects-enum-at) start of scenario as Unix time, i.e. Number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds. Regarding usage for determination of angle of celestial light sources see remark above. |
    | sun | [celestial\_light\_source](#sec-environment-class-celestial_light_source) | no | Sun as instance of celestial\_light\_source. |
    | moon | [celestial\_light\_source](#sec-environment-class-celestial_light_source) | no | Moon as instance of celestial\_light\_source. |

State variables
:   Table 156. State variables of actor environment


    | Variable | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | weather | [weather](#sec-environment-class-weather) | no | See struct [weather](#sec-environment-class-weather) |

### 8.10.2.1 Methods

#### 8.10.2.1.1 Method local\_to\_unix\_time()

Returns the unix time from local date and time input.

Prototype
:   ```
    extend environment:
        def local_to_unix_time(year: uint, month: uint, day: uint, hour: uint, minute: uint, second: uint, time_zone: float) -> time
    ```

Return value
:   Returns the unix time to be used for environment actor with the local date, time and the time zone as input.

Parameters
:   Table 157. Parameter for method local\_to\_unix\_time()


    | Parameter | Type | Description |
    | --- | --- | --- |
    | year | uint | Year with century, e.g. 2022. |
    | month | uint | Month in the range of 1 to 12. |
    | day | uint | Day of the month in the range of 1 to 31. |
    | hour | uint | Hour (24-hour clock) in the range of 0 to 23. |
    | minute | uint | Minute in the range of 0 to 59. |
    | second | uint | Seconds in the range of 0 to 60, 60 for representing leap seconds. |
    | time\_zone | float | Time zone offset indicating a positive or negative time difference from UTC/GMT in hours. Using type float because e.g. Îles Marquises use -9.5. |

### 8.10.2.2 Examples

Code 75. Syntax examples for environment actor

```
# instantiate the environment actor
environment: environment

# set datetime with unix time
keep(environment.datetime == 1643764822.0)
# alternative: use local_to_unix_time for convenience and better readability
keep(environment.datetime == environment.local_to_unix_time(year: 2022, month: 2, day: 2, hour: 2, minute: 20, second: 22, time_zone: 0))
# note: this can be shortened by dropping the names of the arguments while preserving their order
keep(environment.datetime == environment.local_to_unix_time(2022, 2, 2, 2, 20, 22, 0))

# set geodetic position
keep(environment.geodetic_position.lat == 48.0231718deg)
keep(environment.geodetic_position.lon == 11.68087deg)
```

## 8.10.3 Struct weather

Structure for weather related effects.

Basic information
:   Table 158. Basic information of struct weather


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Used by** | [environment](#sec-environment-class-environment) |

Parameters
:   Table 159. Struct weather


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | [air](#sec-environment-class-air) | [air](#sec-environment-class-air) | no | See [air](#sec-environment-class-air) |
    | rain | [precipitation](#sec-environment-class-precipitation) | no | Liquid water in form of droplets falling under gravity. |
    | snow | [precipitation](#sec-environment-class-precipitation) | no | Frozen water in delicately-crystalline flakes falling under gravity. |
    | [wind](#sec-environment-class-wind) | [wind](#sec-environment-class-wind) | no | See [wind](#sec-environment-class-wind) |
    | [fog](#sec-environment-class-fog) | [fog](#sec-environment-class-fog) | no | See [fog](#sec-environment-class-fog) |
    | [clouds](#sec-environment-class-clouds) | [clouds](#sec-environment-class-clouds) | no | See [clouds](#sec-environment-class-clouds) |

## 8.10.4 Struct air

Structure for air related effects.

Basic information
:   Table 160. Basic information of struct air


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Used by** | [weather](#sec-environment-class-weather) |

Parameters
:   Table 161. Struct air


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | temperature | [temperature](physical_types.html#sec-physical_types-class-temperature) | no | Temperature on ground level. |
    | pressure | [pressure](physical_types.html#sec-physical_types-class-pressure) | no | Atmospheric pressure on ground level. |
    | relative\_humidity | float | no | Relative humidity on ground level. |

## 8.10.5 Struct precipitation

Structure for air-related effects for different types of precipitation.

Basic information
:   Table 162. Basic information of struct precipitation


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Used by** | [weather](#sec-environment-class-weather) |

Parameters
:   Table 163. Struct precipitation


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | intensity | [speed](physical_types.html#sec-physical_types-class-speed) | no | Global intensity of [precipitation](#sec-environment-class-precipitation) given as volumetric flux. In case of (partially) solid precipitation, the equivalent melted volume shall be considered. Note that volumetric flux is describing a volume flow across an area in units of mmph or millimeter\_per\_hour. After reduction, the unit results in the same unit as for speed. As of now, it is not possible to define multiple physical types with the same unit. Therefore, the speed type is used for volumetrix flux as well. |

## 8.10.6 Struct wind

Properties relating to wind.

Basic information
:   Table 164. Basic information of struct wind


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Used by** | [weather](#sec-environment-class-weather) |

Parameters
:   Table 165. Struct wind


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | speed | [speed](physical_types.html#sec-physical_types-class-speed) | yes | The expected value of [wind](#sec-environment-class-wind) speed. To estimate the expected value, rolling mean value over a specific short interval (for example, 3s) can be used. |
    | direction | [angle](physical_types.html#sec-physical_types-class-angle) | yes | The origin direction of the [wind](#sec-environment-class-wind) (not target direction) in the ground/x-y-plane with clockwise increasing values to match common definitions. This results in 0 deg for a [wind](#sec-environment-class-wind) blowing from the North 90 deg for a [wind](#sec-environment-class-wind) blowing from the East 90 deg, if x-axis and y-axis are mapped to East and North. |

## 8.10.7 Struct fog

Visible aerosol consisting of water droplets suspended in the air close to ground level.

Basic information
:   Table 166. Basic information of struct fog


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Used by** | [weather](#sec-environment-class-weather) |

Parameters
:   Table 167. Struct fog


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | visual\_range | [length](physical_types.html#sec-physical_types-class-length) | yes | Value of optical range of visible light in the standard setting, which corresponds to a certain density of fog. |

## 8.10.8 Struct clouds

Specification of the clouds in the sky.

Basic information
:   Table 168. Basic information of struct clouds


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |
    | **Used by** | [weather](#sec-environment-class-weather) |

Parameters
:   Table 169. Struct clouds


    | Parameter | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | cloudiness | uint | yes | Using okta scale to define which portion of the sky is covered with clouds. Ranging from 0 for completely clear sky to 8 for a completely overcast sky. The value 9 indicates an obscured sky, e.g. in dense fog. Values above 9 shall not be used. |

## 8.10.9 Struct celestial\_light\_source

Celestial light sources, typically sun or moon.

Basic information
:   Table 170. Basic information of struct celestial\_light\_source


    |  |  |
    | --- | --- |
    | **Instantiable** | yes |

State variables
:   Table 171. State variables of struct celestial\_light\_source


    | Variable | Type | Mandatory | Description |
    | --- | --- | --- | --- |
    | position | [celestial\_position\_2d](physical_types.html#sec-physical_types-class-celestial_position_2d) | yes | Position of the light source, see definition of physical type celestial\_position\_2d. |