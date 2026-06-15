# ASAM OpenLABEL v1.0.0 — 7. Multi-sensor data labeling

- **Source**: ASAM_OpenLABEL_BS_V1-0-0.html
- **Version**: v1.0.0
- **Date**: November 9, 2021
- **License**: Restricted distribution (ASAM e.V. member access)

---

## 7. Multi-sensor data labeling


### 7.1. Introduction


Multi-sensor data labeling is the process of enriching data streams with information on the location and the characteristics of labeled objects or the entire scenario at a given point in time.


Labels summarize relevant semantic entities and show their spatiotemporal location within the data through spatiotemporal constructs, such as labeling geometries. There are different types of labeling geometries. Each type provides a suitable input representation for specific computer vision and machine-learning tasks.


This chapter covers multi-sensor data labeling in detail, including the following topics:


- List the raw data considered relevant for the multi-sensor data labeling use case.
- Introduce and describe in detail the annotation schema, its structure, elements, and the different ways of expressing labeling geometries, coordinate systems, transforms, and other information relevant for multi-sensor data labeling.
- Describe the mechanisms that govern the reference to external knowledge repositories, such as ontologies, that organize and define the semantics of the labels.
- Supported data types and their representation.
- Provide examples that show how to utilize the schema to produce valid annotation instances in relevant specific cases.


_Related deliverables_


- openlabel_json_schema.json


_Related topics_


- Introduction
- Scope
- Conceptual overview


#### 7.1.1. Raw data sources for multi-sensor data labeling


Examples for raw data sources:


- Images
- Videos
- Point clouds


### 7.2. Annotation schema


The annotation schema defines the structure of annotations, data types, and conventions needed to unambiguously interpret the annotations. The annotation data format specifies how the annotation data is encoded for storage in computer files.


The annotation schema is described and formatted as a JSON schema. It defines the shape which valid JSON annotation instances shall conform to. The structure of the ASAM OpenLABEL annotation schema is serialized in the [ASAM OpenLABEL JSON schema file](https://openlabel.asam.net/V1-0-0/schema/openlabel_json_schema.json). The annotation schema itself conforms to the JSON schema Draft 7 specification [13].


The annotation schema of ASAM OpenLABEL addresses the following general features related to multi-sensor data labeling:


- Labeling different spatiotemporal objects.
- Static and dynamic (time) properties of objects.
- Geometric and non-geometric attributes for objects.
- Nested attributes.
- Management of coordinate systems, odometry and sensor configuration.
- Multi-source (sensor) annotations for objects.
- Persistent identities of objects through time.
- Linkage to ontologies and external resources.
- Relations between elements, for example, object performs action.
- Different type of elements: objects, actions, events, and contexts.
- Customizable and optional fields.


The annotation schema defines three main characteristic aspects of annotation data:


- Structure: How data is organized, using hierarchies and key-value dictionaries.
- Types: Primitive data types for key-value items.
- Conventions: Documented interpretation of data values.


The annotation schema for multi-sensor data labeling follows the same principles of the annotation schema for scenario tagging, meaning JSON and JSON schema, as described in chapter Scenario tagging.


### 7.3. Structure


The ASAM OpenLABEL annotation schema for multi-sensor data labeling is structured as a dictionary and can be described from top to bottom. This section contains diagrams intended to visualize the structure. The details of the structure can all be consulted at the ASAM OpenLABEL JSON schema file.


Any ASAM OpenLABEL JSON data shall have a root key named `openlabel.` Its value is a dictionary containing the rest of the structure as described in the next sections. The version of the schema shall be defined inside the `metadata` structure, using the key `schema_version`. All other entries are optional.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        }
    }
}
```


The following example shows a JSON payload corresponding to the first level items inside the root `openlabel` value, which are related to multi-sensor data labeling.


_JSON example_


```json
{
    "openlabel": {
        "objects": { ... },
        "actions": { ... },
        "events": { ... },
        "contexts": { ... },
        "relations": { ... },
        "frames": { ... },
        "frame_intervals": { ... },
        "metadata": { ... },
        "ontologies": { ... },
        "resources": { ... },
        "coordinate_systems": { ... },
        "streams": { ... }
    }
}
```


For multi-sensor data labeling, the ASAM OpenLABEL structure defines dictionaries for the elements, meaning `objects`, `actions`, `events`, `contexts`, and `relations`. Each entry of the dictionary is a key-value pair where the key is a unique identifier of the element, for example, an `object`. The value is the container of static information.


Supporting structures define the following:


- ontologies that are used.
- External resources to enable linked data.
- coordinate_systems to explicitly specify how to transform data.
- streams which contain information on the data being labeled, for example, sensor information, such as intrinsic calibration parameters of cameras.


In case time-information is needed, for example, for labeling video sequences, the item `frames` contains a dictionary of containers at frame level. `frame_intervals` summarize the frame intervals that contain information for this ASAM OpenLABEL annotation file.

[Image: fig openlabel format labeling.drawio]

*Figure 14. ASAM OpenLABEL labeling structure*


Figure 14 shows the ASAM OpenLABEL data structure for multi-sensor data labeling.

[Image: fig openlabel format frames.drawio]

*Figure 15. ASAM OpenLABEL frame structure*


Figure 15 shows the structure of the `frame` value. Its structure is similar to the `openlabel` value as it contains dictionaries for the elements, meaning `objects`, `actions`, `events`, `contexts`, and `relations`. Only the dynamic information inside them is detailed.


In addition, `frame_properties` may contain information about timestamping details, or transforms of specific coordinate systems and other stream properties.


Annotation data is stored as element data, for example, `object_data`, which each element may contain in the form of arrays of structures, organized per data type.

[Image: fig openlabel format attributes generic.drawio]

*Figure 16. ASAM OpenLABEL attributes*


Figure 16 shows the structure of generic attributes (see Data types (generic)).

[Image: fig openlabel format attributes geometric.drawio]

*Figure 17. ASAM OpenLABEL geometric attributes*


Figure 17 shows the structure of the geometric attributes (see Data types (geometric)).


### 7.4. Elements


`objects`, `actions`, `events`, `contexts`, and `relations` are elements. These structures share similar properties in terms of attributes, types, and hierarchies.


- objects: A structure to represent information about physical entities in scenes. Examples of objects are pedestrians, cars, the ego-vehicle, traffic signs, lane markings, building, and trees.
- actions: A description of semantically meaningful acts being done. They may be defined for several frame intervals, similar to objects, for example, isWalking.
- events: Instants in time which have semantic load. events may trigger other events or actions, for example, startsWalking.
- contexts: Other descriptive information about the scene that contains no spatial or temporal information and therefore is not targeted by actions or events, for example: properties of the scene, such as Urban or Highway. weather conditions, such as Sunny or Cloudy. general information about the location, such as Germany or Spain.


_Attributes_


- uid: A unique identifier that determines the identity of the element. It can be a simple unsigned integer (from 0 upwards, for example 0) or a Universal Unique Identifier (UUID) of 32 hexadecimal characters, for example 123e4567-e89b-12d3-a456-426614174000. uid may not be sequential nor start at 0, which is useful for preserving identifiers from other label files.
- name: A friendly identifier of the element, is not unique but employed by human users to rapidly identify elements in the scene, for example, Peter.
- type: A semantic type of the element. It determines which class the element belongs to, for example, Car, Running, see Ontologies.


Optionally, elements may also have the following items:


- ontology_uid: A string identifier of the ontology which contains the definition of the type of the element (see Ontologies).
- Element data, for example object_data: Container of static information about the object (see Data types (geometric)).
- Element data pointers, for example, object_data_pointers: Pointers to element data at frames (see Frames).
- frame_intervals: An array of frame intervals where the element exists.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "objects": {
            "0": {
                "name": "car1",
                "type": "Car"
            }
        }
    }
}
```


The example shows a sample `object` with the mandatory items `name` and `type`.


> **NOTE**: JSON only permits keys to be strings. Therefore, the integer unique identifiers shall be stringified: 0. However, carefully written APIs can parse JSON strings into integers for better access efficiency and sorting capabilities.


_Rules_


- All elements shall have a uid as key.
- The uid shall be unique for each element type.
- Each element type (action, object, event, context, and relation) may have its own list of unique identifiers.
- All elements shall have a type.
- All elements shall have a name. The entry can be left empty as they are not used to index the elements.


#### 7.4.1. Element data


The main mechanism to add information about an element is to define element data, using the data types defined in Data types (geometric). Element data can be added statically or dynamically.


_Rules_


- Static element data shall be added at the element value, under the corresponding key, for example, object_data. Static element data specifies the type of data used, for example, bbox or vec, which becomes the key for an array of such data types in order to have one or more of those data types.


_JSON example_


```json
{
   "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "objects": {
           "0": {
               "name": "pedestrian1",
               "type": "Pedestrian",
               "object_data": {
                   "bbox" : [{
                            "name" : "body",
                            "val" : [303.73, 935.58, 135.62, 330.88]
                        }, {
                            "name" : "head",
                            "val" : [289.93, 814.08, 38.20, 39.96]
                        }
					]
               }
           }
       }
   }
}
```


The example shows a single `object` of type `Pedestrian` with two `bbox` items, one to describe the `body` and the other for the `head`.


_Rules_


- Dynamic element data shall be added similarly, but inside the corresponding frame (see Frames).
- Element data may be nested inside other element data as attributes.


> **NOTE**: Only non-geometrical element data types can be nested (see Data types (geometric)).


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "objects": {
            "0": {
               "name": "car1",
               "type": "Car",
               "object_data": {
                   "bbox" : [{
                            "name" : "shape",
                            "val" : [100, 100, 500, 300],
                            "attributes": {
                                "boolean": [{
                                        "name": "visible",
                                        "val": true
                                    },
                                    {
                                        "name": "interpolated",
                                        "val": false
                                    }
                                ]
                            }
                        }
					]
                }
            }
        }
    }
}
```


The example shows `string` and `num` attributes added to a `bbox`.


> **NOTE**: Attributes are nested just like any other element data and therefore can contain arrays of element data, indexed by type.


#### 7.4.2. Universal Unique Identifiers (UUID)


UUIDs in this specification are derived by using RFC 4122 [16].


When using UUIDs, the keys are substituted by 32 hexadecimal character strings.


_JSON example_


```json
{
   "openlabel": {
       "metadata": {
            "schema_version": "1.0.0"
        },
        "objects": {
           "c44c1fc2-ee48-4b17-a20e-829de9be1141": {
               "name": "van1",
               "type": "Van"
           }
       }
   }
}
```


The example shows that the key identifier of an `object` is a string containing 32 hexadecimal characters following the UUID convention.


### 7.5. Frames


In `frames` all dynamic (temporal) information of the annotations shall be specified at frame level. Each frame is indexed within the ASAM OpenLABEL JSON data with an integer number.


The frame number is a ASAM OpenLABEL identifier of a certain instant in time. Properties of the frame can be specified to match specific timestamps or frame indexes in video sequences (see Frame properties).


> **NOTE**: In multi-stream annotation data, a frame may represent several time instants as sensor data might not be perfectly aligned (see Synchronization).


_Class_


```
frame
```


A frame is a container of dynamic, timewise, information.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 18. Diagram of the frame class*


*Table 6. Properties of the frame class*

| Name | Type | Additional properties | Reference | Description |
| --- | --- | --- | --- | --- |
| actions | object | false | #/definitions/action_data | This is a JSON object that contains dynamic information on OpenLABEL actions. Action keys are strings containing numerical UIDs or 32 bytes UUIDs. Action values may contain an "action_data" JSON object. |
| contexts | object | false | #/definitions/context_data | This is a JSON object that contains dynamic information on OpenLABEL contexts. Context keys are strings containing numerical UIDs or 32 bytes UUIDs. Context values may contain a "context_data" JSON object. |
| events | object | false | #/definitions/event_data | This is a JSON object that contains dynamic information on OpenLABEL events. Event keys are strings containing numerical UIDs or 32 bytes UUIDs. Event values may contain an "event_data" JSON object. |
| frame_properties | object | true | #/definitions/stream | This is a JSON object which contains information about this frame. |
| objects | object | false | #/definitions/object_data | This is a JSON object that contains dynamic information on OpenLABEL objects. Object keys are strings containing numerical UIDs or 32 bytes UUIDs. Object values may contain an "object_data" JSON object. |
| relations | object | false |  | This is a JSON object that contains dynamic information of OpenLABEL relations. Relation keys are strings containing numerical UIDs or 32 bytes UUIDs. Relation values are empty. The presence of a key-value relation pair indicates the specified relation exists in this frame. |


#### 7.5.1. Frame intervals


The `frame_intervals` key defines the array of frame intervals for which the ASAM OpenLABEL JSON data contains information.


_Class_


```
frame_interval
```


A frame interval defines a starting and ending frame number as a closed interval. That means the interval includes the limit frame numbers.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 19. Diagram of the frame interval class*


*Table 7. Properties of the frame interval class*

| Name | Type | Description |
| --- | --- | --- |
| frame_end | integer | Ending frame number of the interval. |
| frame_start | integer | Initial frame number of the interval. |


_JSON example_


```json
{
   "openlabel": {
       "metadata": {
            "schema_version": "1.0.0"
        },
        "frame_intervals": [{
                "frame_start": 0, "frame_end": 1
            }, {
                "frame_start": 5, "frame_end": 7
            }
        ],
        "frames": {
            "0": { ... },
            "1": { ... },
            "5": { ... },
            "6": { ... },
            "7": { ... }
        }
    }
}
```


The example shows `frames` indexed as `0`, `1`, `5`, `6`, and `7`. The `frame_intervals` show the corresponding two intervals.


> **NOTE**: Frame intervals are also properties of elements, specifying the periods of time where the element exists or has data. Using several frame intervals makes it possible to explicitly declare time gaps where the element disappears or does not exist, while maintaining the same uid.


Inside each `frame`, dynamic information about elements may be included, using the same structure defined for elements.


_JSON example_


```json
{
   "openlabel": {
       "metadata": {
            "schema_version": "1.0.0"
        },
       "frames": {
           "0": {
               "objects": {
                   "1": {}
               }
           },
           "1": {
               "objects": {
                   "1": {}
               }
           }
       },
       "objects": {
           "1": {
               "name": "van1",
               "type": "Van",
               "frame_intervals": [{"frame_start": 0, "frame_end": 1}]
           }
       }
   }
}
```


The example shows an `object` which exists in frames `0` and `1` but has no specific information at those frames.


If the specific information of the `object` for a given frame is nothing but its existence, then the `object` information at such frame is just a pointer to its unique identifier, as shown in the example above.


When frame-specific information is added, it is enclosed as `object_data` inside the corresponding frame and `object` (see Element data).


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "frames": {
            "0": {
                "objects": {
                    "1": {
                        "object_data": {
                            "bbox": [{
                                   "name": "shape",
                                   "val": [12, 867, 600, 460]
                                }
                            ]
                        }
                    }
                }
            },
            "1": { ... }
        },
        "objects": {
            "1": {
                "name": "van1",
                "type": "Van",
                "frame_intervals": [{"frame_start": 0, "frame_end": 1}]
            }
        }
    }
}
```


The example shows an `object` which exists in `frames` `0` and `1`. The `object` has specific geometric information, for example, a `bbox` named `shape` at frame 0.


#### 7.5.2. Element data pointers


Since element data is not indexed by integer unique identifiers, such as elements, the structure defines a mechanism to have an index over each element data by adding element data pointers. For example, `object_data_pointers` within an `object` contain key-value pairs to identify which `object_data` names are used and which are their associated `frame_intervals`.


_Class_


```
element_data_pointers
```


This is a JSON object which contains OpenLABEL element data pointers. Element data pointer keys shall be the "name" of the element data this pointer points to.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 20. Diagram of the element data pointers class*


_JSON example_


```json
{
   "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "objects": {
           "0": {
               "name": "car0",
               "type": "car",
               "frame_intervals": [{"frame_start": 0, "frame_end": 10}],
               "object_data": {
                   "text": [{
                           "name": "color",
                           "val": "blue"
                       }
                   ],
                },
                "object_data_pointers": {
                    "color": {
                        "type": "text",
                    },
                    "shape": {
                        "type": "bbox",
                        "frame_intervals": [{"frame_start": 0, "frame_end": 10}],
                        "attributes": {
                            "visible": "boolean"
                        }
                    }
                }
            }
        },
        "frames": {
            "0": { ... },
            ...
            "10": { ... }
        }
        ...
    }
}
```


The example shows that the pointers may refer to static (frame-less, `color` attribute) and dynamic (frame-specific, `shape` attribute) `object_data` and also contains information about the nested attributes (`visible` attribute of `shape`).


This feature is useful for rapidly retrieving element data information from the ASAM OpenLABEL JSON data, without the need to explore the entire set of frames.


#### 7.5.3. Frame properties


Frame properties may include three types of details about the frame:


- timestamp: A relative or absolute time reference that specifies the time instant this frame corresponds to.
- streams (see Streams): Sensors may have dynamic properties for a certain specific instant, such as intrinsic calibration data or sync details (see Synchronization).
- transforms: Coordinate systems may have changed their relative position with respect to parent coordinate systems for specific frames (see Coordinate Systems and Transforms).


_Class_


```
frame
```


A frame is a container of dynamic, timewise, information.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 21. Diagram of the frame class*


*Table 8. Properties of the frame class*

| Name | Type | Additional properties | Reference | Description |
| --- | --- | --- | --- | --- |
| actions | object | false | #/definitions/action_data | This is a JSON object that contains dynamic information on OpenLABEL actions. Action keys are strings containing numerical UIDs or 32 bytes UUIDs. Action values may contain an "action_data" JSON object. |
| contexts | object | false | #/definitions/context_data | This is a JSON object that contains dynamic information on OpenLABEL contexts. Context keys are strings containing numerical UIDs or 32 bytes UUIDs. Context values may contain a "context_data" JSON object. |
| events | object | false | #/definitions/event_data | This is a JSON object that contains dynamic information on OpenLABEL events. Event keys are strings containing numerical UIDs or 32 bytes UUIDs. Event values may contain an "event_data" JSON object. |
| frame_properties | object | true | #/definitions/stream | This is a JSON object which contains information about this frame. |
| objects | object | false | #/definitions/object_data | This is a JSON object that contains dynamic information on OpenLABEL objects. Object keys are strings containing numerical UIDs or 32 bytes UUIDs. Object values may contain an "object_data" JSON object. |
| relations | object | false |  | This is a JSON object that contains dynamic information of OpenLABEL relations. Relation keys are strings containing numerical UIDs or 32 bytes UUIDs. Relation values are empty. The presence of a key-value relation pair indicates the specified relation exists in this frame. |


_JSON example_


```json
{
    "openlabel": {
        "frames": {
            "0": {
                "frame_properties": {
                    "timestamp": "2020-04-11 12:00:01",
                    "streams": {
                        "Camera1": {
                        "stream_properties": {
                            "intrinsics_pinhole": {
                                "camera_matrix_3x4": [ 1000.0,    0.0, 500.0, 0.0,
                                                            0.0, 1000.0, 500.0, 0.0,
                                                            0.0,    0.0,   0.0, 1.0],
                                    "distortion_coeffs_1xN": [],
                                    "height_px": 480,
                                    "width_px": 640
                            },
                            "sync": {
                                "frame_stream": 1,
                                "timestamp": "2020-04-11 12:00:02"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```


The example shows `frame_properties` of frame 0, containing information about a `timestamp` and some properties specific for frame 0 corresponding to stream `Camera1`.


> **NOTE**: The sync field within stream_properties defines the frame number of the stream that corresponds to this frame, along with timestamping information, if needed. This feature is useful for annotating multiple cameras which might not be perfectly aligned. In such cases, frame 0 of the ASAM OpenLABEL JSON data corresponds to frame 0 of the first stream to occur. In this way, frame_stream shall identify which frame of this stream corresponds to the frame in which it is enclosed.


#### 7.5.4. Synchronization


This section provides detail on the synchronization of multiple `streams` and their time information `frames`.


Labels can be produced to be related to specific streams, for example, cameras and LiDAR. When multiple streams of this type are present and labels need to be produced for several of them, for example, bounding boxes for images of the camera and cuboids for the point clouds of the LiDAR, a synchronization and matching strategy is needed.


In determining the synchronization of the data streams, for example, images and point clouds correspond to the data source set-up and not to the annotation stage. That means that the data container may contain precise HW timestamps for images and point clouds. In addition, the correspondence between frame indexes for multiple cameras, for example, frame `45` of camera `1`, corresponds because of proximity in time to frame `23` of camera `2` may be due to a different frequency they use or if they started with some delay.


Therefore, when producing labels for such different frames, the annotation format needs to allocate space and structure for such timing information. This shall be done in a way that all labels are easily associated with their corresponding data and time.


The JSON schema defines the `frame` data containers, which correspond to **master frame indexes**.


##### One stream


In many cases, there is a single stream of data that needs to be labeled, for example, an image sequence.


###### Simple case


The simplest use-case for a stream:


- Nothing needs to be specified, for example, sensor names or timestamps.
- Frame indexes are integers, starting from 0.
- master frame index coincides with stream-specific frames index. This means stream-specific frame index is not labeled.

[Image: fig streams one stream.drawio]

*Figure 22. One stream*


Figure 22 shows a simple timeline where `frames` represent discrete samples of time and are indexed using a **master frame index**.


_JSON example_


```json
{
    "openlabel": {
        "frames": {
            "0": { ... },
            "1": { ... }
        }
    }
}
```


The example shows the indexing approach in ASAM OpenLABEL where `frames` are indexed using an ordered numeric string, for example, `0` and `1`.


###### Stream frame index not coincident with master frame index


It is possible to define a specific frame numbering for **stream-specific frames** inside the **master frame index**, which always starts from 0. This means that these counts are non-coincident, and this reflects the fact that the stream indexes are discontinuous or start at a certain value.

[Image: fig streams one stream not coincident stream index and frame index.drawio]

*Figure 23. One stream (not coincident stream index and frame index)*


Figure 23 shows a simple timeline where the **master frame index** starts at `0` and corresponds to a specific frame index of a stream, starting at `45`.


_JSON example_


```json
{
    "openlabel": {
        "frames": {
            "5": {
                "frame_properties": {
                    "timestamp": "2020-04-11 12:00:01",
                    "streams": {
                        "Camera1": {
                            "stream_properties": {
                                "sync": { "frame_stream": 91}
                            }
                        }
                    }
                }
            }
        }
    }
}
```


The example shows how the **master frame index**, for example, `5`, can be linked to a **stream-specific frame index**, for example, `91`, using `stream_properties` inside `frame_properties`.


Other properties, such as timestamps, may be added for detailed timing information of each stream frame.

[Image: fig streams one stream with timestamps and other properties.drawio]

*Figure 24. One stream (with timestamps and other properties)*


Figure 24 shows a simple timeline with defined `frames` which span over a certain period of time, for example, corresponding to the exposure time of a camera.


_JSON example_


```json
{
    "openlabel": {
        "frames": {
            "0": {
                "frame_properties": {
                    "timestamp": "2020-04-11 12:00:01",
                    "aperture_time_us": "56"
                }
            }
        }
    }
}
```


The example shows how a certain frame may have customized `frame_properties`, such as `aperture_time_us`, to define the exposure time in microseconds.


##### Multiple streams


Complex labeling examples may include multiple streams, for example, labels that need to be defined for different sensors.


###### Same frequency and same start and indexes


The **master frame index** coincides with each of the stream indexes. It is fully synchronized.

[Image: fig streams several streams same frequency.drawio]

*Figure 25. Several steams (same frequency and same start and indexes)*


Figure 25 shows two timelines corresponding to two streams, `Camera1` and `Camera2`, with **stream-specific frame indexes** coinciding with the **master frame index**.


###### Same frequency and different start and indexes


It is possible to define **stream indexes** independently to reflect, for example, that one stream is delayed by one frame but still synchronized.

[Image: fig streams several streams same frequency different starts.drawio]

*Figure 26. Several streams (same frequency and different start and indexes)*


Figure 26 shows how two different timelines corresponding to two different streams can be shifted so the **stream-specific frame indexes** do not match with the **master frame index**. In the example, the **master frame index** = 1 corresponds to `Camera1` in frame 1 and `Camera2` in frame 80. Note, that in this example, for master frame = 0, there is no information about `Camera2` to represent that this stream started producing information after the stream of `Camera1`.


_JSON example_


```json
{
    "openlabel": {
        "frames": {
            "1": {
                "frame_properties": {
                    "timestamp": "2020-04-11 12:00:01",
                    "streams": {
                        "Camera1": {
                            "stream_properties": {
                                "sync": { "frame_stream": 1}
                            }
                        },
                        "Camera2": {
                            "stream_properties": {
                                "sync": { "frame_stream": 0}
                            }
                        }
                    }
                }
            }
        }
    }
}
```


The example shows how different **stream specific frame indexes** can be defined by a certain **master frame index** as `frame_properties`.


Other possible differences in synchronization, for example jitter, may be labeled by embedding timestamping information for each stream frame.

[Image: fig streams several streams jitter.drawio]

*Figure 27. Several streams containing jitter*


Figure 27 shows another use-case where frames do not follow a perfectly periodic sampling rate. This feature can be labeled, adding a jitter variable as a `frame_properties`.


###### Same frequency and constant shift


If the frame shift is constant, a more compact representation is possible by specifying the shift at root `stream_properties` rather than on each frame, as was shown in the previous examples:

[Image: fig streams several streams constant shift.drawio]

*Figure 28. Several streams (same frequency and constant shift)*


Figure 28 shows a specific case where the time shift between two streams (`Camera1` and `Camera2`) is constant and kept fixed for the entire scene.


_JSON example_


```json
{
    "openlabel": {
        "streams": {
            "Camera1": {
                "stream_properties": {
                    "sync": { "frame_stream": 0}
                }
            },
            "Camera2": {
                "stream_properties": {
                    "sync": { "frame_stream": 1}
                }
            }
        }
    }
}
```


The example shows how to represent a fixed time shift between a certain stream and the **master frame index** as `stream_properties` instead of as `frame_properties`. In the example, `Camera2` is shifted one frame ahead of the **master frame index**, while `Camera1` has shift 0.


###### Different frequency


Streams might represent data coming from sensors with different capturing frequency, for example, a camera at 30 Hz and a LiDAR at 10 Hz. Following the previous examples, it is possible to embed stream frames inside master frames so the frequency information is also included.

[Image: fig streams several streams different frequency.drawio]

*Figure 29. Several streams (different frequency)*


Figure 29 shows a typical configuration where the **master frame index** follows the fastest stream, in this case the `Camera1` stream.

[Image: fig streams several streams different frequency and type.drawio]

*Figure 30. Several streams (different frequency)*


Figure 30 shows a typical configuration where the **master frame index** follows the slowest stream, in this case the `Lidar1` stream.


##### Specifying coordinate system for each label


After defining the coordinate systems (see Coordinate Systems and Transforms) and the timing information, as shown in the examples above, labels for elements and element data may be declared for specific coordinate systems.


Coordinate systems of specific streams can be defined as well. In this way, for each image the information about labels, timings and coordinate systems are given together.


_JSON example_


```json
{
    "openlabel": {
        "frames": {
            "0": {
                "objects": {
                    "0": {
                        "object_data": {
                            "bbox": [
                                {
                                    "name": "shape2D",
                                    "val": [600, 500, 100, 200],
                                    "coordinate_system": "Camera1"
                                }
                            ],
                            "cuboid": [
                                {
                                    "name": "shape3D",
                                    "val": [ ... ],
                                    "coordinate_system": "Lidar1"
                                }
                            ]
                        }
                    }
                },
                "frame_properties": {
                    "streams": {
                        "Camera1": {
                            "stream_properties": {
                                "sync": { "frame_stream": 1, "timestamp": "2020-04-11 12:00:07"},
                            }
                        },
                        "Lidar1": {
                            "stream_properties": {
                                "sync": { "frame_stream": 0, "timestamp": "2020-04-11 12:00:10"}
                            }
                        }
                    }
                }
            }
        },
        "objects": {
            "0": {
                "name": "car1",
                "type": "car",
                "coordinate_system": "Camera1",
                ...
            }
        }
    }
}
```


The example shows that `objects` may be expressed with respect to a specific `coordinate_system`. For example, `objects` = 0 bounding box with the name `shape2D` is expressed with respect to the `Camera1` coordinate system. The cuboid with name `shape3D` is expressed with respect to the `Lidar1` coordinate system.


### 7.6. Streams


Complex scenes may be observed by several sensing devices, which produce multiple streams of data. Each of these streams might have different properties, for example, intrinsic calibration parameters and frequency. The ASAM OpenLABEL JSON schema defines the option to specify such information for a multi-sensor, and thus a multi-stream, which is set-up by allocating space for such stream-specific descriptions. In addition, it offers the ability to choose for each specific labeled element what stream they correspond to.


_Class_


```
streams
```


This is a JSON object which contains OpenLABEL streams. Stream keys can be any string, for example, a friendly stream name.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 31. Diagram of the streams class*


```
stream
```


A stream describes the source of a data sequence, usually a sensor.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 32. Diagram of the stream class*


*Table 9. Properties of the stream class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| description | string |  | Description of the stream. |
| stream_properties |  | #/definitions/stream_properties | Additional properties of the stream. |
| type | string |  | A string encoding the type of the stream. |
| uri | string |  | A string encoding the URI, for example, a URL, or file name, for example, a video file name, the stream corresponds to. |


_JSON example_


```json
{
   "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "streams": {
            "Camera1": {
                "type": "camera",
                "uri": "./some_path/some_video.mp4",
                "description": "Frontal camera",
                "stream_properties": {
                    "intrinsics_pinhole": {
                        "camera_matrix_3x4": [ 1000.0,    0.0, 500.0, 0.0,
                                                    0.0, 1000.0, 500.0, 0.0,
                                                    0.0,    0.0,   0.0, 1.0],
                        "distortion_coeffs_1xN": [],
                        "height_px": 480,
                        "width_px": 640
                    }
                }
            }
        }
    }
}
```


The example shows the item `streams`, which contains information about the streams that contain the data to be labeled. In the example, a stream with name `Camera1` is defined to be of `type` `camera` and to have some `stream_properties`, such as intrinsic calibration parameters.


### 7.7. Coordinate systems


A coordinate system is a numerical system to specify the coordinates of points and other geometric elements in a given space.


ASAM OpenLABEL defines mechanisms to represent labels which are often related to numerical properties of objects, such as position, size, or other physical magnitudes. Different coordinate systems may exist in arbitrary scenes that contain objects. Therefore, labels that represent numerical magnitudes of the objects need to be specified with respect to specific coordinate systems.


ASAM OpenLABEL has been devised to consider scenes as Euclidean spaces and right-handed Cartesian coordinate systems, where coordinates specify the distance from the origin along the specified axis. 2D and 3D coordinate systems are considered.


Points and other geometries expressed with respect to a particular coordinate system can be expressed with respect to another coordinate system using transformations between the coordinate systems.


Labels may be defined as relative to specific coordinate systems. This is particularly necessary for geometric labels, such as polygons, cuboids, or bounding boxes, which define magnitudes under a certain coordinate system. For example, a 2D line may be defined within the coordinate system of an image frame, and a 3D cuboid inside a 3D Cartesian coordinate system.


Coordinate systems shall be declared with a friendly name, used as an index, and in the form of parent-child links to establish their hierarchy:


- type: The type of coordinate system is defined so reading applications have a simplified view of the hierarchy: scene_cs, this corresponds to static coordinate systems. local_cs, this is a coordinate system of a rigid body, such as a vehicle, which carries with it the sensors. sensor_cs, a coordinate system attached to a sensor. custom_cs, any other coordinate system defined by the user.


> **NOTE**: type does not restrict the definition of complex coordinate system hierarchies. It is only intended to give a hint for parsing applications.


- parent: Each coordinate system can declare its parent coordinate system in the hierarchy.
- pose_wrt_parent: A default or static pose of this coordinate system with respect to the declared parent. It may be defined in several ways: 4x4 homogeneous matrix quaternion and translation Euler angles and translation


> **NOTE**: If not defined, the coordinate system is assumed to be exactly the same as its parent coordinate system.


- children: The list of children for this coordinate system.


In addition, as multiple coordinate systems may be defined, it is necessary to define mechanisms to declare how to convert values of magnitudes from one coordinate system to another. Therefore, **transforms** between two coordinate systems are also defined.


_Class_


```
coordinate_systems
```


This is a JSON object which contains OpenLABEL coordinate systems. Coordinate system keys can be any string, for example, a friendly coordinate system name.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 33. Diagram of the coordinate systems class*


```
coordinate_system
```


A coordinate system is a 3D reference frame. Spatial information on objects and their properties can be defined with respect to coordinate systems.


| Additional properties: | true |
| --- | --- |

[Image: Diagram]

*Figure 34. Diagram of the coordinate system class*


*Table 10. Properties of the coordinate system class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| children | array |  |  | List of children of this coordinate system. |
| parent | string | true |  | This is the string UID of the parent coordinate system this coordinate system is referring to. |
| pose_wrt_parent |  |  | #/definitions/transform_data | JSON object containing the transform data. |
| type | string | true |  | This is a string that describes the type of the coordinate system, for example, "local", "geo"). |


### 7.8. Transforms


A transform is a mathematical expression which determines how a coordinate system relates to another. In ASAM OpenLABEL, transforms are composed of a rotation and a translation component in 3D Euclidean space. Transformations are understood as passive and are thus equivalent to positions between coordinate systems. Different alternatives are supported:


- Quaternion and translation vector
- 4x4 Homogeneous matrix
- Vector of Euler angles with sequence code, and translation vector


_Class_


```
transform
```


This is a JSON object with information about this transform.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 35. Diagram of the transform class*


*Table 11. Properties of the transform class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| dst | string | true |  | The string UID, that is, the name, of the destination coordinate system for geometric data converted with this transform. |
| src | string | true |  | The string UID, that is, the name, of the source coordinate system of geometrical data this transform converts. |
| transform_src_to_dst |  | true | #/definitions/transform_data | JSON object containing the transform data. |


```
transform_data
```


JSON object containing the transform data.

[Image: Diagram]

*Figure 36. Diagram of the transform data class*


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "coordinate_systems": {
            "odom": {
                "type": "scene_cs",
                "parent": "",
                "children": [
                    "vehicle-iso8855"
                ]
            },
            "vehicle-iso8855": {
                "type": "local_cs",
                "parent": "odom",
                "children": [
                    "CAM_1",
                    "CAM_2"
                ]
            },
            "CAM_1" : {
				"type" : "sensor_cs",
				"parent" : "base",
				"children" : [],
				"pose_wrt_parent" : {
					"matrix4x4" : [0.984807753012208, 0.0, 0.17364817766693033, 2.3, 0.0, 1.0, 0.0, 0.0, -0.17364817766693033, 0.0, 0.984807753012208, 1.3, 0.0, 0.0, 0.0, 1.0]
				}
			},
            "CAM_2" : {
				"type" : "sensor_cs",
				"parent" : "base",
				"children" : [],
				"pose_wrt_parent" : {
					"euler_angles" : [0.0, 0.17453292519943295, 0.0],
					"translation" : [2.3, 0.0, 1.3],
					"sequence" : "ZYX"
				}
			}
        },
       ...
   }
}
```


The example shows the `coordinate_systems` item having several coordinate systems defined, including coordinate systems specific for the cameras (`CAM_1` and `CAM_2`) and other coordinate systems for the local and scene-level frameworks.


The transforms between coordinate systems may also be defined for each frame, overriding the default static pose defined above.


Transforms are defined with a friendly name used as index and the following properties:


- src: The name of the source coordinate system. This shall be the name of a valid (declared) coordinate system.
- dst: The destination coordinate system. This shall be the name of a valid (declared) coordinate system.
- transform_src_to_dst: This is the transform expressed in algebraic form, for example, as a 4x4 matrix enclosing a 3D rotation and a 3D translation between the coordinate systems.


_JSON example_


```json
{
    "openlabel" : {
        "metadata" : {
            "schema_version" : "1.0.0"
        },
        "coordinate_systems" : {
            "base" : {
                "type" : "local_cs",
                "parent" : "",
                "children" : []
            },
            "world" : {
                "type" : "scene_cs",
                "parent" : "",
                "children" : []
            }
        },
        "frames" : {
            "10" : {
                "frame_properties" : {
                    "transforms" : {
                        "base_to_world" : {
                            "src" : "base",
                            "dst" : "world",
                            "transform_src_to_dst" : {
                                "matrix4x4" : [1.0, 0.0, 0.0, 0.1, 0.0, 1.0, 0.0, 0.1, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
                            }
                        }
                    }
                }
            },
            "11" : {
                "frame_properties" : {
                    "transforms" : {
                        "base_to_world" : {
                            "src" : "base",
                            "dst" : "world",
                            "transform_src_to_dst" : {
                                "euler_angles" : [0.0, 0.0, 0.0],
                                "translation" : [1.0, 1.0, 0.0],
                                "sequence" : "ZYX"
                            },
                            "custom_property1" : 0.9,
                            "custom_property2" : "Some tag"
                        }
                    }
                }
            }
        }
    }
}
```


The example shows that the relationship between coordinate systems can be defined with `transforms` which can be defined for specific frames inside `frame_properties`. In the example, the transform between `base` and `world` coordinate systems is defined for frames `10` and `11`.


> **NOTE**: In general, coordinate systems associated with sensors may have the same name as the corresponding streams. For instance, Camera1 can be the name of a coordinate system and also the name of a stream. In this way, a sensor, such as a camera or a LiDAR, has internal data, for example intrinsics, defined at streams. External data is set-up with respect to other sensors at coordinate_systems or transforms at frame level.


With this structure, it is possible to describe particular and typical transformation cases, such as odometry poses of a vehicle with respect to a certain scene coordinate system:


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "frames": {
            "0": {
                "frame_properties": {
                    "transforms": {
                        "odom_to_vehicle-iso8855": {
                            "src": "odom",
                            "dst": "vehicle-iso8855",
                            "transform_src_to_dst": {
                                "matrix4x4": [1.0, 3.7088687554289227e-17, ...]
                            }
                        },
                        "raw_gps_data": [49.011212804408,8.4228850417969, ...],
                        "status": "interpolated"
                    }
                }
            }
        }
        ...
    }
}
```


The example shows a typical use case where the transforms encode the odometry, that is, the accumulated relative pose between a fixed coordinate system (in the example `odom`) and a moving coordinate system. In the example, `vehicle-iso8855` represents the usual coordinate system of a moving vehicle located in the rear axle, following the ISO 8855 convention, specified in [11].


> **NOTE**: By using additional properties, it is possible to embed detailed and customized information about the transforms, such as additional non-linear coefficients. In the example, the entries for raw_gps_data are only exemplary.


### 7.9. Ontologies


The `ontologies` item shall contain pointers to knowledge repositories, for example, URLs of ontologies that are used in the ASAM OpenLABEL JSON data to define the semantic type of elements. Elements can then point to concepts in these ontologies, so an application may consult an element’s meaning or investigate additional properties.


The format of the pointers shall use a key-value structure, where the key is a non-constrained string as a unique identifier, and the value may be the URL of the ontology or knowledge repository.


_Class_


```
ontologies
```


This is the JSON object of OpenLABEL ontologies. Ontology keys are strings containing numerical UIDs or 32 bytes UUIDs. Ontology values may be strings, for example, encoding a URI. JSON objects containing a URI string and optional lists of included and excluded terms.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 37. Diagram of the ontologies class*


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "ontologies": {
            "0": "https://www.somedomain.org/ontology",
            "1": "https://www.someotherdomain.org/ontology"
        },
        "objects": {
            "0": {
                "name": "car1",
                "type": "Car",
                "ontology_uid": 0
            },
            "1": {
                "name": "person1",
                "type": "Person",
                "ontology_uid": 0
            },
            "2": {
                "name": "mobile_phone1",
                "type": "MobilePhone",
                "ontology_uid": 1
            }
        }
    }
}
```


The example shows that the objects `car1` and `person1` are of types `Car` and `Person`. The definition of these types can be found at the ontology with `ontology_uid` = `0`. The definition of object `mobile_phone1` can be found at the ontology with `ontology_uid` = `1`.


### 7.10. Data types (geometric)


ASAM OpenLABEL defines geometric and non-geometric (generic) data types, which all together add the needed flexibility to represent any kind of information of labels or tags.


This section provides details about geometric data types for the multi-sensor data labeling use case. Examples of `object_data` are used, but the ASAM OpenLABEL JSON schema also includes definitions of `action_data`, `event_data`, and `context_data`. The difference is that only `object_data` can be of the geometric and non-geometric type.


Geometric `object_data` types are more complex and have specific fields. Also, these types may contain generic `object_data` as attributes.


_Rules_


- objects shall have a unique identifier.
- object_data shall have a unique name.


_Related topics_


- Data types (generic)
- Element data pointers


#### 7.10.1. Bounding boxes


Bounding boxes are geometric entities which enclose the shape of an object in Cartesian coordinates. Bounding boxes define minimum and maximum limits at each dimension so the entire object lies within the specified limits.


Bounding boxes are used to label objects and entities in 2D and 3D data representations, such as images or point clouds. Bounding boxes are useful as the most basic and compact representation of the position and size of an object. Bounding boxes have become the most popular labeling type for computer vision and machine learning because of its simplicity and good alignment with matrix operations in programming languages and hardware architectures.


There are three main bounding box types supported by ASAM OpenLABEL:


- 2D bounding box
- 2D rotated bounding box
- 3D bounding box (cuboid)


##### 2D bounding box (bbox)


A 2D bounding box is defined as a rectangle by an array of four floating point numbers:


*Table 12. Attributes of the 2D bounding box*

| Attribute | Unit | Description |
| --- | --- | --- |
| x | px | Specify the x-coordinate of the center of the rectangle. |
| y | px | Specify the y-coordinate of the center of the rectangle. |
| w | px | Specify the width of the rectangle in the x/y-coordinate system. |
| h | px | Specify the height of the rectangle in the x/y-coordinate system. |


Table 12 shows the available attributes of a 2D bounding box.

[Image: fig bbox definition]

*Figure 38. 2D bounding box definition*


Figure 38 shows a 2D bounding box on an image, enclosing an entire object defined by its center position (in pixels) and its width and height.


_Class_


```
bbox
```


A 2D bounding box is defined as a 4-dimensional vector [x, y, w, h], where [x, y] is the center of the bounding box and [w, h] represent the width (horizontal, x-coordinate dimension) and height (vertical, y-coordinate dimension), respectively.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 39. Diagram of the bbox class*


*Table 13. Properties of the bbox class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | The array of 4 values that define the [x, y, w, h] values of the bbox. |


_JSON example_


```json
"bbox": [{
    "name": "head",
    "val": [400, 200, 100, 120]
}]
```


The example shows a 2D bounding box serialized in JSON. The center of the rectangle is specified by the points `x=400` and `y=200`. The dimensions of the rectangle are specified by `width=100` and `height=120`.


For complex set-ups, it is possible to define the `coordinate_system` in which these magnitudes are expressed.


_JSON example_


It is also possible to embed non-geometric object data.


```json
"bbox": {
    "name": "head",
    "val": [400, 200, 100, 120],
    "coordinate_system": "Camera1",
    "attributes" : {
        "boolean" : [{
                "name" : "visible",
                "val" : false
            }, {
                "name" : "occluded",
                "val" : false
            }
        ]
    }
}
```


The example shows non-geometric object data, such as `visible` and `occluded`, embedded in a bounding box.


> **NOTE**: An object can contain multiple bbox entries, for example, to represent the body, head, and arms of a human. The same applies to all other object_data.


##### 2D rotated bounding box (rbbox)


A 2D rotated bounding box is defined as a 5-dimensional vector by five numbers:


*Table 14. Attributes of the 2D rotated bounding box*

| Attribute | Unit | Description |
| --- | --- | --- |
| x | px | Specify the x-coordinate of the center of the rectangle. |
| y | px | Specify the y-coordinate of the center of the rectangle. |
| w | px | Specify the width of the rectangle in the x/y-coordinate system (horizontal, x-coordinate dimension). |
| h | px | Specify the height of the rectangle in the x/y-coordinate system (vertical, y-coordinate dimension). |
| alpha | radians | Specifies the rotation of the rotated bounding box. It is defined as a right-handed rotation, meaning positive from x-axes to y-axes. The origin of rotation is placed at the center of the bounding box, meaning x, y. |


Table 14 shows the available attributes of a 2D rotated bounding box.

[Image: fig rbbox definition]

*Figure 40. 2D rotated bounding box definition*


Figure 40 shows a 2D rotated bounding box on an image, enclosing an entire object defined by its center position (in pixels), its width and height, and the rotation angle.


_Class_


```
rbbox
```


A 2D rotated bounding box is defined as a 5-dimensional vector [x, y, w, h, alpha], where [x, y] is the center of the bounding box and [w, h] represent the width (horizontal, x-coordinate dimension) and height (vertical, y-coordinate dimension), respectively. The angle alpha, in radians, represents the rotation of the rotated bounding box, and is defined as a right-handed rotation, that is, positive from x to y axes, and with the origin of rotation placed at the center of the bounding box (that is, [x, y]).


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 41. Diagram of the rbbox class*


*Table 15. Properties of the rbbox class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | The array of 5 values that define the [x, y, w, h, alpha] values of the bbox. |


_JSON example_


```json
"rbbox": [{
    "name": "outline",
    "val": [400, 200, 100, 120, 0.785]
}]
```


The example shows a 2D rotated bounding box serialized in JSON. The center of the 2D rotated bounding box is specified by the points `x=400` and `y=200`. The dimensions of the 2D rotated bounding box are specified by the `width=100` and `height=120`. The rotation of the 2D rotated bounding box is specified by `alpha=0.785`.


##### 3D bounding box (cuboid)


A 3D bounding box is a cuboid in 3D Euclidean space. It is defined by position, rotation, and size. Position and size are defined as 3-vectors, while rotation can be expressed in two alternative forms, using 4-vector quaternion notation or 3-vector Euler notation (to be applied in ZYX order equivalent to yaw-pitch-roll order).


One option is that the cuboid is defined as (x, y, z, qa, qb, qc, qd, sx, sy, and sz), where:


*Table 16. Attributes of the 3D bounding box (cuboid) using quaternion*

| Attribute | unit | Description |
| --- | --- | --- |
| x | m | Specifies the x-coordinate of the 3D position of the center of the cuboid. |
| y | m | Specifies the y-coordinate of the 3D position of the center of the cuboid. |
| z | m | Specifies the z-coordinate of the 3D position of the center of the cuboid. |
| qa |  | Specify the quaternion in non-unit form (x, y, z, and w) as in the SciPy convention. |
| qb |  | Specify the quaternion in non-unit form (x, y, z, and w) as in the SciPy convention. |
| qc |  | Specify the quaternion in non-unit form (x, y, z, and w) as in the SciPy convention. |
| qd |  | Specify the quaternion in non-unit form (x, y, z, and w) as in the SciPy convention. |
| sx | m | Specifies the x-dimension of the cuboid or the x-coordinate. |
| sy | m | Specifies the y-dimension of the cuboid or the y-coordinate. |
| sz | m | Specifies the z-dimension of the cuboid or the z-coordinate. |


Table 16 shows the available attributes of a 3D bounding box (cuboid) using quaternion. The quaternions conform to the SciPy convention [17].


Another option is that the cuboid is defined as (x, y, z, rx, ry, rz, sx, sy, and sz), where:


*Table 17. Attributes of the 3D bounding box (cuboid) using Euler angles*

| Attribute | unit | Description |
| --- | --- | --- |
| x | m | Specifies the x-coordinate of the 3D position of the center of the cuboid. |
| y | m | Specifies the y-coordinate of the 3D position of the center of the cuboid. |
| z | m | Specifies the z-coordinate of the 3D position of the center of the cuboid. |
| rz | rad | Specify Euler angles, rz = yaw. |
| ry | rad | Specify Euler angles, ry = pitch. |
| rx | rad | Specify Euler angles, rx = roll. |
| sx | m | Specifies the x-dimension of the cuboid or the x-coordinate. |
| sy | m | Specifies the y-dimension of the cuboid or the y-coordinate. |
| sz | m | Specifies the z-dimension of the cuboid or the z-coordinate. |


Table 17 shows the available attributes of a 3D bounding box (cuboid) using Euler angles.

[Image: fig cuboid]

*Figure 42. 3D bounding box definition*


Figure 42 shows a 3D bounding box (cuboid) on 3D space plot. The same cuboid can be expressed using the two defined alternatives: using Euler angles in ZYX order, or with a Quaternion. Note the center of the cuboid is used as origin of the cuboid coordinate system.


_Class_


```
cuboid
```


A cuboid or 3D bounding box. It is defined by the position of its center, the rotation in 3D, and its dimensions.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 43. Diagram of the cuboid class*


*Table 18. Properties of the cuboid class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val |  | true |  | List of values encoding the position, rotation and dimensions. Two options are supported, using 9 or 10 values. If 9 values are used, the format is (x, y, z, rx, ry, rz, sx, sy, sz), where (x, y, z) encodes the position, (rx, ry, rz) encodes the Euler angles that encode the rotation, and (sx, sy, sz) are the dimensions of the cuboid in its object coordinate system. If 10 values are used, then the format is (x, y, z, qx, qy, qz, qw, sx, sy, sz) with the only difference of the rotation values which are the 4 values of a quaternion. |


_JSON example_


```json
"cuboid": [{
    "name": "shape",
    "val": [12.0, 20.0, 0.0, 1.0, 1.0, 1.0, 1.0, 4.0, 2.0, 1.5]
}]
```


An alternative is defined by nine numbers, substituting the quaternion vector by 3 Euler angles (`rx`, `ry`, `rz`) and respectively defining the rotation of the object coordinate system in the x-, y- and z-axes. The rotation is assumed to be applied ZYX.


#### 7.10.2. Semantic segmentation: image and poly2d


Semantic segmentation responds to the need for more detailed annotations by defining one or more labels per pixel of a given image (for details about the different possible use cases and semantic segmentation taxonomy, see concept Semantic segmentation and example Semantic segmentation).


To facilitate visual perception, a color code for each class may be specified. The information on a certain pixel belonging to a certain category is expressed by assigning a specific RGB value to that pixel, which visually represents that category.


In terms of the data format, such dense information can be tackled with different approaches. Each of them has different purposes or responds to different needs:


- Separate images: Historically, semantic segmentation information has been stored as separate images, usually formatted as PNG images (lossless). This is the simplest approach and the one offering the smallest storage footprint. However, there are many separate files in the file system. Therefore, the main ASAM OpenLABEL JSON file may contain one or more URLs/URIs of these images.


_JSON example_


```json
"objects": {
    "0": {
        "name": "",
        "type": "",
        "object_data": {
            "string": [
                {
                    "name": "semantic mask uri - dictionary 1",
                    "val": "/someURLorURI/someImageName1.png"
                },{
                    "name": "semantic mask uri - dictionary 2",
                    "val": "/someURLorURI/someImageName2.png"
                }
            ]
        }
    }
}
```


- Embedded images: Image content can be written in code, using any image processing software. The code is expressed as a string in base64 and then embedded within the JSON file. This approach creates large JSON files (base64 adds 4/3 overhead) but mitigate the need to manage multiple files:


_JSON example_


```json
"objects": {
    "0": {
        "name": "",
        "type": "",
        "object_data": {
            "image": [
                {
                    "name": "semantic mask - dictionary 1",
                    "val": "iVBORw0KGgoAAAANSUhEUgAAAeAAAAKACAIAAADLqjwFAAAKu0lEQVR42u3dPW7VYBCGUSe6JWW6NCyDErEvKvaFKFkGDR0lfYiEkABFN8n9+fzOzDkFDRLgAT0a2Z/NtgEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc0uevb25MASCwzo8/CjRAYp0FGiC0zgINEFpngQYIrbNAA4TWWaABQuss0AChdRZogMQ0CzRAbp0FGiC0zgINEFpngQYIrbNAA4TWWaABQuv84d1PgQZIrLMNGiC0zrmBfv/2o7/U0r58+2QIcE6dH90aH0BgnQUaILTOjw6GCLBvmp+ssw0aILTOAg0QWmeBBgits0ADhNZ585AQYH2dn02zDRogt85VN+jjb6nt9RbizY/vD3f3/rGCOl+kzptbHCdU+LSf1W5Q51fVWaDPLfLJv45egzoL9M5dfvbXV2pQZ4FOSfOTv51MQ9c0n1xngd4zzTIN6izQ0WmWaVBngY5Os0yDOgt0dJplGtT5b0PfJAyvc7k/J6jzxetcdYM+513BcsmzSkOhOl8qzRM36LoLqVUaptV5VqCrN06jYVSdBwW6R900GubUeUqgO3VNo2FInUcEul/RNBom1Hlrfw66a8t8exp2T/O169x8g+69adqjoXedOwd6Qr80GhrXuW2g55RLo6FrnXsGelqzNBpa1nnzNTtAnQPT3HODnrlOWqKhX527BXpypzQamtV5G/u5UUCdw+vcKtBWSBOATnW2QQPqHFrnPoG2PJoDNKvz5pgdIM2ZdW6yQVsbTQP61XlzDxpQ58w6dwi0hdFMoGWdbdCAOofWeav+kNCqeGQyvuiPOtdNsw0aUOfcOgs0oM65Cgfa/Q3zgcZ1tkED6izQAOr8Sl71BgaluVCdbdCAOgv0pXkCZkqoc+8626ABdRZoAHUWaECdG9R5c4oDaFznumm2QQPqLNAA6izQgDr3qLNAA+os0Bfl/QuzQp3b13kreorj4e5ed14+K0NgQpr71XlziwNQZ4EGUGeBBtRZoAHU+Xq86g2UrHPvNNugAXUWaAB1FmhAnQV6Z96/MCXUWaAB1HkfTnEA6WmeWWcbNKDOAg2gznMC7QmY+aDOAg2gzgINqLM6/1H7FIcv9x+ZjCFQtM7SbIMG1FmgrYpmgjqrsw0aUGeBtjCaBqizQAPqPFWTb3E4zmF9pmKa1dkGDaizQFseTQB1VmeBBtRZoK2Qrh3UeR/dPtg/82mhOlOlztI8d4MG1FmgrZOuF3VWZ4HWLFeKOgu0crlGUGeB1i9XhzozO9CNK6bOqPMEh/ZX2O/gnTqTn2Z1tkFPLJo6o84CrdGuAtRZoNVNnVFnhge6dOPUGXUe6DDtgn+XrtBjQ2mmRJ2l2QY9rnrqjDrboOc2OnaVlmbUmcPw6w/MtDSjzgh0XKalGXVGoOMyLc2oMwIdl2lpplya1VmgIzJ9vVLrMuqMQF+4pCf3WpFRZwR6aa//a7cKo85ckP80dkW7QZ0RaECd+3CLA9RZmm3QgDoj0IA6CzSgzgg0oM4CDagzCZziAGlWZxs0oM4INKizOgs0oM4INKDOw3hICHPrLM02aECdEWhQZ3UWaECdEWhAnQUaUGcEGlBnnuWYHfRPszrboAF1RqBBndVZoAF1RqABdeYfHhJCwzpLsw0aUGcEGtRZnQUaUGcEGlBnBBrUmYKc4oDaaVZnGzSgzgg0qLM6I9Cgzgg0oM4INKgzXTjFAZXqLM02aECd2d+NEYA6I9CAOiPQoM4INKDOCDTMSrM6I9Cgzgg0qLM6I9Cgzgg0oM4INHSvszQj0KDOCDSoszoj0KDOCDSgzgg0qDMCDSxOszoj0KDOCDSoszoj0KDOCDSgzgg0qDMINKyvszQj0KDOCDSoszoj0KDOCDSgzgg0qDMINCxOszoj0KDOCDSoszoj0KDOINCgzgg0dK+zNCPQoM4INKizOiPQoM4g0KDOCDSoMwg0qDMCDdKszgg0qDMINOqszgg0qDMINKgzAg3t6yzNCDSoMwg06qzOCDSoMwg0qDMCDeoMAg2L06zOCDSoMwg06qzOCDSoMwg0qDMCDeoMAg3r6yzNCDSoMwg06qzOCDSoMwg0qDMCDeoMAg2L06zOCDSoMwg06qzOCDSoMwg0qDMINN3rLM0INKgzCDTqrM4INKgzCDSoMwg06gwCDeoMAo00qzMCDeoMAo06qzMINOoMAg3qDAJN+zpLMwIN6gwCjTqrMwg06gwCDeoMAo06g0DD4jSrMwg06gwCjTqrMwg06gwCDeoMAo06g0DD+jpLMwg06gwCjTqrMwg06gwCDeoMAo06AwLN4jSrMwg06gwCjTqrMwg06gwCDeoMAk33OkszCDTqDAKNOqszCDTqDAIN6gwCjToDAs3iNKszCDTqDAKNOqszCDTqDAg06gwCjToDAs36OkszCDTqDAKNOqszCDTqDAg06gwCjToDAs3iNKszCDTqDAi0OqszCDTqDAg06gwCTfc6SzMINOoMCLQ6qzMINOoMCDTqDAKNOgMCjToDAi3N6gwCjToDAq3O6gwCjToDAo06g0DTvs7SDAKNOgMCrc7qDAKNOgMCjToDAq3OgECzOM3qDAKNOgMCrc7qDAKNOgMCjToDAq3OgECzvs7SDAKNOgMCrc7qDAJtBOoMCDTqDAi0OgMCzeI0qzMINOoMCLQ6qzMg0OoMCDTqDAh09zpLMwg06gwItDqrMyDQ6gwINOoMCLQ6AwKNOgMCLc3qDAi0OgMCrc7qDAi0OgMCjToDAt2+ztIMCLQ6AwKtzuoMCLQ6AwKNOgMCrc4AAr04zeoMCLQ6AwKtzuoMCLQ6AwKNOgMCrc4AAr2+ztIMCLQ6AwKtzuoMCLQ6Awi0OgMCrc4AAr04zeoMCLQ6AwKtzuoMCLQ6Awi0OgMC3b3O0gwItDoDAq3O6gwItDoDCLQ6AwKtzgACvTjN6gwItDoDTA20OgMCrc4AAq3OgECrM4BA71lnaQYEWp0BpgZanQGBVmcAgVZnQKDVGUCgd0uzOgMCrc4AUwOtzoBAqzOAQKszQN1AO7ABCLQ6Awi0OgPUDbQ6AwKtzgACrc4AdQOtzoBAl0+zOgMCrc4AUwOtzgCJgVZngMRAqzNAYqAd2ABIDLQ6AyQGWp0BEgOtzgCJgVZngMRAqzNAXKAdpwNIDLQ6AyQGWp0BEgOtzgCJgVZngMRAqzNAYqAdpwNIDLQ6AyQGWp0BEgOtzgCJgVZngMRAqzPAmW4T/hDqDJAYaHUGeNJVbnG8/P6GOgMsDfQLG63OAEfsdotDnQGOO0gzQKbV56DVGSDICd+xAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqOcXcO/DOJCe2z8AAAAASUVORK5CYII=",
                    "mime_type": "image/png",
                    "encoding": "base64"
                }
            ]
        }
    }
}
```


- Polygons: Another option is to decompose the entire semantic segmentation mask into different classes or object instances. This approach has the benefit of identifying individual objects directly within the JSON file. Thus, a user application can directly read specific objects, without the need to load the PNG image and find the object of interest. The counterpart is an increased JSON size. Polygons (2D) can be expressed directly as lists of x,y-coordinates, using MODE_POLY2D_ABSOLUTE. However, this may create very large and redundant information. Lossless compression mechanisms can be applied to convert the, possibly long, list of x,y-coordinates into smaller strings:


_JSON example_


```json
"objects": {
    "0": {
        "name": "car1",
        "type": "#Car",
        "object_data": {
            "poly2d": [
                {
                    "name": "poly1",
                    "val": ["5","5","1","mBIIOIII"],
                    "mode": "MODE_POLY2D_SRF6DCC",
                    "closed": false
                }, {
                    "name": "poly2",
                    "val": [5,5,10,5,11,6,11,8,9,10,5,10,3,8,3,6,4,5],
                    "mode": "MODE_POLY2D_ABSOLUTE",
                    "closed": false
                }
            ]
        }
    }
}
```


The example shows the following:


- RLE or Chain Code algorithms can losslessly compress a sequence of x,y-coordinates. The poly2d.py script is used for polyline poly1, and specified using mode MODE_POLY2D_SRF6DCC. Polyline poly2 is encoded with no compression, and thus the specified mode is MODE_POLY2D_ABSOLUTE.
- Using polygons implies that labels are created at object-level, rather than image-level. This might be useful, for example, for searching applications that locate all objects of type car.


> **NOTE**: Using PNG masks, either as separate files or embedded inside the JSON file, is the preferred way to store labels for machine-learning applications. They do not search inside the masks, but rather move them directly into training pipelines.


#### 7.10.3. Poly3d


A `poly3d` is an `object_data` that represents a polygon in 3D space. It is defined as a list of 3D points. The array is a concatenation of x,y,z-values, corresponding to the x,y,z-coordinate of each point with respect to the defined coordinate system. Therefore, the array shall always have a number of values multiple of 3.


_Class_


```
poly3d
```


A 3D polyline defined as a sequence of 3D points.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 44. Diagram of the poly3d class*


*Table 19. Properties of the poly3d class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| closed | boolean | true |  | A boolean that defines whether the polyline is closed or not. In case it is closed, it is assumed that the last point of the sequence is connected with the first one. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | List of numerical values of the polyline, according to its mode. |


_JSON example_


```json
"poly3D" : [{
    "closed" : false,
    "coordinate_system" : "vehicle_iso8855",
    "name" : "lane_marking",
    "val" : [557.02, 29.69, -1.63, 562.51, 29.97, -1.59, 568.00, 30.36, -1.58, 571.98, 30.76, -1.57]
}]
```


The example shows a `poly3D` `object_data` specified to have four points, and thus 4 x 3 = 12 values.


#### 7.10.4. Mesh


`mesh` is a special type of `object_data`, which describes a complex structure with point-line-area hierarchies. It is intended to represent 3D meshes, where points, lines, and areas compose the mesh by defining their interrelations. The elements point, line, and area may have their own properties, just like any other `object_data`.


_Class_


```
mesh
```


A mesh encodes a point-line-area structure. It is intended to represent flat 3D meshes, such as several connected parking lots, where points, lines and areas composing the mesh are interrelated and can have their own properties.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 45. Diagram of the mesh class*


*Table 20. Properties of the mesh class*

| Name | Type | Additional properties | Reference | Description |
| --- | --- | --- | --- | --- |
| area_reference | object | false | #/definitions/area_reference | This is the JSON object for the areas defined for this mesh. Area keys are strings containing numerical UIDs. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| line_reference | object | false | #/definitions/line_reference | This is the JSON object for the 3D lines defined for this mesh. Line reference keys are strings containing numerical UIDs. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| point3d | object | false | #/definitions/point3d | This is the JSON object for the 3D points defined for this mesh. Point3d keys are strings containing numerical UIDs. |


_JSON example_


```json
"mesh" : [{
    "name" : "parkslot1",
    "point3d" : {
        "0" : {
            "name" : "Vertex0",
            "val" : [25, 25, 0],
        },
        "1" : {
            "name" : "Vertex1",
            "val" : [26, 25, 0],
        },
        "2" : {
            "name" : "Vertex2",
            "val" : [26, 26, 0],
        },
        "3" : {
            "name" : "Vertex3",
            "val" : [25, 26, 0],
        },
        "4" : {
            "name" : "Vertex4",
            "val" : [27, 25, 0],
        },
        "5" : {
            "name" : "Vertex5",
            "val" : [27, 26, 0],
        }
    },
    "line_reference" : {
        "0" : {
            "name" : "Edge",
            "reference_type" : "point3d",
            "val" : [0, 1],
        },
        "1" : {
            "name" : "Edge",
            "reference_type" : "point3d",
            "val" : [1, 2],
        },
        "2" : {
            "name" : "Edge",
            "reference_type" : "point3d",
            "val" : [2, 3],
        },
        "3" : {
            "name" : "Edge",
            "reference_type" : "point3d",
            "val" : [3, 0],
        },
        "4" : {
            "name" : "Edge",
            "reference_type" : "point3d",
            "val" : [1, 4],
        },
        "5" : {
            "name" : "Edge",
            "reference_type" : "point3d",
            "val" : [4, 5],
        },
        "6" : {
            "name" : "Edge",
            "reference_type" : "point3d",
            "val" : [5, 2],
        }
    },
    "area_reference" : {
        "0" : {
            "name" : "Slot",
            "reference_type" : "line_reference",
            "val" : [0, 1, 2, 3],
        },
        "1" : {
            "name" : "Slot",
            "reference_type" : "line_reference",
            "val" : [4, 5, 6, 1],
        }
    }
}]
```


The example shows an ideal `object_data` to describe complex parking areas, where parking lots can share lines and points. Properties of areas may define whether the parking lot is empty or used.


Mesh contains a dictionary of `point3d`. Their keys may be used to specify lines as a `line_reference`. This `line_reference` is also stored as a dictionary, so their keys may be used to specify areas as `area_reference`.


The elements `point3d`, `line_reference`, and `area_reference` are `object_data`. They may have attributes of non-geometric type, that is, `boolean`, `text`, `num` and `vec`. This gives them full flexibility to describe complex meshes.


_JSON example_


```json
"6" : {
    "name" : "Edge",
    "reference_type" : "point3d",
    "val" : [5, 2],
    "attributes" : {
        "text" : [{
                "name" : "line_type",
                "val" : "dashed"
            }, {
                "name" : "line_color",
                "val" : "yellow"
            }
        ],
    }
}
```


The example shows a `line_reference` with attributes.


> **NOTE**: A line_reference shall have only two reference points, as a line is defined by two points. An area_reference may have as many line references as desired as it may represent a complex polyline.


#### 7.10.5. Mat and binary


Matrices and binary data are a special form of data and may be expressed using types `mat` and `bin` `object_data`.


- Matrices are defined by the number of rows, columns, and channels. The numerical values are stored as a list of numbers.
- Binary data may be defined by an encoding format and data type.


> **TIP**: mat is useful to define list of points, such as a 3xN array of N 3D points in homogeneous coordinates, which may be points from a point cloud file.


_Class_


```
mat
```


A matrix.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 46. Diagram of the mat class*


*Table 21. Properties of the mat class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| channels | number | true |  | Number of channels of the matrix. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| data_type | string | true |  | This is a string that declares the type of the numerical values of the matrix, for example, "float". |
| height | number | true |  | Height of the matrix. Expressed in number of rows. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | Flattened list of values of the matrix. |
| width | number | true |  | Width of the matrix. Expressed in number of columns. |


```
binary
```


A binary payload.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 47. Diagram of the binary class*


*Table 22. Properties of the binary class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| data_type | string | true |  | This is a string that declares the type of the values of the binary object. |
| encoding | string | true |  | This is a string that declares the encoding type of the bytes for this binary payload, for example, "base64". |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | string | true |  | A string with the encoded bytes of this binary payload. |


#### 7.10.6. Point2d and Point3d


Point2d and Point3d are basic structures to define individual points in 2D and 3D space. They are `object_data`.


`point2d` and `point3d` are defined by their value, as a list of 2 and 3 floating point numbers.


In addition, `point2d` and `point3d` have an `id` attribute as a numerical identifier. This may be used to integrate them into larger structures, for example, a `mesh`.


_Class_


```
point2d
```


A 2D point.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 48. Diagram of the point2d class*


*Table 23. Properties of the point2d class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| id | integer |  |  | This is an integer identifier of the point in the context of a set of points. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | List of two coordinates to define the point, for example, x, y. |


```
point3d
```


A 3D point.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 49. Diagram of the point3d class*


*Table 24. Properties of the point3d class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| id | integer |  |  | This is an integer identifier of the point in the context of a set of points. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | List of three coordinates to define the point, for example, x, y, z. |


### 7.11. Resources


The `resources` item shall contain pointers to external resources, such as files or databases, which may contain additional information about elements labeled in the ASAM OpenLABEL data. Inside each resource, a unique identifier of the element shall be used to create the link.


An example is a lane marking labeling task. If an existing high-definition map exists in the form of an ASAM OpenDRIVE file, then road or lane elements labeled in ASAM OpenLABEL may exist in the map. Then, a link to the matched road or lane can be created using a `resource_uid` and a id at the resource.


_Class_


```
resources
```


This is the JSON object of OpenLABEL resources. Resource keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource values are strings that describe an external resource, for example, file name, URLs, that may be used to link data of the OpenLABEL annotation content with external existing content.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 50. Diagram of the resources class*


_JSON example_


```json
{
	"openlabel" : {
		"metadata" : {
			"schema_version" : "1.0.0"
		},
		"resources" : {
			"0" : "../resources/xodr/multi_intersections.xodr"
		},
		"objects" : {
			"0" : {
				"name" : "road1",
				"type" : "road",
				"resource_uid" : {
					"0" : "217"
				}
			},
			"1" : {
				"name" : "lane1",
				"type" : "lane",
				"resource_uid" : {
					"0" : "3"
				}
			}
		}
	}
}
```


The example shows that `lane1` is labeled as an object of type `lane`. `lane1` exists in the resource `0` with `resource_uid` `3`. That means that the id of the lane inside the resource is `3`.


### 7.12. Use cases


The following section provides practical use cases for ASAM OpenLABEL.


#### 7.12.1. 2D bounding boxes


This use case shows object labeling with 2D bounding boxes in images.


Single image and sequences of images are presented separately to show the differences between static and dynamic labeling, for example, with a persistent ID for tracked objects.


##### Single image


The single image approach aims at adding bounding boxes to define the position and size of objects in a single image. Variants of this labeling task may include adding other properties of the object or attributes to the bounding boxes, for example, confidence values.

[Image: fig sample bbox]

*Figure 51. Example image*


Figure 51 shows an exemplary traffic situation.

[Image: fig bboxes]

*Figure 52. Example image with resulting bounding boxes*


Figure 52 shows the target dictionary of classes and their bounding boxes, including `Car`, `Bus`, `Semaphore`, and `ZebraCross`. Only some objects are marked with their respective class for demonstration purpose.


The ASAM OpenLABEL [openlabel100_test_bbox_simple.json](https://openlabel.asam.net/V1-0-0/examples/openlabel100_test_bbox_simple.json) file contains basic bounding boxes defined for each object.


The ASAM OpenLABEL [openlabel100_test_bbox_simple_attributes.json](https://openlabel.asam.net/V1-0-0/examples/openlabel100_test_bbox_simple_attributes.json) file contains extended properties of objects and bounding boxes.


#### 7.12.2. 3D bounding boxes (cuboids)


This use case shows an example of 3D bounding boxes (or cuboids) labels. The example shows the creation of `object` labels in a sequence of point clouds obtained from a LiDAR sensor. Labels correspond to physical objects, that is, cars and pedestrians.

[Image: fig example cuboid lidar view]

*Figure 53. Example visualization of a cuboid in a point cloud view*


Cuboids have been produced automatically using a 3D object detector on the point cloud. Figure 53 shows several cuboids which enclose the 3D points that correspond to physical objects, that is, cars and a pedestrian, in the point cloud.


In this example, the cuboids are expressed using the preferred quaternion-translation vector form, which implies that ten values define the cuboid data, as explained in 3D bounding box (cuboid).


The ASAM OpenLABEL [openlabel100_example_cuboids.json](https://openlabel.asam.net/V1-0-0/examples/openlabel100_example_cuboids.json) file contains the labels for the entire scene, including transform entries for all frames representing the odometry values obtained with a differential GPS.


#### 7.12.3. Point clouds


Labeling point clouds in ASAM OpenLABEL is performed using a similar approach to 2D image segmentation.


A point cloud is a set of 3D points, each of them corresponding to a certain 3D position in space. Each point may be given additional values, depending on the source sensor or process. LiDAR sensors, for example, usually attach a timestamp and intensity values to each point.


Labeling a point cloud means adding a label to each point which determines the class that point corresponds to, for example, `car` or `pavement`.


The number of points in a point cloud depends on the source sensor or application. When this number is large, for example, several millions, an encoding strategy is preferable in order to compress the disk space required to store the labels.


Labels correspond to classes, and integer indexes are used to encode class values. For example, class `car` can be encoded as `0`, `pedestrian` as `1`, `pavement` as `2`, etc. A dictionary with the class-index map needs to be stored externally.


By indexing class labels as integers the set of labels of a point cloud is a list or sequence of integers, where the position of the label in the list shall correspond to the position of the point within the point cloud.


For example, `11122222222000000000000…​` is a list of label indexes, each of them labeling a 3D point as belonging to class `1`, `2`, etc.


In ASAM OpenLABEL two approaches are defined to represent such a list of labels.


One is to use an external file, for example, an external file which contains the data values, possibly in binary form.


_JSON example_


```json
{
  "objects": {
    "0": {
      "name": "3DPointCloudSegmentation0",
      "type": "3DPointCloudSegmentation",
      "object_data": {
        "text": [{
          "name": "uri",
          "val": "http://semantic3d.net/data/sem8_labels_training.7z"
        }]
      }
    }
  }
}
```


The example shows an `object` which contains an URI to an external file containing the labels of the 3D point cloud.


The second option is to embed a stringified version of the label values into the ASAM OpenLABEL JSON payload.


A lossless compression approach is recommended to reduce the potentially large volume of data of this payload. For example, several million integers may be used to represent the labels of an entire point cloud.


Considering the nature of the labels of point clouds, that is, many repeated labels for 3D points that are close in space, a Run-Length-Encoding (RLE) mechanism may significantly compress it.


As an example, `11122222222000000000000` is converted into `#3V1#8V2#13V0`, where the number after character `#` defines the count of the repeated value, defined after character `V`. In this example, there are three consecutive `1` labels, then eight consecutive `2` labels. Using this approach, the compression ratio depends on the data but is always superior to 1.0 if in average the count of repeated values is at least four.


_JSON example_


```json
{
  "objects": {
    "1": {
      "name": "3DPointCloudSegmentation1",
      "type": "3DPointCloudSegmentation",
      "object_data": {
        "binary": [{
          "name": "labels",
          "val": "#2142V6#21379V5#902V3#762V5#3V3#2195V2#36V6#11V2#2V6#2V2#17V6#2V2#4V6#2V2#10V6#720V2#1V6#1V2#3V6#3V2#42V6#50V2#2V6#3V2#25V6#12V2#5V6#1V2#12V6#12V2#1V6#2V2#3V6#1V2#20V6#57V2#5V6#7V2#1V6#1V2#7V6#3V2#29V6#2752V2#3V6#4V2#3V6#12V2#1V6#1V2#5V6#2V2#5V6#1V2#6V6#1V2#3V6#1V2#12V6#45V2#18V6#7V2#76V6#333V2#1V6#2V2#5V6#1V2#1V6#1V2#2V6#20V2#2V6#5V2#193V6#421V2#1V6#406V2#8V6#2V2#1V6#3V2#1V6#4V2#1V6#1V2#17V6#94V2#24V6#1V2#33V6#7V2#2V6#51V2#74V6#640V2#1V6#4V2#12V6#2V2#21V6#16V2#63V6#1154V2#3V6#2502V2#3V3#1V2#121V3#76V2#26V3#354V2#1V3#1V2#6V3#3V2#1V3#6V2#6V3#1V2#2V3#5V2#2V3#5125V2#10812V3#36244V2#2V5#1V2#32V5#17V2#2V5#1V2#18V5#7V2#29V5#3V2#1V5#8V2#4V5#5V2#2V5#1V2#20V5#19V2#4V5#8V2#1V5#9V2#93V5#548V2#2V5#2V2#5V5#1V2#1V5#2V2#66V5#380V2#4V5#6V2#1V5#1V2#2V5#1V2#56V5#5V2#1V5#1V2#1V5#5V2#3V5#5V2#1V5#3V2#19V5#3V2#2V5#5V2#4V5#5V2#2V5#1V2#3V5#3V2#99V5#7V2#1049V5#11748V2#174V3#1195V2#1V3#1V2#1V3#3V2#1V3#7V2#17V3#34V2#24V3#8992V2#1V3#31V2#1V3#2V2#2V3#9655V2#1V3#2V2#20V3#7V2#2V3#3V2#39V3#4V2#13V3#3V2#6V3#2V2#1V3#3V2#6V3#1V2#20V3#7V2#6V3#8V2#1V3#1V2#112V3#5V2#273V3#2V2#494V3#4V2#472V3#32V2#5V3#2V2#5V3#7V2#16V3#3V2#3V3#12212V2#46972V5#231V2#1V5#2V2#1V5#6V2#4V5#1V2#1V5#4V2#2V5#2V2#65V5#14V2#1V5#2V2#2V5#6V2#1V5#2V2#26V5#8V2#47V5#7V2#4V5#6V2#29V5#2V2#1V5#1V2#1V5#4V2#7V5#1V2#136V5#4V2#1V5...",
          "data_type": "",
          "encoding": "rle"
        }]
      }
    }
  }
}
```


In this example, a pseudo JSON object is shown with a RLE encoded payload of a list of labels indexes embedded inside a `binary` element where the `encoding` type is specified to be `rle`.


> **NOTE**: The RLE-based encoding and decoding process can be implemented very efficiently and can be thought as an equivalent to embedding PNG images payloads for 2D semantic segmentation.


> **NOTE**: The RLE-based compression ratio is about 1:1000 for the examples of the dataset, where labels are provided as CSV files [18]. For example, point cloud bildstein_station1 contains ~29 million points. The labels file (CSV) has 3 bytes per point (label, whitespace, and separator) which makes ~89 MB (if whitespace is removed, this is ~58 MB). The ASAM OpenLABEL RLE-based approach produces a 88 kB JSON file.

[Image: fig point cloud rgb]

*Figure 54. 3D point cloud bildstein_station1 [18]*

[Image: fig point cloud class]

*Figure 55. 3D point cloud segmentation bildstein_station1 [18]*


Figure 54 shows a render of a 3D point cloud, colored according to RGB values obtained with a camera sensor. Figure 55 shows the same render coloring 3D points according to their associated class.


The ASAM OpenLABEL [openlabel100_point_cloud_labels_rle.json](https://openlabel.asam.net/V1-0-0/examples/openlabel100_point_cloud_labels_rle.json) file contains the 3D point cloud segmentation of `bildstein_station1` using RLE encoding.


#### 7.12.4. Semantic segmentation


This use case shows a complete ASAM OpenLABEL JSON file corresponding to a semantic segmentation of an image labeled at pixel-level. Two variants are considered:


- Class-level annotation
- Instance-level annotation


The input data are PNG images from existing open-source datasets which contain semantic segmentation at pixel level. The output are ASAM OpenLABEL JSON files covering different encoding options.


##### Class labels


The class label approach is to label an image in a way that each pixel is categorized as belonging to a certain class.


The example image and dictionary of classes are derived from the Mapillary Vistas Dataset (image `-3-MmXdwhyIQhtb4-8NqHQ`) [19].

[Image: fig sample segmentation class]

*Figure 56. Example of a PNG-colored image [19]*


These types of labels are represented as PNG images, where each pixel is painted with a certain RGB color according to its class, as shown in Figure 56. To parse the labels, a PNG image is needed, along with a configuration file which contains the class dictionary. This dictionary maps RGB colors to classes.


There are three example JSON files for this use case:


- ASAM OpenLABEL openlabel-3-MmXdwhyIQhtb4-8NqHQ_class_b64.json file with the base64 codification of the PNG payload.
- ASAM OpenLABEL openlabel-3-MmXdwhyIQhtb4-8NqHQ_class_MODE_POLY2D_ABSOLUTE.json file with each segmented class encoded as a polygon, described in absolute mode.
- ASAM OpenLABEL openlabel-3-MmXdwhyIQhtb4-8NqHQ_class_MODE_POLY2D_SRF6DCC.json file with each segmented class encoded as a polygon, described in chain-code.


##### Instance labels


These labels are frequently represented as PNG images with instance-coded classes. That means that each RGB color value corresponds to a class in a dictionary and an instance identifier.

[Image: fig sample segmentation instance]

*Figure 57. Example of an image with contrast enhanced [19]*


Figure 57 shows an example instance image from the Mapillary Vistas Dataset (image `-3-MmXdwhyIQhtb4-8NqHQ`) with contrast enhanced for better visualization [19].


There are three example JSON files for this use case:


- ASAM OpenLABEL openlabel-3-MmXdwhyIQhtb4-8NqHQ_instances_b64.json file with the base64 codification of the PNG payload.
- ASAM OpenLABEL openlabel-3-MmXdwhyIQhtb4-8NqHQ_instances_MODE_POLY2D_ABSOLUTE.json file with each segmented class encoded as a polygon, described in absolute mode.
- ASAM OpenLABEL openlabel-3-MmXdwhyIQhtb4-8NqHQ_instances_MODE_POLY2D_SRF6DCC.json file with each segmented class encoded as a polygon, described in chain-code.


##### Full and partial scene segmentation


This use case shows examples for partial and full scene segmentation.

[Image: fig example semantic segmentation original image]

*Figure 58. Example of an original image used for semantic segmentation*


Figure 58 shows an example image of a typical traffic scene.


Note the following:


- It contains instantiable objects (cars).
- It contains non-instantiable objects (sky, vegetation, …​).
- The two main cars overlap.

[Image: fig example semantic segmentation non instance aware]

*Figure 59. Example of a semantic segmentation that is non instance-aware*


Figure 59 shows a partial segmentation of the image which is non-instance aware.


- It is partially segmented because only some parts of the image have been labeled, for example, the cars. Other parts of the image are left grayed and unlabeled.
- It is non-instance aware because pixels are labeled according only to their class. In this way, a big blob of pixels in the center of the image is assigned the same label because they correspond to the class car. Thus, the overlapping cars cannot be separated from this information alone.


_JSON example_


```json
{
    "objects": {
      "0": {
        "name": "class0",
        "type": "car",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [425, 143, 424, 144, 423, 144, 422, 145, 422, 146, 419, 149, 419, 150, 418, 151, 418, 169, 421, 169, 421, 167, 422, 166, 440, 166, 441, 167, 441, 169, 445, 169, 445, 156, 446, 155, 447, 155, 447, 152, 445, 152, 444, 151, 444, 148, 442, 146, 442, 145, 440, 143],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [1, -1, -1, -1]
            }, {
              "name": "contour1",
              "val": [118, 112, 117, 113, 107, 113, 106, 114, 106, 115, 105, 116, 105, 117, 104, 118, 104, 120, 103, 121, 103, 124, 102, 125, 102, 129, 101, 130, 101, 134, 100, 135, 100, 137, 99, 138, 99, 167, 98, 168, 96, 168, 95, 169, 95, 174, 97, 176, 98, 176, 99, 177, 100, 177, 101, 178, 105, 178, 107, 180, 120, 180, 121, 181, 121, 184, 122, 185, 122, 186, 126, 190, 127, 190, 128, 191, 145, 191, 150, 186, 154, 186, 155, 187, 182, 187, 183, 188, 220, 188, 221, 189, 221, 196, 220, 197, 220, 199, 219, 200, 219, 201, 218, 202, 218, 205, 217, 206, 217, 221, 218, 222, 218, 224, 219, 225, 219, 248, 221, 250, 221, 251, 223, 253, 235, 253, 235, 247, 236, 246, 236, 242, 238, 240, 245, 240, 246, 241, 254, 241, 255, 242, 260, 242, 261, 243, 266, 243, 267, 244, 279, 244, 280, 245, 297, 245, 298, 246, 344, 246, 345, 245, 349, 245, 350, 246, 350, 250, 349, 251, 349, 259, 363, 259, 363, 258, 364, 257, 364, 252, 365, 251, 365, 231, 366, 230, 366, 221, 367, 220, 367, 214, 368, 213, 368, 198, 367, 197, 367, 181, 362, 176, 362, 175, 361, 174, 361, 173, 362, 172, 370, 172, 371, 171, 372, 171, 373, 170, 374, 170, 374, 165, 372, 163, 362, 163, 362, 167, 361, 168, 360, 168, 359, 167, 359, 161, 358, 160, 358, 154, 357, 153, 357, 152, 356, 151, 356, 150, 354, 148, 354, 147, 353, 146, 353, 145, 352, 144, 352, 142, 350, 140, 350, 139, 348, 137, 348, 136, 344, 132, 343, 132, 342, 131, 339, 131, 338, 130, 329, 130, 328, 129, 267, 129, 266, 130, 261, 130, 260, 131, 257, 131, 255, 133, 254, 133, 248, 139, 234, 125, 233, 125, 230, 122, 229, 122, 227, 120, 226, 120, 225, 119, 224, 119, 223, 118, 221, 118, 220, 117, 215, 117, 214, 116, 207, 116, 206, 115, 193, 115, 192, 114, 172, 114, 171, 113, 133, 113, 132, 112],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, 0, -1, -1]
            }]
        }
        ...
      }
    }
}
```


The example shows the JSON objects corresponding to class `car`. It contains two contours:


- A contour for the small car at the right of the image.
- A contour for the center blob. It corresponds to two cars that are not distinguished in this type of non-instance aware semantic segmentation.

[Image: fig example semantic segmentation instance aware]

*Figure 60. Example of a semantic segmentation that is instance-aware*


Figure 60 shows the instance-aware semantic segmentation of the partial segmentation example. In this case, the source PNG image contains different colors for each instance of the class `car`.


_JSON example_


```json
{
    "objects": {
      "1": {
        "name": "instance0",
        "type": "car",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [425, 143, 424, 144, 423, 144, 422, 145, 422, 146, 419, 149, 419, 150, 418, 151, 418, 169, 421, 169, 421, 167, 422, 166, 440, 166, 441, 167, 441, 169, 445, 169, 445, 156, 446, 155, 447, 155, 447, 152, 445, 152, 444, 151, 444, 148, 442, 146, 442, 145, 440, 143],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, -1, -1, -1]
            }
          ]
        },
        ...
      },
      "2": {
        "name": "instance1",
        "type": "car",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [118, 112, 117, 113, 107, 113, 106, 114, 106, 115, 105, 116, 105, 117, 104, 118, 104, 120, 103, 121, 103, 124, 102, 125, 102, 129, 101, 130, 101, 134, 100, 135, 100, 137, 99, 138, 99, 167, 98, 168, 96, 168, 95, 169, 95, 174, 97, 176, 98, 176, 99, 177, 100, 177, 101, 178, 105, 178, 107, 180, 120, 180, 121, 181, 121, 184, 122, 185, 122, 186, 126, 190, 127, 190, 128, 191, 145, 191, 150, 186, 154, 186, 155, 187, 182, 187, 183, 188, 220, 188, 220, 184, 221, 183, 221, 181, 222, 180, 222, 179, 224, 177, 224, 176, 226, 174, 226, 173, 228, 171, 228, 170, 230, 168, 230, 167, 231, 166, 231, 165, 233, 163, 233, 162, 234, 161, 234, 160, 235, 159, 235, 158, 236, 157, 236, 156, 238, 154, 238, 153, 239, 152, 239, 151, 241, 149, 241, 148, 243, 146, 243, 145, 245, 143, 245, 142, 248, 139, 234, 125, 233, 125, 230, 122, 229, 122, 227, 120, 226, 120, 225, 119, 224, 119, 223, 118, 221, 118, 220, 117, 215, 117, 214, 116, 207, 116, 206, 115, 193, 115, 192, 114, 172, 114, 171, 113, 133, 113, 132, 112],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, -1, -1, -1]
            }
          ]
        },
        ...
      },
      "3": {
        "name": "instance2",
        "type": "car",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [267, 129, 266, 130, 261, 130, 260, 131, 257, 131, 255, 133, 254, 133, 249, 138, 249, 139, 246, 142, 246, 143, 244, 145, 244, 146, 242, 148, 242, 149, 240, 151, 240, 152, 239, 153, 239, 154, 237, 156, 237, 157, 236, 158, 236, 159, 235, 160, 235, 161, 234, 162, 234, 163, 232, 165, 232, 166, 231, 167, 231, 168, 229, 170, 229, 171, 227, 173, 227, 174, 225, 176, 225, 177, 223, 179, 223, 180, 222, 181, 222, 183, 221, 184, 221, 196, 220, 197, 220, 199, 219, 200, 219, 201, 218, 202, 218, 205, 217, 206, 217, 221, 218, 222, 218, 224, 219, 225, 219, 248, 221, 250, 221, 251, 223, 253, 235, 253, 235, 247, 236, 246, 236, 242, 238, 240, 245, 240, 246, 241, 254, 241, 255, 242, 260, 242, 261, 243, 266, 243, 267, 244, 279, 244, 280, 245, 297, 245, 298, 246, 344, 246, 345, 245, 349, 245, 350, 246, 350, 250, 349, 251, 349, 259, 363, 259, 363, 258, 364, 257, 364, 252, 365, 251, 365, 231, 366, 230, 366, 221, 367, 220, 367, 214, 368, 213, 368, 198, 367, 197, 367, 181, 362, 176, 362, 175, 361, 174, 361, 173, 362, 172, 370, 172, 371, 171, 372, 171, 373, 170, 374, 170, 374, 165, 372, 163, 362, 163, 362, 167, 361, 168, 360, 168, 359, 167, 359, 161, 358, 160, 358, 154, 357, 153, 357, 152, 356, 151, 356, 150, 354, 148, 354, 147, 353, 146, 353, 145, 352, 144, 352, 142, 350, 140, 350, 139, 348, 137, 348, 136, 344, 132, 343, 132, 342, 131, 339, 131, 338, 130, 329, 130, 328, 129],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, -1, -1, -1]
            }
          ]
        },
        ...
      }
    }
}
```


The example shows the JSON objects that represent each of the instances of the class `car`.

[Image: fig example semantic segmentation full scene segmentation non instance aware]

*Figure 61. Example of a full scene segmentation that is non instance-aware*


Figure 61 shows a complete scene segmentation example. All pixels of the image have been labeled with a certain class value.


For simplification, a reduced dictionary has been used:


- Car
- Vegetation
- Sky
- Poles
- Street
- Miscellaneous


Note that each class is given a certain RGB value at the PNG image.

[Image: fig example semantic segmentation full scene segmentation instance aware]

*Figure 62. Example of a full scene segmentation that is instance-aware*


Figure 62 shows the same complete scene segmentation example but with instance-aware coloring of instantiable classes. That means that pixels corresponding to class `car` are colored according to the instance they correspond to.


Both non-instance aware and instance-aware segmentations can be encoded together into a single ASAM OpenLABEL JSON payload. Class-level polygons, that is, non-instance aware, can be encoded as ASAM OpenLABEL objects with names that include the word `class`, and the type `car`. In addition, instance-aware shapes can be encoded as other ASAM OpenLABEL objects with names that include the name `instance` and the type `car`.


_JSON example_


```json
{
    "objects": {
      "0": {
        "name": "class0",
        "type": "car",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [425, 143, 424, 144, 423, 144, 422, 145, 422, 146, 419, 149, 419, 150, 418, 151, 418, 169, 421, 169, 421, 167, 422, 166, 440, 166, 441, 167, 441, 169, 445, 169, 445, 156, 446, 155, 447, 155, 447, 152, 445, 152, 444, 151, 444, 148, 442, 146, 442, 145, 440, 143],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [1, -1, -1, -1]
            }, {
              "name": "contour1",
              "val": [118, 112, 117, 113, 107, 113, 106, 114, 106, 115, 105, 116, 105, 117, 104, 118, 104, 120, 103, 121, 103, 124, 102, 125, 102, 129, 101, 130, 101, 134, 100, 135, 100, 137, 99, 138, 99, 167, 98, 168, 96, 168, 95, 169, 95, 174, 97,...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, 0, -1, -1]
            }
          ]
        },
        ...
      },
      "1": {
        "name": "instance0",
        "type": "car",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [425, 143, 424, 144, 423, 144, 422, 145, 422, 146, 419, 149, 419, 150, 418, 151, 418, 169, 421, 169, 421, 167, 422, 166, 440, 166, 441, 167, 441, 169, 445, 169, 445, 156, 446, 155, 447, 155, 447, 152, 445, 152, 444, 151, 444, 148, 442, 146, 442, 145, 440, 143],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, -1, -1, -1]
            }
          ]
        },
        "object_data_pointers": {
          "contour0": {
            "type": "poly2d",
            "frame_intervals": []
          }
        }
      },
      "2": {
        "name": "instance1",
        "type": "car",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [118, 112, 117, 113, 107, 113, 106, 114, 106, 115, 105, 116, 105, 117, 104, 118, 104, 120, 103, 121, 103, 124, 102, 125, 102, 129, 101, 130, 101, 134, 100, 135, 100, 137, 99, 138, 99, 167, 98, 168, 96, 168, 95, 169, 95, 174, 97, ...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, -1, -1, -1]
            }
          ]
        },
        ...
      },
      "3": {
        "name": "instance2",
        "type": "car",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [267, 129, 266, 130, 261, 130, 260, 131, 257, 131, 255, 133, 254, 133, 249, 138, 249, 139, 246, 142, 246, 143, 244, 145, 244, 146, 242, 148, 242, 149, ...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, -1, -1, -1]
            }
          ]
        },
        ...
      },
      "4": {
        "name": "class1",
        "type": "vegetation",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [381, 157, 381, 160, 384, 160, 385, 159, 383, 157],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [1, -1, -1, -1]
            }, {
              "name": "contour1",
              "val": [444, 145, 444, 147, 445, 148, 445, 151, 447, 151, 448, 152, 448, 149, 446, 149, 445, 148, 445, 145],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [2, 0, -1, -1]
            }, {
              "name": "contour2",
              "val": [376, 142, 375, 143, 373, 143, 373, 161, 375, 161, 377, 159, 379, 159, 379, 156, 378, 156, 376, 154, 376, 153, 374, 151, 374, 150, 375, 149, 378, 149, 379, 150, 379, 142],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [3, 1, -1, -1]
            }, {
              "name": "contour3",
              "val": [376, 138, 379, 138],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [4, 2, -1, -1]
            }, {
              "name": "contour4",
              "val": [361, 41, 361, 52, 362, 53, 362, 85, 363, 86, 363, 159, 366, 159, 367, 160, 371, 160, 371, 143, 369, 143, 368, 142, 368, 134, 369, 133, 375, 133, 376, 134, 379, 134, 376, 134, 375, 133, 375, 129, 376, 128, 384, 128, 385, 129, 385, 133, 384, 134, 381, 134, 384, 134, 385, 135, 385, 137, 384, 138, 381, 138, 384, ...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [5, 3, -1, -1]
            }, {
              "name": "contour5",
              "val": [3, 29, 1, 31, 0, 31, 0, 151, 3, 151, 4, 152, 7, 152, 8, 151, 21, 151, 21, 119, 22, 118, 22, 74, 23, 73, 23, 47, 24, 46, 24, 34, 23, 33, 21, 33, 21, 34, 23, 36, 23, 38, 22, 39, 21, 39, 20, 40, 19, 40, 19, 41, 16, 44, 14, 44, 10, 48, 9, 48, 8, 47, 8, 44, 7, 43, 7, 42, 8, 41, 8, 34, 7, 33, 7, 32, 6, 31, 6, 30, 5, 29],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [6, 4, -1, -1]
            }, {
              "name": "contour6",
              "val": [237, 17, 235, 19, 231, 19, 224, 26, 222, 26, 221, 27, 221, 29, 220, 30, 219, 30, 218, 31, 216, 31, 214, 33, 212, 33, 211, 34, 210, 34, 210, 36, 209, 37, 209, 39, 207, 41, 206, 41, 205, 42, 204, 42, 202, 40, 202, 36, 200, 34, 200, 33, ...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [7, 5, -1, -1]
            }, {
              "name": "contour7",
              "val": [65, 1, 64, 2, 63, 2, 62, 3, 62, 7, 60, 9, 58, 9, 57, 8, 57, 6, 56, 5, 56, 4, 55, 3, 53, 3, 51, 5, 50, 5, 50, 6, 49, 7, 49, 8, 48, 9, 48, 10, 47, 11, 47, 17, 46, 18, 44, 18, 43, 19, 34, 19, 32, 17, 31, 17, 30, 16, 26, 16, 25, 17, 25, ...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, 6, -1, -1]
            }
          ]
        },
        ...
      },
      "5": {
        "name": "class2",
        "type": "sky",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [28, 29, 27, 30, 27, 33, 28, 32, 29, 32, 30, 31, 30, 30, 29, 30],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [1, -1, -1, -1]
            }, {
              "name": "contour1",
              "val": [31, 22, 29, 24, 30, 24, 31, 23],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [2, 0, -1, -1]
            }, {
              "name": "contour2",
              "val": [125, 0, 125, 22, 125, 21, 127, 19, 133, 19, 135, 21, 135, 23, 136, 23, 139, 26, 140, 26, 141, 27, 141, 28, 142, 28, 143, 29, 143, 30, 144, 30, 144, 23, ...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [3, 1, -1, -1]
            }, {
              "name": "contour3",
              "val": [0, 0, 0, 30, 1, 30, 3, 28, 5, 28, 7, 30, 7, 31, 8, 32, 8, 33, 9, 34, 9, 41, 8, 42, 8, 43, 9, 44, 9, 47, 10, 47, 14, 43, 16, 43, 18, 41, 18, 40, 19, 39, ...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, 2, -1, -1]
            }
          ]
        },
        ...
      },
      "6": {
        "name": "class3",
        "type": "poles",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [385, 151, 385, 157],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [1, -1, -1, -1]
            }, {
              "name": "contour1",
              "val": [402, 145, 402, 151],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [2, 0, -1, -1]
            }, {
              "name": "contour2",
              "val": [394, 139, 394, 143, 395, 143, 396, 144, 396, 160, 396, 144, 397, 143, 398, 143, 398, 139],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [3, 1, -1, -1]
            }, {
              "name": "contour3",
              "val": [349, 137, 351, 139, 351, 140, 353, 142, 353, 143, 353, 137],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [4, 2, -1, -1]
            }, {
              "name": "contour4",
              "val": [446, 130, 446, 137, 445, 138, 444, 138, 443, 137, 441, 137, 440, 138, 440, 142, 443, 145, 443, 146, 443, 145, 444, 144, 445, 144, 446, 145, 446, 148, 448, 148, 449, 149, 449, 156, 449, 149, 450, 148, 452, 148, 452, 130],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [5, 3, -1, -1]
            }, {
              "name": "contour5",
              "val": [376, 129, 376, 133, 375, 134, 369, 134, 369, 142, 371, 142, 372, 143, 372, 162, 372, 143, 373, 142, 375, 142, 376, 141, 379, 141, 380, 142, 380, 161, 380, 142, 381, 141, 384, 141, 384, 139, 381, 139, 380, 138, 381, 137, 384, 137, 384, 135, 381, 135, 380, 134, 381, 133, 384, 133, 384, 129],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [8, 4, 6, -1]
            }, {
              "name": "contour6",
              "val": [375, 138, 376, 137, 379, 137, 380, 138, 379, 139, 376, 139],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [7, -1, -1, 5]
            }, {
              "name": "contour7",
              "val": [375, 134, 376, 133, 379, 133, 380, 134, 379, 135, 376, 135],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, 6, -1, 5]
            }, {
              "name": "contour8",
              "val": [25, 20, 24, 21, 23, 21, 24, 22, 24, 23, 25, 24, 25, 46, 24, 47, 24, 73, 23, 74, 23, 118, 22, 119, 22, 151, 24, 151, 24, 110, 25, 109, 25, 72, 26, 71, 26, 30, 27, 29, 27, 26, 28, 25, 28, 24, 30, 22, 30, 21, 29, 21, 28, 20],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [9, 5, -1, -1]
            }, {
              "name": "contour9",
              "val": [363, 14, 362, 15, 360, 15, 359, 16, 359, 17, 358, 18, 354, 18, 353, 17, 352, 17, 351, 18, 347, 18, 347, 20, 352, 20, 353, 21, 358, 21, 359, 22, 359, 65, 360, 66, 360, 163, 361, 164, 361, 163, 362, 162, 362, 86, 361, 85, 361, 53, 360, 52, 360, 21, 361, 20, 362, 20, 365, 17, 367, 17, 368, 16, 371, 16, 371, 15, 370, 14, 369, 15, 366, 15, 365, 14],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [10, 8, -1, -1]
            }, {
              "name": "contour10",
              "val": [114, 0, 114, 22, 113, 23, 113, 66, 112, 67, 112, 102, 111, 103, 111, 112, 117, 112, 118, 111, 122, 111, 122, 61, 123, 60, 123, 29, 124, 28, 124, 0],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, 9, -1, -1]
            }
          ]
        },
        ...
      },
      "7": {
        "name": "class4",
        "type": "miscellaneous",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [458, 166, 457, 167, 456, 167, 456, 168, 457, 169, 470, 169, 470, 166],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [1, -1, -1, -1]
            }, {
              "name": "contour1",
              "val": [370, 161, 371, 161],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [2, 0, -1, -1]
            }, {
              "name": "contour2",
              "val": [377, 160, 379, 160],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [3, 1, -1, -1]
            }, {
              "name": "contour3",
              "val": [363, 160, 363, 161, 366, 161, 366, 160],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [4, 2, -1, -1]
            }, {
              "name": "contour4",
              "val": [359, 160],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [5, 3, -1, -1]
            }, {
              "name": "contour5",
              "val": [381, 155, 381, 156, 383, 156, 386, 159, 384, 161, 383, 161, 385, 161, 386, 162, 388, 162, 389, 163, 390, 163, 391, 164, 396, 164, 397, 165, 403, 165, 404, 164, 404, 163, 405, 162, 403, 160, 401, 160, 400, 159, 398, 159, 397, 158, 397, 160, 396, 161, 395, 160, 395, 158, 394, 157, 391, 157, 390, 156, 387, 156, 386, 155, 386, 157, 385, 158, 384, 157, 384, 155],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [6, 4, -1, -1]
            }, {
              "name": "contour6",
              "val": [450, 154, 450, 156, 451, 156, 452, 157, 453, 157, 454, 158, 456, 158, 457, 159, 458, 159, 459, 160, 460, 160, 461, 161, 463, 161, 464, 162, 470, 162, 470, 159, 469, 159, 467, 157, 464, 157, 463, 158, 463, 160, 462, 161, 461, 161, 459, 159, 458, 159, 455, 156, 453, 156, 452, 155, 451, 155],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [7, 5, -1, -1]
            }, {
              "name": "contour7",
              "val": [448, 153, 448, 156],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [8, 6, -1, -1]
            }, {
              "name": "contour8",
              "val": [382, 150],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [9, 7, -1, -1]
            }, {
              "name": "contour9",
              "val": [375, 150, 375, 151, 377, 153, 377, 154, 378, 155, 379, 155, 379, 154, 378, 153, 378, 152, 379, 151, 378, 150],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [10, 8, -1, -1]
            }, {
              "name": "contour10",
              "val": [386, 149, 388, 149],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [11, 9, -1, -1]
            }, {
              "name": "contour11",
              "val": [403, 147, 403, 150, 406, 150, 407, 151, 410, 151, 411, 152, 414, 152, 415, 153, 417, 153, 417, 151, 418, 150, 418, 149, 416, 149, 415, 148, 410, 148, 409, 147],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [12, 10, -1, -1]
            }, {
              "name": "contour12",
              "val": [399, 143, 398, 144, 397, 144, 397, 149, 401, 149, 401, 146, 400, 145, 400, 143],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [13, 11, -1, -1]
            }, {
              "name": "contour13",
              "val": [392, 143, 391, 144, 391, 146, 392, 147, 391, 148, 395, 148, 395, 144, 394, 144, 393, 143],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [14, 12, -1, -1]
            }, {
              "name": "contour14",
              "val": [73, 128, 73, 130, 69, 134, 67, 134, 65, 136, 61, 136, 60, 135, 51, 135, 50, 136, 49, 136, 48, 137, 47, 137, 48, 138, 48, 142, 47, 143, 47, 147, 56, 147, 57, 148, 62, 148, 63, 149, 61, 151, 25, 151, 24, 152, 8, 152, 7, 153, 4, 153, 3, 152, 0, 152, 0, 166, 18, 166, 19, 167, 53, 167, 54, 168, 94, 168, 95, 167, 98, 167, 98, 148, 97, 147, 97, 140, 89, 140, 88, 139, 88, 137, 83, 137, 82, 136, 82, 134, 83, 133, 84, 133, 85, 132, 86, 132, 86, 131, 83, 131, 80, 134, 79, 134, 76, 131, 76, 130, 74, 128],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, 13, -1, -1]
            }
          ]
        },
        ...
      },
      "8": {
        "name": "class5",
        "type": "street",
        "object_data": {
          "poly2d": [{
              "name": "contour0",
              "val": [360, 164, 360, 167, 361, 167, 361, 165],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [1, -1, -1, -1]
            }, {
              "name": "contour1",
              "val": [367, 161, 366, 162, 363, 162, 371, 162, 370, 162, 369, 161],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [2, 0, -1, -1]
            }, {
              "name": "contour2",
              "val": [379, 152, 379, 153],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [3, 1, -1, -1]
            }, {
              "name": "contour3",
              "val": [397, 150, 397, 157, 398, 158, 400, 158, 401, 159, 403, 159, 406, 162, 405, 163, 405, 164, 403, 166, 397, 166, 396, 165, 391, 165, 390, 164, 389, 164, 388, 163, 386, 163, 385, 162, 383, 162, 382, 161, 381, 161, 380, 162, 379, 161, ...],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [4, 2, -1, -1]
            }, {
              "name": "contour4",
              "val": [389, 149, 388, 150, 383, 150, 382, 151, 381, 151, 381, 154, 384, 154, 384, 151, 385, 150, 386, 151, 386, 154, 387, 155, 390, 155, 391, 156, 394, 156, 395, 157, 395, 149],
              "mode": "MODE_POLY2D_ABSOLUTE",
              "closed": true,
              "hierarchy": [-1, 3, -1, -1]
            }
          ]
        },
        ...
      }
    }
}
```


The example shows the non-instance aware and instance-aware objects together in the same JSON payload. The long polygon’s coordinate arrays have been customized for better visualization.


> **NOTE**: There are different encoding options in ASAM OpenLABEL. Absolute coordinates may be used to maintain some level of human readability. However, applying chain encoding mechanisms significantly compact the representation of the coordinates. In addition, the third option is to encode the entire source PNG image as a base64 payload and embed it into a ASAM OpenLABEL object.
