# ASAM Openodd v1.0.0 — B.1 Tabular format ISO 34503 as CSV

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/11_annexes/11_e_iso34503_01_tabular.html
> **Standard**: ASAM Openodd v1.0.0, 2025-04-03
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# B.1 Tabular format ISO 34503 as CSV

The listing in [Code 214](#code-taxonomy-csv) shows a tabular representation of the taxonomy defined in ISO 34503 [[4](../bibliography.html#bib-iso34503)].

|  |  |
| --- | --- |
|  | [Code 214](#code-taxonomy-csv) can be saved in a CSV file and imported into a spreadsheet application. Ensure that the correct separators are used. In this case the correct separators are commas. |

Code 214. Definition of a taxonomy (comma separated values)

```
CONCEPT_ID,PARENT_ID,TYPE,UNIT_TYPE,AFFILIATION_SOURCE,AFFILIATION_CONCEPT,RANGE_EXPRESSION,AFFILIATION_SOURCE_NAME_EN,CONCEPT_NAME_EN,DESCRIPTION_EN,AFFILIATION_SOURCE_NAME_DE,CONCEPT_NAME_DE,DESCRIPTION_DE
scenery_elements,,record,,ISO 34503,,,ISO 34503,Scenery Elements,Describe the scenery aspects.,ISO 34503,Szenerieelemente,Beschrieb die landschaftlichen Aspekte.
zone,scenery_elements,record,,ISO 34503,,,ISO 34503,Zone,Describe the various applicable zones.,ISO 34503,Zone,Beschreiben Sie die verschiedenen anwendbaren Zonen.
geofenced_areas,zone,record,,ISO 34503,,,ISO 34503,Geofenced Areas,,ISO 34503,Geo Fenced Bereich,
zone_type,zone,record,,ISO 34503,,,ISO 34503,Zonentype,,ISO 34503,Zonentyp,
fixed_zone,zone,categorical,,ISO 34503,,,ISO 34503,Fixed Zone,,ISO 34503,Ortsgebundene Zone,
school_zone,fixed_zone,categoricalLiteral,,ISO 34503,,,ISO 34503,School Zone,,ISO 34503,Schulzone,
environmental_zone,fixed_zone,categoricalLiteral,,ISO 34503,,,ISO 34503,Environmental Zone,,ISO 34503,Umweltzone,
industrial_zone,fixed_zone,categoricalLiteral,,ISO 34503,,,ISO 34503,Industrial Zone,,ISO 34503,Industriegebiet,
parking_lot,fixed_zone,categoricalLiteral,,ISO 34503,,,ISO 34503,Parking Lot,,ISO 34503,Parkplatz,
dynamic_zone,zone,record,,ISO 34503,,,ISO 34503,Dynamic Zone,,ISO 34503,Ortsveränderliche Zone,
interference_zone,zone,record,,ISO 34503,,,ISO 34503,Interference Zone,,ISO 34503,Interferenzzone,
port_zone,zone,record,,ISO 34503,,,ISO 34503,Port Zone,,ISO 34503,Hafenzone,
freight_distribution_centre,zone,record,,ISO 34503,,,ISO 34503,Freight Distribution Center,,ISO 34503,Frachtverteilungszentrum,
region_or_states,scenery_elements,record,,ISO 34503,,,ISO 34503,Region or  States,,ISO 34503,Region oder Bundesland,
drivable_area,scenery_elements,record,,ISO 34503,,,ISO 34503,Drivable Area,,ISO 34503,Befahrbare Fläche,
drivable_area_type,drivable_area,categorical,,ISO 34503,,,ISO 34503,Drivable Area Type,,ISO 34503,Typ der befahrbaren Fläche,
motorways_or_highways_or_interstates,drivable_area_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Motorways or Highways or Interstates,Motorways or highways or interstates are high-traffic roads where non-motorized vehicles and pedestrians are prohibited.,ISO 34503,Autobahnen oder Schnellstraßen,"Autobahnen bzw. Schnellstraßen sind stark befahrene Straßen, auf denen nicht-motorisierte Fahrzeuge und Fußgänger verboten sind."
primary_roads,drivable_area_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Primary Roads,"Dual-carriage ways, single carriage ways.",ISO 34503,Hauptstraßen,Ein- und mehrstreifige Straßen.
radial_roads,drivable_area_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Radial Roads,High density traffic roads which connect the motorways to distributor roads or urban centres.,ISO 34503,Zubringerstraße,"Straßen für hohe Verkehrslast, die Autobahnen mit Zubringerstraßen oder Stadtzentren verbindet."
distributor_roads,drivable_area_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Distributor Roads,Connect radial roads with minor or local roads and generally have low to moderate capacity.,ISO 34503,Verteilerstraßen,"Straßen mit geringer Verkehrslast, die Neben- oder Ortsstraßen verbinden."
minor_or_local_roads,drivable_area_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Minor or Local Roads,,ISO 34503,Neben- oder Ortsstraßen,
slip_roads_or_off_ramps,drivable_area_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Slip Roads or Off Ramps,Used to drive on to and off a motorway or highways or interstates.,ISO 34503,Auf- oder Ausfahrten,Autobahnauf- bzw. -abfahrt.
parking_space,drivable_area_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Parking Space,,ISO 34503,Parkplatz,
shared_space,drivable_area_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Shared Space,May be shared between subject vehicle and other actors.,ISO 34503,Gemeinschaftsstraße,Kann von Fahrzeugen mit anderen Verkehrsteilnehmern gemeinsam genutzt werden.
drivable_area_type_classification,drivable_area,categorical,,ISO 34503,,,ISO 34503,Drivable Area Type Classification,,ISO 34503,Typ der befahrbaren Fläche,
with_active_traffic_management,drivable_area_type_classification,categoricalLiteral,,ISO 34503,,,ISO 34503,With Active Traffic Management,,ISO 34503,Mit aktiver Verkehrssteuerung,
without_active_traffic_management,drivable_area_type_classification,categoricalLiteral,,ISO 34503,,,ISO 34503,Without Active Traffic Management,,ISO 34503,Ohne aktiver Verkehrssteuerung,
drivable_area_geometry,drivable_area,record,,ISO 34503,,,ISO 34503,Drivable Area Geometry,,ISO 34503,Befahrbare Flächengeometrie,
horizontal_plane,drivable_area_geometry,categorical,,ISO 34503,,,ISO 34503,Horizontal Plane,,ISO 34503,Lageplanelement,
straight_lines,horizontal_plane,categoricalLiteral,,ISO 34503,,,ISO 34503,Straight Lines,,ISO 34503,Gerade,
curves,horizontal_plane,categoricalLiteral,,ISO 34503,,,ISO 34503,Curves,,ISO 34503,Kurve,
transverse_plane_plane,drivable_area_geometry,categorical,,ISO 34503,,,ISO 34503,Transverse Plane,,ISO 34503,Querschnittselement,
horizontal_transverse_plane_type,transverse_plane_plane,categorical,,ISO 34503,,,ISO 34503,Horizontal Transverse Plane Type,,ISO 34503,Querschnittselementtyp,
divided,horizontal_transverse_plane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Divided,,ISO 34503,Getrennte Richtungsfahrbahnen,
undivided,horizontal_transverse_plane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Undivided,,ISO 34503,Nicht getrennte Richtungsfahrbahnen,
pavements,horizontal_transverse_plane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Pavements,,ISO 34503,Gehweg,
barriers_on_road_edges,transverse_plane_plane,categoricalLiteral,,ISO 34503,,,ISO 34503,Barriers on Road Edges,,ISO 34503,Fahrbahnbegrenzungen,
types_of_lanes_together,transverse_plane_plane,categoricalLiteral,,ISO 34503,,,ISO 34503,Types_of Lanes Together,,ISO 34503,Überlagerung von Fahrstreifentypen,
superelevation_banking,transverse_plane_plane,categoricalLiteral,,ISO 34503,,,ISO 34503,Superelevation Banking,,ISO 34503,Überhöhung,
longitudinal_plane,drivable_area_geometry,categorical,,ISO 34503,,,ISO 34503,Longitudinal Plane,,ISO 34503,Höhenplanelement,
up_slope,longitudinal_plane,categorical,,ISO 34503,,,ISO 34503,Up Slope,positive gradient,ISO 34503,Steigung,positiver Gradient
down_slope,longitudinal_plane,categorical,,ISO 34503,,,ISO 34503,Down Slope,negative gradient,ISO 34503,Gefälle,negativer Gradient
level_plane,longitudinal_plane,categorical,,ISO 34503,,,ISO 34503,Level Plane,,ISO 34503,Ebene,
drivable_area_lane_specification,drivable_area,categorical,,ISO 34503,,,ISO 34503,Drivable Area Lane Specification,,ISO 34503,Fahrstreifencharakteristik,
lane_dimensions,drivable_area_lane_specification,categorical,,ISO 34503,,,ISO 34503,Lane Dimensions,,ISO 34503,Fahrstreifendimension,
lane_marking,drivable_area_lane_specification,categorical,,ISO 34503,,,ISO 34503,Lane Marking,,ISO 34503,Fahrstreifenmarkierung,
clear_lane_marking,lane_marking,categoricalLiteral,,ISO 34503,,,ISO 34503,Clear Lane Marking,,ISO 34503,deutliche Fahrstreifenmarkierung,
blurred_lane_marking,lane_marking,categoricalLiteral,,ISO 34503,,,ISO 34503,Blurred Lane Marking,,ISO 34503,verschwommene Fahrstreifenmarkierung,
no_lane_marking,lane_marking,categoricalLiteral,,ISO 34503,,,ISO 34503,No Lane Marking,,ISO 34503,keine Fahrstreifenmarkierung,
temporary_lane_marking,lane_marking,categoricalLiteral,,ISO 34503,,,ISO 34503,Temporary Lane Marking,,ISO 34503,temporäre Fahrstreifenmarkierung,
lane_type,drivable_area_lane_specification,categorical,,ISO 34503,,,ISO 34503,Lane Type,,ISO 34503,Fahrstreifentyp,
bus_lane,lane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Bus Lane,,ISO 34503,Busfahrstreifen,
traffic_lane,lane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Traffic Lane,,ISO 34503,Verkehrsfahrstreifen,
cycle_lane,lane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Cycle Lane,,ISO 34503,Fahrradfahrstreifen,
tram_lane,lane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Tram Lane,,ISO 34503,Straßenbahnfahrstreifen,
emergency_lane,lane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Emergency Lane,,ISO 34503,Notfallfahrstreifen,
shared_lane,lane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Shared Lane,,ISO 34503,gemeinsam genutzter Fahrstreifen,
other_special_purpose_lanes,lane_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Other Special Purpose Lanes,,ISO 34503,Spezialfallfahrstreifen,
direction_of_travel,drivable_area_lane_specification,categorical,,ISO 34503,,,ISO 34503,Direction of Travel,,ISO 34503,Fahrtrichtung,
right_hand_travel,direction_of_travel,categoricalLiteral,,ISO 34503,,,ISO 34503,Right Hand Travel,,ISO 34503,Rechtsverkehr,
left_hand_travel,direction_of_travel,categoricalLiteral,,ISO 34503,,,ISO 34503,Left Hand Travel,,ISO 34503,Linksverkehr,
speed_limit,drivable_area,float,velocity,ISO 34503,,,ISO 34503,Speed Limit,,ISO 34503,Geschwindigkeitsbeschränkung,
drivable_area_signs,drivable_area,categorical,,ISO 34503,,,ISO 34503,Drivable Area Signs,,ISO 34503,Verkehrsschilder,
sign_types,drivable_area_signs,categorical,,ISO 34503,,,ISO 34503,Sign Types,,ISO 34503,Verkehrsschildart,
regulatory_signs,sign_types,categoricalLiteral,,ISO 34503,,,ISO 34503,Regulatory Signs,e.g. traffic lights,ISO 34503,Vorschriftszeichen,
warning_signs,sign_types,categoricalLiteral,,ISO 34503,,,ISO 34503,Warning Signs,,ISO 34503,Gefahrzeichen,
information_signs,sign_types,categoricalLiteral,,ISO 34503,,,ISO 34503,Information Signs,,ISO 34503,Verkehrsrichtzeichen,
sign_features,drivable_area_signs,categorical,,ISO 34503,,,ISO 34503,Sign Features,,ISO 34503,Verkehrsschilcharakteristik,
movable_signs,sign_features,categoricalLiteral,,ISO 34503,,,ISO 34503,Movable Signs,,ISO 34503,Ortsveränderliche Verkehrsschilder,
fixed_signs,sign_features,categoricalLiteral,,ISO 34503,,,ISO 34503,Fixed Signs,,ISO 34503,Orstfeste Verkehrsschilder,
drivable_area_edge,drivable_area,categorical,,ISO 34503,,,ISO 34503,Drivable Area Edge,,ISO 34503,Fahrbahnrand,
line_markers,drivable_area_edge,categoricalLiteral,,ISO 34503,,,ISO 34503,Line Markers,,ISO 34503,Randline,
snowbanks,drivable_area_edge,categoricalLiteral,,ISO 34503,,,ISO 34503,Snowbanks,,ISO 34503,Schneewall,
solid_barriers,drivable_area_edge,categoricalLiteral,,ISO 34503,,,ISO 34503,Solid Barriers,"e.g. grating, rails, curb, cones",ISO 34503,Fahrbahnrandbarriere,"Gitter, Geländer, Bordstein, Kegel"
temporary_line_marker,drivable_area_edge,categoricalLiteral,,ISO 34503,,,ISO 34503,Temporary Line Marker,,ISO 34503,temporäre Fahrbahnmarkierung,
none,drivable_area_edge,categoricalLiteral,,ISO 34503,,,ISO 34503,None,,ISO 34503,keine Fahrbahnmarkierung,
drivable_area_shoulder,drivable_area,categorical,,ISO 34503,,,ISO 34503,Drivable Area Shoulder,,ISO 34503,Bankett,
paved_or_gravel,drivable_area_shoulder,categoricalLiteral,,ISO 34503,,,ISO 34503,Paved or Gravel,,ISO 34503,befestigt oder geschottert,
grass,drivable_area_shoulder,categoricalLiteral,,ISO 34503,,,ISO 34503,Grass,,ISO 34503,Rasen,
drivable_area_surface,drivable_area,categorical,,ISO 34503,,,ISO 34503,Drivable Area Surface,,ISO 34503,Oberfläche,
drivable_area_surface_type,drivable_area_surface,categorical,,ISO 34503,,,ISO 34503,Drivable Area Surface Type,,ISO 34503,Oberflächenart,
asphalt,drivable_area_surface_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Asphalt,,ISO 34503,Asphalt,
cement_concrete,drivable_area_surface_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Cement Concrete,,ISO 34503,Beton,
pavers,drivable_area_surface_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Pavers,,ISO 34503,Kleinpflaster,
cobblestone,drivable_area_surface_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Cobblestone,,ISO 34503,Kopfsteinpflaster,
granite_setts,drivable_area_surface_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Granite Setts,,ISO 34503,Kleinpflaster,
gravel,drivable_area_surface_type,categoricalLiteral,,ISO 34503,,,ISO 34503,Gravel,,ISO 34503,Schotter,
drivable_area_surface_features,drivable_area_surface,categorical,,ISO 34503,,,ISO 34503,Drivable Area Surface Features,,ISO 34503,Oberflächencharakteristik,
damages,drivable_area_surface_features,categorical,,ISO 34503,,,ISO 34503,Damages,,ISO 34503,Oberflächenbeschädigung,
cracks,damages,categoricalLiteral,,ISO 34503,,,ISO 34503,Cracks,,ISO 34503,Gerissener Belag,
potholes,damages,categoricalLiteral,,ISO 34503,,,ISO 34503,Potholes,,ISO 34503,Schlaglöcher,
ruts,damages,categoricalLiteral,,ISO 34503,,,ISO 34503,Ruts,,ISO 34503,Spurrillen,
swells,damages,categoricalLiteral,,ISO 34503,,,ISO 34503,Swells,,ISO 34503,Welliger_Belag,
artifical_features,drivable_area_surface_features,categorical,,ISO 34503,,,ISO 34503,Artifical Features,,ISO 34503,Oberflächeninfrastruktur,
speed_bumps,artifical_features,categoricalLiteral,,ISO 34503,,,ISO 34503,Speed Bumps,,ISO 34503,Bremsschwelle,
intentional_speed_reduction_obstacles,artifical_features,categoricalLiteral,,ISO 34503,,,ISO 34503,Intentional Speed Reduction Obstacles,,ISO 34503,Verkehrsberuhigungselemente,
drivable_area_included_surface_condition,drivable_area_surface,categorical,,ISO 34503,,,ISO 34503,Drivable Area Included Surface Condition,,ISO 34503,Oberflächenzustand,
icy,drivable_area_included_surface_condition,categoricalLiteral,,ISO 34503,,,ISO 34503,Icy,,ISO 34503,Eisschicht,
flooded,drivable_area_included_surface_condition,categoricalLiteral,,ISO 34503,,,ISO 34503,Flooded,,ISO 34503,überflutet,
standing_water,drivable_area_included_surface_condition,categoricalLiteral,,ISO 34503,,,ISO 34503,Standing Water,,ISO 34503,Stehendes_Wasser,
snow_on_surface,drivable_area_included_surface_condition,categoricalLiteral,,ISO 34503,,,ISO 34503,Snow on Surface,,ISO 34503,Schneebedeckte_Oberfläche,
wet,drivable_area_included_surface_condition,categoricalLiteral,,ISO 34503,,,ISO 34503,Wet,,ISO 34503,Nasse_Straßenoberfläche,
surface_contamination,drivable_area_included_surface_condition,categoricalLiteral,,ISO 34503,,,ISO 34503,Surface Contamination,,ISO 34503,Oberflächenkontamination,
junctions,scenery_elements,categorical,,ISO 34503,,,ISO 34503,Junctions,,ISO 34503,Knotenpunkte,
roundabout_diameter,junctions,float,length,ISO 34503,,,ISO 34503,Roundabout Diameter,inscribed circle diameter,ISO 34503,Kreisverkehraußendurchmesser,Beschreibt den Kreisverkehrdurchmesser
roundabout,junctions,categorical,,ISO 34503,,,ISO 34503,Roundabout,,ISO 34503,Kreisverkehr,
mini,roundabout,categoricalLiteral,,ISO 34503,,roundabout_diameter: < 28 m,ISO 34503,Mini,Less than 28m inscribed circle diameter,ISO 34503,Minikreisverkehr,Kreisverkehr mit weniger als 28m Durchmesser.
compact,roundabout,categoricalLiteral,,ISO 34503,,roundabout_diameter: [28 .. 36] m,ISO 34503,Compact,With a central island of at least 4m diameter and inscribed circle diameter between 28m and 36m.,ISO 34503,Kompakter_Kreisverkehr,Kreisverkehr mit einem Durchmesser zwischen 28 und 36m und einer Mittelinsel mit mindestens 4m Durchmesser.
normal,roundabout,categoricalLiteral,,ISO 34503,,roundabout_diameter: [36 .. 100] m,ISO 34503,Normal,With a central island of at least 4m diameter and inscribed circle diameter between 36 and 100m.,ISO 34503,Normaler_Kreisverkehr,Kreisverkehr mit einem Durchmesser zwischen 36 und 100m und einer Mittelinsel mit mindestens 4m durchmesser.
large,roundabout,categoricalLiteral,,ISO 34503,,roundabout_diameter: > 100 m,ISO 34503,Large,Greater than 100m inscribed circle diameter.,ISO 34503,Großer_Kreisverkehr,Kreisverkehr mit mehr als 100m durchmesser.
double_roundabout,roundabout,Boolean,,ISO 34503,,,ISO 34503,Double Roundabout,Two roundabouts which are separated by a short link.,,Doppelter_Kreisverkehr,"Zwei Kreisverkehre, die durch eine kurze Verbindung verbunden sind."
roundabout_classification,roundabout,categorical,,ISO 34503,,,ISO 34503,Roundabout Classification,,ISO 34503,Kreisverkehrarten,
signalized_roundaboud,roundabout,categoricalLiteral,,ISO 34503,,,ISO 34503,Signalized Roundaboud,,ISO 34503,Kreisverkehr mit Lichtsignalanlage,
non_signalised_roundabout_with_yielding_traffic,roundabout,categoricalLiteral,,ISO 34503,,,ISO 34503,Non Signalized Roundaboud with Yielding Traffic,,ISO 34503,Vorfahrtsbeschilderter Kreisverkehr ohne Lichtsignalanlage,
non_signalised_roundabout_without_yielding_traffic,roundabout,categoricalLiteral,,ISO 34503,,,ISO 34503,Non Signalized Roundaboud without Yielding Traffic,,ISO 34503,Kreisverkehr ohne Lichtsignalanlage und ohne Vorfahrtsbeschilderung,
intersection,junctions,categorical,,ISO 34503,,,ISO 34503,Intersection,,ISO 34503,Kreuzung,
t_junction,intersection,categoricalLiteral,,ISO 34503,,,ISO 34503,T-Junction,,ISO 34503,T-Kreuzung,
y_junction,intersection,categoricalLiteral,,ISO 34503,,,ISO 34503,Y-Junction,,ISO 34503,Y-Kreuzung,
cross_road,intersection,categoricalLiteral,,ISO 34503,,,ISO 34503,Cross Road,,ISO 34503,orthogonale Kreuzung,
staggered,intersection,categoricalLiteral,,ISO 34503,,,ISO 34503,Staggered,,ISO 34503,Versetzte Kreuzungsarme,
grade_separated,intersection,categoricalLiteral,,ISO 34503,,,ISO 34503,Grade Separated,,ISO 34503,Niveauentkoppelte Kreuzung,
intersection_classification,junctions,categorical,,ISO 34503,,,ISO 34503,Intersection Classification,,ISO 34503,Kreuzungsarten,
signalized_intersection,intersection_classification,categoricalLiteral,,ISO 34503,,,ISO 34503,Signalized Intersection,,ISO 34503,Kreuzung mit Lichtsignalanlage,
non_signalized_intersection,intersection_classification,categoricalLiteral,,ISO 34503,,,ISO 34503,Non Signalized Intersection,,ISO 34503,Kreuzungsarme ohne Lichtsignalanlage,
```