# ASAM OpenSCENARIO® DSL v2.2.0 — 7.4 Expressions

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/language-reference/expressions_main.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.4 Expressions

Expressions are used in multiple places within type members, for example within the body of:

* Constraints
* Expression method implementations
* Event definitions

Each expression produces a value.
Because the language is strongly typed, each expression has a type that is known statically (at compile time).

Expressions are composed of atoms.
Atoms are identifiers or constant literals.
Atoms are combined to compound expressions through operators and method application.

## 7.4.1 Atomic expressions

### 7.4.1.1 Identifiers

Identifiers that occur in expressions are evaluated to the values of the fields that they identify.
The type of the reference is the type of the referenced field.

### 7.4.1.2 Literals

Any literal value of any type is a valid atomic expression if it fulfills the following two conditions:

1. The *type* of the literal value is as specified in  [Section 7.3, "Types"](types.html#top-lc-types).
2. The literal value uses the *syntax* that is specified in  [Section 7.2, "Language structure and syntax"](language_syntax.html#top-lc-syntax-language).

If the literal value is a valid atomic expression, the following is true for the expression:

* The *value* of the expression is the literal value itself.
* The *type* of the expression is the type of the literal as defined in  [Section 7.3, "Types"](types.html#top-lc-types).

### 7.4.1.3. `it` expression

`it` is a reference to the instance of a type in whose scope it occurs.
In a modifier, `it` refers to the invoking scenario and gives access to the members of the scenario (see [Section 7.3.12.2, "Modifier declaration"](types.html#sec-lc-types-modifier-declaration)) or the parameters inside the composition operator of the do-block (see [Section 7.3.12.1.2, "Compound modifiers"](types.html#sec-lc-types-compound-modifiers)).

Code 39. Setting vehicle color using the 'it' expression.

```
struct car inherits vehicle(vehicle_category == car):
    color: color

struct truck inherits vehicle(vehicle_category == truck)

scenario truck_test:
    dut_truck: truck with:
        keep(it.axles.size() > 2)

    car_in_traffic: car with:
        keep(it.color == silver)
```

## 7.4.2 Compound expressions

*Compound expressions* are formed from other expressions, called *sub-expressions*, by applying operators or methods to these sub-expressions to form a composition.

All sub-expressions are evaluated from left to right in the order in which they appear in the compound expression unless specified otherwise.

### 7.4.2.1 Method application

Expressions may contain calls to methods.
Methods are declared as type members with a binding that maps each method to its implementation.
Method applications take the following form:

Code 40. Method application

```
<object>.method_name(<positional-arg>, <named-argument-name>: <named-arg>)
```

Method arguments can be passed in the following ways:

* As *positional arguments*

  + Positional arguments must be passed before all named arguments.
  + Positional arguments are matched against the defined arguments of the method by their position.
* As *named arguments*

  + Named arguments are passed after all positional arguments, if any.
  + Named arguments are matched against the defined arguments of the method by the argument name identifier.
  + The argument name identifier is prefixed with a colon (':') before the argument value expression.
* As a combination of both

All argument sub-expressions in a method application expression are evaluated before the method implementation is invoked.
The resultant values are passed as arguments to the method.

If no value is passed for an argument of the method, the default value of that argument declared in the method declaration will be used.
It is an error if no value is passed for an argument without a declared default value.

Method application in expressions can only invoke methods with a declared return type.
The method application yields the return value of the method as the value of the method application expression.

The type of the return value is the declared return type of the invoked method.

Method application can produce side effects.

Note that unlike invocation of behaviors, modifiers, and composition operators, method application does not support range expressions to be used interchangeably with providing single values.

### 7.4.2.2 Logical operators

ASAM OpenSCENARIO provides the following logical operators:

Table 5. Boolean operators


| Operator | Operator name | Description | Example |
| --- | --- | --- | --- |
| `not` | Negation | True if its operand is false, otherwise false | `not b` |
| `and` | Conjunction | True if both operands are true, otherwise false | `x < 5 and x > 0` |
| `or` | Disjunction | True if either operand is true, otherwise false | `x > 5 or x < 0` |
| `=>` | Implication | True if either the first operand is false, or both operands are true, otherwise false | `b => c` |

All operators are short-circuiting, meaning that sub-expressions are evaluated in left-to-right order until the result of the operator can be determined.
Any remaining sub-expressions that, based on the rules of Boolean logic, cannot affect the result of the operator are not evaluated.

The *precedence* of the operators is the order of the operators in the [table of Boolean operators](#tab-lc-operators-logical-boolean) from highest to lowest.

### 7.4.2.3 Arithmetic operators

ASAM OpenSCENARIO provides the following arithmetic operators:

Table 6. Arithmetic operators


| Operator | Operator name | Description | Example |
| --- | --- | --- | --- |
| `-` | Unary minus | Yields the negative of its single operand | `- x` |
| `*` | Multiplication | Multiplies the two operands | `x * y` |
| `/` | Division | Divides its left-hand operand by its right-hand operand | `x / y` |
| `%` | Modulus | Divides its left-hand operand by its right-hand operand and returns the remainder | `x % y` |
| `+` | Addition | Adds the two operands | `x + y` |
| `-` | Subtraction | Subtracts its right-hand operand from its left-hand operand | `x - y` |

All binary arithmetic operators have the following requirement:  
After applying the [rules of implicit numeric type conversion](#sec-lc-operators-arithmetic-numeric-conversions), the type of the two operands must be identical.

#### 7.4.2.3.1 Numeric type conversion rules

* Physical types are not converted.
* If at least one of the operands is of type `float`, then the other is converted implicitly to type `float`.
* If both operands are of type `uint` or both operands are of type `int`, then no conversion is performed.
* If one operand is `int` and the other `uint` then the other is converted to type `int`.

The type of the result of the operator is the common type of its arguments.

For the unary minus operator, the result type of the operator is the type of its operand, or `int` if the operand is of type `uint`.

Calculations involving the type `float` follow the rules set forth in *ANSI/IEEE Std 754-2019*.

Calculations involving the type `int` follow *two’s complement signed arithmetic* rules.

Calculations involving the type `uint` follow *unsigned arithmetic* rules.

#### 7.4.2.3.2 Precedence

The precedence of the arithmetic operators is as follows:

* *Unary minus* has the highest precedence of arithmetic operators.
* *Multiplication*, *division*, and *modulus* have the next highest precedence.
* *Addition* and *subtraction* have the lowest precedence of arithmetic operators.

  Operators with the same precedence associate *left-to-right*.

### 7.4.2.4 Relational operators

#### 7.4.2.4.1 Relational operators over numeric expressions

The relational operators apply to numeric sub-expressions, including the following types:

* *Integers* (`int` and `uint`)
* *Real numbers* (`float`)
* *Physical types*

Table 7. Relational operators over numeric expressions


| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `==` | Equality | Yields true if the two operands are numerically equal. | `x == y` |
| `!=` | Inequality | Yields true if the two operands are not numerically equal. | `x != y` |
| `<` | Less than | Yields true if the left-hand operand is strictly less than the right-hand operand. | `x < y` |
| `<=` | Less or equal | Yields true if the left-hand operand is strictly less than or equal to the right-hand operand. | `x <= y` |
| `>` | Greater than | Yields true if the left-hand operand is strictly greater than the right-hand operand. | `x > y` |
| `>=` | Greater or equal | Yields true if the left-hand operand is strictly greater than or equal to the right-hand operand. | `x >= y` |
| `in` | Membership | Yields true if the left-hand operand lies in the range given by the right-hand operand or is a member of the list given by the right-hand operand. | `x in [2.5..5.5]  y in [2, 5]` |

All binary relational operators over numeric types have the following requirement:  
After applying the [numeric type conversions](#sec-lc-operators-arithmetic-numeric-conversions), the type of the two sub-expressions must be identical.

#### 7.4.2.4.2 Relational operators over non-numeric expressions

The operators in the [following table](#tab-lc-operators-relational-non-numeric) apply to enumerated types, strings, and Boolean expressions.

Table 8. Relational operators over non-numeric expressions


| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `==` | Equality | Yields true if the two operands have the same value. | `x == y` |
| `!=` | Inequality | Yields true if the two operands do not have the same value. | `x != y` |
| `in` | Membership | Yields true if the left-hand operand is a member of the list given by the right-hand operand. | `x in ["Foo", "Bar"]` |

For all binary relational operators over non-numeric types, the type of the two sub-expressions must be identical or one must inherit from the other.

Two values are considered the same if they are identical.
For an enumerated type, *'identical'* means that the enumeration values have the same unsigned integer value.
For strings, *'identical'* means that the strings contain identical content.
For structured types, *'identical'* means that both operands refer to the same object, meaning the operators check for object identity.
This means that two separate instances of a struct type will not be considered equal, even if every member of one operand is considered equal to the corresponding member of the other operand.
A member-wise comparison of structured types is currently not part of ASAM OpenSCENARIO. If this is needed, it can, for example, be done with an expression method:

Code 41. Implementing member-wise comparison

```
struct my_date:
    year:  uint
    month: uint
    day:   uint
    def same_day_as(other: my_date) -> bool is expression year == other.year and month == other.month and day == other.day

scenario my_scenario:
    x: my_date
    y: my_date

    keep(x.same_day_as(y))
```

### 7.4.2.5 Type check operator

Use the type check operator to check if an object is of a given type.
The type check operator yields a Boolean value.

| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `<object>.is(<type>)` | Type check | Returns true if the expression is of the specified type, otherwise false. | `"foo".is(string)` |

Type checking does not perform type conversion.
Conversion can be performed with the type conversion operator (see [Section 7.4.2.6, “Type conversion operator”](#sec-lc-operators-type-conversion)).

In the following example the operator `.is` returns true if the object `my_car` is of type `vehicle`, otherwise false.

Code 42. Object type checking

```
my_car.is(vehicle)
```

### 7.4.2.6 Type conversion operator

All type conversions in ASAM OpenSCENARIO are *explicit*, with the following exceptions:

* Conversion of `int` to `uint`.
* Conversion of `int` or `uint` to `float`.
* Compound types are *implicitly upcast* to their base classes in contexts where this is required.
* Lists follow the same implicit conversion rules as their element type.

Downcasting may be needed in the following situations:

* Accessing one of the latent subtypes that may exist through the conditional inheritance mechanism.
* Iterating through a collection of types.

Downcasting is possible using the conversion operator `as`:

| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `<exp>.as(<type>)` | Type conversion | Returns the expression, converted to the specified type.  An error is raised if the conversion cannot be performed (meaning <exp> is not of the specified type). | `vehicle.as(car)` |

For example:

Code 43. Object downcasting

```
extend vehicle:
    emergency_vehicle: bool

actor emergency_vehicle inherits vehicle(emergency_vehicle: true):
    sirens_active: bool

scenario my_scenario:
    my_car: vehicle
    keep(my_car.emergency_vehicle == true)
    keep(my_car.as(emergency_vehicle).sirens_active == true)
```

### 7.4.2.7 List operators

The following operators apply to lists.

#### 7.4.2.7.1 List relational operators

Table 9. List relational operators


| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `==` | List equality | Yields true if the first list operand is considered equal to the second list operand, otherwise false. | `[40, 41] == [40, 41]` |
| `!=` | List inequality | Yields true if the first list operand is not considered equal to the second list operand, otherwise false. | `[40, 41] != [40, 42]` |
| `in` | Membership | Returns true if the first operand is found in the second operand, otherwise false.  If the first operand is itself a list, then returns true if each member of that list is found in the second operand, otherwise false. | `42 in [40, 41, 42]  [42, 43] in [40, 41, 42]` |

Equality for two lists is established if every member of the first list is equal - under the relevant equality operator `==` of the member type - to the member with the same index in the second list.

#### 7.4.2.7.2 Other list operators

Table 10. Other list operators


| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `<list>.size()` | Size | Returns the size of a list, meaning the number of members, as an unsigned integer. | `[4, 5].size()` |
| `<list>[ <integer-exp> ]` | Index | Returns the indexed list member. | `my_list[2]` |

List members are indexed starting from 0.

#### 7.4.2.7.3 List member evaluation operators

The following operators accept an expression as an argument.
The variable `it` is defined in the expression scope, referring to the current list member.

Table 11. Other list operators


| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `<list>.filter(<bool-exp>)` | Filter | Returns an ordered sub-list containing the members of the list for which the <bool-exp> returns true. | `my_traffic.filter(it.is(vehicle))` |
| `<list>.first_index(<bool-exp>)` | First index | Returns the index of the first member of the list for which the <bool-exp> returns true. If no such item is found, -1 is returned. | `my_traffic.first_index(it.is(vehicle))` |
| `<list>.count(<bool-exp>)` | Count | Returns the number of members of the list for which the <bool-exp> returns true. | `my_traffic.count(it.is(vehicle))` |
| `<list>.has(<bool-exp>)` | Has | Returns true if there are any members of the list for which the <bool-exp> returns true. Otherwise returns false. | `my_traffic.has(it.is(vehicle))` |
| `<list>.map(<exp>)` | Map | Returns the result of applying <exp> to all members in <list>. The returned list has the same size as <list>. Its members are of the type returned by <exp>. | `my_traffic.map(it.speed)` |

#### 7.4.2.7.4 List construction

A list can be constructed by specifying list members as expressions, using the following syntax:

```
list-constructor ::= '[' expression (',' expression)* ']'
```

* If any of the expressions returns a list, the members of that list are added to the result (meaning the returned list is flattened).

When constructing a list, a common type is determined for the list elements based on the implicit conversion rules.
All elements are implicitly converted to that type to form the list.
The following rules are applied to determine the common list type:

* If all elements are of the same type, this is the common list type.
* If all elements are of type int or uint, the common list type is int.
* If all elements are of type float, int or uint, the common list type is float.
* If all elements are of structured types of the same kind (for example all are structs or all are actors), the inheritance hierarchy is searched for the first base type that all elements have in common. If such a type exists, this is the common list type.
* In any other case, an error is raised.

Code 44. Example list construction

```
actor truck inherits vehicle (vehicle_category == truck)
actor van inherits vehicle (vehicle_category == car)

struct foo:
    v1: truck
    v2: van
    all_traffic_participants:  list of traffic_participant = [ v1, v2 ]
```

In this example, `v1` and `v2` are both derived from the common type vehicle, so this constructs a list of vehicles as a default value for `all_traffic_participants`.
This is then implicitly converted to a list of `traffic_participant` according to the implicit type conversion rules (see [Section 7.4.2.6, “Type conversion operator”](#sec-lc-operators-type-conversion)).

### 7.4.2.8 Range operators

#### 7.4.2.8.1 Range construction

A range can be constructed for any numeric type using the range constructor syntax:

```
range-constructor ::= 'range' '(' expression ',' expression ')' | '[' expression '..' expression ']'
```

When constructing a range, both expressions must be of the same type or convertible to a common type according to the rules for implicit numeric type conversion (see [Numeric type conversion rules](#sec-lc-operators-arithmetic-numeric-conversions)):

* If both expressions are of the same type, this is the base type of the range.
* If one expression is of type `float`, and the other is of type `int` or `uint` then the other is converted to type `float`, and the base type of the range is `float`.
* If one expression is of type `int` and the other is of type `uint` then the other is converted to type `int`, and the base type of the range is `int`.
* In any other case, an error is raised.

When constructing a range of a physical type, both expressions must be of that physical type, with possibly different units.

The expression with the lower numeric value will provide the lower bound, with the other expression providing the upper bound of the range.
The bounds are inclusive.
It is not required that the lower and upper bounds of a range are provided in this order, i.e. either the first or the second expression can provide an upper bound and vice versa.

Type conversions involving ranges are described in [language-reference:types.adoc#sec-lc-types-range-conversions](types.html#sec-lc-types-range-conversions).

Code 45. Examples for valid range construction

```
scenario bar:
    speedrange: range of speed = [50kph .. 100mph]
    floatrange: range of float = [1.5 .. 3.5]
    intrange: range of int = [-10 .. 10]
    uintrange: range of uint = [0 .. 20]
    mixedrange: range of float = [10 .. 20.5]
```

#### 7.4.2.8.2 Range type conversion rules

A range type can be converted to another range type if the base type of the source range type can be converted to the base type of the target range type according to the rules for implicit numeric type conversion (see [Numeric type conversion rules](#sec-lc-operators-arithmetic-numeric-conversions)).

A numeric type can be converted to a range type if the numeric type can be converted to the base type of the target range type according to the rules for implicit numeric type conversion (see [Numeric type conversion rules](#sec-lc-operators-arithmetic-numeric-conversions)).
In that case any expression of the numeric type is treated as the range `[v .. v]`, where `v` is the value of the expression.

Code 46. Examples for valid range type conversions

```
scenario baz:
    r1: range of float = [1 .. 5]   # Implicit int to float conversion: [1.0 .. 5.0]
    r2: range of float = 3          # Numeric to range conversion: [3.0 .. 3.0]
    r3: range of int = 10           # Numeric to range conversion: [10 .. 10]
    r4: range of float = r3         # Implicit int to float conversion: [10.0 .. 10.0]
```

#### 7.4.2.8.3 Range relational operators

Table 12. Range relational operators


| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `==` | Range equality | Yields true if the lower and upper bounds of the first range operand are considered equal to the respective bounds of the second range operand, otherwise false. | `[40.0 .. 41.0] == [41.0 .. 40.0]` |
| `!=` | Range inequality | Yields true if either the lower or the upper bounds of the first range operand are not considered equal to the respective bounds of the second range operand, otherwise false. | `[40 .. 41] != [40 .. 42]` |
| `in` | Membership | Returns true if the first operand is included in the inclusive range specified by the second operand, otherwise false.  If the first operand is itself a range, then returns true if each bound of that range is included in the second operand, otherwise false. | `42 in [40.0 .. 42.0]  [42 .. 43] in [40.0 .. 44.0]` |

Equality for two ranges is established if both the lower and upper bounds of the first range are equal - under the relevant equality operator `==` of the base type - to the respective bounds of the second range.
The same rules for equality of numeric types apply as described in [Relational operators over numeric expressions](#sec-lc-operators-relational-numeric), including the rules for implicit numeric type conversion.

#### 7.4.2.8.4 Other range operators

Table 13. Other range operators


| Operator | Operator type | Description | Example |
| --- | --- | --- | --- |
| `<list>.lower()` | Range lower bound | Returns the lower bound of a range. | `[4 .. 5].lower()` |
| `<list>.upper()` | Range upper bound | Returns the upper bound of a range. | `[4 .. 5].upper()` |

### 7.4.2.9 Other operators

ASAM OpenSCENARIO also offers the following operators:

Table 14. Other operators


| Operator | Operator name | Description | Example |
| --- | --- | --- | --- |
| `? :` | Ternary | Returns the value of its second operand if its first operand is true, else returns the value of its third operand. | `(x > y) ? (x - y) : (y - x)` |
| `( )` | Parenthesized expression | Returns the value of the expression inside the parentheses. | `(x - y)` |