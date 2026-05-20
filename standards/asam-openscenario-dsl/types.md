# ASAM Openscenario Dsl v2.2.0 — 7.3 Types

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/language-reference/types.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.3 Types

## 7.3.1 Type system

ASAM OpenSCENARIO is designed to be strong and statically typed.
All expressions of ASAM OpenSCENARIO have a statically defined type.
ASAM OpenSCENARIO source code can be type-checked before runtime, ensuring that only well-formed scenarios can be executed.

The types are classified according to two properties:

1. A type is either built-in or user-defined.
2. A type is either composed of other types or not.

This leads to the following classes of types:

Primitive types
:   Primitive types are the built-in basic types.
    Primitive types include the following types:

    * Boolean
    * Integer
    * Floating point
    * String

      Of these, the Integer and Floating point types form the set of primitive numeric types in ASAM OpenSCENARIO.

Enumeration types
:   These are user-defined basic types, allowing the user to define purpose-built enumerations of values.

Physical types
:   These are user-defined basic types that enable the user to define types for physical quantities.
    All physical types include unit information.
    Conversions between physical types take those units into account.
    In combination with the primitive numeric types, physical types form the set of numeric types in ASAM OpenSCENARIO.

List types
:   These built-in aggregate types provide containers for the elements of one type.
    The elements in a list can be any other type, except another list type.

Range types
:   These built-in aggregate types represent closed intervals over a numeric base type.
    A range type is written as `range of <T>`, where `<T>` is one of the numeric types, including `int`, `uint`, `float`, or a physical type (e.g., `speed`).
    A value of a range type denotes all values of that type between and including the lower and upper bounds.

Compound types
:   These user-defined types can compose other arbitrary types.
    This includes other composed and non-composed types, as well as methods and further components, depending on the kind of compound type.
    The simplest compound types are structs, which contain fields and methods.
    Scenarios, actions and actors, like structs, comprise fields and methods.
    Scenarios and actions also contain a behavior specification in the form of a do statement.
    Actors can have associated scenarios and actions.

## 7.3.2 Primitive types

Primitive types are the basic built-in data types natively supported by the language.
Note that their names are keywords and not namespaced identifiers, as they are for types that are not built-in.

Primitive types may be extended, which means they can be modified beyond their built-in functionality, through the addition of further methods (see [Section 7.3.9, “Extension”](#sec-lc-extension)).
Note that methods defined in this way are defined using namespaced identifiers, like any other methods.

Code 12. Primitive type extension

```
extend float:
    def doubled() -> float is expression 2.0 * it

extend string:
    def greeter(prefix: string = "Hello") -> string is expression prefix + ", " + it + "!"
```

### 7.3.2.1 Boolean type

The Boolean type, called `bool`, represents binary logical values, which can be either true or false.
The two values are represented by the *literals* `true` and `false`.

Code 13. Boolean field declaration

```
my_bool: bool = true
```

### 7.3.2.2 Integer types

The two primitive integer types are `int` and `uint`:

`int`
:   A primitive integer type that holds signed integer values with 64-bit size.
    It supports the range of whole values from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 inclusively.  
    Integer literals can be denoted in decimal using unadorned integer literals, like `-42`.
    They can also be denoted in hexadecimal, using a prefix of `0x`, for example, `0x0539`.

`uint`
:   A primitive integer type that holds unsigned integer values with 64-bit size.
    It supports the range of whole values from 0 to 18,446,744,073,709,551,615 inclusively.  
    Integer literals can be denoted in decimal using unadorned integer literals, like `42`.
    They can also be denoted in hexadecimal, using a prefix of `0x`, for example, `0x0539`.

The integer types are part of the set of primitive numeric types in ASAM OpenSCENARIO.

Code 14. Integer field declarations

```
my_int: int = -42
my_hexa_int: int = 0x0539
my_uint: uint = 42
my_hexa_uint: uint = 0x0539
```

### 7.3.2.3 Floating-point type

The floating-point type, called `float`, holds floating-point values according to the ANSI/IEEE Std 754-2019 binary64 (formerly called double precision) basic floating-point format.
This includes all defined values as per the standard, including normal and subnormal finite numbers, positive and negative infinities, not-a-number (nan), and positive and negative 0.

Floating-point literals are denoted in decimal using the following format:

```
float-literal ::= ['+' | '-'] ( digit* '.' digit+ [('e' | 'E') ['+'|'-'] digit+] | digit+ ('e' | 'E') ['+'|'-'] digit+ | 'inf' | 'nan' )
```

The floating-point type is part of the set of primitive numeric types in ASAM OpenSCENARIO.

The conversion from `int` and `uint` to `float` is implicit, but the conversion from `float` to `int` or `uint` requires explicit conversion operators.

|  |  |
| --- | --- |
|  | Automatic conversion from `int` or `uint` to `float` can lead to loss of precision for values that are not representable exactly in the 53-bit mantissa of binary64 floating-point format. |

All calculations involving floating-point and physical types shall be performed under the rules of the ANSI/IEEE Std 754-2019 standard, with default round to nearest, ties to even rounding rules, and without any floating point traps enabled.

Code 15. Floating-point field declarations

```
my_float: float = 3.14159
my_exp_float: float = 42.0E4
my_min_exp_float: float = 1e6
my_min_float: float = .5
```

### 7.3.2.4 String type

The string type represents strings of Unicode characters.
It is considered a primitive built-in basic type in ASAM OpenSCENARIO.
No separate type for individual characters is provided.

String literals are denoted using a subset of the Python string literal syntax, as specified in  [Section 7.2, "Language structure and syntax"](language_syntax.html#top-lc-syntax-language).

Code 16. String field declarations

```
my_string1: string = "Hello, World!"
my_string2: string = 'String Value'
```

String methods are discussed in [Section 8.13, "String Methods"](../domain-model/primitive_types.html#sec-primitive_types-string-methods).

## 7.3.3 Enumeration types

Enumeration types are the basic user-defined data types.
They enumerate a finite but extensible set of possible values.

An enumeration type consists of a set of named unique members.
Already declared enumeration types can be extended, extending the set of named unique members.
Each instance of an enumeration type can hold one of the members at any one point in time.

Each enumeration member is assigned an unsigned integer value, either explicitly or implicitly.
By default, the implicit enumeration member values are derived automatically using succeeding integer values from the last explicitly given literal integer value, or from 0 if no such value exists.
If enumeration types are extended, then implicit integer values will be derived as above, with the last existing enumeration member giving the starting point, until an explicit value is given.

When explicitly assigning integer values to an enumeration member, the assigned value can be specified either as a literal value, or by referencing another enumeration member of this or another enumeration by its name.
It is an error if these references form a cycle.
Note that explicitly assigned values using references to another enumeration member are ignored for the purposes of deriving succeeding implicit integer values for enumeration members.
If multiple enumeration members of the same enumeration are assigned the same unsigned integer value, they are considered equivalent, and hence compare as equal in all relational operators.
It is implementation-defined, which literal name is used to present equivalent enumeration values in user interfaces.

Code 17. Enumeration type definitions

```
enum rgb_color: [red, green, blue]
enum cmyk_color: [cyan = 1, magenta = 2, yellow, black]
enum named_color: [tan, mauve, pink, grey, gray = grey, violet, greyish = grey, brown]

extend rgb_color: [alpha]
```

All conversions between integer and enumeration types have to be performed using explicit conversion operators.

Code 18. Conversion

```
# Example enumeration fields
my_rgb_color: rgb_color = green
my_cmyk_color: cmyk_color = black
my_named_color: named_color = gray
my_new_rgb_color: rgb_color = alpha

# Conversion to integer
x: int = my_rgb_color.as(int)     # x == 1
y: int = my_new_rgb_color.as(int) # y == 3
z: uint = my_cmyk_color.as(uint)  # z == 4
a: uint = my_named_color.as(uint) # a == 3
b: uint = grey.as(uint)           # b == 3
c: uint = greyish.as(uint)        # c == 3
d: uint = brown.as(uint)          # d == 5

# Conversion from integer
my_car_color: cmyk_color = 3.as(cmyk_color) # my_car_color == yellow
my_color: named_color = 3.as(named_color)   # my_color == grey == gray == greyish
```

|  |  |
| --- | --- |
|  | The named members of an enumeration type are available as literals of that type. If multiple enumeration types use the same literal, then the literal is overloaded: Which literal and hence value the literal is evaluated to will depend on the type requirements of the place it is used in. If this ambiguity cannot be resolved uniquely, meaning multiple choices would remain valid after type resolution, an error is signaled. |

In order to avoid the potential for such errors, or to be specific which enumeration type is needed, enumeration members can be referenced with the enumeration type prefixed with a separating `!` character.

Code 19. Overloading and using explicit literals

```
# Extend rgb_color again, adding black, which overloads black with cmyk_color!black
extend rgb_color: [black]

# Example enumeration fields
my_rgb_color: rgb_color = rgb_color!green  # Can always use long name
my_cmyk_color: cmyk_color = black          # Resolved to cmyk_color!black
my_new_rgb_color: rgb_color = black        # Resolved to rgb_color!black

# Resolution in expressions
field1: bool = (black == black)            # Could be either type -> error signalled
field2: bool = (rgb_color!black == rgb_color!black)  # True
```

## 7.3.4 Physical types and units

In addition to the primitive numeric types, ASAM OpenSCENARIO supports the definition of physical types.
Physical types represent physical quantities.

The definition of a physical type has to provide two parts:

1. The ***basis*** for representing a physical quantity (like mass).
2. A base ***unit*** that is used to measure that quantity.

The definition of additional units for a given physical type allows the use of other, more common units to define or represent that physical quantity.
Performing unit and dimension checks on all physical calculations is still possible with these newly defined types.

The physical types are commonly used in the domain model, mainly to define entity properties that are of a physical nature.

The unit system employed in ASAM OpenSCENARIO is based on the approach taken in the "Functional Mock-Up Interface for Model Exchange and Co-Simulation", Version 2.0.2.

This approach is based on the *International System of Units (SI)*.

Units are defined by specifying the following properties:

* The exponents of the 7 SI base units (kg, m, s, A, K, mol, cd).
* The exponent of the radian (rad).
* A factor.
* An offset.

The following unit definition specifies 1 as the exponent to the SI base unit meter and 1000.0 as the factor.

Code 20. Defining a new physical unit 'km'

```
unit km of length is SI(m: 1, factor: 1000.0)
```

All units of a physical type have identical exponents for all SI base units and the radian.
All units can therefore be converted directly.
For conversion the base unit value is calculated from the unit value specified according to the following formula:

*base\_unit\_value = unit\_value \* factor + offset*

The basic physical types in ASAM OpenSCENARIO are:

* `mass`
* `length`
* `time`
* `angle`
* `temperature`
* `luminous_intensity`
* `electrical_current`
* `amount_of_substance`

The base units of these types are the SI base units.

The basic physical types and units as well as other types and units (like `speed`, `angular_rate`, `pressure`, and `illuminance`, among others) are defined in the domain model.

Physical types and units are defined using the following syntax:

```
type <quantity Type> is SI(<base_unit>: <exponent>[,...,<base_unit>:<exponent>])
unit <name> of <quantity Type> is SI(<base_unit>:<exponent>[,...,<base_unit>:<exponent>], factor: <float-literal>, offset: <float-literal>)
```

Code 21. More examples for defining units

```
type length is SI(m: 1)

unit m of length is SI(m: 1)
unit foot of length is SI(m: 1, factor: 0.3048)

type speed is SI(m: 1, s: -1)
type acceleration is SI(m: 1, s: -2)

unit |foot/s| of speed is SI(m: 1, s: -1, factor: 0.3048)
unit |foot/s^2| of acceleration is SI(m: 1, s: -2)
unit |foot/s/s| of acceleration is SI(m: 1, s: -2)
unit g of acceleration is SI(m: 1, s: -2, factor: 9.80665)
unit kph of speed is SI(m: 1, s: -1, factor: 0.27777777778, offset: 0.0)
unit deg of angle is SI(rad: 1, factor: 0.0174532925199, offset: 0.0)
unit F of temperature is SI(K: 1, factor: 0.5555555556, offset: 255.372222222)
```

Units are specified in physical type literals by giving the unit name directly after the float literal.

Code 22. Specifying units in physical type literals

```
my_dist: length
keep(my_dist == 15|foot/s| * 3s + 10m)
keep(my_dist == 10m)

my_speed: speed
keep(my_speed == 5m / 2s)
```

A unit specification is a mandatory part of any physical type literal.

Unit names form their own separate global namespace.
All unit names must be globally unique within that namespace.

|  |  |
| --- | --- |
|  | The design of the units does not currently allow the definition of units defined by logarithmic factors of the quantity (for example dBW). This feature might be included in future extensions of the standard. |

## 7.3.5 Compound types

ASAM OpenSCENARIO provides for several compound types that are a means to group together elements that are logically related.
This chapter gives an overview of the compound types available in the language.

Compound types are grouped into [Section 7.3.5.1, “Structured types”](#sec-lc-structured-types) and [Section 7.3.5.2, “Aggregate types”](#sec-lc-aggregate-types).

### 7.3.5.1 Structured types

Structured types provide a way to build complex types from simpler ones.
A structured type acts as a container for its members.

The ASAM OpenSCENARIO language offers four kinds of structured types:

* [Structs](language_syntax.html#sec-lc-syntax-structs)
* [Actors](language_syntax.html#sec-lc-syntax-actors)
* [Scenarios](language_syntax.html#sec-lc-syntax-scenarios)
* [Actions](language_syntax.html#sec-lc-syntax-actions)

Additionally, ASAM OpenSCENARIO provides modifiers, which are similarly structured as scenarios and actions but are not considered a proper structured type in their own right (see [Section 7.3.5.1.5, “Modifiers”](#sec-lc-aggregate-modifiers)).

All of these structured types, as well as modifiers, may contain the following kinds of members:

* [Fields](#sec-lc-fields)
* [Methods](#sec-lc-methods)
* [Event definitions](#sec-lc-events)
* [Constraints](#sec-lc-constraints)
* [Coverage](coverage_main.html#top-lc-coverage-main)

Specific structured types can have additional kinds of members.

Fields represent data members inside structured types.
Each field has a defined type.
When instantiating a structured type, each field holds an instance of its respective type.
A field can be defined as a parameter or a variable.
Methods describe and implement the behavior of an object, which is an instantiation of a class.
Fields, methods, and events are named and must have a unique name within the type.

Structured types may be extended, which means they can be modified after their initial declaration (see [Section 7.3.9, “Extension”](#sec-lc-extension)).

They may also be derived from existing structured types (see [Section 7.3.8, “Inheritance”](#sec-lc-types-inheritance)).
However, a structured type may only be derived from the same kind of type: For example, a scenario cannot be derived from a struct.
The difference between inheritance and extension is that the former creates a new type, while the latter modifies an existing type without creating a new one.

#### 7.3.5.1.1 Structs

There are many situations where multiple values, methods, and other elements belong to a larger entity.
The `struct` types provide the most basic way of composing these into a more complex data type.

Code 23. struct definition

```
enum traffic_light_colors: [red, amber, green]

struct traffic_light:
    id: int
    name: string
    pose: pose_3d
    active_colors: list of traffic_light_colors
    country: string
```

Structs do not offer any additional members beyond the common ones.

#### 7.3.5.1.2 Actors

The `actor` keyword can be used to declare user-defined types of actors.
Actors are entities that can perform actions within a scenario.

Code 24. actor definition

```
actor rock:
    kind: string
    weight: mass
    extent: length
    position: position_3d
```

Actors do not offer any additional members beyond the common ones.

#### 7.3.5.1.3 Scenarios

A scenario is a structured type that describes the behavior of one or more actors in a traffic system.
It can optionally be *associated with* an actor that can be referenced within the scenario via the implicit `actor` field.
This actor is called the *associated actor* and can be interpreted as the actor performing the behavior described in the scenario.
However, within a scenario, the `actor` field and other parameter fields can be used in the same way.
A scenario can have at most one associated actor, but an actor can have multiple associated scenarios.

In addition to the general structured type members, a scenario can contain behavior specifications, in the form of `on` and `do` directives.

Not more than one `do` directive can be effectively present in any scenario or action.
Multiple `on` directives may be present.

The `do` directive allows the specification of unconditional behavior of the scenario, by invoking other behaviors (actions and scenarios).

The temporal relationships behaviors invoked by a scenario are described using scenario composition operators (see [Section 7.3.13, “Scenario composition”](#sec-lc-composition)).
Scenarios can also contain modifier applications (see [Section 7.3.12, “Modifiers”](#sec-lc-modifiers)).

A behavior invocation can include a `with` block that can contain constraint declarations, modifier applications, and `until` directives.
Inside the `with` block, the special expression `it` can be used to reference the invocation that the with block is attached to.

Code 25. scenario definition

```
scenario pass_ego:
    ego: vehicle
    passing_car: vehicle

    do parallel:
        ego.drive() with:
            speed(50kph)

        passing_car.drive() with:
            lane(left_of: ego)
            speed(70kph)
```

The `on` directive allows the invocation of `emit` and `call` directives when the event that is specified in the `on` directive occurs (see [Section 7.3.10, “Event definitions”](#sec-lc-events)).

When invoking behaviors (actions and scenarios) or applying modifiers, arguments passed in through the argument list result in constraints on the parameter fields of the behavior or modifier as follows:

* If a single value of the given declared type (or a subtype thereof) is passed in, an equality constraint between the parameter and this value is active during the invocation:

  ```
  do ego.change_speed(speed: 10kph)
  ```

  is equivalent to the following constraint being applied inside the action:

  ```
  keep(speed == 10kph)
  ```

  and

  ```
  do ego.change_speed(speed_range: [10kph..25kph])
  ```

  is equivalent to the following constraint being applied inside the action:

  ```
  keep(speed_range == [10kph..25kph])
  ```
* If a range expression is passed in for a parameter with a declared numeric type, an in-range constraint between the parameter and this range is active during the invocation:

  ```
  do ego.change_speed(speed: [10kph..25kph])
  ```

  is equivalent to the following constraint being applied inside the action:

  ```
  keep(speed in [10kph..25kph])
  ```

The argument list can make use of positional or named arguments, as described in [Section 7.4.2.1, "Method application"](expressions_main.html#sec-lc-expressions-method-application).

The inheritance of scenarios is restricted in that scenarios associated with an actor must only inherit from a scenario associated with an actor of the same type, or associated with an actor of a more general type.
Scenarios associated with no actor must only inherit from a scenario associated with no actor.

#### 7.3.5.1.4 Actions

Actions are similar to scenarios in that they can have the same members, including optional behavior specifications.

Actions differ from scenarios in that, from the perspective of an ASAM OpenSCENARIO specification, they are seen as atomic behavior descriptions that cannot be further decomposed:
Their internal structure, if any, is to be considered opaque from the point of view of the user.

Implementations are therefore free to implement actions specified in the domain model in implementation-defined ways or using the ASAM OpenSCENARIO language features as they see fit.

For the specialization of actions via inheritance, the same restrictions regarding associated actors apply as for scenarios (see [Section 7.3.5.1.3, “Scenarios”](#sec-lc-types-scenarios)).

#### 7.3.5.1.5 Modifiers

Compound modifier declarations can have the same members as scenario and action structured type declarations, except `do` directives.
Modifiers can influence the behavior by applying them to actors, scenarios, and behavior invocations as well as scenario composition operators.

They are however not considered proper structured types, since they cannot be used as types for fields or arguments, nor do they support inheritance or extension.

Instances of modifiers are only implicitly created through modifier applications.

Modifiers are described in more detail in [Section 7.3.12, “Modifiers”](#sec-lc-modifiers).

### 7.3.5.2 Aggregate types

Aggregate types serve as containers for uniform members of another type.
ASAM OpenSCENARIO provides the list type and range type as aggregate types.

#### 7.3.5.2.1 Lists

A list is an aggregate type that represents an ordered collection of elements of a specific base type.

```
list-type-declarator ::= 'list' 'of' ( non-aggregate-type-declarator | range-type-declarator )
```

A list is an ordered container of unnamed members.
Each list is declared with a specific member type.
All members shall be of this type or of a type derived from it (see [Section 7.3.8, “Inheritance”](#sec-lc-types-inheritance)).
The list’s element type can be any type, except another list type.
Lists have a variable size, but the size can be constrained.

Basic operations on lists are:

* access a member by index
* retrieve the number of contained elements (i.e. the list’s size)
* filter (create a new list with only selected items)
* check if a list contains a specific object / all objects of another list
* compare two lists for equality

Lists can be initialized with comma separated elements in square brackets.
List types don’t have a name.

```
car_list: list of vehicle = [car1, car2]
```

If a list is initialized by using constraints on its elements, the size is automatically constrained to fit the constrained element into the list.
In the following example, the list will automatically have a size of at least 5 so that it contains an element with index 4.
The first four elements (at index 0 to 3) will have unconstrained values.
The list size could be greater than 5, if required to satisfy other constraints.
If there are no other applicable constraints, the list size will be exactly 5.

```
struct point:
    x, y: float

struct data:
    coords: list of point with:
        keep(it[4].x == 1.5)
        keep(it[4].y == 2.5)
```

List operators are discussed in [Section 7.4.2.7, "List operators"](expressions_main.html#sec-lc-operators-list).

#### 7.3.5.2.2 Ranges

A range is an aggregate type that denotes a closed interval of values of a numeric base type.

```
range-type-declarator ::= 'range' 'of' numeric-type-declarator
```

The base type is any of the numeric types, including `int`, `uint`, `float`, or a physical type (e.g., `speed`).

Ranges are constructed using range constructors:

```
range-constructor ::= 'range' '(' expression ',' expression ')' | '[' expression '..' expression ']'
```

`range(<expr>,<expr>)` and `[ <expr> .. <expr> ]` are range constructor expressions where the expressions provide the lower and upper bounds in any order.
The bounds are inclusive.
The rules of range type conversion allow the conversion of scalar numeric types to range types, by creating a range with identical lower and upper bounds, as well as conversions between range types of different base types.
See [Section 7.4.2.8.2, "Range type conversion rules"](expressions_main.html#sec-lc-operators-range-conversions) for details.

```
r1: range of int = [3 .. 7]
r2: range of float = [1.0 .. 0.0]
r3: range of speed = [50kph .. 80mph]
r4: range of length = range(5m, 10m)
r5: range of int = 5                   # Equivalent to [5 .. 5]
```

Range operators are discussed in [Section 7.4.2.8, "Range operators"](expressions_main.html#sec-lc-operators-range).

## 7.3.6 Fields

Fields belong to structs, actors, scenarios, actions, or modifiers.

They represent named data members inside those compound types.

Each field has a name, a defined type, and a value.

At runtime, a field holds a value of the defined type.

A field can be defined as a parameter or a variable:

* A *parameter field* can be assigned a value through constraints.
* A *variable field* can be assigned a value by initializing it with a default value, by using the sample construct, through external procedural code assignment, and by the execution environment providing a value externally.

Code 26. driving\_speed

```
struct driving_speed:
      area: area_kind
      speed: speed
      keep(area == city => speed < 50kph)
      keep(area == highway => speed < 100kph)
      keep(area == school => speed < 30kph)
```

Multiple variables or parameters can be defined in one declaration if they share all of their properties:

Code 27. Multiple fields declared in one declaration

```
struct positive_vector_3d:
      x, y, z: speed = 0kph with:
          keep(it >= 0kph)
```

All of the fields in the declaration have the same type, default value, and constraints.

### 7.3.6.1 Difference between parameters and variables

Within ASAM OpenSCENARIO, fields are separated into *parameters* and *variables*.
Parameters and variables are used to define usability and mutability during two processing stages.
The first stage is *scenario initialization* and the second one is *scenario execution*.

* *Parameters* are assigned their values during *scenario initialization* through constraint propagation.
  The values assigned remain constant over the subsequent scenario execution stage.
* *Variables* can change over time, including *scenario initialization* and *scenario execution* stages.

#### 7.3.6.1.1 Parameters

Parameters are fields that are evaluated and fixed before scenario execution.

An example is the maximal acceleration property of a vehicle behavioral model.
This parameter must be set before the scenario execution.

Parameters have the following properties:

* All fields are parameters by default, if not specified otherwise.
* Parameters are bound during the scenario initialization stage and are fixed from start of scenario execution.
* A parameter value is selected from all the possible values of the field type that comply with all the constraints applicable to that parameter.
  The selection between multiple possible values is arbitrary.
  For example, it can be randomized.
* To set a parameter to a specific value, write a constraint that requires that value.
  An equality constraint is an example of a constraint that can be used in that case.
* Parameters have an optional default value specification.
  Specifying a default value is exactly equivalent to providing an equality constraint of strength `default` with the left-hand side being the parameter, and the right-hand side being the default value expression.

Parameter field declarations can also include an optional `with` block with additional constraint declarations.
Inside the `with` block, the special expression `it` can be used to reference the field that the with block is attached to.

See [Code 29](#code-lc-fields-example-scalar-field) for an example of the `with` block as applied to field declarations.

#### 7.3.6.1.2 Variables

Variables are fields that are allowed to change over time.

A variable receives a default value if no value is assigned to it.
The default value is specified using a default value specification or as part of a sample expression.
The default value is evaluated at the time the instance that contains the variable is instantiated.

A value can be assigned either explicitly or through the connection of the variable to the simulation state.

An example is the current velocity of a vehicle during scenario runtime.
At runtime, a driver model controls the current velocity value.

Variables have the following properties:

* Variables must be specified explicitly with the keyword `var`.
* Variables always have a value.
* Variables are modified and handled by external sources such as driver models or simulators and by the *sample* construct.
* Variables cannot be constrained.
  But parameters can be constrained by sampling the values of the variables during constraint resolution.
* If a variable of structured type is declared, this results in all its fields behaving as variables, even if they are not declared as variables themselves.

Code 28. Constraining parameters by variable value sampling

```
scenario vehicle.follow_vehicle:
    other: vehicle
    distance: length

    do actor.change_space_gap(target: distance, direction: behind, reference: other)

scenario main:
    ego: vehicle
    car1, car2: vehicle
    var dist: length = sample(ego.object_distance(reference: car1, direction: longitudinal), every(2s))

    do serial:
        parallel:
            car1.drive() with:
                speed(50kph)

            ego.drive() with:
                position(behind: car1)

        car2.follow_vehicle(other: ego, distance: dist)
```

### 7.3.6.2 Field examples

#### 7.3.6.2.1 Scalar field declarations

The following example shows an actor with two fields of type speed:

* A variable named *current\_speed* that holds a value specifying the current speed.
  Most likely this variable is assigned different values while a scenario is running.
* A parameter named *max\_speed* that has a default constraint.
  This variable receives a value during the pre-run generation of 120 *kmph*, unless its constraint is overridden.

Code 29. Scalar field declarations

```
actor my_car inherits vehicle (vehicle_category == car):
    var current_speed: speed
    max_speed: speed with:
        keep(default it == 120kmph)
```

#### 7.3.6.2.2 Scenario field

This example shows a struct field *storm\_data* instantiated in a scenario called *env.snowstorm*.
Constraints are set on the two fields of *storm\_data*.
The *wind\_velocity* field is monitored for coverage.

Code 30. Scenario field

```
enum storm_type: [rain_storm, ice_storm, snow_storm]

struct storm_data:
    storm: storm_type
    wind_velocity: speed

scenario env.snowstorm:
    storm_data: storm_data with:
        keep(it.storm == snow_storm)
        keep(default it.wind_velocity >= 30kmph)
        cover(wind_velocity, expression: it.wind_velocity, unit: kmph)
```

#### 7.3.6.2.3 Structured type variables

This example shows a struct variable *current\_position* instantiated in an actor *car*.

Code 31. Structured type variable

```
struct position:
    x: float
    y: float
    z: float

actor car:
    var current_position: position
    keep(current_position.x < 100) # error: cannot constrain current_position.x, because it is treated as a variable
```

## 7.3.7 Methods

A *method* in the context of ASAM OpenSCENARIO is a member function defined within a structured type.
It describes and implements the behavior of an object, which is an instantiation of a class.

A method is a named block of organized and reusable code that can be invoked to perform a specific task and to return values.
In the overall semantics of ASAM OpenSCENARIO, method invocation is a zero-time mechanism, even if the actual execution of a method implementation consumes wall-clock time.

Code 32. Method definitions

```
def even_items(arg1: list of int) -> int is expression arg1.filter(it % 2 == 0)
def my_add(x: float, y: float) -> float is expression x+y

def my_sin(x: float) -> float is external com.example.cpp(identifier: "sin")

def my_distance(x1: float, y1: float, x2: float, y2: float) -> float is undefined

def my_distance(x1: float, y1: float, x2: float, y2: float) -> float is only external com.example.python(module: "mymod", name: "my_dist")
```

Each method has a fully specified type signature, which is given as part of the declaration of the method:

Code 33. Method declaration syntax

```
def <method-name>(<argument-list-specification>) [-> <return-type>] <method-implementation>
```

For each method argument, its name and type are specified:

Code 34. Method definition

```
def my_add(x: float, y: float) -> float is expression x+y
```

Optionally default values can be specified for arguments:

Code 35. Method definition

```
def my_add(x: float, y: float = 1.0) -> float is expression x+y
```

This allows the caller of a method to not provide a value for a given argument.
Inside the method body, the argument will then have the value of the expression given as the default value.
This expression is evaluated at the time of the method invocation, prior to the execution of the method implementation.
It is only evaluated when no value for the argument is passed in the invocation of the method.

The optional type of the returned value of the method is specified after the argument list declaration.

Methods without a declared return type can only be invoked with the `call` directive in behavior specifications.
They cannot be invoked in other expressions.

Code 36. External logging method

```
def my_value_logger(val: float) is external com.example.cpp(identifier: "my_logger")
```

A method declaration is followed by the method implementation.
There are two basic kinds of implementations for a method:

* *Expression methods* are implemented by providing an ASAM OpenSCENARIO expression that yields the return value as the result of its evaluation.
* *External methods* are implemented outside of ASAM OpenSCENARIO.
  The mechanism to bind implementations to the method declaration is implementation-specific.

### 7.3.7.1 Undefined methods

Additionally, a method can be explicitly left unimplemented, making it an undefined method:

Code 37. Undefined method syntax

```
def <method-name>(<argument-list-specification>) [-> <return-type>] is [only] undefined
```

An undefined method can only be invoked if an overriding implementation is provided through inheritance or extension.
If an undefined method is invoked without an implementation, an error is raised.

|  |  |
| --- | --- |
|  | It is intentionally left open whether implementations will only detect this at runtime or can already detect this at compile time through static analysis. In either case, an error is only raised if an undefined method is actually invoked, not if there is just the potential that it could be invoked. |

### 7.3.7.2 Overriding methods

When methods are overridden through inheritance or extension mechanisms, the overriding method implementation must contain an `only` qualifier.
Otherwise, an error is raised.

An error is raised if the method type signature of an overriding method is different from the method it is overriding.

It is not an error if a method definition contains an `only` qualifier and there is no existing method to be overridden.

For overriding, the ordering is based on the inheritance relationships of the types that the methods are defined in.
For the ordering of extensions that have the same inheritance relationship, the textual order of the extensions is used.

### 7.3.7.3 Expression methods

Expression methods are implemented by providing an ASAM OpenSCENARIO expression that yields the return value for a method invocation.
The expression can reference the named arguments of the method as well as all other fields that are in scope.

Code 38. Expression method syntax

```
def <method-name>(<argument-list-specification>) [-> <return-type>] is [only] expression <expression>
```

### 7.3.7.4 External methods

The implementation of an external method can be defined in any programming language that is supported by the ASAM OpenSCENARIO implementation:
The structured identifier in combination with the optional argument list provides an implementation-defined specification of the external method definition.
The ASAM OpenSCENARIO implementation uses this information to locate the external method implementation.

|  |  |
| --- | --- |
|  | A future release of ASAM OpenSCENARIO might standardize specifications for the support of certain external languages. For this reason, a set of identifiers is reserved for use in future versions of the specification. |

Any structured identifier starting with the identifier `osc` is reserved for future use.

Code 39. External method syntax

```
def <method-name>(<argument-list-specification>) [-> <return-type>] is [only] external <structured-identifier>(<argument-list>)
```

## 7.3.8 Inheritance

Inheritance in ASAM OpenSCENARIO takes on a role similar to other class-oriented languages.
It is a mechanism of basing a class upon another class, retaining its members and behavior while allowing the new class to modify them to its needs.
Inheritance can be applied to structs, actors, scenarios, and actions.

ASAM OpenSCENARIO provides two types of inheritance:

* Unconditional inheritance
* Conditional inheritance

### 7.3.8.1 Unconditional inheritance

ASAM OpenSCENARIO allows single inheritance between extensible classes.
This works like inheritance in most OO programming languages: A new subtype is declared, endowed with all the features of the parent type (supertype).
Both types are accessible.

Modifications to the supertype are automatically applied to the subtype.
Changes to the subtype do not affect the supertype.

Code 40. Unconditional inheritance

```
struct base:
    f1: bool

struct derived inherits base:
    f2: bool          #derived has both f1 and f2 fields
```

The inherited structured type members are retained in the inheriting type.
The inheriting type can add new structured type members that are valid for the structured type.

For method members, the inheriting type can also override existing method implementations as specified in [Section 7.3.7.2, “Overriding methods”](#sec-lc-types-overriding-methods).

Any added members must, in combination with any existing members, still fulfill all relevant restrictions for the specific compound type:
For example, not more than one `do` directive can be effectively present in any scenario or action.

The inheritance of scenarios and actions is restricted in that:

* scenarios and actions belonging to an actor must only inherit from a scenario or action belonging to an actor of the same type, or an actor of a more general type, and
* scenarios and actions not belonging to an actor must only inherit from a scenario or action not belonging to an actor.

### 7.3.8.2 Conditional inheritance

Conditional inheritance enables the creation of subtypes that depend upon a value of a Boolean or enumerated field in the base type.
The condition always sets a single field to a specific value.
The field value (determinant) is a constant literal that is fixed during execution.

Conditional inheritance is specified by declaring the field and value that defines the dynamic subtype.

#### 7.3.8.2.1 Defining conditional inheritance

Code 41. Conditional inheritance

```
extend vehicle:
    is_electric: bool

actor truck inherits vehicle (vehicle_category == truck):
    ...                    # Fields / methods / events unique to truck

actor electric_vehicle inherits vehicle(is_electric == true):
    ...                    # Fields / methods /events unique to electric_vehicle
```

Why is conditional inheritance based on attributes?

* Because this allows for multiple orthogonal dimensions.

  + Like truck, bus, and so on, but also electric\_vehicle versus non-electric.
* Because it lets you add constraints on the attributes.

  + For example, "I want 20% trucks", or "No electric buses".
* Because in verification, initially, you do not know if you want sub-types.

  + Perhaps you just have the *is\_electric: bool* field, and later you want to make it into a sub-type (for example, to add the remaining\_charge field).

#### 7.3.8.2.2 When to use conditional inheritance

Use ***conditional inheritance*** in the following cases:

* When you want the type to auto-specialize to the "right" sub-type.
* For example, define *tp: traffic\_participant* and it becomes a person / animal / vehicle.

Use ***unconditional inheritance*** in the following cases:

* When you do not want the type to auto-specialize to the "right" sub-type.
* For example, define `r: road`, and it will not become child-of-road.

There is no way to auto-specialize in unconditional inheritance.

The reasons are:

* It is unclear, which sub-types can live together.
* It is unclear, if you need to specialize.  
  For example, if you only created sub-types for the "special" cases, but the parent actor can also be used sometimes.

#### 7.3.8.2.3 Relations between conditional and unconditional Inheritance

The rule governing the relationship between these two kinds of inheritance is as follows:

* **Rule 1:** A conditional type cannot be inherited unconditionally.

Inheritance relationships form a tree whose trunk is the predefined types.
Main limbs are inherited unconditionally.
The final branches of the unconditional inheritance tree can be the roots of conditionally inherited sub-trees.

#### 7.3.8.2.4 Relations between conditional subtypes

Any pair of conditional subtypes (types conditionally inherited from the same supertype) have one of the following relationships:

* One of the types can be a supertype of the other.
* Both types have a common supertype (meaning they are orthogonal).

#### 7.3.8.2.5 Type membership

Consider a field declared as type *car*.
It may be assigned an object whose *emergency\_vehicle* field is set to *true*.
Because the field is declared as type *car*, its value must be an instance of *car*, and only features of *car* are accessible.

The language also provides type-membership checking, using the *is()* and *as()* operators.
Using type checking, you can access features under an active subtype, even though it is not the declared type.
Such active but undeclared subtypes (*police\_car* in this example) are called latent subtypes.
This is summarized by the following two rules:

* **Rule 2:** The declared type determines the type membership of an object.
* **Rule 3:** Dynamic type check allows access to latent subtype features.

Code 42. Inheritance example defining a police car

```
extend vehicle:
    emergency_vehicle: bool

actor car inherits vehicle (vehicle_category == car):
    ...             # Fields / methods /events unique to car

actor police_car inherits car(emergency_vehicle == true):
    ...             # Fields / methods /events unique to police_car
```

## 7.3.9 Extension

An extension enables the user to manipulate elements that are already defined in the code.
Manipulation in this case means adding, changing, or fine-tuning.

All instances of a type are endowed with the union of features declared in all the extensions of that type.

Features in an extension cannot shadow previously declared features.
But some features, like method declarations, allow overrides.

Extension modifies the type being extended.
All instances of the type get the newly added features.
For instance, adding a *weight* field to the *car* actor adds this field to every *car* in every scenario.

|  |  |
| --- | --- |
|  | Extension is different from inheritance, where you define a new type. |

Extension is helpful if a library of inter-related actors and scenarios already exists, and you just want to add some fields, constraints, scenarios, or other features to accommodate project-specific needs.

Extension can be applied to the following entities:

* *Primitive types*  
  Adding new methods to primitive types, or overriding method implementations.
* *Enumerated types*  
  Adding new items to an already defined enumerated type.
* *Structs, actors, scenarios, actions*  
  Adding new structured type members, for example, fields, methods, or events - or overriding method implementations.
* *Coverage*  
  Fine-tuning coverage item behavior.

Extensions are applied at compile time.

Any added members must, in combination with any existing members, still fulfill all relevant restrictions for the specific compound type:
For example, not more than one `do` directive can be effectively present in any scenario or action.

## 7.3.10 Event definitions

### 7.3.10.1 Introduction

*Events* are named entities, signifying a zero-time occurrence in time.
Events can optionally have parameters describing that occurrence.
Typically, events are used to indicate the occurrence of a particular situation.

* The start, end, or failure of a scenario are predefined events.
* Via *event specifications*, events can be specified to occur when a certain condition renders true.
* Events can also be emitted and waited for by scenarios, which provides means for synchronizing concurrently active scenarios.

Events are defined using the `event` structured type member declaration.

For example:

```
event car_arrived                             # An event with no parameter
event accident_occurred(other_car: vehicle)   # An event with a single parameter
event e1 is @e2 if (x > y)                    # An event with a formula
```

*Event specifications* are specifications of conditions for the occurrence of an event.
They are used in different places, such as the `wait` statement, to specifically describe the event that is waited for, or in the `on` directives, to specify the event that shall trigger a specific behavior.
Event specifications can also be used in an event declaration to describe a condition under which the event occurs.

For example:

```
on @x.accident:                # When the event happens, do something
     call dut_error(...)
wait distance_to(car2) < 10m   # Wait until the expression is true
event e1 is @e2 if (x > y)     # Emits e1 when e2 happens and the Boolean expression returns true
```

### 7.3.10.2 Events

Syntax:

```
event <name> [(<argument-list-specification>)] [is <event-specification>]
```

Events are declared as members of any structured object.

Events have a name, and optional arguments (parameters).
The arguments are specified like the arguments to a method definition:
Each argument has a name, a type, and an optional default value.
The default value expression is evaluated at the time of an event being emitted if no value is provided for the given argument.
The result of evaluating the default expression is then used as the value for the argument as if provided by the event emitter.

An event can have an event specification that describes an event or a condition, or both, under which the event is emitted.
An event specification is only allowed to be provided for events with no parameters.

Events are inherited as any other structured type members.
Their declaration can be overridden by inheriting types.

Events are emitted in one of the following ways:

* Via `emit` directives
* Through external code
* By declaring an event with an event specification that specifies a condition under which the event occurs
* Executing scenarios triggers certain built-in scenario life cycle events (see [Section 7.3.10.3, “Pre-defined events”](#sec-lc-type-pre-defined-events))

The *emit* directive emits an event and specifies values for all parameters (for events with parameters).

```
emit <event-path> [(<argument-list>)]
```

### 7.3.10.3 Pre-defined events

The following events are pre-defined for all scenarios:

* The `start` event marks the beginning of the execution of a scenario.
* The `end` event is emitted when a scenario execution is finished.
* The `fail` event is emitted if the scenario cannot reach its end – for example, if the allotted duration time elapses.

### 7.3.10.4 Event specifications

The syntax of an event specification is as follows:

```
@<event-path> [[as <event-field-name>] if <event-condition>]
```

Alternatively, just an event condition can be provided:

```
<event-condition>
```

An event specification is said to produce an event occurrence:

* If just the *event condition* is specified, the event occurs whenever the condition evaluates to `true`.
* If just the *event-path* is specified, then the event occurs whenever that event occurs.
* If both are specified, then whenever the event occurs, the *event condition* is evaluated: If it evaluates to `true`, the event occurs.

An *event condition* can consist of one of the following expression types:

* *bool expression*: An expression that returns a value of type `bool`, which is the value of the condition.
* *rise expression*: Returns `true` when the *bool expression* specified inside the parentheses changes values from `false` to `true`, otherwise returns `false`.
* *fall expression*: Returns `true` when the *bool expression* specified inside the parentheses changes values from `true` to `false`, otherwise returns `false`.
* *elapsed expression*: Returns `true` from the first time instant when the time that passed from the start of the *event context* equals or exceeds the *duration expression* specified inside the parentheses, and all later time instants.
  Returns `false` otherwise.
* *every expression*: Returns `true` at each first time instant when the time that passed from the start of the *event context* equals or exceeds a multiple of the *duration expression* specified inside the parentheses.
  Returns `false` otherwise.
  If an optional `offset` named argument is included, then the first instance (and all further instances) will be offset into the future by the given duration.
  Otherwise, the first instance will be at the start of the *event context*.

The start of the *event context* is defined as follows:

* If the event specification is used in a `wait` directive, the start of the event context is the start of the execution of the `wait` directive.
* If the event specification is used in an `until` directive, the start of the event context is the start of the execution of the annotated behavior invocation or composition.
* If the event specification is used in an `on` directive, the start of the event context is the start of the execution of the scenario or action that contains the `on` directive.
* If the event specification is used in a `sample` expression, the start of the event context is the start of the execution of the scenario or action that directly or indirectly contains the variable declaration that uses the `sample` expression.

If an event specification is used in an event declaration, the event context of the event specification will be the event context of the place of use of the declared event.

For `elapsed` and `every` expressions, as well as for the evaluation of pure event conditions, the minimum internal time resolution or time quantum of an implementation is implementation-defined.

If the minimal time quantum is not sufficiently small to allow an implementation to hit the trigger points exactly, then the trigger points will be moved to the next possible time instant.

Implementations should take the required trigger points into account when they are capable of determining suitable minimum time quanta.

If an *event-path* is specified, then the referenced event occurrence can be bound to a field using the `as <event-field-name>` clause:
This clause makes a field with the given name available in the current context, that holds the *event object*, to allow access to its parameters.

Aside from the declaration of events, event specifications are used in the following language constructs:

* `wait` directive, delaying the execution of a scenario until the specified event occurs.
* `on` directive, executing actions immediately when the specified event occurs.
* `until` directive, terminating a nested scenario when the specified event occurs.
* Sampling of values using `sample()` when the specified event occurs.

Some use cases require accessing information about an event after it has occurred, which is possible in ASAM OpenSCENARIO.
The *scope* of the event specified in an event specification is as follows:

* `on` directive: The event field name defined in the event specification of the `on` directive can be used within the body of the `on` directive, for example, to access an event parameter and pass it to the call of an external method.
* `sample` statement: The event field name defined in the event specification used within a `sample` statement can be used within the expression part of the `sample` statement.
* In all other cases, such as `wait` or `until`, an event cannot be accessed beyond the event specification. That is, the event field name can only be used within the `if` clause of an event specification if one is present.

### 7.3.10.5 Examples

```
until (dist(v1, v2) < 10)

on @traffic.accident:
    log_info("Accident happened")

do serial:
    bike.drive() with:
        lane(1, from: right)
        until @observation_complete
```

Wait example:

```
do one_of:
    wait @car1.accident if (x > y)   # When car1 had an accident and x is bigger than y
    wait rise(terrible_accident)     # When terrible_accident changes from false to true
    wait elapsed(20sec)              # When 20 seconds have passed
car2.stop()
```

In the above example `car2` will stop if one of the following happens:

* `car1` emitted the event `accident` and `x` is bigger than `y`
* `terrible_accident` changes from `false` to `true`
* 20 seconds have passed

A more complex example:

```
actor car inherits vehicle (vehicle_category == car)

scenario main:
    dut: car
    do t: dut.test_drive()

scenario car.test_drive:
    event go
    event brk(dx: length)
    car1: car
    def measure(d: length) is external myext("measure")

    do parallel:
        serial:
            emit go   (1)
            d1: dut.drive()
            emit brk(dx: 10m)   (2)
        serial:
            wait @go
            d2: car1.drive()
            wait @brk as dat if dat.dx < 20m   (3)

    on @brk as s if s.dx > 5m:   (4)
        call measure(s.dx)
```

|  |  |
| --- | --- |
| **1** | The `go` event is emitted. |
| **2** | The `brk` event with a `dx` of 10 m is emitted. |
| **3** | The scenario execution ends when `dx` is less than 20 m. |
| **4** | If the distance `dx` is greater than 5 m on emission of the `brk` event, execute the `on` modifier. |

In the above example the `go` event is emitted, enabling `car` to perform `drive()` and then wait for the `brk` event.
When `brk` is received with the proper distance, execution ends.
The event `brk` may also cause the `on` modifier to execute, depending on the Boolean condition.

## 7.3.11 Constraints

A constraint restricts the range of possible values that parameter fields may have during scenario execution.
In this chapter, the construct of constraints is introduced and its structure and functionality are explained.
See  [Section 7.6, "Semantics"](Semantics.html#top-lc-semantics) for the interaction of constraints and overall semantics.

### 7.3.11.1 Declaration and mandatory body of constraints

Constraints can be declared as members of a structured type, which may be a `struct`, a `scenario`, an `action`, an `actor`, or a `modifier`.
They can also be declared using a `with` clause on specific fields and on behavior invocations within a `do` directive.
Declaring a constraint in a `with` clause of a field is equivalent to declaring it directly as a member.
In a structured type declaration, constraints are declared using the keyword `keep`, followed by a Boolean expression.
This Boolean expression is the mandatory part of the constraint body.
It defines the relationship between any fields referenced in the expression.
A constraint is considered satisfied if the expression evaluates to true.

The fields that are referred to in the Boolean expression may reside in the same instance of a structured type.
The fields may also refer to scopes of different instances.
In the second case, those fields must be identified using path expressions to access the respective scope.

Any Boolean expression can be used in constraints (see  [Section 7.4, "Expressions"](expressions_main.html)).
In a constraint, there should be at least one parameter that is affected by the constraint.

See [Section 7.2.2.4.3, "Constraints"](language_syntax.html#sec-lc-syntax-constraints) for the syntax of constraint declarations.

### 7.3.11.2 Time aspect of constraints

Scenario execution is a multi-stage process.
The set of constraints that are applicable at any point in time is determined according to the rules described in this section.

This section uses the term *"applying"* constraints instead of *"satisfying"* constraints:
A constraint is applicable and is therefore applied when it pertains to the current point in time of scenario execution.
Whether an applicable constraint needs to be satisfied depends on the strength of the constraint itself and other applicable constraints, as described in [Section 7.3.11.3, “Constraint strength”](#sec-lc-types-constraint-strength).

Constraints are applied as long as their scope is active.
Constraints apply for the lifetime of the instance of the structured type in which they are declared.

If a constraint is placed inside the declaration of a scenario, then the constraint applies to the lifetime of that scenario.

If a constraint is placed inside a behavior invocation (meaning a scenario invocation or an action invocation) inside a scenario, then the constraint applies only to the lifetime of that invocation.

The following is an example of the case that a constraint is placed inside a behavior invocation:

* The invocation part inside the scenario is serially composed of two actions.
* Inside of one action, a constraint is declared.
* This constraint does not apply to the second action.

Code 43. A constraint inside a behavior invocation

```
actor car inherits vehicle (vehicle_category == car):

scenario car.lose_constraint:
    do serial():
        actor.assign_speed() with:
            keep(it.speed <= 30kph)
        actor.drive()        # Constraint keep(it.speed <= 30kph) does not apply anymore.
```

If a constraint references different scopes, the path expressions of those scopes must be valid whenever the constraint is applied.

### 7.3.11.3 Constraint strength

Two constraint strengths are defined:

* Hard constraint
* Default constraints

The different constraint strengths have implications on which applicable constraints need to be satisfied.
The constraint strength applies to the whole constraint body.

#### 7.3.11.3.1 Hard constraints

* If no prefix is given, a constraint is considered a hard constraint.
* Hard constraints *must* be satisfied.
  If this is not possible, an error must be raised.
* Hard constraints may not be overridden.

  ```
  keep (x<3)    # This restricts x to any value less than 3
  keep (x==2)   # This must restrict x to the value of 2. It can be applied together with the first constraint
  keep (x==5)   # This contradicts the first two constraints, so an error must be raised.
  ```

#### 7.3.11.3.2 Default constraints

* A default constraint is created by prefixing the expression with the keyword `default`
* Alternatively, providing a default value for a field can be used as a short-hand notation for creating a default constraint for equality of this field
* Default constraints must be satisfied unless they are overridden.
  If this is not possible, an error must be raised.
* A default constraint can be overridden by another default or hard constraint which appears after it (in textual order).
* It can also be explicitly overridden with the remove default operator `remove_default(<parameter>)`.
  This operator has the effect of removing all prior (in textual order) default constraints that influence that parameter.
  After the use of this operator, new constraints on the parameter may be stated with new keep clauses.
* A short-hand notation for implicitly overriding a default constraint can be used: A default constraint can be overridden directly with a `keep` clause if the following two conditions are met:

  + The overriding keep clause is either an equality or a range constraint.
  + The overriding keep clause has the parameter as the only expression on the left side of the Boolean expression.

Code 44. Default Constraints

```
x: int                  # Declare field x
keep (default x == 3)   # Create a default constraint on field x

x: int = 3              # Equivalent to the previous two lines
```

Code 45. Overriding

```
keep (default x==2)
keep (x > 100)          # Error: This does not override the default constraint, because it is not an equality or range constraint on the field.
keep (x + 5 == 1)       # Error: This does not override the default constraint, because the parameter is not the only expression on the left side of the Boolean expression.
keep (true => x == 6)   # Error: This does not override the default constraint, because it is not an equality or range constraint on the field.
keep (7 == x)           # Error: This does not override the default constraint, the overridden parameter must be on the left side of the equality or range constraint.
keep (x == 5)           # Implicit way of overriding: This must restrict y to the value of 5 instead of 2.

keep (default y==2 and z==1)   # this declares a default constraint that applies to the two parameters y and z
remove_default(y)              # Explicit way of overriding (step 1): Removes all default constraints that apply to y.
keep (y > 100)                 # Explicit way of overriding (step 2): Must restrict y to greater than 100.
```

#### 7.3.11.3.3 Full constraint syntax

This leads to the following full constraint syntax:

Code 46. Full constraint syntax

```
keep ([ hard|default ] <boolean-expression>)
```

### 7.3.11.4 Constraints inside a scenario invocation

The following example shows how a scenario can be further constrained within its invocation:

Code 47. Constrained scenario example

```
actor car inherits vehicle (vehicle_category == car)

scenario car.follow:
    other: car
    distance: length
    keep(distance < 50m)   # distance must be less than 50m on any invocation of this scenario.

scenario main:
    dut: car
    c: car

    do c.follow() with:
        keep(it.other == dut)
        keep(it.distance == 20m)   # distance is constrained to 20m for this scenario invocation.
```

A short-hand notation allows to express the equivalent invocation with passing parameters:

Code 48. Constrained scenario example with parameter passing

```
actor car inherits vehicle (vehicle_category == car)

scenario car.follow:
    other: car
    distance: length
    keep(distance < 50m)   # distance must be less than 50m on any invocation of this scenario.

scenario main:
    dut: car
    c: car

    do c.follow(other: dut, distance: 20m)   # Passing parameters, distance is constrained to 20m for this scenario invocation.
```

## 7.3.12 Modifiers

Modifiers are the means for modifying the behavior of actors or scenarios.
A modifier has one *declaration* and is possibly *applied* multiple times.

Different types of *associations of modifiers* influence what a modifier can be applied to.

The three types of *associations of modifiers* are:

1. **Actor-associated modifiers**  
   Modifiers can be associated with a specific actor type.
   These modifiers can be applied within a scenario type declaration to fields or path expressions representing actor instances of the associated actor type.
   Modifier applications can either appear as direct scenario members, or they can appear within the *with* block of a behavior invocation (of *do* section of the scenario declaration).
2. **Scenario-associated modifiers**  
   Modifiers can be associated with a specific scenario type.
   These modifiers can be applied to invocations of the associated scenario inside the *with* block of the invocation.
   Modifiers can also be applied as a scenario member, for example within an extension of the associated scenario type.
3. **Unassociated modifiers**  
   Modifiers may not be associated with any scenario or actor.
   Applications of unassociated modifiers can appear as members in scenario type declarations, or they can appear within the *with* block of a behavior invocation.

ASAM OpenSCENARIO provides two types of modifiers:

1. Atomic modifiers  
   Modifiers, whose implementation is atomic.
2. Compound modifiers  
   Modifiers, whose implementation is created by using scenario members.

### 7.3.12.1 Atomic modifiers

Atomic modifiers are modifiers that are built into the language or come as part of a vendor library.

Vendor-supplied modifiers have implementations that are beyond the scope of this document.

Following is the list of atomic modifiers that are part of ASAM OpenSCENARIO.

#### 7.3.12.1.1 Override modifier

The `override()` modifier allows defining that a specific behavior invocation is of higher priority than another behavior invocation.
Therefore the specific behavior should override the behavior of the lower behavior, meaning that the lower-priority behavior shall terminate upon the start of the higher-priority behavior.

The `override()` modifier has three parameters:

1. The *overridden* behavior invocation  
   Specifies the behavior invocation to be overridden.
   Can be specified by a path expression such as "x.y.z".
2. The *by* behavior invocation  
   Specifies the behavior invocation doing the overriding.
   This can also be specified by a path expression.
3. The *mode*, which can be `on_start` (default) or `when_active`

   * `on_start` means, that the *overridden* behavior invocation shall terminate when the *by* behavior invocation starts, even when it is already active.
   * `when_active` means, that, in addition to the *on\_start* condition, the *overridden* behavior invocation shall not start during the entire time the *by* behavior invocation is active.

These parameters are specified positionally.

For example:

```
override(X, Y) # Override X when Y starts
override(X, Y, when_active)  # Override X when Y starts or is active
```

Code 49. Overriding a specific invocation

```
parallel:
    X: cut_in_and_slow()
    serial:
      foo()
      Y: bar() with:
         override(X, Y)
```

In this example, the start of `Y: bar()` terminates `X: cut_in_and_slow()`.

Example: `a1()` should be done.
When event `@e2` happens, `a2()` should be done.
When `@e3` happens, `a3()` should be done.
Note that `@e2` could happen either before or after `@e3`.

`a1()`, `a2()` and `a3()` are contradictory, so only one of them should run at any one time.

The example can be written like this:

Code 50. Last one wins

```
parallel:
   a1: a1()
   serial:
      wait @e2
      a2: a2()
   serial:
      wait @e3
      a3: a3()
with:
   override(a1, a2)
   override(a1, a3)
   override(a2, a3)
   override(a3, a2)
```

If `a3` starts up last, it finds `a2` already there.
`a3`, therefore, terminates `a2`.

|  |  |
| --- | --- |
|  | This corresponds to the ASAM OpenSCENARIO XML 1.3.1 concept of *"overwrite"*. |

If the same behavior as in the previous example should be achieved, but with the first one (of `a2` and `a3`) winning, simply change the last two lines to:

```
   override(a2, a3, when_active)
   override(a3, a2, when_active)
```

If `a3` arrives last, it finds `a2` already active.
Therefore it does not start (and vice versa).
Note that the check of *"should `a3` even start"* is performed first, before it has a chance to start and thus overrides `a2`.

|  |  |
| --- | --- |
|  | This corresponds to the ASAM OpenSCENARIO XML 1.3.1 concept of *"skip"*. |

#### 7.3.12.1.2 Compound modifiers

Compound modifiers declarations are created by using scenario members, except `do` blocks.

Compound modifiers can be defined by a user or be part of a vendor library.

Compound modifiers can be applied in the following contexts:

* In a scenario, as a scenario member:  
  The modifier applies for each invocation of the scenario.
* In a scenario, inside a `with` block of a behavior invocation:
  The modifier applies for that behavior invocation only.
* In a scenario, inside a `with` block of a composition operator:  
  The modifier applies for the duration of the behavior defined by the composition operator.

For modifier application, a composition operator is treated like any other behavior invocation:
A modifier applied to a composition operator (a composition of certain scenario invocations or other compositions) behaves like applying the modifier to a scenario with the behavior specification consisting solely of the same behavior composition within its `do` block.
If a compound modifier is applied to a composition operator, the special expression `it` can be used to access the parameters of the composition operator application.

### 7.3.12.2 Modifier declaration

Code 51. Modifier declaration syntax

```
modifier <modifier-name>:
    <scenario-member-decl>...

modifier [<actor-name>.]<modifier-name> [of <qualified-behavior-name>]:
            <scenario-member-decl>...
```

* `<actor-name>`  
  The name of the actor type to which this modifier belongs.
  The actor members can be accessed from within the modifier using the special (implicit) field `actor`.
* `<modifier-name>`  
  A unique name, either in the actor scope (if an actor is specified) or the global scope (if an associated actor is not specified).
* `of <qualified-behavior-name>`  
  This modifier can be applied only to an invocation of the specified scenario or as a member of that scenario.  
  The scenario members can be accessed from within the modifier using the special expression `it`.

### 7.3.12.3 Modifier association types

Modifier declaration can be separated into the three types of association:

1. ***Unassociated modifiers***  
   Modifiers that are not associated with any specific actor.

   Code 52. Unassociated modifier example

   ```
   modifier force_lane():   # define a global modifier that forces a vehicle to be in a specific lane
      vehicle: vehicle      # when this modifier is applied, specify the vehicle
      lane: int             # when this modifier is applied specify the lane the vehicle needs to be in
      ...
   ```
2. ***Actor-associated modifiers***  
   Modifiers that need to be applied to a specific actor.

   Code 53. Actor-associated modifier example (keep\_lane() is defined in the domain model (see [Section 8.9.16, "Modifier keep\_lane()"](../domain-model/movement-modifiers.html#sec-dm-actions-drive-modifiers-keep-lane))

   ```
   modifier vehicle.keep_lane(): # modifier keeps actor in lane (default: current lane)
      lane = actor.lane          # access context actor via 'actor' field; parameter is assigned during modifier instantiation
      keep(actor.lane == lane)   # constraint to keep the lane to the lane initially assigned
   ```
3. ***Scenario-associated modifiers***  
   Modifiers that can be applied as a member of a specific scenario, or inside a `with` block of an invocation of that scenario.

   Code 54. Scenario-associated modifier

   ```
   modifier vehicle.follow_vehicle() of drive: #define a modifier that belongs to a vehicle that follows a specific vehicle only inside a drive
      target: vehicle # when this modifier is applied, specify the target the vehicle has to follow
      ... # here one can use 'it' to refer to the specific driver()
   ```

### 7.3.12.4 Modifier application

#### 7.3.12.4.1 Modifier application syntax

The syntax to apply a modifier is similar to that for scenario invocation:

Code 55. Modifier application syntax

```
[<actor-expression>.]<modifier-name>([<expression>[,...,<expression>][,<argument-name: expression>[,...,<argument-name: expression>]]])
```

* `<actor-expression>`  
  An expression specifying the actor of that modifier (if it exists).
* `<modifier-name>`  
  The name of the modifier.

  + `<expression>`  
    An expression passed to a parameter field of the modifier in the order of the parameter fields.
  + `<argument-name: expression>`  
    Expressions can be passed in any order if the parameter field name is specified.

An expression for a parameter is acting as a constraint on that parameter field:

* If a single value of the given declared type (or a subtype thereof) is passed in, an equality constraint between the parameter and this value is active during the invocation:

  ```
  do ego.drive() with:
      speed(speed: 10kph)
  ```

  is equivalent to the following constraint being applied inside the modifier:

  ```
  keep(speed == 10kph)
  ```

  and

  ```
  do ego.drive() with:
      speed(speed_range: [10kph..25kph])
  ```

  is equivalent to the following constraint being applied inside the modifier:

  ```
  keep(speed_range == [10kph..25kph])
  ```
* If a range expression is passed in for a parameter with a declared numeric type, an in-range constraint between the parameter and this range is active during the invocation:

  ```
  do ego.drive() with:
      speed(speed: [10kph..25kph])
  ```

  is equivalent to the following constraint being applied inside the modifier:

  ```
  keep(speed in [10kph..25kph])
  ```

Modifiers can be applied in two places:

1. Modifier application as a member

   * The modifier applies to the whole scenario execution (or to the struct/actor).
2. Modifier application within a `with` block

   * The modifier applies only for that `with` block.
   * A modifier-associated actor can be omitted when it is the same as the scenario actor the modifier is applied in.

#### 7.3.12.4.2 Modifier application examples

##### Applying an unassociated modifier

Code 56. Applying an unassociated modifier

```
scenario top.drive_in_lane:
    my_lane: int with:   # the lane that the vehicle should drive in
        keep(default it == 0)
    v: vehicle
    force_lane(vehicle: v, lane: my_lane)   # use an unassociated modifier to require the vehicle to be in lane my_lane
    do serial:
       v.drive(...) with:
           force_lane(vehicle: v, lane: my_lane)   # use an unassociated modifier to require the vehicle to be in lane my_lane in this drive only
```

##### Applying an actor-associated modifier

Code 57. Applying an actor-associated modifier to an actor within a scenario

```
scenario top.drive_in_lane:
    my_lane: int   # the lane that the vehicle should drive in
    v: vehicle
    v.keep_lane()   # use a modifier to require the vehicle to stay in the current lane
    do serial:
       v.drive(...) with:
           keep_lane()   # use a modifier to require the vehicle to stay in the current lane in this drive only
```

##### Applying an actor-associated modifier within an actor declaration

This example show how to apply an actor-associated modifier within an actor (type) declaration. This applies the modifier to each instance of that actor.
In this example, we assume a modifier `speed_warning_modifier` that issues an event when a vehicle’s speed exceeds the speed limit by a given tolerance.

Code 58. Applying an actor-associated modifier to an actor within an actor declaration

```
actor my_vehicle inherits vehicle (vehicle_category == car):
    ...
    speed_warning_modifier(tolerance: 10kph) # issue warning events when the speed is 10 km/h over the current speed limit
```

##### Applying a scenario-associated modifier

Code 59. Applying a scenario-associated modifier

```
scenario top.drive_in_lane:
    v: vehicle
    the_other_vehicle: vehicle   # the vehicle that v should follow
    do serial:
       v.drive(...) with:
           follow_vehicle(target: the_other_vehicle)   # use a modifier to require the vehicle to follow the_other_vehicle in this drive only
```

## 7.3.13 Scenario composition

A scenario may invoke other behaviors (scenarios or actions) and use scenario composition operators to define their temporal arrangement.
For example, invoked scenarios may be composed in series or parallel (or otherwise overlapping).
There is also a composition operator to define alternative behavior.
Composition operators can be used within a `do` block of a scenario declaration.

The behavior of composition operators is formally defined in [Section 7.6.2.1, "Composition operators"](Semantics.html#sec-lc-semantics-composition-operators).
This section only lists the operators and provides a structural description.

All composition operators define an optional parameter `duration: range of stdtypes::time` that constrains the execution time of the composed scenarios. The inclusive bounds specify the admissible elapsed time (start-to-end) of the composed scenarios. If omitted, the composed scenarios' duration is unconstrained by this parameter. Passing a single time (for example `duration: 5s`) is allowed and is implicitly promoted to `[5s..5s]`.

|  |  |
| --- | --- |
|  | The parameter names for composition operators are not namespaced identifiers. They are universally available and must be specified as unprefixed unqualified identifiers. The argument list to a composition operator is an unqualified argument list. |

### 7.3.13.1 Serial composition

The members execute one at a time, in the defined order.
A member is invoked immediately after its predecessor ends.

Code 60. Syntax for serial composition

```
    serial:
        member_1
        member_2
        …
```

### 7.3.13.2 Parallel composition

All of the members execute in parallel or overlap in certain ways.

Code 61. Syntax for parallel composition

```
    parallel:
        member_1
        member_2
        …
```

The behavior of parallel is controlled by the following optional parameters:

Table 4. Relational operators over non-numeric expressions


| Parameter | Type | Description |
| --- | --- | --- |
| overlap | Enum | The following values are defined:  * **equal**    All members start and end together.   Constrains start\_to\_start (STS) to 0 and end\_to\_end (ETE) to 0. * **start**    All members start together.   This is the default.   STS == 0. * **end**    All members end together.   ETE == 0. * **initial**    First member starts with or after all other members.   STS ⇐ 0. * **final**    First member ends with or before all other members.   ETE >=0. * **inside**    First member starts before or with all other members and ends after or with all other members.   STS >=0 and ETE ⇐ 0. * **full**    First member starts with or after all other members and ends before or with all other members.   STS ⇐ 0 and ETE >= 0. * **any**    No constraint on overlap. |
| start\_to\_start | Time | Determines the offset between the first member’s start time and all other members' start times. The time value can be positive, zero, or negative. |
| end\_to\_end | Time | Determines the offset between the first member’s end time and all other members' end times. The time value can be positive, zero, or negative. |

* In addition to any other constraints, there must be at least one point in time in which all members of parallel overlap.
* The first member of parallel is called the *primary*, all other members are *secondary*.
* Depending on the parameters, parallel composition is usually *not commutative*:  
  `Parallel(a, b, c)` is *not* the same as `parallel(b, a, c)`.
* Parallel can be decomposed as follows:  
  `parallel(a, b, c, d)` is the same as `parallel(parallel(parallel(a, b), c), d)`.

### 7.3.13.3 One-of composition

Only one of the members is invoked.
This composition operator can be used to specify alternative behavior.

Code 62. Syntax for one-of composition

```
    one_of:
        member_1
        member_2
        …
```

## 7.3.14 Global parameters

Global parameter declarations are declarations of typed parameters that are accessible globally.

For example, a global parameter can be accessed within any scenario or actor declaration in the same file, imported files, or importing files.
This is in contrast to parameter declarations contained within structured type declarations that are only accessible within these structured type declarations (see [Section 7.3.6, “Fields”](#sec-lc-fields)).

Global parameters are therefore global in both scope and extent.
Any local fields defined within structured type declarations with the same name as a global parameter will shadow the global declaration within that structured type declaration:
In other words, within that structured type declaration any references to the field name will reference the local field, not the global parameter.

The duration of the binding of the parameter to its value (the extent of the global) is from the beginning of processing of the overall scenario file (including any imports) until the end of processing of the overall scenario file.

The syntax for global parameter declarations is given in [Section 7.2.2.3, "Global parameter declarations"](language_syntax.html#sec-lc-syntax-language-global-parameter-declarations).
An example of defining global parameters for map and environment is given below:

Code 63. Defining and using global parameters 'map' and 'environment'

```
global map: map
global environment: environment

scenario foo:
    my_field: temperature = environment.weather.air.temperature
    do parallel:
        bar(newfield: 0.5)

scenario bar:
    newfield: float
    environment: enviroment
    keep(newfield <= environment.weather.air.relative_humidity)
```

In this example, the `environment` reference in scenario `foo` references the global parameter, whereas the `environment` reference in scenario `bar` references the local field of the same name.

|  |  |
| --- | --- |
|  | Since global parameter declarations are truly global in scope and extent, they should be used sparingly to avoid clashes when combining scenarios from multiple sources, for example. |

## 7.3.15 Type resolution and order

For type resolution there are no restrictions on the ordering of type use and type declaration in terms of textual ordering.
Note that this includes the ordering of field references and field use for structured types.
Equally, there are no restrictions on the ordering of unit use and unit declaration.

The ordering of types and type extensions for the resolution of method overriding is based on the inheritance relationships of the types that the methods are defined in.
For the ordering of extensions that have the same inheritance relationship, the textual order of the extensions is used.