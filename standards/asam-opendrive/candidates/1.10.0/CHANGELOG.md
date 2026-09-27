# OpenDRIVE 1.10 candidate

Based on ASAM OpenDRIVE V1.9.0, the model in `standards/asam-opendrive/uml/opendrive.scxml`. This file is generated from `changes.json` by `scripts/candidate_model.py`; edit that file instead.

The OpenDRIVE V1.9.0 model with the changes below. Each makes the model say, in terms a UML reader understands, what the normative schema says, or corrects a defect the model and the schema share. Changes marked *unchanged* leave the normative schema exactly as it is; the others change it, and say how.

## ODR-1: An attribute's multiplicity says what its use says

The schema makes an XSDattribute required exactly when its `use` tag is `required`, and optional otherwise; the attribute's UML multiplicity plays no part. For these attributes the two disagree, so a UML reader of the model, such as the OWL target, requires what the schema makes optional, or the reverse. The multiplicity is set to what `use` says.

**Normative schema:** unchanged: the derivation reads `use`, not the multiplicity

- multiplicity of t_junction_connection_virtual_default.connectingRoad (attribute 18) := 0..1
- multiplicity of t_junction_roadSection.id (attribute 19) := 0..1
- multiplicity of t_road_link_predecessorSuccessor.elementType (attribute 31) := 0..1
- multiplicity of t_road_type_speed.unit (attribute 60) := 0..1
- multiplicity of t_junction_roadSection.roadId (attribute 64) := 0..1
- multiplicity of t_road_objects_object_surface_CRG.file (attribute 70) := 0..1
- multiplicity of t_road_objects_object_surface_CRG.hideRoadSurfaceCRG (attribute 71) := 0..1
- multiplicity of t_road_objects_object_surface_CRG.zScale (attribute 72) := 0..1
- multiplicity of t_junction_roadSection.sStart (attribute 73) := 0..1
- multiplicity of t_license.name (attribute 106) := 0..1
- multiplicity of t_junction_roadSection.sEnd (attribute 109) := 0..1
- multiplicity of t_junction_direct.type (attribute 126) := 0..1
- multiplicity of t_junction_connection_virtual.connectingRoad (attribute 128) := 0..1
- multiplicity of t_junction_virtual.type (attribute 130) := 0..1
- multiplicity of t_junction_virtual.mainRoad (attribute 131) := 0..1
- multiplicity of t_junction_virtual.sStart (attribute 132) := 0..1
- multiplicity of t_junction_virtual.sEnd (attribute 133) := 0..1
- multiplicity of t_junction_virtual.orientation (attribute 134) := 0..1
- multiplicity of t_junction_connection_direct.linkedRoad (attribute 135) := 0..1
- multiplicity of t_junction_crossing.type (attribute 136) := 0..1
- multiplicity of t_junction_connection_common.connectingRoad (attribute 144) := 0..1
- multiplicity of t_junction_crossPath.crossingRoad (attribute 145) := 0..1
- multiplicity of t_junction_boundary_segment_lane.boundaryLane (attribute 146) := 0..1
- multiplicity of t_junction_crossPath.id (attribute 163) := 0..1
- multiplicity of t_junction_crossPath.roadAtEnd (attribute 164) := 0..1
- multiplicity of t_junction_crossPath.roadAtStart (attribute 183) := 0..1
- multiplicity of t_junction_crossPath_laneLink.s (attribute 192) := 0..1
- multiplicity of t_junction_crossPath_laneLink.from (attribute 198) := 0..1
- multiplicity of t_junction_crossPath_laneLink.to (attribute 199) := 0..1
- multiplicity of t_road_signals_board_sign.v (attribute 218) := 0..1
- multiplicity of t_road_signals_board_sign.z (attribute 219) := 0..1
- multiplicity of t_road_signals_displayArea.height (attribute 228) := 0..1
- multiplicity of t_road_objects_object_repeat.heightStart (attribute 234) := 1..1
- multiplicity of t_road_objects_object_repeat.heightEnd (attribute 235) := 1..1
- multiplicity of t_road_signals_displayArea.index (attribute 244) := 0..1
- multiplicity of t_road_signals_signal_road.s (attribute 245) := 0..1
- multiplicity of t_road_signals_signal_road.t (attribute 246) := 0..1
- multiplicity of t_road_signals_displayArea.width (attribute 282) := 0..1
- multiplicity of t_road_signals_displayArea.v (attribute 290) := 0..1
- multiplicity of t_road_signals_displayArea.z (attribute 291) := 0..1
- multiplicity of t_junction_elevationGrid.sStart (attribute 316) := 0..1
- multiplicity of t_junction_elevationGrid.gridSpacing (attribute 317) := 0..1
- multiplicity of t_junction_elevationGrid_elevation.center (attribute 378) := 0..1
- multiplicity of t_junction_boundary_segment.roadId (attribute 398) := 0..1
- multiplicity of t_road_objects_object_skeleton_polyline_vertexRoad.dz (attribute 408) := 0..1
- multiplicity of t_junction_predecessorSuccessor.elementDir (attribute 420) := 0..1
- multiplicity of t_junction_boundary_segment_lane.type (attribute 432) := 0..1
- multiplicity of t_junction_boundary_segment_joint.type (attribute 434) := 0..1
- multiplicity of t_junction_boundary_segment_lane.sStart (attribute 435) := 0..1
- multiplicity of t_junction_boundary_segment_lane.sEnd (attribute 436) := 0..1
- multiplicity of t_junction_boundary_segment_joint.contactPoint (attribute 481) := 0..1
- multiplicity of t_road_objects_object_skeleton_polyline_vertexRoad.s (attribute 619) := 0..1
- multiplicity of t_road_objects_object_skeleton_polyline_vertexRoad.t (attribute 620) := 0..1
- multiplicity of t_road_objects_object_skeleton_polyline_vertexLocal.z (attribute 622) := 0..1
- multiplicity of t_road_signals_vmsBoard.displayType (attribute 623) := 0..1
- multiplicity of t_road_objects_object_skeleton_polyline_vertexLocal.u (attribute 636) := 0..1
- multiplicity of t_road_objects_object_skeleton_polyline_vertexLocal.v (attribute 637) := 0..1
- multiplicity of t_road_lateralProfile_crossSectionSurface_strip.id (attribute 642) := 0..1
- multiplicity of t_signalGroup_vmsGroup.id (attribute 646) := 0..1
- multiplicity of t_signalGroup_vmsBoardReference.signalId (attribute 647) := 0..1
- multiplicity of t_signalGroup_vmsBoardReference.groupIndex (attribute 648) := 0..1
- multiplicity of t_signals_semantics_speed.type (attribute 649) := 0..1
- multiplicity of t_signals_semantics_speed.value (attribute 650) := 0..1
- multiplicity of t_signals_semantics_speed.unit (attribute 651) := 0..1
- multiplicity of t_header_roadRegulation.type (attribute 660) := 0..1
- multiplicity of t_header_signalRegulation.type (attribute 661) := 0..1
- multiplicity of t_header_signalRegulation.subtype (attribute 662) := 0..1
- multiplicity of t_signalGroup_vmsBoardReference.vmsIndex (attribute 663) := 0..1
- multiplicity of t_road_signals_vmsBoard.v (attribute 667) := 0..1
- multiplicity of t_road_signals_vmsBoard.z (attribute 668) := 0..1
- multiplicity of t_road_signals_signal_road.zOffset (attribute 669) := 0..1
- multiplicity of t_signals_semantics_lane.type (attribute 670) := 0..1
- multiplicity of t_signals_semantics_priority.type (attribute 671) := 0..1
- multiplicity of t_signals_semantics_supplementaryTime.type (attribute 672) := 0..1
- multiplicity of t_signals_semantics_supplementaryTime.value (attribute 673) := 0..1
- multiplicity of t_road_lateralProfile_crossSectionSurface_coefficients.s (attribute 675) := 0..1
- multiplicity of t_road_lanes_laneSection_lr_lane_access_restriction.type (attribute 676) := 0..1
- multiplicity of t_signals_semantics_supplementaryDistance.type (attribute 677) := 0..1
- multiplicity of t_signals_semantics_supplementaryDistance.value (attribute 678) := 0..1
- multiplicity of t_signals_semantics_supplementaryDistance.unit (attribute 679) := 0..1
- multiplicity of t_signals_semantics_supplementaryEnvironment.type (attribute 706) := 0..1
- multiplicity of t_road_objects_object_outlines_outline_curveLocal.hdg (attribute 777) := 1..1
- multiplicity of t_road_objects_object_outlines_outline_curveLocal.length (attribute 778) := 1..1

## ODR-2: A base class does not also hold what its subtypes declare

The schema comments these particles out of `_OpenDriveElement` and `t_junction` "to comply with the sequence order of earlier OpenDRIVE versions": every subtype declares them itself, in its own place. The model draws them on the base class as well, so a UML reader sees each of them twice on every subtype. They are removed from the base class, which is what the schema implements.

**Normative schema:** unchanged: the normative schema already leaves them out

- _OpenDriveElement → g_additionalData (connector 6) removed
- t_junction.priority → t_junction_priority (connector 86) removed
- t_junction.controller → t_junction_controller (connector 87) removed
- t_junction.surface → t_road_surface (connector 88) removed
- t_junction → g_additionalData (connector 243) removed
- t_junction.planView → t_road_planView (connector 354) removed
- t_junction.objects → t_road_objects (connector 355) removed

## ODR-3: An element is one association

`t_junction_virtual` draws its `connection` element three times, once to its declared type and once to each of the two types its `xs:alternative`s select. UML gives a class one property per name, so a reader sees three conflicting `connection` properties. The alternatives are already stated by their `XSDAlternative_*` tags; the association to the declared type is kept.

**Normative schema:** unchanged: the derivation declares one element per role

- t_junction_virtual.connection → t_junction_connection_virtual_default (connector 255) removed
- t_junction_virtual.connection → t_junction_connection_virtual (connector 538) removed

## ODR-4: The junction's type alternatives are numbered in the schema's order

`XSDAlternative_nr` orders an element's type alternatives, and the first whose test holds assigns the type. The model numbers `junction`'s crossing 1, direct 2 and virtual 3; the schema lists virtual, direct, crossing. The tests are mutually exclusive, so the language is the same, but the model should say what the schema does.

**Normative schema:** unchanged

- tag XSDAlternative_nr = '1' on t_junction_virtual (class 181)
- tag XSDAlternative_nr = '3' on t_junction_crossing (class 186)

## ODR-5: The schema's element order is recorded in the model

A sequence fixes the order of its elements in a document, and the schema gives these content models an order the model does not state: only 20 associations carry a `position` tag, and some of those contradict the schema. Each association of these classes gets the `position` of its element in the normative schema.

**Normative schema:** unchanged: it is the normative order, now stated

- tag position = '1' on ? (connector 184) (not in the export)
- tag position = '2' on ? (connector 183) (not in the export)
- tag position = '3' on ? (connector 186) (not in the export)
- tag position = '4' on ? (connector 187) (not in the export)
- tag position = '5' on ? (connector 188) (not in the export)
- tag position = '6' on ? (connector 189) (not in the export)
- tag position = '7' on ? (connector 1) (not in the export)
- tag position = '8' on ? (connector 401) (not in the export)
- tag position = '1' on t_header.geoReference → t_header_GeoReference (connector 75)
- tag position = '2' on t_header.offset → t_header_Offset (connector 79)
- tag position = '3' on t_header.license → t_license (connector 316)
- tag position = '4' on t_header → g_additionalData (connector 10)
- tag position = '5' on t_header.defaultRegulations → t_header_defaultRegulations (connector 405)
- tag position = '1' on t_header_roadRegulation → _OpenDriveElement (connector 413)
- tag position = '2' on t_header_roadRegulation → g_additionalData (connector 492)
- tag position = '3' on t_header_roadRegulation.semantics → t_signals_semantics (connector 420)
- tag position = '1' on t_header_signalRegulation → _OpenDriveElement (connector 414)
- tag position = '2' on t_header_signalRegulation → g_additionalData (connector 491)
- tag position = '3' on t_header_signalRegulation.semantics → t_signals_semantics (connector 421)
- tag position = '1' on t_junction_common.connection → t_junction_connection_common (connector 329)
- tag position = '2' on t_junction_common.crossPath → t_junction_crossPath (connector 356)
- tag position = '3' on t_junction_common.priority → t_junction_priority (connector 335)
- tag position = '4' on t_junction_common.controller → t_junction_controller (connector 338)
- tag position = '5' on t_junction_common.surface → t_road_surface (connector 256)
- tag position = '6' on t_junction_common.planView → t_road_planView (connector 340)
- tag position = '7' on t_junction_common.objects → t_road_objects (connector 371)
- tag position = '8' on t_junction_common.boundary → t_junction_boundary (connector 365)
- tag position = '9' on t_junction_common.elevationGrid → t_junction_elevationGrid (connector 364)
- tag position = '10' on t_junction_common → g_additionalData (connector 332)
- tag position = '1' on t_junction_connection.laneLink → t_junction_connection_laneLink (connector 125)
- tag position = '2' on t_junction_connection → g_additionalData (connector 24)
- tag position = '1' on t_junction_connection_virtual.predecessor → t_junction_predecessorSuccessor (connector 126)
- tag position = '2' on t_junction_connection_virtual.successor → t_junction_predecessorSuccessor (connector 91)
- tag position = '1' on t_junction_crossing.roadSection → t_junction_roadSection (connector 306)
- tag position = '2' on t_junction_crossing.priority → t_junction_priority (connector 307)
- tag position = '3' on t_junction_crossing.controller → t_junction_controller (connector 278)
- tag position = '4' on t_junction_crossing.surface → t_road_surface (connector 280)
- tag position = '5' on t_junction_crossing.planView → t_road_planView (connector 362)
- tag position = '6' on t_junction_crossing.objects → t_road_objects (connector 373)
- tag position = '7' on t_junction_crossing → g_additionalData (connector 277)
- tag position = '1' on t_junction_direct.connection → t_junction_connection_direct (connector 330)
- tag position = '2' on t_junction_direct.priority → t_junction_priority (connector 336)
- tag position = '3' on t_junction_direct.controller → t_junction_controller (connector 337)
- tag position = '4' on t_junction_direct.surface → t_road_surface (connector 279)
- tag position = '5' on t_junction_direct.planView → t_road_planView (connector 361)
- tag position = '6' on t_junction_direct.objects → t_road_objects (connector 372)
- tag position = '7' on t_junction_direct → g_additionalData (connector 333)
- tag position = '1' on t_junction_virtual.connection → t_junction_connection (connector 274)
- tag position = '2' on t_junction_virtual.crossPath → t_junction_crossPath (connector 317)
- tag position = '3' on t_junction_virtual.priority → t_junction_priority (connector 334)
- tag position = '4' on t_junction_virtual.controller → t_junction_controller (connector 339)
- tag position = '5' on t_junction_virtual.surface → t_road_surface (connector 131)
- tag position = '6' on t_junction_virtual.planView → t_road_planView (connector 309)
- tag position = '7' on t_junction_virtual.objects → t_road_objects (connector 370)
- tag position = '8' on t_junction_virtual → g_additionalData (connector 331)
- tag position = '1' on t_road.link → t_road_link (connector 160)
- tag position = '2' on t_road.type → t_road_type (connector 95)
- tag position = '3' on t_road.planView → t_road_planView (connector 135)
- tag position = '4' on t_road.elevationProfile → t_road_elevationProfile (connector 134)
- tag position = '5' on t_road.lateralProfile → t_road_lateralProfile (connector 133)
- tag position = '6' on t_road.lanes → t_road_lanes (connector 161)
- tag position = '7' on t_road.objects → t_road_objects (connector 165)
- tag position = '8' on t_road.signals → t_road_signals (connector 166)
- tag position = '9' on t_road.surface → t_road_surface (connector 67)
- tag position = '10' on t_road.railroad → t_road_railroad (connector 167)
- tag position = '11' on t_road → g_additionalData (connector 30)
- tag position = '1' on t_road_elevationProfile.elevation → t_road_elevationProfile_elevation (connector 128)
- tag position = '2' on t_road_elevationProfile → g_additionalData (connector 70)
- tag position = '1' on t_road_lanes.laneOffset → t_road_lanes_laneOffset (connector 142)
- tag position = '2' on t_road_lanes.laneSection → t_road_lanes_laneSection (connector 143)
- tag position = '3' on t_road_lanes → g_additionalData (connector 72)
- tag position = '1' on t_road_lanes_laneSection.left → t_road_lanes_laneSection_left (connector 116)
- tag position = '2' on t_road_lanes_laneSection.center → t_road_lanes_laneSection_center (connector 115)
- tag position = '3' on t_road_lanes_laneSection.right → t_road_lanes_laneSection_right (connector 117)
- tag position = '4' on t_road_lanes_laneSection → g_additionalData (connector 77)
- tag position = '1' on t_road_lanes_laneSection_center.lane → t_road_lanes_laneSection_center_lane (connector 139)
- tag position = '2' on t_road_lanes_laneSection_center → g_additionalData (connector 78)
- tag position = '1' on t_road_lanes_laneSection_lcr_lane_link.predecessor → t_road_lanes_laneSection_lcr_lane_link_predecessorSuccessor (connector 110)
- tag position = '2' on t_road_lanes_laneSection_lcr_lane_link.successor → t_road_lanes_laneSection_lcr_lane_link_predecessorSuccessor (connector 111)
- tag position = '3' on t_road_lanes_laneSection_lcr_lane_link → g_additionalData (connector 23)
- tag position = '1' on t_road_lanes_laneSection_lcr_lane_roadMark.sway → t_road_lanes_laneSection_lcr_lane_roadMark_sway (connector 105)
- tag position = '2' on t_road_lanes_laneSection_lcr_lane_roadMark.type → t_road_lanes_laneSection_lcr_lane_roadMark_type (connector 136)
- tag position = '3' on t_road_lanes_laneSection_lcr_lane_roadMark.explicit → t_road_lanes_laneSection_lcr_lane_roadMark_explicit (connector 103)
- tag position = '4' on t_road_lanes_laneSection_lcr_lane_roadMark → g_additionalData (connector 228)
- tag position = '1' on t_road_lanes_laneSection_lr_lane.link → t_road_lanes_laneSection_lcr_lane_link (connector 181)
- tag position = '2' on t_road_lanes_laneSection_lr_lane → LaneGeometry (connector 25)
- tag position = '3' on t_road_lanes_laneSection_lr_lane.roadMark → t_road_lanes_laneSection_lcr_lane_roadMark (connector 141)
- tag position = '4' on t_road_lanes_laneSection_lr_lane.material → t_road_lanes_laneSection_lr_lane_material (connector 106)
- tag position = '5' on t_road_lanes_laneSection_lr_lane.speed → t_road_lanes_laneSection_lr_lane_speed (connector 109)
- tag position = '6' on t_road_lanes_laneSection_lr_lane.access → t_road_lanes_laneSection_lr_lane_access (connector 107)
- tag position = '7' on t_road_lanes_laneSection_lr_lane.height → t_road_lanes_laneSection_lr_lane_height (connector 180)
- tag position = '8' on t_road_lanes_laneSection_lr_lane.rule → t_road_lanes_laneSection_lr_lane_rule (connector 140)
- tag position = '9' on t_road_lanes_laneSection_lr_lane → g_additionalData (connector 12)
- tag position = '1' on t_road_lanes_laneSection_lr_lane_access.restriction → t_road_lanes_laneSection_lr_lane_access_restriction (connector 368)
- tag position = '2' on t_road_lanes_laneSection_lr_lane_access → g_additionalData (connector 263)
- tag position = '1' on t_road_lateralProfile_crossSectionSurface.tOffset → t_road_lateralProfile_crossSectionSurface_tOffset (connector 396)
- tag position = '2' on t_road_lateralProfile_crossSectionSurface.surfaceStrips → t_road_lateralProfile_crossSectionSurface_surfaceStrip (connector 395)
- tag position = '3' on t_road_lateralProfile_crossSectionSurface → g_additionalData (connector 493)
- tag position = '1' on t_road_lateralProfile_crossSectionSurface_strip.width → t_road_lateralProfile_crossSectionSurface_strip_width (connector 388)
- tag position = '2' on t_road_lateralProfile_crossSectionSurface_strip.constant → t_road_lateralProfile_crossSectionSurface_strip_constant (connector 389)
- tag position = '3' on t_road_lateralProfile_crossSectionSurface_strip.linear → t_road_lateralProfile_crossSectionSurface_strip_linear (connector 391)
- tag position = '4' on t_road_lateralProfile_crossSectionSurface_strip.quadratic → t_road_lateralProfile_crossSectionSurface_strip_quadratic (connector 392)
- tag position = '5' on t_road_lateralProfile_crossSectionSurface_strip.cubic → t_road_lateralProfile_crossSectionSurface_strip_cubic (connector 390)
- tag position = '6' on t_road_lateralProfile_crossSectionSurface_strip → g_additionalData (connector 470)
- tag position = '1' on t_road_link.predecessor → t_road_link_predecessorSuccessor (connector 121)
- tag position = '2' on t_road_link.successor → t_road_link_predecessorSuccessor (connector 122)
- tag position = '3' on t_road_link → g_additionalData (connector 7)
- tag position = '1' on t_road_objects.object → t_road_objects_object (connector 150)
- tag position = '2' on t_road_objects.objectReference → t_road_objects_objectReference (connector 171)
- tag position = '3' on t_road_objects.tunnel → t_road_objects_tunnel (connector 173)
- tag position = '4' on t_road_objects.bridge → t_road_objects_bridge (connector 172)
- tag position = '5' on t_road_objects → g_additionalData (connector 231)
- tag position = '1' on t_road_objects_object.repeat → t_road_objects_object_repeat (connector 113)
- tag position = '2' on t_road_objects_object.outline → t_road_objects_object_outlines_outline (connector 118)
- tag position = '3' on t_road_objects_object.outlines → t_road_objects_object_outlines (connector 123)
- tag position = '4' on t_road_objects_object.material → t_road_objects_object_material (connector 124)
- tag position = '5' on t_road_objects_object.validity → t_road_objects_object_laneValidity (connector 410)
- tag position = '6' on t_road_objects_object.parkingSpace → t_road_objects_object_parkingSpace (connector 146)
- tag position = '7' on t_road_objects_object.markings → t_road_objects_object_markings (connector 147)
- tag position = '8' on t_road_objects_object.borders → t_road_objects_object_borders (connector 148)
- tag position = '9' on t_road_objects_object → g_additionalData (connector 232)
- tag position = '10' on t_road_objects_object.surface → t_road_objects_object_surface (connector 253)
- tag position = '11' on t_road_objects_object.skeleton → t_road_objects_object_skeleton (connector 387)
- tag position = '1' on t_road_objects_object_surface → g_additionalData (connector 283)
- tag position = '2' on t_road_objects_object_surface.CRG → t_road_objects_object_surface_CRG (connector 244)
- tag position = '1' on t_road_planView.geometry → t_road_planView_geometry (connector 129)
- tag position = '2' on t_road_planView → g_additionalData (connector 65)
- tag position = '1' on t_road_signals.signal → t_road_signals_signal_road (connector 157)
- tag position = '2' on t_road_signals.signalReference → t_road_signals_signalReference (connector 156)
- tag position = '3' on t_road_signals → g_additionalData (connector 236)
- tag position = '1' on t_road_signals_signal.validity → t_road_objects_object_laneValidity (connector 114)
- tag position = '2' on t_road_signals_signal.dependency → t_road_signals_signal_dependency (connector 155)
- tag position = '3' on t_road_signals_signal.reference → t_road_signals_signal_reference (connector 158)
- tag position = '4' on t_road_signals_signal → t_physicalPosition (connector 43)
- tag position = '5' on t_road_signals_signal → g_additionalData (connector 237)
- tag position = '6' on t_road_signals_signal.semantics → t_signals_semantics (connector 404)
- tag position = '1' on t_road_signals_staticBoard → g_additionalData (connector 381)
- tag position = '2' on t_road_signals_staticBoard.sign → t_road_signals_board_sign (connector 342)
- tag position = '1' on t_road_type.speed → t_road_type_speed (connector 127)
- tag position = '2' on t_road_type → g_additionalData (connector 64)
- tag position = '1' on t_signals_semantics_prohibited → g_additionalData (connector 446)
- tag position = '2' on t_signals_semantics_prohibited.animal → t_signals_semantics_animal (connector 513)
- tag position = '3' on t_signals_semantics_prohibited.person → t_signals_semantics_person (connector 512)
- tag position = '4' on t_signals_semantics_prohibited.vehicle → t_signals_semantics_vehicle (connector 509)
- tag position = '1' on t_signals_semantics_supplementaryAllows → g_additionalData (connector 459)
- tag position = '2' on t_signals_semantics_supplementaryAllows.animal → t_signals_semantics_animal (connector 505)
- tag position = '3' on t_signals_semantics_supplementaryAllows.person → t_signals_semantics_person (connector 504)
- tag position = '4' on t_signals_semantics_supplementaryAllows.vehicle → t_signals_semantics_vehicle (connector 503)
- tag position = '1' on t_signals_semantics_supplementaryProhibits → g_additionalData (connector 460)
- tag position = '2' on t_signals_semantics_supplementaryProhibits.animal → t_signals_semantics_animal (connector 508)
- tag position = '3' on t_signals_semantics_supplementaryProhibits.person → t_signals_semantics_person (connector 507)
- tag position = '4' on t_signals_semantics_supplementaryProhibits.vehicle → t_signals_semantics_vehicle (connector 506)

## ODR-6: The content an element includes from a group or a choice is named

An association to an `XSDgroup` or an `XSDchoice` class has no role in the model: the schema includes the target's particles in place, and a group reference needs no name. A UML reader, however, treats an unnamed end as no property at all, so the additional data of every element, and the choices `LaneGeometry`, `t_outline_geometry`, `t_polyline_geometry` and `t_physicalPosition`, are not part of the model it reads. Naming the end makes them part of it; the pipeline then includes the target's properties in place, as the schema does.

**Normative schema:** unchanged: a group reference and a nested compositor carry no role

- target role of t_license → g_additionalData (connector 315) := 'additionalData', navigable
- target role of ? (connector 1) := 'additionalData', navigable (not in the export)
- target role of t_header → g_additionalData (connector 10) := 'additionalData', navigable
- target role of t_header_Offset → g_additionalData (connector 96) := 'additionalData', navigable
- target role of t_road → g_additionalData (connector 30) := 'additionalData', navigable
- target role of t_junction_common → g_additionalData (connector 332) := 'additionalData', navigable
- target role of t_road_link → g_additionalData (connector 7) := 'additionalData', navigable
- target role of t_road_link_predecessorSuccessor → g_additionalData (connector 292) := 'additionalData', navigable
- target role of t_road_type → g_additionalData (connector 64) := 'additionalData', navigable
- target role of t_road_type_speed → g_additionalData (connector 293) := 'additionalData', navigable
- target role of t_road_planView → g_additionalData (connector 65) := 'additionalData', navigable
- target role of t_road_planView_geometry → g_additionalData (connector 69) := 'additionalData', navigable
- target role of t_road_planView_geometry_line → g_additionalData (connector 298) := 'additionalData', navigable
- target role of t_road_planView_geometry_spiral → g_additionalData (connector 299) := 'additionalData', navigable
- target role of t_road_planView_geometry_arc → g_additionalData (connector 300) := 'additionalData', navigable
- target role of t_road_planView_geometry_poly3 → g_additionalData (connector 301) := 'additionalData', navigable
- target role of t_road_planView_geometry_paramPoly3 → g_additionalData (connector 302) := 'additionalData', navigable
- target role of t_junction_boundary_segment → g_additionalData (connector 376) := 'additionalData', navigable
- target role of t_road_elevationProfile → g_additionalData (connector 70) := 'additionalData', navigable
- target role of t_road_elevationProfile_elevation → g_additionalData (connector 296) := 'additionalData', navigable
- target role of t_road_lateralProfile → g_additionalData (connector 71) := 'additionalData', navigable
- target role of t_road_lateralProfile_superelevation → g_additionalData (connector 294) := 'additionalData', navigable
- target role of t_road_lateralProfile_shape → g_additionalData (connector 295) := 'additionalData', navigable
- target role of t_road_lanes → g_additionalData (connector 72) := 'additionalData', navigable
- target role of t_road_objects_object_surface_CRG → g_additionalData (connector 284) := 'additionalData', navigable
- target role of t_road_lanes_laneOffset → g_additionalData (connector 259) := 'additionalData', navigable
- target role of t_road_lanes_laneSection → g_additionalData (connector 77) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_left → g_additionalData (connector 220) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_center → g_additionalData (connector 78) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_right → g_additionalData (connector 227) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane → g_additionalData (connector 12) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane → LaneGeometry (connector 25) := 'laneGeometry', navigable
- target role of t_road_lanes_laneSection_lcr_lane_link → g_additionalData (connector 23) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lcr_lane_link_predecessorSuccessor → g_additionalData (connector 265) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane_width → g_additionalData (connector 266) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane_border → g_additionalData (connector 267) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lcr_lane_roadMark → g_additionalData (connector 228) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lcr_lane_roadMark_sway → g_additionalData (connector 268) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lcr_lane_roadMark_type → g_additionalData (connector 229) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lcr_lane_roadMark_type_line → g_additionalData (connector 269) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lcr_lane_roadMark_explicit → g_additionalData (connector 230) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lcr_lane_roadMark_explicit_line → g_additionalData (connector 270) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane_material → g_additionalData (connector 261) := 'additionalData', navigable
- target role of t_road_objects_object_outlines → g_additionalData (connector 245) := 'additionalData', navigable
- target role of t_road_objects_object_outlines_outline → t_outline_geometry (connector 119) := 't_outline_geometry', navigable
- target role of t_road_objects_object_outlines_outline → g_additionalData (connector 246) := 'additionalData', navigable
- target role of t_road_objects_object_outlines_outline_cornerRoad → g_additionalData (connector 285) := 'additionalData', navigable
- target role of t_road_objects_object_outlines_outline_cornerLocal → g_additionalData (connector 286) := 'additionalData', navigable
- target role of t_road_objects_object_material → g_additionalData (connector 271) := 'additionalData', navigable
- target role of t_road_objects_object_laneValidity → g_additionalData (connector 272) := 'additionalData', navigable
- target role of t_road_objects_object_parkingSpace → g_additionalData (connector 282) := 'additionalData', navigable
- target role of t_road_objects_object_markings → g_additionalData (connector 247) := 'additionalData', navigable
- target role of t_road_objects_object_markings_marking → g_additionalData (connector 248) := 'additionalData', navigable
- target role of t_road_objects_object_borders → g_additionalData (connector 249) := 'additionalData', navigable
- target role of t_road_objects_object_borders_border → g_additionalData (connector 250) := 'additionalData', navigable
- target role of t_road_objects_objectReference → g_additionalData (connector 233) := 'additionalData', navigable
- target role of t_road_objects_tunnel → g_additionalData (connector 235) := 'additionalData', navigable
- target role of t_road_signals_signal_positionInertial → g_additionalData (connector 312) := 'additionalData', navigable
- target role of t_road_signals_signalReference → g_additionalData (connector 238) := 'additionalData', navigable
- target role of t_road_surface → g_additionalData (connector 239) := 'additionalData', navigable
- target role of t_road_surface_CRG → g_additionalData (connector 297) := 'additionalData', navigable
- target role of t_road_railroad → g_additionalData (connector 240) := 'additionalData', navigable
- target role of t_road_railroad_switch → g_additionalData (connector 241) := 'additionalData', navigable
- target role of t_junction_connection → g_additionalData (connector 24) := 'additionalData', navigable
- target role of t_junction_predecessorSuccessor → g_additionalData (connector 257) := 'additionalData', navigable
- target role of t_junction_connection_laneLink → g_additionalData (connector 254) := 'additionalData', navigable
- target role of t_junction_priority → g_additionalData (connector 36) := 'additionalData', navigable
- target role of t_junction_controller → g_additionalData (connector 84) := 'additionalData', navigable
- target role of t_junctionGroup → g_additionalData (connector 251) := 'additionalData', navigable
- target role of t_junctionGroup_junctionReference → g_additionalData (connector 258) := 'additionalData', navigable
- target role of t_station → g_additionalData (connector 290) := 'additionalData', navigable
- target role of t_station_platform → g_additionalData (connector 252) := 'additionalData', navigable
- target role of t_station_platform_segment → g_additionalData (connector 291) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane_speed → g_additionalData (connector 262) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane_access → g_additionalData (connector 263) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane_height → g_additionalData (connector 260) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane_rule → g_additionalData (connector 264) := 'additionalData', navigable
- target role of t_road_objects → g_additionalData (connector 231) := 'additionalData', navigable
- target role of t_road_objects_object → g_additionalData (connector 232) := 'additionalData', navigable
- target role of t_road_objects_bridge → g_additionalData (connector 234) := 'additionalData', navigable
- target role of t_road_signals → g_additionalData (connector 236) := 'additionalData', navigable
- target role of t_road_signals_signal → t_physicalPosition (connector 43) := 't_physicalPosition', navigable
- target role of t_road_signals_signal → g_additionalData (connector 237) := 'additionalData', navigable
- target role of t_road_signals_signal_dependency → g_additionalData (connector 304) := 'additionalData', navigable
- target role of t_road_signals_signal_reference → g_additionalData (connector 311) := 'additionalData', navigable
- target role of t_road_signals_signal_positionRoad → g_additionalData (connector 313) := 'additionalData', navigable
- target role of t_road_railroad_switch_mainTrack → g_additionalData (connector 287) := 'additionalData', navigable
- target role of t_road_railroad_switch_sideTrack → g_additionalData (connector 288) := 'additionalData', navigable
- target role of t_road_railroad_switch_partner → g_additionalData (connector 289) := 'additionalData', navigable
- target role of t_controller → g_additionalData (connector 242) := 'additionalData', navigable
- target role of t_controller_control → g_additionalData (connector 303) := 'additionalData', navigable
- target role of t_road_objects_object_repeat → g_additionalData (connector 273) := 'additionalData', navigable
- target role of t_road_objects_object_markings_marking_cornerReference → g_additionalData (connector 281) := 'additionalData', navigable
- target role of t_road_objects_object_surface → g_additionalData (connector 283) := 'additionalData', navigable
- target role of t_junction_direct → g_additionalData (connector 333) := 'additionalData', navigable
- target role of t_junction_roadSection → g_additionalData (connector 276) := 'additionalData', navigable
- target role of t_junction_crossPath → g_additionalData (connector 380) := 'additionalData', navigable
- target role of t_junction_crossPath_laneLink → g_additionalData (connector 379) := 'additionalData', navigable
- target role of t_road_signals_staticBoard → g_additionalData (connector 381) := 'additionalData', navigable
- target role of t_road_signals_displayArea → g_additionalData (connector 382) := 'additionalData', navigable
- target role of t_junction_virtual → g_additionalData (connector 331) := 'additionalData', navigable
- target role of t_junction_crossing → g_additionalData (connector 277) := 'additionalData', navigable
- target role of t_road_objects_object_skeleton_polyline_vertexRoad → g_additionalData (connector 466) := 'additionalData', navigable
- target role of t_road_objects_object_skeleton_polyline_vertexLocal → g_additionalData (connector 465) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface → g_additionalData (connector 493) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_surfaceStrip → g_additionalData (connector 494) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_tOffset → g_additionalData (connector 495) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_strip → g_additionalData (connector 470) := 'additionalData', navigable
- target role of t_junction_boundary → g_additionalData (connector 374) := 'additionalData', navigable
- target role of t_junction_elevationGrid_elevation → g_additionalData (connector 378) := 'additionalData', navigable
- target role of t_road_objects_object_skeleton → g_additionalData (connector 468) := 'additionalData', navigable
- target role of t_road_objects_object_skeleton_polyline → t_polyline_geometry (connector 386) := 't_polyline_geometry', navigable
- target role of t_road_objects_object_skeleton_polyline → g_additionalData (connector 467) := 'additionalData', navigable
- target role of t_junction_elevationGrid → g_additionalData (connector 377) := 'additionalData', navigable
- target role of t_signalGroup_vmsGroup → g_additionalData (connector 487) := 'additionalData', navigable
- target role of t_signalGroup_vmsBoardReference → g_additionalData (connector 488) := 'additionalData', navigable
- target role of t_header_defaultRegulations → g_additionalData (connector 469) := 'additionalData', navigable
- target role of t_signals_semantics → g_additionalData (connector 464) := 'additionalData', navigable
- target role of t_signals_semantics_speed → g_additionalData (connector 418) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_coefficients → g_additionalData (connector 471) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_strip_width → g_additionalData (connector 472) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_strip_constant → g_additionalData (connector 474) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_strip_cubic → g_additionalData (connector 476) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_strip_linear → g_additionalData (connector 473) := 'additionalData', navigable
- target role of t_road_lateralProfile_crossSectionSurface_strip_quadratic → g_additionalData (connector 475) := 'additionalData', navigable
- target role of t_header_signalRegulation → g_additionalData (connector 491) := 'additionalData', navigable
- target role of t_road_signals_vmsBoard → g_additionalData (connector 419) := 'additionalData', navigable
- target role of t_signals_semantics_lane → g_additionalData (connector 444) := 'additionalData', navigable
- target role of t_signals_semantics_warning → g_additionalData (connector 453) := 'additionalData', navigable
- target role of t_signals_semantics_prohibited → g_additionalData (connector 446) := 'additionalData', navigable
- target role of t_signals_semantics_supplementaryTime → g_additionalData (connector 458) := 'additionalData', navigable
- target role of t_signals_semantics_supplementaryAllows → g_additionalData (connector 459) := 'additionalData', navigable
- target role of t_signals_semantics_supplementaryProhibits → g_additionalData (connector 460) := 'additionalData', navigable
- target role of t_signals_semantics_supplementaryDistance → g_additionalData (connector 461) := 'additionalData', navigable
- target role of t_signals_semantics_supplementaryEnvironment → g_additionalData (connector 462) := 'additionalData', navigable
- target role of t_signals_semantics_supplementaryExplanatory → g_additionalData (connector 463) := 'additionalData', navigable
- target role of t_signals_semantics_routing → g_additionalData (connector 454) := 'additionalData', navigable
- target role of t_signals_semantics_streetname → g_additionalData (connector 455) := 'additionalData', navigable
- target role of t_signals_semantics_tourist → g_additionalData (connector 457) := 'additionalData', navigable
- target role of t_header_roadRegulation → g_additionalData (connector 492) := 'additionalData', navigable
- target role of t_signals_semantics_parking → g_additionalData (connector 456) := 'additionalData', navigable
- target role of t_signals_semantics_priority → g_additionalData (connector 445) := 'additionalData', navigable
- target role of t_road_lanes_laneSection_lr_lane_access_restriction → g_additionalData (connector 375) := 'additionalData', navigable

## ODR-7: The alternatives of a choice are stated as one union set

A class whose `modelGroup` is `choice`, and every `XSDchoice` class, makes its elements mutually exclusive: a document gives exactly one of them. A UML reader sees independent properties instead, and the OWL target and the SHACL require every one of them at once, which rejects every conforming document. ShapeChange's `SC_UNION_SET` tag states, on the association ends, which properties exclude each other; the value names the choice. The additional data that `t_road_planView_geometry`'s choice also offers as an alternative is left out of the set; see the change request.

**Normative schema:** unchanged: the derivation does not read `SC_UNION_SET`

- tag SC_UNION_SET = 't_road_planView_geometry' on the target end of t_road_planView_geometry.poly3 → t_road_planView_geometry_poly3 (connector 97)
- tag SC_UNION_SET = 't_road_planView_geometry' on the target end of t_road_planView_geometry.arc → t_road_planView_geometry_arc (connector 98)
- tag SC_UNION_SET = 't_road_planView_geometry' on the target end of t_road_planView_geometry.spiral → t_road_planView_geometry_spiral (connector 99)
- tag SC_UNION_SET = 't_road_planView_geometry' on the target end of t_road_planView_geometry.line → t_road_planView_geometry_line (connector 100)
- tag SC_UNION_SET = 't_road_planView_geometry' on the target end of t_road_planView_geometry.paramPoly3 → t_road_planView_geometry_paramPoly3 (connector 130)
- tag SC_UNION_SET = 'LaneGeometry' on the target end of LaneGeometry.border → t_road_lanes_laneSection_lr_lane_border (connector 61)
- tag SC_UNION_SET = 'LaneGeometry' on the target end of LaneGeometry.width → t_road_lanes_laneSection_lr_lane_width (connector 68)
- tag SC_UNION_SET = 't_outline_geometry' on the target end of t_outline_geometry.cornerRoad → t_road_objects_object_outlines_outline_cornerRoad (connector 144)
- tag SC_UNION_SET = 't_outline_geometry' on the target end of t_outline_geometry.cornerLocal → t_road_objects_object_outlines_outline_cornerLocal (connector 145)
- tag SC_UNION_SET = 't_outline_geometry' on the target end of t_outline_geometry.curveLocal → t_road_objects_object_outlines_outline_curveLocal (connector 524)
- tag SC_UNION_SET = 't_physicalPosition' on the target end of t_physicalPosition.positionRoad → t_road_signals_signal_positionRoad (connector 175)
- tag SC_UNION_SET = 't_physicalPosition' on the target end of t_physicalPosition.positionInertial → t_road_signals_signal_positionInertial (connector 176)
- tag SC_UNION_SET = 't_polyline_geometry' on the target end of t_polyline_geometry.vertexRoad → t_road_objects_object_skeleton_polyline_vertexRoad (connector 384)
- tag SC_UNION_SET = 't_polyline_geometry' on the target end of t_polyline_geometry.vertexLocal → t_road_objects_object_skeleton_polyline_vertexLocal (connector 385)
- tag SC_UNION_SET = 't_road_objects_object_outlines_outline_curveLocal' on the target end of t_road_objects_object_outlines_outline_curveLocal.arc → t_road_objects_object_outlines_outline_curveLocal_arc (connector 530)
- tag SC_UNION_SET = 't_road_objects_object_outlines_outline_curveLocal' on the target end of t_road_objects_object_outlines_outline_curveLocal.paramPoly3 → t_road_objects_object_outlines_outline_curveLocal_paramPoly3 (connector 531)
- tag SC_UNION_SET = 't_road_objects_object_outlines_outline_curveLocal' on the target end of t_road_objects_object_outlines_outline_curveLocal.line → t_road_objects_object_outlines_outline_curveLocal_line (connector 533)

## ODR-8: No element requires a child of the abstract base type

`t_header_defaultRegulations`, `t_header_roadRegulation`, `t_header_signalRegulation` and `t_signalGroup_vmsGroup` each have an unnamed 1..1 association to `_OpenDriveElement`, the abstract base of every OpenDRIVE type. The schema therefore requires a child element `<_OpenDriveElement>`, which no document can supply without `xsi:type`, so none of these four elements can occur in a valid file. The associations are removed.

**Normative schema:** changed: the four types no longer require an `_OpenDriveElement` child

- t_signalGroup_vmsGroup → _OpenDriveElement (connector 415) removed
- t_header_defaultRegulations → _OpenDriveElement (connector 412) removed
- t_header_signalRegulation → _OpenDriveElement (connector 414) removed
- t_header_roadRegulation → _OpenDriveElement (connector 413) removed

## ODR-9: An attribute's type refers to the class it names

These attributes name a class of the model as their type, but EA holds only the name: the classifier reference is missing, so nothing resolves it and the schema types them `xs:string`. The reference is set to the class of that name.

**Normative schema:** changed: the attributes are typed by their class instead of `xs:string`

- type of t_road_lanes_laneSection_lcr_lane_link_predecessorSuccessor.layer (attribute 749) refers to e_layerType (class 269)
- type of t_road_signals_displayArea.width (attribute 282) refers to t_grEqZero (class 2)
- type of t_road_signals_displayArea.height (attribute 228) refers to t_grEqZero (class 2)
- type of t_junction_elevationGrid_elevation.left (attribute 399) refers to t_junction_grid_position_list (class 195)
- type of t_junction_elevationGrid_elevation.center (attribute 378) refers to t_junction_grid_position_list (class 195)
- type of t_junction_elevationGrid_elevation.right (attribute 379) refers to t_junction_grid_position_list (class 195)
- type of t_junction_elevationGrid.sStart (attribute 316) refers to t_grEqZero (class 2)
- type of t_junction_elevationGrid.gridSpacing (attribute 317) refers to t_grEqZero (class 2)

## ODR-10: The model declares no target namespace, as the schema does not

Every schema package carries `targetNamespace` `http://code.asam.net/simulation/standard/opendrive_schema`, but no normative document declares a target namespace, so OpenDRIVE elements are in no namespace. The seven packages sharing one namespace is also what makes the OWL target report 227 classes outside their schema. The tag is removed; the pipeline names the schema package in its configuration, as it does for OpenSCENARIO.

**Normative schema:** unchanged: the normative schema has no target namespace

- tag targetNamespace removed from Road (package 6)
- tag targetNamespace removed from Signal (package 9)
- tag targetNamespace removed from Lane (package 7)
- tag targetNamespace removed from Junction (package 5)
- tag targetNamespace removed from Object (package 8)
- tag targetNamespace removed from Railroad (package 10)
- tag targetNamespace removed from Core (package 4)
