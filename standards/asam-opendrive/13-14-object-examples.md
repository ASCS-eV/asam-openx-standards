# ASAM OpenDRIVE® v1.9.0 — 13.14 Combinations of elements and attributes for object types

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/13_objects/13_14_object_examples.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 13.14 Combinations of elements and attributes for object types

## 13.14.1 barrier

A barrier is a continuous object, which cannot be passed.

Table 110. Combinations of attributes and elements for `<object type="barrier">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<skeleton>` `<marking>` `<border>` `<material>` `<surface>` `<parkingSpace>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| barrier | hedge | common hedge made out of vegetation and bushes without gaps | not allowed | not recommended | recommended, size is defined in `<repeat>` | not allowed | not allowed | not allowed | not allowed |
| guardRail | metal guard rail along the side of the road (without the vertical poles) |
| jerseyBarrier | lower wall mostly made out of concrete to separate driving lanes |
| wall | higher wall out of concrete, bricks, stones …​ |
| railing | any kind of railing along the roadside |
| fence | metal or wooden fence |
| noiseProtections | higher wall for noise protection |
| other | all other barrier objects subtypes that do not fit into current categories |

**XML example**

```
<object type="barrier"
        subtype="guardRail"
        name="guardRail"
        id="4000203"
        s="7.4615629425e+01"
        t="-1.4796332056e+01"
        zOffset="-0.328297280316"
        validLength="78.2913194973"
        orientation="none">
    <repeat s="7.4615629425e+01"
            length="2.2248725912e+00"
            distance="0.0000000000e+00"
            tStart="-1.4796332056e+01"
            tEnd="-1.4797490375e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="-3.2829728032e-01"
            zOffsetEnd="-2.0316925494e-01" />
    <repeat s="7.6840502016e+01"
            length="1.9924939859e+00"
            distance="0.0000000000e+00"
            tStart="-1.4797490375e+01"
            tEnd="-1.4799675135e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="-2.0316925494e-01"
            zOffsetEnd="-9.9028462309e-02" />
    <repeat s="7.8832996002e+01"
            length="3.3472807403e+00"
            distance="0.0000000000e+00"
            tStart="-1.4799675135e+01"
            tEnd="-1.4796827566e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="-9.9028462309e-02"
            zOffsetEnd="5.4099928501e-02" />
    <repeat s="8.2180276743e+01"
            length="2.0283762167e+00"
            distance="0.0000000000e+00"
            tStart="-1.4796827566e+01"
            tEnd="-1.4790365646e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="5.4099928501e-02"
            zOffsetEnd="1.2659902980e-01" />
    <repeat s="8.4208652959e+01"
            length="8.1152058043e+00"
            distance="0.0000000000e+00"
            tStart="-1.4790365646e+01"
            tEnd="-1.4802913672e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="1.2659902980e-01"
            zOffsetEnd="1.7346901590e-01" />
    <repeat s="9.2323858764e+01"
            length="8.1137326328e+00"
            distance="0.0000000000e+00"
            tStart="-1.4802913672e+01"
            tEnd="-1.4932009665e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="1.7346901590e-01"
            zOffsetEnd="1.8665641186e-01" />
    <repeat s="1.0043759140e+02"
            length="8.1135361793e+00"
            distance="0.0000000000e+00"
            tStart="-1.4932009665e+01"
            tEnd="-1.4813360696e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="1.8665641186e-01"
            zOffsetEnd="1.7471050187e-01" />
    <repeat s="1.0855112758e+02"
            length="8.1144815334e+00"
            distance="0.0000000000e+00"
            tStart="-1.4813360696e+01"
            tEnd="-1.4794688826e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="1.7471050187e-01"
            zOffsetEnd="1.6260260750e-01" />
     <repeat s="1.1666560911e+02"
            length="8.1145989742e+00"
            distance="0.0000000000e+00"
            tStart="-1.4794688826e+01"
            tEnd="-1.4789712834e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="1.6260260750e-01"
            zOffsetEnd="1.5562310985e-01" />
     <repeat s="1.2478020808e+02"
            length="8.1144823549e+00"
            distance="0.0000000000e+00"
            tStart="-1.4789712834e+01"
            tEnd="-1.4785309018e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="1.5562310985e-01"
            zOffsetEnd="1.4723730991e-01" />
     <repeat s="1.3289469044e+02"
            length="8.1147823670e+00"
            distance="0.0000000000e+00"
            tStart="-1.4785309018e+01"
            tEnd="-1.4796174945e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="1.4723730991e-01"
            zOffsetEnd="1.7293727744e-01" />
     <repeat s="1.4100947281e+02"
            length="2.9774693217e+00"
            distance="0.0000000000e+00"
            tStart="-1.4796174945e+01"
            tEnd="-1.4801054064e+01"
            widthStart="1.0000000000e-01"
            widthEnd="1.0000000000e-01"
            heightStart="3.0000000000e-01"
            heightEnd="3.0000000000e-01"
            zOffsetStart="1.7293727744e-01"
            zOffsetEnd="1.9761954152e-01" />
</object>
```

## 13.14.2 building

A building is a closed object, which cannot be passed.

Table 111. Combinations of attributes and elements for <object type="building">


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<skeleton>` `<marking>` `<border>` `<material>` `<surface>` `<parkingSpace>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building | building | regular building like a house or office | optional | recommended | not allowed | optional | optional, default value for @closed="true" | not allowed | not allowed |
| busStop | bus stop with little roof and sign |
| tollBooth | small building with a barrier to collect tolls or charges |
| other | all other building objects subtypes that do not fit into current categories |

**XML example**

```
<object type="building"
        subType="building"
        name="house"
        id="0"
        s="2.4028125000000038e+01"
        t="1.2802136334240046e+01"
        zOffset="4.9999999999998934e-03"
        orientation="none"
        length="1.1300000000000001e+01"
        width="9.9900000000000002e+00"
        height="1.2230000000000000e+01"
        hdg="2.6413812899682183e+00"
        pitch="0.0000000000000000e+00"
        roll="0.0000000000000000e+00">
</object>
```

## 13.14.3 crosswalk

A crosswalk is an object on the road that can be passed.
It is recommended to be defined as `<crossPath>` within a junction for pedestrian/bicycle simulation.
If the crosswalk is defined as an object only, it will not be used for pedestrian/bicycle simulation.

Table 112. Combinations of attributes and elements for <object type="crosswalk">


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<marking>` `<surface>` `<material>` | `<skeleton>` `<border>` `<parkingSpace>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| crosswalk | pedestrian | pedestrian crosswalk without zebra markings | not allowed | mandatory | not allowed | optional | optional, default value for @closed="true" | not allowed | optional | not allowed |
| bicycle | bicycle crossing, in Germany normally with red paint | optional |
| zebra | zebra crossing | optional |
| virtual | invisible crosswalk | not recommended |
| other | all other crosswalk objects subtypes that do not fit into current categories | optional |

**XML example**

```
<object type="crosswalk"
        id="10"
        s="10.0"
        t="0.0"
        zOffset="0.0"
        orientation="none"
        length="10.0"
        width="7.0"
        hdg="0.0"
        pitch="0.0"
        roll="0.0">
    <outlines>
        <outline id="0" closed="true">
            <cornerRoad s="5.0" t="3.5" dz="0.0" height="0.0" id="0"/>
            <cornerRoad s="8.0" t="-3.5" dz="0.0" height="0.0" id="1"/>
            <cornerRoad s="12.0" t="-3.5" dz="0.0" height="0.0" id="2"/>
            <cornerRoad s="15.0" t="3.5" dz="0.0" height="0.0" id="3"/>
        </outline>
    </outlines>
    <markings>
        <marking width="0.1"
                 color="white"
                 zOffset="0.005"
                 spaceLength ="0.05"
                 lineLength ="0.2"
                 startOffset="0.0"
                 stopOffset="0.0">
            <cornerReference id="0"/>
            <cornerReference id="1"/>
        </marking>
        <marking width="0.1"
                 color="white"
                 zOffset="0.005"
                 spaceLength ="0.05"
                 lineLength ="0.2"
                 startOffset="0.0"
                 stopOffset="0.0">
            <cornerReference id="2"/>
            <cornerReference id="3"/>
        </marking>
    </markings>
</object>
```

## 13.14.4 gantry

A gantry is an object above a road on which `<signals>` are placed.

Table 113. Combinations of attributes and elements for `<object type="gantry">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<skeleton>` | `<marking>` `<border>` `<material>` `<surface>` `<parkingSpace>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gantry | gantry | has poles on either side of lanes and an overhead construction between them | not allowed | mandatory, for the entire gantry | not allowed | optional | not recommended, default value for @closed="true" | not allowed | recommended, recommended to use `<polyline>`, of which first vertex and last vertex have @intersectionPoint="true" | not allowed |
| gantryHalf | has a pole on one side of the road and an overhead construction attached to it | recommended, recommended to use `<polyline>`, of which first vertex has an @intersectionPoint="true" |
| other | all other gantry objects subtypes that do not fit into current categories | recommended |

**XML example**

```
<object type="gantry"
        subtype="gantry"
        name="SignGantry"
        id="4000001"
        s="25.0"
        t="-3.0"
        zOffset="0.00"
        roll="0"
        pitch="0"
        validLength=""
        orientation="none"
        height="5.5"
        length="0.5"
        width="6.5"
        dynamic="no"
        hdg="0">
    <skeleton>
        <polyline id="1">
            <vertexRoad s="25.0"
                        t="0.0"
                        dz="0.0"
                        width="0.5"
                        length="0.5"
                        id="0"
                        intersectionPoint="true" />
            <vertexRoad s="25.0"
                        t="0.0"
                        dz="5.25"
                        width="0.5"
                        length="0.5"
                        id="1" />
            <vertexRoad s="25.0"
                        t="-6.0"
                        dz="5.25"
                        width="0.5"
                        length="0.5"
                        id="2" />
            <vertexRoad s="25.0"
                        t="-6.0"
                        dz="0.0"
                        width="0.5"
                        length="0.5"
                        id="3"
                        intersectionPoint="true" />
        </polyline>
    </skeleton>
</object>
```

## 13.14.5 obstacle

An obstacle is an object on or beside the road that cannot be passed.

Table 114. Combinations of attributes and elements for `<object type="obstacle">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<skeleton>` `<marking>` `<border>` `<material>` `<surface>` `<parkingSpace>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| obstacle | advertisingColumn |  | either or | | not allowed | optional | not recommended, default value for @closed="true" | not allowed | not allowed |
| art |  |
| seating |  |
| picknick |  |
| box |  |
| phonebooth |  |
| chargingStation |  |
| distributionBox | for example, electrical, communication |
| crashBox |  |
| dumpster |  |
| dustbin |  |
| fountain |  |
| gritContainer |  |
| hydrant |  |
| parkingMeter |  |
| pillar | for example, bridge pillars |
| plantPot |  |
| postBox |  |
| railing | for example, bicycle stand, handrail |
| rock |  |
| roadBlockage |  |
| wall |  |
| fence |  |
| other | all other obstacle objects subtypes that do not fit into current categories |

**XML example**

```
<object type="obstacle"
        subType="hydrant"
        name="GermanHydrant"
        id="1"
        s="8.3817187499999548e+01"
        t="-4.6359023698365620e+00"
        zOffset="0.0000000000000000e+00"
        orientation="none"
        radius="1.500000000000000e-01"
        height="1.2520000000000000e+00"
        hdg="0.0000000000000000e+00"
        pitch="0.0000000000000000e+00"
        roll="0.0000000000000000e+00">
</object>
```

## 13.14.6 parkingSpace

A parkingSpace is an object on a lane on which vehicles are parked.

Table 115. Combinations of attributes and elements for `<object type="parkingSpace">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<parkingSpace>` `<material>` `<marking>` `<surface>` | `<skeleton>` `<border>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| parkingSpace | openSpace | typically outdoors, no limit to the top | not allowed | mandatory | not allowed | optional | optional, default value for @closed="true" | not allowed | optional | not allowed |
| closedSpace | typically indoors, limit to the top for example, inside a building |
| other | all other parkingSpace objects subtypes that do not fit into current categories |

**XML example**

```
<object type="parkingSpace"
        subtype="openSpace"
        name="parkingSpace_50deg"
        id="9"
        s="1.5e+01" t="-6.0e+00"
        zOffset="0.0"
        orientation="+"
        length="6.04e+00"
        width="2.5e+00"
        height="0.0"
        hdg="5.41052e+00"
        pitch="0.0"
        roll="0.0">
    <outlines>
        <outline id="51" closed="true">
            <cornerRoad s="11.60" t="-4.00" dz="0.001" height="0.0" id="0">
            <cornerRoad s="15.25" t="-8.15" dz="0.001" height="0.0" id="1">
            <cornerRoad s="18.39" t="-8.15" dz="0.001" height="0.0" id="2">
            <cornerRoad s="15.14" t="-4.00" dz="0.001" height="0.0" id="3">
        </outline>
    </outlines>
    <markings>
        <marking width="0.1"
                 color="white"
                 zOffset="0.005"
                 spaceLength="0.0"
                 lineLength="1.0"
                 startOffset="0.0"
                 stopOffset="0.0">
            <cornerReference id="0"/>
            <cornerReference id="1"/>
        </marking>
        <marking width="0.1"
                 color="white"
                 zOffset="0.005"
                 spaceLength="0.0"
                 lineLength="1.0"
                 startOffset="0.0"
                 stopOffset="0.0" >
            <cornerReference id="2"/>
            <cornerReference id="3"/>
        </marking>
    </markings>
    <parkingSpace access="all">
    </parkingSpace>
</object>
```

```
<object type="parkingSpace"
        subtype="closed"
        name="parkingGarage"
        id="10"
        s="3.0e+01"
        t="-6.0"
        zOffset="0.0"
        length="6.0"
        width="3.45"
        height="2.64"
        hdg="0.0"
        roll="0.0"
        pitch="0.0"
        orientation="+">
    <outlines>
        <outline id="53" fillType="concrete" outer="false">
            <cornerLocal v="-3.0" u="-1.43" z="0.0" height="2.11" id="0">
            <cornerLocal v="-3.0" u="1.43" z="0.0" height="2.11" id="1">
            <cornerLocal v="2.705" u="1.43" z="0.0" height="2.11" id="2">
            <cornerLocal v="2.705" u="-1.43" z="0.0" height="2.11" id="3">
        </outline>
    </outlines>
    <parkingSpace access="residents">
    </parkingSpace>
</object>
```

## 13.14.7 pole

A pole is thin long object beside drivable lanes.

Table 116. Combinations of attributes and elements for `<object type="pole">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<skeleton>` | `<border>` `<parkingSpace>` `<material>` `<marking>` `<surface>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pole | emergencyCallBox |  | either or | | not allowed | optional | optional, default value for @closed="true" | not allowed | optional | not allowed |
| permanentDelineator |  | optional |
| bollard |  | optional |
| trafficSign | pole for Traffic Signs | optional |
| trafficLight | pole for trafficLight and trafficSign objects | recommended if it has an extrusion. Use `<polyline>`, of which first vertex has an @intersectionPoint="true". |
| powerPole | has power cables attached | optional |
| streetLamp | has a light source. Might also have trafficSigns or trafficLights attached to it. | recommended if it has an arm. Use `<polyline>`, of which first vertex has an @intersectionPoint="true". |
| windTurbine |  | optional |
| other | all other pole objects subtypes that do not fit into current categories | optional |

**XML example**

```
<object type="pole"
        subtype="emergencyCallBox"
        name="emergencyCallBoxGerman"
        id="4"
        s="1.1350690873e+02"
        t="-5.4331497312e+00"
        zOffset="0.000"
        validLength="0.0"
        hdg="0.000"
        orientation="none"
        height="1.800"
        radius="0.05"
        roll="0"
        pitch="0"
        dynamic="no">
</object>
```

## 13.14.8 roadMark

A roadMark object is painted on the road and can be passed.

Table 117. Combinations of attributes and elements for `<object type="roadMark">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<marking>` `<material>` `<surface>` | `<skeleton>` `<border>` `<parkingSpace>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| roadMark | arrowLeft |  | not allowed | mandatory | not allowed | optional | optional, default value for @closed="true" | not allowed | optional | not allowed |
| arrowLeftLeft |  | optional, default value for @closed="true" | not allowed |
| arrowLeftRight |  | optional, default value for @closed="true" | not allowed |
| arrowRight |  | optional, default value for @closed="true" | not allowed |
| arrowRightRight |  | optional, default value for @closed="true" | not allowed |
| arrowRightLeft |  | optional, default value for @closed="true" | not allowed |
| arrowStraight |  | optional, default value for @closed="true" | not allowed |
| arrowStraightLeft |  | optional, default value for @closed="true" | not allowed |
| arrowStraightRight |  | optional, default value for @closed="true" | not allowed |
| arrowStraightLeftRight |  | optional, default value for @closed="true" | not allowed |
| arrowMergeLeft |  | optional, default value for @closed="true" | not allowed |
| arrowMergeRight |  | optional, default value for @closed="true" | not allowed |
| signalLines | these are referenced by a signal | either or  optional, default value for @closed="true" | |
| text | for example, YIELD or 50, might be referenced by a signal | optional, default value for @closed="true" | not allowed |
| symbol | for example, Wheelchair or bicycle | optional, default value for @closed="true" | not allowed |
| paint |  | either or  optional, default value for @closed="true" | |
| area | for example, restricted area, keep clear area | optional, default value for @closed="true" | not allowed |
| other | all other roadMark objects subtypes that do not fit into current categories | optional, default value for @closed="true" | not allowed |

**XML example**

```
<object type="roadMark"
        subtype="arrowStraight"
        name="arrowStraightWhite"
        id="5"
        s="1.5856415945e+00"
        t="1.7853615772e+00"
        zOffset="0.000"
        orientation="none"
        hdg="0.000"
        length="7.373"
        width="0.552"
        roll="0"
        pitch="0"
        validLength="0"
        height="0"
        dynamic="no">
    <outline id="1" outer="true" closed="true" laneType="driving">
        <cornerLocal u="-3.6386" v="0.1123" z="0.0000" height="0.0000" id="0"/>
        <cornerLocal u="-3.6864" v="-0.1213" z="0.0000" height="0.0000" id="1"/>
        <cornerLocal u="0.8244" v="-0.0792" z="0.0000" height="0.0000" id="2"/>
        <cornerLocal u="0.8167" v="-0.2762" z="0.0000" height="0.0000" id="3"/>
        <cornerLocal u="3.6864" v="-0.0093" z="0.0000" height="0.0000" id="4"/>
        <cornerLocal u="0.8104" v="0.2762" z="0.0000" height="0.0000" id="5"/>
        <cornerLocal u="0.7872" v="0.0582" z="0.0000" height="0.0000" id="6"/>
        <cornerLocal u="-3.6386" v="0.1123" z="0.0000" height="0.0000" id="7"/>
    </outline>
    <material roadMarkColor="white"/>
    <validity fromLane="1" toLane="1"/>
</object>
```

## 13.14.9 roadSurface

A roadSurface object is on the road and can be passed.

Table 118. Combinations of attributes and elements for `<object type="roadSurface">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<material>` `<surface>` | `<skeleton>` `<border>` `<parkingSpace>` `<marking>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| roadSurface | manhole | mostly metal cover to access sewerage tunnels | either or | | not allowed | optional | optional, default value for @closed="true" | not allowed | optional | not allowed |
| pothole | road damage |
| patch | road damage that has been fixed |
| speedbump | mostly raised surface to prevent higher speeds |
| drainGutter | water drainage |
| other | all other roadSurface objects subtypes that do not fit into current categories |

**XML example**

```
<object type="roadSurfaceElement"
        subType="patch"
        name="Rd_Damage_Patch_22_CRG"
        id="2"
        s="3.1064163564293011e+01"
        t="1.6886219784199805e+00"
        zOffset="0.0000000000000000e+00"
        validLength="0.0000000000000000e+00"
        orientation="none"
        length="1.9179999999999999e+00"
        width="3.2229999999999999e+00"
        height="0.0000000000000000e+00"
        hdg="5.7401170550235827e+00"
        pitch="0.0000000000000000e+00"
        roll="0.0000000000000000e+00">
    <surface>
        <CRG file="Rd_Damage_Patch_22_Center.crg" hideRoadSurfaceCRG="true" zScale="1"/>
    </surface>
</object>
```

## 13.14.10 trafficIsland

A trafficIsland object is on the road and should not be passed by vehicles.

Table 119. Combinations of attributes and elements for `<object type="trafficIsland">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<material>` `<border>` `<marking>` | `<skeleton>` `<surface>` `<parkingSpace>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| trafficIsland | island | typical traffic island with some curbstone, road marking | either or | | not allowed | not recommended | either or  recommended, default value for @closed="true" | | optional | not allowed |
| other | all other trafficIsland objects subtypes that do not fit into current categories |

**XML example**

```
<object type="trafficIsland"
        subtype="island"
        name="ExampleIsland"
        id="8"
        s="5.0000000000000441e+01"
        t="4.4053649617126212e-13"
        zOffset="0.0000000000000000e+00"
        orientation="none"
        length="5.0000000000000000e+00"
        width="1.0000000000000000e+00"
        height="1.0000000000000000e-01"
        hdg="0.0000000000000000e+00"
        pitch="0.0000000000000000e+00"
        roll="0.0000000000000000e+00">
    <outlines>
        <outline id="50" fillType="cobble" closed="true">
            <cornerRoad s="52.5" t="1.5" dz="0.0" height="0.1"/>
            <cornerRoad s="52.6" t="1.1" dz="0.0" height="0.1"/>
            <cornerRoad s="52.7" t="0.7" dz="0.0" height="0.1"/>
            <cornerRoad s="52.8" t="0.6" dz="0.0" height="0.1"/>
            <cornerRoad s="52.9" t="0.55" dz="0.0" height="0.1"/>
            <cornerRoad s="53.0" t="0.5" dz="0.0" height="0.1"/>
            <cornerRoad s="57.0" t="0.5" dz="0.0" height="0.1"/>
            <cornerRoad s="57.5" t="0.5" dz="0.0" height="0.01"/>
            <cornerRoad s="61.5" t="0.5" dz="0.0" height="0.01"/>
            <cornerRoad s="62.0" t="0.5" dz="0.0" height="0.1"/>
            <cornerRoad s="66.0" t="0.5" dz="0.0" height="0.1"/>
            <cornerRoad s="66.1" t="0.55" dz="0.0" height="0.1"/>
            <cornerRoad s="66.2" t="0.6" dz="0.0" height="0.1"/>
            <cornerRoad s="66.3" t="0.7" dz="0.0" height="0.1"/>
            <cornerRoad s="66.4" t="1.1" dz="0.0" height="0.1"/>
            <cornerRoad s="66.5" t="1.5" dz="0.0" height="0.1"/>
            <cornerRoad s="66.4" t="1.9" dz="0.0" height="0.1"/>
            <cornerRoad s="66.3" t="2.3" dz="0.0" height="0.1"/>
            <cornerRoad s="66.2" t="2.4" dz="0.0" height="0.1"/>
            <cornerRoad s="66.1" t="2.45" dz="0.0" height="0.1"/>
            <cornerRoad s="66.0" t="2.5" dz="0.0" height="0.1"/>
            <cornerRoad s="62.0" t="2.5" dz="0.0" height="0.1"/>
            <cornerRoad s="61.5" t="2.5" dz="0.0" height="0.01"/>
            <cornerRoad s="57.5" t="2.5" dz="0.0" height="0.01"/>
            <cornerRoad s="57.0" t="2.5" dz="0.0" height="0.1"/>
            <cornerRoad s="53.0" t="2.5" dz="0.0" height="0.1"/>
            <cornerRoad s="52.9" t="2.45" dz="0.0" height="0.1"/>
            <cornerRoad s="52.8" t="2.4" dz="0.0" height="0.1"/>
            <cornerRoad s="52.7" t="2.3" dz="0.0" height="0.1"/>
            <cornerRoad s="52.6" t="1.9" dz="0.0" height="0.1"/>
        </outline>
    </outlines>
    <borders>
        <border width="0.1" type="curb" outlineId="50" useCompleteOutline="true"/>
    </borders>
</object>
```

## 13.14.11 tree

A tree object is a single vegetational object with a trunk.

Table 120. Combinations of attributes and elements for `<object type="tree">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<skeleton>` | `<outline>` with `<curveLocal>` | `<material>` `<surface>` `<border>` `<parkingSpace>` `<marking>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tree | needle | needle tree | either or | | not allowed | optional | recommended, 2 entries, one for trunk, one for crown | | not allowed | not allowed |
| leaf | leaf tree |
| palm | palm tree |
| other | all other tree objects subtypes that do not fit into current categories |

**XML example**

```
<object type="tree"
        subtype="leaf"
        name="leafTree"
        id="6"
        s="9.3817187499999548e+01"
        t="-5.001023698365620e+00"
        zOffset="-1.00"
        roll="0"
        pitch="0"
        validLength=""
        orientation="none"
        height="7.50"
        length="4.00"
        width="4.00"
        dynamic="no"
        hdg="0">
    <skeleton>
        <polyline id="1">
            <vertexLocal u="-0.2" v="1.0" z="1.120" radius="0.15" id="0" intersectionPoint="true" />
            <vertexLocal u="-0.2" v="1.0" z="4.500" radius="0.12" id="1"/>
        </polyline>
    </skeleton>
    <outlines>
        <outline id="2" closed="true">
            <cornerLocal u="2.0" v="0.0" z="4.0" height="3.5" id="0"/>
            <cornerLocal u="1.0" v="2.0" z="4.0" height="3.5" id="1"/>
            <cornerLocal u="-1.0" v="2.0" z="4.0" height="3.5" id="2"/>
            <cornerLocal u="-2.0" v="0.0" z="4.0" height="3.5" id="3"/>
            <cornerLocal u="-1.0" v="-2.0" z="4.0" height="3.5" id="4"/>
            <cornerLocal u="-1.0" v="-2.0" z="4.0" height="3.5" id="5"/>
        <outline>
    </outlines>
</object>
```

## 13.14.12 vegetation

A vegetation object is a single vegetational object without a trunk or an area of vegetation.

Table 121. Combinations of attributes and elements for `<object type="vegetation">`


| @type | @subType | Description | Bounding volume using @radius and @height | Bounding volume using @width, @length and @height | `<repeat>` with @distance="0" | `<repeat>` with @distance>"0" | `<outline>` without `<curveLocal>` | `<outline>` with `<curveLocal>` | `<skeleton>` `<material>` `<surface>` `<border>` `<parkingSpace>` `<marking>` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vegetation | bush | a single bush | either or | | not allowed | optional | optional, default value for @closed="true" | not allowed | not allowed |
| forest | an area that is a forest |
| hedge | a single hedge |
| other | all other vegetation objects subtypes that do not fit into current categories |

**XML example**

```
<object type="vegetation"
        subType="bush"
        name="VegBush06"
        id="3"
        s="5.5223437499999534e+01"
        t="1.1123800966684282e+01"
        zOffset="-1.6500000000000004e-01"
        validLength="0.0000000000000000e+00"
        orientation="none"
        radius="1.5409999999999998e+00"
        height="3.1600000000000001e+00"
        hdg="0.0000000000000000e+00"
        pitch="0.0000000000000000e+00"
        roll="0.0000000000000000e+00">
</object>
```