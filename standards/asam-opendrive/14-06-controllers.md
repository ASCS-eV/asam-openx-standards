# ASAM OpenDRIVE® v1.9.0 — 14.6 Signal Controllers

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/14_signals/14_06_controllers.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 14.6 Signal Controllers

A signal controller applies a signal cycle to a signal group.
The mapping of dynamic signals to a signal group is done in `<controller>`.
The ID of the referenced signal is stored in the `<control>` element within the `<controller>` element.
Unlike signal dependency, signal controllers are high-level elements that do not depend on other signals.

Dynamic content like the signal cycle itself is specified outside of this standard, for example, in ASAM OpenSCENARIO.
For detailed definitions of terms specific to dynamic signals see  [Annex C, *Terms for dynamic signals (normative)*](../16_annexes/terms/top_ter_dynamic_signals.html#top-7028394a-a7a3-439b-8bc9-dbbd1b8506c8).

![img](../_images/00_images_reused/fig_junction.drawio.svg)

Figure 135. Example of a junction with 20 traffic lights mapped into six signal groups (IDs 42-47)

[Figure 135](#fig-2bb60c87-ffac-4a05-b217-42541fffe1bf) shows an example of an X-Junction with six traffic signals for vehicles, six traffic signals for trams, and eight traffic signals for pedestrians.
These are grouped into six signal groups that are controlled by controller with ID `42` to `47`.

![img](../_images/14_signals/fig_signal_program.svg)

Figure 136. Example of a signal program that defines the signal cycles for the signal groups

[Figure 136](#fig-df589d01-586d-422f-9bf6-04f135d65ced) shows an example of an appropriate signal program for signals controlled by controller with ID `42` and `44`.

**Elements in UML model**

**`<controller>` element**

In ASAM OpenDRIVE®, controllers are represented by the `<controller>` element within the `<OpenDRIVE>` element.

```
UML class: t_controller
XML tag:   <controller> (Multiplicity: 0..*)
```

Controllers provide a signal program for a traffic signal or a signal group.
The mapping of traffic signals to a signal group is done in t\_controller.
Dynamic content like the signal program itself is specified outside of this standard (i.e.
in OpenSCENARIO).

Table 128. Attributes of the <controller> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | Unique ID within database |
| `name` | string | optional | Name of the controller. May be chosen freely. |
| `sequence` | nonNegativeInteger | optional | Sequence number (priority) of this controller with respect to other controllers of same logical level |

![img](../_images/uml_class_diagrams/EAID_B88092E5_0933_4514_984D_54D2E961692B.png)

Figure 137. UML class diagram of the Controller class

[Figure 137](#fig-c538a48d-acd0-4012-8d59-47108f27b8b4) shows the UML class diagram of the ASAM OpenDRIVE® Controller class.

**`<control>` element**

In ASAM OpenDRIVE®, controlled signals are represented by the `<control>` element within the `<controller>` element.

```
UML class: t_controller_control
XML tag:   <control> (Multiplicity: 1..*)
```

Provides information about a single signal within a signal group controlled by the corresponding controller.

Table 129. Attributes of the <control> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `signalId` | string | required | ID of the controlled signal |
| `type` | string | optional | Type of control.  Free Text, depends on the application. |

**XML example**

* [UC\_Simple-X-Junction-TrafficLights.xodr](../_attachments/use_cases/UC_Simple-X-Junction-TrafficLights/UC_Simple-X-Junction-TrafficLights.xodr)

**Rules**

The following rules apply to controllers:

* [asam.net:xodr:1.7.0:road.signal.controller.valid\_for\_signals](../16_annexes/map_rules.html#asam-net-xodr-1-7-0-road-signal-controller-valid-for-signals): Controllers shall be valid for one or more signals.

**Related topics**

* [Section 14.1, "Introduction to signals"](14_01_introduction.html#top-6a25938a-15c5-4eff-bde6-d82d3caf279a)
* [Section 14.3, "Signal dependency"](14_03_signal_dependency.html#top-f4d8bdcc-3f58-454d-b14e-801a880d9c41)
* [Section 12.14, "Signal synchronization groups in junctions"](../12_junctions/12_14_signal_synchronization_groups.html#top-add49732-8747-40b6-93b0-1b3ff20afeb9)