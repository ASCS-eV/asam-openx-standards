# ASAM OpenODD® v1.0.0 — A.2 XML taxonomy representation

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_b_xml_02_taxonomy.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# A.2 XML taxonomy representation

## A.2.1 Taxonomy XML export

### A.2.1.1 Overview

The purpose of the XML export is to provide an XML representation of the taxonomy which is aligned with the ASAM OpenODD® model.
Each taxonomy export should result in a single XML file comprising all taxonomy concepts and their specification, across multiple languages.

The XML format has the following advantages:

* Unique IDs are specified for each **taxonomy concept**.
* Multi-language translation can be provided for every **taxonomy concept**.
* XML Schema validation can be used to verify each document.

### A.2.1.2 Hierarchical XML taxonomy format

We start by illustrating the XML usage; the schema specification is detailed in subsequent sections.

Consider the following example taxonomy YAML:

```
TAXONOMY:
    environmental_conditions:                             # This is a *Record*.
        weather:                                          # This is a *Record*.
            wind:                                         # This is a *Record*.
                wind_speed: float velocity                # This is an attribute of type "float" having a unit type of "velocity".
            rainfall:                                     # This is a *Record*.
                rainfall_rate: float precipitation_rate   # This is an attribute of type "float" having a unit type of "precipitation_rate".
                rainfall_type:                            # This is an attribute of type *Categorical*.
                    - dynamic                             # This is a *Categorical Literal* specified by the categorical_literal symbol "dynamic".
                    - convective                          # This is a *Categorical Literal* specified by the categorical_literal symbol "convective".
                    - orographic                          # This is a *Categorical Literal* specified by the categorical_literal symbol "orographic".
```

To represent this example, and taxonomy in general, there is a need for a `<TAXONOMY_CONCEPT>` element.

As per the ASAM OpenODD® model, the concept element comprises of an ID attribute representing the Unique ID (UID) of the concept, which is a string unique within the XML export.

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <TAXONOMY_CONCEPT id="environment_condition">
    </TAXONOMY_CONCEPT>
</TAXONOMY>
```

As per the ASAM OpenODD® model, the `<TAXONOMY_CONCEPT>` element, there is a need to specify the description, and comments which can be translated to multiple languages:

* A `<DESCRIPTION/>` child element (within `<TAXONOMY_CONCEPT/>`) comprising an English text description.
* A `<COMMENT/>` child element (within `<TAXONOMY_CONCEPT/>`) comprising an English text of the comment.
* An `<I13N/>` child of either `<DESCRIPTION/>` or `<COMMENT/>` providing the translation of the parent English text.
  That `<I13N/>` element comprises a `language` attribute specifying the 2-char ISO 639 [[10](../bibliography.html#bib-iso639)] code of the language.

This is achieved by introducing an internationalization `<I13N/>` element, and an `<COMMENT/>` element, as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <TAXONOMY_CONCEPT id="001" name="environment_condition">
        <I13N language="DE">Umweltbedingung</I13N>
        <I13N language="CN">环境条件</I13N>
        <DESCRIPTION>The root element.
            <I13N  language="DE">Das Wurzelelement.</I13N>
            <I13N  language="CN">根元素.</I13N>
        </DESCRIPTION>
        <COMMENT>Comment about the root element.
            <I13N  language="DE">Ein Kommentar zum Wurzelelement.</I13N>
            <I13N  language="CN">对根元素进行注释。.</I13N>
        </COMMENT>
    </TAXONOMY_CONCEPT>
</TAXONOMY>
```

The XML schema for the Taxonomy Concept `<TAXONOMY_CONCEPT/>` element is as follows:

* It comprises an `xs:unique` attribute with the path `TAXONOMY_CONCEPT/id`.
* It comprises an `xs:complexType` `xs:sequence` of one of the following child elements:

  + A `<DESCRIPTION/>` child element comprising a description; its child `<I13N/>` elements are specified as part of the `<DESCRIPTION/>` element schema.
  + A `<COMMENT/>` child element comprising a comment; its child `<I13N/>` elements are specified as part of the `<COMMENT/>` schema.
  + A `<META_DATA/>` child element comprising a meta-data map, intended for use by the toolchain; its child `<META_DATA/>` elements are specified as part of the `<META_DATA/>` schema.
  + A `<EXPORT/>` child element comprising the export instructions for this concept; see the export instructions specification in ASAM OpenODD® model.
  + A `<STRUCT/>` child group used to specify user-defined structures mapping to the Record object in the ASAM OpenODD® model.
* The following attributes are specified for the `<TAXONOMY_CONCEPT/>` element:

  + The `id` attribute specifying the string id of the concept unique within the XML file; no need to provide global uniqueness; see ID specification in ASAM OpenODD® model.
  + The `name` attribute, which matches the `id` attribute.
  + The `parent_id` (optional) attribute used when providing a `record` based format rather than pure hierarchy format.
    The record based format allows concepts to be specified as a flat list of elements mirroring the tabular representation format; see explanation and example in the next sub-section.
  + The `custom_type` (optional) attribute used when the concept is a user-define type specified in the taxonomy data; it is the `Record` object defined in the ASAM OpenODD® model.

```
<xs:element name='TAXONOMY_CONCEPT'>
    <xs:unique name="uniqueConceptId">
        <xs:selector xpath="TAXONOMY_CONCEPT/id"/>
        <xs:field xpath="."/>
    </xs:unique>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            <xs:element ref="EXPORT" minOccurs="0" maxOccurs="1"/>
            <xs:group ref="STRUCT" minOccurs="1" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="custom_type" type="xs:IDREF" use="optional"/>
    </xs:complexType>
</xs:element>
```

Putting all these requirements together, the XML representation of the full YAML example above is as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <TAXONOMY_CONCEPT id="001" name="environment_condition">
        <I13N language="DE">Umweltbedingung</I13N>
        <I13N language="CN">环境条件</I13N>
        <DESCRIPTION>The root element.
            <I13N  language="DE">Das Wurzelelement.</I13N>
            <I13N  language="DE">根元素.</I13N>
        </DESCRIPTION>
        <COMMENT>Comment on the root element.
            <I13N  language="DE">Das Wurzelelement.</I13N>
            <I13N  language="DE">根元素.</I13N>
        </COMMENT>
        <TAXONOMY_CONCEPT id="002" name="weather">
            <I13N language="DE">Wetter</I13N>
            <I13N language="CN">天气</I13N>
            <TAXONOMY_CONCEPT id="002" name="wind">
                <I13N language="DE">Wind</I13N>
                <I13N language="CN">风</I13N>
                <NUMERIC id="003" name="wind_speed" value_type="float" unit_type="velocity">
                    <I13N language="DE">Windgeschwindigkeit</I13N>
                    <I13N language="CN">风速</I13N>
                </NUMERIC>
            </TAXONOMY_CONCEPT>
            <TAXONOMY_CONCEPT id="004" name="rainfall">
                <I13N language="DE">Niederschlag</I13N>
                <I13N language="CN">雨量</I13N>
                <NUMERIC id="003" name="rainfall_rate" value_type="float" unit_type="velocity">
                    <I13N language="DE">Niederschlagsmenge</I13N>
                    <I13N language="CN">降雨率</I13N>
                </NUMERIC>
                <CATEGORICAL id="004" name="rainfall_type">
                    <I13N language="DE">Niederschlagsart<I13N/>
                    <I13N language="CN">降雨类型<I13N/>
                    <CATEGORICAL id="005" name="rain_dynamic">
                        <I13N language="DE">dynamisch<I13N/>
                        <I13N language="CN">动态的<I13N/>
                    <CATEGORICAL/>
                    <CATEGORICAL id="006" name="rain_convective">
                        <I13N language="DE">konvektiv<I13N/>
                        <I13N language="CN">对流的<I13N/>
                    <CATEGORICAL/>
                    <CATEGORICAL id="007" name="rain_orographic">
                        <I13N language="DE">orographisch<I13N/>
                        <I13N language="DE">地形<I13N/>
                    <CATEGORICAL/>
                </CATEGORICAL>
            </TAXONOMY_CONCEPT>
        </TAXONOMY_CONCEPT>
    </TAXONOMY_CONCEPT>
</TAXONOMY>
```

### A.2.1.3 Flat list XML format using patent ID

The challenge with the above nested solution is that it is difficult to maintain and extend with additional elements.
A more maintainable format decouples the representation of the children from that of their parents.
It is equivalent to a `row` based format, whereby each child is added as a decoupled row.

To avoid additional (child) elements from being nested within parents, there is a need to use a `parentId` attribute.
Each concept specified the ID of its parent, thus defining the entire hierarchy.

To illustrate the simplification achieved using parent\_id, consider the following example below, which is the full representation of the above example hierarchical taxonomy:
With this example, there is a flat list of **self-contained** `</TAXONOMY_CONCEPT/>` elements.

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <TAXONOMY_CONCEPT id="id001" name="environmental_conditions"/>
    <TAXONOMY_CONCEPT id="id002" name="weather" parent_id="id001"/>
    <TAXONOMY_CONCEPT id="id003" name="wind" parent_id="id002"/>
    <NUMERIC id="id004" name="wind_speed" value_type="float" parent_id="id003" unit_std="ASAM" unit_type="velocity"/>
    <TAXONOMY_CONCEPT id="id005" name="rainfall" parent_id="id001"/>
    <TAXONOMY_CONCEPT id="id006" name="rainfall_rate" parent_id="id001">
        <I13N language="DE">Niederschlagsmenge</I13N>
        <COMMENT>Average rain over an area and a period of time.
            <I13N language="DE">Durchschnittlicher Niederschlag über einem Gebiet in einem bestimmten Zeitraum.</I13N>
        </COMMENT>
    </TAXONOMY_CONCEPT>
    <NUMERIC id="id007" name="wind_speed" parent_id="id003" value_type="float" unit_std="ASAM" unit_type="velocity">
        <I13N language="DE">Windgeschwindigkeit</I13N>
    </NUMERIC>

    <CATEGORICAL id="id008" name="rainfall_type" parent_id="id005">
        <I13N language="DE">Niederschlagsart</I13N>
        <CATEGORICAL id="id009" name="rain_dynamic">
            <I13N language="DE">dynamisch</I13N>
        </CATEGORICAL>
        <CATEGORICAL id="id010" name="rain_convective">
            <I13N language="DE">konvektiv</I13N>
        </CATEGORICAL>
        <CATEGORICAL id="id011" name="rain_orographic">
            <I13N language="DE">orographisch</I13N>
        </CATEGORICAL>
    </CATEGORICAL>
</TAXONOMY>
```

### A.2.1.4 XML format for user-defined (custom) types

The approach extends to defining taxonomy based user-defined types.
A new `custom_type` attribute is introduced, which refers to the ID of the concept sed as the type; any taxonomy subtree can become a custom type.
This can be illustrated using the following example (notice the use of `custom_type`):

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <TAXONOMY_CONCEPT id="id001" name="vector_types">
        <TAXONOMY_CONCEPT id="id002" name="cartesian_vector">
            <NUMERIC id="id003" name="x" value_type="float" unit_std="ASAM" unit_type="length"/>
            <NUMERIC id="id004" name="y" value_type="float" unit_std="ASAM" unit_type="length"/>
            <NUMERIC id="id005" name="z" value_type="float" unit_std="ASAM" unit_type="length"/>
        </TAXONOMY_CONCEPT>
        <TAXONOMY_CONCEPT id="id006" name="radial_vector">
            <NUMERIC id="id007" name="r" value_type="float" unit_std="ASAM" unit_type="length"/>
            <NUMERIC id="id008" name="a" value_type="float" unit_std="ASAM" unit_type="angle"/>
        </TAXONOMY_CONCEPT>
    </TAXONOMY_CONCEPT>
    <TAXONOMY_CONCEPT id="id009" name="dynamic_environment">
        <TAXONOMY_CONCEPT id="id010" name="vehicles">
            <TAXONOMY_CONCEPT id="id011" name="position" custom_type="id002"/>
            <TAXONOMY_CONCEPT id="id012" name="trajectory" custom_type="id006"/>
            <TAXONOMY_CONCEPT id="id013" name="velocity" custom_type="id006">
                <CATEGORICAL id="id014" name="vehicle_type">
                    <CATEGORICAL id="id015" name="motorcycle"/>
                    <CATEGORICAL id="id016" name="car"/>
                    <CATEGORICAL id="id017" name="truck"/>
                </CATEGORICAL>
            </TAXONOMY_CONCEPT>
        </TAXONOMY_CONCEPT>
    </TAXONOMY_CONCEPT>
</TAXONOMY>
```

### A.2.1.5 XML format for numeric attributes

Numeric attributes are specified using the `<NUMERIC/>` elements, having the following attributes:

* The `id` attribute specifying the string id of the concept unique within the XML file; no need to provide global uniqueness; see ID specification in the ASAM OpenODD® model section.
* The `value_type` indicating whether it is a `float` or an `integer` number.
* The `unit_std` specifying which units standard is associated with the numeric value. See the ASAM OpenODD® model for the role of the unique specification standard.
* The `unit_type` specifying which types of units are compatible with the numeric value; only compatible unique types can be compared. See the ASAM OpenODD® model for the role of unit\_type and the list of supported unit types.

The following is a simple example representing a parent `rainfall` concept having an attribute `rainfall_rate` child which is a float precipitation rate:

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <TAXONOMY_CONCEPT id="id001" id="rainfall"/>
    <NUMERIC id="id002" parent_id="id001" id="rainfall_rate" value_type="float" unit_std="ASAM" unit_type="precipitation_rate"/>
</TAXONOMY>
```

The full XSD specification for numeric values is as follows:

* The attributes of `id`, `name`, `parent_id`, having the same specification and role as for the `<TAXONOMY_CONCEPT/>` element.
  The xpath of the unique `id` is `NUMERIC/id`.
* The xs:complexType xs:sequence represents the same elements of `DESCRIPTION`, `COMMENT`, `META_DATA` and `I13N`, having the same role as for the `<TAXONOMY_CONCEPT/>` element.
* The attribute of `value_type` which is an `xs:simpleType` `xs:enumeration` of either a `float` or an `integer`.
* The attribute of `unit_sts` which specifies the standard of unique use to specify the `unit_type`.
* The attribute of `unit_type` which is a `xs:simpleType` `xs:enumeration` of supported unit types, as per the corresponding ASAM OpenODD® model section.

```
<xs:element name='NUMERIC'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="value_type" use="required">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="float"/>
                    <xs:enumeration value="integer"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="unit_std" type="xs:string" use="required"/>
        <xs:attribute name="unit_type" use="required">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="length"/>
                    <xs:enumeration value="area"/>
                    <xs:enumeration value="volume"/>
                    <xs:enumeration value="angle"/>
                    <xs:enumeration value="force"/>
                    <xs:enumeration value="mass"/>
                    <xs:enumeration value="duration"/>
                    <xs:enumeration value="time"/>
                    <xs:enumeration value="count"/>
                    <xs:enumeration value="fraction"/>
                    <xs:enumeration value="percent"/>
                    <xs:enumeration value="temperature"/>
                    <xs:enumeration value="frequency"/>
                    <xs:enumeration value="charge"/>
                    <xs:enumeration value="flux"/>
                    <xs:enumeration value="grains"/>
                    <xs:enumeration value="electric_potential"/>
                    <xs:enumeration value="electric_current"/>
                    <xs:enumeration value="electric_current_density"/>
                    <xs:enumeration value="power"/>
                    <xs:enumeration value="data_size"/>
                    <xs:enumeration value="velocity"/><!-- = length / time -->
                    <xs:enumeration value="precipitation_rate"/><!-- = length / time ; not volume over time  -->
                    <xs:enumeration value="occurrence"/><!-- = count / time -->
                    <xs:enumeration value="bandwidth"/><!-- = data_size / time -->
                    <xs:enumeration value="pressure"/><!-- = force / area -->
                    <xs:enumeration value="torque"/><!-- = force * length -->
                    <xs:enumeration value="acceleration"/><!-- = velocity / time^2 -->
                    <xs:enumeration value="risk"/><!-- = occurrence / time -->
                    <xs:enumeration value="reliability"/><!-- = occurrence / time -->
                    <xs:enumeration value="confidence"/><!-- = occurrence / count -->
                    <xs:enumeration value="percentile"/><!-- = count / count -->
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
    <xs:unique name="uniqueNumericId">
        <xs:selector xpath="NUMERIC/id"/>
        <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

### A.2.1.6 XML format for categorical attributes

Numeric attributes are specified using the `<NUMERIC/>` elements, having the following attributes:

* The `id` attribute specifying the string id of the concept unique within the XML file; no need to provide global uniqueness; see ID specification in the ASAM OpenODD® model.
* A hierarchy of child `<CATEGORICAL/>` element representing the category sub-tree.

As an example, consider representing the `vru` (Vulnerable Road User) concept having the categorical values of `toddler`, `child`, and `adult`:

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
   <CATEGORICAL id="id003" name="vru">
        <CATEGORICAL id="id004" name="toddler"/>
        <CATEGORICAL id="id005" name="child"/>
        <CATEGORICAL id="id006" name="adult"/>
    </CATEGORICAL>
</TAXONOMY>
```

The equivalent flat-list XML format for specifying the same categorical tree is as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <CATEGORICAL id="id003" name="vru"/>
    <CATEGORICAL id="id004" name="toddler" parent_id="id003"/>
    <CATEGORICAL id="id005" name="child" parent_id="id003"/>
    <CATEGORICAL id="id006" name="adult" parent_id="id003"/>
</TAXONOMY>
```

The full XSD specification for numeric values is as follows:

* The attributes of `id`, `name`, `parent_id`, having the same specification and role as for the `<TAXONOMY_CONCEPT/>` element.
  The xpath of the unique `id` is `CATEGORICAL/id`.
* The `xs:complexType` `xs:sequence` represents the same elements of `DESCRIPTION`, `COMMENT`, `META_DATA`, and `I13N`, having the same role as for the `<TAXONOMY_CONCEPT/>` element.

```
    <xs:element name='CATEGORICAL'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='CATEGORICAL' minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required"/>
            <xs:attribute name="name" type="xs:string" use="required"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
        <xs:unique name="uniqueCategoricalId">
          <xs:selector xpath="CATEGORICAL/id"/>
          <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
```

### A.2.1.7 XML format for specifications of categorical ranges

Categorical literal values may specify ranges over numeric concepts, according to "replace by range constraints".
This enables converting numeric values into enumerations.

As an example, consider representing the four rain levels of `not_detectable`, `light_rain`, `moderate_rain`, `heavy_rain`:

```
rainfall is
    rainfall_rate is float precipitation_rate
    rainfall_level is
        not_detectable when rainfall_rate is less than 0.1 mm/h
        light_rain when     rainfall_rate in [0.1 .. 2.5] mm/h
        moderate_rain when  rainfall_rate in [2.5 .. 7.6] mm/h
        heavy_rain when     rainfall_rate is greater than 7.6 mm/h
```

This example can be described using **flat XML** as follows:

* The parent `rainfall` and the numeric attribute `rainfall_rate` follow the format described above.
* The categorical literals are each specified as independent self contained `<CATEGORICAL_RANGES/>` elements having their parent\_id point to the `rainfall` element.
* The `not_detectable` literal is defined as using the `<CATEGORICAL_RANGE_UPPER/>` expression and the `<SMALLER_THAN_NUMBER_TERM/>` element indicating that when the `rainfall_rate` is less than 0.1 then the `rainfall_level` is `not_detectable`.
* The `light_rain` literal is defined as using the `<CATEGORICAL_RANGE_MIDDLE/>` expression and the `<CATEGORICAL_RANGE_MIDDLE/>` element indicating that when the `rainfall_rate` is between 0.1 and 2.5 then the `rainfall_level` is `light_rain`.
* The `moderate_rain` literal is defined as using the `<CATEGORICAL_RANGE_MIDDLE/>` expression and the `<CATEGORICAL_RANGE_MIDDLE/>` element indicating that when the `rainfall_rate` is between 2.5 and 7.6 then the `rainfall_level` is `moderate_rain`.
* The `heavy_rain` literal is defined as using the `<CATEGORICAL_RANGE_LOWER/>` expression and the `<GREATER_THAN_NUMBER_TERM/>` element indicating that when the `rainfall_rate` is greater than 7.6 then the `rainfall_level` is `heavy`.

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <TAXONOMY_CONCEPT id="id001" name="rainfall"/>
    <NUMERIC id="id002" parent_id="id001" id="rainfall_rate" value_type="float" unit_std="ASAM" unit_type="precipitation_rate"/>
    <CATEGORICAL id="id003" name="rainfall_level" parent_id="id001"/>
    <CATEGORICAL_RANGES id="id004" name="not_detectable" numeric_field="rainfall_rate" parent_id="id003">
        <CATEGORICAL_RANGE_UPPER>
            <SMALLER_THAN_NUMBER_TERM max="0.1"/>
        </CATEGORICAL_RANGE_UPPER>
    </CATEGORICAL_RANGES>
    <CATEGORICAL_RANGES id="id005" name="light_rain" numeric_field="rainfall_rate" parent_id="id003">
        <CATEGORICAL_RANGE_MIDDLE>
            <RANGE_NUMBER_TO_CONCEPT_TERM min="0.1" max="2.5"/>
        </CATEGORICAL_RANGE_MIDDLE>
    </CATEGORICAL_RANGES>
    <CATEGORICAL_RANGES id="id005" name="moderate_rain" numeric_field="rainfall_rate" parent_id="id003">
        <CATEGORICAL_RANGE_MIDDLE>
            <RANGE_NUMBER_TO_CONCEPT_TERM min="1.5" max="7.6"/>
        </CATEGORICAL_RANGE_MIDDLE>
    </CATEGORICAL_RANGES>
    <CATEGORICAL_RANGES id="id006" name="heavy_rain" numeric_field="rainfall_rate" parent_id="id003">
        <CATEGORICAL_RANGE_LOWER>
            <GREATER_THAN_NUMBER_TERM max="7.6"/>
        </CATEGORICAL_RANGE_LOWER>
    </CATEGORICAL_RANGES>
</TAXONOMY>
```

The full XSD specification for numeric values is as follows:

* The attributes of `id`, `name`, `parent_id`, having the same specification and role as for the `<TAXONOMY_CONCEPT/>` element.
  The xpath of the unique `id` is `CATEGORICAL/id`.
* The `xs:complexType` `xs:sequence` represents the same elements of `DESCRIPTION`, `COMMENT`, `META_DATA`, and `I13N`, having the same role as for the `<TAXONOMY_CONCEPT/>` element.

```
    <xs:element name='CATEGORICAL_RANGES'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
                <xs:element ref="CATEGORICAL_RANGE_LOWER" minOccurs="0" maxOccurs="1"/>
                <xs:element ref="CATEGORICAL_RANGE_MIDDLE" minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref="CATEGORICAL_RANGE_UPPER" minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required"/>
            <xs:attribute name="name" type="xs:string" use="optional"/>
            <xs:attribute name="numeric_field" type="xs:IDREF" use="required"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
        <xs:unique name="uniqueRangeId">
          <xs:selector xpath="CATEGORICAL_RANGES/id"/>
          <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
```

### A.2.1.8 XML format for Boolean concept specifications

The specification of Boolean concepts is following the same pattern as for the other concept types.

The full XSD specification for numeric values is as follows:

* The attributes of `id`, `name`, `parent_id`, having the same specification and role as for the `<TAXONOMY_CONCEPT/>` element.
  The xpath of the unique `id` is `BOOLEAN/id`.
* The `xs:complexType` `xs:sequence` represents the same elements of `DESCRIPTION`, `COMMENT`, `META_DATA`, and `I13N`, having the same role as for the `<TAXONOMY_CONCEPT/>` element.

```
<xs:element name='BOOLEAN'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
    <xs:unique name="uniqueBooleanId">
      <xs:selector xpath="BOOLEAN/id"/>
      <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

### A.2.1.9 XML format for Boolean threshold specifications

Boolean thresholds are very common for converting continuous numeric values into true/false values.
Consider, for example, designing the flag `is_dangerous_wind` using the numeric field `wind_speed`.
Assume that speed above 50 km/h is dangerous.
This could be specified using the following free-form example, providing a taxonomy with a numeric `wind_speed` field to support the specification of the `is_dangerous_wind` Boolean threshold concept:

```
wind is
    wind_speed is float velocity
    is_dangerous_wind is             # categorical object
        true when                    # categorical literal object (*not* boolean primitive type)
            wind_speed is greater than 50 km/h     # upper bound expression
        false when                   # categorical literal object (*not* boolean primitive type)
            wind_speed is less than or equal to 50 km/h    # lower bound expression object
```

The specification of Boolean concepts is following the same pattern as for the other concept types.
In addition to the standard attributes, a Boolean threshold includes the following attributes:

* The `field` attribute referring to the numeric field used to define the threshold.
* The `threshold` attribute specifying the numeric threshold.
* the `unit` attribute specifying the unit (not `unit_type`) used to interpret the numeric value; for example, km/h.

The full XSD specification for numeric values is as follows:

* The attributes of `id`, `name`, `parent_id`, having the same specification and role as for the `<TAXONOMY_CONCEPT/>` element.
  The xpath of the unique `id` is `BOOLEAN/id`.
* The `xs:complexType` `xs:sequence` represents the same elements of `DESCRIPTION`, `COMMENT`, `META_DATA`, and `I13N`, having the same role as for the `<TAXONOMY_CONCEPT/>` element.
* The `field`, `threshold` and `unit` attributes as specified above.

```
<xs:element name='BOOLEAN_THRESHOLD'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="field" type="xs:IDREF" use="required"/>
        <xs:attribute name="threshold" type="xs:float" use="required"/>
        <xs:attribute name="unit" type="xs:string" use="required"/>
    </xs:complexType>
    <xs:unique name="uniqueBooleanThresholdId">
        <xs:selector xpath="BOOLEAN_THRESHOLD/id"/>
        <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

### A.2.1.10 XML format for taxonomy measure specifications

Measures are numeric taxonomy attributes defined on top of categorical literals.
Example measures include `length`, `width`, `duration`, `confidence`, `occurrence_rate`.

Consider the example taxonomy with measures of `occurrence` and `confidence` associated with the Vulnerable Road Users (VRU) of `toddler`, `child`, `adult`:

```
vulnerable_road_user is
    pedestrians is
        civil is
            toddler
            child
            adult
        toddler.occurrence is a float representing risk
        toddler.confidence is a float representing confidence
        child.occurrence is a float representing risk
        child.confidence is a float representing confidence
        adult.occurrence is a float representing risk
        adult.confidence is a float representing confidence
    pedestrians.occurrence is a float representing risk
    pedestrians.confidence is a float representing confidence
```

The following is an example XML fragment specifying such measures:

* The taxonomy hierarchy is described as per the above, using a concept hierarchy.
* The measures are numeric attributes which use the doc notation, leveraging the requirements that concept names are unique.
* The flat XML format can be supported for measures as it is supported for regular taxonomy numeric attributes, per above specifications.

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
   <TAXONOMY_CONCEPT id="id001" name="vulnerable_road_user">
        <TAXONOMY_CONCEPT id="id002" name="pedestrians">
            <CATEGORICAL id="id003" name="civil">
                <CATEGORICAL id="id004" name="toddler"/>
                <CATEGORICAL id="id005" name="child"/>
                <CATEGORICAL id="id006" name="adult"/>
            </CATEGORICAL>
            <NUMERIC id="id007" name="toddler.occurrence_rate" value_type="float" unit_std="ASAM" unit_type="risk"/>
            <NUMERIC id="id008" name="toddler.confidence" value_type="float" unit_std="ASAM" unit_type="confidence"/>
            <NUMERIC id="id009" name="child.occurrence_rate" value_type="float" unit_std="ASAM" unit_type="risk"/>
            <NUMERIC id="id010" name="child.confidence" value_type="float" unit_std="ASAM" unit_type="confidence"/>
            <NUMERIC id="id011" name="adult.occurrence_rate" value_type="float" unit_std="ASAM" unit_type="risk"/>
            <NUMERIC id="id012" name="adult.confidence" value_type="float" unit_std="ASAM" unit_type="confidence"/>
        </TAXONOMY_CONCEPT>
        <NUMERIC id="id013" name="pedestrians.occurrence_rate" value_type="float" unit_std="ASAM" unit_type="risk"/>
        <NUMERIC id="id014" name="pedestrians.confidence" value_type="float" unit_std="ASAM" unit_type="confidence"/>
    </TAXONOMY_CONCEPT>
</TAXONOMY>
```

Note that measures are defined as regular taxonomy attributes using the "." notation.
As such, there is no need for a dedicated schema to differentiate measures from other numeric attributes.

### A.2.1.11 Incorporating meta-data using XML

Rich meta data can be added to taxonomy concepts using XML.
Meta-data comprises a generic collection of key-value pairs.
Consider, as an example, specifying for each taxonomy concept, the name of the most recent editor and the last updated date.

The following is an example XML description of such meta-data:

* A `<META_DATA/>` element is added as a child of the `<TAXONOMY_CONCEPT/>` element.
* An `<ITEM/>` element is added as a child to the `<META_DATA/>` element for each key-value pair.
* The `<ITEM/>` element comprises the attributes of `key` and `value` specifying the content of the meta-data item.
* Whereas the meta-data can be combined with multi-language `<I13N/>` elements to provide full translation, there are no constraints on the language used to specify the content of the `key` and `value` attributes.

```
<?xml version="1.0" encoding="UTF-8"?>
<TAXONOMY xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <TAXONOMY_CONCEPT id="id001" name="environmental_conditions">
        <TAXONOMY_CONCEPT id="id002" name="weather">
            <META_DATA>
                <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                <ITEM key="last_updated_by" value="John Doe"/>
                <ITEM key="last_updated_date" value="2023-02-07"/>
            </META_DATA>
            <TAXONOMY_CONCEPT id="id003" name="wind">
                <META_DATA>
                    <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                    <ITEM key="last_updated_by" value="John Doe"/>
                    <ITEM key="last_updated_date" value="2023-02-07"/>
                </META_DATA>
                <NUMERIC id="id004" name="wind_speed" value_type="float" unit_std="ASAM" unit_type="velocity">
                    <META_DATA>
                        <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                        <ITEM key="last_updated_by" value="John Doe"/>
                        <ITEM key="last_updated_date" value="2023-02-07"/>
                    </META_DATA>
                </NUMERIC>
            </TAXONOMY_CONCEPT>
        </TAXONOMY_CONCEPT>
        <TAXONOMY_CONCEPT id="id005" name="rainfall">
            <TAXONOMY_CONCEPT id="id006" name="rainfall_rate">
                <I13N language="DE">Niederschlagsmenge</I13N>
                <COMMENT>Average rain over an area and a period of time.
                    <I13N language="DE">Durchschnittlicher Niederschlag über ein Gebiet in einem bestimmten Zeitraum.</I13N>
                </COMMENT>
                <META_DATA>
                    <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                    <ITEM key="last_updated_by" value="John Doe"/>
                    <ITEM key="last_updated_date" value="2023-02-07"/>
                </META_DATA>

                <NUMERIC id="id007" name="wind_speed" value_type="float" unit_std="ASAM" unit_type="velocity">
                    <I13N language="DE">Windgeschwindigkeit</I13N>
                    <META_DATA>
                        <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                        <ITEM key="last_updated_by" value="John Doe"/>
                        <ITEM key="last_updated_date" value="2023-02-07"/>
                    </META_DATA>
                </NUMERIC>

                <CATEGORICAL id="id008" name="rainfall_type">
                    <I13N language="DE">Niederschlagsart</I13N>
                    <META_DATA>
                        <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                        <ITEM key="last_updated_by" value="John Doe"/>
                        <ITEM key="last_updated_date" value="2023-02-07"/>
                    </META_DATA>

                    <CATEGORICAL id="id009" name="rain_dynamic">
                        <I13N language="DE">dynamisch</I13N>
                        <META_DATA>
                            <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                            <ITEM key="last_updated_by" value="John Doe"/>
                            <ITEM key="last_updated_date" value="2023-02-07"/>
                        </META_DATA>
                    </CATEGORICAL>
                    <CATEGORICAL id="id010" name="rain_convective">
                        <I13N language="DE">konvektiv</I13N>
                        <META_DATA>
                            <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                            <ITEM key="last_updated_by" value="John Doe"/>
                            <ITEM key="last_updated_date" value="2023-02-07"/>
                        </META_DATA>
                    </CATEGORICAL>
                    <CATEGORICAL id="id011" name="rain_orographic">
                        <I13N language="DE">orographisch</I13N>
                        <META_DATA>
                            <ITEM key="imported_from" value="taxonomy_file_01.yml"/>
                            <ITEM key="last_updated_by" value="John Doe"/>
                            <ITEM key="last_updated_date" value="2023-02-07"/>
                        </META_DATA>
                    </CATEGORICAL>
                </CATEGORICAL>
            </TAXONOMY_CONCEPT>
        </TAXONOMY_CONCEPT>
    </TAXONOMY_CONCEPT>
</TAXONOMY>
```

The following is the XSD specification for the `<META_DATA/>` elements:

* The `xs:element` `META_DATA` is defined as a `xs:complex_type` `xs:sequence` of `<ITEM/>` elements.
* Each `xs:element` `ITEM` comprises of a `key` and `value` attribute, plus an optional sequence (min\_occurs=0) of `<I13N/>` elements supporting internationalization of the meta-data.

```
<xs:element name='META_DATA'>
    <xs:complexType>
        <xs:sequence>
            <xs:element name="ITEM" minOccurs="1" maxOccurs="unbounded">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="I13N" minOccurs="0" maxOccurs="unbounded"/>
                    </xs:sequence>
                    <xs:attribute name="key" use="required"/>
                    <xs:attribute name="value" use="required"/>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## A.2.2 ASAM OpenODD® taxonomy XML schema

The root of the XML schema is the `<ODD>` element, which specifies a single `<TAXONOMY>` element as a child.

The `<TAXONOMY>` element includes an unbounded of `<STRUCT>` elements as children, plus an `<EXPORT>` element specifying the export instructions.  
The following is the XSD specification of the `<TAXONOMY>` element:

```
<xs:element name='TAXONOMY'>
    <xs:complexType>
        <xs:sequence>
            <xs:group ref='STRUCT' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='EXPORT' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

* A `<STRUCT>` element defines a **taxonomy concept** of type **Record** which accepts various typed children.  
  The following is the XSD fragment for the `<TAXONOMY_CONCEPT>` element:

```
<xs:group name="STRUCT">
    <xs:choice>
        <xs:element ref='NUMERIC' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='BOOLEAN' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='BOOLEAN_THRESHOLD' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='CATEGORICAL' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='CATEGORICAL_RANGES' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='CATEGORICAL_RANGE_LOWER' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='CATEGORICAL_RANGE_MIDDLE' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='CATEGORICAL_RANGE_UPPER' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='CONCEPT' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='TAXONOMY_DEFINED_TYPE' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='SHAPE_FILE' minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref='BINARY_EXTENSION' minOccurs="0" maxOccurs="unbounded"/>
    </xs:choice>
</xs:group>
```

The `<STRUCT>` element comprises of the following taxonomy concept types:

* `CONCEPT`: This is a tree node containing a subtree, also known as a parent.  
  It comprises a unique ID attribute, as well as a name, an optional parent\_id and an optional custom\_type (taxonomy user defined type).  
  It can also contain a nested `<STRUCT>` element.  
  The `<TAXONOMY_CONCEPT>` element can optionally be associated with `<I13N>` element to support multiple languages, a `<COMMENT>` element supporting a multi-language comment, a `<META_DATA>` element to link key-value pairs to the concept, and `<EXPORT>` specifying export instructions.  
  The following is the XSD fragment for the `<TAXONOMY_CONCEPT>` element:

```
<xs:element name='TAXONOMY_CONCEPT'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            <xs:element ref="EXPORT" minOccurs="0" maxOccurs="1"/>
            <xs:group ref="STRUCT" minOccurs="1" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="custom_type" type="xs:IDREF" use="optional"/>
    </xs:complexType>
    <xs:unique name="uniqueConceptId">
        <xs:selector xpath="CONCEPT/id"/>
        <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

* `NUMERIC`: This is a numeric attribute corresponding to a **taxonomy concept** **Primitive Type** specifying a float or integer value\_type and associated with a `unit_type`.  
  The `<NUMERIC>` element can optionally be associated with an `<I13N>` element to support multiple languages, a `<COMMENT>` element supporting a multi-language comment, and an `<META_DATA>` element to link key-value pairs to the concept.  
  The following is the XSD fragment for the `<NUMERIC>` element:

```
<xs:element name='NUMERIC'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="value_type" use="required">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="float"/>
                    <xs:enumeration value="integer"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="unit_std" type="xs:string" use="required"/>
        <xs:attribute name="unit_type" use="required">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    ... the xs:enumeration for all unit types ...
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
    </xs:complexType>
    <xs:unique name="uniqueNumericId">
        <xs:selector xpath="NUMERIC/id"/>
        <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

* `BOOLEAN`: This is a Boolean attribute corresponding to a **taxonomy concept** **Primitive Type** specifying a flag.
  It is associated with a name and an optional parent\_id.  
  The `<BOOLEAN>` element can optionally be associated with `<I13N>` element to support multiple languages, a `<COMMENT>` element supporting a multi-language comment, and a `<META_DATA>` element to link key-value pairs to the concept.
  The following is the XSD fragment for the `<BOOLEAN>` element:

```
<xs:element name='BOOLEAN'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
    <xs:unique name="uniqueBooleanId">
        <xs:selector xpath="BOOLEAN/id"/>
        <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

* `BOOLEAN_THRESHOLD`:
  This is a Boolean attribute corresponding to a **taxonomy concept** **Primitive Type** specifying a flag.
  It is associated with a name and an optional parent\_id.  
  In addition, this attribute specifies a numeric, `field`, and a corresponding `threshold` and the `unit` used to determine the truth value of this flag.  
  The `<BOOLEAN_THRESHOLD>` element can optionally be associated with an `<I13N>` element to support multiple languages, a `<COMMENT>` element supporting a multi-language comment, and a `<META_DATA>` element to link key-value pairs to the concept.

The following is the XSD fragment for the `<BOOLEAN_THRESHOLD>` element:

```
<xs:element name='BOOLEAN_THRESHOLD'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="field" type="xs:IDREF" use="required"/>
        <xs:attribute name="threshold" type="xs:float" use="required"/>
        <xs:attribute name="unit" type="xs:string" use="required"/>
    </xs:complexType>
    <xs:unique name="uniqueBooleanThresholdId">
        <xs:selector xpath="BOOLEAN_THRESHOLD/id"/>
        <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

* `CATEGORICAL`:
  This is a categorical attribute corresponding to a **taxonomy concept** of **Categorical** type.  
  It specifies a list of possible values which can be associated with the attribute; multiple values could be assigned (that means this is a set).  
  It is associated with a name and an optional parent\_id.  
  The `<CATEGORICAL>` element can optionally be associated with `<I13N>` element to support multiple languages, a `<COMMENT>` element supporting a multi-language comment, and a `<META_DATA>` element to link key-value pairs to the concept.  
  The following is the XSD fragment for the `<CATEGORICAL>` element:

```
<xs:element name='CATEGORICAL'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='CATEGORICAL' minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
    <xs:unique name="uniqueCategoricalId">
        <xs:selector xpath="CATEGORICAL/id"/>
        <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

* `CATEGORICAL_RANGES`: This is a categorical attribute corresponding to a **taxonomy concept** of **Categorical** type.
  It specifies a list of possible values which can be associated with the attribute; multiple values could be assigned (that means this is a set).  
  It is associated with a name and an optional parent\_id.  
  In addition, this attribute specifies a numeric , `numeric_field`, and a reference to a list of **Expression** elements describing the range of values defining the **Categorical Literal**.  
  The `<CATEGORICAL_RANGES>` element can optionally be associated with `<I13N>` element to support multiple languages, a `<COMMENT>` element supporting a multi-language comment, and a `<META_DATA>` element to link key-value pairs to the concept.  
  The following is the XSD fragment for the `<CATEGORICAL_RANGES>` element:

```
<xs:element name='CATEGORICAL_RANGES'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            <xs:element ref="CATEGORICAL_RANGE_LOWER" minOccurs="0" maxOccurs="1"/>
            <xs:element ref="CATEGORICAL_RANGE_MIDDLE" minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref="CATEGORICAL_RANGE_UPPER" minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="optional"/>
        <xs:attribute name="numeric_field" type="xs:IDREF" use="required"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
    <xs:unique name="uniqueRangeId">
        <xs:selector xpath="CATEGORICAL_RANGES/id"/>
        <xs:field xpath="."/>
    </xs:unique>
</xs:element>
```

The categorical range values are literals associated a categorical literal with a range of values for a numerical attribute.
The association of ranges induces an order onto the literals.

* `CATEGORICAL_RANGE_UPPER`:
  This is the "smallest" enum value defined by an upper bound constraint on the numerical field.
* The `category` attribute specifies the string provided in the taxonomy, for example `heavy_rain`.
* It comprises the attributes of `id`, `parent_id` attributes following the convention used for `<TAXONOMY_CONCEPT/>`.
* It is specified in terms of the `<LOWER_BOUND/>` constraint.
* It supports `<DESCRIPTION/>`, `<COMMENT/>` and `<I13N/>` according to the convention used for `<TAXONOMY_CONCEPT/>`
* The upper bound element is defined according to the following XSD fragment:

```
<xs:element name='CATEGORICAL_RANGE_UPPER'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            <xs:group ref="LOWER_BOUND" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="category" type="xs:string" use="required"/>
        <xs:attribute name="id" type="xs:ID" use="optional"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
</xs:element>
```

The lower bound expression is defined by the following XSD fragment:

```
<xs:group name="LOWER_BOUND">
    <xs:choice>
        <xs:element ref="GREATER_THAN_NUMBER_TERM"/>
        <xs:element ref="GREATER_THAN_CONCEPT_TERM"/>
    </xs:choice>
</xs:group>
```

The expression specifying a range of numeric values is defined by the following XSD fragment (note that meta-data can be attached to the entire term):

```
<xs:element name='SMALLER_THAN_NUMBER_TERM'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
        <xs:attribute name="max" type="xs:float" use="required"/>
        <xs:attribute name="field" type="xs:IDREF"/>
        <xs:attribute name="unit" type="xs:string" use="required"/>
    </xs:complexType>
</xs:element>
```

The expression specifying a range of ordered categorical-range literals is defined by the following XSD fragment (note that meta-data can be attached to the entire term):

```
<xs:element name='SMALLER_THAN_CONCEPT_TERM'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
        <xs:attribute name="max" type="xs:IDREF" use="required"/>
        <xs:attribute name="field" type="xs:IDREF"/>
    </xs:complexType>
</xs:element>
```

* `CATEGORICAL_RANGE_MIDDLE`: All "middle" enum values defined by a range constraint on the numerical field.
  The "range middle" element is defined according to the following XSD described below, having the following attribution:
* The `category` attribute specifies the string provided in the taxonomy, for example `heavy_rain`.
* It comprises the attributes of `id`, `parent_id` attributes following the convention used for `<TAXONOMY_CONCEPT/>`.
* It is specified in terms of the `<RANGE/>` constraint.
* It supports `<DESCRIPTION/>`, `<COMMENT/>` and `<I13N/>` according to the convention used for `<TAXONOMY_CONCEPT/>`
* The upper bound element is defined according to the following XSD fragment:

```
<xs:element name='CATEGORICAL_RANGE_MIDDLE'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            <xs:group ref="RANGE" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="category" type="xs:string" use="required"/>
        <xs:attribute name="id" type="xs:ID" use="optional"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
</xs:element>
```

The range expression has several flavors:

* two numbers
* number and concept
* concept to number
* concept to concept

This is defined by the following XSD fragment:

```
<xs:group name="RANGE">
    <xs:choice>
        <xs:element ref="RANGE_TWO_NUMBERS_TERM"/>
        <xs:element ref="RANGE_NUMBER_TO_CONCEPT_TERM"/>
        <xs:element ref="RANGE_CONCEPT_TO_NUMBER_TERM"/>
        <xs:element ref="RANGE_CONCEPT_TO_CONCEPT_TERM"/>
    </xs:choice>
</xs:group>
```

The `NUMBER_TO_NUMBER` flavor is defined as follows:

```
<xs:element name='RANGE_TWO_NUMBERS_TERM'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
        <xs:attribute name="min" type="xs:float" use="required"/>
        <xs:attribute name="max" type="xs:float" use="required"/>
        <xs:attribute name="field" type="xs:IDREF"/>
        <xs:attribute name="unit" type="xs:string" use="required"/>
    </xs:complexType>
</xs:element>
```

The `NUMBER_TO_CONCEPT` flavor is defined as follows:

```
<xs:element name='RANGE_NUMBER_TO_CONCEPT_TERM'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
        <xs:attribute name="min" type="xs:float" use="required"/>
        <xs:attribute name="max" type="xs:IDREF" use="required"/>
        <xs:attribute name="field" type="xs:IDREF"/>
        <xs:attribute name="unit" type="xs:string" use="required"/>
    </xs:complexType>
</xs:element>
```

The `CONCEPT_TO_NUMBER` flavor is defined as follows:

```
<xs:element name='RANGE_CONCEPT_TO_NUMBER_TERM'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
        <xs:attribute name="min" type="xs:IDREF" use="required"/>
        <xs:attribute name="max" type="xs:float" use="required"/>
        <xs:attribute name="field" type="xs:IDREF"/>
    </xs:complexType>
</xs:element>
```

The `CONCEPT_TO_CONCEPT` flavor is defined as follows:

```
<xs:element name='RANGE_CONCEPT_TO_CONCEPT_TERM'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
        <xs:attribute name="min" type="xs:IDREF" use="required"/>
        <xs:attribute name="max" type="xs:IDREF" use="required"/>
        <xs:attribute name="field" type="xs:IDREF"/>
    </xs:complexType>
</xs:element>
```

* `CATEGORICAL_RANGE_LOWER`: This is the "largest" enum value defined by a lower bound constraint on the numerical field.
  The "upper bound" element is defined according to the following XSD described below, having the following attribution:
* The `category` attribute specifies the string provided in the taxonomy, for example `heavy_rain`.
* It comprises the attributes of `id`, `parent_id` attributes following the convention used for `<TAXONOMY_CONCEPT/>`.
* It is specified in terms of the `<UPPER_BOUND/>` constraint.
* It supports `<DESCRIPTION/>`, `<COMMENT/>` and `<I13N/>` according to the convention used for `<TAXONOMY_CONCEPT/>`
* The upper bound element is defined according to the following XSD fragment:

```
<xs:element name='CATEGORICAL_RANGE_LOWER'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            <xs:group ref="UPPER_BOUND" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="category" type="xs:string" use="required"/>
        <xs:attribute name="id" type="xs:ID" use="optional"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
</xs:element>
```

The lower bound expression is defined by the following XSD fragment:

```
<xs:group name="UPPER_BOUND">
    <xs:choice>
        <xs:element ref="SMALLER_THAN_NUMBER_TERM"/>
        <xs:element ref="SMALLER_THAN_CONCEPT_TERM"/>
    </xs:choice>
</xs:group>
```

The expression specifying a range of numeric values is defined by the following XSD fragment (note that meta-data can be attached to the entire term):

```
<xs:element name='GREATER_THAN_NUMBER_TERM'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
        <xs:attribute name="min" type="xs:float" use="required"/>
        <xs:attribute name="field" type="xs:IDREF"/>
        <xs:attribute name="unit" type="xs:string" use="required"/>
    </xs:complexType>
</xs:element>
```

The expression specifying a range of ordered categorical-range literals is defined by the following XSD fragment (note that meta-data can be attached to the entire term):

```
<xs:element name='GREATER_THAN_CONCEPT_TERM'>
    <xs:complexType>
        <xs:sequence>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
        <xs:attribute name="min" type="xs:IDREF" use="required"/>
        <xs:attribute name="field" type="xs:IDREF"/>
    </xs:complexType>
</xs:element>
```

* `TAXONOMY_DEFINED_TYPE`: The user-defined type based on a taxonomy subtree is used to extend the basic types with complex structures.

This is defined using the following XSD fragment:

```
<xs:element name='TAXONOMY_DEFINED_TYPE'>
    <xs:complexType>
        <xs:attribute name="id" type="xs:ID"/>
        <xs:attribute name="type_id" type="xs:IDREF"/>
        <xs:attribute name="name" type="xs:string"/>
    </xs:complexType>
</xs:element>
```

* `SHAPE_FILE`: A special type is used to refer to a binary shape file.

Such concepts are primarily used to specify geo-fenced areas, as well as scope whereby special restrictions apply.
A shape file concept is defined as follows:

```
<xs:element name='SHAPE_FILE'>
    <xs:complexType>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="file_name" type="xs:string" use="required"/>
    </xs:complexType>
</xs:element>
```

* `BINARY_EXTENSION`: Binary extensions are supported as well (beyond user-defined taxonomy types and shapefiles).

The binary extension is defined as follows:

```
<xs:element name='BINARY_EXTENSION'>
    <xs:complexType>
        <xs:attribute name="id" type="xs:ID" use="required"/>
        <xs:attribute name="name" type="xs:string" use="required"/>
        <xs:attribute name="file_name" type="xs:string" use="required"/>
    </xs:complexType>
</xs:element>
```