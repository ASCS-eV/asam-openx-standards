# ASAM OpenLABEL v1.0.0 — 2. Introduction

- **Source**: ASAM_OpenLABEL_BS_V1-0-0.html
- **Version**: v1.0.0
- **Date**: November 9, 2021
- **License**: Restricted distribution (ASAM e.V. member access)

---

## 2. Introduction


### 2.1. Overview


ASAM OpenLABEL standardizes the annotation format and the labeling methods for multi-sensor data streams and scenario files. Using a standardized format helps cut costs and save resources used in creating, converting, and transferring annotated and tagged data. ASAM OpenLABEL is represented in a JSON format and can therefore be easily parsed by tools and applications.


ASAM OpenLABEL specifies the different labeling methods that can be applied to multi-sensor data streams, for example, 2D bounding boxes for image data. With ASAM OpenLABEL, several labeling methods are provided which enable users to label common data streams, such as images or point clouds. Besides adding labels to multi-sensor data streams (labeling), ASAM OpenLABEL also provides methods to add tags to scenarios (tagging). These tags can be used to categorize scenarios and make them searchable in large databases. They can also provide additional information about the individual scenario, such as who captured or created the scenario, and with what setup was the scenario captured.


ASAM OpenLABEL provides a common data structure for organizing annotations for labeling multi-sensor data streams and tagging simulation and test scenarios.


#### 2.1.1. Multi-sensor data labeling


For the development, testing, and validation of highly automated driving functions, the industry makes extensive use of Machine Learning (ML), especially for realizing perception and prediction tasks. Machine learning requires significant amounts of training data. The data has to be annotated and enriched with metadata to be useful in the training and validation phases.


The lack of an industry standard aligning the structure and organization of these annotations creates several difficulties:


- It limits the reuse of annotated datasets.
- It poses challenges regarding the maintenance and updating of the annotations.
- It limits the sharing of datasets across the industry and between industry and academia.
- It has a negative impact on the quality of annotations.


The goals of the multi-sensor data labeling use case in ASAM OpenLABEL are as follows:


- Enable efficient sharing of annotated perception datasets and object lists.
- Increase the overall quality of annotations by providing a common data structure for annotations.
- Improve the maintainability and reuse of annotated datasets.


The multi-sensor data labeling use case in ASAM OpenLABEL fulfills the requirements of the following main target groups:


- Perception/computer-vision engineers
- Machine-learning engineers
- Perception/computer-vision research scientists
- Machine-learning research scientists
- Data-annotation engineers
- Data-annotation analysts
- Test engineers


#### 2.1.2. Scenario tagging


Scenario databases storing multi-sensor data, annotated multi-sensor data, simulation scenarios, and test scenarios can be very extensive. The sensor data and scenarios stored in these databases must be organized and tagged using semantic, meaningful tags. These tags refer, for example, to the content of the data, its ODD, the high-level behavior of the dynamic agents, and administrative information. Extracting the information required for the tags from scenario artifacts can be difficult and inefficient, and for some types of data it is impossible. This is due to the fact that the scenario definition language used is limited. Scenario tagging based on ASAM OpenLABEL addresses these issues.


The goals of the scenario tagging use case in ASAM OpenLABEL are as follows:


- Enable standardized clustering of test scenarios in scenario databases.
- Facilitate scenario storage systems that are separate to scenario definition representation.
- Enable efficient search and filtering of test scenarios in scenario databases.
- Enable sharing of information on test scenario categories and clusters between different databases or owners.
- Facilitate the sharing of scenarios between systems that may not have the ability to inspect the scenario definition or underlying scenario data.
- Improve maintainability and reuse of test scenarios and scenario data.
- Enable and enhance machine-learning training and validation datasets with additional information to organize the datasets.
- Enable specific machine-learning classification tasks to be performed on scenario data.


The scenario tagging use case in ASAM OpenLABEL fulfills the requirements of the following main target groups:


- Systems engineers
- Validation and verification engineers
- Functional-safety engineers
- Simulation specialists


#### 2.1.3. Deliverables


- ASAM OpenLABEL specification, this document
- ASAM OpenLABEL annotation schema provided in the openlabel_json_schema.json file
- ASAM OpenLABEL standardized set of tags for the scenario tagging use case provided in the openlabel_ontology_scenario_tags.ttl file
- ASAM OpenLABEL JSON examples provided at the openlabel.asam.net website


### 2.2. Conventions and notation


#### 2.2.1. Naming conventions


The following conventions apply in this document:


- Element names should be meaningful names with defined semantics.
- Element names should be written in camel case, ascii strings.
- The first character shall be a letter, an underscore, or a dollar sign ($).
- Subsequent characters may be a letter, a digit, an underscore, or a dollar sign.
- Reserved JavaScript keywords should be avoided.
- All element names should be uniquely defined in one ontology.


#### 2.2.2. Units


Unless stated otherwise, all numeric values within this specification are in SI units. Table 1 represents details of the units used.


*Table 1. Units*

| Unit of | Unit | Symbol |
| --- | --- | --- |
| Length | Meter | m |
| Duration, (relative) time | Second | s |
| Speed | Meters per second | m/s |
| Mass | Kilogram | kg |
| Angle | Radians | rad |
| Light intensity | Lux | lx |
| Image coordinate | Pixel | px |


##### Timestamp


The timestamp used in labeling depends on the raw sensor data. Different sensors sample data with various timestamp formats:


- UT (Universal Time): UT is derived from the rotation of the Earth. With the improvement of measurement, UT has several versions: UT0, UT1, UT2. UT time scale is irregular, since the rotation rate of the Earth is not constant.
- TAI (Temps Atomique International): TAI is the international atomic time scale based on a continuous counting of the SI second. It is provided by several laboratories around the world. The instruments "producing" TAI are ensembles of atomic frequency standards, such as rubidium oscillators, cesium oscillators, and hydrogen masers. TAI was set to coincide exactly with UT1 (universal Time version 1) at 0 hours of 1 January 1958.
- UTC (Universal Time Coordinated): UTC was introduced for the purpose of having a time with a constant scale but not deviating too much from UT1. UTC has the same time scale as TAI. A leap second is introduced into UTC once the difference between UT1 and UTC is longer than 0.9s.


The time reference of many GNSS (Global Navigation Satellite System) systems are based on the time scale of UTC and TAI with a specific constant offset [1].


- GPST (GPS Time) [2]: GPST is based on TAI as provided by the frequency standards of the GPS control center. It was introduced at 0 hours on 6 January 1980 (UTC) and always has a constant offset of -19s to TAI.
- GST (Galileo System Time): GST is a continuous time scale maintained by the Galileo Central Segment and synchronized with TAI. GST started from 0 hours on 22 August 1999 (UTC) and the offset between GST and TAI is -13 seconds.
- GLONASST (GLONASS Time) [3]: GLONASST is generated by the GLONASS Central Synchroniser and is synchronized with TAI. The constant offset between GLONASS and UTC (SU) is three hours.
- BDT (BeiDou Time): BDT is a continuous time scale starting at 0 hours on 1 January 2006 (UTC). It is synchronized with UTC (BSNC). The constant offset to TAI is -33 seconds.


The following overview shows how different timestamp standards can be transformed:


- UTC = TAI - LS
- GPST = UTC(USNO) + LS - 19s
- GST = TAI - 13s
- GLONASST = UTC(SU) + 3h
- BDT = UTC(BSNC) + LS - 33s

[Image: fig gnss time system and utc]

*Figure 1. The relationship between GNSS time systems and UTC*


Figure 1 shows the relationship between GNSS time systems and UTC. It was derived from Timescales [4].


Unix time is widely used in operating systems. It is the number of seconds that have elapsed since the Unix epoch, not counting UTC leap seconds. The Unix epoch started at 00:00:00 UTC on 1 January 1970. Every day is treated as if it contains exactly 86,400 seconds. Due to its handling of leap seconds, it is not a linear representation of UTC.


##### Representation of date and time format


The representation of data and time format is specified by the ISO 8601 standard [5]. The following format pattern is used:


`yyyy-MM-ddTHH:mm:ss.FFFZ`


Here, `T` is used as time designator. `.` is used as separator for the following millisecond portion. An explanation is given in the table below:


*Table 2. Date and time formats*

| Specifiers | Meaning | Example |
| --- | --- | --- |
| yyyy | Year (four digits) | 2021 |
| M,MM | Month in year (without/with leading zero) | 9, 09 |
| d,dd | Day in month (without/with leading zero) | 3, 03 |
| H,HH | Hours, 0-23 count (without/with leading zero) | 7, 07 |
| m,mm | Minutes (without/with leading zero) | 2, 02 |
| s,ss | Seconds (without/with leading zero) | 4, 04 |
| F,FF,FFF | Milliseconds (without/with leading zeros) | 357, 04, 002 |
| Z | RFC 822 time zone shifted to GMT | Z, +0100 |


If the time is in UTC, add a `Z` character directly after the time without a space. `Z` is the zone designator for the zero UTC offset. For example, `11:45 UTC` is represented as `11:45Z` or `T1145Z`.


If the time is in time zone other than UTC, the UTC offset is appended to the time in the same way that `Z` was above, in the form ±[hh]:[mm], ±[hh][mm], or ±[hh].


At a given date and time of 2021-09-03 11:23:56 in the Central European Time zone (CET), the following standard-format output is produced:


`2021-09-03T11:23:56.000+0100`


#### 2.2.3. Modal verbs


To ensure compliance with the ASAM OpenLABEL standard, users need to be able to distinguish between mandatory requirements, recommendations, permissions, as well as possibilities and capabilities.


The following rules for using modal verbs apply:


*Table 3. Rules for using modal verbs*

| Provision | Verbal form |
| --- | --- |
| Requirements Requirements shall be followed strictly in order to conform to the standard. Deviations are not allowed. | shall shall not |
| Recommendations Recommendations indicate that one possibility out of the several available is particularly suitable, without mentioning or excluding the other possibilities. | should should not |
| Permissions Permissions indicate a course of action permissible within the limits of ASAM OpenLABEL deliverables. | may need not |
| Possibilities and capabilities Verbal forms used to state possibilities or capabilities, whether technical, material, physical, etc. | can cannot |
| Obligations and necessities Verbal forms used to describe legal, organizational, or technical obligations and necessities that are not regulated or enforced by the ASAM OpenLABEL standard. | must must not |


#### 2.2.4. Typographic conventions


This documentation uses the following typographical conventions:


*Table 4. Typographical conventions*

| Mark-up | Definition |
| --- | --- |
| Code elements | This format is used for code elements, such as technical names of classes and attributes, as well as attribute values. |
| Terms | This format is used to introduce glossary terms, new terms and to emphasize terms. |


#### 2.2.5. Use of IDs


The following rules apply to the use of IDs in ASAM OpenLABEL:


- IDs shall be unique within a class.
