# ASAM OpenDRIVE® v1.9.0 — G.1 Revision history ASAM OpenDRIVE® 1.8.0

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/revision_history/ASAM_OpenDRIVE_revision_history_V1-8-0.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# G.1 Revision history ASAM OpenDRIVE® 1.8.0

## G.1.1 Classes and attributes

### G.1.1.1 t\_header\_roadRegulation

```
XML element: <roadRegulations>
Introduced:  1.8.0
```

Table 215. Changed attributes of t\_header\_roadRegulation


| Name | Introduced |
| --- | --- |
| type | 1.8.0 |

### G.1.1.2 t\_header\_signalRegulation

```
XML element: <signalRegulations>
Introduced:  1.8.0
```

Table 216. Changed attributes of t\_header\_signalRegulation


| Name | Introduced |
| --- | --- |
| subtype | 1.8.0 |
| type | 1.8.0 |

### G.1.1.3 t\_license

```
XML element: <license>
Introduced:  1.8.0
```

Table 217. Changed attributes of t\_license


| Name | Introduced |
| --- | --- |
| name | 1.8.0 |
| resource | 1.8.0 |
| spdxid | 1.8.0 |
| text | 1.8.0 |

### G.1.1.4 t\_header\_defaultRegulations

```
XML element: <defaultRegulations>
Introduced:  1.8.0
```

### G.1.1.5 t\_junction\_connection\_virtual

```
XML element: <connection type="virtual">
Deprecated:  1.8.0
```

### G.1.1.6 t\_junction\_crossPath

```
XML element: <crossPath>
Introduced:  1.8.0
```

Table 218. Changed attributes of t\_junction\_crossPath


| Name | Introduced |
| --- | --- |
| crossingRoad | 1.8.0 |
| id | 1.8.0 |
| roadAtEnd | 1.8.0 |
| roadAtStart | 1.8.0 |

### G.1.1.7 t\_junction\_boundary

```
XML element: <boundary>
Introduced:  1.8.0
```

### G.1.1.8 t\_junction\_crossPath\_laneLink

```
XML element: <endLaneLink>
XML element: <startLaneLink>
Introduced:  1.8.0
```

Table 219. Changed attributes of t\_junction\_crossPath\_laneLink


| Name | Introduced |
| --- | --- |
| from | 1.8.0 |
| s | 1.8.0 |
| to | 1.8.0 |

### G.1.1.9 t\_junction\_connection\_laneLink

```
XML element: <laneLink>
```

Table 220. Changed attributes of t\_junction\_connection\_laneLink


| Name | Introduced |
| --- | --- |
| overlapZone | 1.8.0 |

### G.1.1.10 t\_junction\_elevationGrid\_elevation

```
XML element: <elevation>
Introduced:  1.8.0
```

Table 221. Changed attributes of t\_junction\_elevationGrid\_elevation


| Name | Introduced |
| --- | --- |
| center | 1.8.0 |
| left | 1.8.0 |
| right | 1.8.0 |

### G.1.1.11 t\_junction\_crossing

```
XML element: <junction type="crossing">
Introduced:  1.8.0
```

### G.1.1.12 t\_junction\_predecessorSuccessor

```
XML element: <predecessor>
XML element: <successor>
Deprecated:  1.8.0
```

Table 222. Changed attributes of t\_junction\_predecessorSuccessor


| Name | Deprecated |
| --- | --- |
| elementDir | 1.8.0 |
| elementId | 1.8.0 |
| elementS | 1.8.0 |
| elementType | 1.8.0 |

### G.1.1.13 t\_junction\_boundary\_segment\_lane

```
XML element: <segment type="lane">
Introduced:  1.8.0
```

Table 223. Changed attributes of t\_junction\_boundary\_segment\_lane


| Name | Introduced |
| --- | --- |
| boundaryLane | 1.8.0 |
| roadId | 1.8.0 |
| sEnd | 1.8.0 |
| sStart | 1.8.0 |
| type | 1.8.0 |

### G.1.1.14 t\_junction\_roadSection

```
XML element: <roadSection>
Introduced:  1.8.0
```

Table 224. Changed attributes of t\_junction\_roadSection


| Name | Introduced |
| --- | --- |
| id | 1.8.0 |
| roadId | 1.8.0 |
| sEnd | 1.8.0 |
| sStart | 1.8.0 |

### G.1.1.15 t\_junction\_elevationGrid

```
XML element: <elevationGrid>
Introduced:  1.8.0
```

Table 225. Changed attributes of t\_junction\_elevationGrid


| Name | Introduced |
| --- | --- |
| gridSpacing | 1.8.0 |
| sStart | 1.8.0 |

### G.1.1.16 t\_junction\_boundary\_segment\_joint

```
XML element: <segment type="joint">
Introduced:  1.8.0
```

Table 226. Changed attributes of t\_junction\_boundary\_segment\_joint


| Name | Introduced |
| --- | --- |
| contactPoint | 1.8.0 |
| jointLaneEnd | 1.8.0 |
| jointLaneStart | 1.8.0 |
| roadId | 1.8.0 |
| transitionLength | 1.8.0 |
| type | 1.8.0 |

### G.1.1.17 t\_road\_lanes\_laneSection\_lr\_lane\_access

```
XML element: <access>
```

Table 227. Changed attributes of t\_road\_lanes\_laneSection\_lr\_lane\_access


| Name | Deprecated |
| --- | --- |
| restriction | 1.8.0 |

### G.1.1.18 t\_road\_lanes\_laneSection\_right\_lane

```
XML element: <lane>
```

Table 228. Changed attributes of t\_road\_lanes\_laneSection\_right\_lane


| Name | Introduced |
| --- | --- |
| advisory | 1.8.0 |
| direction | 1.8.0 |
| dynamicLaneDirection | 1.8.0 |
| dynamicLaneType | 1.8.0 |
| roadWorks | 1.8.0 |

### G.1.1.19 t\_road\_lanes\_laneSection\_lr\_lane\_access\_restriction

```
XML element: <restriction>
Introduced:  1.8.0
```

Table 229. Changed attributes of t\_road\_lanes\_laneSection\_lr\_lane\_access\_restriction


| Name | Introduced |
| --- | --- |
| type | 1.8.0 |

### G.1.1.20 t\_road\_lanes\_laneSection\_left\_lane

```
XML element: <lane>
```

Table 230. Changed attributes of t\_road\_lanes\_laneSection\_left\_lane


| Name | Introduced |
| --- | --- |
| advisory | 1.8.0 |
| direction | 1.8.0 |
| dynamicLaneDirection | 1.8.0 |
| dynamicLaneType | 1.8.0 |
| roadWorks | 1.8.0 |

### G.1.1.21 t\_road\_lanes\_laneSection\_center\_lane

```
XML element: <lane>
```

Table 231. Changed attributes of t\_road\_lanes\_laneSection\_center\_lane


| Name | Deprecated |
| --- | --- |
| level | 1.8.0 |
| type | 1.8.0 |

### G.1.1.22 t\_road\_objects\_object\_skeleton\_polyline

```
XML element: <polyline>
Introduced:  1.8.0
```

Table 232. Changed attributes of t\_road\_objects\_object\_skeleton\_polyline


| Name | Introduced |
| --- | --- |
| id | 1.8.0 |

### G.1.1.23 t\_road\_objects\_object\_material

```
XML element: <material>
```

Table 233. Changed attributes of t\_road\_objects\_object\_material


| Name | Introduced |
| --- | --- |
| roadMarkColor | 1.8.0 |

### G.1.1.24 t\_road\_objects\_object\_skeleton\_polyline\_vertexLocal

```
XML element: <vertexLocal>
Introduced:  1.8.0
```

Table 234. Changed attributes of t\_road\_objects\_object\_skeleton\_polyline\_vertexLocal


| Name | Introduced |
| --- | --- |
| id | 1.8.0 |
| intersectionPoint | 1.8.0 |
| radius | 1.8.0 |
| u | 1.8.0 |
| v | 1.8.0 |
| z | 1.8.0 |

### G.1.1.25 t\_road\_objects\_object\_skeleton\_polyline\_vertexRoad

```
XML element: <vertexRoad>
Introduced:  1.8.0
```

Table 235. Changed attributes of t\_road\_objects\_object\_skeleton\_polyline\_vertexRoad


| Name | Introduced |
| --- | --- |
| dz | 1.8.0 |
| id | 1.8.0 |
| intersectionPoint | 1.8.0 |
| radius | 1.8.0 |
| s | 1.8.0 |
| t | 1.8.0 |

### G.1.1.26 t\_road\_objects\_object\_skeleton

```
XML element: <skeleton>
Introduced:  1.8.0
```

### G.1.1.27 t\_road\_objects\_object\_repeat

```
XML element: <repeat>
```

Table 236. Changed attributes of t\_road\_objects\_object\_repeat


| Name | Introduced |
| --- | --- |
| detachFromReferenceLine | 1.8.0 |

### G.1.1.28 t\_road\_lateralProfile\_crossSectionSurface\_tOffset

```
XML element: <tOffset>
Introduced:  1.8.0
```

### G.1.1.29 t\_road\_lateralProfile\_crossSectionSurface\_strip\_constant

```
XML element: <constant>
Introduced:  1.8.0
```

### G.1.1.30 t\_road\_lateralProfile\_crossSectionSurface\_strip\_linear

```
XML element: <linear>
Introduced:  1.8.0
```

### G.1.1.31 t\_road\_lateralProfile\_crossSectionSurface\_strip\_quadratic

```
XML element: <quadratic>
Introduced:  1.8.0
```

### G.1.1.32 t\_road\_lateralProfile\_crossSectionSurface\_surfaceStrip

```
XML element: <surfaceStrips>
Introduced:  1.8.0
```

### G.1.1.33 t\_road\_lateralProfile\_crossSectionSurface

```
XML element: <crossSectionSurface>
Introduced:  1.8.0
```

### G.1.1.34 t\_road\_planView\_geometry\_poly3

```
XML element: <poly3>
```

Table 237. Changed attributes of t\_road\_planView\_geometry\_poly3


| Name | Deprecated |
| --- | --- |
| a | 1.8.0 |
| b | 1.8.0 |
| c | 1.8.0 |
| d | 1.8.0 |

### G.1.1.35 t\_road\_lateralProfile\_crossSectionSurface\_coefficients

```
XML element: <coefficients>
Introduced:  1.8.0
```

Table 238. Changed attributes of t\_road\_lateralProfile\_crossSectionSurface\_coefficients


| Name | Introduced |
| --- | --- |
| a | 1.8.0 |
| b | 1.8.0 |
| c | 1.8.0 |
| d | 1.8.0 |

### G.1.1.36 t\_road\_lateralProfile\_crossSectionSurface\_strip\_cubic

```
XML element: <cubic>
Introduced:  1.8.0
```

### G.1.1.37 t\_road\_lateralProfile\_crossSectionSurface\_strip\_width

```
XML element: <width>
Introduced:  1.8.0
```

### G.1.1.38 t\_road\_lateralProfile\_crossSectionSurface\_strip

```
XML element: <strip>
Introduced:  1.8.0
```

### G.1.1.39 t\_road\_signals\_signal\_road

```
XML element: <signal>
```

Table 239. Changed attributes of t\_road\_signals\_signal\_road


| Name | Introduced |
| --- | --- |
| length | 1.8.0 |

### G.1.1.40 t\_signals\_semantics\_speed

```
XML element: <speed>
Introduced:  1.8.0
```

Table 240. Changed attributes of t\_signals\_semantics\_speed


| Name | Introduced |
| --- | --- |
| type | 1.8.0 |

### G.1.1.41 t\_signals\_semantics\_streetname

```
XML element: <streetname>
Introduced:  1.8.0
```

### G.1.1.42 t\_signals\_semantics\_supplementaryAllows

```
XML element: <supplementaryAllows>
Introduced:  1.8.0
```

### G.1.1.43 t\_signals\_semantics\_lane

```
XML element: <lane>
Introduced:  1.8.0
```

Table 241. Changed attributes of t\_signals\_semantics\_lane


| Name | Introduced |
| --- | --- |
| type | 1.8.0 |

### G.1.1.44 t\_signals\_semantics\_tourist

```
XML element: <tourist>
Introduced:  1.8.0
```

### G.1.1.45 t\_road\_signals\_staticBoard

```
XML element: <staticBoard>
Introduced:  1.8.0
```

### G.1.1.46 t\_signalGroup\_vmsBoardReference

```
XML element: <vmsBoardReference>
Introduced:  1.8.0
```

Table 242. Changed attributes of t\_signalGroup\_vmsBoardReference


| Name | Introduced |
| --- | --- |
| groupIndex | 1.8.0 |
| signalId | 1.8.0 |
| vmsIndex | 1.8.0 |

### G.1.1.47 t\_signals\_semantics\_supplementaryProhibits

```
XML element: <supplementaryProhibits>
Introduced:  1.8.0
```

### G.1.1.48 t\_signalGroup\_vmsGroup

```
XML element: <vmsGroup>
Introduced:  1.8.0
```

Table 243. Changed attributes of t\_signalGroup\_vmsGroup


| Name | Introduced |
| --- | --- |
| id | 1.8.0 |

### G.1.1.49 t\_signals\_semantics\_prohibited

```
XML element: <prohibited>
Introduced:  1.8.0
```

### G.1.1.50 t\_signals\_semantics\_supplementaryExplanatory

```
XML element: <supplementaryExplanatory>
Introduced:  1.8.0
```

### G.1.1.51 t\_signals\_semantics\_supplementaryEnvironment

```
XML element: <supplementaryEnvironment>
Introduced:  1.8.0
```

Table 244. Changed attributes of t\_signals\_semantics\_supplementaryEnvironment


| Name | Introduced |
| --- | --- |
| type | 1.8.0 |

### G.1.1.52 t\_signals\_semantics\_routing

```
XML element: <routing>
Introduced:  1.8.0
```

### G.1.1.53 t\_signals\_semantics\_parking

```
XML element: <parking>
Introduced:  1.8.0
```

### G.1.1.54 t\_signals\_semantics

```
XML element: <semantics>
Introduced:  1.8.0
```

### G.1.1.55 t\_signals\_semantics\_priority

```
XML element: <priority>
Introduced:  1.8.0
```

Table 245. Changed attributes of t\_signals\_semantics\_priority


| Name | Introduced |
| --- | --- |
| type | 1.8.0 |

### G.1.1.56 t\_road\_signals\_vmsBoard

```
XML element: <vmsBoard>
Introduced:  1.8.0
```

Table 246. Changed attributes of t\_road\_signals\_vmsBoard


| Name | Introduced |
| --- | --- |
| displayHeight | 1.8.0 |
| displayType | 1.8.0 |
| displayWidth | 1.8.0 |
| v | 1.8.0 |
| z | 1.8.0 |

### G.1.1.57 t\_road\_signals\_board\_sign

```
XML element: <sign>
Introduced:  1.8.0
```

Table 247. Changed attributes of t\_road\_signals\_board\_sign


| Name | Introduced |
| --- | --- |
| length | 1.8.0 |
| v | 1.8.0 |
| z | 1.8.0 |

### G.1.1.58 t\_signals\_semantics\_warning

```
XML element: <warning>
Introduced:  1.8.0
```

### G.1.1.59 t\_signals\_semantics\_supplementaryDistance

```
XML element: <supplementaryDistance>
Introduced:  1.8.0
```

Table 248. Changed attributes of t\_signals\_semantics\_supplementaryDistance


| Name | Introduced |
| --- | --- |
| type | 1.8.0 |
| unit | 1.8.0 |
| value | 1.8.0 |

### G.1.1.60 t\_signals\_semantics\_supplementaryTime

```
XML element: <supplementaryTime>
Introduced:  1.8.0
```

Table 249. Changed attributes of t\_signals\_semantics\_supplementaryTime


| Name | Introduced |
| --- | --- |
| type | 1.8.0 |
| value | 1.8.0 |

### G.1.1.61 t\_road\_signals\_displayArea

```
XML element: <displayArea>
Introduced:  1.8.0
```

Table 250. Changed attributes of t\_road\_signals\_displayArea


| Name | Introduced |
| --- | --- |
| height | 1.8.0 |
| index | 1.8.0 |
| v | 1.8.0 |
| width | 1.8.0 |
| z | 1.8.0 |

### G.1.1.62 t\_road\_signals\_signal\_positionRoad

```
XML element: <positionRoad>
Deprecated:  1.8.0
```

## G.1.2 Attributes and enumerations

### G.1.2.1 e\_junction\_type

```
Attribute name: type
```

Table 251. Changed enumeration literals of e\_junction\_type


| Name | Introduced |
| --- | --- |
| crossing | 1.8.0 |

### G.1.2.2 e\_junction\_segment\_type

```
Attribute name: type
```

Table 252. Changed enumeration literals of e\_junction\_segment\_type


| Name | Introduced |
| --- | --- |
| joint | 1.8.0 |
| lane | 1.8.0 |

### G.1.2.3 e\_junctionGroup\_type

```
Attribute name: type
```

Table 253. Changed enumeration literals of e\_junctionGroup\_type


| Name | Introduced |
| --- | --- |
| complexJunction | 1.8.0 |
| highwayInterchange | 1.8.0 |

### G.1.2.4 e\_laneAdvisory

```
Attribute name: advisory
```

Table 254. Changed enumeration literals of e\_laneAdvisory


| Name | Introduced |
| --- | --- |
| both | 1.8.0 |
| inner | 1.8.0 |
| none | 1.8.0 |
| outer | 1.8.0 |

### G.1.2.5 e\_accessRestrictionType

```
Attribute name: restriction
Attribute name: type
```

Table 255. Changed enumeration literals of e\_accessRestrictionType


| Name | Introduced |
| --- | --- |
| HOV | 1.8.0 |

### G.1.2.6 e\_laneType

```
Attribute name: laneType
Attribute name: type
```

Table 256. Changed enumeration literals of e\_laneType


| Name | Introduced | Deprecated |
| --- | --- | --- |
| HOV |  | 1.8.0 |
| bidirectional |  | 1.8.0 |
| bus |  | 1.8.0 |
| roadWorks |  | 1.8.0 |
| shared | 1.8.0 |  |
| sidewalk |  | 1.8.0 |
| slipLane | 1.8.0 |  |
| special1 |  | 1.8.0 |
| special2 |  | 1.8.0 |
| special3 |  | 1.8.0 |
| taxi |  | 1.8.0 |
| walking | 1.8.0 |  |

### G.1.2.7 e\_roadMarkColor

```
Attribute name: color
Attribute name: roadMarkColor
```

Table 257. Changed enumeration literals of e\_roadMarkColor


| Name | Introduced |
| --- | --- |
| black | 1.8.0 |

### G.1.2.8 e\_lane\_direction

```
Attribute name: direction
```

Table 258. Changed enumeration literals of e\_lane\_direction


| Name | Introduced |
| --- | --- |
| both | 1.8.0 |
| reversed | 1.8.0 |
| standard | 1.8.0 |

### G.1.2.9 e\_borderType

```
Attribute name: type
```

Table 259. Changed enumeration literals of e\_borderType


| Name | Introduced |
| --- | --- |
| paint | 1.8.0 |

### G.1.2.10 e\_outlineFillType

```
Attribute name: fillType
```

Table 260. Changed enumeration literals of e\_outlineFillType


| Name | Introduced |
| --- | --- |
| paint | 1.8.0 |

### G.1.2.11 e\_objectType

```
Attribute name: type
```

Table 261. Changed enumeration literals of e\_objectType


| Name | Introduced | Deprecated |
| --- | --- | --- |
| patch |  | 1.8.0 |
| railing |  | 1.8.0 |
| roadSurface | 1.8.0 |  |
| soundBarrier |  | 1.8.0 |
| streetLamp |  | 1.8.0 |

### G.1.2.12 e\_road\_signals\_displayType

```
Attribute name: displayType
```

Table 262. Changed enumeration literals of e\_road\_signals\_displayType


| Name | Introduced |
| --- | --- |
| LED | 1.8.0 |
| monochromGraphic | 1.8.0 |
| other | 1.8.0 |
| rotatingPrismHorizontal | 1.8.0 |
| rotatingPrismVertical | 1.8.0 |
| simpleMatrix | 1.8.0 |

### G.1.2.13 e\_signals\_semantics\_supplementaryTime

```
Attribute name: type
```

Table 263. Changed enumeration literals of e\_signals\_semantics\_supplementaryTime


| Name | Introduced |
| --- | --- |
| day | 1.8.0 |
| time | 1.8.0 |

### G.1.2.14 e\_signals\_semantics\_priority

```
Attribute name: type
```

Table 264. Changed enumeration literals of e\_signals\_semantics\_priority


| Name | Introduced |
| --- | --- |
| 4way | 1.8.0 |
| keepClearLine | 1.8.0 |
| noParkingLine | 1.8.0 |
| noTurnOnRed | 1.8.0 |
| priorityRoad | 1.8.0 |
| priorityRoadEnd | 1.8.0 |
| priorityToTheRightRule | 1.8.0 |
| stop | 1.8.0 |
| stopLine | 1.8.0 |
| trafficLight | 1.8.0 |
| turnOnRedAllowed | 1.8.0 |
| waitingLine | 1.8.0 |
| yield | 1.8.0 |

### G.1.2.15 e\_signals\_semantics\_lane

```
Attribute name: type
```

Table 265. Changed enumeration literals of e\_signals\_semantics\_lane


| Name | Introduced |
| --- | --- |
| noOvertakeCars | 1.8.0 |
| noOvertakeCarsEnd | 1.8.0 |
| noOvertakeTrucks | 1.8.0 |
| noOvertakeTrucksEnd | 1.8.0 |
| priorityOverOncoming | 1.8.0 |
| roundabout | 1.8.0 |
| yieldForOncoming | 1.8.0 |

### G.1.2.16 e\_signals\_semantics\_supplementaryEnvironment

```
Attribute name: type
```

Table 266. Changed enumeration literals of e\_signals\_semantics\_supplementaryEnvironment


| Name | Introduced |
| --- | --- |
| fog | 1.8.0 |
| rain | 1.8.0 |
| snow | 1.8.0 |

### G.1.2.17 e\_signals\_semantics\_speed

```
Attribute name: type
```

Table 267. Changed enumeration literals of e\_signals\_semantics\_speed


| Name | Introduced |
| --- | --- |
| maximum | 1.8.0 |
| maximumEnd | 1.8.0 |
| minimum | 1.8.0 |
| minimumEnd | 1.8.0 |
| recommended | 1.8.0 |
| recommendedEnd | 1.8.0 |
| zone | 1.8.0 |
| zoneEnd | 1.8.0 |

### G.1.2.18 e\_signals\_semantics\_supplementaryDistance

```
Attribute name: type
```

Table 268. Changed enumeration literals of e\_signals\_semantics\_supplementaryDistance


| Name | Introduced |
| --- | --- |
| for | 1.8.0 |
| in | 1.8.0 |