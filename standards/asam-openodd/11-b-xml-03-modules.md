# ASAM OpenODD® v1.0.0 — A.3 XML module representation

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_b_xml_03_modules.html
> **Standard**: ASAM OpenODD® v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# A.3 XML module representation

## A.3.1 Overall XML specification of ODD modules

The structure of the modular ODD specification using XML needs to include both taxonomy and modules.
Further, the XSD differentiates between the root module, regarded as modules of the "ODD" type, from the other modules.

* The root element is `<ODD/>`.
* The `<TAXONOMY/>` element is a direct child of the `<ODD/>` element; its context is as per the schema specified in the previous section.
* All top-level modules (do not depend on other modules), of type `ODD`, are direct children of the `<ODD/>` element.
* The other modules are listed within the `<MODULES/>` element.
  The child elements of the `<MODULES/>` elements represent modules which depend on the top-level modules or on other modules.

The following is the general structure of the overall XML specification of the ODD:

```
<ODD>
    <TAXONOMY/> <!-- the taxonomy concept hierarchy -->
    <MODULE/>   <!-- root module -->
    <MODULES/>  <!-- all other modules -->
</ODD>
```

The list of non-root modules is specified as an `xs:complexType` `xs:sequence` of references to `<MODULE/>` elements:

```
<xs:element name="MODULES">
    <xs:complexType>
        <xs:sequence minOccurs="1" maxOccurs="unbounded" >
            <xs:element ref="MODULE"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The model reference is used in lieu of direct inclusion of modules to support module-reuse through multiple references to a single module.
The schema definition for the reference is as follows:

* The reference is made using the `id` attribute, pointing to the model of interest.
* The module hierarchy can be represented using a flat XMLformat by leveraging the `parent_id` attribute.

```
<xs:element name="MODULE_REF">
    <xs:complexType>
        <!-- ID of the module element -->
        <xs:attribute name="id" type="xs:IDREF"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
</xs:element>
```

## A.3.2 Basic module specification

### A.3.2.1 Overview

As specified by the model, a module comprises of `TITLE`, `DESCRIPTION`, `COMMENT`, `LABEL`, `INCLUDE`, and `EXCLUDE` sections.

* The title, description and comment elements can be translated.
* Multiple label elements are used to define those label propositions which evaluate to `true` whenever the module evaluates to `true`.
* Meta-data can be added to the module to provide information such as the author’s name, update datetime, and other context information.
* One of the following options is valid:

  + A module comprising a single INCLUDE\_AND and EXCLUDE\_OR section.
  + A module comprising a single INCLUDE\_OR and EXCLUDE\_AND section.
  + A module comprising a single INCLUDE\_AND and EXCLUDE\_AND section.
  + A module comprising a single INCLUDE\_OR and EXCLUDE\_OR section.

Consider for example the following module:

* It comprises a single INCLUDE\_AND and EXCLUDE\_OR section.
* The INCLUDE\_AND section accepts situations in which the road\_type is either `expressway` and `town_local` by referring to the concepts with `id="id002"` and `id="id003"`.
* The EXCLUDE\_OR section rejects situation in which the `rain_rate` is greater than 3 mm/hr by referring to the concept with `id="id005"`.

```
      ...
      <TAXONOMY_CONCEPT id="id001" name="road_type">
           <CATEGORICAL id="id002" name="expressway"/>
           <CATEGORICAL id="id003" name="town_local"/>
      </TAXONOMY_CONCEPT>
      ...
      <TAXONOMY_CONCEPT id="id004" name="rain">
          <NUMERIC id="id005" name="rain_rate" value_type="float" unit_std="ASAM" unit_type="precipitation_rate"/>
      </TAXONOMY_CONCEPT>
      ...
      <MODULE id="id_use_case1_module">
        <INCLUDE_AND>
            <SET field="id001"> <!-- road_type -->
                <CATEGORICAL_REF id="id002"/>  <!-- categorical literal -->
                <CATEGORICAL_REF id="id003"/>  <!-- categorical literal -->
            </SET>
        </INCLUDE_AND>
        <EXCLUDE_OR>
            <GREATER_THAN_NUMBER_TERM field="id005" min="3" unit="mmph"/>  <!-- numeric attribute -->
        </EXCLUDE_OR>
      </MODULE>
      ...
```

The module XSD is specified as follows:

* The `<MODULE/>` element is an xs:complexType xs:sequence of `TITLE`, `DESCRIPTION`, `COMMENT`, `META_DATA`, `LABEL` elements and include/exclude groups.
* The `<INCLUDE/>` group is either an `<INCLUDE_AND/>` or `<INCLUDE_OR/>` element.
* The `<EXCLUDE/>` group is either an `<EXCLUDE_AND/>` or `<EXCLUDE_OR/>` element.
* Each include/exclude section is a xs:complexType xs:sequence of conditions.

  + Each include/exclude element comprises of the `id` and, optionally, the `parent_id` attribute

```
    <xs:element name="MODULE">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="TITLE" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="DESCRIPTION" minOccurs="0" maxOccurs="1"/>
                <xs:element ref="COMMENT" minOccurs="0" maxOccurs="1"/>
                <xs:element ref="META_DATA" minOccurs="0" maxOccurs="1"/>
                <xs:element ref="LABEL" minOccurs="0" maxOccurs="unbounded"/>
                <xs:group ref="INCLUDE" minOccurs="1" maxOccurs="1"/>
                <xs:group ref="EXCLUDE" minOccurs="1" maxOccurs="1"/>
                <xs:element ref="EXPORT" minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required"/>
        </xs:complexType>
        <xs:unique name="uniqueModuleId">
          <xs:selector xpath="MODULE/id"/>
          <xs:field xpath="."/>
        </xs:unique>
    </xs:element>
```

The include/exclude section is defined as follows:

* The `<INCLUDE/>` and `<EXCLUDE/>` elements are defined as a reference to either an `<INCLUDE_AND/>` or `<INCLUDE_OR/>` element.
* The content of the section is a sequence of conditions.

```
    <xs:group name="INCLUDE">
        <xs:choice>
            <xs:element ref="INCLUDE_AND"/>
            <xs:element ref="INCLUDE_OR"/>
        </xs:choice>
    </xs:group>
    <xs:element name="INCLUDE_AND">
        <xs:complexType>
            <xs:sequence>
                <xs:group ref="CONDITION" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>
    <xs:element name="INCLUDE_OR">
        <xs:complexType>
            <xs:sequence>
                <xs:group ref="CONDITION" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>

    <xs:group name="EXCLUDE">
        <xs:choice>
            <xs:element ref="EXCLUDE_AND"/>
            <xs:element ref="EXCLUDE_OR"/>
        </xs:choice>
    </xs:group>
    <xs:element name="EXCLUDE_AND">
        <xs:complexType>
            <xs:sequence>
                <xs:group ref="CONDITION" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>
    <xs:element name="EXCLUDE_OR">
        <xs:complexType>
            <xs:choice>
                <xs:group ref="CONDITION" minOccurs="1" maxOccurs="unbounded"/>
            </xs:choice>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>
```

### A.3.2.2 The format of the CONDITION element

A <CONDITION/> group is a xs:choice between numerous condition options:

* It can use a module reference, implying that the condition evaluates to `true` if and only if the module evaluates to `true`.
* It can use a label reference, implying that the condition evaluates to `true` whenever one of the modules declaring this label evaluates to `true` (meaning it is a "big OR").
* It can use an AND of a sequence of conditions, which evaluates to `true` if **all** of the conditions listed evaluate to `true`.
* It can use an OR of a sequence of conditions, which evaluates to `true` if **one** of conditions listed evaluate to `true`.
* It can also refer to an empty value defined by the `<UNKNOWN/>` element.
* In addition, a condition can be associated with meta-data.
* A reference to a module: The condition evaluates to `true` if and only if the module evaluates to `true`.
* It can use the 5 expressions described in the UML, including Equal, GreaterThan, SmallerThan, Range or List (defined as a SET element).

  + A reference to a greater-than `<GREATER_THAN_NUMBER_TERM/>` element representing a greater-than a specific number expression per the UML model.
  + A reference to a greater-than `<GREATER_THAN_CONCEPT_TERM/>` element representing a greater-than a concept (parameterized).
  + A reference to a smaller-than `<SMALLER_THAN_NUMBER_TERM/>` element representing a smaller-than a specific number expression per the UML model.
  + A reference to a smaller-than `<SMALLER_THAN_CONCEPT_TERM/>` element representing a smaller-than a concept (parameterized).
  + A reference to an equal `<EQUAL_TO_NUMBER_TERM/>` element representing an equal to a specific number expression per the UML model.
  + A reference to an equal `<EQUAL_TO_CONCEPT_TERM/>` element representing an equal to a concept (parameterized).
  + A reference to a range:

    - The element `<RANGE_TWO_NUMBERS_TERM/>` represents a range between two numbers.
    - The element `<RANGE_NUMBER_TO_CONCEPT_TERM/>` represents a number lower-bound and a concept upper bound.
    - The element `<RANGE_CONCEPT_TO_NUMBER_TERM/>` represents a concept lower-bound and a number upper bound.
    - The element `<RANGE_TWO_NUMBERS_TERM/>` represents a number lower-bound and a number upper bound.
* A nested `<AND/>` or `</OR>` element is represented using an xs:complexType xs:sequence of `<CONDITION/>` element, defined recursively; the XSD cannot validate the requirement of a single level nested of OR within AND and AND within OR.
* A special provision is provided to specify a missing value using the `<UNKNOWN/>` element.
* In addition, full meta-data linking is supported via the `<UNKNOWN/>` element.

```
<xs:group name="CONDITION">
    <xs:choice>
        <xs:element ref="MODULE_REF"/>
        <xs:element ref="LABEL_REF"/>
        <xs:element ref="BOOLEAN_REF"/>
        <xs:element ref="GREATER_THAN_NUMBER_TERM"/>
        <xs:element ref="GREATER_THAN_CONCEPT_TERM"/>
        <xs:element ref="SMALLER_THAN_NUMBER_TERM"/>
        <xs:element ref="SMALLER_THAN_CONCEPT_TERM"/>
        <xs:element ref="EQUAL_TO_NUMBER_TERM"/>
        <xs:element ref="EQUAL_TO_CONCEPT_TERM"/>
        <xs:element ref="RANGE_TWO_NUMBERS_TERM"/>
        <xs:element ref="RANGE_NUMBER_TO_CONCEPT_TERM"/>
        <xs:element ref="RANGE_CONCEPT_TO_NUMBER_TERM"/>
        <xs:element ref="SET"/>
        <xs:element name="AND" minOccurs="0" maxOccurs="unbounded">
            <xs:complexType>
                <xs:sequence>
                    <xs:group ref="CONDITION" minOccurs="1" maxOccurs="unbounded"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:element name="OR" minOccurs="0" maxOccurs="unbounded">
            <xs:complexType>
                <xs:sequence>
                    <xs:group ref="CONDITION" minOccurs="1" maxOccurs="unbounded"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:element name="UNKNOWN"/>
        <xs:element ref="META_DATA" minOccurs="0" maxOccurs="1"/>
    </xs:choice>
</xs:group>
```

### A.3.2.3 Example XML modules specification

Consider representing the following free-form modules:

```
id_use_case1_module when
    INCLUDE_AND is true when
        road_type is
            expressway
            town_local
    EXCLUDE_OR is false when
        rain_rate is smaller than 3 mm/hr

id_use_case2_module when
    INCLUDE_AND is true when
        id_module1 is true
        road_type is town_local
    EXCLUDE_OR is false when
        rain_rate is less than 8 mm/hr

id_module1 when
    INCLUDE_AND is true when
        id_module1 is true
        positioning is GPS
    EXCLUDE_OR is false when
        visibility is smaller than 1 km
```

This example module is described using XML as follows:

* All modules are placed under the `<MODULES/>` element.
* The 3 modules correspond to 3 elements, and their ids of each module element correspond to the module ids above.
* The `<INCLUDE/>` and `<EXCLUDE/>` sections comprise of a list of conditions; a single condition element in this example.
* The conditions are per the format described above.

  + The expression elements specified above are nested in each section element.
  + Module references are using the `<MODULE_REF/>` element.

```
<MODULES>
    <MODULE id="id_use_case1_module">
        <INCLUDE_AND>
            <SET field="id001">
                <CATEGORICAL_REF id="id002"/>
                <CATEGORICAL_REF id="id003"/>
            </SET>
        </INCLUDE_AND>
        <EXCLUDE_OR>
            <SMALLER_THAN_NUMBER_TERM field="id005" max="3" unit="mmph"/>
        </EXCLUDE_OR>
    </MODULE>
    <MODULE id="id_use_case2_module">
        <INCLUDE_AND>
            <SET field="id001">
                <CATEGORICAL_REF id="id003"/>
            </SET>
            <MODULE_REF id="id_module1"/>
        </INCLUDE_AND>
        <EXCLUDE_OR>
            <SMALLER_THAN_NUMBER_TERM field="id005" max="8" unit="mph"/>
        </EXCLUDE_OR>
    </MODULE>
    <MODULE id="id_module1">
        <EXCLUDE_AND>
            <SET field="id008">
                <!-- positioning -->
                <CATEGORICAL_REF id="id009"/>
                <!-- GPS -->
            </SET>
        </EXCLUDE_AND>
    </MODULE>
</MODULES>
```

## A.3.3 A Simplified "flat XML" leveraging Using parent IDs

A deep XML hierarchy may be difficult to manage.
As an example, it is common to store data in a database, and extract an XML export to transfer the data onto other systems.

To illustrate the simplification achieved using `parent_id`, consider the above example modules represented using a `parent_id` rather than a fully nested structure:

* The root module is introduced using a single element, `<MODULE id="id_root_module"/>`.
* The requirement that the two use case modules are in scope is achieved using `<MODULE_REF>` elements specifying that they are included using a `condition_type="INCLUDE_OR"` attribute.
* The individual modules are listed under the `<MODULES/>` elements using a single element per module, only specifying their IDs.
* The conditions refer to the module to which they below using `parent_id="<module_id>"`, and indicate which section the condition resides in using the `condition_type` attribute.

```
<?xml version="1.0" encoding="UTF-8"?>
<ODD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    <MODULE id="id_root_module"/>
    <MODULE_REF id="id_use_case1_module" parent_id="id_root_module" condition_type="INCLUDE_OR"/>
    <MODULE_REF id="id_use_case2_module" parent_id="id_root_module" condition_type="INCLUDE_OR"/>
    <MODULES>
        <MODULE id="id_use_case1_module"/>
        <MODULE id="id_use_case2_module"/>
        <MODULE id="id_module1"/>
        <!-- conditions for 1st module -->
        <SET field="id001" parent_id="id_use_case1_module" condition_type="INCLUDE_AND">
            <CATEGORICAL_REF id="id002"/>
            <CATEGORICAL_REF id="id003"/>
        </SET>
        <GREATER_THAN_NUMBER_TERM field="id005" min="3" unit="mmph" parent_id="id_use_case1_module" condition_type="EXCLUDE_OR"/>
        <!-- conditions for 2nd module -->
        <SET field="id001" parent_id="id_use_case2_module" condition_type="INCLUDE_AND">
            <CATEGORICAL_REF id="id003"/>
        </SET>
        <MODULE_REF id="id_module1" parent_id="id_use_case2_module" condition_type="INCLUDE_AND"/>
        <!-- module referenced in condition -->
        <SMALLER_THAN_NUMBER_TERM field="id005" max="8" unit="mph" parent_id="id_use_case2_module" condition_type="EXCLUDE_OR"/>
        <!-- conditions for 3rd module -->
        <SET field="id008" parent_id="id_module1" condition_type="EXCLUDE_AND">
            <!-- positioning -->
            <CATEGORICAL_REF id="id009"/>
            <!-- GPS -->
        </SET>
    </MODULES>
</ODD>
```

The above flat-XML structure can be easily mapped to a table in which each row represents a condition, and the ODD is simply assembled from a list of rows.
Note that the corresponding flat-XML format for the accompanying taxonomy is described in the section detailing the flat taxonomy XML format.

```
<xs:element name="MODULE_REF">
    <xs:complexType>
        <!-- ID of the module element -->
        <xs:attribute name="id" type="xs:IDREF"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
    </xs:complexType>
</xs:element>
<xs:element name="BOOLEAN_REF">
    <xs:complexType>
        <!-- ID of the boolean attribute -->
        <xs:attribute name="id" type="xs:IDREF"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string"/>
    </xs:complexType>
</xs:element>
<xs:element name="LABEL">
    <xs:complexType>
        <!-- ID of the label element -->
        <xs:attribute name="id" type="xs:ID"/>
        <xs:attribute name="name" type="xs:string"/>
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
    </xs:complexType>
</xs:element>
<xs:element name="LABEL_REF">
    <xs:complexType>
        <!-- ID of a label element -->
        <xs:attribute name="id" type="xs:IDREF"/>
        <xs:attribute name="condition_type" type="xs:string"/>
    </xs:complexType>
</xs:element>
```

The following schema fragment describes the usage of parent\_id and condition\_type attributes:

* All condition elements specify an optional `parent_id` attribute,
* In addition, all condition elements specify an optional condition\_type type attribute.
* When specified in the nested format, those attributes can be inferred from the nested XML structure.
* It is possible to mix nested and flat structures to optimize as needed.

```
<xs:element name="GREATER_THAN_NUMBER_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="GREATER_THAN_CONCEPT_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="SMALLER_THAN_NUMBER_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="SMALLER_THAN_CONCEPT_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="EQUAL_TO_NUMBER_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="EQUAL_TO_CONCEPT_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="RANGE_TWO_NUMBERS_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="RANGE_NUMBER_TO_CONCEPT_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="RANGE_CONCEPT_TO_NUMBER_TERM">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
<xs:element name="SET">
    <xs:complexType>
        ...
        <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        <xs:attribute name="condition_type" type="xs:string" use="optional"/>
        ...
    </xs:complexType>
</xs:element>
```

## A.3.4 Conditions with nested AND/OR aggregations

An important aspect of condition sections is the ability to include nested sub-sections:

* An `<INCLUDE_AND/>`,`<EXCLUDE_AND/>` section can specify an `<OR/>` subsection representing a disjunction of conditions.
* An `<INCLUDE_OR/>`,`<EXCLUDE_OR/>` section can specify an `<AND/>` subsection representing a conjunction of conditions.

This is illustrated below:

* The `<INCLUDE_AND/>` element comprises an `<OR/>` condition, referring to two categorical literal.

  + This condition will accept situations in which both GPS and beacon\_positioning are available.
* The `<EXCLUDE_OR/>` element comprises an `<AND/>` condition, referring to a single categorical literal.

  + This condition will reject situations in which a construction\_site\_detours is present.

```
...
<CATEGORICAL id="id018" name="GPS"/>
...
<CATEGORICAL id="id022" name="beacon_positioning"/>
...
<CATEGORICAL id="id027" name="construction_site_detours"/>
...
<INCLUDE_AND>
    ...
    <OR>
        <SET field="id015">
            <CATEGORICAL_REF id="id018"/> <!-- GPS -->
        </SET>
        <SET field="id019">
            <CATEGORICAL_REF id="id022"/> <!-- beacon_positioning -->
        </SET>
    </OR>
    ...
</INCLUDE_AND>
...
<EXCLUDE_OR>
    ...
    <AND>
        <SET field="id025">
            <CATEGORICAL_REF id="id027"/>
        </SET>
        <BOOLEAN_REF id="id024" /> <!-- construction_site_detours -->
    </AND>
    ...
</EXCLUDE_OR>
...
```

## A.3.5 Adding internationalization to modules

Internationalization of modules is achieved by adding an `<I13N/>` element as follows:

* Translations can be added only to the elements `<TITLE/>`,`<DESCRIPTION/>` and `<COMMENT/>`.
* Translations can be added using `<I13N/>` elements nested within the translated element.
* Each `<I13N/>` occurrence needs to specify the language it represents.

```
<MODULE id="id_root_module" handle="root_module">
    <TITLE>Meta Data Module
        <I13N language="DE">Metadatenmodul</I13N>
        <I13N language="JP">メタデータモジュール</I13N>
    </TITLE>
    <DESCRIPTION>Illustrate attaching meta data for modules.
        <I13N language="DE">Veranschaulichen Sie das Anhängen von Metadaten für Module</I13N>
        <I13N language="JP">モジュールのメタデータの添付を示す</I13N>
    </DESCRIPTION>
    <COMMENT>This is a basic example of internationalization.
        <I13N language="DE">Dies ist ein grundlegendes Beispiel für Internationalisierung</I13N>
        <I13N language="JP">これは国際化の基本的な例です</I13N>
    </COMMENT>
    <INCLUDE_OR>
        ...
    </INCLUDE_OR>
    <EXCLUDE_OR>
        ...
    </EXCLUDE_OR>
</MODULE>
```

This capability is achieved through the following schema fragment:

* Each of the above elements is defined using an `xs:complexType` `xs:sequence` of `<I13N/>` elements.
* The `<I13N/>` element specifies a required `language` attribute.

```
<xs:element name="COMMENT">
    <xs:complexType mixed="true">
        <xs:sequence>
            <xs:element ref="I13N" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>
<xs:element name="TITLE">
    <xs:complexType mixed="true">
        <xs:sequence>
            <xs:element ref="I13N" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>
<xs:element name="DESCRIPTION">
    <xs:complexType mixed="true">
        <xs:sequence>
            <xs:element ref="I13N" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>
<xs:element name="I13N">
    <xs:complexType mixed="true">
        <xs:attribute name="language" type="xs:string" use="required"/>
    </xs:complexType>
</xs:element>
```

In addition, descriptions can be added to conditions.

* All condition specifications include a reference to a `<DESCRIPTION/>` element.
* All description elements within condition can include nested `<I13N/>` elements and can be translated.

As an example, the XSD specification of the `<GREATER_THAN_NUMBER_TERM/>` condition is as follows:

* The reference to the `<DESCRIPTION/>` element is nested within the `xs:complexType` `xs:sequence`.

```
<xs:element name="GREATER_THAN_NUMBER_TERM">
    <xs:complexType>
        <xs:sequence>
            ...
            <xs:element ref="DESCRIPTION" minOccurs="0" maxOccurs="1"/>
            ...
        </xs:sequence>
        ...
    </xs:complexType>
</xs:element>
```

## A.3.6 Adding meta-data to modules

Modules can be associated with rich meta-data.
The XML meta-data specifies a collection of key-value pairs using `<ITEM/>` elements nested within the `<META_DATA/>` element.
As an example, specifying the date and type that a person updated a module can be achieved as follows:

```
...
<META_DATA>
    <ITEM key="last_updated_by" value="John Smith"/>
    <ITEM key="last_updated_date" value="2023-02-07"/>
</META_DATA>
...
```

Meta-data can be attached in various locations within a module:

* Meta-data can be associated with the `</MODULE/>` as a whole.
* Meta-data can be associated with an `INCLUDE` or `EXCLUDE` section.
* Meta-data can be associated with individual expression conditions within the section.

The addition of meta-data within the XML format is illustrated below.

```
<?xml version="1.0" encoding="UTF-8"?>
<ODD xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="open_odd.xsd">
    ...
    <MODULE id="id_example_module_metadata">
        <META_DATA> <!-- module meta-data -->
            <ITEM key="last_updated_by" value="John Doe"/>
            <ITEM key="last_updated_date" value="2023-02-07"/>
        </META_DATA>
        <INCLUDE_AND>
            <META_DATA> <!-- section meta-data -->
                <ITEM key="last_updated_by" value="John Doe"/>
                <ITEM key="last_updated_date" value="2023-02-07"/>
            </META_DATA>
            <SET field="id001">
                <CATEGORICAL_REF id="id002"/>
                <CATEGORICAL_REF id="id003"/>
                <META_DATA> <!-- individual condition meta-data -->
                    <ITEM key="last_updated_by" value="John Doe"/>
                    <ITEM key="last_updated_date" value="2023-02-07"/>
                </META_DATA>
            </SET>
        </INCLUDE_AND>
        <EXCLUDE_OR>
            <META_DATA> <!-- section meta-data -->
                <ITEM key="last_updated_by" value="John Doe"/>
                <ITEM key="last_updated_date" value="2023-02-07"/>
            </META_DATA>
            <GREATER_THAN_NUMBER_TERM field="id006" min="3" unit="mmph">
                <META_DATA> <!-- individual condition meta-data -->
                    <ITEM key="last_updated_by" value="John Doe"/>
                    <ITEM key="last_updated_date" value="2023-02-07"/>
                </META_DATA>
            <GREATER_THAN_NUMBER_TERM/>
        </EXCLUDE_OR>
    </MODULE>
    ...
</ODD>
```

This capability is achieved through the following XSD specifications:

* The `<MODULE/>` element includes a reference to the `<META_DATA/>` element within the `xs:complexType` `xs:sequence`.
* The `<CONDITION/>` group includes a reference to the `<META_DATA/>` element within the `xs:choice`.
* Each of the condition elements, for example `SET`, `GREATER_THAN_NUMBER_TERM`, includes a reference to the `<META_DATA/>` element within the `xs:complexType` `xs:sequence`.

```
<xs:element name="MODULE">
    <xs:complexType>
        <xs:sequence>
            ...
            <xs:element ref="META_DATA" minOccurs="0" maxOccurs="1"/>
            ...
        </xs:sequence>
        ...
    </xs:complexType>
</xs:element>

<xs:group name="CONDITION">
    <xs:choice>
        ...
        <xs:element ref="META_DATA" minOccurs="0" maxOccurs="1"/>
        ...
    </xs:choice>
    ...
</xs:group>

<xs:element name="GREATER_THAN_NUMBER_TERM">
    <xs:complexType>
        <xs:sequence>
            ...
            <xs:element ref="META_DATA" minOccurs="0" maxOccurs="1"/>
            ...
        </xs:sequence>
        ...
    </xs:complexType>
</xs:element>
```