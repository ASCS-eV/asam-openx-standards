# ASAM OpenLABEL v1.0.0 — 6. Conceptual overview

- **Source**: ASAM_OpenLABEL_BS_V1-0-0.html
- **Version**: v1.0.0
- **Date**: November 9, 2021
- **License**: Restricted distribution (ASAM e.V. member access)

---

## 6. Conceptual overview


### 6.1. Data annotation in ASAM OpenLABEL


Data annotation is the process of enriching raw data, for example, data streams from multiple sensors, such as cameras, LiDAR, radar, or test scenario artifacts with additional metadata. These metadata are related to the content of the raw data, for example, static or dynamic objects populating a video, actions they are performing, or environmental conditions. Additional information regarding the data may also be included.

[Image: fig overview data annotation.drawio]

*Figure 2. Relevant concepts for data annotation*


Figure 2 shows the concept and terms related to data annotation.


Raw data is data that can be enriched with metadata. Raw data can take many forms, for example, individual files, file streams, or test scenario artifacts. Relevant examples of raw data for ASAM OpenLABEL are png images, frames in a video sequence, pcd point clouds, or OpenSCENARIO files.


Annotation instances enrich raw data with metadata required for the specific task. Annotation instances are usually serialized in a text-based file, for example, JSON. JSON is the format used for ASAM OpenLABEL. Annotation instances shall conform to a predefined *annotation schema*.


The annotation schema provides the specific structure and set of constraints that the annotation instances need to follow to be considered well-formed and valid. The definition of an annotation schema is the core of ASAM OpenLABEL. The annotation schema for ASAM OpenLABEL is represented as a JSON schema.


For applications with heavy semantic load, such as the use cases relevant for ASAM OpenLABEL, it is advisable to refer to external knowledge repositories, for example, ontologies or vocabularies. An annotation schema regulates the data validity of annotation instances providing its data model. Knowledge repositories can add value to this: They provide information about the content of the annotations and analyze the validity of the content. Such external resources organize, structure, and define the semantics of the entities that annotations are referring to. Ontologies additionally define the relationships between the entities. ASAM OpenLABEL assumes the use of external knowledge repositories to organize the semantic content of annotations.


ASAM OpenLABEL defines annotation schemas that are valid for specific use cases with specific raw data to be annotated. The two primary use cases considered for ASAM OpenLABEL are multi-sensor data labeling and scenario tagging.


#### 6.1.1. Multi-sensor data labeling

[Image: fig overview multi sensor data labeling.drawio]

*Figure 3. Multi-sensor data labeling concept*


Figure 3 shows the concepts related to data annotation as representation for multi-sensor data labeling. ASAM OpenLABEL covers the definition of the annotation schema for multi-sensor data labeling.


Multi-sensor data labeling use cases focus on raw data that is the output of multiple sensors, for example, cameras, LiDAR, or radar. These sensors equip typical advanced driver assistance systems (ADAS) and autonomous driving (AD) systems. The format of such raw data is often pcd, png, other common image formats, point cloud, or video formats.


For this type of raw data, there is lots of semantic content that has to be annotated. The annotations require geometries, for example, bounding boxes, polygons, or other primitives to isolate and localize relevant semantic concepts within the raw data. Semantically, labels usually refer to agents type identification, their relations, actions they are performing, and contexts in which these actions or agents take place or exist.


Additional information included in this annotation use case encompass details about spatial calibration across sensors, temporal synchronizations, coordinate transforms, and consistent entity IDs across frames and sensor streams.


_Example_

[Image: fig example multi sensor data labeling.drawio]

*Figure 4. Multi-sensor data labeling example*


Figure 4 shows an example using ASAM OpenLABEL for multi-sensor data labeling. The files `example.pcd`, `example.png` and `example.json` contain multiple raw sensor data streams that are annotated according to the ASAM OpenLABEL annotation schema. The ASAM OpenLABEL annotation schema is contained in the `openlabel_json_schema.json` file. The `example.json` file contains annotations of the `example.pcd`, `example.png` and `example.json` files. The annotations in the `example.json` file contain references to an external ontology in the `example.owl` file. The `example.json` file can be validated using the `openlabel_json_schema.json` file. The `example.owl` file is used to semantically enrich the annotations in the `example.json` file.


#### 6.1.2. Scenario tagging

[Image: fig overview scenario tagging.drawio]

*Figure 5. Scenario tagging concept*


Figure 5 shows the concepts related to data annotation as representation of scenario tagging. ASAM OpenLABEL covers the definition of the annotation schema for scenario tagging and an ontology for tags.


Scenario tagging use cases focus on raw data that is used in the development, testing, and validation process of ADAS and AD functions, for example, test scenarios or simulation scenarios. Often the format of such raw data is OpenSCENARIO, GEOscenario, M-SDL, or other domain specific languages or formats used to describe and store simulation and test scenarios.


> **NOTE**: In addition to the raw data types mentioned above, videos, natural language descriptions, or any other data that contains a visualization or a description of a driving situation evolving through time, and so even valid OpenLABEL annotation instances for multi-sensor data labeling, can be treated as relevant raw data for the scenario tagging use case.


Annotations for this type of data usually are not semantically dense, and consist of a set of tags that are associated with a specific (set of) scenario instance(s). Semantically, tags usually refer to elements related to the content of the scenario, such as its ODD, or the behavior of some agents.


Additional information included in this annotation use case encompass details about authorship, versioning, and other high-level administrative information related to the scenario.


_Example_

[Image: fig example scenario tagging.drawio]

*Figure 6. Scenario tagging example*


Figure 6 shows an example using ASAM OpenLABEL for tagging scenario files. The `example.xosc` file contains a scenario description that was annotated following the ASAM OpenLABEL annotation schema. The ASAM OpenLABEL annotation schema is contained in the `openlabel_json_schema.json` file. The annotations of the `example.xosc` file are contained in the `example.json` file. The annotations in the `example.json` file contain references to an external ontology in the `openlabel_ontology_scenario_tags.ttl` file. The `example.json` file can be validated using the `openlabel_json_schema.json` file. The `openlabel_ontology_scenario_tags.ttl` file is used to semantically enrich the annotations in the `example.json` file.


### 6.2. Annotation schema and its format


The annotation schema defines the structure of annotations, data types, and conventions needed to unambiguously interpret the annotations. It also specifies how the annotation data is encoded for storage into computer files.


The annotation schema of ASAM OpenLABEL is designed to be flexible enough to tackle annotation tasks, ranging from simple object-level labeling in single images, using, for example, bounding boxes or semantic segmentation, to complex multi-sensor data labeling tasks, involving, for example, cuboids, odometry, coordinate systems, and transforms. The annotation schema and its format (JSON schema) is also designed to facilitate serialization of labels in files or messages that can be stored and exchanged between computers and stay readable for humans at the same time.


#### 6.2.1. Annotation schema (JSON schema)


The annotation schema is described and formatted as a JavaScript Object Notation schema (JSON schema). It defines the shape against which valid JSON annotation instances should conform to. The structure of ASAM OpenLABEL annotation schema is serialized in the [ASAM OpenLABEL JSON schema file](https://openlabel.asam.net/V1-0-0/schema/openlabel_json_schema.json). The annotation schema itself conforms to the JSON schema Draft 7 specification [13].


There are several software packages in different programming languages that can be used to validate a JSON payload against the JSON schema. A JSON schema validation asserts constraints on the structure of the instance JSON data.


The JSON schema validation only inspects the structure and type of the key-value pairs. A JSON schema does not validate the semantics behind the content of key-value pairs. Certain level of semantic validation can be achieved by using external resources, such as the ontologies of ASAM OpenXOntology, reasoning engines, and validation scripts.


The annotation schema data structure of ASAM OpenLABEL represents annotations as a dictionary. Therefore, all data is represented as key-value pairs. These key-value pairs are sometimes referred to as items in certain programming languages. Keys are strings, that is, arrays of characters. Values can be the following:


- Primitives (string, number, and Boolean)
- Arrays of primitives
- Dictionaries
- null (A special type to denote the key exists but has no value.)


Keys, as strings, encode either keywords defined in the JSON schema, for example `object`, `coordinate_system`, `name`, `type`, or identifiers. Identifiers can be numerical, for example `0`, `5`, strings, for example `CAM`, `ODOM`, or unique identifiers, for example, `123e4567-e89b-12d3-a456-426614174000`. The JSON schema determines which pattern keys shall follow for different types of items, for example, regular expressions to determine that keys shall be string representations of numbers from 0 to 9.


This data structure matches with the syntax of JSON data formatting. As a consequence, ASAM OpenLABEL content can be expressed as JSON strings and made persistent as JSON files.


##### JSON payloads and files


Any ASAM OpenLABEL annotation instance can be expressed as JSON string payloads. That means the actual data pack that contains the key-value pairs is expressed as a string.


A JSON file, for example, `openlabel_annotation.json`, can be created by storing the JSON string payload using any computer programming language that serializes it into a text file. In ASAM OpenLABEL, UTF-8 (8-bit Unicode Transformation Format) shall be used as the encoding format of characters.


_JSON example_


```json
{
    "openlabel" : {
        "metadata" : {
            "schema_version" : "1.0.0"
        },
        "objects" : {
            "0" : {
                "name" : "object1",
                "type" : "car"
            },
            "1" : {
                "name" : "object2",
                "type" : "pedestrian"
            }
        }
    }
}
```


> **TIP**: JSON data can be shown clearly arranged using tabular spaces. Nevertheless, other representations are equally valid. They are preferred for reducing the size of the JSON files. See, for example, the above code: {"openlabel":{"metadata":{"schema_version":"1.0.0"},"objects":{"0":{"name":"object1","type":"car"},"1":{"name":"object2","type":"pedestrian"}}}}


##### JSON parsers


Any JSON parser application, package, and programming language can be used to interpret (parse) the content.


Example languages and libraries supporting reading and writing JSON data and validating the JSON schema are, for example, Python, Typescript/JavaScript, and C++.


It is out of the scope of this standard to define reference implementations of parsers to load and save JSON data compliant with the JSON schema.


##### Other encoding formats


The ASAM OpenLABEL format matches the syntax of JSON. It was originally developed using the JSON schema as the main pillar to define the structure. Therefore, this version of ASAM OpenLABEL enforces the utilization of JSON as an annotation and file format.


Nevertheless, other encoding formats may be considered for future versions of ASAM OpenLABEL as long as they satisfy the same structure, type, and constraints requirements defined by the JSON schema.


#### 6.2.2. Structure

[Image: fig openlabel format highlevel.drawio]

*Figure 7. ASAM OpenLABEL high-level annotation structure*


Figure 7 shows the high-level structure of the ASAM OpenLABEL annotation schema. ASAM OpenLABEL can be used for labeling and tagging.


Labeling focuses on producing spatiotemporal descriptive information of data, such as images. Objects, actions, events, contexts, and relations provide flexibility and complex labels.


Tagging aims to provide mechanisms to add simple and complex tags to any content, such as images, data files, or scenarios.


Additional structures provide details for metadata, ontologies, frames, and coordinate systems.


The following list shows all objects used in ASAM OpenLABEL.


_JSON schema_


```json
{
    "openlabel" : {
        "properties": {
            "actions": {...},
            "contexts": {...},
            "coordinate_systems": {...},
            "events": {...},
            "frame_intervals": {...},
            "frames": {...},
            "metadata": {...},
            "objects": {...},
            "ontologies": {...},
            "relations": {...},
            "resources": {...},
            "streams": {...},
            "tags": {...}
            }
        }
    }
}
```


The annotation schema format is represented in the ASAM OpenLABEL JSON schema. The main object is the `openlabel` object. It contains the basic objects used in ASAM OpenLABEL. Some objects are utilized in both multi-sensor data labeling and scenario tagging use cases, for example, the `metadata` and `ontologies` objects. Some other objects are exclusively used in one and not the other of the two use cases.


The following list shows all objects used in the domain of multi-sensor data labeling.


_JSON schema_


```json
{
    "openlabel" : {
        "properties": {
            "actions": {...},
            "contexts": {...},
            "coordinate_systems": {...},
            "events": {...},
            "frame_intervals": {...},
            "frames": {...},
            "metadata": {...},
            "objects": {...},
            "ontologies": {...},
            "relations": {...},
            "resources": {...},
            "streams": {...}
        }
    }
}
```


The following list shows all objects used in the domain of scenario tagging.


_JSON schema_


```json
{
    "openlabel" : {
        "properties": {
            "metadata": {...},
            "ontologies": {...},
            "tags": {...}
        }
    }
}
```


The specific annotation schema for multi-sensor data labeling and scenario tagging, including detailed descriptions of each object, can be found in each corresponding section.


_Related topics_


- Multi-sensor data labeling
- Scenario tagging


### 6.3. Metadata


In ASAM OpenLABEL, metadata is understood as additional information about the labels and the content to be labeled. Examples for metadata are the ASAM OpenLABEL version used, file version, authorship, or any other custom information.


The information inside `metadata` shall be used for informative purposes by applications or humans managing ASAM OpenLABEL files.


_Class_


```
metadata
```


This JSON object contains information, that is, metadata, about the annotation file itself.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 8. Diagram of the metadata class*


*Table 5. Properties of the metadata class*

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| annotator | string |  | Name or description of the annotator that created the annotations. |
| comment | string |  | Additional information or description about the annotation content. |
| file_version | string |  | Version number of the OpenLABEL annotation content. |
| name | string |  | Name of the OpenLABEL annotation content. |
| schema_version | string | true | Version number of the OpenLABEL schema this annotation JSON object follows. |
| tagged_file | string |  | File name or URI of the data file being tagged. |


### 6.4. Coordinate systems


> **NOTE**: This section contains concepts that are relevant for multi-sensor data labeling use cases.


A coordinate system is a system of numbers, that is designed as a way to uniquely determine the position of points over a manifold, such as the Euclidean space, for example, the 2D position of a pixel within an image, or the 3D position of a LiDAR return point in the world relative to the rear axle of the vehicle.


A coordinate transform or coordinate transformation is a relation that expresses the mapping from coordinates on one coordinate system to coordinates in another coordinate system. A coordinate transform always requires two coordinate systems containing the source and the target coordinate system.


Raw data to be annotated with ASAM OpenLABEL may contain multiple streams of sensor data coming from different exteroceptive and interoceptive sensors. This triggers the need to define multiple coordinate systems and several transforms that express the following:


- How data from different sensors are spatiotemporally related.
- How the labels relate to the sensor data.
- How the sensor data relates to the real world.


ASAM OpenLABEL defines mechanisms to represent information about coordinate systems and transforms in the annotation schema.


More specifically, coordinate systems and their transforms fulfill the need to express spatiotemporal relation for the following, non-exhaustive, set of use cases:


- Express how the labeled objects of interest are spatially located with respect to a GNSS/INS system, to map data, or to other sensors.
- Express how light rays generated intensity values.
- Express how LiDAR points are geolocated with respect to the world coordinates, vehicle coordinates, etc.
- Express the intrinsic calibration parameters of a camera sensor.
- Express the distortion coefficients from fish-eye camera lenses to rectified images.


To accommodate for all these and more potential use cases, the ASAM OpenLABEL standard provides a method to describe an arbitrary number of coordinate systems and a method to describe the transforms between those coordinate systems.


In addition, the ASAM OpenLABEL standard provides a way to describe transforms that are fixed over time, transforms that vary occasionally at specific time instants, frames, and transforms that vary continuously.


As specified in section Coordinate systems, users may define arbitrary names for coordinate systems. However, despite the ability to describe an arbitrary set of coordinate systems, a small set of names is reserved and refers to pre-defined coordinate systems specified in ASAM OpenLABEL as there are some coordinate systems that are commonly used in many systems and are standardized. The coordinate systems with standardized namespaces include:


- vehicle-iso8855
- odom
- map-UTM
- geographic-wgs84


Whenever these names are used for a coordinate system, they shall have the meaning defined in the related standard.

[Image: fig coordinate systems with heading pitch roll]

*Figure 9. Coordinate systems with heading, pitch, and roll*


- vehicle-iso8855 A right-handed coordinate system with the origin at the center of the rear axle projected down to ground level. Note that the origin is attached to the rigid body of the vehicle and not to an axle suspended between it and the body. It is at ground level when the vehicle is nominally loaded but it may be above or below ground level, depending on the actual load. Similarly, the axis pointing forward may point slightly upwards or downwards relative to ground level depending on the front to back loading of the vehicle. The x-axis is forward, the y-axis to the left, and the z-axis upwards. See also the ISO 8855 specification [11].

[Image: 600]

*Figure 10. Vehicle coordinate system, ISO 8855*


- odom A 3D cartesian coordinate system that is approximately fixed in the world. The transform between the vehicle-iso8855 coordinate system and odom is guaranteed to be continuous so that it varies smoothly over time.


> **NOTE**: The transform between odom and map-UTM may be discontinuous. That means there may be sudden jumps in the value of the transform. The odom origin is often the starting point of the vehicle at the time the system is switched on. See the ROS documentation [14].


- map-UTM A 3D cartesian coordinate system useful for mapping moderately sized regions of the Earth. It is locked to the Earth and is a set of slices of flat coordinates that cover the Earth. See the UTM specification [15].
- geospatial-wgs84 A 3D ellipsoidal coordinate system used for GNSS systems, meaning latitude, longitude, and altitude. It is fixed to the Earth, which means that it ignores, for example, continental drift, and covers the entire Earth.


For common use cases, there may be several sets of coordinate systems (blue boxes) and transforms between them that are commonly used, as the following diagrams show.

[Image: fig transform much.drawio]

*Figure 11. Example of a transform of a multi-sensor setup into a geospatial coordinate system*


Figure 11 shows an example of a Robot Operating System (ROS) based system.


The sensors described in the example system in the introduction might have the following coordinate systems and transform tree.

[Image: fig transform mid.drawio]

*Figure 12. Example of a transform of a camera and GPS sensor setup into a geospatial coordinate system*


Figure 12 shows how a set of data captured from a dash-cam, a single camera including a GPS, might look like.

[Image: fig transform low.drawio]

*Figure 13. Example of a transform of a camera setup into a odom coordinate system*


Figure 13 shows how a single camera with no other data, with the movement of the camera deduced by structure from motion, might look like.


_Related topics_


- Coordinate Systems schema


### 6.5. Semantic segmentation


Semantic image segmentation, also called pixel-level classification, is the task of clustering those parts of an image together which belong to the same object class. Technically, it means assigning to each pixel a value/code corresponding to a certain class of interest (object/entity category).


The semantic segmentation task treats objects as stuff, which is amorphous and uncountable. Multiple objects of the same class are treated as a single entity. Thus, no information exists about specific instances of a class. Cars are all assigned a color code, for example blue, and are treated as being part of the same amorphous "car stuff".


Semantic segmentation annotations follow the form of the objects and have no fixed shape. Manually, this is usually achieved by drawing refined polygons around the regions of interest, or by painting the region of interest through a paintbrush-like feature. The result is a precise mask that isolates only the object of interest and no surrounding pixels.


In the 2D annotation space this method provides the highest accuracy of the objects. However, this comes at an increased cost in comparison with other annotation methods. Furthermore, segmentations take up more time during the labeling process than other 2D annotation methods and thus have lower throughput.


> **NOTE**: This section contains concepts that are relevant for multi-sensor data labeling use cases.


#### 6.5.1. Formal definition


Formally, semantic segmentation can be defined as follows:


Let \(P={p_{1}, p_{2}, ... p_{p}}\) be the set of all the pixels in a given frame, for example, an image.


Then, the cardinality \(|P|\) is equal to the number of pixels in such a frame.


Let \(C={c_{1}, c_{2}, ... c_{c}}\) be the set of all the classes that are defined for a labeling task, for example, \(c_1=car, c_2=pedestrian\).


Then, the cardinality \(|C|\) is equal to the number of classes that are defined for such a task.


To perform semantic segmentation labeling on an image, it means establishing a relation that is valid when a pixel \(p_{x}\) represents a portion of an object belonging to one of the defined classes \(c_{y}\).


\(R_{seg}\) can be defined as a relation between the sets \(P\) and \(C\). Formally, this means defining a subset of the cartesian product \(R_{seg} \subset P \times C\), where \(P \times C = { (p_{1},c_{1}), (p_{1},c_{2}), ... (p_{n},c_{m}) }\)


Let \(D \subseteq P\) be the domain of the semantic segmentation relation \(R_{seg}\), the following taxonomy is produced:


**Semantic segmentation taxonomy**


- Partial scene segmentation when \(\exists p_{x} \in P: (p_{x}, c_{y}) \notin R_{seg}\). There are some pixels that have no classes associated with them. In this case \(D \subset P\).
- Full scene segmentation when \(\forall p_{x} \in P, \exists c_{y} \in C : (p_{x},c_{y}) \in R_{seg}\). All pixels have a class associated. In this case \(D\) coincides with \(P\). Note that in the use case, despite the class unlabeled or other indicating all pixels outside of the real classes of interest, there is still a form of full scene segmentation performed.
- Single-class per pixel segmentation when \(\forall p_{x} \in D, \exists! c_{y} \in C: (p_{x},c_{y}) \in R_{seg}\). This is the case when each labeled pixel is associated with exactly one class.
- Multi-class per pixel segmentation when \(\exists p_{x} \in D, \exists c_{1}, c_{2}... c_{k} \in C: (p_{x},c_{1}), (p_{x},c_{2}), ...(p_x,c_{k}) \in R_{seg}\). This is the case when at least one labeled pixel is associated with more than one class.


#### 6.5.2. Instance segmentation


Instance segmentation enriches the semantic segmentation information, adding a separation among specific different instances of objects belonging to a class. This method is used to separate *stuff* into individual, countable *things*. Semantic classes can be either things (objects with a well-defined shape, for example a car, a person) or stuff (amorphous background regions, for example grass, sky). In contrast with semantic segmentation task, where each pixel belongs to a set of predefined classes, in instance segmentation the number of instances is not known before.


**Formal definition**


Formally, instance segmentation can be defined as an extension of semantic segmentation as follows:


- Let \(I={i_{1}, i_{2}, ...i_{n}}\) be the set of all the instances of countable objects in the scene (image).
- Then the cardinality of the set \(|I|\) is equal to the total number of object instances that populate the scene.
- To perform instance segmentation labeling on an image, it means establishing a ternary relation \(I_{seg} \in P \times C \times I\) that is valid when a pixel \(p_{x}\) represents a portion of an object belonging to one of the defined classes \(c_{y}\) and to a specific object instance \(i_{z}\). \(P \times C \times I = { (p_{1},c_{1},i_{1}), (p_{1},c_{1},i_{2}), ... (p_{n},c_{m},i_{l}) }\)


> **NOTE**: Instance awareness may be added to any kind of semantic segmentation described before by extending the relation to an additional instance set.


Let \(D_{in} \subseteq P\) be the domain of the instance segmentation relation \(I_{seg}\).


- Instance unique segmentation when \(\forall p_{x} \in D_{in}, \exists! c_{y} \in C, \exists! i_{z} \in I: (p_{x},c_{y},i_{z}) \in I_{seg}\). This is the case when each labeled pixel is associated with exactly one class and exactly one instance of that class.
- Multi-class multi-instance segmentation when \(\exists p_{x} \in D_{in}, \exists c_{1},c_{2}, ... c_{c} \in C, \exists i_{1},i_{2},... i_{i} \in I : (p_{x},c_{1},i_{1}),(p_{x},c_{1},i_{2})... (p_{x},c_{c},i_{i}) \in I_{seg}\). This is the case when each labeled pixel may be associated with more than one class and with more than one instance of those classes.


> **NOTE**: Starting from this general definition, all possible particular cases, permutations, or ways to construct semantic and instance segmentation labeling can be covered.


_Related topics_


- Semantic segmentation schema
- Semantic segmentation examples
