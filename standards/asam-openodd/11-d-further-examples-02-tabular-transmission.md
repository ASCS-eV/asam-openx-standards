# ASAM Openodd v1.0.0 — D.2 Tabular format file transmission

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_d_further_examples_02_tabular_transmission.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# D.2 Tabular format file transmission

In this section, we present an example illustrating the usage of tabular format for exchanging several ODD relevant artifacts.

Consider an example ODD specification, defined in ISO 34503 [[4](../bibliography.html#bib-iso34503)], shown below:

Table 162. ISO 34503 Table B.1 — Tabular ODD definition using Clauses 8 to 12 in default mode


| Top-level attribute | Sub-attribute | Qualifier | Attribute | Attribute value |
| --- | --- | --- | --- | --- |
| Scenery | Zones | Include | Region | Germany |
| Scenery | Drivable area | Include | Drivable area type | Motorways |
| Scenery | Temporary road structures | Exclude | Temporary road structures | Road works |
| Dynamic elements | Subject vehicle | Include | Maximum speed | 130 km/h |

ISO 34503 provides a straightforward tabular representation aimed at creating a human-readable version of an ODD specification.

While maintaining the benefit of human-readability, our proposed tabular format is more aligned with implementation needs, facilitating the storage, retrieval, and updating of machine-readable ODD specifications and their supplementary artifacts.

In this section, we demonstrate the concept of file transmission(add ref to File Transmission) by presenting a tabular specification of the aforementioned ODD using our proposed schema.
During the exchange of the ODD specification among various stakeholders, two major artifacts need to be shared to ensure semantic interpretation of the ODD. These are:

* Taxonomy Artifact
* ODD Specification

These artifacts, modeled using our proposed tabular format, are shown below.

Table 163. Taxonomy Artifact


| CONCEPT\_ID | PARENT\_ID | TYPE | UNIT\_TYPE | AFFILIATION\_SOURCE | AFFILIATION\_CONCEPT | AFFILIATION\_SOURCE\_NAME\_EN | CONCEPT\_NAME\_EN | DESCRIPTION\_EN | AFFILIATION\_SOURCE\_NAME\_DE | CONCEPT\_NAME\_DE | DESCRIPTION\_DE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scenery |  | record |  | ISO 34503 | Scenery | ISO 34503 | Scenery | Scenery Elements | ISO 34503 | Szenario | Szenario Elemente |
| zones | scenery | record |  | ISO 34503 | Zones | ISO 34503 | Zones | Zones include special road configurations which may differ from typical conditions for driving, or areas with specific driving regulations or environmental conditions. | ISO 34503 | Zonen | Zonen umfassen spezielle Straßenkonfigurationen, die von typischen Fahrbedingungen abweichen können, oder Bereiche mit spezifischen Fahrvorschriften oder Umweltbedingungen. |
| region | zones | categorical |  | ISO 34503 | region | ISO 34503 | Region | Region | ISO 34503 | Region | Region |
| Germany | region | categorical\_literal |  | ISO 34503 | rainfall\_type\_dynamic | ISO 34503 | Germany Region | Applicable traffic norms corresponding to Germany region | ISO 34503 | Deutschland Region | Anwendbare Verkehrsregeln für die Region Deutschland |
| drivable\_area | scenery | record |  | ISO 34503 | drivable\_area | ISO 34503 | Drivable Area | A drivable area refers to the area on which the ADS equipped vehicle may operate. | ISO 34503 | Befahrbarer Bereich | Ein befahrbarer Bereich bezieht sich auf den Bereich, in dem das mit ADS ausgestattete Fahrzeug betrieben werden darf. |
| drivable\_area\_type | drivable\_area | categorical |  | ISO 34503 | drivable\_area\_type | ISO 34503 | Drivable Area Type | Categorical classification of drivable area type | ISO 34503 | Befahrbare Bereich Typ | Kategorische Klassifizierung des befahrbaren Bereichs |
| Motorways | drivable\_area\_type | categorical\_literal |  | ISO 34503 | Motorways | ISO 34503 | Motorways | motorways or highways or interstates | ISO 34503 | Autobahnen | Autobahnen oder Schnellstraßen oder Fernstraßen |
| temporary\_road\_structures | scenery | record |  | ISO 34503 | temporary\_road\_structures | ISO 34503 | Temporary Road Structures | Concepts related to temporary road structures | ISO 34503 | Temporäre Straßenstrukturen | Konzepte im Zusammenhang mit temporären Straßenstrukturen |
| temporary\_road\_structure | temporary\_road\_structures | categorical |  | ISO 34503 | temporary\_road\_structure | ISO 34503 | Temporary Road Structure | Categorical classification of temporary road structures | ISO 34503 | Temporäre Straßenstruktur | Kategorische Klassifizierung von temporären Straßenstrukturen |
| road\_works | temporary\_road\_structure | categorical\_literal |  | ISO 34503 | road\_works | ISO 34503 | Road Works | Road Works | ISO 34503 | Straßenarbeiten | Straßenarbeiten |
| dynamic\_elements |  | record |  | ISO 34503 | dynamic\_elements | ISO 34503 | Dynamic Elements | Movable object or actor in the ODD within the DDT timeframe | ISO 34503 | Dynamische Elemente | Bewegliches Objekt oder Akteur im ODD innerhalb des DDT-Zeitrahmens |
| subject\_vehicle | dynamic\_elements | record |  | ISO 34503 | subject\_vehicle | ISO 34503 | Subject Vehicle | Ego-vehicle under consideration | ISO 34503 | Subjekt Fahrzeug | Betroffenes Fahrzeug |
| maximum\_speed | subject\_vehicle | float | speed | ISO 34503 | maximum\_speed | ISO 34503 | Maximum Speed | Subject vehicle’s maximum allowable speed | ISO 34503 | Höchstgeschwindigkeit | Höchstzulässige Geschwindigkeit des betroffenen Fahrzeugs |

This table provides a snippet of all relevant taxonomy concepts that will be used to create the ODD specification. For file-based exchange, this taxonomy is exported as `iso34503.csv`.

The table below presents an ODD specification corresponding to the aforementioned ISO 34503 example, created using our proposed tabular format. Previously create taxonomy is referenced in row 5. The created ODD specification can now be exported as `iso34503_tab_B_1.csv`, refer Row4.

Table 164. **ODD** Specification - EN


| MODULE\_ID | ROLE | CONTENT or CONDITION |
| --- | --- | --- |
| 001 | handle | odd\_example\_1 |
| 001 | type | odd |
| 001 | export | iso34503\_tab\_B\_1.csv |
| 001 | references | iso34503.csv |
| 001 | title-EN | ODD ISO34503 Example |
| 001 | include\_or | region: Germany |
| 001 | include\_or | drivable\_area\_type:Motorways |
| 001 | exclude\_or | temporary\_road\_structures:road\_works |
| 001 | include\_or | maximum\_speed:130.00 km/h |

The ODD specification can be exported in different languages, if supported by the referenced taxonomy. In our case, since the taxonomy supports the German language, an ODD specification in German is shown below.

Table 165. **ODD** Specification - DE


| MODULE\_ID | ROLE | CONTENT or CONDITION |
| --- | --- | --- |
| 001 | handle | odd\_example\_1 |
| 001 | type | odd |
| 001 | export | iso34503\_tab\_B\_1\_DE.csv |
| 001 | references | iso34503.csv |
| 001 | title-DE | ODD ISO34503 Beispiel |
| 001 | include\_or | region: Germany |
| 001 | include\_or | drivable\_area\_type:Motorways |
| 001 | exclude\_or | temporary\_road\_structures:road\_works |
| 001 | include\_or | maximum\_speed:130.00 km/h |