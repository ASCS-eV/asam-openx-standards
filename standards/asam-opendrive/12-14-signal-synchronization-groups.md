# ASAM Opendrive v1.9.0 — 12.14 Signal synchronization groups in junctions

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/12_junctions/12_14_signal_synchronization_groups.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 12.14 Signal synchronization groups in junctions

Multiple signal groups can be mapped to a signal synchronization group that consists of a list of signal controllers in a junction which can be synchronized (see  [Section 14.6, "Signal Controllers"](../14_signals/14_06_controllers.html#top-bb3b8324-47ba-4c80-aee7-a4a443cd0ef3)).
This mapping can be used for example in case an ASAM OpenSCENARIO `TrafficSignalControllerAction` is setting the semantic state for one signal group and afterwards syncing all other signal groups of that particular signal synchronization group to switch to the matching phase in their signal cycle.
For detailed definitions of terms specific to dynamic signals see  [Annex C, *Terms for dynamic signals (normative)*](../16_annexes/terms/top_ter_dynamic_signals.html#top-7028394a-a7a3-439b-8bc9-dbbd1b8506c8).
In future it might be beneficial to extend this to junction groups or to a more generic approach matching the synchronization group definition.

![img](../_images/00_images_reused/fig_junction.drawio.svg)

Figure 110. Example of a junction with 20 traffic lights mapped into six signal groups (IDs 42-47)

[Figure 110](#fig-b13ae64c-fb46-4223-bbae-645a0ecfad9a) shows a junction with 20 traffic lights mapped into six signal groups.
If controller ID `46` switches the signals in this signal group to semantic state `go`, one would like to automatically set all other signals within the junction to a matching phase according to their signal cycle.
For example signals controlled by controller ID `44` should be switched to semantic state `stop`.

Junction controllers are used to map signal groups respectively the controllers controlling the signal groups into a synchronization group within one junction.
A junction controller is described by `<controller>` elements within the `<junction>` element.

The @type attribute of control depends on the application and is not specified in ASAM OpenDRIVE.

**Elements in UML model**

**`<controller>` element**

In ASAM OpenDRIVE, controllers are represented by the `<controller>` element within the `<junction>` element.

```
UML class: t_junction_controller
XML tag:   <controller> (Multiplicity: 0..*)
```

Lists the controllers that should be grouped in a sychronization group (limited to that particular junction).

Table 84. Attributes of the <controller> element


| Name | Type | Use | Description |
| --- | --- | --- | --- |
| `id` | string | required | ID of the controller |
| `sequence` | nonNegativeInteger | optional | Sequence number (priority) of this controller with respect to other controllers in the same junction |
| `type` | string | optional | Type of control for this junction. Free text, depending on the application. |

**XML example**

* [UC\_Simple-X-Junction-TrafficLights.xodr](../_attachments/use_cases/UC_Simple-X-Junction-TrafficLights/UC_Simple-X-Junction-TrafficLights.xodr)

**Related topics**

* [Section 12.1, "Introduction to junctions"](12_01_introduction.html#top-ba9039b6-b319-4618-bbfb-5ad28a9c95c0)
* [Section 12.13, "Junction groups"](12_13_junction_groups.html#top-99e6f0a6-ad6b-4c5e-bace-622208adfc2f)
* [Section 14.6, "Signal Controllers"](../14_signals/14_06_controllers.html#top-bb3b8324-47ba-4c80-aee7-a4a443cd0ef3)