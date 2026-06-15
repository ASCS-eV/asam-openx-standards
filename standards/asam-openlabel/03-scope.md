# ASAM OpenLABEL v1.0.0 — 3. Scope

- **Source**: ASAM_OpenLABEL_BS_V1-0-0.html
- **Version**: v1.0.0
- **Date**: November 9, 2021
- **License**: Restricted distribution (ASAM e.V. member access)

---

## 3. Scope


ASAM OpenLABEL establishes the basic principles and methods for annotating multi-sensor data streams and for tagging test scenarios for automated driving development, validation, and verification.


The ASAM OpenLABEL standard


- specifies the annotation schema to which valid ASAM OpenLABEL annotation instances shall conform.
- represents the annotation schema for ASAM OpenLABEL in JSON schema. The JSON schema defines the structure, sequence, elements, and values of ASAM OpenLABEL.
- explains relationships between different elements in the ASAM OpenLABEL annotation schema, for example, actions, objects, events, contexts, relations, frames, tags.
- gives guidelines for using ASAM OpenLABEL.


This version of ASAM OpenLABEL does not discuss quality nor provide quality criteria related to annotations. Future versions of ASAM OpenLABEL may deal with this issue.


### 3.1. Multi-sensor data labeling


The ASAM OpenLABEL standard


- defines and organizes the annotation data structures, including geometries, coordinate systems and transforms, and other concepts relevant to spatiotemporal annotations for multi-sensor data labeling.
- does not provide a taxonomy/ontology of physical/abstract entities relevant to the road traffic domain. Instead, it specifies mechanisms to include external knowledge repositories/ontologies and recommends the use of ASAM OpenXOntology as the ontology of reference.
- does not provide rules, specifications, or guidelines on how to annotate entities for multi-sensor data labeling. Nor does it provide any recommendations as to what elements of a physical entity should be included or not included in a geometry.


> **NOTE**: An ASAM OpenLABEL multi-sensor data labeling instance shall follow the provided multi-sensor data labeling schema to be considered valid and compliant with ASAM OpenLABEL.


### 3.2. Scenario tagging


The ASAM OpenLABEL standard


- defines and organizes the annotation data structure for test scenario tagging.
- defines the set of ASAM OpenLABEL tags, their relationships, and the mechanisms to include the ASAM OpenLABEL set of scenario tags in valid annotation instances of test scenarios.
- does not define a language or format to describe test scenarios.


> **NOTE**: An ASAM OpenLABEL scenario tagging instance shall use the tagging schema and the set of tags provided in ASAM OpenLABEL to be considered valid and compliant with ASAM OpenLABEL.
