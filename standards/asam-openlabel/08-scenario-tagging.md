# ASAM OpenLABEL v1.0.0 — 8. Scenario tagging

- **Source**: ASAM_OpenLABEL_BS_V1-0-0.html
- **Version**: v1.0.0
- **Date**: November 9, 2021
- **License**: Restricted distribution (ASAM e.V. member access)

---

## 8. Scenario tagging


### 8.1. Introduction


Tagging scenarios means enriching raw data with additional metadata. In the context of ASAM OpenLABEL these metadata are called tags. Tags provide high-level information related to the content of the scenario. Tags help to describe the scenario and act as keywords for searching and filtering scenarios within scenario databases. Tags refer to the whole container of information and do not include spatiotemporal, geometric, or other constructs utilized to isolate and localize the tagged concepts within the raw data.


Additionally, tags may also be relevant for training, validating, and testing specific machine-learning classification algorithms.


This chapter covers scenario tagging in detail, including the following topics:


- The ontology providing the set of standardized ASAM OpenLABEL scenario tags.
- The semantics and the logic governing the semantics of the ASAM OpenLABEL scenario tags.
- The annotation schema to which valid ASAM OpenLABEL scenario tagging annotation instances should conform to.
- The mechanisms that govern the reference to external knowledge repositories, such as ontologies, that organize and define the semantics of the labels.


_Related deliverables_


- openlabel_json_schema.json
- openlabel_ontology_scenario_tags.ttl


_Related topics_


- Introduction
- Scope
- Conceptual overview


#### 8.1.1. Raw data sources for scenario tagging


Examples for raw data sources:


- Test scenario files for simulation, for example OSC, M-SDL, Safety Pool SDL, Geoscenario, and other files describing simulation scenarios.
- Sensor data streams, similarly to the multi-sensor data labeling use case. Examples are images, videos, and point clouds.
- Valid ASAM OpenLABEL multi-sensor data labeling annotation instances can also be used as raw data to which additional scenario tagging metadata apply.


### 8.2. Tagging semantics


ASAM OpenLABEL assumes the use of an external knowledge repository, for example, an ontology, where the tags are organized, their semantics is defined, and values for tags are also defined, where relevant.


This section provides the following:


- A description of the ASAM OpenLABEL scenario tagging ontology organizing the set of standardized tags for ASAM OpenLABEL.
- A description of the mechanisms used to define the subset(s) of the ontology that are considered in a specific tagging instance, together with the logic that governs the interpretation of missing tags.
- A description of the mechanisms used to assign valid tag values from the ontology and how to deal with the semantics of multiple values per single tag.


#### 8.2.1. ASAM OpenLABEL tags


The ASAM OpenLABEL tags are the reference set of tags used to provide a summary of the content of a scenario which may be represented as a scenario definition in some Scenario Definition Language (SDL) or some sensor data.


Scenario tagging provides a summary of the scenario and is not intended to be used for identifying individual objects or actors within a scenario. Tagging at this level of detail is provided by ASAM OpenLABEL Multi-sensor data labeling.


The ASAM OpenLABEL tags are organized into three categories which can be used to describe different aspects of a scenario.


- Operational Design Domain (ODD) tags: ODD tags describe the environmental conditions and road features present in a scenario, such as rainfall and junction. The ASAM OpenLABEL ODD tags are aligned with and share their definitions with the BSI PAS 1883 ODD Taxonomy [10].
- Behavior tags: Behavior tags describe the types of road users and the behaviors exhibited by them in a scenario, such as a pedestrian who is walking.
- Administration tags: Administration tags describe the qualities of a scenario which cannot or may not easily be derived from a scenario, such as the creation date of a scenario.


_Related topics_


- Scenario Tagging
- Normative references


##### Tag structure


Within the ODD and Behavior categories, and where applicable in the Administration category, tags are organized into a hierarchical structure with their position in the hierarchy reflecting the generality of a tag. Generality increases up the hierarchy, while specificity increases down the hierarchy, for example:


```text
scenery
|-junction
|--roundabout
|---large roundabout
```


The example shows that `large roundabout` is at the lowest position in the hierarchy as it is the most specific form of `roundabout`. When moving up the hierarchy, the tags become less specific and more general.


This hierarchical relationship between tags is a fundamental concept as it makes it possible to draw inferences about scenario content, for example, if a scenario is tagged with `large roundabout`. Then the hierarchical relationships can be applied and it is possible to infer the more general statement that the scenario contains a `roundabout`. Going further, it is possible to infer the even more general statement that it contains a `junction`.


Applying inferencing in this way means that when tagging a scenario, only tags using the most specific tags that are applicable need to be applied. It becomes unnecessary to apply the more general tags which can be inferred.


This allows for more concise scenario tagging and efficient storage because unnecessary tags do not have to be stored. This bottom-up approach of selecting only the most specific tags which apply means only a minimal set of tags are needed to tag a scenario, and it is this approach that shall be used for ASAM OpenLABEL scenario tagging.


The minimal set does not include any tag that may be inferred from any other tag in the minimal set. The minimal set may be used to define the complete tag set for a scenario which includes all tags that belong to the minimal set and all those which may be inferred from the minimal set.


##### ASAM OpenLABEL scenario tagging ontology


The ASAM OpenLABEL tags and relations between them form the ASAM OpenLABEL scenario tagging ontology. The ASAM OpenLABEL scenario tagging ontology is available as a machine-readable form which uses the RDF turtle format, but which still manages to be human-readable.


The RDF turtle format is a W3C Recommendation and is a textual syntax that allows an RDF graph to be completely written in a compact and natural text form [20]. It provides levels of compatibility with the N-Triples [N-TRIPLES] format as well as the triple pattern syntax of the SPARQL W3C Recommendation [21].


The RDF turtle definition of the ASAM OpenLABEL scenario tagging ontology provides compatibility with a variety of RDF tools and toolkits that, in turn, offer inference and querying functionalities.


The tag hierarchy is replicated in the ASAM OpenLABEL scenario tagging ontology through the use of subclassing. The following is an excerpt from the ASAM OpenLABEL scenario tagging ontology which shows the definitions for the `Intersection` and `Roundabout` tags and how they are related to the more general `Junction` tag through a sub-class relationship, with the `Odd` tag being the root of the hierarchy for the ODD tags, and all tags being a sub-class of `Tag`.


_RDF turtle example_


```turtle
@base <https://openlabel.asam.net/V1-0-0/ontologies#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<Tag> a rdfs:Class ;
	rdfs:subClassOf rdfs:Class ;
	rdfs:label "Base Tag"@en ;
	rdfs:comment "The base tag"@en .

<Odd> a rdfs:Class ;
	rdfs:subClassOf <Tag> ;
	rdfs:label "ODD"@en ;
	rdfs:comment "Refer to BSI PAS-1883 Section 5"@en ;
	rdfs:seeAlso "https://www.bsigroup.com/en-GB/CAV/pas-1883" .

<OddScenery> a rdfs:Class ;
    rdfs:subClassOf <Odd> ;
    rdfs:label "Junction"@en ;
    rdfs:comment "Refer to BSI PAS-1883 Section 5.1.a"@en ;
    rdfs:seeAlso "https://www.bsigroup.com/en-GB/CAV/pas-1883" .

<SceneryJunction> a rdfs:Class ;
    rdfs:subClassOf <OddScenery> ;
    rdfs:label "Junction"@en ;
    rdfs:comment "Refer to BSI PAS-1883 Section 5.2.1.c"@en ;
    rdfs:seeAlso "https://www.bsigroup.com/en-GB/CAV/pas-1883" .

<JunctionIntersection> a rdfs:Class ;
    rdfs:subClassOf <SceneryJunction> ;
    rdfs:label "Intersection"@en ;
    rdfs:comment "Refer to BSI PAS-1883 Section 5.2.4"@en ;
    rdfs:seeAlso "https://www.bsigroup.com/en-GB/CAV/pas-1883" .

<JunctionRoundabout> a rdfs:Class ;
    rdfs:subClassOf <SceneryJunction> ;
    rdfs:label "Roundabout"@en ;
    rdfs:comment "Refer to BSI PAS-1883 Section 5.2.4"@en ;
    rdfs:seeAlso "https://www.bsigroup.com/en-GB/CAV/pas-1883" .
```


Administration tags represent values which characterize a scenario rather than being things which a scenario contains and as such, they are defined as RDF properties which relate values to scenarios. The following excerpt from the ASAM OpenLABEL scenario tagging ontology is for the `Scenario name` administration tag, which defines a textual property that allows a scenario to be assigned a name.


_RDF turtle example_


```turtle
<scenarioName> a rdfs:Property ;
    rdfs:label "Scenario name"@en ;
    rdfs:comment "The name of the scenario"@en ;
    rdfs:domain <Scenario> ;
    rdfs:range rdfs:Literal .
```


##### Tag naming convention


Tag names in the ontology shall be unique and to avoid ambiguity, the names of the tag classes follow a naming convention which is constructed using a prefix from the parent class name and a suffix from the child class. Pascal case is used for class names, whilst camel case is used for properties.


> **NOTE**: It shall be assumed that tags in a tagging instance are processed in a case-sensitive manner and therefore shall correspond exactly with ASAM OpenLABEL tag names.


##### Tagging instance ontology usage


When creating an ASAM OpenLABEL tagging instance, the instance shall reference the ASAM OpenLABEL scenario tagging ontology to give meaning to the tags used in the instance. This is achieved by referencing the ASAM OpenLABEL scenario tagging ontology from the ontologies section in the instance using the `https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl`, and by specifying the ontology to which the tags belong.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "ontologies": {
            "0": {
                "uri": "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl"
            }
        },
        "tags": {
            "0": {
                "type": "SpecialStructurePedestrianCrossing",
                "ontology_uid": "0"
            }
        }
    }
}
```


The example shows how the ASAM OpenLABEL scenario tagging ontology is referenced and that it has been assigned `0` as the ontology identifier. Each ontology in the ontologies section shall be given a unique identifier. This is then referred to by the `SpecialStructurePedestrianCrossing` tag by its `ontology_uid` element to indicate that the tag is a member of the ontology.


_Related topics_


- Tags
- Ontologies


#### 8.2.2. Tagging subsets


When tagging scenarios, it may be that not all of the available tags in an ontology are to be considered due to cost/time or technical constraints. In addition, they may be out of scope for the intended use of the tagged scenarios.


For example, if a tagging technician wants to tag a collected dataset for lane detection purposes, they only annotate lane-related features, such as the lane dimensions and lane marking types. Other types of features are ignored.

[Image: fig tagging boundary.drawio]

*Figure 63. Scenario tagging ontology*


This means that a lot of information is absent in the tagged data. However, this information can be interesting and important for other users because different users may have various usage purposes on the same dataset. For example, an environment perception researcher might be more interested in junctions than lane numbers.


This ambiguity may lead to unexpected and inconsistent results when querying scenarios where the presence of a road feature is not desired and could result in the incorrect selection of scenarios which include that road feature but were not tagged with it.


The ambiguity means that it is not possible to determine from the tagging whether:


- The relevant feature does not exist in the collected data.


Or


- The relevant feature does exist in the collected data but it has not been tagged.


This uncertainty of the cause of an absent tag can lead to unexpected and inconsistent system responses. One typical use case is when querying datasets for the specific road features, for example, users are allowed to retrieve tagged data based on some conditions with regard to a specific tag value. In the above example, the tagging technician has only tagged lane-relevant attributes and there are no tags for the queried T-junction, even if a T-junction actually exists in the data. If the environment perception researcher wants to query all scenarios without a T-junction, the system can either return nothing because there is no information about junctions or return the tagged data because no T-junction is tagged.


That means that the problem is how should the absence of a tag be interpreted. Does it mean that the scenario does not contain that thing, or does it mean that it is not know as to whether the scenario contains that thing.


To resolve this uncertainty and ensure predictable behavior, ASAM OpenLABEL allows for the subset of tags that has been used in the tagging process to be specified. By knowing this subset, it can be used to assert that, if a tag is not present in the scenario tags but is present in the ontology subset, then it means that the scenario does not contain that thing. For tags outside the subset, it is unknown as to whether the scenario contains that thing or not. It is not valid to use tags outside of the bounds of the ontology subset.


Ontology subsets are defined by specifying the minimal set of tags which bound the subset, and this is termed the tagging boundary. As with scenario tagging, the tagging boundary shall not include any tags which can be inferred from other members of the tagging boundary.


Subsets can be defined either by inclusion or exclusion. The subset is formed from tags on the inside or the outside of the boundary. When deciding which method to use, it is suggested using whichever method results in the smallest set of tags for the boundary.


When using the inclusion method, the subset is defined as the empty set, in addition to the boundary tags, and the ascendants of the boundary tags.


When using the exclusion method, the subset is defined as the complete set of ontology tags minus the boundary tags and the descendants of the boundary tags.


If no boundary is specified, the entire set of tags from the ontology forms the subset.


> **NOTE**: Administration tags shall not be included in the tagging boundary and their absence from a tagging instance means that the information about the scenario for that tag is unknown.


In the tagging schema, the tagging boundary is specified for an ontology using the `boundary_list` element, and `boundary_mode` is used to determine whether the inclusion or exclusion method should be used be setting it to `include` or `exclude` respectively.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
           "schema_version": "1.0.0"
        },
        "ontologies": {
            "0": {
                "uri": "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl",
                "boundary_list": ["JunctionIntersection", "JunctionRoundabout"],
                "boundary_mode": "include"
            }
        },
        "tags": {
            "0": {
                "type": "JunctionIntersection",
                "ontology_uid": "0"
            }
        }
    }
}
```


The example shows a subset of the ASAM OpenLABEL scenario tagging ontology that only includes the tags for `intersections` and `roundabouts`. Considering this, it can be asserted that the tagged scenario contains an `intersection` and does not contain a `roundabout`. We can infer that it contains a `junction` but it is unknown as to whether the scenario contains a `pedestrian crossing`.


In implementation, scenario querying systems shall not allow the querying of scenarios with tags which fall outside of the boundary as the results are undefined as tags outside the boundary have no meaning.


> **NOTE**: Administration tags shall not need to be included in the tagging subset.


_Related topics_


- Tags
- Ontologies


#### 8.2.3. Tagging extensions


There may be situations in which the ASAM OpenLABEL tags do not meet the precise needs of a tagging objective and additional tags are needed. ASAM OpenLABEL makes it possible to extend the set of tags used for tagging. Additional tags may be added independent of the ASAM OpenLABEL scenario tagging ontology or can be used to extend it.


For example, in the UK, there are different types of pedestrian crossings, such as a `Toucan Crossing` which is a crossing for pedestrians and cycles. ASAM OpenLABEL allows the ASAM OpenLABEL `Pedestrian Crossing` tag to be extended with this more specific type of crossing.


_RDF turtle example_


```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ol: <https://openlabel.asam.net/V1-0-0/ontologies#> .
@prefix ex: <https://example.org/ontologies/v1#> .

ex:ToucanCrossing a rdfs:Class ;
    rdfs:subClassOf ol:SpecialStructurePedestrianCrossing ;
    rdfs:label "Toucan Crossing" ;
    rdfs:comment "A type of crossing designed for both pedestrians and cyclists" ;
    rdfs:seeAlso "https://docs.example.org/ontologies/v1#ToucanCrossing" .
```


The example shows how to create a new ontology which references the ASAM OpenLABEL scenario tagging ontology and defines a new class of `ToucanCrossing` which is a subclass of the ASAM OpenLABEL `Pedestrian crossing` tag (`SpecialStructurePedestrianCrossing`).


Ontologies shall be defined using the RDF turtle format and shall be assigned a URI so that they can be uniquely identified. The URI should resolve to a resource from where the RDF turtle definition can be downloaded.


The class name of new tags should follow the tag naming convention described elsewhere in this chapter.


When creating a new tag, the following properties shall be defined:


- rdfs:label: Should be a short, human friendly name for the tag.
- rdfs:comment: Should be a short description conveying the meaning of the tag.
- rdfs:seeAlso: Should be a URL to a resource that contains a definition of the tag.


The following example shows how a new ontology shall be referenced from the ontologies section of the ASAM OpenLABEL instance. The new `ToucanCrossing` tag may be added then.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "ontologies": {
            "0": {
                "uri": "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl"
            },
            "1": {
                "uri": "https://example.org/ontologies/v1"
            }
        },
        "tags": {
            "0": {
                "type": "ToucanCrossing",
                "ontology_uid": "1"
            }
        }
    }
}
```


A new tag which does not extend the ASAM OpenLABEL scenario tagging ontology shall be defined such that the new tag is a subclass of the base rdfs class and is therefore not related to the ASAM OpenLABEL scenario tagging ontology.


_RDF turtle example_


```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix ol: <https://openlabel.asam.net/V1-0-0/ontologies#> .
@prefix ex: <https://example.org/ontologies/v1#> .

ex:ScenarioStatus a rdfs:Class ;
    rdfs:subClassOf rdfs:Class ;
    rdfs:label "Scenario Status" ;
    rdfs:comment "Internal status code" ;
    rdfs:seeAlso "https://docs.example.org/ontologies/v1#ScenarioStatus" .
```


> **NOTE**: Enumerations should be avoided as they are not extensible, and values should be defined as subclasses instead.


_Rules_


- Ontologies shall have a unique URI so that they can be uniquely identified.


_Related topics_


- Structure
- Tags
- Ontologies


#### 8.2.4. Tagging values


For some classes of scenario content, it is desirable to be able to include quantitative values to specify the scope for the class. For example, when tagging a scenario for rainfall, the amount of rain might be specified. There are several tags like this within the ASAM OpenLABEL scenario tagging ontology that can have values specified, and the ontology contains property definitions to support this.


The following example shows the definition for the `Rainfall` tag and its associated `Rainfall Intensity` property. Note that the domain of the property is the tag. Tag properties are named by convention as being the associated tag name converted to camel case with the suffix 'Value' appended.


_RDF turtle example_


```turtle
<EnvironmentWeather> a rdfs:Class ;
    rdfs:subClassOf <OddEnvironment> ;
    rdfs:label "Weather"@en ;
    rdfs:comment "Refer to BSI PAS-1883 Section 5.3.1"@en ;
    rdfs:seeAlso "https://www.bsigroup.com/en-GB/CAV/pas-1883" .

<WeatherRain> a rdfs:Class ;
    rdfs:subClassOf <EnvironmentWeather> ;
    rdfs:label "Rainfall"@en ;
    rdfs:comment "Refer to BSI PAS-1883 Section 5.3.1.2"@en ;
    rdfs:seeAlso "https://www.bsigroup.com/en-GB/CAV/pas-1883" .

<weatherRainValue> a rdfs:Property ;
	rdfs:label "Rainfall Intensity (mm/h)"@en ;
	rdfs:comment "Refer to BSI PAS-1883 Section 5.3.1.2"@en ;
	rdfs:domain <WeatherRain> ;
	rdfs:range xsd:decimal ;
	rdfs:seeAlso "https://www.bsigroup.com/en-GB/CAV/pas-1883" .
```


Within an ASAM OpenLABEL instance, values associated with a tag are specified by adding the `tag_data` element to the `tag` element.


The following example specifies rainfall with a value of `3.1`. Note that the metric and units for the value are specified in the ontology and not repeated in the instance.


_JSON example_


```json
{
    "tags": {
        "0": {
            "type": "WeatherRain",
            "ontology_uid": "0",
            "tag_data": {
                "num": [{
                    "type": "value",
                    "val": "3.1"
                }]
            }
        }
    }
}
```


Refer to Data types (generic) for more detail on the `tag_data` element and the different types of data that are supported.


Where a tag can have a value specified it should not be mandatory as it may be that the value is not known or cannot be determined. For example, it may be possible to detect that a scenario contains rainfall but not the amount of rain, in which case it is still desirable to tag the scenario for rainfall but not to specify the amount.


Similarly, when querying scenarios, it might be desirable to include or exclude scenarios containing rain, in which case they would query using the rainfall tag without specifying an amount.


_Related topics_


- Tags
- Data types (generic)


#### 8.2.5. Tagging multiple values


In many cases, due to the variability of the natural world it is not appropriate to use exact values for tags and it is necessary to specify a range or multiple values.


> **NOTE**: Repeating a tag in an ASAM OpenLABEL instance is not allowed, nor is it necessary with the ability to specify multiple values.


Ranges are particularly suitable for describing quantities measured using non-integer values, such as rainfall and lane widths. In this case, variability in the measured value over time or space is likely, as is an imprecise measurement.


A range can be specified by indicating the upper and lower bounds of the set of possible values as in the following example:


_JSON example_


```json
{
    "tag_data": {
        "vec": [{
            "type": "range",
            "val": [3.4, 3.7]
            }
        ]
    }
}
```


It is also possible to specify a range with only the upper or lower bound, as in the two following examples, in which case the limit on the possible range of values is determined by the definition of the tag.


_JSON example_


```json
{
    "tag_data": {
        "num": [{
            "type": "min",
            "val": 1.2
        }]
    }
}
```


The example shows a range specified with only a lower bound.


_JSON example_


```json
{
    "tag_data": {
        "num": [{
            "type": "max",
            "val": 20.1
        }]
    }
}
```


The example shows a range specified with an upper bound.


For situations where there is a discontinuous range, it is possible to specify this using multiple ranges as follows.


_JSON example_


```json
{
    "tag_data": {
        "vec": [{
            "type": "range",
            "val": [3.4, 3.7]
            }, {
            "type": "range",
            "val": [3.9, 4.1]
        }]
    }
}
```


For tags where a discrete value is appropriate, such as `Number of lanes`, multiple values can be supplied together as a set for the same tag, as shown in the following example:


_JSON example_


```json
{
    "tag_data": {
        "vec": [{
            "type": "values",
            "val": [2, 3]
        }]
    }
}
```


The example shows a set of values.


_Rule_


- Repeating a tag in a ASAM OpenLABEL instance shall not be allowed.
- Specified ranges should not overlap.


_Related topics_


- Tags
- Data types (generic)


### 8.3. Annotation schema


The annotation schema defines the structure of annotations, data types, and conventions needed to unambiguously interpret the annotations. The annotation data format specifies how the annotation data is encoded for storage in computer files.


The annotation schema is described and formatted as a JSON schema. It defines the shape which valid JSON annotation instances shall conform to. The structure of the ASAM OpenLABEL annotation schema is serialized in the [ASAM OpenLABEL JSON schema file](https://openlabel.asam.net/V1-0-0/schema/openlabel_json_schema.json). The annotation schema itself conforms to the JSON schema Draft 7 specification [13].


The annotation schema of ASAM OpenLABEL addresses the following general features related to scenario tagging:


- Tagging different ODD, behavioral, and administrative characteristics of the raw data instance.
- Defining a tagging subset that determines the subset of tags relevant for the specific tagging instance.
- Discrete values and value range definitions for specific tags.
- Linkage to ontologies and external resources.
- Customizable and optional fields.


The annotation schema defines three main characteristic aspects of annotation data:


- Structure: How data is organized, using hierarchies and key-value dictionaries.
- Types: Primitive data types for key-value items.
- Conventions: Documented interpretation of data values.


The annotation schema for scenario tagging follows the same principles of the annotation schema for multi-sensor data labeling, meaning JSON and JSON schema, as described in chapter Multi-sensor data labeling.


### 8.4. Structure


The ASAM OpenLABEL annotation schema for scenario tagging is structured as a dictionary and can be described from top to bottom. This section contains diagrams intended to visualize the structure. The details of the structure can all be consulted at the ASAM OpenLABEL JSON schema file.


Any ASAM OpenLABEL JSON data shall have a root key named `openlabel`. Its value is a dictionary containing the rest of the structure as described in the next sections. The version of the schema shall be defined inside the `metadata` structure, under the key `schema_version`. All other entries are optional.


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


The following example shows a JSON payload corresponding to the first level items inside the root `openlabel` value, which are related to scenario tagging.


_JSON example_


```json
{
    "openlabel": {
        "tags": { ... },
        "metadata": { ... },
        "ontologies": { ... },
    }
}
```


For scenario tagging, the ASAM OpenLABEL structure defines dictionaries for the `tags`. Each entry of the dictionary is a key-value pair where the key is a unique identifier of the `tag`. The value is the container of its static information. Supporting structures define the used `ontologies` to provide linkage to external semantic definitions of terms.

[Image: fig openlabel format tagging.drawio]

*Figure 64. ASAM OpenLABEL tagging structure*


Figure 64 shows the ASAM OpenLABEL data structure for scenario tagging.


_Class_


```
openlabel
```


The OpenLABEL root JSON object, which contains all other JSON objects.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 65. Diagram of the openlabel class*


*Table 25. Properties of the openlabel class*

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


### 8.5. Tags


Tags are used to provide information about a certain data file, which may be specified at the `metadata` entry in the JSON file.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0",
            "tagged_file": "../resources/scenarios/scenario.file"
        }
    }
}
```


Similarly to `object_data`, `tags` may have `tag_data` in the form of generic data types (that is, `num`, `vec`, `text`, `boolean`). See Data types (generic) for details.

[Image: fig openlabel format attributes generic.drawio]

*Figure 66. ASAM OpenLABEL attributes*


_Class_


```
tag
```


A tag is a special type of label that can be attached to any type of content, such as images, data containers, folders. In ASAM OpenLABEL the main purpose of a tag is to allow adding metadata to scenario descriptions.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 67. Diagram of the tag class*


*Table 26. Properties of the tag class*

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

*Figure 68. Diagram of the tag data class*


_JSON example_


```json
{
	"tags" : {
        "0" : {
            "type" : "RoadTypeMotorway",
            "ontology_uid" : "0"
        },
        "1" : {
            "type" : "LaneSpecificationLaneCount",
            "ontology_uid" : "0",
            "tag_data" : {
                "vec" : [{
                        "type" : "values",
                        "val" : ["2", "3"]
                    }
                ]
            }
        },
        "2" : {
            "type" : "LaneSpecificationDimensions",
            "ontology_uid" : "0",
            "tag_data" : {
                "vec" : [{
                        "type" : "range",
                        "val" : ["3.4", "3.7"]
                    }, {
                        "type" : "range",
                        "val" : ["3.9", "4.1"]
                    }
                ]
            }
        },
        "3" : {
            "type" : "WeatherRain",
            "ontology_uid" : "0",
            "tag_data" : {
                "num" : [{
                        "type" : "min",
                        "val" : "1.2"
                    }
                ]
            }
        },
        "4" : {
            "type" : "MotionWalk",
            "ontology_uid" : "0"
        },
        "5" : {
            "type" : "MotionDrive",
            "ontology_uid" : "0"
        },
        "6" : {
            "type" : "scenarioUniqueReference",
            "ontology_uid" : "0",
            "tag_data" : {
                "text" : [{
                        "type" : "value",
                        "val" : "{02ed611e-a376-11eb-973f-b818cf5bef8c}"
                    }
                ]
            }
        },
        "7" : {
            "type" : "scenarioName",
            "ontology_uid" : "0",
            "tag_data" : {
                "text" : [{
                        "type" : "value",
                        "val" : "FSD01726287 Roundabout first exit"
                    }
                ]
            }
        },
        "9" : {
            "type" : "scenarioVersion",
            "ontology_uid" : "0",
            "tag_data" : {
                "text" : [{
                        "type" : "value",
                        "val" : "1.0"
                    }
                ]
            }
        },
        "10" : {
            "type" : "projectId",
            "ontology_uid" : "1",
            "tag_data" : {
                "text" : [{
                        "type" : "value",
                        "val" : "123456"
                    }
                ]
            }
        },
        "12" : {
            "type" : "ToucanCrossing",
            "ontology_uid" : "2"
        },
        "13" : {
            "type" : "RainDropletSize",
            "ontology_uid" : "2",
            "tag_data" : {
                "num" : [{
                        "type" : "value",
                        "val" : "0.2"
                    }
                ]
            }
        }
    }
}
```


### 8.6. Ontologies


Tags are particularly sensitive to precise definitions as they are mainly used for searching. As a consequence, tags may be defined in specific ontologies.


_Class_


```
ontologies
```


This is the JSON object of OpenLABEL ontologies. Ontology keys are strings containing numerical UIDs or 32 bytes UUIDs. Ontology values may be strings, for example, encoding a URI. JSON objects containing a URI string and optional lists of included and excluded terms.


| Additional properties: | false |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 69. Diagram of the ontologies class*


_JSON example_


```json
{
	"openlabel" : {
		"metadata" : {
			"schema_version" : "1.0.0",
			"tagged_file" : "../resources/scenarios/some_scenario_file"
		},
        "ontologies": {
            "0": {
                "uri": "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl"
            }
        },
		"tags" : {
			"0" : {
				"type" : "RoundaboutDouble",
				"ontology_uid" : "0"
				}
			}
		}
	}
}
```


The example shows the referenced URL of an ontology `https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl` with id `0`. Within tag `0` this referenced ontology is defined for semantic verification by using the `ontology_uid` key to reference on the ontology by using the id `0` value.


Tag subset inclusion and exclusion may be defined for each ontology.


_JSON example_


```json
{
	"openlabel" : {
		"metadata" : {
			"schema_version" : "1.0.0"
		},
		"ontologies" : {
			"0" : {
				"uri" : "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl",
                "boundary_list": ["RoadTypeMotorway", "RoadTypeMinor"],
                "boundary_mode": "include"
			},
			"1" : {
                "uri" : "https://mycompany/ontologies/v1",
                "boundary_list": ["JunctionRoundabout"],
                "boundary_mode": "exclude"
            }
		}
	}
}
```


The example shows tagging subset inclusion for the tags `RoadTypeMotorway` and `RoadTypeMinor` by using the `boundary_mode` inclusion key for the first ontology. It also shows tagging subset exclusion for the tag `JunctionRoundabout`, by using the `boundary_mode` exclusion key.


### 8.7. Data types (generic)


ASAM OpenLABEL defines geometric and non-geometric (generic) data types, which all together provide the flexibility needed to represent any kind of information on labels or tags.


Non-geometric (generic) `tag_data` are primitive data types like the following:


- Boolean: boolean
- Number: May be a single number or a floating-point precision: num
- Text: text
- Vector. A vector is an array of numbers or strings.: vec


These are `attributes` that can be used freely to express any property of the `tag`.


_Rules_


- For scenario tagging, only non-geometric (generic) data types are considered.
- tags shall have a unique identifier.
- tag_data shall have a unique name.


_Related topics_


- Data types (geometric)
- Boolean
- Number
- Text
- Vector


#### 8.7.1. Boolean


A Boolean `object_data`. It has the same properties as the other generic attributes.


_Class_


```
boolean
```


A boolean.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 70. Diagram of the boolean class*


*Table 27. Properties of the boolean class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| type | string |  |  | This attribute specifies how the boolean shall be considered. In this schema the only possible option is as a value. |
| val | boolean | true |  | The boolean value. |


_JSON example_


```json
{
"boolean": [{
    "name": "visible",
    "val": true
}]
}
```


#### 8.7.2. Number


The most basic attribute or generic data type is `num`. It defines a floating-point number and is defined by a `name` key, and `val` key. Optional properties are `coordinate_system` and other nested `object_data` as `attributes`.


_Class_


```
num
```


A number.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 71. Diagram of the num class*


*Table 28. Properties of the num class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| type | string |  |  | This attribute specifies whether the number shall be considered as a value, a minimum, or a maximum in its context. |
| val | number | true |  | The numerical value of the number. |


_JSON example_


```json
{
"num": [{
    "name": "height_m",
    "val": 1.98
}]
}
```


The value of the key `num` is an array. Any element, for example `object`, may have multiple `object_data` entries of `num`. The same principle applies to all other `object_data`.


Nesting generic data types, for example `text`, into other generic data type, for example `num`, can be done infinitely. ASAM OpenLABEL does not limit the hierarchy depth.


_JSON example_


```json
{
"num": [{
    "name": "height_m",
    "val": 1.98,
    "coordinate_system": "WORLD",
    "attributes": {
        "num": [{
            "name": "confidence",
            "val": 0.98
        }]
    },
    "custom_prop1": "SomeValue",
    "custom_prop2": 0.99
}]
}
```


#### 8.7.3. Text


A `text` is a string or chain of characters which represent textual information. It has the same properties as the other generic attributes.


_Class_


```
text
```


A text.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 72. Diagram of the text class*


*Table 29. Properties of the text class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| type | string |  |  | This attribute specifies how the text shall be considered. The only possible option is as a value. |
| val | string | true |  | The characters of the text. |


_JSON example_


```json
{
"text": [{
    "name": "license plate",
    "val": "8440CMN"
}]
}
```


#### 8.7.4. Vector


Arrays of `text` or `num` can be created under `vec`. It has the same properties as the other generic attributes.


_Class_


```
vec
```


A vector (list) of numbers or strings.


| Additional properties: | true |
| --- | --- |
| Type: | object |

[Image: Diagram]

*Figure 73. Diagram of the vec class*


*Table 30. Properties of the vec class*

| Name | Type | Required | Reference | Description |
| --- | --- | --- | --- | --- |
| attributes |  |  | #/definitions/attributes | Attributes is the alias of element data that can be nested inside geometric object data. For example, a certain bounding box can have attributes related to its score, visibility, etc. These values can be nested inside the bounding box as attributes. |
| coordinate_system | string |  |  | Name of the coordinate system in respect of which this object data is expressed. |
| name | string |  |  | This is a string encoding the name of this object data. It is used as index inside the corresponding object data pointers. |
| type | string |  |  | This attribute specifies whether the vector shall be considered as a descriptor of individual values or as a definition of a range. |
| val | array | true |  | The numerical values of the vector (list) of numbers. |


_JSON example_


```json
{
"vec": [{
    "name": "scores",
    "val": [0.98, 0.76, 0.98]
}]
}
```


The example shows an array of numbers.


_JSON example_


```json
{
"vec": [{
    "name": "locations",
    "val": ["Madrid", "Paris", "Rome"]
}]
}
```


The example shows an array of strings.


### 8.8. Use cases


#### 8.8.1. Scenario tagging example


The following example shows an ASAM OpenLABEL instance which has been used to tag an OpenSCENARIO 1.x file.

[Image: fig crossroads scenario]

*Figure 74. Crossroad scenario*


The example contains ODD tags summarizing the road features present in the scenario, behavior tags for the car and bus and their driving behavior, as well as administration tags describing scenario ID, name, version, owner, and license.


The scenario is contained in a separate file `scenario123.osc` and is referenced using the `tagged_file` element.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0",
            "tagged_file": "../resources/scenarios/scenario123.osc"
        },
        "ontologies": {
            "0": {
                "uri": "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl",
                "boundary_list": ["DrivableAreaSigns", "DrivableAreaEdge","DrivableAreaSurface"],
                "boundary_mode": "exclude"
            }
        },
        "tags": {
            "0": {
                "type": "RoadTypeMinor",
                "ontology_uid": "0"
            },
            "1": {
                "type": "HorizontalStraights",
                "ontology_uid": "0"
            },
            "3": {
                "type": "LaneTypeTraffic",
                "ontology_uid": "0"
            },
            "4": {
                "type": "ZoneSchool",
                "ontology_uid": "0"
            },
            "5": {
                "type": "IntersectionCrossroad",
                "ontology_uid": "0"
            },
            "6": {
                "type": "SpecialStructurePedestrianCrossing",
                "ontology_uid": "0"
            },
            "7": {
                "type": "WeatherWind",
                "ontology_uid": "0",
                "tag_data": {
                    "vec": [{
                        "type": "range",
                        "val": ["10", "25"]
                        }
                    ]
                }
            },
            "8": {
                "type": "IlluminationDay",
                "ontology_uid": "0"
            },
            "9": {
                "type": "FixedStructureBuilding",
                "ontology_uid": "0"
            },
            "10": {
                "type": "FixedStructureVegetation",
                "ontology_uid": "0"
            },
            "10": {
                "type": "TravelDirectionRight",
                "ontology_uid": "0"
            },
            "11": {
                "type": "VehicleCar",
                "ontology_uid": "0"
            },
            "12": {
                "type": "VehicleBus",
                "ontology_uid": "0"
            },
            "13": {
                "type": "MotionDrive",
                "ontology_uid": "0"
            },
            "15": {
                "type": "scenarioUniqueReference",
                "ontology_uid": "0",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "c133241e-f325-11eb-a72f-e817714ba02d"
                    }]
                }
            },
            "16": {
                "type": "scenarioName",
                "ontology_uid": "0",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "Scenario 123"
                    }]
                }
            },
            "17": {
                "type": "scenarioVersion",
                "ontology_uid": "0",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "1.0"
                    }]
                }
            },
            "18": {
                "type": "ownerURL",
                "ontology_uid": "0",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "https://example.com"
                    }]
                }
            },
            "19": {
                "type": "licenseURI",
                "ontology_uid": "0",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "https://example.org/licenses/publicdomain/"
                    }]
                }
            }
        }
    }
}
```


#### 8.8.2. Ontology extension


Below is an example of how the ASAM OpenLABEL scenario tagging ontology may be extended to add a new administration tag to record the project that a scenario was created for.


In the ASAM OpenLABEL scenario tagging ontology, administration tags are generally defined as properties which apply to the `Scenario` class. To add a new administration tag, a new property shall be defined.


_RDF turtle example_


```turtle
@prefix ex: <https://example.org/ontologies/v1/> .
@prefix asam: <https://openlabel.asam.net/V1-0-0/ontologies/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:projectReference a rdfs:Property ;
    rdfs:label "Project Reference"@en ;
    rdfs:comment "The project which the scenario was created for"@en ;
    rdfs:domain asam:Scenario ;
    rdfs:range rdfs:Literal .
```


The example shows how a new property, `projectReference`, is defined in an RDF turtle file.


Note the following:


- The ASAM OpenLABEL scenario tagging ontology is referenced using the asam: prefix.
- A new namespace specifies ex: for the ontology extension.
- The name for the new property follows the convention of using camel case.


Having created the ontology extension, it can be used from a tagging instance by referencing the new ontology from the `ontologies` element.


> **NOTE**: The new ontology should be made available for download from the specified URI to enable users of the tagging instance to process the file.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0",
            "tagged_file": "../resources/scenarios/scenario.osc"
        },
        "ontologies": {
            "0": {
                "uri": "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl"
            },
            "1": {
                "uri": "https://example.org/ontologies/v1"
            }
        },
        "tags": {
            "0": {
                "type": "projectReference",
                "ontology_uid": "1",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "X0002465"
                    }]
                }
            }
        }
    }
}
```


The example shows how the new `projectReference` tag is used to tag a scenario with the project reference `X0002465`. The `ontology_uid` refers to the ontology extension.


#### 8.8.3. Embedded scenario


The following is an example of how a scenario definition can be embedded in a tagging instance as an alternative to being stored in a separate file in order to aid portability.


When embedding a scenario definition, the `scenarioDefinitionLanguageURI` tag should be used to specify which scenario definition language has been used for the scenario definition.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0"
        },
        "ontologies": {
            "0": {
                "uri": "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl"
            }
        },
        "tags": {
            "0": {
                "type": "RoadTypeMinor",
                "ontology_uid": "0"
            },
            "1": {
                "type": "JunctionRoundabout",
                "ontology_uid": "0"
            },
            "2": {
                "type": "LaneSpecificationLaneCount",
                "ontology_uid": "0",
                "tag_data": {
                    "vec": [{
                        "type": "values",
                        "val": [1, 2]
                        }
                    ]
                }
            },
            "3": {
                "type": "scenarioDefinitionLanguageURI",
                "ontology_uid": "0",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "https://example.org/languages/SDL/1.0/"
                    }]
                }
            },
            "4": {
                "type": "scenarioDefinition",
                "ontology_uid": "0",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "def ra1 as Roundabout; def r1, r2, r3 as Road.Minor; ra1.Exits = [r1,r2,r3]; r1.Lanes = 2;"
                    }]
                }
            }
        }
    }
}
```


#### 8.8.4. Scenario instance in Turtle


When processing a tagging instance, the ASAM OpenLABEL scenario tagging ontology may be used to help create a model of the scenario which can be loaded into a reasoning engine in order to determine inferred tags.


_JSON example_


```json
{
    "openlabel": {
        "metadata": {
            "schema_version": "1.0.0",
            "tagged_file": "../resources/scenarios/scenario123.osc"
        },
        "ontologies": {
            "0": {
                "uri": "https://openlabel.asam.net/V1-0-0/ontologies/openlabel_ontology_scenario_tags.ttl"
            }
        },
        "tags": {
            "0": {
                "type": "RoundaboutNormal",
                "ontology_uid": "0"
            },
            "1": {
                "type": "WeatherRain",
                "ontology_uid": "0",
                "tag_data": {
                    "num": [{
                        "type": "value",
                        "val": "1.2"
                        }
                    ]
                }
            },
            "16": {
                "type": "scenarioName",
                "ontology_uid": "0",
                "tag_data": {
                    "text": [{
                        "type": "value",
                        "val": "Scenario 123"
                    }]
                }
            }
        }
    }
}
```


The example shows a tagging instance of a scenario and is followed by a corresponding model of the scenario in RDF turtle format.


_RDF turtle example_


```turtle
@prefix asam: <https://openlabel.asam.net/V1-0-0/ontologies/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix data: <https://example.org/data/> .

data:tagRoundabout a asam:RoundaboutNormal .

data:tagRain a asam:WeatherRain ;
    asam:weatherRainValue 1.2 .

data:scenario123 a asam:Scenario ;
    asam:scenarioName "Scenario 123" ;
    asam:hasTag data:tagRoundabout ;
    asam:hasTag data:tagRain .
```


In this RDF turtle definition, the scenario is defined as an instance of the `scenario` class which is defined in the ASAM OpenLABEL scenario tagging ontology and represents the domain of all scenarios. The scenario instance is also assigned the value `Scenario 123` specified in the tagging instance using the Administration tag `scenarioName` property.


The tags from the tagging instance are defined in RDF turtle using the ODD tag classes in the ontology. In this example there is a tag instance `tagRain` which is of tag type `WeatherRain` with a rainfall value of 1.2, and a tag instance `tagRoundabout` of type `RoundaboutNormal`.


In order to associate these tag instances with the scenario, the ontology defines a `hasTag` property which is used for making the association.


This RDF turtle definition can be loaded into a reasoning engine to determine the inferred tags, such as does the scenario contain a `Junction`.
