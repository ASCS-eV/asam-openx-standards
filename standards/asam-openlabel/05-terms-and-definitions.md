# ASAM OpenLABEL v1.0.0 — 5. Terms and definitions

- **Source**: ASAM_OpenLABEL_BS_V1-0-0.html
- **Version**: v1.0.0
- **Date**: November 9, 2021
- **License**: Restricted distribution (ASAM e.V. member access)

---

## 5. Terms and definitions


**AD (Autonomous Driving)**
: Non-abbreviated form: Autonomous Driving


**ADAS (Advanced Driver Assistance System)**
: Non-abbreviated form: Advanced Driver Assistance System


**Annotation (process)**
: Process of enriching raw data, for example, test scenario artifacts or data streams from multiple sensors, such as cameras, LiDARs, and radars with metadata. This metadata describes the content of the raw data, for example, static or dynamic objects populating a video, actions that are performed, or environmental conditions. Additional information regarding the data may also be included. Already enriched data can be enriched even further as well.


**Annotation instance**
: Enriches raw data with metadata required for the specific task. Annotation instances are usually serialized in a text-based file format, for example, JSON. Annotation instances have to conform to a pre-defined annotation schema.


**Annotation instance format**
: File format for serialization and storage of annotation instances. ASAM OpenLABEL uses JSON as annotation instance format.


**Annotation schema**
: Provides structure and constraints for annotation instances. Annotation instances shall adhere to the schema to be considered well-formed and valid. The definition of an annotation schema is the core of ASAM OpenLABEL.


**Annotation schema format**
: File format for serialization and storage of an annotation schema. ASAM OpenLABEL uses JSON schema as annotation schema format.


**Knowledge repository**
: Database that stores, organizes, and categorizes knowledge. In the context of ASAM OpenLABEL, knowledge repositories organize, structure, and define domain concepts relevant to the annotation task, for example, the road traffic domain. Knowledge repositories may be defined, for example, as free texts, structured taxonomies, or formal ontologies.


**Labeling**
: Process for generating spatiotemporal descriptions for data, using labeling geometries and other constructs to provide richer information compared to tags.


> **NOTE**: Labeling is a specialization of Annotation.


**Labeling geometries**
: Spatiotemporal constructs used to identify, isolate, and localize specific semantic concepts to be annotated in the raw data, for example, bounding boxes, cuboids, and others.


**LiDAR (Light Detection and Ranging)**
: Restricted term: LIDAR Method for measuring distances by illuminating the target with laser light and measuring the reflection with a sensor.


**ODD (Operational Design Domain)**
: Source: SAE J3016 (2021) [12] Operating conditions under which a given driving automation system or feature thereof is specifically designed to function, including, but not limited to, environmental, geographical, and time-of-day restrictions, and/or the requisite presence or absence of certain traffic or roadway characteristics.


**Ontology**
: Formal, explicit specification of a shared conceptualization. Ontologies may be defined in formal knowledge representation languages. In the context of ASAM OpenLABEL, an ontology is a machine-readable artifact that organizes and defines semantic concepts relevant to the labeling tasks.


**Radar (Radio Detection and Ranging)**
: Restricted term: RADAR Device or system that consists of a synchronized radio transmitter and receiver that emits radio waves and processes their reflections for display. A radar is used especially for detecting and locating objects.


**Raw data**
: Data that can be enriched with metadata. Raw data may take many forms, for example, individual files, file streams, or test scenarios artifacts. Relevant examples of raw data for ASAM OpenLABEL are png images, frames in a video sequence, pcd point clouds, OpenSCENARIO files, and OpenLABEL files themselves.


**Tagging**
: Process for adding simple and complex semantic tags to any information container, such as images, videos, or test scenarios. Tagging is a specialization of the annotation process.


**Test scenario**
: Scenario intended for testing and assessment of Advanced Driver Assistance Systems (ADAS) and system under test.
