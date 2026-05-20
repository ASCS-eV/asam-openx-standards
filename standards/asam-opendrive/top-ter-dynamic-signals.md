# ASAM OpenDRIVE® v1.9.0 — Annex C: Terms for dynamic signals (normative)

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/16_annexes/terms/top_ter_dynamic_signals.html
> **Standard**: ASAM OpenDRIVE® v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# Annex C: Terms for dynamic signals (normative)

Signal controller
:   A signal controller applies a signal cycle (see [signal cycle](#sec-fe178b76-4fb3-48c9-b19c-981b8b9a787f)) to a signal or a signal group (see [signal group](#sec-5dffe4c1-df1e-4cf7-b9a4-b8eac9a3683e)).

Signal cycle
:   A signal cycle is an ordered list of phases (see [signal phase](#sec-a435dfb3-ccb8-4235-ba38-01e74ef56d0e)) for one dynamic signal.

    A signal cycle starts with the first phase, which is active for the specified duration and switches then to the next phase.
    The signal cycle is looped, so when the end of the last phase is reached, it continues with the start of the first phase again.
    The duration of a cycle is the sum of the durations of its phases.

    As the signal cycle is part of the dynamic content, it should be specified in ASAM OpenSCENARIO and set in standard-specific elements:

    | Standard | Element |
    | --- | --- |
    | ASAM OpenSCENARIO XML | `TrafficSignalController` |
    | ASAM OpenSCENARIO DSL | `traffic_light_controller` |

Signal group
:   Each dynamic signal needs to be in exactly one signal group.

    Dynamic signals with exactly the same signal cycle (see [signal cycle](#sec-fe178b76-4fb3-48c9-b19c-981b8b9a787f)) can, but are not required to be grouped into a signal group.
    Two signal cycles are considered the same if they have the same phases (see [signal phase](#sec-a435dfb3-ccb8-4235-ba38-01e74ef56d0e)) in the same order and therefore also have the same duration.
    This means a signal group can, but is not required to have more than one element.
    This allows a signal cycle to be specified only once for the whole signal group.
    For most use cases this grouping will be done within one intersection.

    As the grouping is part of the static content, the signal group should be specified in ASAM OpenDRIVE® via the `<controller>` element.

Signal phase
:   A phase of a dynamic signal is the semantic state (see [signal state](#sec-ca1171ec-384a-4d5a-b377-82e719da237b)) in combination with a (possibly infinite) duration, which specifies how long this semantic state is active.
    This term is not to be confused with the English civil engineering term *stage* or the German term *Phase*.

    As the signal phase is part of the dynamic content, it should be specified in ASAM OpenSCENARIO and set in standard-specific elements:

    | Standard | Element |
    | --- | --- |
    | ASAM OpenSCENARIO XML | `Phase` |
    | ASAM OpenSCENARIO DSL | `traffic_light_phase` |

    Possible phases could be: `go` for 5 seconds, `caution` for infinite seconds, `stop` for 20 seconds etc.

Signal state
:   A state of a dynamic signal is the combination of the semantic and the observable state of a signal.

    The semantic state of a signal refers to the rules imposed on traffic obeying the signal at a given point in time.
    For example, a signal may be in a semantic `stop` state meaning that obeying traffic must not pass a certain stop line associated with the signal,
    or it may be in a semantic `caution` state meaning that obeying traffic may pass the signal but must yield to other traffic and pedestrians as it does so.

    The observable state is the physically observable aspects of the state of the signal such as the light bulb state for a traffic light, sound being produced, or messages being broadcast over a vehicle-to-infrastructure communication network.
    The observable state of a dynamic signal is usually determined by its semantic state, but can be changed independently of it as well.
    For example, in British Columbia the semantic state `go` can either result in a flashing green light bulb (if the traffic light is pedestrian-controlled) or in a solid green light bulb.
    Other examples are the modelling of broken traffic light bulbs (no color at all), or old traffic light bulbs that show different colors than expected (like orange instead of red for the semantic state `stop`).

    The set of possible observable states for a given signal must be inferred from the `type` and `subtype` of the signal. Possible observable states may include but are not limited to `on`, `off`, `flashing` for single-bulb traffic lights and `red`, `amber`, `green` for typical traffic lights having three light bulbs

    As the signal state is part of the dynamic content, it should be specified in ASAM OpenSCENARIO.
    The semantic state is set together with its duration using standard-specific elements:

    | Standard | Element for semantic state |
    | --- | --- |
    | ASAM OpenSCENARIO XML | `TrafficSignalState` |
    | ASAM OpenSCENARIO DSL | `semantic_traffic_light_state` |

    The observable state is also set using standard-specific elements:

    | Standard | Element for observable state |
    | --- | --- |
    | ASAM OpenSCENARIO XML | `TrafficSignalGroupState` |
    | ASAM OpenSCENARIO DSL | `semantic_traffic_light_state` |

Signal synchronization group
:   Multiple signal groups (see [signal group](#sec-5dffe4c1-df1e-4cf7-b9a4-b8eac9a3683e)) which should be kept synchronized and whose signal cycles (see [signal cycle](#sec-fe178b76-4fb3-48c9-b19c-981b8b9a787f)) have the same finite duration can, but are not required to be mapped to a synchronization group.
    This mapping can be used to indicate that whenever the phase of one signal group is set - by an ASAM OpenSCENARIO XML `TrafficSignalControllerAction`, an ASAM OpenSCENARIO® DSL `set_group_semantic_state` , or otherwise - the other signal groups in that synchronization group should be set to the corresponding position in their signal cycles.

    As the grouping is part of the static content this should be specified in ASAM OpenDRIVE®.
    Currently there is the t\_junction\_controller in ASAM OpenDRIVE® to set the grouping of signal groups.