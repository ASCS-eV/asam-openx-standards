# ASAM OpenODD® v1.0.0 — 8.4 ODD module mapping

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/08_tabular/08_04_openodd_tabular_modules.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.4 ODD module mapping

## 8.4.1 General information

The purpose of [Section 8.4, "ODD module mapping"](08_04_openodd_tabular_modules.html) is to provide a standardized format for exporting and importing modules.
Each module export should result in a single "denormalized" file rather than a collection of interrelated files representing a "normalized" model.
The focus is on ease of exchange, usage, and storage rather than ease of import or export.
Multi-language support is achieved through the taxonomy concepts.
The ids and conditions of the modules do not have to be translated into multiple languages.
However, the titles and descriptions shall be translated.

The taxonomy concepts that support the module specification are exported separately.
In other words, an ODD export results in two files, one for the taxonomy and one for the modules.

This specification also supports other tabular formats such as the parquet files format, see [Section 8.1.4, "Storage Mechanisms"](08_01_openodd_schema_intro.html#sec-parquet-files).

## 8.4.2 Module tabular specification

Multiple modules can be exported into a single table.
Each module is represented by multiple rows.
The number of rows per module varies based on its content.
All rows that represent a single module share a common `MODULE_ID`.

The module table specification comprises the following columns:

* `MODULE_ID`: A module identifier, also known as a `module id`, shall be unique within the scope of the files of a transmission.
  It is not necessary for the ID to be unique across multiple transmissions.
  Module IDs can be comprehensible English-language strings and are not translated into other languages.
* `ROLE`: The role is specified by this row.
  Multiple rows represent a single module.
  The following roles are supported:

  + `id`: This row specifies a unique id for the module.
    It can be a comprehensible English-language string and does not have to be translated into other languages.
    This id shall be a string that is unique within the scope of the files within a single transmission.
  + `definition_type`: This row specifies the intended usage of this module.
    Currently, the types `odd` and `module` are supported:

    - `ODD`: Modules of the `ODD` kind represent the environment conditions of the module and serve as the entry point for inference purposes. No module shall reference an ODD-kind module.
    - `TOD`: Modules of the `TOD` kind represent the expected environment conditions of the module. No module shall reference an TOD-kind module.
    - `Standard` (default): All other modules are of this kind. These modules can be referenced other modules.
    - additional kinds such as **Boundary Module**: A rule describing general boundary conditions which cannot be violated by any other module.
  + `reference`: This row represents a reference to external taxonomy and other files on which the module depends.
  + `title-XX`: This row represents a language translated title.
    The language is specified by the `XX` of the type.
  + `description-XX`: This row represents a language translated description. The language is specified by the `XX` of the type.
  + `tags-XX`: This row represents a language translated list of labels, separated by `;`.
    The language is specified by the `XX` of the type.
  + `labels`: This row represents a list of labels, separated by`;`.
    Labels combine the results of labelled rules using `INCLUDE_OR` semantics and provide them under the given alias.
  + `include_and`: This row represents a single entry within the `INCLUDE_AND` section.
    Only a single INCLUDE\_AND section is allowed, thus all rows of this type are combined with the `AND` operator.
  + `include_or`: This row represents a single entry within the `INCLUDE_OR` section.
    Only a single `INCLUDE_OR` section is allowed, thus all rows of this type are combined with the `OR` operator.
  + `exclude_and`: This row represents a single entry within the `EXCLUDE_AND` section.
    Only a single `EXCLUDE_AND` section is allowed, thus all rows of this type are combined with the `AND` operator.
  + `exclude_or`: This row represents a single entry within the `EXCLUDE_OR` section.
    Only a single `EXCLUDE_OR` section is allowed, thus all rows of this type are combined with the `OR` operator.
  + `export`: This row represents export instructions, for example which file the module should be exported to.
    The exported file shall contain an `IMPORT` statement as required to maintain integrity across multiple files.
* `CONTENT_OR_CONDITION`: The value of this field depends on the `ROLE` of the row.
  The use of this field is described below depending on the role:

  + `id`: The content field contains a string that represents the module id.
    It has to be unique within the scope of the files in the transmission.
    It can be a comprehensible English-language string and does not have to be translated to other languages.
  + `definition_type`: The content field contains either `odd` or `module`.
  + `reference`: The content field represents the name of the taxonomy file that is used.
    It could be a yaml file, xml file, CSV file, or any other compliant taxonomy format.
  + `title-XX`: The content field specifies a language translated title.
    The language is specified by the `XX` of the type.
  + `description-XX`: The content field specifies a language translated description.
    The language is specified by the `XX` of the type.
  + `tags-XX`: The content field specifies a language translated list of labels, separated by `;`.
    The language is specified by the `XX` of the type.
  + `labels`: The content field specifies the list of labels, separated by `;`.
  + `include_and`: The content field specifies a condition using the following format:

    - Multiple conditions are allowed.
      They are separated with the `;` character and combined with the `OR` operator.
    - Each condition specifies the concept name, followed by `:` and a syntax compliant expression.
    - Concepts name could be replaced with a valid taxonomy concept ID.
  + `include_or`: This row represents a single entry within the `INCLUDE_OR` section.
    Only a single `INCLUDE_OR` section is allowed, thus all rows of this type are combined with the `OR` operator.

    - Multiple conditions are allowed.
      They are separated with the `;` character and combined with the `AND` operator.
    - Each condition specifies the concept name, followed by `:` and a syntax compliant expression.
    - Concepts name could be replaced with a valid taxonomy concept ID.
  + `exclude_and`: This row represents a single entry within the `EXCLUDE_AND` section.
    Only a single `EXCLUDE_AND` section is allowed, thus all rows of this type are combined with the `AND` operator.

    - Multiple conditions are allowed.
      They are separated with the `;` character and combined with the `OR` operator.
    - Each condition specifies the concept name, followed by `:` and a syntax compliant expression.
    - Concepts name could be replaced with a valid taxonomy concept ID.
  + `exclude_or`: This row represents a single entry within the `EXCLUDE_OR` section.
    Only a single `EXCLUDE_OR` section is allowed, thus all rows of this type are combined with the `OR` operator.

    - Multiple conditions are allowed.
      They are separated with the `;` character and combined with the `AND` operator.
    - Each condition specifies the concept name, followed by `:` and a syntax compliant expression.
    - Concepts name could be replaced with a valid taxonomy concept ID.
  + `export`: This row represents export instructions, for example which file the module should be exported to.
    The exported file shall contain an `IMPORT` statement as required to maintain integrity across multiple files.

|  |  |
| --- | --- |
|  | The restrictions associated with the sections can be found in [Section 6.4.3.3, "INCLUDE and EXCLUDE semantics"](../06_model_concept/06_04_openodd_modules.html#sec-include-and-exclude-semantics). For example, there shall be at least one single include or exclude, and no more than one single exclude and no more than one single exclude are permitted. |

## 8.4.3 Illustrating module representation with tabular format

In this section, we provide an example representation of different modules expressed in free-form notation (refer [Code 108](#code-module-representation)) as a Tabular Module specification discussed in the previous section.

Code 108. Example for a module representation (free-form notation)

```
file2
    IMPORT definitions from
        taxonomy.yml  # assumes all taxonomy concepts are defined in this file
        file1.yml     # connectivity definition

    ODD is
        odd_main_module_1 is defined as             # The main ODD specification entry point
            TITLE is ODD for ADS v0.23
            INCLUDE_AND when
                road_type is                        # Only specific road types are inside ODD
                    town_expressway
                    town_collector
                    town_arterial
            EXCLUDE_OR when                         # These are not safe for V0.23
                bad_weather is true                 # Numerous distinct conditions may represent bad weather
                bad_connectivity is true            # Numerous distinct conditions may represent bad connectivity
                AND when                            # Exclude a very specific type of work zones
                    road_type is town_expressway    # on the town_expressway road type
                    zone_type is work_zone

        bad_weather_module_1 is defined as
            LABEL defined by this module
                bad_weather                         # This module defines one of the bad weather conditions
            INCLUDE_AND when
                rain_intensity_type is              # This type of rain results in too many vision subsystem detection errors
                    convective
                    orographic

        bad_weather_module_2 is defined as
            LABEL defined by this module
                bad_weather                         # This module defines one of the bad weather conditions
            INCLUDE_OR when
                wind_speed is greater than 50 km/h  # This wind intensity results in unstable sensors, leading to too many vision subsystem detection errors

file1
    IMPORT definitions from
        taxonomy.yml                                # assumes all taxonomy concepts are defined in this file

    MODULES specification is as follows
        bad_connectivity_module_1 is defined as
            TITLE is conditions for bad connectivity
            LABELS defined by this module
                bad_connectivity                    # This module defines one of the bad connectivity conditions
            INCLUDE_OR when
                downlink_latency is greater than 10 msec    # Need to receive real-time events
                downlink_throughput is less than 1 Mbps     # Need to receive large amounts of data

        bad_connectivity_module_2 is defined as
            TITLE is unacceptable positioning
            LABELS defined by this module
                bad_connectivity                    # This module defines one of the bad connectivity conditions
            INCLUDE_OR                              # The minimal positioning are:
                global_positioning is true          # it is sufficient to have GNSS per the global_positioning module
                local_positioning is true           # it is sufficient to have positioning beacons per the local_positioning module
```

Table 145. Module export in multi-language translation


| MODULE\_ID | ROLE | CONTENT or CONDITION |
| --- | --- | --- |
| 001 | id | odd\_main\_module\_1 |
| 001 | definition\_type | odd |
| 001 | export | file2.yml |
| 001 | references | taxonomy.yml |
| 001 | title-EN | ODD for ADS v0.23 |
| 001 | title-DE | ODD für ADS v0.23 |
| 001 | title-JP | 自動運転システム向け運用設計ドメイン v0.23 |
| 001 | title-CN | 自动驾驶系统的操作设计领域 v0.23 |
| 001 | include\_or | road\_type: [town\_expressway, town\_collector, town\_arterial] |
| 001 | exclude\_or | bad\_weather: true |
| 001 | exclude\_or | bad\_connectivity: true |
| 001 | exclude\_or | road\_type: [town\_expressway]; zone\_type: [work\_zone] |
| 002 | id | bad\_connectivity\_module\_1 |
| 002 | definition\_type | module |
| 002 | export | file1.yml |
| 002 | references | taxonomy.yml |
| 002 | title-EN | Conditions for bad connectivity |
| 002 | title-DE | Bedingungen für schlechte Konnektivität |
| 002 | title-JP | 接続不良の条件 |
| 002 | title-CN | 连接不良的条件 |
| 002 | labels | bad\_connectivity |
| 002 | include\_or | downlink\_latency: < 10 msec |
| 002 | include\_or | downlink\_throughput: > 1 Mbps |
| 003 | id | bad\_connectivity\_module\_2 |
| 003 | definition\_type | module |
| 003 | export | file1.yml |
| 003 | references | taxonomy.yml |
| 003 | title-EN | Unacceptable positioning |
| 003 | title-DE | Inakzeptable Verortung |
| 003 | title-JP | 許容できない配置 |
| 003 | title-CN | 不可接受的定位 |
| 003 | labels | bad\_connectivity |
| 003 | include\_or | global\_positioning: true |
| 003 | include\_or | local\_positioning: true |
| 004 | id | bad\_weather\_module\_1 |
| 004 | definition\_type | module |
| 004 | export | file2.yml |
| 004 | references | taxonomy.yml |
| 004 | title-EN | Specification of bad weather because of rain |
| 004 | title-DE | Definition von schlechtem Wetter wegen Regens |
| 004 | title-JP | 雨による悪天候の仕様 |
| 004 | title-CN | 下雨等恶劣天气规范 |
| 004 | labels | bad\_weather |
| 004 | include\_and | rain\_intensity\_type: [convective, orographic] |
| 005 | id | bad\_weather\_module\_2 |
| 005 | definition\_type | module |
| 005 | export | file2.yml |
| 005 | references | taxonomy.yml |
| 005 | title-EN | Specification of bad weather because of wind |
| 005 | title-DE | Definition von schlechtem Wetter wegen Wind |
| 005 | title-JP | 風による悪天候の仕様 |
| 005 | title-CN | 大风造成的恶劣天气规范 |
| 005 | labels | bad\_weather |
| 005 | include\_or | wind\_speed: > 50 km/h |

|  |  |
| --- | --- |
|  | The expressions in this example use spaces for readability, which are not part of the specification. |