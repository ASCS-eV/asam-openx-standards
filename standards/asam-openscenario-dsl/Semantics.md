# ASAM Openscenario Dsl v2.2.0 — 7.6 Semantics

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/language-reference/Semantics.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.6 Semantics

This chapter describes the behavioral semantics of scenarios, scenario modifiers, and actions of ASAM OpenSCENARIO.
ASAM OpenSCENARIO is a declarative and constraint-based language where a scenario model may not only define one concrete behavior, but a whole family of behaviors, with different possible values for parameters such as vehicle speeds, scenario durations, or environmental conditions.
Therefore, the semantics definition of ASAM OpenSCENARIO is also of a declarative nature and based on the notion of *trace acceptance* as explained in [Section 7.6.1, “Semantic foundations”](#sec-lc-semantics-semantic-foundations).

This standard does not provide any operational semantics, which means that it does not define how to choose the next step in the execution of an ASAM OpenSCENARIO model based on a given trace prefix.
Any operational semantics is valid as long as, given an ASAM OpenSCENARIO model, it produces traces that are accepted by that model according to the declarative semantics.
One reason for this standard not to provide any operational semantics is that different use cases may require different operational semantics.
In some cases, it may be sufficient to produce only one particular trace of the possible traces described by a given ASAM OpenSCENARIO model.
In other cases, it may be desired to produce a representative variety of the possible traces or to choose traces in a way that quickly reaches some coverage goal.

This section is structured as follows:

* The semantic foundations contain some preliminary definitions (see [Section 7.6.1, “Semantic foundations”](#sec-lc-semantics-semantic-foundations)).
* The following sections cover the semantics aspects of language concepts related to scenarios and actions (see [Section 7.6.2, “Scenarios”](#sec-lc-semantics-scenarios) and [Section 7.6.3, “Actions”](#sec-lc-semantics-actions)).

## 7.6.1 Semantic foundations

A *trace* is a timed behavior occurring in a traffic system, or a model thereof, such as a simulation.
An *ASAM OpenSCENARIO 2.0 model* (or *scenario model* in short) consists of a tree of composed scenarios and actions that specify a set of traces that it *accepts*.
All other traces are *rejected*.

![An illustration of a set of traces accepted by a specification](_images/lc_set-of-trances-accepted.svg)

Figure 4. An illustration of a set of traces accepted by an ASAM OpenSCENARIO model

[Figure 4](#fig-set-of-trances-accepted) shows a set of traces accepted by an ASAM OpenSCENARIO model as a tube.
The traces are single threads.
The traces are accepted if they are enclosed in the tube.
Traces not enclosed in the tube are rejected.

Trace acceptance is not related to passing or failing tests.
If an ASAM OpenSCENARIO model does not accept a trace, it means that the behavior is outside the scope of the ASAM OpenSCENARIO model.
Test criteria can only be evaluated for accepted traces, meaning, if the behaviors are within the scope of the ASAM OpenSCENARIO model.

An ASAM OpenSCENARIO model is *inconsistent* if the set of traces that it accepts is empty.
This can happen because of contradictions in constraints.
For example, requiring a car to drive faster than 50 km/h and slower than 50 km/h at the same time.
In a test setting, it can also happen that a vehicle under test causes a trace to be rejected.
That is, because the vehicle under test is uncontrollable from the perspective of the test system, it may force the traffic system into a state that violates constraints of the ASAM OpenSCENARIO model.
Moreover, the satisfiability of an ASAM OpenSCENARIO model also depends on particular driver models and physics models that are combined with the ASAM OpenSCENARIO model and influence how the traffic system objects behave.

The following chapters contain more precise definitions of some key concepts.

### 7.6.1.1 Actor system

An ASAM OpenSCENARIO model defines a possible system of actor objects, which can be vehicles, other moving objects, or also static or virtual objects.
This set of actor objects is called the *actor system* or *traffic system*.
Each actor object has a set of *fields* as defined by its *type* definition.
A field has a *type* that specifies a domain of possible values.
Domains can be discrete (such as int or enum values) or continuous (real-valued, such as speed or acceleration).
Domains can also be compound types (see [Section 7.3.5, "Compound types"](types.html#sec-lc-compound-types)), such as structs or actor types.

### 7.6.1.2 State

The *state* of an actor system is an actor system with a *valuation* of the actor objects' fields.
A valuation is a mapping for each field to a value from the domain defined by the field’s type.

\(\theta(o, \rho, t) = v\) is the valuation of the field \(\rho\) of the actor object \(o\) at time \(t\).

### 7.6.1.3 Trace

A *trace* \(\pi\) is a continuous-time sequence of actor system states.
\(\pi(t)\) identifies the actor system state at time \(t\), where \(t\) is a real number, meaning that \(\pi\) is a function \(\pi: \mathbb{R}\_{\geq 0} \rightarrow S\) where \(S\) is the set of states.
Traces can have arbitrary lengths but are always finite.

All states in a trace share the same actor system and only the valuations of their fields change over time.

Notation:

* \(\pi[t\_a,t\_b]\) is the subtrace of a trace \(\pi\) from the closed interval starting at time \(t\_a\) and ending at time \(t\_b\), that is, including the states at \(t\_a\) and \(t\_b\).

### 7.6.1.4 Behavior invocation tree

An ASAM OpenSCENARIO model has one main scenario that can *invoke* one or more other *behaviors* (a *behavior* being either a scenario or an action).
Each invoked scenario has a scenario type that defines how, again, that scenario invokes other behaviors.
Actions are atomic behaviors, meaning that they are not composed of other behaviors (from the perspective of an ASAM OpenSCENARIO model).
The scenario invocation relationships give rise to a *behavior invocation tree* that is defined by the ASAM OpenSCENARIO model, where the root is the main scenario, the leaves are action invocations, and intermediate nodes are scenario invocations.

### 7.6.1.5 Behaviors versus behavior invocations

The concepts *scenario* and *scenario invocation* relate as follows:

* A *scenario* (also *scenario type* or *scenario declaration*) describes a set of possible behaviors (traces) involving some set of actor objects in some actor systems.
* A *scenario invocation* happens when a scenario refers to another scenario as part of its behavior definition.

When invoking a scenario, the invoking (parent) scenario may specify additional constraints, especially for which actor objects the invoked (child) scenario must apply, by constraining how fields of the invoked scenario may *bind* to actor objects in an actor system.
Moreover, the invoking scenario may specify at what time and for which duration the invoked scenario shall apply.
For example, a scenario defining a certain choreography of vehicle movements may invoke an `overtaking` scenario and specify which vehicle shall overtake which other vehicle, possibly also constraining the time and duration of this maneuver, the speeds of the vehicles, and so on.
Therefore, semantically, a *scenario invocation* describes a subset of the possible behaviors described by its scenario type; especially a *scenario invocation* refines when these behaviors shall occur.

![An illustration of how the set of traces accepted by a scenario is a subset of the composition of the traces accepted by the scenario invocations](_images/lc_scenario-type-and-invocation.svg)

Figure 5. An illustration of how the set of traces accepted by a scenario is a subset of the composition of the traces accepted by the scenario invocations, which themselves are subsets of the traces accepted by their type scenario.

[Figure 5](#fig-scenario-type-and-invocation) shows how the set of traces accepted by a scenario \(Sc\_0\) is a subset of the composition of the traces accepted by the scenario invocations \(sc\_1:Sc\_1\) and \(sc\_2:Sc\_2\).
The traces accepted by the scenario invocations \(sc\_1:Sc\_1\) and \(sc\_2:Sc\_2\) are themselves subsets of the traces accepted by their type scenarios \(Sc\_1\) and \(Sc\_2\), reduced by constraints specified in the invoking scenario \(Sc\_0\).

The terminology of *scenario* and *scenario invocation* also maps to actions: *actions* and *action invocations* are distinguished in the same way as scenarios and scenario invocations, except that actions cannot invoke any other scenarios or actions, because actions are atomic.
As scenarios and actions are behaviors, we also call scenario invocations and action invocations more generally *behavior invocations*.

### 7.6.1.6 Accepting a trace

An ASAM OpenSCENARIO model only accepts a trace if its main scenario also accepts the trace.
A trace is an element of the possible behaviors described by its main scenario.
This depends on, for example, whether the time and value constraints formulated by the scenario are satisfied by the trace and whether, recursively, all behavior invocations accept subtraces of the given trace.

The next sections contain a more detailed definition of the different conditions for when a *scenario* accepts a given trace.

## 7.6.2 Scenarios

A scenario describes the behavior of one or several actors in a traffic system.
This chapter is divided into the following parts:

* [Composition operators](#sec-lc-semantics-composition-operators)
* [Scenario fields and bindings](#sec-lc-semantics-scenario-fields-and-bindings)
* [Scenario constraints](#sec-lc-semantics-scenario-constraints)
* [Time constraints](#sec-lc-semantics-time-constraints)
* [Events](#sec-lc-semantics-events)

Each section adds necessary conditions for trace acceptance.

For more information about scenarios in the context of ASAM OpenSCENARIO, refer to the [Scenario](../conceptual-overview/key_terms.html#sec-global-terminology-scenario) definition.

### 7.6.2.1 Composition operators

A scenario invokes one or more behaviors (scenarios or actions) or directives using three composition operators.

* `serial`: The serial (sequential) composition of scenarios
* `parallel`: The parallel composition of scenarios
* `one_of`: The one-of composition of scenarios (at least one of a set of scenarios must hold)

In addition, a scenario can invoke a single scenario, action, or directive directly in the `do` section.

In the following subsections, the semantics of these three composition operators are defined.
The subsections also contain the semantics of the direct invocation.

The semantics is expressed in terms of conditions for trace acceptance.
For compositionality reasons, a definition of when a scenario accepts the following elements is required:

* A given trace \(\pi[t\_{start},t\_{end})\)
* A trace over a right-open time interval between the following times:

  + A start time \(t\_{start}\)
  + An end time \(t\_{end}\)

For formal definitions, the left-pointing triangle symbol \(\triangleleft\) is introduced.
This triangle symbol indicates that a scenario invokes another scenario or a composition of other scenarios.
For example, \(Sc\_0 \triangleleft b\_1:B\_1\) means that scenario \(Sc\_0\) specifies a direct invocation \(b\_1\) of the behavior (type) \(B\_1\); \(Sc\_0 \triangleleft \texttt{serial}(b\_1:B\_1, b\_2:B\_2)\) means that scenario \(Sc\_0\) specifies a serial composition of the behavior invocations \(b\_1:B\_1\) and \(b\_2:B\_2\).

In the following subsections, trace acceptance is defined for behaviors that are non-zero time.
That means that zero-time behaviors, for example, emit directives (that emit events), are excluded from the trace acceptance conditions defined in the following subsections.
However, the zero-time directives influence trace acceptance in other ways, and this is defined in their particular subsection in this chapter, see for example [Section 7.6.2.5.2, “Emit (event)”](#sec-lc-semantics-emit-event).

#### 7.6.2.1.1 Direct invocation

A scenario can invoke a single scenario or action directly in the `do` section.
The invocation can express specific required values or ranges of values for any of the scenario parameters. Details are shown in [Code 44](#code-lc-semantics-example-simple-behavior-invocation):

Code 44. Simple behavior invocation

```
scenario vehicle.accelerate:
    target_speed: speed
    do drive(duration: [2s..4s]) with:
        speed(speed: target_speed, at: end)
```

Here, the action `drive()` of the parent actor of this scenario is invoked with a speed modifier.
The parameter `duration` of the `drive` scenario is required to be between 2 and 4 seconds.
The `speed` modifier specifies a target speed to be reached at the end of the execution of the drive action invocation (which also is the end of this scenario).

A scenario
\(Sc\_0 \triangleleft b\_1:B\_1\)
(\(Sc\_0\) specifies a direct scenario invocation
\(b\_1:B\_1\))
accepts
a trace \(\pi[t\_a,t\_b)\) *only if* \(b\_1:B\_1\) accepts \(\pi[t\_a,t\_b)\).

#### 7.6.2.1.2 Serial composition

A scenario can invoke a series of two or more behaviors.
[Code 45](#code-lc-semantics-example-serial-operator) shows a scenario \(\texttt{two\_phases}\) that specifies two driving phases of a vehicle:

* The first phase (phase1) starts with the vehicle at a standstill (speed = 0 kph) and ends with the vehicle’s speed at 10 kph.
* The second phase (phase2) starts, where the vehicle is driving with a speed between 10 and 15 kph.
  The duration of this series of behavior invocations must be between 10 and 30 seconds.

Code 45. Use of the serial operator

```
scenario vehicle.two_phases:
    do serial (duration: [10s..30s]):
        phase1: drive() with:
            speed(speed: 0kph, at: start)
            speed(speed: 10kph, at: end)
        phase2: drive() with:
            speed(speed: [10kph..15kph])
```

[Code 45](#code-lc-semantics-example-serial-operator) contains no constraints on the duration of the two invoked behaviors.
This means, that this scenario accepts any trace as long as the trace fulfills the following conditions:

1. The trace must be between 10 and 30 seconds long.
2. The trace must describe the behavior of a vehicle.
3. The vehicle starts at a standstill (phase1).
4. At some point the vehicle reaches 10 kph.
5. Then the vehicle continues driving at a speed between 10 and 15 kph (phase2).

Note that during the first phase, the acceleration does not need to be monotonic.
The acceleration may even include values higher than 10 kph and lower than 0 kph, as long as a speed of 10 kph is reached at least once, so that `phase1` and `phase2` can happen within 10 to 30 seconds.

More formally, a scenario that specifies a serial composition of \(n\) behavior invocations accepts a trace only if it is possible to partition the trace into \(n\) segments such that the \(i\)th scenario invocation accepts the \(i\)th segment.
If a serial composition also specifies an optional minimum and maximum time duration, the trace duration must be within the specified range.

For a more concise formal definition, an alternative notation of the minimum and maximum duration parameters is introduced:

* \(\Delta\_{min}\): Minimum duration (default is \(0\))
* \(\Delta\_{max}\): Maximum duration (default is \(\infty\))

A scenario \(Sc \triangleleft \texttt{serial}[\Delta\_{min}, \Delta\_{max}](b\_1 : B\_1, .., b\_n : B\_n)\) accepts a trace \(\pi[t\_0,t\_n)\) *only if*

* \(\Delta\_{min} \leq (t\_n - t\_0) \leq \Delta\_{max}\) and
* there exist times \(t\_1, ... , t\_{n-1}\) with \(t\_0 < t\_1 < \ldots < t\_{n-1} < t\_n\) such that behavior invocation \(b\_i:B\_i\) accepts \(\pi[t\_{i-1},t\_{i})\) for all \(i \in 1, .., n\).

For [Code 45](#code-lc-semantics-example-serial-operator) this means that a trace \(\pi[t\_0,t\_n)\) is accepted by this example scenario only if
\(\pi[t\_0,t\_n)\) can be divided into two subtraces \(\pi[t\_0,t'), \pi[t',t\_n)\) (one for each of the invocations `phase1` and `phase2`) such that

* `phase1` accepts \(\pi[t\_0,t')\): at time \(t\_0\) the speed of the actor is 0 kph and at the time \(t'\) the speed is 10 kph (in between it may have any speed, even grater than 10 kph or less than 0 kph).
* `phase2` accepts \(\pi[t',t\_n)\): the speed of the actor does not exceed the boundaries of 10 and 15 kph during \([t',t\_n)\).
* The difference between \(t\_n\) and \(t\_0\) is greater or equal to 10 seconds or less than or equal to 30 seconds.

#### 7.6.2.1.3 One-of composition

The one-of composition operator models the alternative occurrence of one scenario from a set of two or more scenarios.

In the following example it is specified for a vehicle to either stay on lane 0 and decrease speed from 100 kph to 0 kph or to change lane from 0 to 1 and keep the speed within 60 to 100 kph.
This way a vehicle either brakes on lane 0, for example, because of an obstacle, or changes the lane to avoid the obstacle and keeps on driving.
The duration constraint expresses that either scenario must happen within 10 to 30 seconds.

Code 46. Use of the one-of operator

```
scenario vehicle.one_of:
    do one_of(duration : [10s..30s]):
        phase_a: drive() with:
            speed(speed: 100kph, at: start)
            speed(speed: 0kph, at: end)
            lane(0)
        phase_b: drive() with:
            speed(speed: [60kph..100kph])
            lane(0, at: start)
            lane(1, at: end)
```

More formally, a scenario \(Sc \triangleleft \texttt{one\\_of}[\Delta\_{min}, \Delta\_{max}](b\_1:B\_1, ... ,b\_n:B\_n)\) accepts a trace \(\pi[t,t')\) *only if*

* \(\Delta\_{min} \leq (t' - t) \leq \Delta\_{max}\) and
* at least one behavior invocation \(b\_i:B\_i\), \(i \in 0, ..., n\) accepts \(\pi[t,t')\).

#### 7.6.2.1.4 Parallel composition

The parallel composition operator models the parallel or otherwise overlapping occurrence of two or more scenarios.
The operator takes a list of two or more behavior invocations.
The first one is called the *primary behavior invocation* and the others are called *secondary behavior invocations*.
The operator furthermore accepts four parameters:

* `overlap`: Specifies an overlap kind, which can be `equal`, `start`, `end`, `initial`, `final`, `inside`, `full`, and `any`.
  Default is `start`.
* `start_to_start`: Specifies the allowed offset between the start of the primary behavior invocation and the starts of the secondary behavior invocations.
  This parameter is optional.
* `end_to_end`: Specifies the allowed offset between the end of the primary behavior invocation and the ends of the secondary behavior invocations.
  This parameter is optional.
* `duration`: Specifies the overall duration of the parallel behavior invocations, from the first start of an invoked behavior until the last end of an invoked behavior.
  This parameter is optional.

The following listing shows an example of the parallel operator.

Code 47. Use of the parallel operator

```
scenario parallel_phases:
    v1, v2: vehicle
    do parallel():
        phaseA: v1.drive() with:
            speed(speed: 0kph, at: start)
            speed(speed: 10kph, at: end)
        phaseB: v2.drive() with:
            speed(speed: [10kph..15kph])
            position(distance: [5m..100m], behind: v1, at: start)
```

Here, `phaseA` specifies that actor `v1` accelerates from 0 kph to 10 kph.
In parallel, `phaseB` specifies that another actor `v2` is driving with a speed between 10 and 15 kph.
At the start of the scenario, `v2` should be 5 to 100 meters behind `v1`.

`parallel()` is used here without any parameters.
This means that the overlap kind defaults to `start` and both phases must start at the same time but may end at different times.
More details on the available parameters can be found in the next subsection.

##### Overlap parameter semantics

If a scenario invokes a number of behaviors using the parallel operator with `parallel(equal)`, it means that all invoked behaviors start and end at the same time, meaning a true parallel occurrence of the invoked behaviors.

The other overlap kinds are less strict.
The overlap kind `start`, which is the default if no other overlap kind is specified, requires that all invoked behaviors start at the same time, but can end at different times.
The converse holds for the overlap kind `end`: The end times must be equal, but start times can be different.

The overlap kinds `initial` and `final` require that the secondary behavior invocations cover the start, or the end, of the primary behavior invocation.

![lc parallel overlap kinds equal start end initial final](_images/lc_parallel-overlap-kinds-equal-start-end-initial-final.svg)

Figure 6. Different behavior invocation overlappings allowed by overlap kinds equal, start, end, initial, and final

[Figure 6](#fig-parallel-overlap-kinds-equal-start-end-initial-final) illustrates which parallel or overlapping occurrences of the primary behavior invocation and the secondary behavior invocations are allowed with the overlap kinds `equal`, `start`, `end`, `initial`, and `final`.

The overlap kind `inside` requires that the secondary behavior invocations are fully overlapped by the primary behavior invocation.
`full`, by contrast, requires that all secondary behavior invocations are fully overlapped by the primary behavior invocation.
The overlap kind `any` places no requirement on the overlapping of the invoked scenarios except that there must exist at least one point in time where all scenarios overlap.

![lc parallel overlap kinds inside full any](_images/lc_parallel-overlap-kinds-inside-full-any.svg)

Figure 7. Different behavior invocation overlappings allowed by overlap kinds inside, full, and any

[Figure 7](#fig-parallel-overlap-kinds-inside-full-any) illustrates the overlappings allowed by `inside`, `full`, and `any`.

##### Values for offset and duration parameters

The `start_to_start` and `end_to_end` parameters specify what time offsets are allowed from the start time of the primary behavior invocation to the start time of each secondary behavior invocation.
The values for these parameters can be a range of times (like `start_to_start: [-5s..3s]`) or a single positive or negative time value (like `start_to_start: -5s`).
A positive offset means that the secondary behavior invocations start after the primary behavior invocations and negative offsets mean that the secondary behavior invocations start before the primary behavior invocation.

![lc parallel start to start min max constraints](_images/lc_parallel-start-to-start-min-max-constraints.svg)

Figure 8. An illustration of minimum and maximum start\_to\_start offsets

[Figure 8](#fig-parallel-start-to-start-min-max-constraints) illustrates different cases of `start_to_start` values.
The `end_to_end` constraint works in the same way for end times.

More formally, the semantics of the parallel operator is as follows.
For a more concise formal definition, an alternative notation of the parameters is introduced:

* \(\Delta\_{min}\): Minimum duration (default is \(0\))
* \(\Delta\_{max}\): Maximum duration (default is \(\infty\))
* \(\Delta\_{start-min}\): Minimum difference between the start of the primary behavior invocation and the start of each secondary behavior invocation (default is \(-\infty\))
* \(\Delta\_{start-max}\): Maximum time difference between the start of the primary behavior invocation and the start of each secondary behavior invocation (default is \(\infty\))
* \(\Delta\_{end-min}\): Minimum time difference between the end of the primary behavior invocation and the end of each secondary behavior invocation (default is \(-\infty\))
* \(\Delta\_{end-max}\): Maximum time difference between the end of the primary behavior invocation and the end of each secondary behavior invocation (default is \(\infty\))
* \(\chi\): Overlap kind

A scenario
\(Sc \triangleleft \texttt{parallel}[\Delta\_{min}, \Delta\_{max}, \chi, \Delta\_{start-min}, \Delta\_{start-max}, \Delta\_{end-min}, \Delta\_{end-max}](b\_0:B\_0, .., b\_n:B\_n)\) accepts a trace \(\pi[t, t')\) *only if* for all
\(i \in [0..n]\) there exist times \(t^{b\_i}\_{start}\) and \(t^{b\_i}\_{end}\) such that

* \(\Delta\_{min} \leq t' - t \leq \Delta\_{max}\), meaning the duration of \(\pi[t, t')\) is between \(\Delta\_{min}\) and \(\Delta\_{max}\).
* \(t \leq t^{b\_i}\_{start} < t^{b\_i}\_{end} \leq t'\), meaning the time stamps \(t^{b\_i}\_{start}\) and \(t^{b\_i}\_{end}\) mark time intervals between \(t\) and \(t'\).
* \(b\_i\) accepts \(\pi[t^{b\_i}\_{start}, t^{b\_i}\_{end})\), meaning each parallel behavior invocation accepts a subtrace of \(\pi[t, t')\) where \(t^{b\_i}\_{start}\) and \(t^{b\_i}\_{end}\) mark the beginnings, respectively, the ends of the subtrace.
* \(\forall j \in [1..n]\) it holds that all start and end times of the secondary behavior invocations respect the start\_to\_start and end\_to\_end offsets relative to the primary scenario:

  + \(t^{b\_j}\_{start} - t^{b\_0}\_{start}\geq \Delta\_{start-min}\)
  + \(t^{b\_j}\_{start} - t^{b\_0}\_{start}\leq \Delta\_{start-max}\)
  + \(t^{b\_j}\_{end} - t^{b\_0}\_{end}\geq \Delta\_{end-min}\)
  + \(t^{b\_j}\_{end} - t^{b\_0}\_{end}\leq \Delta\_{end-max}\)
* There exists a time \(t\_{\bowtie}\) such that \(t^{b\_i}\_{start} \leq t\_{\bowtie}\) and \({\bowtie} \leq t^{b\_i}\_{end}\), meaning there exists a point in time where all parallel behavior invocations overlap.
* There exists a \(j\) with \(t^{b\_j}\_{start} = t\), meaning one of the parallel behavior invocations accepts a subtrace of \(\pi[t, t')\) starting at time \(t\).
  Or, in other words, there is no time at the beginning of the trace that is not covered by any of the parallel behavior invocations.
* There exists a \(k\) with \(t^{b\_k}\_{end} = t'\), meaning one of the parallel scenarios accepts a subtrace of \(\pi[t, t')\) ending at time \(t'\).
  Or, in other words, there is no time at the end of the trace that is not covered by any of the parallel behavior invocations.
* If \(\chi = \texttt{equal}\) then it holds that \(t^{b\_i}\_{start} = t\) and \(t^{b\_i}\_{end} = t'\).
  This is equivalent to saying that \(\pi[t, t')\) is accepted by \(b\_i\) (\(\forall i \in [0..n]\)), meaning the trace satisfies all parallel behavior invocations.
* If \(\chi = \texttt{start}\) then
  \(t^{b\_i}\_{start} = t\).
  That is, all behavior invocations accept some subtrace of \(\pi[t, t')\) starting at \(t\).
* If \(\chi = \texttt{end}\) then
  \(t^{Sc\_i}\_{end} = t'\).
  That is, all behavior invocations accept some subtrace of \(\pi[t, t')\) ending at \(t'\).
* If \(\chi = \texttt{inside}\) then \(\forall j \in [1..n]\) it holds that
  \(t^{b\_0}\_{start} \leq t^{b\_j}\_{start}\)
  and
  \(t^{b\_0}\_{end} \geq t^{b\_j}\_{end}\).
* If \(\chi = \texttt{full}\) then
  \(\forall j \in [1..n]\) it holds that
  \(t^{b\_0}\_{start} \geq t^{b\_j}\_{start}\)
  and
  \(t^{b\_0}\_{end} \leq t^{b\_j}\_{end}\).
* If \(\chi = \texttt{initial}\) then \(\forall j \in [1..n]\) it holds that
  \(t^{b\_j}\_{start} \leq t^{b\_0}\_{start} \leq t^{b\_j}\_{end}\).
* If \(\chi = \texttt{final}\) then \(\forall j \in [1..n]\) it holds that
  \(t^{b\_j}\_{start} \leq t^{b\_0}\_{end} \leq t^{Sc\_j}\_{end}\).

### 7.6.2.2 Scenario fields and bindings

To decide whether a scenario accepts a trace, the following relation is needed: The scenario and its fields have to be related to objects in the states of the given trace.
For a scenario to accept a trace, there must exist *bindings* of object-typed fields of the scenario to objects in the states of the trace.
This section defines the concept and necessary conditions for scenario field bindings in more detail.

A system state \(\pi(t)\) of a trace \(\pi\) at time \(t\) consists of a set of actor objects.
An ASAM OpenSCENARIO model defines actor types for these objects that appear in the system states.
In addition, an ASAM OpenSCENARIO model defines types like scenarios or scenario modifiers that do not represent actor objects, but are concepts within the ASAM OpenSCENARIO model to describe the behavior of actor objects.
These types are called *scenario model types*.

Scenarios have fields that can be typed by actor object types and scenario model types.
Moreover, scenario fields can be *parameters* or *variables*.
In order for a scenario to accept a trace, there must exist *bindings* from scenario parameters typed by actor object types to corresponding system objects that remain unchanged during the lifetime of a scenario.

More formally, a scenario \(Sc\) with actor object type parameters \(P^{sys} = p^{sys}\_1, ..., p^{sys}\_n\) accepts a trace \(\pi[t\_a, t\_b)\) only if there exists a *binding* of actor object type parameters \(b^{sys}\_{Sc} : P^{sys} \rightarrow O\), which is a function that is total, non-injective, non-surjective, from the actor type scenario parameters \(P^{sys}\) to actor objects \(O\) that are shared by all system states \(\pi(t)\) where \(t \in [t\_a, t\_b)\).
That is, the binding does not change over time \([t\_a, t\_b)\) and also actor objects do not disappear over time \([t\_a, t\_b)\).

In a composite scenario (see [Section 7.6.2.1, “Composition operators”](#sec-lc-semantics-composition-operators)), the invoking scenario can specify constraints, specific values, or ranges of specific values for the parameters of the invoked scenarios.
In addition to the conditions given in composition operators, an invoked scenario accepts a (sub-)trace only if there exists an instance of the invoked scenario that respects the constraints imposed by the invoking (parent) scenario for that trace.

![lc scenario field bindings](_images/lc_scenario-field-bindings.svg)

Figure 9. An illustration of an ASAM OpenSCENARIO scenario execution state showing scenario instances and field bindings.

[Figure 9](#fig-scenario-field-bindings) shows the concept of scenario instances and parameter bindings.

The parameter bindings of a scenario to actor objects and values of a trace that it accepts is called a *scenario instance* of that scenario.
The behavior invocation relationships (compare [Section 7.6.1.4, “Behavior invocation tree”](#sec-lc-semantics-behavior-invocation-tree)) at a certain time of a given trace can imply a tree of scenario instances.
These scenario instances comprise a *scenario state* (middle of the figure) that corresponds to a system state (bottom of the figure).
The top of the figure shows parts of an ASAM OpenSCENARIO model that describes an overtaking scenario involving two cars.
Indeed, two cars exist in the system state shown at the bottom.
The extension of the main scenario specifies two parameters of the actor type `Car` and invokes the scenario `Car.overtake` with these cars: Car `c1` is specified as the overtaking car and the main actor of the `Car.overtake` scenario and car `c2` is specified as the overtaken car.

This leads to a configuration of scenario instances with bindings from actor type parameters to actor objects: First, there is an instance of the main scenario `top.main`, where the parameters `c1` and `c2` bind to `carA` and `carB`.
The main scenario constrains the invocation `Car.overtake` in a way that the implicit main parameter `it` must be equal to the value bound to `top.main.c1`, namely `carA`, and the parameter `overtaken_car` must be equal to the value bound to `top.main.c2`, namely `carB`.

The invocation of `Car.overtake` by the extension of `top.main` does not constrain the value of the `overtaken_lane` parameter.
Thus, an arbitrary binding for this parameter to a lane instance can be chosen.
The scenario `car.overtake` probably has an additional constraint to ensure a meaningful binding for the parameter.
But this constraint is not shown in the figure.

The invocation of `Car.overtake` by the extension of `top.main` causes the parameter `overtake1` to be bound to the instance of the scenario `Car.overtake` here labeled `ot1:Car.overtake`.

### 7.6.2.3 Scenario constraints

The structure and functionality of constraints are already described in [Section 7.3.11, "Constraints"](types.html#sec-lc-constraints).

In those sections also time aspects and strengths of constraints are specified.
This chapter defines how constraints influence trace acceptance within the declarative semantic of ASAM OpenSCENARIO.

The core part of constraints are Boolean expressions which state limitations for the values of parameter fields inside instances of structured types (struct, scenario, actor, or modifier).
By default, those limitations are applied as long as the instance in which they are declared exists. (A scenario can exist for a certain time, see also scenario instance in [Section 7.6.2.2, “Scenario fields and bindings”](#sec-lc-semantics-scenario-fields-and-bindings)).
During the lifetime of an instance of a structured type, all constrained parameter fields must be bound to values satisfying the constraints at each point in time.
Furthermore, there are special constraints that can be specified to hold at certain points in time, using the keyword *at*.

If a (parent) scenario (type) \(Sc\_P\) defines a scenario invocation \(sc:Sc\) (of type \(Sc\)), there are three different kinds of constraints to consider:

* The constraints specified by the type of the invoked scenario \(Sc\), denoted as \(C\_{Sc}\)
* The constraints specified by the parent scenario \(Sc\_P\) in the scenario invocation using modifiers, denoted as \(C\_{sc:Sc}\)
* Other constraints specified by the parent scenario \(Sc\_P\), denoted as \(C\_{ScP}\)

If a (parent) scenario \(Sc\_P\) invokes another scenario \(sc:Sc\), all three sets of constraints \(C\_{Sc}\), \(C\_{sc:Sc}\), and \(C\_{ScP}\) must hold for the lifetime of \(sc:Sc\), which is the time that the invocation \(sc:Sc\) is active.
[Figure 5](#fig-scenario-type-and-invocation) compares the three sets of constraints.

A scenario invocation \(sc:Sc\) accepts a trace *only if* it satisfies the constraints \(C\_{Sc}\) and \(C\_{sc:Sc}\), this means that there exists a binding for scenario fields to values and actor objects in the actor system, such that these constraints are satisfied. In addition, the trace is only accepted if all constraints of all objects in the traffic system are satisfied in all states of the trace.

A trace can be rejected in the following cases:

* Contradictions between constraints:  
  There can be contradicting constraints for example if `keep(speed>10kph)` and `keep(speed<10kph)` are defined within the same vehicle actor.
  Such constraints can also conflict if they are placed on the same actor instance from within different scenarios that can be active in parallel.
  Such cases may be less obvious.
  Moreover, there can be a complex interplay between constraints.
  For example, imagine a vehicle is constrained to a certain minimum distance to a preceding vehicle, while the preceding vehicle has some constraints forcing it to accelerate.
  Then the following vehicle may be forced to violate constraints on the maximum speed.
* Impossible constraints because of other behavior restrictions:  
  For example, there can be constraint conflicts between scenario constraints and constraints implied by atomic actions that are invoked directly or indirectly from that scenario.
  Trace acceptance conditions defined for atomic actions may contradict constraints in scenarios invoking these actions.
  Refer to the definition of the semantics of action, for example,  [Section 8.8, "Movement actions"](../domain-model/actions.html).)
  There can also be conflicts with specific behavior models, such as driver models.

### 7.6.2.4 Time constraints

Time constraints may occur in the context of the following language constructs:

* *Composition Operators*  
  When composing different behaviors by using composition operators like serial or parallel the duration of the composed behaviors can be restricted by using the "duration" parameter.
  For semantic details, refer to [Section 7.6.2.1, “Composition operators”](#sec-lc-semantics-composition-operators).
* *Action Invocations*  
  When invoking actions from the domain model specification (like drive or changeLane) the duration of that action may be restricted by using the parameter "duration".
* *Wait directives*  
  The `wait` directive may be used to introduce phases with a certain time duration into a scenario where it is not further constrained what happens during that duration.
  Note that this directive may also be invoked using the specification of an event to wait for.
  The semantics of that directive is described in [Section 7.6.2.5, “Events”](#sec-lc-semantics-events).

#### 7.6.2.4.1 Action invocation using duration parameter

The duration parameter may be constrained when invoking an action.
It adds a restriction to the set of accepted traces regarding the time duration of the respective action.

Formally, \(\pi(t, t')\) is accepted by the action \(drive (duration: [dur^-..dur^+\))] if

* \(t' - t \geq dur^-\), and
* \(t' - t \leq dur^+\)

This is an example where the action `drive` is constrained via the `duration` parameter to take between 30 and 60 seconds.

+

```
...
do:
    car1.drive(duration: [30s..60s])
```

#### 7.6.2.4.2 Wait directive

The wait directive when used with an `elapsed()` expression adds a phase of the given duration to the scenario and it is not further specified what is allowed or intended to happen during this time.
Hence, formally in this 'intended specification gap' anything is allowed to happen.
It only needs to be assured that the (sub-)trace corresponds to the specified waiting time, meaning that the (sub-)trace has the correct length.

Formally, \(\pi(t, t')\) is accepted by the wait directive \(wait elapsed([dur^-..dur^+\))] if

* \(t' - t \geq dur^-\), and
* \(t' - t \leq dur^+\)

Code 48. Wait directive

```
scenario wait_time:
    my_vehicle: vehicle
    do serial:
        phase1: my_vehicle.drive() with:
            speed(speed: 0kph, at: start)
            speed(speed: 10kph, at: end)
        phase2: wait elapsed([10s..20s])
        phase3: my_vehicle.drive() with:
            speed(speed: [10kph..15kph])
```

This example is very similar to the one from the composition section for serial.
But here, another phase in between (*phase2*) was added, which invokes a wait directive with a duration of 10 to 20 seconds.
This means that during a time interval of 10 to 20 seconds anything is allowed to happen.
Afterward, the action of phase3 is invoked.

### 7.6.2.5 Events

This chapter defines how events and directives involving events, such as `emit`, `wait`, or `until` influence whether a trace accepts a given behavior trace.

To do so, this subsection defines:

* How traces are extended with events formally.
* What it means for a scenario to accept a trace extended with events.
* How the individual directives, like `emit` and `wait`, work using events.

There are four sources of events in ASAM OpenSCENARIO:

* A scenario fires start and end events when it starts and ends.
* A scenario can fire events explicitly using the `emit` directive.
* A structured type (such as a scenario or an actor) can have *event declarations* with an *event specification* that defines when this event occurs.
  The event specification can consist of a condition, such as a rise, fall, or elapse condition or another Boolean expression.
  An event with such an event specification occurs every time the specified condition evaluates to true.
  The event specification can also consist of a reference to another event plus an optional condition.
  In this case, the event occurs every time the referenced event occurs and the condition evaluates to true.
* External functions can fire events.
  For example, an external function that connects to an external simulation application can cause an event to occur under certain conditions in that external simulation application.

Events are abstract objects: An event is an instance of an event definition identified by the name of the event given in the definition and parameter values for the parameters defined in the event definition (if any).
An event carries no information about its source.

Events are *purely* abstract objects, which means that they are used only as a control mechanism within the language to specify:

* Constraints on values at certain points in time
* Constraints on the relative timing of scenarios
* Points in time in which external functions are invoked

Events do not necessarily have a direct resemblance in the modeled traffic system, nor are certain conditions that occur within the modeled traffic system necessarily events in terms of a given ASAM OpenSCENARIO model.

For example, the starts and ends of scenarios do typically correspond to certain conditions.
It can be the case that a scenario ends when a vehicle reaches a certain speed.
However, there could also be sequences of scenarios where there is no uniquely identifiable point in time at which one scenario ends and the other begins, for example, when there are overlapping ranges of possible speeds of a vehicle required by two subsequent scenarios.

As another example, the honk of a horn can be considered.
A given traffic system behavior where a vehicle’s horn sounds could be accepted by an ASAM OpenSCENARIO model that does not require or model the honk event at all.
Likewise, defining and emitting an event called "honk" does not necessarily mean that a vehicle’s horn sounds in the modeled traffic system.
Such an event must first translate to a change in a field value of a vehicle object in the traffic system.
More technically and less semantically speaking, a honk event could also be a trigger for an external function call that then leads to a honk happening in an external simulation tool.

Events occur at certain points in time.
This is formally represented by an *event occurrence function*.
This function defines for every point in time the set of events occurring at that time.
Formally, an event occurrence function has the type \(\epsilon: \mathbb{R}\_{\geq 0} \to \mathbb{P}(E)\), where \(E\) is a set of events identified by a name and parameter values.
(\(\mathbb{P}(E)\) denotes the powerset of \(E\), that is, the set of all sets of events.)

Based on the event occurrence function, we define an *event trace* as a tuple \((\epsilon, \pi)\) that combines an event occurrence function \(\epsilon\) with a trace \(\pi\).
Both share a time axis, so \(\epsilon\) defines when events occur within the trace \(\pi\).

Note that the above definition implies that for every point in time there cannot be two occurrences of identical events.
If, for example, the same event (referring to the same event definition by their name and with identical parameter values) is emitted by two scenarios at the same time, this will lead to the occurrence of only one instance of this event.
If it is important to separate two occurrences of events, then they must be equipped with parameters that make this separation possible.
For example, honk events could be equipped with a parameter that specifies the vehicle which is the source of the honk signal.
Also, note that there is no order among the events occurring at the same time.

#### 7.6.2.5.1 Trace acceptance and event trace consistency

A scenario \(Sc\) accepts a trace \(\pi\) only if there exists an event trace \((\epsilon, \pi)\) where the event occurrence defined by \(\epsilon\) satisfy the following conditions:

* \((\epsilon, \pi)\) must be *event trace consistent* with scenario \(Sc\), which means that \(\epsilon\) places events on the trace timeline in such a way that this corresponds to

  + the time stamps of the start and end of scenarios that are invoked directly and indirectly by the scenario \(Sc\): At these points in time, the predefined `start` and `end` events for the scenario invocations must occur.
  + the time stamps of `emit` directives directly or indirectly invoked by \(Sc\).
  + the time stamps of value changes that trigger qualified events.
* `wait` directive invocations are terminated if and not before a waited for event occurs while the wait directive invocation is active.
* Invocations of behaviors with an `until` directive are terminated exactly when a specified event occurs.

All other trace acceptance conditions defined above remain unaffected and must hold in addition to the conditions given here.

In the following, the semantics of the `emit`, `wait`, `until`, and `on` directives are defined in more detail.

#### 7.6.2.5.2 Emit (event)

The `emit` directive is a zero-time directive that emits an event (which may be waited for in another scenario).
Within an `emit` directive invocation, values must be specified for all parameters defined in the event declaration.
At the time of invocation, any expressions specifying the event parameters are immediately evaluated, so that a concrete event instance is emitted.

An `emit` directive typically appears within a serial composition, either directly or indirectly, because its invoking scenario is in turn invoked within a serial composition higher up in the behavior invocation tree.
In this case, the `emit` directive emits an event at the same point in time as the previous behavior invocation terminates with respect to the next level of serial composition in the behavior invocation tree.
That means that the `end` event of the previous behavior invocation and the event emitted by the `emit` directive occur at the same time.
If an `emit` invocation is not preceded by another behavior in a serial composition, and therefore happens at the beginning of the direct or indirect parent scenario, this means that the emitted event must occur at the beginning of the trace that shall be accepted by that scenario.
An `emit` directive is zero-time, which means that the start and end of an `emit` invocation happen at the same point in time.

Because an `emit` directive is zero-time, there is no notion of trace acceptance defined for `emit` directives:
`emit` directives, as well as all other zero-time directives, are excluded from the trace acceptance semantics definition of the scenario composition operators (see [Section 7.6.2.1, “Composition operators”](#sec-lc-semantics-composition-operators)).
`emit` directives only influence trace acceptance of the parent scenarios indirectly by influencing the event trace consistency condition defined above (see [Section 7.6.2.5.1, “Trace acceptance and event trace consistency”](#sec-lc-semantics-trace-acceptance-and-event-trace-consistency)):
It is required that the event trace \((\epsilon, \pi)\) contains the emitted events at the time stamps where the `emit` directive invocation occurs.

Code 49. `emit` event

```
event vehicle_reached_speed(vehicle : vehicle, vehicle_speed : speed) # event definition

...

scenario vehicle.two_phases:
    do serial:
        phase1: drive() with:
            speed(speed: 0kph, at: start)
            speed(speed: [25kph..35kph], at: end)
        emit vehicle_reached_speed(actor, actor.speed)
        phase2: drive() with:
            speed(speed: [30kph..50kph])
```

This is an example of how an event can be emitted within a serial composition.
The event definition is also shown on top: The event requires as parameter values a reference to a vehicle (`vehicle`) and a speed value (`vehicle_speed`).
The scenario describes two driving phases.
The first phase requires the vehicle to reach a speed between 25 and 35 kph.
The event is emitted after the first phase, more specifically at the same point in time in which the first scenario terminates.
The event emitted carries as parameter values a reference to the vehicle object which is subject to the scenario (which can be accessed via the *actor* field inherent to all scenarios that are invoked on actors), as well as the speed value of that vehicle at the point in time in which the event is emitted.

Such an event can be caught by another scenario using the `wait` directive.

#### 7.6.2.5.3 Wait (event)

The `wait` directive for events serves as a synchronization point, delaying subsequent behavior invocations until the waited for event has occurred.

Except for delaying the next behavior, the `wait` statement imposes no constraints.
If certain constraints shall hold while waiting, such constraints can be specified in a surrounding parallel composition.

Regarding trace acceptance, it is required that a trace satisfies any constraints imposed by modifiers.
Other than that, `wait` directives only influence trace acceptance of the parent scenarios indirectly by influencing the event trace consistency condition defined above (see [Section 7.6.2.5.1, “Trace acceptance and event trace consistency”](#sec-lc-semantics-trace-acceptance-and-event-trace-consistency)):
It is required that the event trace \((\epsilon, \pi)\) contains waited for events only at the time stamps where the `wait` directive invocation terminates or is inactive.

Note that this semantics definition entails that traces can be accepted that never lead to progressing a `wait` directive invocation, and hence, never lead to the occurrence of any subsequent behavior.
In use cases where this is not acceptable, for example, upper time bounds can be specified for the invoking scenario.

Code 50. `wait` event

```
scenario vehicle.sync_with_other_vehicle:
    other_vehicle: vehicle
    do parallel:
        other_vehicle.two_phases
        serial:
          wait @vehicle_reached_speed as vrs_event \
                if vrs_event.vehicle == other_vehicle \
                    and vrs_event.vehicle_speed in [30kph..32kph]
          drive() with:
            speed(speed: other_vehicle.speed + 20 kph, at: start)
```

In this example, we have a scenario `sync_with_other_vehicle` that can be invoked on vehicles.
It holds a field to another vehicle (`other_vehicle`) and defines a parallel composition of an invocation of the `two_phases` scenario from [Section 7.6.2.5.2, “Emit (event)”](#sec-lc-semantics-emit-event) on the vehicle `other_vehicle` and a serial composition of a `wait` action followed by an invocation of `drive()`.
The `drive()` action is invoked on whichever vehicle `sync_with_other_vehicle` will be invoked.

The `wait` directive waits for the event `vehicle_reached_speed` that is emitted in the `two_phases` scenario (see [Section 7.6.2.5.2, “Emit (event)”](#sec-lc-semantics-emit-event)).

Moreover, the `wait` directive specifies two conditions:

1. The first condition is that the `vehicle` parameter of the event must be equal to `other_vehicle`
   They must both bind to the same vehicle actor object.
2. The second condition is that the parameter `vehicle_speed` must be within the range of 30 to 32 kph.

If a `vehicle_reached_speed` event occurs that satisfies these two conditions, the `wait` invocation terminates and the subsequent `drive()` action starts, specifying that the vehicle on which `sync_with_other_vehicle` is invoked must drive with a speed 20 kph higher than the speed of `other\_vehicle´ immediately after the occurrence of the event.

#### 7.6.2.5.4 Until (event)

The `until` directive specifies that a behavior invocation shall terminate exactly on the occurrence of a specific event, and not before or after.

The `until` directive influences trace acceptance indirectly by influencing the event trace consistency condition (see [Section 7.6.2.5.1, “Trace acceptance and event trace consistency”](#sec-lc-semantics-trace-acceptance-and-event-trace-consistency)):
For event trace consistency, events must occur in such a way that invocations of behaviors with an `until` directive are terminated exactly when a specified event occurs.

When multiple `until` directives apply to a behavior invocation, they are treated as if a single `until` directive was given that matches any of the specified events:
The invocation terminates exactly when the first of these specified events occurs.

Code 51. Use of the `until` directive

```
scenario vehicle.accelerate_to_speed_with_other_vehicle:
    target_speed : speed
    other_vehicle : vehicle
    do drive() with:
        speed(speed: target_speed, at: end)
        until @vehicle_reached_speed as vrs_event \
             if vrs_event.vehicle == other_vehicle \
                and vrs_event.vehicle_speed == target_speed
```

This example shows a scenario for vehicles that invokes a drive action and specifies a target speed that shall be reached at the end of the scenario.
In addition, the scenario defines a field called `other_vehicle` and it specifies that the scenario must end exactly at the occurrence of the event `vehicle_reached_speed` under the condition that the event carries as the `vehicle` parameter value a reference to the same vehicle as bound to `other_vehicle`, and a `vehicle_speed` parameter value the same value as set for `target_speed`.

#### 7.6.2.5.5 On (event)

Scenarios can have `on` directives, which define that on the occurrence of an event, another zero-time behavior shall take place, such as a method call or emitting another event.
`on` directives only influence trace acceptance if they trigger other events via `emit` directives (see [Section 7.6.2.5.2, “Emit (event)”](#sec-lc-semantics-emit-event)).

## 7.6.3 Actions

Actions are atomic behaviors that can be performed by actors, and they can be invoked from scenarios.

The domain model of ASAM OpenSCENARIO specifies a set of domain actions, such as the `drive()` action, including their semantics (see  [Section 8.8, "Movement actions"](../domain-model/actions.html#top-dm-movement_actions)).

In this release of the standard, the action semantics are not specified formally, and the precise semantics are left to the implementation of the respective actions.