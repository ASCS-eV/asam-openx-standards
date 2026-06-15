# ASAM OpenLABEL v1.0.0 — 9. References

- **Source**: ASAM_OpenLABEL_BS_V1-0-0.html
- **Version**: v1.0.0
- **Date**: November 9, 2021
- **License**: Restricted distribution (ASAM e.V. member access)

---

## 9. References


### 9.1. Classes


```
action
```


An action is a type of element intended to describe temporal situations with semantic load as a certain activity happening in real life, such as crossing-zebra-cross, standing-still, playing-guitar. As such, actions are defined by their type, the frame intervals in which the action happens, and any additional action data, for example, numbers, booleans, text as attributes of the actions.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 75. Diagram of the action class*


*Table 31. Properties of the action class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| action_data |  |  | #/definitions/action_data | Additional data to describe attributes of the action. |
| action_data_pointers |  |  | #/definitions/element_data_pointers | This is a JSON object which contains OpenLABEL element data pointers. Element data pointer keys shall be the "name" of the element data this pointer points to. |
| frame_intervals | array |  | #/definitions/frame_interval | The array of frame intervals where this action exists or is defined. |
| name | string | true |  | Name of the action. It is a friendly name and not used for indexing. |
| ontology_uid | string |  |  | This is the UID of the ontology where the type of this action is defined. |
| resource_uid |  |  | #/definitions/resource_uid | This is a JSON object that contains links to external resources. Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource_uid values are strings describing the identifier of the element in the external resource. |
| type | string | true |  | The type of an action defines the class the action corresponds to. |


```
action_data
```


Additional data to describe attributes of the action.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 76. Diagram of the action data class*


*Table 32. Properties of the action data class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| boolean | array | #/definitions/boolean | List of "boolean" that describe this action. |
| num | array | #/definitions/num | List of "num" that describe this action. |
| text | array | #/definitions/text | List of "text" that describe this action. |
| vec | array | #/definitions/vec | List of "vec" that describe this action. |


```
area_reference
```


An area reference is a JSON object which defines the area of a set of 3D line segments by means of defining the indexes of all lines which outline the area. Note that coplanar 3D lines are assumed.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 77. Diagram of the area reference class*


*Table 33. Properties of the area reference class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| attributes |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| name | string |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| reference_type | string |  | This is the type of the reference as a string with the name of the element data (e.g. line_reference) |
| val | array |  | The array of indexes of the references of type reference_type. |


```
attributes
```


Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 78. Diagram of the attributes class*


*Table 34. Properties of the attributes class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| boolean | array | #/definitions/boolean | A boolean. |
| num | array | #/definitions/num | A number. |
| text | array | #/definitions/text | A text. |
| vec | array | #/definitions/vec | A vector (list) of numbers or strings. |


```
bbox
```


A 2D bounding box is defined as a 4-dimensional vector [x, y, w, h], where [x, y] is the center of the bounding box and [w, h] represent the width (horizontal, x-coordinate dimension) and height (vertical, y-coordinate dimension), respectively.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 79. Diagram of the bbox class*


*Table 35. Properties of the bbox class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | The array of 4 values that define the [x, y, w, h] values of the bbox. |


```
binary
```


A binary payload.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 80. Diagram of the binary class*


*Table 36. Properties of the binary class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| data_type | string | true |  | This is a string that declares the type of the values of the binary object. |
| encoding | string | true |  | This is a string that declares the encoding type of the bytes for this binary payload, for example, "base64". |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | string | true |  | A string with the encoded bytes of this binary payload. |


```
boolean
```


A boolean.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 81. Diagram of the boolean class*


*Table 37. Properties of the boolean class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| type | string |  |  | This attribute specifies how the boolean shall be considered. In this schema the only possible option is as a value. |
| val | boolean | true |  | The boolean value. |


```
context
```


A context is a type of element which defines any nonspatial or temporal annotation. Contexts can be used to add richness to the contextual information of a scene, including location, weather, application-related information.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 82. Diagram of the context class*


*Table 38. Properties of the context class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| context_data |  |  | #/definitions/context_data | Additional data to describe attributes of the context. |
| context_data_pointers |  |  | #/definitions/element_data_pointers | This is a JSON object which contains OpenLABEL element data pointers. Element data pointer keys shall be the "name" of the element data this pointer points to. |
| frame_intervals | array |  | #/definitions/frame_interval | The array of frame intervals where this context exists or is defined. |
| name | string | true |  | Name of the context. It is a friendly name and not used for indexing. |
| ontology_uid | string |  |  | This is the UID of the ontology where the type of this context is defined. |
| resource_uid |  |  | #/definitions/resource_uid | This is a JSON object that contains links to external resources. Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource_uid values are strings describing the identifier of the element in the external resource. |
| type | string | true |  | The type of a context defines the class the context corresponds to. |


```
context_data
```


Additional data to describe attributes of the context.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 83. Diagram of the context data class*


*Table 39. Properties of the context data class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| boolean | array | #/definitions/boolean | List of "boolean" that describe this context. |
| num | array | #/definitions/num | List of "num" that describe this context. |
| text | array | #/definitions/text | List of "text" that describe this context. |
| vec | array | #/definitions/vec | List of "vec" that describe this context. |


```
coordinate_system
```


A coordinate system is a 3D reference frame. Spatial information on objects and their properties can be defined with respect to coordinate systems.


| Additional properties: | true |
| --- | --- |

[Image: Diagram]

*Figure 84. Diagram of the coordinate system class*


*Table 40. Properties of the coordinate system class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| children | array |  |  | List of children of this coordinate system. |
| parent | string | true |  | This is the string UID of the parent coordinate system this coordinate system is referring to. |
| pose_wrt_parent |  |  | #/definitions/transform_data | JSON object containing the transform data. |
| type | string | true |  | This is a string that describes the type of the coordinate system, for example, "local", "geo"). |


```
coordinate_systems
```


This is a JSON object which contains OpenLABEL coordinate systems. Coordinate system keys can be any string, for example, a friendly coordinate system name.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 85. Diagram of the coordinate systems class*


```
cuboid
```


A cuboid or 3D bounding box. It is defined by the position of its center, the rotation in 3D, and its dimensions.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 86. Diagram of the cuboid class*


*Table 41. Properties of the cuboid class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val |  | true |  | List of values encoding the position, rotation and dimensions. Two options are supported, using 9 or 10 values. If 9 values are used, the format is (x, y, z, rx, ry, rz, sx, sy, sz), where (x, y, z) encodes the position, (rx, ry, rz) encodes the Euler angles that encode the rotation, and (sx, sy, sz) are the dimensions of the cuboid in its object coordinate system. If 10 values are used, then the format is (x, y, z, qx, qy, qz, qw, sx, sy, sz) with the only difference of the rotation values which are the 4 values of a quaternion. |


```
element_data_pointer
```


This item contains pointers to element data of elements, indexed by "name", and containing information about the element data type, for example, bounding box, cuboid, and the frame intervals in which this element_data exists within an element. That means, these pointers can be used to explore element data dynamic information within the JSON content.


| Type: | object |
| --- | --- |

[Image: Diagram]

*Figure 87. Diagram of the element data pointer class*


*Table 42. Properties of the element data pointer class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attribute_pointers | object |  |  | This is a JSON object which contains pointers to the attributes of the element data pointed by this pointer. The attributes pointer keys shall be the "name" of the attribute of the element data this pointer points to. |
| frame_intervals | array | true | #/definitions/frame_interval | List of frame intervals of the element data pointed by this pointer. |
| type | string |  |  | Type of the element data pointed by this pointer. |


```
element_data_pointers
```


This is a JSON object which contains OpenLABEL element data pointers. Element data pointer keys shall be the "name" of the element data this pointer points to.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 88. Diagram of the element data pointers class*


```
event
```


An event is an instantaneous situation that happens without a temporal interval. Events complement actions providing a mechanism to specify triggers or to connect actions and objects with causality relations.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 89. Diagram of the event class*


*Table 43. Properties of the event class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| event_data |  |  | #/definitions/event_data | Additional data to describe attributes of the event. |
| event_data_pointers |  |  | #/definitions/element_data_pointers | This is a JSON object which contains OpenLABEL element data pointers. Element data pointer keys shall be the "name" of the element data this pointer points to. |
| frame_intervals | array |  | #/definitions/frame_interval | The array of frame intervals where this event exists or is defined. Note that events are thought to be instantaneous. That means, they are defined for a single frame interval where the starting and ending frames are the same. |
| name | string | true |  | Name of the event. It is a friendly name and not used for indexing. |
| ontology_uid | string |  |  | This is the UID of the ontology where the type of this event is defined. |
| resource_uid |  |  | #/definitions/resource_uid | This is a JSON object that contains links to external resources. Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource_uid values are strings describing the identifier of the element in the external resource. |
| type | string | true |  | The type of an event defines the class the event corresponds to. |


```
event_data
```


Additional data to describe attributes of the event.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 90. Diagram of the event data class*


*Table 44. Properties of the event data class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| boolean | array | #/definitions/boolean | List of "boolean" that describe this event. |
| num | array | #/definitions/num | List of "num" that describe this event. |
| text | array | #/definitions/text | List of "text" that describe this event. |
| vec | array | #/definitions/vec | List of "vec" that describe this event. |


```
frame
```


A frame is a container of dynamic, timewise, information.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 91. Diagram of the frame class*


*Table 45. Properties of the frame class*

| Name | Type | Additional properties | Reference | Description |
| --- | --- | --- | --- | --- |
| actions | object | false | #/definitions/action_data | This is a JSON object that contains dynamic information on OpenLABEL actions. Action keys are strings containing numerical UIDs or 32 bytes UUIDs. Action values may contain an "action_data" JSON object. |
| contexts | object | false | #/definitions/context_data | This is a JSON object that contains dynamic information on OpenLABEL contexts. Context keys are strings containing numerical UIDs or 32 bytes UUIDs. Context values may contain a "context_data" JSON object. |
| events | object | false | #/definitions/event_data | This is a JSON object that contains dynamic information on OpenLABEL events. Event keys are strings containing numerical UIDs or 32 bytes UUIDs. Event values may contain an "event_data" JSON object. |
| frame_properties | object | true | #/definitions/stream | This is a JSON object which contains information about this frame. |
| objects | object | false | #/definitions/object_data | This is a JSON object that contains dynamic information on OpenLABEL objects. Object keys are strings containing numerical UIDs or 32 bytes UUIDs. Object values may contain an "object_data" JSON object. |
| relations | object | false |  | This is a JSON object that contains dynamic information of OpenLABEL relations. Relation keys are strings containing numerical UIDs or 32 bytes UUIDs. Relation values are empty. The presence of a key-value relation pair indicates the specified relation exists in this frame. |


```
frame_interval
```


A frame interval defines a starting and ending frame number as a closed interval. That means the interval includes the limit frame numbers.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 92. Diagram of the frame interval class*


*Table 46. Properties of the frame interval class*

| Name | Type | Description |
| --- | --- | --- |
| frame_end | integer | Ending frame number of the interval. |
| frame_start | integer | Initial frame number of the interval. |


```
image
```


An image.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 93. Diagram of the image class*


*Table 47. Properties of the image class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| encoding | string | true |  | This is a string that declares the encoding type of the bytes for this image, for example, "base64". |
| mime_type | string | true |  | This is a string that declares the MIME (multipurpose internet mail extensions) of the image, for example, "image/gif". |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | string | true |  | A string with the encoded bytes of this image. |


```
line_reference
```


A line reference is a JSON object which defines a 3D line segment by means of defining the indexes of its two extreme points.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 94. Diagram of the line reference class*


*Table 48. Properties of the line reference class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| attributes |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| name | string |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| reference_type | string |  | This is the type of the reference as a string with the name of the element data (e.g. point3d) |
| val | array |  | The array of indexes of the references of type reference_type. |


```
mat
```


A matrix.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 95. Diagram of the mat class*


*Table 49. Properties of the mat class*

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
mesh
```


A mesh encodes a point-line-area structure. It is intended to represent flat 3D meshes, such as several connected parking lots, where points, lines and areas composing the mesh are interrelated and can have their own properties.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 96. Diagram of the mesh class*


*Table 50. Properties of the mesh class*

| Name | Type | Additional properties | Reference | Description |
| --- | --- | --- | --- | --- |
| area_reference | object | false | #/definitions/area_reference | This is the JSON object for the areas defined for this mesh. Area keys are strings containing numerical UIDs. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| line_reference | object | false | #/definitions/line_reference | This is the JSON object for the 3D lines defined for this mesh. Line reference keys are strings containing numerical UIDs. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| point3d | object | false | #/definitions/point3d | This is the JSON object for the 3D points defined for this mesh. Point3d keys are strings containing numerical UIDs. |


```
metadata
```


This JSON object contains information, that is, metadata, about the annotation file itself.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 97. Diagram of the metadata class*


*Table 51. Properties of the metadata class*

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| annotator | string |  | Name or description of the annotator that created the annotations. |
| comment | string |  | Additional information or description about the annotation content. |
| file_version | string |  | Version number of the OpenLABEL annotation content. |
| name | string |  | Name of the OpenLABEL annotation content. |
| schema_version | string | true | Version number of the OpenLABEL schema this annotation JSON object follows. |
| tagged_file | string |  | File name or URI of the data file being tagged. |


```
num
```


A number.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 98. Diagram of the num class*


*Table 52. Properties of the num class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| type | string |  |  | This attribute specifies whether the number shall be considered as a value, a minimum, or a maximum in its context. |
| val | number | true |  | The numerical value of the number. |


```
object
```


An object is the main type of annotation element. Object is designed to represent spatiotemporal entities, such as physical objects in the real world. Objects shall have a name and type. Objects may have static and dynamic data. Objects are the only type of elements that may have geometric data, such as bounding boxes, cuboids, polylines, images, etc.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 99. Diagram of the object class*


*Table 53. Properties of the object class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| coordinate_system | string |  |  | This is the string key of the coordinate system this object is referenced with respect to. |
| frame_intervals | array |  | #/definitions/frame_interval | The array of frame intervals where this object exists or is defined. |
| name | string | true |  | Name of the object. It is a friendly name and not used for indexing. |
| object_data |  |  | #/definitions/object_data | Additional data to describe attributes of the object. |
| object_data_pointers |  |  | #/definitions/element_data_pointers | This is a JSON object which contains OpenLABEL element data pointers. Element data pointer keys shall be the "name" of the element data this pointer points to. |
| ontology_uid | string |  |  | This is the UID of the ontology where the type of this object is defined. |
| resource_uid |  |  | #/definitions/resource_uid | This is a JSON object that contains links to external resources. Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource_uid values are strings describing the identifier of the element in the external resource. |
| type | string | true |  | The type of an object defines the class the object corresponds to. |


```
object_data
```


Additional data to describe attributes of the object.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 100. Diagram of the object data class*


*Table 54. Properties of the object data class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| area_reference | array | #/definitions/area_reference | List of "area_reference" that describe this object. |
| bbox | array | #/definitions/bbox | List of "bbox" that describe this object. |
| binary | array | #/definitions/binary | List of "binary" that describe this object. |
| boolean | array | #/definitions/boolean | List of "boolean" that describe this object. |
| cuboid | array | #/definitions/cuboid | List of "cuboid" that describe this object. |
| image | array | #/definitions/image | List of "image" that describe this object. |
| line_reference | array | #/definitions/line_reference | List of "line_reference" that describe this object. |
| mat | array | #/definitions/mat | List of "mat" that describe this object. |
| mesh | array | #/definitions/mesh | List of "mesh" that describe this object. |
| num | array | #/definitions/num | List of "num" that describe this object. |
| point2d | array | #/definitions/point2d | List of "point2d" that describe this object. |
| point3d | array | #/definitions/point3d | List of "point3d" that describe this object. |
| poly2d | array | #/definitions/poly2d | List of "poly2d" that describe this object. |
| poly3d | array | #/definitions/poly3d | List of "poly3d" that describe this object. |
| rbbox | array | #/definitions/rbbox | List of "rbbox" that describe this object. |
| text | array | #/definitions/text | List of "text" that describe this object. |
| vec | array | #/definitions/vec | List of "vec" that describe this object. |


```
ontologies
```


This is the JSON object of OpenLABEL ontologies. Ontology keys are strings containing numerical UIDs or 32 bytes UUIDs. Ontology values may be strings, for example, encoding a URI. JSON objects containing a URI string and optional lists of included and excluded terms.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 101. Diagram of the ontologies class*


```
openlabel
```


The OpenLABEL root JSON object, which contains all other JSON objects.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 102. Diagram of the openlabel class*


*Table 55. Properties of the openlabel class*

| Name | Type | Required | Additional properties | Reference | Description |
| --- | --- | --- | --- | --- | --- |
| actions | object |  | false | #/definitions/action | This is the JSON object of OpenLABEL actions. Action keys are strings containing numerical UIDs or 32 bytes UUIDs. |
| contexts | object |  | false | #/definitions/context | This is the JSON object of OpenLABEL contexts. Context keys are strings containing numerical UIDs or 32 bytes UUIDs. |
| coordinate_systems |  |  |  | #/definitions/coordinate_systems | This is a JSON object which contains OpenLABEL coordinate systems. Coordinate system keys can be any string, for example, a friendly coordinate system name. |
| events | object |  | false | #/definitions/event | This is the JSON object of OpenLABEL events. Event keys are strings containing numerical UIDs or 32 bytes UUIDs. |
| frame_intervals | array |  |  | #/definitions/frame_interval | This is an array of frame intervals. |
| frames | object |  | false | #/definitions/frame | This is the JSON object of frames that contain the dynamic, timewise, annotations. Keys are strings containing numerical frame identifiers, which are denoted as master frame numbers. |
| metadata |  | true |  | #/definitions/metadata | This JSON object contains information, that is, metadata, about the annotation file itself. |
| objects | object |  | false | #/definitions/object | This is the JSON object of OpenLABEL objects. Object keys are strings containing numerical UIDs or 32 bytes UUIDs. |
| ontologies |  |  |  | #/definitions/ontologies | This is the JSON object of OpenLABEL ontologies. Ontology keys are strings containing numerical UIDs or 32 bytes UUIDs. Ontology values may be strings, for example, encoding a URI. JSON objects containing a URI string and optional lists of included and excluded terms. |
| relations | object |  | false | #/definitions/relation | This is the JSON object of OpenLABEL relations. Relation keys are strings containing numerical UIDs or 32 bytes UUIDs. |
| resources |  |  |  | #/definitions/resources | This is the JSON object of OpenLABEL resources. Resource keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource values are strings that describe an external resource, for example, file name, URLs, that may be used to link data of the OpenLABEL annotation content with external existing content. |
| streams |  |  |  | #/definitions/streams | This is a JSON object which contains OpenLABEL streams. Stream keys can be any string, for example, a friendly stream name. |
| tags | object |  | false | #/definitions/tag | This is the JSON object of tags. Tag keys are strings containing numerical UIDs or 32 bytes UUIDs. |


```
point2d
```


A 2D point.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 103. Diagram of the point2d class*


*Table 56. Properties of the point2d class*

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

*Figure 104. Diagram of the point3d class*


*Table 57. Properties of the point3d class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| id | integer |  |  | This is an integer identifier of the point in the context of a set of points. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | List of three coordinates to define the point, for example, x, y, z. |


```
poly2d
```


A 2D polyline defined as a sequence of 2D points.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 105. Diagram of the poly2d class*


*Table 58. Properties of the poly2d class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| closed | boolean | true |  | A boolean that defines whether the polyline is closed or not. In case it is closed, it is assumed that the last point of the sequence is connected with the first one. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| hierarchy | array |  |  | Hierarchy of the 2D polyline in the context of a set of 2D polylines. |
| mode | string | true |  | Mode of the polyline list of values: "MODE_POLY2D_ABSOLUTE" determines that the poly2d list contains the sequence of (x, y) values of all points of the polyline. "MODE_POLY2D_RELATIVE" specifies that only the first point of the sequence is defined with its (x, y) values, while all the rest are defined relative to it. "MODE_POLY2D_SRF6DCC" specifies that SRF6DCC chain code method is used. "MODE_POLY2D_RS6FCC" specifies that the RS6FCC method is used. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val |  | true |  | List of numerical values of the polyline, according to its mode. |


```
poly3d
```


A 3D polyline defined as a sequence of 3D points.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 106. Diagram of the poly3d class*


*Table 59. Properties of the poly3d class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| closed | boolean | true |  | A boolean that defines whether the polyline is closed or not. In case it is closed, it is assumed that the last point of the sequence is connected with the first one. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | List of numerical values of the polyline, according to its mode. |


```
rbbox
```


A 2D rotated bounding box is defined as a 5-dimensional vector [x, y, w, h, alpha], where [x, y] is the center of the bounding box and [w, h] represent the width (horizontal, x-coordinate dimension) and height (vertical, y-coordinate dimension), respectively. The angle alpha, in radians, represents the rotation of the rotated bounding box, and is defined as a right-handed rotation, that is, positive from x to y axes, and with the origin of rotation placed at the center of the bounding box (that is, [x, y]).


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 107. Diagram of the rbbox class*


*Table 60. Properties of the rbbox class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string | true |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| val | array | true |  | The array of 5 values that define the [x, y, w, h, alpha] values of the bbox. |


```
rdf_agent
```


An RDF agent is either an RDF semantic object or subject.


| Type: | object |
| --- | --- |

[Image: Diagram]

*Figure 108. Diagram of the rdf agent class*


*Table 61. Properties of the rdf agent class*

| Name | Type | Description |
| --- | --- | --- |
| type | string | The OpenLABEL type of element. |
| uid | string | The element UID this RDF agent refers to. |


```
relation
```


A relation is a type of element which connects two or more other elements, for example, objects, actions, contexts, or events. RDF triples are used to structure the connection with one or more subjects, a predicate, and one or more semantic objects.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 109. Diagram of the relation class*


*Table 62. Properties of the relation class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| frame_intervals | array |  | #/definitions/frame_interval | The array of frame intervals where this relation exists or is defined. |
| name | string | true |  | Name of the relation. It is a friendly name and not used for indexing. |
| ontology_uid | string |  |  | This is the UID of the ontology where the type of this relation is defined. |
| rdf_objects | array | true | #/definitions/rdf_agent | This is the list of RDF semantic objects of this relation. |
| rdf_subjects | array | true | #/definitions/rdf_agent | This is the list of RDF semantic subjects of this relation. |
| resource_uid |  |  | #/definitions/resource_uid | This is a JSON object that contains links to external resources. Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource_uid values are strings describing the identifier of the element in the external resource. |
| type | string | true |  | The type of a relation defines the class the predicated of the relation corresponds to. |


```
resource_uid
```


This is a JSON object that contains links to external resources. Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource_uid values are strings describing the identifier of the element in the external resource.


| Type: | object |
| --- | --- |

[Image: Diagram]

*Figure 110. Diagram of the resource uid class*


```
resources
```


This is the JSON object of OpenLABEL resources. Resource keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource values are strings that describe an external resource, for example, file name, URLs, that may be used to link data of the OpenLABEL annotation content with external existing content.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 111. Diagram of the resources class*


```
stream
```


A stream describes the source of a data sequence, usually a sensor.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 112. Diagram of the stream class*


*Table 63. Properties of the stream class*

| Name | Type | Reference | Description |
| --- | --- | --- | --- |
| description | string |  | Description of the stream. |
| stream_properties |  | #/definitions/stream_properties | Additional properties of the stream. |
| type | string |  | A string encoding the type of the stream. |
| uri | string |  | A string encoding the URI, for example, a URL, or file name, for example, a video file name, the stream corresponds to. |


```
stream_properties
```


Additional properties of the stream.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 113. Diagram of the stream properties class*


```
streams
```


This is a JSON object which contains OpenLABEL streams. Stream keys can be any string, for example, a friendly stream name.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 114. Diagram of the streams class*


```
tag
```


A tag is a special type of label that can be attached to any type of content, such as images, data containers, folders. In ASAM OpenLABEL the main purpose of a tag is to allow adding metadata to scenario descriptions.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 115. Diagram of the tag class*


*Table 64. Properties of the tag class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| ontology_uid | string | true |  | This is the UID of the ontology where the type of this tag is defined. |
| resource_uid |  |  | #/definitions/resource_uid | This is a JSON object that contains links to external resources. Resource_uid keys are strings containing numerical UIDs or 32 bytes UUIDs. Resource_uid values are strings describing the identifier of the element in the external resource. |
| tag_data |  |  | #/definitions/tag_data | Tag data can be a JSON object or a string which contains additional information about this tag. |
| type | string | true |  | The type of a tag defines the class the tag corresponds to. |


```
tag_data
```


Tag data can be a JSON object or a string which contains additional information about this tag.

[Image: Diagram]

*Figure 116. Diagram of the tag data class*


```
text
```


A text.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 117. Diagram of the text class*


*Table 65. Properties of the text class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| type | string |  |  | This attribute specifies how the text shall be considered. The only possible option is as a value. |
| val | string | true |  | The characters of the text. |


```
transform
```


This is a JSON object with information about this transform.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 118. Diagram of the transform class*


*Table 66. Properties of the transform class*

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

*Figure 119. Diagram of the transform data class*


```
vec
```


A vector (list) of numbers or strings.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 120. Diagram of the vec class*


*Table 67. Properties of the vec class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| type | string |  |  | This attribute specifies whether the vector shall be considered as a descriptor of individual values or as a definition of a range. |
| val | array | true |  | The numerical values of the vector (list) of numbers. |
