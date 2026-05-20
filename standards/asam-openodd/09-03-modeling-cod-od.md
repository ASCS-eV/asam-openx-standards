# ASAM Openodd v1.0.0 — 9.3 Modeling COD/OD

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/09_openscenario_dsl/09_03_modeling_cod_od.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 9.3 Modeling COD/OD

## 9.3.1 General information

A Current Operational Domain (COD) represents the specific operating conditions which exist at a specific moment (presently) in the immediate vicinity of an ADS.
It is a model that is based on a domain concepts definition model (taxonomy), and it assigns concrete values to all or some of the fields (attributes) in that domain concepts definition model (taxonomy).

An Operational Domain (OD) represents a set of operating conditions, possibly for a specific geographical region and/or a specific period of time.
Similarly to a COD, the OD is a model that is based on a domain concepts definition model (taxonomy), and it assigns concrete values to all or some of the fields (attributes) in that domain concepts definition model (taxonomy).

It may be that the domain concepts definition model (taxonomy) for the OD is different from the one used for the COD (or ODD), possibly extending it with additional attributes.
For example, where a domain concepts definition model (taxonomy) used for a COD and ODD may contain an attribute `wind_speed` to represent the current speed of the wind as perceived by an ADS, the domain concepts definition model (taxonomy) used by the OD may contain additional fields (attributes), like the average wind speed, upper and lower bounds of wind speeds, or the probability and average duration of storm.

## 9.3.2 Modeling COD

The COD specifies concrete values for the attributes in a given domain concepts definition model (taxonomy).
In a V&V process based on ASAM OpenSCENARIO DSL, a COD will exist primarily in the memory of a supporting execution engine as illustrated in [Figure 22](09_01_overview.html#fig-overview-type-and-instance-models-in-a-scenario-based-v-v-process).

However, a COD can also be represented using the ASAM OpenSCENARIO DSL language.
To do this, an ASAM OpenSCENARIO DSL file imports a given domain concepts definition model (taxonomy) and defines values for the fields (attributes ) via type extensions and keep statements of the form `<field-name> == value`.

[Code 119](#code-concrete-values) shows an example of how a COD is modeled using ASAM OpenSCENARIO DSL.
The example shows concrete values that are assigned to fields of a `weather` `TaxonomyConcept` instance (represented as a struct in the domain concepts definition model).
The code assumes that the domain concepts definition model (taxonomy) defines the fields `wind_speed`, `wind`, and `rainfall` for `weather`.
Also, the example shows how concrete time and location information (see [Code 110](09_02_modeling_taxonomy.html#code-modeling-odd-taxonomy)) is encoded.

Code 119. Example concrete values (ASAM OpenSCENARIO DSL notation)

```
# Import existing domain concepts definition (taxonomy) file
import "Domain_Concepts_Definition_ISO_34503.osc"

unit m of distance is SI(m: 1, factor: 1.0)
unit mps of speed is SI(m: 1, s: -1, factor: 1.0)

unit s of time is SI(s: 1)  # Seconds
unit ms of time is SI(s: 1, factor: 0.001)  # Milliseconds
unit min of time is SI(s: 1, factor: 60)  # Minutes
unit h of time is SI(s: 1, factor: 3600)  # Hours

unit deg of angle is SI (rad: 1, factor: 0.01745329251) # pi/180

# "2024-06-01 08:12:53.784"
extend date_time:
    keep (year == 2024)
    keep (month == 6)
    keep (day == 1)
    keep (hour == 8 h)
    keep (minute == 12 min)
    keep (second == 53 s)
    keep (millisecond == 784 ms)


extend geo_location_3D:
    keep (latitude = 48.0232 deg)
    keep (longitude = 11.7153 deg)
    keep (altitude = 126.3 m)


extend weather:
    keep(wind_speed == 26.522 mps)
    keep(wind == storm)
    keep(rainfall == heavy_rain)
```

## 9.3.3 Modeling OD

ODs are modeled using the same approach as described for CODs.
The code example [Code 120](#code-modeling-ods-asam-openscenario-dsl) shows part ASAM OpenSCENARIO DSL file representing an OD.
The example assumes that all the fields (attributes) and units appearing in the `keep`-constraints are defined in the imported domain concepts definition model (taxonomy) `Domain_Concepts_Definition_ISO_34503_extended_for_OD.osc`.

Code 120. Example modeling ODs in ASAM OpenSCENARIO DSL (ASAM OpenSCENARIO DSL notation)

```
# Import existing domain concepts definition (taxonomy) file
import "Domain_Concepts_Definition_ISO_34503_extended_for_OD.osc"

extend weather:
    keep(average_wind_speed == 8.0mps)
    keep(wind_speed_lower_bound == 0.0mps)
    keep(wind_speed_upper_bound == 105.0mps)
    keep(probability_of_storms_per_day == 0.085)
    keep(mean_storm_duration == 1.75hour)
    ...

extend drivable_area:
    keep(average_road_width == 4.3m)
    keep(minimum_road_width == 2.4m)
    keep(maximum_road_width == 8.2m)
    keep(percentage_two_lane_roads == 20)
    ...
```