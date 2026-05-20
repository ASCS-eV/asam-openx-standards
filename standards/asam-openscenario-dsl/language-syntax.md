# ASAM Openscenario Dsl v2.2.0 — 7.2 Language structure and syntax

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/language-reference/language_syntax.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.2 Language structure and syntax

It can be assumed that processing an ASAM OpenSCENARIO file is typically performed in two steps:

* *Lexical analysis* breaks the character stream into individual tokens, yielding a token stream.
* *Parsing* then processes the token stream into the abstract syntax tree.

The lexical analysis phase is set out in [Section 7.2.1, “Lexical structure”](#sec-lc-syntax-lexical).
The grammar governing the parsing process is set out in [Section 7.2.2, “Grammar of ASAM OpenSCENARIO”](#sec-lc-syntax-grammar).
A modified BNF grammar notation is used as mentioned in Python 3.10 documentation section 1.2.

## 7.2.1 Lexical structure

This section provides the lexical analysis definitions for ASAM OpenSCENARIO.

### 7.2.1.1 Character set

ASAM OpenSCENARIO files use the Unicode character set and must use the UTF-8 encoding.

Whitespace consists of space (U+0020) and tab (U+0009) characters.

### 7.2.1.2 Line structure

Like Python, ASAM OpenSCENARIO is based on a logical line structure.

An ASAM OpenSCENARIO file consists of logical lines:

* Each statement is fully contained within a logical line.
* Each logical line is constructed from one or more physical lines, using a set of line-joining rules.

A physical line is a sequence of characters terminated by an end-of-line sequence.
The end-of-line sequence can be either the CR (U+000D) character, the LF (U+000A) character, or the sequence CR (U+000D) LF (U+000A) characters.
The end of input/file also serves as an implicit end-of-line sequence.

Multiple physical lines can be joined into one logical line in the following two ways:

* A physical line can be *explicitly* joined to the next physical line by placing the `\` backslash (U+005C) character directly before the end-of-line sequence of the previous line.
  The backslash must be placed outside of a string literal or comment.
* A physical line can be *implicitly* joined to the next physical line by splitting the line inside an expression that employs parentheses or square brackets.

Logical lines that contain only whitespace, formfeed (U+000C) characters, and possibly a comment, are ignored.

Each logical line ends with a NEWLINE token indicating the end of the logical line.

### 7.2.1.3 Comments

Comments start with a number sign character (`#`, U+0023) that is outside of a string literal. They end at the end of the physical line. Comments are ignored by the syntax given in [Section 7.2.2, “Grammar of ASAM OpenSCENARIO”](#sec-lc-syntax-grammar).

### 7.2.1.4 Indentation

Whitespace at the beginning of a logical line is considered to be indentation.
For the purposes of indentation calculation, tab characters are replaced with spaces with the assumption that tab stops are every 8 characters.
Formfeed characters at the start of a line are ignored for indentation calculations.

Based on changes to the amount of whitespace on a line after the replacements mentioned above, INDENT and DEDENT tokens are generated using the algorithm specified in Python 3.10 section 2.1.8.

### 7.2.1.5 Tokenization

Tokens are separated by whitespace, except where indicated otherwise.

When splitting the input into tokens, tokens comprise the longest possible match that forms a legal token, when read from left to right.

Besides the already mentioned NEWLINE, INDENT, and DEDENT tokens, the following tokens are recognized in lexical analysis.

#### 7.2.1.5.1 Keywords and identifiers

Identifiers are unlimited in length.
Case is significant.

Valid identifiers match the following productions:

```
identifier ::= ( id-start-char id-char* ) | ( '|' non-vertical-line-char+ '|' )
qualified-identifier ::= identifier | prefixed-identifier
prefixed-identifier ::= ( [ namespace-name ] '::' identifier )
```

where `id-start-char` matches all characters of the following Unicode character categories:

* Ll — Lowercase Letter
* Lm — Modifier Letter
* Lo — Other Letter
* Lt — Titlecase Letter
* Lu — Uppercase Letter
* Nl — Letter Number

It also matches the underscore character `_` (U+005F).

`id-char` matches all characters that `id-start-char` matches, and additionally all characters of the following Unicode character categories:

* Mc — Spacing Combining Mark
* Mn — Nonspacing Mark
* Nd — Decimal Number
* Pc — Connector Punctuations

`non-vertical-line-char` matches all Unicode characters, except the vertical line `|` (U+007C) character.

The second clause in the identifier production defines an alternative way of writing identifiers:

It allows the use of characters that normally are not allowed in identifiers, by delimiting the identifier using `|`.
Besides allowing the use of any other character in identifiers, such identifiers do not need to be separated by whitespace.

Qualified identifiers are either normal unadorned identifiers or identifiers prefixed with a namespace name and `::`.
Through prefixing, an identifier in a namespace can be accessed, even if it is not otherwise accessible in the current namespace.

Certain identifiers are reserved as keywords for use in ASAM OpenSCENARIO built-in language constructs.
Note however that these keywords are only recognized as keywords in the places identified in the grammar.
This means that these identifiers should be treated as normal identifier tokens in all other places.

Table 4. List of reserved keywords


|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| action | actor | and | as | bool |
| call | cd | cover | def | default |
| do | elapsed | emit | enum | event |
| every | export | expression | extend | external |
| factor | fall | false | float | global |
| hard | if | import | in | inf |
| inherits | int | is | it | K |
| keep | kg | list | m | modifier |
| mol | namespace | nan | not | null |
| of | offset | on | one\_of | only |
| or | parallel | rad | range | record |
| remove\_default | rise | s | sample | scenario |
| serial | SI | string | struct | true |
| type | uint | undefined | unit | until |
| use | var | wait | with |  |

#### 7.2.1.5.2 Literals

The following literals are recognized by lexical analysis:

##### String literals

String literals are constant string expressions matching the following production:

```
string-literal ::= shortstring | longstring
shortstring ::= ('"' shortstring-elem* '"') | ("'" shortstring-elem* "'")
longstring ::= ('"""' longstring-elem* '"""') | ("'''" longstring-elem* "'''")
shortstring-elem ::= shortstring-char | string-escape-seq
longstring-elem ::= longstring-char | string-escape-seq
string-escape-seq ::= '\' any-char
```

where `shortstring-char` matches any Unicode character except `\`, the quote character used to introduce the string or any end-of-line character.

`longstring-char` matches any Unicode character except `\`, and `any-char` matches any Unicode character.

##### Boolean literals

The tokens `true` and `false` represent the logically true and false Boolean values.
They are of type `bool`.

```
bool-literal ::= 'true' | 'false'
```

##### Integer literals

Positive integer literals produce an `uint` value.
This will be cast implicitly to `int` type in the appropriate contexts.
Negative integer literals produce an `int` value.
Positive integer literals can also be provided in hexadecimal base through the prefix '0x'.
It is an error to include a positive integer literal in ASAM OpenSCENARIO source code that cannot be represented using the `uint` type.
It is an error to include a negative integer literal in ASAM OpenSCENARIO source code that cannot be represented using the `int` type.

```
integer-literal ::= uint-literal | hex-uint-literal | int-literal
uint-literal ::= digit+
hex-uint-literal ::= '0x' hex-digit+
int-literal ::= '-' digit+
digit ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
hex-digit ::= digit | 'A' | 'a' | 'B' | 'b' | 'C' | 'c' | 'D' | 'd' | 'E' | 'e' | 'F' | 'f'
```

##### Floating-point literals

Floating-point literals produce a `float` value.
It is an error to include a float literal in ASAM OpenSCENARIO source code that cannot be represented using the `float` type.

```
float-literal ::= ['+' | '-'] ( digit* '.' digit+ [('e' | 'E') ['+'|'-'] digit+] | digit+ ('e' | 'E') ['+'|'-'] digit+ | 'inf' | 'nan' )
```

##### Physical type literals

Physical type literals are literals that produce a valid physical type value.

```
physical-literal ::= (float-literal | integer-literal) unit-name
unit-name ::= qualified-identifier
```

A physical type literal is created when an identifier naming a valid unit is included directly after a valid float or integer literal without any intervening whitespace separating the two parts.

#### 7.2.1.5.3 Operators and delimiters

The following tokens are recognized operators and delimiters of the language:

Table 5. List of operator and delimiter tokens


|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ' | " | . | , | : | = | @ | -> | | |
| ( | ) | [ | ] | ? | => | and | or | not |
| == | != | < | <= | > | >= | in | + | - |
| \* | / | % |  |  |  |  |  |  |

## 7.2.2 Grammar of ASAM OpenSCENARIO

The following grammar is structured for explanatory and normative purposes, not necessarily for parser implementation purposes.
For example, implementers might want to eliminate left recursions and need to take into account the interactions between lexical analysis and parser for their particular implementation approach.

### 7.2.2.1 Top-level structure

An ASAM OpenSCENARIO file consists of prelude statements and main statements that comprise namespace statements and top-level declarations.

```
osc-file ::= prelude-statement* main-statement*
```

#### 7.2.2.1.1 Prelude statements

Prelude statements must occur before all other statements in the file.

```
prelude-statement ::= import-statement
```

##### Import statement

The import statement makes all definitions found in the referenced file effective as if they had been included in the referencing file.

```
import-statement ::= 'import' import-reference NEWLINE
import-reference ::= string-literal | structured-identifier

structured-identifier ::= identifier | structured-identifier '.' identifier
```

#### 7.2.2.1.2 Main statements

Main statements currently consist of namespace statements and top-level declarations:

```
main-statement ::= namespace-statement | export-statement | osc-declaration
```

##### Namespace statement

The namespace statement places all following definitions into a specified namespace.

```
namespace-statement ::= 'namespace' namespace-name ['use' namespace-list ] NEWLINE

namespace-list ::= namespace-name (',' namespace-name)*
namespace-name ::= identifier | global-namespace-name
global-namespace-name ::= 'null'
```

##### Export statement

The export statement places all following identifiers into the exported identifier list of the current namespace.
The exported identifier list of a namespace defines all identifiers of the namespace that are made accessible without prefix in any other namespace that uses the given namespace via a `use` clause in a namespace statement.
Note that both accessible and non-accessible identifiers can be exported from a namespace.

```
export-statement ::= 'export' export-specification (',' export-specification)* NEWLINE
export-specification ::= qualified-identifier | export-wildcard-specification
export-wildcard-specification ::=[ [ namespace-name ] '::' ] '*'
```

##### Top-level declarations

All top-level declarations are currently considered type declarations that are described in detail in the next section.

```
osc-declaration ::=   physical-type-declaration
                    | unit-declaration
                    | enum-declaration
                    | struct-declaration
                    | actor-declaration
                    | action-declaration
                    | scenario-declaration
                    | modifier-declaration
                    | type-extension
                    | global-parameter-declaration
```

### 7.2.2.2 Type declarations

Type declarators are the set of all built-in and user-defined types that can be used to declare the type of an entity.

Note that modifier declarations are not considered to define a type that can be used to declare the type of an entity. Modifier names are therefore not considered type declarators.

```
type-declarator ::= non-aggregate-type-declarator | aggregate-type-declarator

non-aggregate-type-declarator ::= non-structural-type-declarator | structural-type-declarator
non-structural-type-declarator ::= primitive-type | physical-type-name | enum-name
structural-type-declarator ::= struct-name | actor-name | qualified-behavior-name

aggregate-type-declarator ::= list-type-declarator | range-type-declarator

primitive-type ::= primitive-numeric-type | 'bool' | 'string'
primitive-numeric-type ::= 'int' | 'uint' | 'float'
numeric-type-declarator ::= primitive-numeric-type | physical-type-name
```

#### 7.2.2.2.1 Physical types and units

Physical types represent physical quantities and are associated with units.

```
physical-type-declaration ::= 'type' physical-type-name 'is' base-unit-specifier NEWLINE
physical-type-name ::= qualified-identifier
```

```
unit-declaration ::= 'unit' unit-name 'of' physical-type-name 'is' unit-specifier NEWLINE

base-unit-specifier ::= SI-base-unit-specifier
unit-specifier ::= SI-unit-specifier

SI-base-unit-specifier ::= 'SI' '(' SI-base-exponent-list ')'
SI-base-exponent-list ::= SI-base-exponent (',' SI-base-exponent)*
SI-base-exponent ::= SI-base-unit-name ':' integer-literal

SI-unit-specifier ::= 'SI' '(' SI-base-exponent-list [',' SI-factor] [',' SI-offset] ')'
SI-factor ::= 'factor' ':' ( float-literal | integer-literal )
SI-offset ::= 'offset' ':' ( float-literal | integer-literal )
SI-base-unit-name ::= 'kg' | 'm' | 's' | 'A' | 'K' | 'mol' | 'cd' | 'rad'
```

#### 7.2.2.2.2 Enumerations

Enumeration types are the basic user-defined data types.
They enumerate a finite but extensible set of possible values.

```
enum-declaration ::= 'enum' enum-name ':' '[' enum-member-decl (',' enum-member-decl)* ']' NEWLINE
enum-member-decl ::= enum-member-name [ '=' enum-member-value ]
enum-name ::= qualified-identifier
enum-member-name ::= qualified-identifier
enum-member-value ::= uint-literal | hex-uint-literal | enum-value-reference

enum-value-reference ::= [enum-name '!'] enum-member-name
```

#### 7.2.2.2.3 Aggregate types

Aggregate types are types that group multiple values into one.
This includes the list and range aggregate types:

```
list-type-declarator ::= 'list' 'of' ( non-aggregate-type-declarator | range-type-declarator )
```

```
range-type-declarator ::= 'range' 'of' numeric-type-declarator
```

#### 7.2.2.2.4 Structured types

Structured types provide a way to build complex types from simpler ones.
A structured type acts as a container for its members.

The ASAM OpenSCENARIO language offers four kinds of structured types:

* [Structs](#sec-lc-syntax-structs)
* [Actors](#sec-lc-syntax-actors)
* [Scenarios](#sec-lc-syntax-scenarios)
* [Actions](#sec-lc-syntax-actions)

##### Structs

```
struct-declaration ::= 'struct' struct-name ['inherits' struct-name ['(' field-name '=='  (enum-value-reference | bool-literal) ')']] ( (':' NEWLINE INDENT
      struct-member-decl+ DEDENT) | NEWLINE )

struct-member-decl ::= event-declaration | field-declaration | constraint-declaration | method-declaration | coverage-declaration
struct-name ::= qualified-identifier
field-name ::= qualified-identifier
```

##### Actors

```
actor-declaration ::= 'actor' actor-name ['inherits' actor-name ['(' field-name '==' (enum-value-reference | bool-literal) ')']] ( (':' NEWLINE INDENT
      actor-member-decl+ DEDENT) | NEWLINE )

actor-member-decl ::= event-declaration | field-declaration | constraint-declaration | method-declaration | coverage-declaration
actor-name ::= qualified-identifier
```

##### Scenarios

```
scenario-declaration ::= 'scenario' qualified-behavior-name ['inherits' qualified-behavior-name ['(' field-name '==' (enum-value-reference | bool-literal) ')']] ( (':' NEWLINE INDENT
      (scenario-member-decl | behavior-specification)+
      DEDENT) | NEWLINE )

scenario-member-decl ::= event-declaration | field-declaration | constraint-declaration | method-declaration | coverage-declaration | modifier-application

qualified-behavior-name ::= [actor-name '.'] behavior-name
behavior-name ::= qualified-identifier
```

##### Actions

```
action-declaration ::= 'action' qualified-behavior-name ['inherits' qualified-behavior-name ['(' field-name '==' (enum-value-reference | bool-literal) ')']] ( (':' NEWLINE INDENT
      (scenario-member-decl | behavior-specification)+
      DEDENT) | NEWLINE )
```

#### 7.2.2.2.5 Modifiers

Modifiers provide a means of modifying object behavior.
Compound modifiers can have the same members that scenario and action structured types allow, with the exception of `do` directives.
They allow the modification of behaviors, like scenario, action, or composition operator invocations.

```
modifier-declaration ::= 'modifier' [actor-name '.'] modifier-name ['of' qualified-behavior-name] ( (':' NEWLINE INDENT
      (scenario-member-decl | on-directive)+
      DEDENT) | NEWLINE )

modifier-name ::= qualified-identifier
```

#### 7.2.2.2.6 Type extension

```
type-extension ::= enum-type-extension | structured-type-extension | primitive-type-extension

enum-type-extension ::= 'extend' enum-name ':' '[' enum-member-decl (',' enum-member-decl)* ']' NEWLINE

structured-type-extension ::= 'extend' extendable-type-name ':' NEWLINE INDENT
      extension-member-decl+ DEDENT

extendable-type-name ::= struct-name | actor-name | qualified-behavior-name
extension-member-decl ::= struct-member-decl | actor-member-decl | scenario-member-decl | behavior-specification

primitive-type-extension ::= 'extend' primitive-type ':' NEWLINE INDENT
      method-declaration+ DEDENT
```

### 7.2.2.3 Global parameter declarations

Global parameter declarations are declarations of typed parameters that are accessible globally.

```
global-parameter-declaration ::= 'global' parameter-declaration
```

### 7.2.2.4 Structured type members

The following entities are usable as members in structured type declarations, depending on the structured type.

#### 7.2.2.4.1 Events

Events are named entities, signifying a zero-time occurrence in time.
They can optionally have parameters describing that occurrence.

Event specifications are specifications of conditions for the occurrence of an event. They are used in different places, such as the `on` or `wait` directives, or as a formula for an event declaration.

```
event-declaration ::= 'event' event-name ['(' argument-list-specification ')'] ['is' event-specification] NEWLINE
event-specification ::= event-reference [ [event-field-decl] 'if' event-condition ]
                       | event-condition

event-reference ::= '@' event-path
event-field-decl ::= 'as' event-field-name
event-field-name ::= qualified-identifier
event-name ::= qualified-identifier
event-path ::= [expression '.'] event-name

event-condition ::= bool-expression | rise-expression | fall-expression | elapsed-expression | every-expression
rise-expression ::= 'rise' '(' bool-expression ')'
fall-expression ::= 'fall' '(' bool-expression ')'
elapsed-expression ::= 'elapsed' '(' duration-expression ')'
every-expression ::= 'every' '(' duration-expression [',' 'offset' ':' duration-expression] ')'

bool-expression ::= expression
duration-expression ::= expression
```

#### 7.2.2.4.2 Fields

Fields represent named data members inside compound types and modifiers.

```
field-declaration ::=  parameter-declaration | variable-declaration
parameter-declaration ::= field-name (',' field-name)* ':' type-declarator ['=' default-value] ( parameter-with-declaration | NEWLINE )
variable-declaration ::= 'var' field-name (',' field-name)* ':' type-declarator ['=' (default-value | sample-expression) ] NEWLINE

sample-expression ::= 'sample' '(' expression ',' event-specification [',' default-value] ')'
default-value ::= expression
```

Parameter declarations can contain `with` blocks that provide relevant constraint declarations.

```
parameter-with-declaration ::= 'with' ':' NEWLINE INDENT
      parameter-with-member+ DEDENT
parameter-with-member ::= constraint-declaration
```

#### 7.2.2.4.3 Constraints

Constraints restrict the range of possible values that fields may have during scenario execution.

```
constraint-declaration ::= keep-constraint-declaration | remove-default-declaration
```

```
keep-constraint-declaration ::= 'keep' '(' [constraint-qualifier] constraint-expression ')' NEWLINE
constraint-qualifier ::= 'default' | 'hard'

constraint-expression ::= expression
```

```
remove-default-declaration ::= 'remove_default' '(' parameter-reference ')' NEWLINE

parameter-reference ::= field-name | field-access
```

#### 7.2.2.4.4 Methods

Methods are member functions defined within a structured type or modifier.

```
method-declaration ::= 'def' method-name '(' [argument-list-specification] ')' ['->' return-type] method-implementation NEWLINE

return-type ::= type-declarator

method-implementation ::= 'is' [method-qualifier] ('expression' expression | 'undefined' | 'external' structured-identifier '(' [argument-list] ')')

method-qualifier ::= 'only'
method-name ::= qualified-identifier
```

#### 7.2.2.4.5 Coverage

Coverage and reporting use similar syntax with the goal of storing data expected to be observed throughout validation or for later analysis.

```
coverage-declaration ::= ('cover' | 'record') '(' argument-list ')' NEWLINE
```

#### 7.2.2.4.6 Modifier application

Modifier application syntax.

```
modifier-application ::= [actor-expression '.'] modifier-name '(' [argument-list] ')' NEWLINE
```

#### 7.2.2.4.7 Behavior specification

Behavior specifications, in the form of `on` and `do` directives provide the behavior description of scenarios and actions.

```
behavior-specification ::= on-directive | do-directive
```

##### On directive

```
on-directive ::= 'on' event-specification ':' NEWLINE INDENT
     on-member+ DEDENT

on-member ::= call-directive | emit-directive
```

```
do-directive ::= 'do' do-member

do-member ::= [label-name ':'] ( composition | behavior-invocation | wait-directive | emit-directive | call-directive )

label-name ::= qualified-identifier
```

##### Composition

```
composition ::= composition-operator ['(' [unqualified-argument-list] ')']':' NEWLINE INDENT
     do-member+ DEDENT [behavior-with-declaration]

composition-operator ::= 'serial' | 'one_of' | 'parallel'
```

##### Behavior invocation

```
behavior-invocation ::= [actor-expression '.'] behavior-name '(' [argument-list] ')' ( behavior-with-declaration | NEWLINE )

behavior-with-declaration ::= 'with' ':' NEWLINE INDENT
      behavior-with-member+ DEDENT
behavior-with-member ::= constraint-declaration
                       | modifier-application
                       | until-directive

actor-expression ::= expression
```

##### Wait directive

```
wait-directive ::= 'wait' event-specification NEWLINE
```

##### Emit directive

```
emit-directive ::= 'emit' event-name ['(' argument-list ')'] NEWLINE
```

##### Call directive

```
call-directive ::= 'call' method-invocation NEWLINE

method-invocation ::= postfix-exp '(' [argument-list] ')'
```

##### Until directive

```
until-directive ::= 'until' event-specification NEWLINE
```

### 7.2.2.5 Common productions

#### 7.2.2.5.1 Argument list specification

```
argument-list-specification ::= argument-specification (',' argument-specification)*

argument-specification ::= argument-name ':' type-declarator ['=' default-value]

argument-name ::= qualified-identifier
```

#### 7.2.2.5.2 Argument list

```
argument-list ::= positional-argument (',' positional-argument)* (',' named-argument)*
                | named-argument (',' named-argument)*

positional-argument ::= expression
named-argument ::= argument-name ':' expression
```

#### 7.2.2.5.3 Unqualified argument list

```
unqualified-argument-list ::= positional-argument (',' positional-argument)* (',' unqualified-named-argument)*
                            | unqualified-named-argument (',' unqualified-named-argument)*

unqualified-argument-name ::= identifier
unqualified-named-argument ::= unqualified-argument-name ':' expression
```

### 7.2.2.6 Expressions

```
expression ::= implication | ternary-op-exp
```

#### 7.2.2.6.1 Ternary operator

```
ternary-op-exp ::= implication '?' expression ':' expression
```

#### 7.2.2.6.2 Logical operators

```
implication ::= disjunction ('=>' disjunction)*
disjunction ::= conjunction ('or' conjunction)*
conjunction ::= inversion ('and' inversion)*
inversion ::= 'not' inversion | relation
```

#### 7.2.2.6.3 Relational operators

```
relation ::= sum | relation relational-op sum
relational-op ::= '==' | '!=' | '<' | '<=' | '>' | '>=' | 'in'
```

#### 7.2.2.6.4 Arithmetics operators

```
sum ::= term | sum additive-op term
additive-op ::= '+' | '-'

term ::= factor | term multiplicative-op factor
multiplicative-op ::= '*' | '/' | '%'

factor ::= postfix-exp | '-' factor
```

#### 7.2.2.6.5 Postfix operators

```
postfix-exp ::= primary-exp
              | cast-exp
              | type-test-exp
              | element-access
              | function-application
              | field-access

cast-exp ::= postfix-exp '.' 'as' '(' type-declarator ')'
type-test-exp ::= postfix-exp '.' 'is' '(' type-declarator ')'
element-access ::= postfix-exp '[' expression ']'
function-application ::= postfix-exp '(' [argument-list] ')'
field-access ::= postfix-exp '.' field-name
```

#### 7.2.2.6.6 Primary expressions

```
primary-exp ::= value-exp | 'it' | qualified-identifier | '(' expression ')'

value-exp ::= integer-literal
            | float-literal
            | physical-literal
            | bool-literal
            | string-literal
            | enum-value-reference
            | list-constructor
            | range-constructor
```

#### 7.2.2.6.7 List and range constructors

```
list-constructor ::= '[' expression (',' expression)* ']'
```

```
range-constructor ::= 'range' '(' expression ',' expression ')' | '[' expression '..' expression ']'
```