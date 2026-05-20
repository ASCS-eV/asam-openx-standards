# ASAM OpenDRIVE® v1.9.0 — Annex E: Categories for signal semantics (informative)

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/signal_semantics_categories/top_signal_semantics_categories.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex E: Categories for signal semantics (informative)

This chapter explains the use of signal semantics `<vehicle>` for signs as specified in  [Section 14.8, "Signal semantics"](../../14_signals/14_08_signal_semantics.html#top-ac3b27c3-c3ac-49cf-bdaf-c52177f1dcee).
Examples are provided for use in combination with either `<prohibited>`, `<supplementaryAllows>`, or `<supplementaryProhibits>`.

Table 214. Vehicle Categories


| @type | Description | Example for `<prohibited>` | Example for `<supplementaryAllows>` | Example for `<supplementaryProhibits>` |
| --- | --- | --- | --- | --- |
| car | A car is a motorized vehicle designed primarily for passenger transportation. A car typically has four wheels. | Cars prohibited | Except cars | For cars |
| van | A van is a motorized vehicle with a larger cargo area than a car, used for transporting goods or people. This category is not intended for mini vans, which shall rather be categorized as cars. |  |  |  |
| bus | A bus is a motorized vehicle designed to carry multiple passengers. | Buses prohibited | Except busses | For busses |
| heavyTruck | A heavy truck is a large commercial vehicle designed for transporting heavy loads. The cargo area is rigidly fixed to the vehicle itself. | Heavy trucks prohibited | Except heavy trucks | For heavy trucks |
| trailer | A trailer is a non-motorized vehicle designed for being towed by a motorized vehicle to carry goods, animals, or people. | Trailers prohibited | Except trailers | For trailers |
| semiTractor | A semi-tractor is a vehicle designed for towing semi-trailers for the transportation of heavy loads. |  |  | For semi tractors |
| semiTrailer | A semi-trailer is a vehicle designed for being towed by a semi-tractor. Characteristics compared to a regular trailer are the large size, the fact that a large portion of the weight is supported at the hitch, and a large overlap with the towing vehicle, i.e. the semi-tractor. | No Semi-Trailers |  |  |
| motorcycle | A motorcycle is a motorized vehicle designed primarily for passenger transportation. Compared to a car, fewer passive safety features, such as a full passenger cell, are typically present. This category includes both two-wheeled motorcycles and three-wheeled vehicles like motorcycles with side-cars or trikes. | Motorcycles prohibited | Except motorcycles | For motorcycles |
| bicycle | A bicycle is a human-powered or motor-assisted, pedal-driven vehicle. This category includes typical two-wheeled bicycles as well as cargo-bikes and other pedal-driven vehicles with more than two wheels. | Bicycles prohibited | Except bicycles | For bicycles |
| standupScooter | A stand-up scooter is a compact, typically two-wheeled device. It is operated with the rider standing on a deck between the wheels. It may be propelled by a motor or the rider making a kicking movement. | Standup scooter prohibited | Except standup scooter | For standup scooter |
| microMobility device | A micro-mobility device is a small, lightweight vehicle for short-distance travel, like hoverboards or roller skates. While bicycles, stand-up scooters, and wheelchairs may technically fall into this category, the respective detailed categories shall be used instead. |  | Except micro-mobility devices | For wheelchairs |
| workMachine | A work machine is a vehicle designed for specific tasks (e.g., construction equipment, agricultural tractors, forklifts). | Work machines prohibited | Except work machines | For work machines |
| train | A train is a vehicle designed for the transport of passengers and freight on rail infrastructure. The rail infrastructure for trains is mostly grade-separated from the public road infrastructure as trains have exclusive right-of-way. Therefore, in case crossings with the road infrastructure occur, the exclusive right-of-way is ensured, e.g. by railway barriers. A train often acts as a series of connected vehicles. |  | Except trains | For trains |
| tram | A tram is a vehicle designed for using rail infrastructure for the transport of passengers on rail infrastructure. The rail infrastructure may fully or partially overlap with public road infrastructure. In contrast to trains, trams do not have exclusive right-of-way. A tram often acts as a series of connected vehicles. |  | Except trams | For trams |
| landVehicle | A land vehicle is a vehicle designed for travel on land. This category is deliberately generic to include land vehicles that do not fall into other categories and may be refined in future versions as needed. |  |  |  |
| other | All other vehicle types that do not fit into current categories. |  |  |  |