# ASAM Opendrive v1.9.0 — 11.2 Lane layers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/11_lanes/11_02_lane_layers.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 11.2 Lane layers

Lanes are part of a lane layer.
A lane layer can either be permanent or temporary.
Each road has exactly one layer of type "permanent" and may have up to one layer of type "temporary".
The permanent layer stretches across the complete length of a road, while the temporary layer might only be present in some sections.
No lane on the temporary lane layer should extend beyond the surface defined by the lanes on the permanent lane layer.
For t-coordinates, the sum of all lane widths plus lane offsets on the temporary lane layer shall not be greater than on the permanent lane layer.
Both layers share the same surface height level.

![img](../_images/11_lanes/lane_sway.png)

Figure 60. Road with two lane layers "permanent" (white markings) and "temporary" (yellow markings) in a roadworks setting

[Figure 60](#fig-8e54e01d-146a-4e0a-8e6c-f0ad6515b8c3) shows a road with a permanent and a temporary lane layer.
It is based on the example file xref:"Ex\_Motorway\_Roadworks\_Temporary\_Layer\_Lane\_offset.xodr" provided in the deliverables.
Each layer has multiple traffic lanes.
The temporary lanes take precedence over the permanent ones for driving.
On the right side, a section of the outside lane is inaccessible to traffic.
On the left side, a section of the inner lane is inaccessible to traffic going the direction defined for the permanent lane.
A temporary lane on top of it is accessible to traffic from the opposite direction.

|  |  |
| --- | --- |
|  | For the full example, see [Ex\_Motorway\_roadworks\_temporary\_layer\_lane\_offset.xodr](../_attachments/examples/Ex_Motorway_roadworks_temporary_layer_lane_offset/Ex_Motorway_roadworks_temporary_layer_lane_offset.xodr). |

The permanent lane layer specifies the underlying lane structure and applies to normal usage conditions.
The temporary layer adds additional lane structure and road markings with higher priority.
It modifies the road usage, i.e. the driving rules.
It does not modify the surface material properties, which are solely defined by the permanent layer.
The temporary layer’s lane markings lie on top of the permanent layer’s line markings.

A typical use case for a temporary lane layer are roadworks, where temporary lanes redirect traffic around the construction site.
Lanes of the permanent layer where access and the ability to drive are restricted may be marked with @roadworks=true.
An example would be a lane where access is physically blocked by beacon objects.

Both layers may have a different number of lanes and lane sections.
Lane sections on different layers do not have to start and end at the same road s-position unless their lanes are linked between the layers.
Lane linking between layers enables vehicles to drive from a permanent onto a temporary lane section and vice versa.
For more on lane sections and lane linking, see  [Section 11.4, "Lane sections"](11_04_lane_sections.html#top-e2c7cf98-db06-4a27-972a-0d165f87a867) and  [Section 11.6, "Lane linkage"](11_06_lane_link.html#top-26f830a9-2eba-4948-aac9-8015c5206efd).

**XML example**

![img](../_images/11_lanes/lane_multi_layer_example.png)

Figure 61. Example with lanes on the permanent and temporary lane layer

[Figure 61](#fig-56f432b4-c98c-4cc0-89b7-fb34de383caa) shows the example of a construction site with lanes on both the permanent and the temporary lane layer.
It is based on the example [Ex\_Lane\_MultiLaneLayer.xodr](../_attachments/examples/Ex_Lane_MultiLaneLayer/Ex_Lane_MultiLaneLayer.xodr).
Lanes on the permanent layer use white lines, lanes on the temporary layer use yellow lines.
The section at the bottom of the image is a road section with only lanes on the permanent layer.

The source code below is an abbreviated excerpt from the full example to illustrate the use of lane layers.
It contains the first section with lanes on both the permanent and the temporary layer.
It only contains a single section on both layers.

```
<lanes layer="permanent">
    <laneSection s="40.0">
        <center>
            <lane id="0" type="none" level="false">
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
        </center>
        <right>
            <lane id="-1" type="median" level="false">
                <link>
                    <predecessor id="-1" layer="permanent"/>
                    <successor id="-1" layer="permanent"/>
                    <successor id="-1" layer="temporary"/>
                </link>
                <width a="2.0" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
            <lane id="-2" type="border" level="false">
                <link>
                    <predecessor id="-2" layer="permanent"/>
                    <successor id="-2" layer="permanent"/>
                    <successor id="-2" layer="temporary"/>
                </link>
                <width a="0.75" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="solid" weight="bold" color="white" height="0.02"/>
            </lane>
            <lane id="-3" type="driving" level="false">
                <link>
                    <predecessor id="-3" layer="permanent"/>
                    <successor id="-3" layer="permanent"/>
                    <successor id="-3" layer="temporary"/>
                </link>
                <width a="3.75" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="broken" weight="standard" color="white" height="0.02"/>
            </lane>
            <lane id="-4" type="driving" level="false">
                <link>
                    <predecessor id="-4" layer="permanent"/>
                    <successor id="-4" layer="permanent"/>
                    <successor id="-4" layer="temporary"/>
                </link>
                <width a="3.75" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="solid" weight="bold" color="white" height="0.02"/>
            </lane>
            <lane id="-5" type="border" level="false">
                <link>
                    <predecessor id="-5" layer="permanent"/>
                    <successor id="-5" layer="permanent"/>
                    <successor id="-5" layer="temporary"/>
                </link>
                <width a="0.75" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
            <lane id="-6" type="stop" level="false">
                <link>
                    <predecessor id="-6" layer="permanent"/>
                    <successor id="-6" layer="permanent"/>
                    <successor id="-6" layer="temporary"/>
                </link>
                <width a="3.0" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
            <lane id="-7" type="shoulder" level="false">
                <link>
                    <predecessor id="-7" layer="permanent"/>
                    <successor id="-7" layer="permanent"/>
                    <successor id="-7" layer="temporary"/>
                </link>
                <width a="1.5" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
        </right>
    </laneSection>
<lanes layer="temporary">
    <laneSection s="40.0">
        <center>
            <lane id="0" type="none" level="false">
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
        </center>
        <right>
            <lane id="-1" type="median" level="false">
                <link>
                    <predecessor id="-1" layer="temporary"/>
                    <successor id="-1" layer="temporary"/>
                </link>
                <width a="2.0" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
            <lane id="-2" type="border" level="false">
                <link>
                    <predecessor id="-2" layer="temporary"/>
                    <successor id="-2" layer="temporary"/>
                </link>
                <width a="0.75" b="0.0" c="0.011625" d="-0.0003875" sOffset="0"/>
                <roadMark sOffset="0" type="solid" weight="bold" color="yellow" height="0.02"/>
            </lane>
            <lane id="-3" type="driving" level="false">
                <link>
                    <predecessor id="-3" layer="temporary"/>
                    <successor id="-3" layer="temporary"/>
                </link>
                <width a="3.75" b="0.0" c="-0.001875" d="6.25e-05" sOffset="0"/>
                <roadMark sOffset="0" type="broken" weight="standard" color="yellow" height="0.02"/>
            </lane>
            <lane id="-4" type="driving" level="false">
                <link>
                    <predecessor id="-4" layer="temporary"/>
                    <successor id="-4" layer="temporary"/>
                </link>
                <width a="3.75" b="0.0" c="-0.001875" d="6.25e-05" sOffset="0"/>
                <roadMark sOffset="0" type="solid" weight="bold" color="yellow" height="0.02"/>
            </lane>
            <lane id="-5" type="border" level="false">
                <link>
                    <predecessor id="-5" layer="temporary"/>
                    <successor id="-5" layer="temporary"/>
                </link>
                <width a="0.75" b="0.0" c="-0.001875" d="6.25e-05" sOffset="0"/>
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
            <lane id="-6" type="stop" level="false">
                <link>
                    <predecessor id="-6" layer="temporary"/>
                    <successor id="-6" layer="temporary"/>
                </link>
                <width a="3.0" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
            <lane id="-7" type="shoulder" level="false">
                <link>
                    <predecessor id="-7" layer="temporary"/>
                    <successor id="-7" layer="temporary"/>
                </link>
                <width a="1.5" b="0.0" c="0.0" d="0.0" sOffset="0"/>
                <roadMark sOffset="0" type="none" weight="standard" color="standard" height="0.02"/>
            </lane>
        </right>
    </laneSection>
```

|  |  |
| --- | --- |
|  | For the full example, see [Ex\_Lane\_MultiLaneLayer.xodr](../_attachments/examples/Ex_Lane_MultiLaneLayer/Ex_Lane_MultiLaneLayer.xodr). |

**Rules**

The following rules apply to the use of lane layers:

* Lane layers may have as many lanes as needed.

* [asam.net:xodr:1.9.0:road.lane.layer.layer\_mandatory\_permanent](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-layer-layer-mandatory-permanent): There shall be at least one lane in the "permanent" layer at each s-coordinate of the road.

* [asam.net:xodr:1.9.0:road.lane.layer.layer\_limits](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-layer-layer-limits): Each road shall have exactly one "permanent" and up to one "temporary" lane layer.

* [asam.net:xodr:1.9.0:road.lane.layer.center\_lane\_permanent](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-layer-center-lane-permanent): Each lane section in the permanent layer shall have a center lane.

* [asam.net:xodr:1.9.0:road.lane.layer.length\_only\_temporary](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-layer-length-only-temporary): Lanes in the permanent lane layer shall not use the attribute @length.

* Omitting @layer shall default to @layer="permanent".

* [asam.net:xodr:1.9.0:road.lane.layer.lane\_phys\_attr\_temporary](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-layer-lane-phys-attr-temporary): Lanes in the "temporary" layer shall not contain `<height>` or `<material>` elements.
  The height and material is instead determined by the permanent layer.

* [asam.net:xodr:1.9.0:road.lane.layer.lane\_group\_width\_temporary](../16_annexes/map_rules.html#asam-net-xodr-1-9-0-road-lane-layer-lane-group-width-temporary): For each lane group, the sum of all lane widths and lane offsets on the temporary lane layer shall not be greater than the sum of lane widths and lane offsets on the permanent lane layer.

**Related topics**

* [Section 11.1, "Introduction to lanes"](11_01_introduction.html#top-9c2a8ffd-2bf4-4fa9-b861-0fbf9cd6817b)
* [Section 11.3, "Lane groups"](11_03_lane_groups.html#top-3c24733f-35b5-43ae-b1da-60920f47ad47)