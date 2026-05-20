# ASAM Openodd v1.0.0 — 8.1 Overview

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/08_tabular/08_01_openodd_schema_intro.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.1 Overview

## 8.1.1 Introduction

This mapping reference consists of [Section 8.1, "Overview"](08_01_openodd_schema_intro.html),  [Section 8.2, "Taxonomy mapping"](08_02_openodd_tabular_taxonomy.html#top-tabular-taxonomy),  [Section 8.3, "COD/OD mapping"](08_03_openodd_tabular_od.html#top-tabular-codod),  [Section 8.4, "ODD module mapping"](08_04_openodd_tabular_modules.html#top-tabular-modules), and the annexes  [Annex D.1, *Tabular format SQL*](../11_annexes/11_d_further_examples_01_tabular_sql.html#top-annexes-further-examples-SQL),  [Annex D.2, *Tabular format file transmission*](../11_annexes/11_d_further_examples_02_tabular_transmission.html#top-annex-file-transmission-example),  [Annex B.1, *Tabular format ISO 34503 as CSV*](../11_annexes/11_e_iso34503_01_tabular.html#top-example-iso34503-database), and  [Annex D.3, *Tabular Format weather COD*](../11_annexes/11_d_further_examples_03_weather_cod.html#top-weather-cod-example).

This mapping reference describes how ASAM OpenODD concepts and structures can be represented in a tabular format such as CSV files, spreadsheets, or suitable tabular formats.
It provides guidance on mapping elements of the ASAM OpenODD model to flat tables to facilitate data representation, storage, and processing in tabular environments.

## 8.1.2 Purpose

The purpose of ASAM OpenODD model to tabular format mapping reference is to support the instantiation of the ASAM OpenODD model, which is hereafter referred as ASAM OpenODD model, along with its storage and retrieval.
The mapping reference tabular format provides a tabular representation data schema to address the following use cases:

* Ability to store a taxonomy in different languages and maintain traceability between various concepts
* Support of import or export of multiple taxonomies
* Ability to instantiate ODD in a modular way with templates that can then be further extended, updated, or refined with ODD conditions
* Provide selective export of ODD and relevant taxonomy concepts
* Ability to include or reference several data sources for modeling CODs

The environmental data contains spatio-temporal data concerning prevalent operating conditions as measured by AV or suitable instrumentations stack, for example weather service provider.
The proposed tabular format has to capture large amounts of measurement data and is an area where the proposed schema contributes the most.

## 8.1.3 Files requirement for exchange

### 8.1.3.1 Use cases

To ensure that every exchange is complete, it is critical to satisfy the requirements that are specified in [Section 6.1.4, "Exchange requirements"](../06_model_concept/06_01_openodd_model.html#sec-model-concept-exchange-requirements).

When transmitting COD or OD, a manifest file can be attached optionally, in which the list of files, their names and roles are specified.
When a manifest file is used, the COD or OD column headers do not need to match their taxonomy because they are mapped by the manifest file.
See [Section 8.3.4, "Use of manifest file"](08_03_openodd_tabular_od.html#sec-manifest-usage) for details about content and format.

The files can be exchanged with or without an archive format.
It is particularly recommended to pack all files as a single zip file, with or without a manifest.

### 8.1.3.2 Export requirements

When exporting ASAM OpenODD, the export is expected to include the taxonomy concepts required to support the subject:

When exporting taxonomy only, then only taxonomy content is needed.
The export can contain a single file or several files that are linked by the keyword `IMPORT`.

* If only conditions (=modules) are exported, the taxonomy file shall be attached to the export files (archive file).
  Please note that, unlike the XML and YAML formats, the taxonomy and the modules cannot be specified in a single table file since both use different tabular specifications.
* When COD or OD are exported, the taxonomy file shall also be exported.
  The tabular representation also supports the inclusion of an optional manifest which is used to map the columns of the data table to taxonomy concepts instead of using the column headers.
* When both conditions (=modules) and OD or COD are exported, then the taxonomy export is also required.

## 8.1.4 Storage Mechanisms

A tabular representation of the ASAM OpenODD model serves two purposes:

1. It is readable by humans, for example csv or spreadsheets.
2. It can be stored in a database, for example SQL.

Therefore, the proposed tabular format shall be compatible with any storage mechanism that supports tabular representation of its content.

A few supported data formats are the following:

* CSV files:
  Comma-separated values (CSV) is a widely known text file format that uses commas to separate values and newlines to separate records.
* Parquet files:
  A parquet file is a columnar file format that is designed for efficient storage and retrieval of large datasets, especially within big data ecosystems, for example Hadoop.
  It uses its binary data types to speed up processing.
  Although using strings is required to support the more graphical nature of the tabular representation, it is advisable to use the native numeric types for data heavy files, especially for COD use cases.
* JSON Lines:
  JSON Lines is a convenient format for storing structured data that may be processed one record at a time.
  It works well with unix-style text processing tools and shell pipelines.
  It is a great format for log files and a flexible format for passing messages between cooperating processes.