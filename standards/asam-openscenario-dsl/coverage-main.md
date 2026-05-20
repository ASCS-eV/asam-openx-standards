# ASAM OpenSCENARIO® DSL v2.2.0 — 7.5 Coverage

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/language-reference/coverage_main.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.5 Coverage

## 7.5.1 Coverage and reporting overview

ASAM OpenSCENARIO coverage and recording features allow users to set goals for a verification and validation undertaking:

* Which scenarios need to be exercised?  
  For example, `cut-in-and-slow` scenario.
* How should they be exercised?  
  For example, `cut-in-and-slow` should be exercised from both left and right sides, and should be performed with all vehicle kinds.
* How many times do values need to be observed to be declared complete?  
  For example, each expressed combination should be tried at least 50 times on-street driving.

Coverage allows storing the values that are expected to be observed throughout the development and V&V process.
Reporting uses similar syntax with the goal to store data for later analysis or KPI analysis.
Coverage and reporting definitions can be reused over multiple ODDs and projects as they can be overridden non-intrusively.

## 7.5.2 Cover

The *cover* directive defines a coverage data collection point.
It can be placed as a member into structs, actors, or scenarios.

Code 44. Syntax of cover directive

```
cover([name: ] <identifier> [, expression: <exp>] [, <param>* ])
```

The mandatory `name` argument provides the user-supplied identifier for the cover directive.
This identifier also serves as the expression to monitor, if the optional `expression` argument is not provided.

The `expression` argument provides the expression to monitor.
The expression must be of a scalar type and must be valid to evaluate in the local context of the cover directive.
The value of the cover item is the value of the expression when the cover group event occurs.
If the `expression` argument is not provided, the expression is derived from the name.

Additional common arguments can be provided, as described in [Section 7.5.5, “Common cover and record arguments”](#sec-lc-coverage-common-arguments).

Coverage is a mechanism for sampling key parameters related to scenario execution.
Analyzing aggregate coverage helps determine how safely the AV behaved and what level of confidence you can assign to the results.

For example, to determine the conditions under which a `cut_in_and_slow_down` scenario failed or succeeded, you might need to measure:

* The *speed* of the device under test car
* The *relative speed* of the passing car
* The *distance* between the two cars

You can specify when to sample these items.
For example, the key events for this scenario are the start and end events of the `change_lane` phase.

Cover items that have the same sampling event are aggregated into a single metric group, along with record data sampled by the same event.
The default event for collection coverage is `end`.

If the range of data that you want to collect is large, you might want to slice that range into sub-ranges or buckets.
For example, if you expect the device under test car to travel at a speed between 10 kph and 130 kph, specifying a bucket size of 10 gives you 12 buckets, with 10 kph – 19 kph as the first bucket.

You can also specify an explanatory line of text to display about the cover item during coverage analysis.

This example defines:

* A name
* A unit of measurement
* A line of display text
* A range for the field speed
* A range slice for the field speed

Code 45. Using cover()

```
cover(speed1, unit: kph,
    text: "Absolute speed of ego at change_lane start (in km/h)",
    range: [10..130], every: 10)
```

You can declare a field and define coverage for it at the same time.
The following examples are equivalent.

Code 46. Two possibilities to define a field and coverage with the same result

```
# Example 1
current_speed: speed with:
    cover(current_speed, unit: kph)

# Example 2
current_speed: speed
cover(current_speed, unit: kph)
```

The following example extends the `dut.cut_in_and_slow` scenario to add a `do-not-generate` field called `rel_d_slow_end`.
This variable is assigned the value that is returned by the `ego.space_gap()` method at the end event of the slow-phase of the scenario.
A coverage for that field, including a unit, display text, and so on is also defined.

```
extend cut_in_and_slow:
    var rel_d_slow_end: distance = sample(ego.space_gap(car1), @slow.end)
    cover(rel_d_slow_end, text: "car1 position relative to ego at slow end (in centimeter)",
            unit: cm, range: [0..6000], every: 50,
            ignore: (rel_d_slow_end < 0cm or rel_d_slow_end > 6000cm))
```

## 7.5.3 Record

The `record` directive defines a performance metric or other data collection point.
It can be placed as a member into structs, actors, or scenarios.

Code 47. Syntax of record directive

```
record([name: ] <identifier> [, expression: <exp>] [, <param>* ])
```

The mandatory `name` argument provides the user-supplied identifier for the record directive.
This identifier will also serve as the expression to monitor if the optional `expression` argument is not provided.

The `expression` argument provides the expression to monitor.
The expression must be of a scalar type and must be valid to evaluate in the local context of the record directive.
The value of the record item is the value of the expression when the record group event occurs.
If the `expression` argument is not provided, the expression is derived from the name.

Additional common arguments can be provided, as described in [Section 7.5.5, “Common cover and record arguments”](#sec-lc-coverage-common-arguments).

The `record` directive is used to capture performance indicators and other data items that are not part of the coverage model, such as the name and version strings identifying the device under test.

The purpose of performance evaluation is to see how well the device under test performed in specific conditions as they occur within a scenario.
Performance can be evaluated along multiple dimensions, like safety, ride comfort, and so on.

Performance metrics can also be used to provide pass or fail indication:
Sampled values that cross a specified threshold indicate, that the device-under-test-performance was outside the acceptable range.

Often, raw performance values need to be interpreted in the context of a specific scenario:
For example, it may be acceptable to cross the max-deceleration threshold if emergency braking is required.

For this purpose, raw performance values can be converted to performance grades.
A *performance grade* (also called a normalized KPI) is a context-dependent number between 0 ("really bad") and 1 ("excellent").
This grade is attributed to some aspect of the device-under-test-behavior.
This grade can be computed using a user-defined grading formula, converting one or more raw values into a grade in a context-dependent way.

The following example shows how record() is used to capture time-to-collision into the metric group associated with the end of a change-lane maneuver.

Code 48. Using record() for capturing

```
extend cut_in_and_slow:
    # Sample the time-to-collision KPI at the end of change_lane
    var ttc_at_end_of_change_lane: duration = sample(ego.time_to_collision(car1), @change_lane.end)

    # Record the KPIs into the cut_in_and_slow.end metric group
    record(ttc_at_end_of_change_lane,
        unit: s,
        text: "Time to collision of ego car to cut-in car at end of the change_lane phase")
```

## 7.5.4 Cross coverage or record

The coverage or record metrics of two or more previously defined items can be combined.
This is done by specifying the items as a list in a new `cover` or `record` directive.
This creates a Cartesian product of the specified metrics, showing every combination of values of the items.

Only items that belong to the same metrics group (same sample event) can be combined in this way.

The following example creates a cross-record: A Cartesian product of the time-to-collision record item and the DUT velocity cover item, both sampled at the start of the change\_lane phase.
This is considered a cross-record because it includes at least one record item.

```
record(ttc_dut_vel, items: [ttc_at_end_of_change_lane, dut_v_cls], event: start,
    text: "Cross record of TTC and absolute DUT velocity")
```

The next example creates a Cartesian product of three cover vectors at the start of the `change_lane` phase of a scenario:

1. The *relative distance* between two cars
2. The *absolute velocity* of the DUT vehicle
3. The *relative speed* of the other vehicle

```
cover(cross_dist_vel, items: [rel_d_cls, dut_v_cls,rel_v_cls], event: change_lane_start,
    text: "Cross coverage of relative distance and absolute velocity")
```

## 7.5.5 Common cover and record arguments

The `cover` and `record` directives accept the following common arguments, which are optional and can be used as named arguments:

* `unit: <unit>`  
  Specifies a unit for a physical quantity, such as time, distance, or speed.
  The value of the field is converted into the specified unit.
  That value is used as the coverage value.
  A unit must be specified for items that have a physical type.
* `range: <range>`  
  Specifies a range of values for the physical quantity in the unit specified with `unit`.
  It is an error if this argument is used in combination with the `buckets` argument.
* `every: <value>`  
  Specifies when to slice the range into sub-ranges.
  If a given value range is large, for example [0..200], this argument can be used to slice that range into sub-ranges every 10 or 20 units.
  It is an error if this argument is used in combination with the `buckets` argument.
* `event: <event-name>`  
  Specifies the event when the field is sampled.
  The default is the end event of the enclosing scenario.
  Items that have the same sampling event are aggregated into a metric group.
  Note that both coverage and performance items can be collected in the same metric group.

  + You can sample a field value on one event and cover it on another.
    This way you can, for example, capture the speed of a car when changing lanes, but associate the cover item with the scenario end metric group.
  + The cover event must be local (an event defined in the enclosing struct, actor, or scenario).
    No dotted path expressions are allowed.
    If necessary, you can define a local event to be derived from some path expression and use that for coverage.
    For example, `event change_lane_start is @change_lane.start`.
* `text: <string>`  
  Provides an explanatory string describing this metric point.
* `items: <list>`  
  Declares a list of identifiers, whose metrics are combined and displayed as a single cross item.
  The identifiers must be separated by commas and enclosed in square brackets.
  The list can include a mix of cover and record identifiers.
  If a record identifier is included, the resulting item is a cross-record item.
* `ignore: <item-bool-exp>`  
  Defines values that are to be completely ignored.
  The expression is a Boolean expression that can contain only the item name and constants.
  If the ignore expression is true when the data is sampled, the sampled value is ignored (meaning not added to the bucket count).
* `disable: <bool>`  
  Must be either the literal `true` or `false`.
  The value `true` completely disables a metric item.
  This argument is used with override (see [Section 7.5.6, “Override”](#sec-lc-coverage-override)), to disable an existing metric item.
  (Default value: `false`).
* `buckets: <list of bucket boundaries>`  
  Provides a way to declare different-sized buckets, by specifying bucket boundaries.
  A list of N values defines N-1 buckets.
  Each value must be greater or equal to the previous one.
  For example, `cover(speed, unit: kph, buckets: [1, 2, 6.5, 10])` creates the following buckets: `1..2, 2..6.5, 6.5..10`.
  It is an error if this argument is used in combination with either `range` or `every` arguments.
* `target: uint`  
  Describes how many times a bucket needs to be sampled to be declared as accomplished.
  For example, you may express that you need 5 cut-ins from the left and 5 cut-ins from the right.
  This requires the target to be set to 5.
  Target is only valid for cover directives and has no meaning for record directives.
* `illegal: <item-bool-exp>`  
  Identifies conditions in which the provided values indicate a malfunction in the ego or the behavior of the ego.
  The expression is a Boolean expression that can contain only the item name and constants.
  Note that error values are automatically ignored.

## 7.5.6 Override

The *override* option is used to override a parameter in an already defined `cover()` or `record()` member.

Coverage extensions and refinements are key aspects for content and library reuse.
The developers of libraries are most familiar with the reusable scenario implementation and overall goals.
They can associate coverage goals with reusable code.
Later on, project-specific users may accept the provided definition or refine the code to reflect their ODD goals.
To maintain reuse, the user refinements should not be intrusive and should not involve modifying the pre-provided reusable code.

Code 49. Syntax of cover and record overrides

```
cover | record(override: <name> [, <param>* ])
```

The override feature works as follows:

* `<name>` must be the name of an existing cover or record item in the event metric group.
* Any other specified parameter in the `<param>` list overrides the corresponding original parameter.
  Parameters not provided in the override retain their original values.
  Parameters originally not contained are added.
* Multiple overrides are allowed.
  The last value provided for each parameter prevails.
* This automatically percolates to any cross-metric using this item.

Code 50. Overriding an original definition

```
# Original definition
cover(speed_diff, units: kph, range: [1..20], every: 5)

# New definition overrides the every: 5 and adds ignore
cover(override: speed_diff, every: 4, ignore: speed_diff in [10kph..13kph])
```

The following restrictions apply to the use of the override mechanism:

* The name of the item cannot be changed.
* The expression, event, and unit as originally defined cannot be overridden.
* Override can only be used in the same type where the cover or record modifier was originally defined.
  It cannot be used to override a cover or record modifier in a subtype.

## 7.5.7 Coverage grading

Coverage provides a clear grade of how much functionality was exercised and observed from the user-defined goal.
Each type has its own default number of coverage buckets:

* Boolean  
  Two buckets.
* Enumerate  
  The number of possible values constitutes a bucket.
* Numeric up to a byte  
  A bucket per possible value.
  For example, a byte has 256 buckets.
* Numeric large size type  
  A default grade of min, max, and three middle buckets, middle buckets of low, medium, and high.

Users can override the default buckets using `range` or `ignore`.
The calculated grade represents the number of buckets that had their values observed in the scenario divided by the total number of buckets for the type.

An example with enumerated types: If 5 values exist, and only 3 of these were observed, then the coverage score would be 60 % done.

Note that coverage grade calculation is not part of the current specification.