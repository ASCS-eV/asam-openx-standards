# OpenSCENARIO XML 1.5 candidate

Based on ASAM OpenSCENARIO XML V1.4.0, the model in `standards/asam-openscenario-xml/uml/openscenario.scxml`. This file is generated from `changes.json` by `scripts/candidate_model.py`; edit that file instead.

The OpenSCENARIO XML V1.4.0 model with the changes below, which make the model say, in terms a UML reader understands, what ASAM's generator makes of it in the normative schema. None of them changes that schema: the port of ASAM's own generator writes it byte for byte from this candidate as from the release.

## OSC-1: A union that also carries other properties is a complex type with a union set

These classes are «union»s whose content is a choice, and they also carry attributes or name references outside the choice, which the schema makes required or optional in their own right. ISO 19103 reads every property of a «union» as an alternative, so a UML reader, and the OWL encoding of a union, folds those properties into the choice: for `Action`, `Color`, `Condition` and `ControllerDistributionEntry` the result is unsatisfiable. Following the ShapeChange maintainer's recommendation, the classes lose «union» and state the choice with ShapeChange's `SC_UNION_SET` tag on the ends of its alternatives; the other properties keep their own multiplicity.

**Normative schema:** unchanged: ASAM's generator writes a complex type from `XSDcomplexType` and its choice from `modelGroup`, and reads neither «union» nor `SC_UNION_SET`

- stereotypes of Action (class 10) := «XSDcomplexType»
- tag SC_UNION_SET = 'Action' on the target end of Action.globalAction → GlobalAction (connector 229)
- tag SC_UNION_SET = 'Action' on the target end of Action.userDefinedAction → UserDefinedAction (connector 231)
- tag SC_UNION_SET = 'Action' on the target end of Action.privateAction → PrivateAction (connector 230)
- stereotypes of AssignControllerAction (class 165) := «XSDcomplexType»
- tag SC_UNION_SET = 'AssignControllerAction' on the target end of AssignControllerAction.controller → Controller (connector 222)
- tag SC_UNION_SET = 'AssignControllerAction' on the target end of AssignControllerAction.catalogReference → CatalogReference (connector 221)
- tag SC_UNION_SET = 'AssignControllerAction' on the target end of AssignControllerAction.objectController → ObjectController (connector 465)
- stereotypes of Color (class 325) := «XSDcomplexType»
- tag SC_UNION_SET = 'Color' on the target end of Color.colorRgb → ColorRgb (connector 328)
- tag SC_UNION_SET = 'Color' on the target end of Color.colorCmyk → ColorCmyk (connector 352)
- stereotypes of Condition (class 194) := «XSDcomplexType»
- tag SC_UNION_SET = 'Condition' on the target end of Condition.byEntityCondition → ByEntityCondition (connector 204)
- tag SC_UNION_SET = 'Condition' on the target end of Condition.byValueCondition → ByValueCondition (connector 426)
- stereotypes of ControllerDistributionEntry (class 200) := «XSDcomplexType»
- tag SC_UNION_SET = 'ControllerDistributionEntry' on the target end of ControllerDistributionEntry.controller → Controller (connector 169)
- tag SC_UNION_SET = 'ControllerDistributionEntry' on the target end of ControllerDistributionEntry.catalogReference → CatalogReference (connector 182)
- stereotypes of EntityAction (class 210) := «XSDcomplexType»
- tag SC_UNION_SET = 'EntityAction' on the target end of EntityAction.addEntityAction → AddEntityAction (connector 223)
- tag SC_UNION_SET = 'EntityAction' on the target end of EntityAction.deleteEntityAction → DeleteEntityAction (connector 160)
- stereotypes of ObjectController (class 20) := «XSDcomplexType»
- tag SC_UNION_SET = 'ObjectController' on the target end of ObjectController.catalogReference → CatalogReference (connector 184)
- tag SC_UNION_SET = 'ObjectController' on the target end of ObjectController.controller → Controller (connector 170)
- stereotypes of ParameterAction (class 121) := «XSDcomplexType», «deprecated»
- tag SC_UNION_SET = 'ParameterAction' on the target end of ParameterAction.setAction → ParameterSetAction (connector 377)
- tag SC_UNION_SET = 'ParameterAction' on the target end of ParameterAction.modifyAction → ParameterModifyAction (connector 379)
- stereotypes of TrafficAction (class 71) := «XSDcomplexType»
- tag SC_UNION_SET = 'TrafficAction' on the target end of TrafficAction.trafficSourceAction → TrafficSourceAction (connector 263)
- tag SC_UNION_SET = 'TrafficAction' on the target end of TrafficAction.trafficSinkAction → TrafficSinkAction (connector 262)
- tag SC_UNION_SET = 'TrafficAction' on the target end of TrafficAction.trafficSwarmAction → TrafficSwarmAction (connector 264)
- tag SC_UNION_SET = 'TrafficAction' on the target end of TrafficAction.trafficAreaAction → TrafficAreaAction (connector 446)
- tag SC_UNION_SET = 'TrafficAction' on the target end of TrafficAction.trafficStopAction → TrafficStopAction (connector 302)
- stereotypes of VariableAction (class 275) := «XSDcomplexType»
- tag SC_UNION_SET = 'VariableAction' on the target end of VariableAction.setAction → VariableSetAction (connector 308)
- tag SC_UNION_SET = 'VariableAction' on the target end of VariableAction.modifyAction → VariableModifyAction (connector 306)

## OSC-2: The alternatives of every other choice are stated as a union set

These classes and groups have `modelGroup` `choice` without being «union»s, so a document gives exactly one of their elements, while a UML reader sees independent properties. The OWL target and the SHACL then require every alternative at once, which rejects every conforming document that uses one. `SC_UNION_SET` on the ends of the alternatives states the choice.

**Normative schema:** unchanged: ASAM's generator does not read `SC_UNION_SET`

- tag SC_UNION_SET = 'ControllerAction' on the target end of ControllerAction.assignControllerAction → AssignControllerAction (connector 220)
- tag SC_UNION_SET = 'ControllerAction' on the target end of ControllerAction.overrideControllerValueAction → OverrideControllerValueAction (connector 168)
- tag SC_UNION_SET = 'ControllerAction' on the target end of ControllerAction.activateControllerAction → ActivateControllerAction (connector 248)
- tag SC_UNION_SET = 'TrafficArea' on the target end of TrafficArea.polygon → Polygon (connector 343)
- tag SC_UNION_SET = 'TrafficArea' on the target end of TrafficArea.roadRange → RoadRange (connector 342)
- tag SC_UNION_SET = 'Trailer' on the target end of Trailer.trailer → ScenarioObject (connector 450)
- tag SC_UNION_SET = 'Trailer' on the target end of Trailer.trailerRef → EntityRef (connector 451)
- tag SC_UNION_SET = 'TrailerAction' on the target end of TrailerAction.connectTrailerAction → ConnectTrailerAction (connector 453)
- tag SC_UNION_SET = 'TrailerAction' on the target end of TrailerAction.disconnectTrailerAction → DisconnectTrailerAction (connector 454)

## OSC-4: A group of alternatives is a group, with a union set

These classes are `XSDgroup`s, whose particles the schema includes in place in each element that references them, and also «union»s, because their content is a choice. The two readings conflict for a UML reader: a «union» is a type of its own, so its alternatives become a separate node below the element instead of the element's own children. The classes keep `XSDgroup` and state the choice with `SC_UNION_SET`, so the pipeline includes their alternatives in place, as the schema does, and keeps them mutually exclusive.

**Normative schema:** unchanged: ASAM's generator writes a group from `XSDgroup` and its choice from `modelGroup`

- stereotypes of BrakeInput (class 302) := «XSDgroup»
- tag SC_UNION_SET = 'BrakeInput' on the target end of BrakeInput.brakePercent → Brake (connector 323)
- tag SC_UNION_SET = 'BrakeInput' on the target end of BrakeInput.brakeForce → Brake (connector 324)
- stereotypes of DeterministicParameterDistribution (class 227) := «XSDgroup»
- tag SC_UNION_SET = 'DeterministicParameterDistribution' on the target end of DeterministicParameterDistribution.deterministicMultiParameterDistribution → DeterministicMultiParameterDistribution (connector 304)
- tag SC_UNION_SET = 'DeterministicParameterDistribution' on the target end of DeterministicParameterDistribution.deterministicSingleParameterDistribution → DeterministicSingleParameterDistribution (connector 305)
- stereotypes of DeterministicSingleParameterDistributionType (class 224) := «XSDgroup»
- tag SC_UNION_SET = 'DeterministicSingleParameterDistributionType' on the target end of DeterministicSingleParameterDistributionType.distributionSet → DistributionSet (connector 268)
- tag SC_UNION_SET = 'DeterministicSingleParameterDistributionType' on the target end of DeterministicSingleParameterDistributionType.distributionRange → DistributionRange (connector 269)
- tag SC_UNION_SET = 'DeterministicSingleParameterDistributionType' on the target end of DeterministicSingleParameterDistributionType.userDefinedDistribution → UserDefinedDistribution (connector 267)
- stereotypes of DistributionDefinition (class 229) := «XSDgroup»
- tag SC_UNION_SET = 'DistributionDefinition' on the target end of DistributionDefinition.deterministic → Deterministic (connector 287)
- tag SC_UNION_SET = 'DistributionDefinition' on the target end of DistributionDefinition.stochastic → Stochastic (connector 442)
- stereotypes of EntityObject (class 212) := «XSDgroup»
- tag SC_UNION_SET = 'EntityObject' on the target end of EntityObject.catalogReference → CatalogReference (connector 183)
- tag SC_UNION_SET = 'EntityObject' on the target end of EntityObject.vehicle → Vehicle (connector 139)
- tag SC_UNION_SET = 'EntityObject' on the target end of EntityObject.pedestrian → Pedestrian (connector 141)
- tag SC_UNION_SET = 'EntityObject' on the target end of EntityObject.miscObject → MiscObject (connector 140)
- tag SC_UNION_SET = 'EntityObject' on the target end of EntityObject.externalObjectReference → ExternalObjectReference (connector 361)
- stereotypes of Gear (class 271) := «XSDgroup»
- tag SC_UNION_SET = 'Gear' on the target end of Gear.manualGear → ManualGear (connector 297)
- tag SC_UNION_SET = 'Gear' on the target end of Gear.automaticGear → AutomaticGear (connector 255)
- stereotypes of OpenScenarioCategory (class 23) := «XSDgroup»
- tag SC_UNION_SET = 'OpenScenarioCategory' on the target end of OpenScenarioCategory.scenarioDefinition → ScenarioDefinition (connector 89)
- tag SC_UNION_SET = 'OpenScenarioCategory' on the target end of OpenScenarioCategory.catalogDefinition → CatalogDefinition (connector 200)
- tag SC_UNION_SET = 'OpenScenarioCategory' on the target end of OpenScenarioCategory.parameterValueDistributionDefinition → ParameterValueDistributionDefinition (connector 285)
- stereotypes of SteadyState (class 219) := «XSDgroup»
- tag SC_UNION_SET = 'SteadyState' on the target end of SteadyState.targetDistanceSteadyState → TargetDistanceSteadyState (connector 296)
- tag SC_UNION_SET = 'SteadyState' on the target end of SteadyState.targetTimeSteadyState → TargetTimeSteadyState (connector 298)
- stereotypes of StochasticDistributionType (class 188) := «XSDgroup»
- tag SC_UNION_SET = 'StochasticDistributionType' on the target end of StochasticDistributionType.probabilityDistributionSet → ProbabilityDistributionSet (connector 273)
- tag SC_UNION_SET = 'StochasticDistributionType' on the target end of StochasticDistributionType.normalDistribution → NormalDistribution (connector 276)
- tag SC_UNION_SET = 'StochasticDistributionType' on the target end of StochasticDistributionType.logNormalDistribution → LogNormalDistribution (connector 360)
- tag SC_UNION_SET = 'StochasticDistributionType' on the target end of StochasticDistributionType.uniformDistribution → UniformDistribution (connector 274)
- tag SC_UNION_SET = 'StochasticDistributionType' on the target end of StochasticDistributionType.poissonDistribution → PoissonDistribution (connector 277)
- tag SC_UNION_SET = 'StochasticDistributionType' on the target end of StochasticDistributionType.histogram → Histogram (connector 275)
- tag SC_UNION_SET = 'StochasticDistributionType' on the target end of StochasticDistributionType.userDefinedDistribution → UserDefinedDistribution (connector 362)

## OSC-3: «transient» is applied where every reader of the model finds it

These three associations are «transient», not mapped to the schema, and ASAM's generator leaves them out of it. EA records the stereotype only in the connector's own column, not in its list of applied stereotypes, which is what EA's API reports and what the export reads; so the export and everything built on it treat the associations as ordinary, and the SHACL requires `CatalogReference.ref`, rejecting every document with a `<CatalogReference>`. The stereotype is applied properly.

**Normative schema:** unchanged: ASAM's generator reads the column

- stereotypes of TrafficSignalControllerAction.phaseRef → Phase (connector 67) := «transient»
- stereotypes of TrafficSignalControllerCondition.phaseRef → Phase (connector 68) := «transient»
- stereotypes of CatalogReference.ref → CatalogElement (connector 189) := «transient»
