# ASAM Opendrive v1.9.0 — Annex A (normative): Enumerations

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/enumerations/map_uml_enumerations.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex A (normative): Enumerations

## A.1 Core

### A.1.1 e\_unitDistance

Table 154. Enumeration literals of the unitDistance attribute


| Name | Type |
| --- | --- |
| `ft` | string |
| `km` | string |
| `m` | string |
| `mile` | string |

### A.1.2 e\_unitSlope

Table 155. Enumeration literals of the unitSlope attribute


| Name | Type |
| --- | --- |
| `%` | string |

### A.1.3 e\_dataQuality\_RawData\_Source

Table 156. Enumeration literals of the dataQuality RawData Source attribute


| Name | Type |
| --- | --- |
| `cadaster` | string |
| `custom` | string |
| `sensor` | string |

### A.1.4 e\_paramPoly3\_pRange

Table 157. Enumeration literals of the paramPoly3 pRange attribute


| Name | Type |
| --- | --- |
| `arcLength` | string |
| `normalized` | string |

### A.1.5 e\_unitSpeed

Table 158. Enumeration literals of the unitSpeed attribute


| Name | Type |
| --- | --- |
| `km/h` | string |
| `m/s` | string |
| `mph` | string |

### A.1.6 e\_dataQuality\_RawData\_PostProcessing

Table 159. Enumeration literals of the dataQuality RawData PostProcessing attribute


| Name | Type |
| --- | --- |
| `cleaned` | string |
| `fused` | string |
| `processed` | string |
| `raw` | string |

### A.1.7 e\_unitMass

Table 160. Enumeration literals of the unitMass attribute


| Name | Type |
| --- | --- |
| `kg` | string |
| `t` | string |

### A.1.8 t\_yesNo

Table 161. Enumeration literals of the yesNo attribute


| Name | Type |
| --- | --- |
| `no` | string |
| `yes` | string |

## A.2 Junction

### A.2.1 e\_junction\_type

Table 162. Enumeration literals of the junction type attribute


| Name | Type | Introduced | Description |
| --- | --- | --- | --- |
| `crossing` | string | 1.8.0 | Unconnected crossing, e.g. railroad or pedestrian |
| `default` | string |  | Common junction, used if no value is specified |
| `direct` | string | 1.7.0 | Direct junction, e.g. entries and exits |
| `virtual` | string |  | Virtual junction, e.g. driveways and entries to parking lots |

### A.2.2 e\_road\_surface\_CRG\_purpose

Table 163. Enumeration literals of the road surface CRG purpose attribute


| Name | Type |
| --- | --- |
| `elevation` | string |
| `friction` | string |

### A.2.3 e\_road\_surface\_CRG\_mode

Table 164. Enumeration literals of the road surface CRG mode attribute


| Name | Type | Description |
| --- | --- | --- |
| `attached0` | string | ASAM OpenCRG reference line: is discarded. Total height: OpenCRG height only |
| `attached` | string | ASAM OpenCRG reference line: is discarded. Total height: ASAM OpenDRIVE height + OpenCRG height |
| `genuine` | string | ASAM OpenCRG reference line: shifted and rotated so beginning of reference line matches position given in ASAM OpenDRIVE. Total height: OpenCRG height only |
| `global` | string | ASAM OpenCRG reference line: shifted and rotated by xOffset, yOffset, zOffset and hOffset. Total height: OpenCRG height only |

### A.2.4 e\_junction\_segment\_type

Table 165. Enumeration literals of the junction segment type attribute


| Name | Type | Introduced |
| --- | --- | --- |
| `joint` | string | 1.8.0 |
| `lane` | string | 1.8.0 |

### A.2.5 e\_junctionGroup\_type

Table 166. Enumeration literals of the junctionGroup type attribute


| Name | Type | Introduced | Description |
| --- | --- | --- | --- |
| `complexJunction` |  | 1.8.0 | for example junctions with slip lanes |
| `highwayInterchange` |  | 1.8.0 | for example clover leaf interchange |
| `roundabout` | string |  |  |
| `unknown` | string |  |  |

### A.2.6 e\_elementDir

Table 167. Enumeration literals of the elementDir attribute


| Name | Type |
| --- | --- |
| `+` | string |
| `-` | string |

### A.2.7 e\_contactPoint

Table 168. Enumeration literals of the contactPoint attribute


| Name | Type |
| --- | --- |
| `end` | string |
| `start` | string |

### A.2.8 e\_connection\_type

Table 169. Enumeration literals of the connection type attribute


| Name | Type |
| --- | --- |
| `default` | string |
| `virtual` | string |

## A.3 Lane

### A.3.1 e\_roadMarkWeight

Table 170. Enumeration literals of the roadMarkWeight attribute


| Name | Type |
| --- | --- |
| `bold` | string |
| `standard` | string |

### A.3.2 e\_laneAdvisory

Table 171. Enumeration literals of the laneAdvisory attribute


| Name | Introduced | Description |
| --- | --- | --- |
| `both` | 1.8.0 | May be used by traffic from both adjacent lanes as an advisory lane. |
| `inner` | 1.8.0 | May be used by traffic from the inner lane as an advisory lane. |
| `none` | 1.8.0 | May not be used as an advisory lane. |
| `outer` | 1.8.0 | May be used by traffic from the outer lane as an advisory lane. |

### A.3.3 t\_bool

Table 172. Enumeration literals of the bool attribute


| Name | Type |
| --- | --- |
| `false` | string |
| `true` | string |

### A.3.4 e\_roadMarkType

Table 173. Enumeration literals of the roadMarkType attribute


| Name | Type | Description |
| --- | --- | --- |
| `botts dots` | string |  |
| `broken broken` | string | From inside to outside, exception: center lane – from left to right |
| `broken solid` | string | From inside to outside, exception: center lane – from left to right |
| `broken` | string |  |
| `curb` | string |  |
| `custom` | string | If detailed description is given in child tags |
| `edge` | string | Describing the limit of usable space on a road |
| `grass` | string | Meaning a grass edge |
| `none` | string |  |
| `solid broken` | string | From inside to outside, exception: center lane – from left to right |
| `solid solid` | string | For double solid line |
| `solid` | string |  |

### A.3.5 e\_accessRestrictionType

Table 174. Enumeration literals of the accessRestrictionType attribute


| Name | Type | Introduced |
| --- | --- | --- |
| `HOV` | string | 1.8.0 |
| `autonomousTraffic` | string |  |
| `bicycle` | string |  |
| `bus` | string |  |
| `delivery` | string |  |
| `emergency` | string |  |
| `motorcycle` | string |  |
| `none` | string |  |
| `passengerCar` | string |  |
| `pedestrian` | string |  |
| `simulator` | string |  |
| `taxi` | string |  |
| `throughTraffic` | string |  |
| `truck` | string |  |
| `trucks` | string |  |

### A.3.6 e\_road\_lanes\_laneSection\_lr\_lane\_access\_rule

Table 175. Enumeration literals of the road lanes laneSection lr lane access rule attribute


| Name | Type |
| --- | --- |
| `allow` | string |
| `deny` | string |

### A.3.7 e\_laneType

Table 176. Enumeration literals of the laneType attribute


| Name | Type | Introduced | Deprecated | Description |
| --- | --- | --- | --- | --- |
| `HOV` | string |  | 1.8.0 | High-occupancy vehicle / carpool vehicle. Use `<access>` instead |
| `bidirectional` | string |  | 1.8.0 | This lane type has two use cases:  a) only driving lane on a narrow road which may be used in both directions;  b) continuous two-way left turn lane on multi-lane roads – US road networks  Use @direction instead |
| `biking` | string |  |  | Lane that is reserved for cyclists. |
| `border` | string |  |  | Hard border at the edge of the road. It has the same height as the adjacent drivable lane. |
| `bus` | string |  | 1.8.0 | Use `<access>` instead |
| `connectingRamp` | string |  |  | Ramp that connects two motorways, for example, motorway junctions. |
| `curb` | string | 1.6.0 |  | Curb at the edge of the road. Curb stones have a different height than the adjacent drivable lanes. |
| `driving` | string |  |  | Normal drivable road that is not one of the other types. |
| `entry` | string |  |  | Lane that is used for sections that are parallel to the main road and merge into the main road. It is mainly used for acceleration lanes. |
| `exit` | string |  |  | Lane that is used for sections that are parallel to the main road and lead to an exit from the main road. It is mainly used for deceleration lanes. |
| `median` | string |  |  | Lane that sits between driving lanes that lead in opposite directions. It is typically used to separate traffic in towns on large roads. |
| `mwyEntry` | string |  | 1.5.0 | deprecated, use entry instead |
| `mwyExit` | string |  | 1.5.0 | deprecated, use exit instead |
| `none` | string |  |  | Space on the outermost edge of the road. A none lane does not have actual content. Its only purpose is for applications to register that ASAM OpenDRIVE is still present in case the (human) driver leaves the road. |
| `offRamp` | string |  |  | Ramp leading away from a motorway and onto rural urban roads. |
| `onRamp` | string |  |  | Ramp leading to a motorway from rural or urban roads. |
| `parking` | string |  |  | Lane with parking spaces. |
| `rail` | string |  |  | Lane used by trains only. |
| `restricted` | string |  |  | Lane on which cars should not drive. The lane has the same height as drivable lanes. Typically, the lane is separated with lines and often contains dotted lines as well. |
| `roadWorks` | string |  | 1.8.0 |  |
| `shared` |  | 1.8.0 |  | Shared by all traffic participants.  For shared walking/biking lanes use `<access>`. |
| `shoulder` | string |  |  | Soft border at the edge of the road. |
| `sidewalk` | string |  | 1.8.0 | Use walking instead |
| `slipLane` | string | 1.8.0 |  | On a slip lane a driver can change roads without driving into the main intersection. |
| `special1` | string |  | 1.8.0 | deprecated |
| `special2` | string |  | 1.8.0 | deprecated |
| `special3` | string |  | 1.8.0 | deprecated |
| `stop` | string |  |  | Hard shoulder on motorways for emergency stops. |
| `taxi` | string |  | 1.8.0 | Use `<access>` instead |
| `tram` | string |  |  | Lane used by trams only. |
| `walking` | string | 1.8.0 |  | Lane on which pedestrians can walk. |

### A.3.8 e\_road\_lanes\_laneSection\_lcr\_lane\_roadMark\_laneChange

Table 177. Enumeration literals of the road lanes laneSection lcr lane roadMark laneChange attribute


| Name | Type |
| --- | --- |
| `both` | string |
| `decrease` | string |
| `increase` | string |
| `none` | string |

### A.3.9 e\_layerType

Table 178. Enumeration literals of the layerType attribute


| Name | Type |
| --- | --- |
| `permanent` | string |
| `temporary` | string |

### A.3.10 e\_roadMarkColor

Table 179. Enumeration literals of the roadMarkColor attribute


| Name | Type | Introduced | Description |
| --- | --- | --- | --- |
| `black` |  | 1.8.0 |  |
| `blue` | string |  |  |
| `green` | string |  |  |
| `orange` | string |  |  |
| `red` | string |  |  |
| `standard` | string |  | equivalent to "white" |
| `violet` | string |  |  |
| `white` | string |  |  |
| `yellow` | string |  |  |

### A.3.11 e\_lane\_direction

Table 180. Enumeration literals of the lane direction attribute


| Name | Introduced | Description |
| --- | --- | --- |
| `both` | 1.8.0 | Bidirectional, both directions are valid. |
| `reversed` | 1.8.0 | Directly opposite to the standard direction. |
| `standard` | 1.8.0 | Direction is determined by the combination of `<left>` or `<right>` lane grouping and the values LHT or RHT of the @rule attribute of a road. |

### A.3.12 e\_roadMarkRule

Table 181. Enumeration literals of the roadMarkRule attribute


| Name | Type |
| --- | --- |
| `caution` | string |
| `no passing` | string |
| `none` | string |

## A.4 Object

### A.4.1 e\_tunnelType

Table 182. Enumeration literals of the tunnelType attribute


| Name | Type | Description |
| --- | --- | --- |
| `standard` | string |  |
| `underpass` | string | i.e. sides are open for daylight |

### A.4.2 e\_borderType

Table 183. Enumeration literals of the borderType attribute


| Name | Type | Introduced |
| --- | --- | --- |
| `concrete` | string |  |
| `curb` | string |  |
| `paint` | string | 1.8.0 |

### A.4.3 e\_sideType

Table 184. Enumeration literals of the sideType attribute


| Name | Type |
| --- | --- |
| `front` | string |
| `left` | string |
| `rear` | string |
| `right` | string |

### A.4.4 e\_outlineFillType

Table 185. Enumeration literals of the outlineFillType attribute


| Name | Type | Introduced |
| --- | --- | --- |
| `asphalt` | string |  |
| `cobble` | string |  |
| `concrete` | string |  |
| `grass` | string |  |
| `gravel` | string |  |
| `paint` | string | 1.8.0 |
| `pavement` | string |  |
| `soil` | string |  |

### A.4.5 e\_objectType

Table 186. Enumeration literals of the objectType attribute


| Name | Type | Introduced | Deprecated | Description |
| --- | --- | --- | --- | --- |
| `barrier` | string |  |  | A barrier is a continuous object, which cannot be passed. |
| `bike` | string |  | 1.5.0 | deprecated |
| `building` | string |  |  | A building is a closed object, which cannot be passed. |
| `bus` | string |  | 1.5.0 | deprecated |
| `car` | string |  | 1.5.0 | deprecated |
| `crosswalk` | string |  |  | A crosswalk is an object on the road that can be passed.  It is recommended to be defined as `<crossPath>` within a junction for pedestrian/bicycle simulation.  If the crosswalk is defined as an object only, it will not be used for pedestrian/bicycle simulation. |
| `gantry` | string |  |  | A gantry is an object above a road on which `<signals>` are placed. |
| `motorbike` | string |  | 1.5.0 | deprecated |
| `none` | string |  |  | All other objects, that don’t fit into existing categories or unknown. |
| `obstacle` | string |  |  | An obstacle is an object on or beside the road that cannot be passed. |
| `parkingSpace` | string |  |  | A parkingSpace is an object on a lane on which vehicles are parked. |
| `patch` | string |  | 1.8.0 | use roadSurface instead |
| `pedestrian` | string |  | 1.5.0 | deprecated |
| `pole` | string |  |  | A pole is a thin long object. |
| `railing` | string |  | 1.8.0 | use barrier instead |
| `roadMark` | string |  |  | A roadMark object is painted on the road and can be passed. |
| `roadSurface` | string | 1.8.0 |  | A roadSurface object is on the road and can be passed. |
| `soundBarrier` | string |  | 1.8.0 | use barrier instead |
| `streetLamp` | string |  | 1.8.0 | use pole instead |
| `trafficIsland` | string |  |  | A trafficIsland object is on the road and should not be passed by vehicles. |
| `trailer` | string |  | 1.5.0 | deprecated |
| `train` | string |  | 1.5.0 | deprecated |
| `tram` | string |  | 1.5.0 | deprecated |
| `tree` | string |  |  | A tree object is a single vegetational object with a trunk. |
| `van` | string |  |  |  |
| `vegetation` | string |  |  | A vegetation object is a single vegetational object without a trunk or an area of vegetation. |
| `wind` | string |  | 1.5.0 | deprecated, use pole instead |

### A.4.6 e\_bridgeType

Table 187. Enumeration literals of the bridgeType attribute


| Name | Type |
| --- | --- |
| `brick` | string |
| `concrete` | string |
| `steel` | string |
| `wood` | string |

### A.4.7 e\_orientation

Table 188. Enumeration literals of the orientation attribute


| Name | Type |
| --- | --- |
| `+` | string |
| `-` | string |
| `none` | string |

### A.4.8 e\_road\_objects\_object\_parkingSpace\_access

Table 189. Enumeration literals of the road objects object parkingSpace access attribute


| Name | Type |
| --- | --- |
| `all` | string |
| `bus` | string |
| `car` | string |
| `electric` | string |
| `handicapped` | string |
| `residents` | string |
| `truck` | string |
| `women` | string |

## A.5 Railroad

### A.5.1 e\_station\_type

Table 190. Enumeration literals of the station type attribute


| Name | Type |
| --- | --- |
| `large` | string |
| `medium` | string |
| `small` | string |

### A.5.2 e\_road\_railroad\_switch\_position

Table 191. Enumeration literals of the road railroad switch position attribute


| Name | Type |
| --- | --- |
| `dynamic` | string |
| `straight` | string |
| `turn` | string |

### A.5.3 e\_station\_platform\_segment\_side

Table 192. Enumeration literals of the station platform segment side attribute


| Name | Type |
| --- | --- |
| `left` | string |
| `right` | string |

## A.6 Road

### A.6.1 e\_road\_link\_elementType

Table 193. Enumeration literals of the road link elementType attribute


| Name | Type |
| --- | --- |
| `junction` | string |
| `road` | string |

### A.6.2 e\_roadType

Table 194. Enumeration literals of the roadType attribute


| Name | Type |
| --- | --- |
| `bicycle` | string |
| `lowSpeed` | string |
| `motorway` | string |
| `pedestrian` | string |
| `rural` | string |
| `townArterial` | string |
| `townCollector` | string |
| `townExpressway` | string |
| `townLocal` | string |
| `townPlayStreet` | string |
| `townPrivate` | string |
| `town` | string |
| `unknown` | string |

### A.6.3 e\_strip\_mode

Table 195. Enumeration literals of the strip mode attribute


| Name | Description |
| --- | --- |
| `independent` | height values due to cross section surfaces are calculated independent of the inner strip |
| `relative` | height values due to cross section surfaces are added to the height values of the outer edge of the inner strip |

### A.6.4 e\_maxSpeedString

Table 196. Enumeration literals of the maxSpeedString attribute


| Name | Type |
| --- | --- |
| `no limit` | string |
| `undefined` | string |

### A.6.5 e\_trafficRule

Table 197. Enumeration literals of the trafficRule attribute


| Name | Type |
| --- | --- |
| `LHT` | string |
| `RHT` | string |

### A.6.6 e\_direction

Table 198. Enumeration literals of the direction attribute


| Name | Type |
| --- | --- |
| `opposite` | string |
| `same` | string |

### A.6.7 e\_countryCode\_deprecated

Table 199. Enumeration literals of the countryCode deprecated attribute


| Name | Type |
| --- | --- |
| `Austria` | string |
| `Brazil` | string |
| `China` | string |
| `France` | string |
| `Germany` | string |
| `Italy` | string |
| `OpenDRIVE` | string |
| `Switzerland` | string |
| `USA` | string |

## A.7 Signal

### A.7.1 e\_road\_signals\_displayType

Table 200. Enumeration literals of the road signals displayType attribute


| Name | Introduced | Description |
| --- | --- | --- |
| `LED` | 1.8.0 | Full LED boards |
| `monochromGraphic` | 1.8.0 | Yellow or white text as lights on black background |
| `other` | 1.8.0 | All other display types that do not fit into current categories |
| `rotatingPrismHorizontal` | 1.8.0 | No lights. Horizontal rotating metal prism. |
| `rotatingPrismVertical` | 1.8.0 | No lights. Vertical rotating metal prism. |
| `simpleMatrix` | 1.8.0 | Outside is fixed, content inside changes. |

### A.7.2 e\_signals\_semantics\_supplementaryTime

Table 201. Enumeration literals of the signals semantics supplementaryTime attribute


| Name | Introduced |
| --- | --- |
| `day` | 1.8.0 |
| `time` | 1.8.0 |

### A.7.3 e\_signals\_semantics\_priority

Table 202. Enumeration literals of the signals semantics priority attribute


| Name | Introduced |
| --- | --- |
| `4way` | 1.8.0 |
| `keepClearLine` | 1.8.0 |
| `noParkingLine` | 1.8.0 |
| `noTurnOnRed` | 1.8.0 |
| `priorityRoadEnd` | 1.8.0 |
| `priorityRoad` | 1.8.0 |
| `priorityToTheRightRule` | 1.8.0 |
| `stopLine` | 1.8.0 |
| `stop` | 1.8.0 |
| `trafficLight` | 1.8.0 |
| `turnOnRedAllowed` | 1.8.0 |
| `waitingLine` | 1.8.0 |
| `yield` | 1.8.0 |

### A.7.4 e\_road\_signals\_signal\_reference\_elementType

Table 203. Enumeration literals of the road signals signal reference elementType attribute


| Name | Type |
| --- | --- |
| `object` | string |
| `signal` | string |

### A.7.5 e\_signals\_semantics\_lane

Table 204. Enumeration literals of the signals semantics lane attribute


| Name | Introduced | Description |
| --- | --- | --- |
| `noOvertakeCarsEnd` | 1.8.0 |  |
| `noOvertakeCars` | 1.8.0 |  |
| `noOvertakeTrucksEnd` | 1.8.0 |  |
| `noOvertakeTrucks` | 1.8.0 |  |
| `other` | 1.9.0 | Actual semantics shall be inferred through other ASAM OpenDRIVE definitions. Use when none of the other enum values fit. |
| `priorityOverOncoming` | 1.8.0 |  |
| `roundabout` | 1.8.0 |  |
| `yieldForOncoming` | 1.8.0 |  |

### A.7.6 e\_personCategory

Table 205. Enumeration literals of the personCategory attribute

### A.7.7 e\_vehicleCategory

Table 206. Enumeration literals of the vehicleCategory attribute


| Name | Type | Description |
| --- | --- | --- |
| `bicycle` | string | A bicycle is a human-powered or motor-assisted, pedal-driven vehicle. This category includes typical two-wheeled bicycles as well as cargo-bikes and other pedal-driven vehicles with more than two wheels. |
| `bus` | string | A bus is a motorized vehicle designed to carry multiple passengers. |
| `car` | string | A car is a motorized vehicle designed primarily for passenger transportation. A car typically has four wheels. |
| `heavyTruck` | string | A heavy truck is a large commercial vehicle designed for transporting heavy loads. The cargo area is rigidly fixed to the vehicle itself. |
| `landVehicle` | string | A land vehicle is a vehicle designed for travel on land. This category is deliberately generic to include land vehicles that do not fall into other categories and may be refined in future versions as needed. |
| `microMobilityDevice` | string | A micro-mobility device is a small, lightweight vehicle for short-distance travel, like hoverboards or roller skates. While bicycles, stand-up scooters, and wheelchairs may technically fall into this category, the respective detailed categories shall be used instead. |
| `motorcycle` | string | A motorcycle is a motorized vehicle designed primarily for passenger transportation. Compared to a car, fewer passive safety features, such as a full passenger cell, are typically present. This category includes both two-wheeled motorcycles and three-wheeled vehicles like motorcycles with side-cars or trikes. |
| `other` | string | Other (unspecified but known) type of vehicle. |
| `semiTractor` | string | A semi-tractor is a vehicle designed for towing semi-trailers for the transportation of heavy loads. |
| `semiTrailer` | string | A semi-trailer is a vehicle designed for being towed by a semi-tractor. Characteristics compared to a regular trailer are the large size, the fact that a large portion of the weight is supported at the hitch, and a large overlap with the towing vehicle, i.e. the semi-tractor. |
| `standupScooter` | string | A stand-up scooter is a compact, typically two-wheeled device. It is operated with the rider standing on a deck between the wheels. It may be propelled by a motor or the rider making a kicking movement. |
| `trailer` | string | A trailer is a non-motorized vehicle designed for being towed by a motorized vehicle to carry goods, animals, or people. |
| `train` | string | A train is a vehicle designed for the transport of passengers and freight on rail infrastructure. The rail infrastructure for trains is mostly grade-separated from the public road infrastructure as trains have exclusive right-of-way. Therefore, in case crossings with the road infrastructure occur, the exclusive right-of-way is ensured, e.g. by railway barriers. A train often acts as a series of connected vehicles. |
| `tram` | string | A tram is a vehicle designed for using rail infrastructure for the transport of passengers on rail infrastructure. The rail infrastructure may fully or partially overlap with public road infrastructure. In contrast to trains, trams do not have exclusive right-of-way. A tram often acts as a series of connected vehicles. |
| `van` | string | A van is a motorized vehicle with a larger cargo area than a car, used for transporting goods or people. This category is not intended for mini vans, which shall rather be categorized as cars. |
| `workMachine` | string | A work machine is a vehicle designed for specific tasks (e.g., construction equipment, agricultural tractors, forklifts). |

### A.7.8 e\_signals\_semantics\_supplementaryEnvironment

Table 207. Enumeration literals of the signals semantics supplementaryEnvironment attribute


| Name | Introduced |
| --- | --- |
| `fog` | 1.8.0 |
| `rain` | 1.8.0 |
| `snow` | 1.8.0 |

### A.7.9 e\_signals\_semantics\_speed

Table 208. Enumeration literals of the signals semantics speed attribute


| Name | Type | Introduced |
| --- | --- | --- |
| `maximumEnd` | string | 1.8.0 |
| `maximum` | string | 1.8.0 |
| `minimumEnd` | string | 1.8.0 |
| `minimum` | string | 1.8.0 |
| `recommendedEnd` | string | 1.8.0 |
| `recommended` | string | 1.8.0 |
| `zoneEnd` | string | 1.8.0 |
| `zone` | string | 1.8.0 |

### A.7.10 e\_signals\_semantics\_supplementaryDistance

Table 209. Enumeration literals of the signals semantics supplementaryDistance attribute


| Name | Introduced |
| --- | --- |
| `for` | 1.8.0 |
| `in` | 1.8.0 |