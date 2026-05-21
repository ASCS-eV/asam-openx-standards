# Cross-References: Concept Mapping Across ASAM Standards

This document maps equivalent or related concepts across ASAM OpenX standards
and ISO 345xx. Use it to find where a concept is defined in each standard.

## Legend

- **§** = section/clause number
- **—** = concept not present in that standard
- Cells show: `term (location)` or just `location` if term matches

## Road Network Concepts

| Concept | OpenDRIVE v1.9 | OpenODD v1.0 | OpenLABEL v1.0 | ISO 34503 |
|---------|---------------|--------------|----------------|-----------|
| Road type | `e_roadType` (A.6.2) | scenery module | `DrivableAreaType` | Clause 8 |
| Lane type | `e_laneType` (A.3.7) | — | `LaneSpecificationType` | — |
| Lane direction | `e_lane_direction` (A.3.11) | — | `LaneSpecificationTravelDirection` | — |
| Traffic direction | `@rule` LHT/RHT (§11) | — | — | — |
| Junction/intersection | `e_junction_type` (A.2.1) | — | `JunctionIntersection`, `JunctionRoundabout` | — |
| Road surface | `e_objectType: roadSurface` (A.4.5) | scenery surfaces | `DrivableAreaSurfaceCondition` | Clause 8 |
| Road marking | `e_roadMarkType` (A.3.4) | — | — | — |
| Speed limit | `<type>` element (§6) | — | — | — |
| Elevation profile | `<elevationProfile>` (§10) | — | — | — |

## Object & Signal Concepts

| Concept | OpenDRIVE v1.9 | OpenODD v1.0 | OpenLABEL v1.0 | OpenSCENARIO v2.2 |
|---------|---------------|--------------|----------------|-------------------|
| Object types | `e_objectType` (A.4.5) | scenery objects | — | entity types |
| Traffic signal | `<signal>` (§14) | — | — | `trafficSignalController` |
| Traffic sign | `<signal>` (§14) | — | — | — |
| Bridge/tunnel | `e_bridgeType` (A.4.6) | — | — | — |
| Barrier/railing | `e_objectType: barrier` | — | — | — |
| Pedestrian crossing | `e_objectType: crosswalk` | — | — | — |

## Environmental Conditions

| Concept | OpenODD v1.0 | OpenLABEL v1.0 | ISO 34503 | OpenSCENARIO v2.2 |
|---------|--------------|----------------|-----------|-------------------|
| Weather (rain) | Annex B, weather module | `WeatherType` | Clause 10.2 | `weather` action |
| Weather (fog) | Annex B, weather module | `WeatherType` | Clause 10.2 | `weather` action |
| Illumination | Annex B, lighting | `IlluminationType` | Clause 10.1 | `timeOfDay` |
| Wind | — | — | Clause 10.3 | — |
| Road condition | Annex B, surface | `DrivableAreaSurfaceCondition` | Clause 8 | — |

## Traffic Participants / Road Users

| Concept | OpenDRIVE v1.9 | OpenODD v1.0 | OpenLABEL v1.0 | OpenSCENARIO v2.2 | TrafficParticipants v1.0 |
|---------|---------------|--------------|----------------|-------------------|--------------------------|
| Vehicle categories | `e_vehicleCategory` (A.7.7) | Clause 7 | `RoadUserType` | `vehicle` entity | vehicle taxonomy |
| Pedestrian | `e_personCategory` (A.7.6) | Clause 7 | `RoadUserType` | `pedestrian` entity | pedestrian types |
| Cyclist | — | Clause 7 | `RoadUserType` | `vehicle` (bicycle) | cyclist types |

## Geometry & Coordinate Systems

| Concept | OpenDRIVE v1.9 | OpenCRG v1.2 | OSI v3.7+ |
|---------|---------------|--------------|-----------|
| Inertial coordinates | §8.2 (ENU) | local frame | `global_ground_truth` |
| Road reference line | §8.3 (s/t/h) | reference line | — |
| Georeferencing | `<geoReference>` proj4 (§6.4) | — | — |
| Surface elevation | `<elevationProfile>` (§10) | CRG height grid | `lane_boundary` z-values |

## Data Quality & Provenance

| Concept | OpenDRIVE v1.9 | hdmap ontology (v6) | Meaning |
|---------|---------------|--------------------:|---------|
| Raw data source | `e_dataQuality_RawData_Source` (A.1.3) | `measurementSystem` | sensor/cadaster/custom |
| Accuracy | — (not in format) | `accuracyLaneModel2d`, `accuracySignals` etc. | Ontology EXTENDS the standard |
| Precision | — (not in format) | `precision` | Relative precision of measurements |

## Format Identification

| Format Name (hdmap:formatType) | Standard | Key Identifier |
|-------------------------------|----------|----------------|
| `ASAM OpenDRIVE` | OpenDRIVE v1.x | `<OpenDRIVE>` root, `revMajor`/`revMinor` |
| `Lanelet` | Lanelet2 | `<osm>` root with lanelet tags |
| `Road5` | IPG Road5 | Proprietary format |
| `Shape` | ESRI Shapefile | `.shp`/`.dbf`/`.shx` |
| `road2sim` | road2sim | Proprietary format |
| `roadXML` | Vires roadXML | `<roadXML>` root |

## Version History Notes

Key version boundaries that affect the hdmap ontology:

| Version | What Changed | Impact on Ontology |
|---------|-------------|-------------------|
| OpenDRIVE 1.4 → 1.5 | 6 town subtypes added to `e_roadType`; 6 lane types added; vehicle object types deprecated | SHACL version-conditional enums |
| OpenDRIVE 1.5 → 1.6 | `curb` lane type added | Included in v1.8+ branch |
| OpenDRIVE 1.7 → 1.8 | `walking`/`shared`/`slipLane` lanes; deprecations of `HOV`/`bus`/`taxi`/`sidewalk`; `roadSurface` replaces `patch` | Largest enum expansion |
| OpenDRIVE 1.8 → 1.9 | `other` added to `e_signals_semantics_lane` only | No hdmap enum impact |
