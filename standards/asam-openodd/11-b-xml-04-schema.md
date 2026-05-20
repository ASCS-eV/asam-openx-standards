# ASAM Openodd v1.0.0 — A.4 XML schema representation

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_b_xml_04_schema.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# A.4 XML schema representation

## A.4.1 Full ASAM OpenODD XML schema

The full schema supports both taxonomy and module specifications.

```
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema' elementFormDefault='qualified'>
    <xs:element name='ODD'>
        <xs:complexType>
            <xs:sequence minOccurs="1" maxOccurs="unbounded">
                <xs:element ref='TAXONOMY' minOccurs="1" maxOccurs="1"/>
                <!--  Root module -->
                <xs:element ref='MODULE' minOccurs="0" maxOccurs="1"/>
                <!--  Support flat list of conditions for tabular representation -->
                <xs:element ref='INCLUDE_AND' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='INCLUDE_OR' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='EXCLUDE_AND' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='EXCLUDE_OR' minOccurs="0" maxOccurs="1"/>
                <xs:group ref='CONDITION' minOccurs="0" maxOccurs="unbounded"/>
                <!--  Remainder of the module tree -->
                <xs:element ref='MODULES' minOccurs="1" maxOccurs="1"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name='TAXONOMY'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='EXPORT' minOccurs="0" maxOccurs="1"/>
                <xs:group ref='STRUCT' minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name='EXPORT'>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="INSTRUCTIONS" minOccurs="1" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:attribute name="view" use="required"/>
                        <xs:attribute name="file_name" use="optional"/>
                        <xs:attribute name="database" use="optional"/>
                        <xs:attribute name="rest_end_point" use="optional"/>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

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
            <xs:element ref='TAXONOMY_CONCEPT' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='TAXONOMY_DEFINED_TYPE' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='SHAPE_FILE' minOccurs="0" maxOccurs="unbounded"/>
            <xs:element ref='BINARY_EXTENSION' minOccurs="0" maxOccurs="unbounded"/>
        </xs:choice>
    </xs:group>

    <xs:element name='TAXONOMY_DEFINED_TYPE'>
        <xs:complexType>
            <xs:attribute name="id" type="xs:ID"/>
            <xs:attribute name="type_id" type="xs:IDREF"/>
            <xs:attribute name="name" type="xs:string"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='SHAPE_FILE'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="I13N" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required"/>
            <xs:attribute name="name" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='BINARY_EXTENSION'>
        <xs:complexType>
            <xs:attribute name="id" type="xs:ID" use="required"/>
            <xs:attribute name="name" type="xs:string" use="required"/>
            <xs:attribute name="file_name" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='COMMENT'>
        <xs:complexType mixed="true">
            <xs:sequence>
                <xs:element ref="I13N" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name='TITLE'>
        <xs:complexType mixed="true">
            <xs:sequence>
                <xs:element ref="I13N" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name='DESCRIPTION'>
        <xs:complexType mixed="true">
            <xs:sequence>
                <xs:element ref="I13N" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name='I13N'>
        <xs:complexType mixed="true">
            <xs:attribute name="language" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

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

    <xs:element name='TAXONOMY_CONCEPT'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
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
        <xs:unique name="uniqueConceptId">
            <xs:selector xpath="CONCEPT/id"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

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
                        <xs:enumeration value="parent"/>
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
                        <xs:enumeration value="illuminance"/>
                        <xs:enumeration value="cloud_cover"/>
                        <xs:enumeration value="density"/>
                        <xs:enumeration value="frequency"/>
                        <xs:enumeration value="charge"/>
                        <xs:enumeration value="flux"/>
                        <xs:enumeration value="grains"/>
                        <xs:enumeration value="electric_potential"/>
                        <xs:enumeration value="electric_current"/>
                        <xs:enumeration value="electric_current_density"/>
                        <xs:enumeration value="power"/>
                        <xs:enumeration value="data_size"/>
                        <xs:enumeration value="velocity"/>
                        <!-- = length / time -->
                        <xs:enumeration value="precipitation_rate"/>
                        <!-- = length / time ; not volume over time  -->
                        <xs:enumeration value="occurrence"/>
                        <!-- = count / time -->
                        <xs:enumeration value="bandwidth"/>
                        <!-- = data_size / time -->
                        <xs:enumeration value="pressure"/>
                        <!-- = force / area -->
                        <xs:enumeration value="torque"/>
                        <!-- = force * length -->
                        <xs:enumeration value="acceleration"/>
                        <!-- = velocity / time^2 -->
                        <xs:enumeration value="risk"/>
                        <!-- = occurrence / time -->
                        <xs:enumeration value="reliability"/>
                        <!-- = occurrence / time -->
                        <xs:enumeration value="confidence"/>
                        <!-- = occurrence / count -->
                        <xs:enumeration value="percentile"/>
                        <!-- = count / count -->
                    </xs:restriction>
                </xs:simpleType>
            </xs:attribute>
        </xs:complexType>
        <xs:unique name="uniqueNumericId">
            <xs:selector xpath="NUMERIC/id"/>
            <xs:field xpath="."/>
        </xs:unique>
    </xs:element>

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
    <xs:element name='CATEGORICAL_REF'>
        <xs:complexType>
            <xs:attribute name="id" type="xs:IDREF"/>
        </xs:complexType>
    </xs:element>

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

    <xs:element name='CATEGORICAL_RANGE_LOWER'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
                <xs:group ref="UPPER_BOUND" minOccurs="1" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="category" type="xs:string" use="required"/>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='CATEGORICAL_RANGE_MIDDLE'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='I13N' minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
                <xs:group ref="RANGE" minOccurs="1" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="category" type="xs:string" use="required"/>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>

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

    <xs:element name='MODULES'>
        <xs:complexType>
            <xs:sequence minOccurs="1" maxOccurs="unbounded">
                <xs:element ref='MODULE'/>
                <xs:group ref='CONDITION' minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

    <xs:element name='MODULE'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='TITLE' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='COMMENT' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='LABEL' minOccurs="0" maxOccurs="unbounded"/>
                <xs:group ref='INCLUDE' minOccurs="0" maxOccurs="1"/>
                <xs:group ref='EXCLUDE' minOccurs="0" maxOccurs="1"/>
                <xs:element ref="EXPORT" minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required"/>
            <xs:attribute name="handle" type="xs:string" use="optional"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='MODULE_REF'>
        <xs:complexType>
            <!-- ID of the module element -->
            <xs:attribute name="id" type="xs:IDREF"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='BOOLEAN_REF'>
        <xs:complexType>
            <!-- ID of the boolean attribute -->
            <xs:attribute name="id" type="xs:IDREF"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='LABEL'>
        <xs:complexType>
            <!-- ID of the label element -->
            <xs:attribute name="id" type="xs:ID"/>
            <xs:attribute name="name" type="xs:string"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='LABEL_REF'>
        <xs:complexType>
            <!-- ID of a label element -->
            <xs:attribute name="id" type="xs:IDREF"/>
            <xs:attribute name="condition_type" type="xs:string"/>
        </xs:complexType>
    </xs:element>

    <xs:group name="INCLUDE">
        <xs:choice>
            <xs:element ref='INCLUDE_AND'/>
            <xs:element ref='INCLUDE_OR'/>
        </xs:choice>
    </xs:group>

    <xs:element name='INCLUDE_AND'>
        <xs:complexType>
            <xs:sequence>
                <xs:group ref='CONDITION' minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='INCLUDE_OR'>
        <xs:complexType>
            <xs:sequence>
                <xs:group ref='CONDITION' minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>

    <xs:group name="EXCLUDE">
        <xs:choice>
            <xs:element ref='EXCLUDE_AND'/>
            <xs:element ref='EXCLUDE_OR'/>
        </xs:choice>
    </xs:group>

    <xs:element name='EXCLUDE_AND'>
        <xs:complexType>
            <xs:sequence>
                <xs:group ref='CONDITION' minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='EXCLUDE_OR'>
        <xs:complexType>
            <xs:choice>
                <xs:group ref='CONDITION' minOccurs="1" maxOccurs="unbounded"/>
            </xs:choice>
            <xs:attribute name="id" type="xs:ID" use="optional"/>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
        </xs:complexType>
    </xs:element>

    <xs:group name='CONDITION'>
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
                        <xs:group ref='CONDITION' minOccurs="1" maxOccurs="unbounded"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="OR" minOccurs="0" maxOccurs="unbounded">
                <xs:complexType>
                    <xs:sequence>
                        <xs:group ref='CONDITION' minOccurs="1" maxOccurs="unbounded"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="UNKNOWN"/>
            <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
        </xs:choice>
    </xs:group>

    <xs:group name="LOWER_BOUND">
        <xs:choice>
            <xs:element ref="GREATER_THAN_NUMBER_TERM"/>
            <xs:element ref="GREATER_THAN_CONCEPT_TERM"/>
        </xs:choice>
    </xs:group>

    <xs:group name="RANGE">
        <xs:choice>
            <xs:element ref="RANGE_TWO_NUMBERS_TERM"/>
            <xs:element ref="RANGE_NUMBER_TO_CONCEPT_TERM"/>
            <xs:element ref="RANGE_CONCEPT_TO_NUMBER_TERM"/>
        </xs:choice>
    </xs:group>

    <xs:group name="UPPER_BOUND">
        <xs:choice>
            <xs:element ref="SMALLER_THAN_NUMBER_TERM"/>
            <xs:element ref="SMALLER_THAN_CONCEPT_TERM"/>
        </xs:choice>
    </xs:group>

    <xs:element name='GREATER_THAN_NUMBER_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="min" type="xs:float" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
            <xs:attribute name="unit" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='GREATER_THAN_CONCEPT_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="min" type="xs:IDREF" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='SMALLER_THAN_NUMBER_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="max" type="xs:float" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
            <xs:attribute name="unit" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='SMALLER_THAN_CONCEPT_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="max" type="xs:IDREF" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='EQUAL_TO_NUMBER_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="value" type="xs:integer" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
            <xs:attribute name="unit" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='EQUAL_TO_CONCEPT_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="value" type="xs:IDREF" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='RANGE_TWO_NUMBERS_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="min" type="xs:float" use="required"/>
            <xs:attribute name="max" type="xs:float" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
            <xs:attribute name="unit" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='RANGE_NUMBER_TO_CONCEPT_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="min" type="xs:float" use="required"/>
            <xs:attribute name="max" type="xs:IDREF" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
            <xs:attribute name="unit" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='RANGE_CONCEPT_TO_NUMBER_TERM'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="min" type="xs:IDREF" use="required"/>
            <xs:attribute name="max" type="xs:float" use="required"/>
            <xs:attribute name="field" type="xs:IDREF"/>
        </xs:complexType>
    </xs:element>

    <xs:element name='SET'>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref='DESCRIPTION' minOccurs="0" maxOccurs="1"/>
                <xs:element ref='META_DATA' minOccurs="0" maxOccurs="1"/>
                <xs:element ref="CATEGORICAL_REF" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="parent_id" type="xs:IDREF" use="optional"/>
            <xs:attribute name="condition_type" type="xs:string" use="optional"/>
            <xs:attribute name="field" type="xs:IDREF"/>
        </xs:complexType>
    </xs:element>
</xs:schema>
```