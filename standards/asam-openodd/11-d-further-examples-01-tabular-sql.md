# ASAM Openodd v1.0.0 — D.1 Tabular format SQL

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_d_further_examples_01_tabular_sql.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# D.1 Tabular format SQL

The concept of a `Record` is assumed to be contained within an external data source and will be referred through external tables from within our database schema.
See the description for Microsoft SQL Server [[17](../bibliography.html#bib-external-tables)] for details on external tables.
By employing this technique, the task of creating tables pertaining to `Taxonomy Concept Values` is delegated to the responsible database engineer.

Code 231. Syntax for Integrating OD data

```
-- Syntax for creating external tables
CREATE EXTERNAL TABLE { database_name.schema_name.table_name | schema_name.table_name | table_name }
    ( <column_definition> [ ,...n ] )
    WITH (
        LOCATION = 'folder_or_filepath',
        DATA_SOURCE = external_data_source_name,
        [ FILE_FORMAT = external_file_format_name ]
        [ , <reject_options> [ ,...n ] ]
    )
[;]

<reject_options> ::=
{
    | REJECT_TYPE = value | percentage
    | REJECT_VALUE = reject_value
    | REJECT_SAMPLE_VALUE = reject_sample_value,
    | REJECTED_ROW_LOCATION = '/REJECT_Directory'
}

<column_definition> ::=
column_name <data_type>
    [ COLLATE collation_name ]
    [ NULL | NOT NULL ]
```

For instance, consider the following exemplary pseudo-code based on aforementioned syntax:

```
CREATE EXTERNAL TABLE weather_data (
  date DATE NOT NULL,
  time DATETIME NOT NULL,
  temperature DOUBLE,
  precipitation FLOAT,
  visibility INT
  PRIMARY KEY (date, time)
)
WITH (LOCATION = 'weather_data.parquet', DATA_SOURCE = 'weather_data.parquet', FILE_FORMAT = 'parquet') AS weather_source
[reject_type VARCHAR(10) DEFAULT 'unknown',
 reject_value FLOAT DEFAULT 0.0]
AS weather_data;
```

|  |  |
| --- | --- |
|  | External tables generally do not support primary key constraints because they are often used for read-only purposes and the data is managed externally. If you need to enforce primary key constraints, you would typically need to import the data into a managed table within your database system. |

In this example, a new external table named weather\_data is created during Schema Implementation using the aforementioned SQL External Table syntax. The table is defined with the following columns:

* date: Date, primary key.
* time: Time of day (for example 08:00 AM), not null.
* temperature: Double, representing temperature in degrees Celsius.
* precipitation: Float, representing precipitation in millimeters.
* visibility: Integer, representing visibility in meters.

The data source for the weather\_data table is specified as the file `weather_data.parquet` located in the folder *weather\_data*. The *LOCATION* option specifies the location of the external data source on the local filesystem.