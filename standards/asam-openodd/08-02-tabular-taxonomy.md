# ASAM OpenODD® v1.0.0 — 8.2 Taxonomy mapping

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/08_tabular/08_02_openodd_tabular_taxonomy.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.2 Taxonomy mapping

## 8.2.1 General information

This section provides a reference mapping for representing ASAM OpenODD® taxonomies in tabular formats.

The tabular taxonomy file can be either stand-alone, accompany a module, or COD specification or both.
Each of these is stored in a denormalized tabular file, flattening relevant entities into a single table.
This is used instead of a normalized collection of interrelated files, one for every entity type of ASAM OpenODD® model.
By utilizing the easy handling and navigability of (single) table files, it enables data analysis and inspection using common tooling.
More elaborate logic might be required to map columns and entity properties to each other during import and export.
Also, checking for inconsistencies during import is advised if the files are processed with common tooling.

## 8.2.2 Taxonomy tabular representation

The taxonomy is presented in tabular form in a single row for a single concept and in columns with the translations for each specified language.
This format can represent the terminology of different languages by repeating the respective fields that are suffixed with a 2-char language code for each supported language.
The language specific fields are only for human consummation and should only be used for presentation, while the other fields can be used to base decisions on in code.

The taxonomy consists of the following columns:

* `CONCEPT_ID` column: This column represents an unique textual handle of every taxonomy concept.
  This is the only primary key of this table and serves as the name for the reference to the concept in other files.
  The key shall be unique within the taxonomy files that are transmitted. Global uniqueness is not required.
  Concept IDs shall be in English and are not translated to other languages.
* `PARENT_ID` column: This is a string column that shall correspond exactly to a single concept ID of another concept.
  For sub-elements of nested taxonomy concepts (record and categorical), this contains the CONCEPT\_ID of the concept that contains the elements.
* `TYPE` column: The type of the concept could be either float, integer, boolean, categorical, categorical literal, or a record, which is a parent of other concepts, or another concept ID representing a user-defined type.
  When the type is another concept ID, the ID refers to an user-defined type.
  This field is part of the **Type** object.

|  |  |
| --- | --- |
|  | `Record` is an instance type which represents a user-define structure comprising attributes and, optionally, other attributes. A row specifying this `TYPE` maps to the `Record` instance in UML. |

* `UNIT_TYPE` column: For numerical fields only, it specifies the type of the unit it represents.
  This field shall be empty for non-numeric types and is part of the **Unit Type** object.
* `AFFILIATION_SOURCE` column [optional]: This optional field is a string that identifies the standard or document in which the concept was originally defined, and could be used if standard provides addressable concepts supplemented with URI, and so forth.
* `AFFILIATION_CONCEPT` column [optional]: This optional field is a string that identifies the specific concept from the affiliated source.
  This provides some kind of global unique identifier to match against.
* `AFFILIATION_SOURCE_NAME_<language-code>` column [optional]: The name of the concept in the specified language.
* `CONCEPT_NAME_<language-code>` column: The name of the concept in the specified language.
* `DESCRIPTION_<language-code>` column: This field is a free text description of the concept in the specified language.
  The content of this field shall be consistent across language translations that represent a single consistent description.
  This field corresponds to the **Description Element**.
* `RANGE_EXPRESSION` column: This represents the range used to define a categorical literal.
* `COMMENTS_<language-code>` column [optional]: This is an optional field that stores the list of comments, that are provided in free text form, in the language specified for this row.
  The concept of this field does not need to be consistent across all languages.
  Each language may have a different list of comments.
  This field corresponds to the **Comments Element**.
* `INSTRUCTIONS` [optional]: This is an optional field that is used to facilitate the import and re-export of the transmitted files and to achieve an exact match.
  The format of the instruction field is the following:  
  `<INSTRUCTIONS> ::= "FILE:" <FileName>`  
  `<FileName> :== a valid file name`

|  |  |
| --- | --- |
|  | The standardization of the BNF of file names is not the scope of this standard. |

The instructions field is used to specify the source file in which the concept was defined.
The field is used to specify the file in which a concept is to be placed during export and it is filled with the name of the source file from which the concept was imported.

[Table 126](#tab-multilanguagetaxonomyrepresentation) shows an tabular representation of a taxonomy:

Table 126. Tabular taxonomy representation in TaxonomyElements.csv


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE | AFFILIATION\_SOURCE | AFFILIATION\_CONCEPT | AFFILIATION\_SOURCE\_NAME\_EN | CONCEPT\_NAME\_EN | DESCRIPTION\_EN | AFFILIATION\_SOURCE\_NAME\_EN | NAME\_DE | DESCRIPTION\_DE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| environmental\_conditions |  | record |  | ISO 34503 | environmental\_conditions | ISO 34503 | Environmental Conditions | Concepts related to environment conditions | ISO 34503 | ISO 34503 Umweltbedingungen | Einträge im Zusammenhang mit Umgebungsbedingungen |
| weather | environmental\_conditions | record |  | ISO 34503 | weather | ISO 34503 | Weather | Concepts related to weather | ISO 34503 | ISO 34503 Wetterverhältnisse | Konzepte im Zusammenhang mit dem Wetter |
| wind | weather | record |  | ISO 34503 | wind | ISO 34503 | Wind | Concepts related to weather | ISO 34503 | ISO 34503 Wind | Konzepte rund um den Wind |
| wind\_speed | wind | float | velocity | ISO 34503 | wind\_speed | ISO 34503 | Wind Speed | Wind speed measured by meteorological sensors | ISO 34503 | ISO 34503 Windgeschwindigkeit | Windgeschwindigkeit gemessen durch meteorologische Sensoren |
| rainfall | weather | record |  | ISO 34503 | rainfall | ISO 34503 | Rainfall | Concepts related to rainfall | ISO 34503 | ISO 34503 Regenfall | Konzepte im Zusammenhang mit Niederschlag |
| rainfall\_rate | rainfall | float | precipitation\_rate | ISO 34503 | rainfall\_rate | ISO 34503 | Rainfall Rate | Rainfall rate measured by meteorological sensors | ISO 34503 | ISO 34503 Niederschlagsrate | Von Wettersensoren gemessene Niederschlagsmenge |
| rainfall\_type | rainfall | categorical |  | ISO 34503 | rainfall\_type | ISO 34503 | Rainfall Type | Categorical classification of rain rate | ISO 34503 | ISO 34503 Niederschlagsart | Kategorische Klassifizierung der Regenrate |
| dynamic | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_dynamic | ISO 34503 | Dynamic Rain Type | Dynamic rain categorization | ISO 34503 | Dynamischer Regentyp | Kategorisierung von dynamischem Regen |
| convective | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_convective | ISO 34503 | Convective Rain Type | Convective rain categorization | ISO 34503 | Konvektiver Regentyp | Kategorisierung von Konvektionsregen |
| orographic | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_orographic | ISO 34503 | Orographic Rain Type | Orographic rain categorization | ISO 34503 | Orografischer Regentyp | Kategorisierung von orographischem Regen |

[Table 126](#tab-multilanguagetaxonomyrepresentation) has the following advantages:

* Unique IDs are specified for each `TaxonomyConcept` instance.
* Comprehensible English-language IDs can be used to improve understanding of ODs and ODDs.
* Multi-language translation can be provided for every `TaxonomyConcept` instance.
* Multi-file export and import is supported.

|  |  |
| --- | --- |
|  | The `Type` column reflects the `Type` class from the ASAM OpenODD® model. However, instead of using the generic term "primitive," it directly specifies the applicable primitive type (for example `int`, `float`, and so on) along with its unit (see the `UNIT_TYPE` column in [Table 126](#tab-multilanguagetaxonomyrepresentation)). |

## 8.2.3. Use of expressions for `TaxonomyConcept`

A `TaxonomyConcept` can be defined using various types of `TaxonomyConcept` instances.
`TaxonomyConcept` definitions can be created using expressions that describe boolean, numeric, ranges with upper and lower bound constraints, as defined in [Section 6.2.4, "Specializations of `TaxonomyConcept`"](../06_model_concept/06_02_openodd_taxonomy.html#sec-specializations-of-taxonomyconcepts).
Although, complex conditions should not be defined in the taxonomy expression column, this complexity needs to be deferred to the creation of modules.
See [Section 8.4.3, "Illustrating module representation with tabular format"](08_04_openodd_tabular_modules.html#sec-illustrating-module-representation-with-tabular-schema).
[Table 127](#tab-taxonomyexpressions1) shows how to use modules to define complex conditions, refer to  [Section 8.4, "ODD module mapping"](08_04_openodd_tabular_modules.html#top-tabular-modules) for more details.
[Table 127](#tab-taxonomyexpressions1) shows a `TaxonomyConcept` definition that uses range expressions:

Table 127. Usage of expressions for defining `TaxonomyConcept` instances


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE | EXPRESSION | AFFILIATION\_SOURCE | AFFILIATION\_CONCEPT | AFFILIATION\_SOURCE\_NAME\_EN | CONCEPT\_NAME\_EN | DESCRIPTION\_EN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| wind | weather | record |  |  | ISO 34503 | wind | ISO 34503 | Wind | Concepts related to weather |
| origin\_direction | wind | integer | angle |  |  | wind\_direction |  | Ground Plane Direction | The origin direction of the wind (not the target direction) in the ground/xy-plane of the world coordinate system. Corresponds to the heading/yaw angle, counted counterclockwise. 0 pointing north. |
| wind\_speed | wind | float | velocity |  | ISO 34503 | wind\_speed | ISO 34503 | Wind Speed | Wind speed measured by meteorological sensors |
| wind\_speed\_level | wind | categorical |  |  | ISO 34503 | wind\_speed | ISO 34503 | Wind Speed | Wind speed measured by meteorological sensors |
| low | wind\_speed\_level | categorical\_literal |  | wind\_speed: [0,20] km/h | ISO 34503 | wind\_speed | ISO 34503 | Wind Speed | Wind speed measured by meteorological sensors |
| medium | wind\_speed\_level | categorical\_literal |  | wind\_speed: [20,40] km/h | ISO 34503 | wind\_speed | ISO 34503 | Wind Speed | Wind speed measured by meteorological sensors |
| high | wind\_speed\_level | categorical\_literal |  | wind\_speed: > 40 km/h | ISO 34503 | wind\_speed | ISO 34503 | Wind Speed | Wind speed measured by meteorological sensors |

|  |  |
| --- | --- |
|  | Categorical, boolean, and count fields do not need to be associated with units. All other numeric fields shall be associated with units. |

|  |  |
| --- | --- |
|  | The column `CONCEPT_ID` specifies English strings. Multilingual translations are provided for the affiliation source, the affiliation concept, the name of concept, and the description. |

[Table 128](#tab-singlelanguagetaxonomyrepresentation) as an example represents the following [Code 101](#code-taxonomy):

Code 101. Definition of a taxonomy (free-form notation)

```
TAXONOMY specification is as follows
    environmental_conditions is                                # this is a `Record`
        weather is                                             # this is a `Record`
            wind is                                            # this is a  Record`
                wind_speed is a float representing velocity    # this is an attribute of type "float" having a unit type of "velocity".
                wind_speed_level is                            # this is an attribute of type `Categorical`
                    low                                        # this is a `CategoricalLiteral`
                    medium                                     # this is a `CategoricalLiteral`
                    high                                       # this is a `CategoricalLiteral`
```

Table 128. Tabular taxonomy representation in TaxonomyElements.csv


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE | AFFILIATION\_SOURCE | AFFILIATION\_CONCEPT | AFFILIATION\_SOURCE\_NAME\_EN | CONCEPT\_NAME\_EN | DESCRIPTION\_EN | AFFILIATION\_SOURCE\_NAME\_EN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| environmental\_conditions |  | record |  | ISO 34503 | environmental\_conditions | ISO 34503 | Environmental Conditions | Concepts related to environment conditions | ISO 34503 |
| weather | environmental\_conditions | record |  | ISO 34503 | weather | ISO 34503 | Weather | Concepts related to weather | ISO 34503 |
| wind | weather | record |  | ISO 34503 | wind | ISO 34503 | Wind | Concepts related to weather | ISO 34503 |
| wind\_speed | wind | float | velocity | ISO 34503 | wind\_speed | ISO 34503 | Wind Speed | Wind speed measured by meteorological sensors | ISO 34503 |
| rainfall | weather | record |  | ISO 34503 | rainfall | ISO 34503 | Rainfall | Concepts related to rainfall | ISO 34503 |
| rainfall\_rate | rainfall | float | precipitation\_rate | ISO 34503 | rainfall\_rate | ISO 34503 | Rainfall Rate | Rainfall rate measured by meteorological sensors | ISO 34503 |
| rainfall\_type | rainfall | categorical |  | ISO 34503 | rainfall\_type | ISO 34503 | Rainfall Type | Categorical classification of rain rate | ISO 34503 |
| dynamic | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_dynamic | ISO 34503 | Dynamic Rain Type | Dynamic rain categorization | ISO 34503 |
| convective | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_convective | ISO 34503 | Convective Rain Type | Convective rain categorization | ISO 34503 |
| orographic | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_orographic | ISO 34503 | Orographic Rain Type | Orographic rain categorization | ISO 34503 |

The tabular taxonomy can be extended to include support for multiple languages.
[Table 129](#tab-multilanguagetaxonomyrepresentation2) shows an tabular representation of a taxonomy supporting German language:

Table 129. Tabular taxonomy representation in TaxonomyElements.csv


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE | AFFILIATION\_SOURCE | AFFILIATION\_CONCEPT | AFFILIATION\_SOURCE\_NAME\_EN | CONCEPT\_NAME\_EN | DESCRIPTION\_EN | AFFILIATION\_SOURCE\_NAME\_EN | NAME\_DE | DESCRIPTION\_DE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| environmental\_conditions |  | record |  | ISO 34503 | environmental\_conditions | ISO 34503 | Environmental Conditions | Concepts related to environment conditions | ISO 34503 | ISO 34503 Umweltbedingungen | Einträge im Zusammenhang mit Umgebungsbedingungen |
| weather | environmental\_conditions | record |  | ISO 34503 | weather | ISO 34503 | Weather | Concepts related to weather | ISO 34503 | ISO 34503 Wetterverhältnisse | Konzepte im Zusammenhang mit dem Wetter |
| wind | weather | record |  | ISO 34503 | wind | ISO 34503 | Wind | Concepts related to weather | ISO 34503 | ISO 34503 Wind | Konzepte rund um den Wind |
| wind\_speed | wind | float | velocity | ISO 34503 | wind\_speed | ISO 34503 | Wind Speed | Wind speed measured by meteorological sensors | ISO 34503 | ISO 34503 Windgeschwindigkeit | Windgeschwindigkeit gemessen durch meteorologische Sensoren |
| rainfall | weather | record |  | ISO 34503 | rainfall | ISO 34503 | Rainfall | Concepts related to rainfall | ISO 34503 | ISO 34503 Regenfall | Konzepte im Zusammenhang mit Niederschlag |
| rainfall\_rate | rainfall | float | precipitation\_rate | ISO 34503 | rainfall\_rate | ISO 34503 | Rainfall Rate | Rainfall rate measured by meteorological sensors | ISO 34503 | ISO 34503 Niederschlagsrate | Von Wettersensoren gemessene Niederschlagsmenge |
| rainfall\_type | rainfall | categorical |  | ISO 34503 | rainfall\_type | ISO 34503 | Rainfall Type | Categorical classification of rain rate | ISO 34503 | ISO 34503 Niederschlagsart | Kategorische Klassifizierung der Regenrate |
| dynamic | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_dynamic | ISO 34503 | Dynamic Rain Type | Dynamic rain categorization | ISO 34503 | Dynamischer Regentyp | Kategorisierung von dynamischem Regen |
| convective | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_convective | ISO 34503 | Convective Rain Type | Convective rain categorization | ISO 34503 | Konvektiver Regentyp | Kategorisierung von Konvektionsregen |
| orographic | rainfall\_type | categorical\_literal |  | ISO 34503 | rainfall\_type\_orographic | ISO 34503 | Orographic Rain Type | Orographic rain categorization | ISO 34503 | Orografischer Regentyp | Kategorisierung von orographischem Regen |

[Table 129](#tab-multilanguagetaxonomyrepresentation2) has the following advantages:

* Unique IDs are specified for each `TaxonomyConcept` instance.
* Comprehensible English-language IDs can be used to improve understanding of ODs and ODDs.
* Multi-language translation can be provided for every `TaxonomyConcept` instance.
* Multi-file export and import is supported.