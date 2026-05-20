# ASAM Openscenario Dsl v2.2.0 — 7.7 Library mechanisms

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/language-reference/Libraries.html
> **Standard**: ASAM Openscenario Dsl v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 7.7 Library mechanisms

## 7.7.1 Introduction

This chapter describes all language features that are relevant to the structuring of collections of scenarios and supporting infrastructure.

This includes scenario libraries, domain model extensions, and helper libraries.

This chapter is targeted at library mechanisms for the language and does not consider scenario databases.

## 7.7.2 Scenario entry point

The scenario entry point is the initial scenario that is selected for scenario execution.
It is instantiated first and starts the overall execution.

For ASAM OpenSCENARIO it is defined by implementation how the scenario entry point is selected from the available scenarios in a file.
This allows implementations to experiment with the best ways to select this entry point while still allowing full flexibility in a scenario and scenario file reuse.

|  |  |
| --- | --- |
|  | A future version of ASAM OpenSCENARIO is likely to provide more standardized and advanced facilities for entry point selection. |

## 7.7.3 Namespaces

To avoid name conflicts, ASAM OpenSCENARIO allows the placement of definitions into separate namespaces.

## 7.7.4 The namespace statement

This is done with the `namespace` statement:

```
namespace-statement ::= 'namespace' namespace-name ['use' namespace-list ] NEWLINE

namespace-list ::= namespace-name (',' namespace-name)*
namespace-name ::= identifier | global-namespace-name
global-namespace-name ::= 'null'
```

The namespace statement switches the active namespace.
Within its scope, all definitions place the defined identifier into this active namespace, unless the defined identifier is explicitly qualified.

The namespace statement is a main statement and can occur at any place any other main statement can occur in a file.
Its scope extends from the point of the namespace statement until the next namespace statement is encountered or the end of file is reached.

Note that namespace statements do not influence the namespace of definitions in files that are imported to a file, meaning the effect of the namespace declaration does not cross file boundaries:
Each file processing starts in the implicit `null` namespace, which is accessed if no namespace declaration is encountered, or if explicitly switched to using a `namespace null` statement.

The namespace statement takes an identifier as its mandatory argument.
The mandatory argument identifies the namespace.
Note that all identifiers starting with `std` are reserved for use by this or future releases of ASAM OpenSCENARIO.

|  |  |
| --- | --- |
|  | Using a naming convention — such as reverse domain name notation — is suggested to avoid name clashes when exchanging namespaces with other entities. This involves replacing the dots in a component-wise reversed domain name under the author’s control with underscores (\_) to create a unique prefix for namespace names. An example would be `com_example_mynamespace`. |

### 7.7.4.1 Referencing namespaces

Code 46. Basic namespace

```
# Defining 'bar' within the namespace 'demo_foo'

namespace demo_foo

struct bar:
    baz: uint
```

Identifiers defined inside of a namespace can be referenced outside of this namespace by pre-pending the namespace name to the identifier name, forming a prefixed or explicitly qualified identifier:

```
identifier ::= ( id-start-char id-char* ) | ( '|' non-vertical-line-char+ '|' )
qualified-identifier ::= identifier | prefixed-identifier
prefixed-identifier ::= ( [ namespace-name ] '::' identifier )
```

The namespace name, followed by two colons (`::`), followed by the definition identifier name, forms a valid reference.
For the null namespace, either the `null` namespace name or the empty string `` `, both followed by two colons (meaning `null:: `` or `::`) are valid prefixes.

Conversely, identifiers not prefixed with a namespace name and two colons are called unprefixed identifiers, or implicitly qualified identifiers.
Unprefixed (meaning implicitly qualified) identifiers are resolved to explicitly qualified identifiers during namespace resolution, under the identifier resolution rules specified in [Section 7.7.4.2, “Resolution rules for unprefixed identifiers”](#sec-lc-libraries-resolution-rules).

Code 47. Referencing an identifier in a different namespace

```
namespace space_one

global baz: uint

namespace space_two

global x: uint = space_one::baz
```

Definitions in the current namespace do not need any prefix prepended to access them.
Explicitly prefixing them is still allowed.

To ease the access of identifiers in other namespaces, namespaces can be added to the use list of a namespace by including them in the `namespace` declaration with a `use` clause.

Code 48. A namespace statement with 'use' clause

```
namespace foo

export bar, az

struct bar:
    az: uint
    ay: uint

namespace bazzle use foo, drizzle

struct foobar inherits bar:
    myz: uint = az      # or foo::az
    myy: uint = foo::ay # ay would reference bazzle::ay, which does not exist, hence an error is raised
```

By including a namespace in the use list of a namespace, all the identifiers in the export list of the other namespace are made available in the current namespace statement scope under the identifier resolution rules specified in [Section 7.7.4.2, “Resolution rules for unprefixed identifiers”](#sec-lc-libraries-resolution-rules).

Note that the effect of the use clause is restricted to the scope of the current namespace statement.
Any other namespace statement that switches to the same namespace can have a different or no use clause, and correspondingly different or no identifiers will be available in the scope of those statements.

The export list of a namespace is maintained with `export` statements, which place identifiers onto the namespace export list:

```
export-statement ::= 'export' export-specification (',' export-specification)* NEWLINE
export-specification ::= qualified-identifier | export-wildcard-specification
export-wildcard-specification ::=[ [ namespace-name ] '::' ] '*'
```

Code 49. Use of 'export' statements for controlled use lists

```
namespace foo

export bar, az

struct bar:
    az: uint
    ay: uint


namespace moo use foo

export newbar, bar, foo::ay # Can also export identifiers from other non-used namespaces

struct newbar inherits bar


namespace bazzle use moo

struct foobar inherits bar: # Or moo::bar or foo::bar
    myz: uint = foo::az # Not available from moo via use
    myy: uint = ay # or moo::ay or foo::ay
```

It is possible to export identifiers from a namespace that are either local to the namespace, or exist in another namespace, by explicitly qualifying the identifier.
In either case the identifier is added to the export list of the current namespace.
A re-exported identifier is still considered identical to the original identifier.

Using the export wild-card specification, an export statement can also add all identifiers of a namespace to the export list of that or another namespace:

Code 50. Use of 'export' statements with wildcard export

```
namespace foo

export *  # In this example equivalent to export of bar, az, ay

struct bar:
    az: uint
    ay: uint

namespace moo use foo

export *, foo::* # Equivalent to newbar, foo::bar, foo::az foo::ay

struct newbar inherits bar

namespace bazzle use moo

struct foobar inherits bar: # Or moo::bar or foo::bar
    myz: uint = az # Available from moo via re-export
    myy: uint = ay # or moo::ay or foo::ay
```

Note that a wild-card export specification includes all identifiers in the given namespace, wherever they are defined.

### 7.7.4.2 Resolution rules for unprefixed identifiers

The following rules apply to the resolution of unprefixed (meaning implicitly qualified) identifiers to explicitly qualified identifiers:

1. For initial definitions of identifiers, the identifier is always placed into the current namespace, even if another identifier from a used namespace would be accessible.

   For types, events, units, enumeration values, labels, and fields, the place of their definition is always considered a place of initial definition for their identifier.

   For methods, the place of initial definition of their identifier is defined as the first place, in order of inheritance, that the method is defined in, whether an implementation is provided or not.
   All other places where a method is defined — meaning through overriding using `is only` — are not considered places of initial definition.
   Hence, an identifier from a used namespace could be resolved for the method name — but only if accessible and not shadowed by an identifier of the current namespace.
2. When resolving an unprefixed identifier in all places that are not a place of initial definition, any identifiers from the current namespace shadow any identifiers accessible from the used namespaces.
   In this case, this means that the unprefixed identifier is resolved to an existing identifier from the current namespace, regardless of any identifiers accessible from the used namespaces.

   When no identifier local to the current namespace is present, the unprefixed identifier is resolved against the identifiers accessible from the used namespaces.
   An error is raised during identifier resolution if more than one same-named identifier is accessible from the used namespaces.

### 7.7.4.3 Resolution examples

Code 51. Examples of identifier resolution in the presence of namespaces

```
namespace foo

export bar, az, my_method, another_method

struct bar:
    az: uint
    def my_method() -> float is undefined
    def another_method() -> float is undefined

namespace moo use foo

struct newbar inherits bar:
    az: float # Is moo::az, hence no conflict with foo::az
    def my_method() -> float is only expression 42 # Will resolve to foo::my_method, and override it
    def another_method() -> float is expression 42 # Will resolve to moo::another_method and not override foo::another_method

scenario demo:
    mybar: newbar
    keep(mybar.az == mybar.my_method()) # mybar.moo::az == mybar.foo::my_method()
    keep(mybar.foo::az == mybar.another_method()) # mybar.foo::az == mybar.moo::another_method()
```

## 7.7.5 Import mechanism

To structure source code, it is good practice to split the code into manageable parts and put these parts into separate files.
The files can then be recombined using an import mechanism.

The import mechanism built into ASAM OpenSCENARIO allows the content of one file (the *referenced file*) to be reused in another file (the *referencing file*).
This mechanism also works recursively, so that a referenced file can refer to further referenced files.

### 7.7.5.1 The import statement

The `import` statement allows importing a file.

The import statement makes all definitions found in the referenced file effective as if they had been included in the referencing file:

* Any prelude statements found in the referenced file are treated as having occurred at the textual location of the import statement.
* Any other statements are treated as having appeared before all non-prelude statements in the referencing file, taking the order of imports into account, meaning non-prelude statements from earlier import statements precede those from later import statements.

The file to be imported can be specified inside the import statement as a [string literal](#sec-lc-libraries-import-using-string-literals) or using [identifiers](#sec-lc-libraries-import-using-identifiers).

In all cases, a file that is referenced multiple times (either directly or transitively) is only imported once.
The import occurs at the place in the transitive reference chain that is first according to depth-first traversal: All later references to the same file result in no further import occurring.

The implementation shall detect multiple references as described using the mechanisms the implementation considers necessary.
In case no other mechanism is found more suitable, an implementation may consider two files to be the same if they have identical content.

#### 7.7.5.1.1 Import using string literals

If the file is specified using a string literal, then the file specification is considered to be a *Uniform Resource Identifier* (URI).
Relative URIs are resolved relative to the location of the referencing file.

Implementations shall support the `file` URI scheme.
Implementations may support more URI schemes.

It is recommended to use a file extension of `.osc` to identify files of this version of ASAM OpenSCENARIO.
This differentiates such files from the XML-based ASAM OpenSCENARIO XML 1.3.1 files using the `.xosc` file extension.

#### 7.7.5.1.2 Import using identifiers

If the file is specified using one or more identifiers separated by a period (`.`), the file specification is considered to be a *module reference* and is resolved to a file specification by the implementation in an implementation-specific manner.
This mechanism can include user- and system-defined library search paths.

Any structured identifier that starts with the `osc` identifier is reserved for use by this version and future versions of ASAM OpenSCENARIO (see also [Section 7.7.5.2, “Importing the standard library”](#sec-lc-libraries-importing-the-standard-library)).

|  |  |
| --- | --- |
|  | Note that the reserved identifier `osc` is different from the file extension `.osc` that is by default used for files of ASAM OpenSCENARIO, even though both use the same three-letter abbreviation. |

|  |  |
| --- | --- |
|  | The current specification of how module references are resolved is intentionally left non-specific for this release in order to allow implementations to evolve with actual usage practice. Future versions of the standard are likely to encode best practices when actual practice is clearer and the other components of a module system are in place. For maximum portability across implementations the URI-based string specifications can be used. |

Code 52. Examples of file import statements

```
# URI-based import statements
import "foo/bar.osc"
import "file:///c:/Users/someone/src/foo/bar.osc"
import "file:/c:/Users/someone/src/foo/bar.osc"
import "/c:/Users/someone/src/foo/bar.osc"
import "file:///home/someone/src/foo/bar.osc"
import "file:/home/someone/src/foo/bar.osc"
import "/home/someone/src/foo/bar.osc"

# Identifier-based import statements
import osc.standard.all   # Imports the standard library, see next section.
import foo.bar            # Imports a module foo.bar in some implementation defined way
```

### 7.7.5.2 Importing the standard library

The ASAM OpenSCENARIO standard library is described in  [Section 8.16, "Standard library"](../domain-model/standard_library.html).
Any scenario file that is to use standard library facilities must import the standard library in one of the ways laid out in the following sections.

ASAM OpenSCENARIO provides three files with definitions that match the ones mandated by the ASAM OpenSCENARIO standard library: `types.osc`, `domain.osc`, and `standard.osc`.
Whether an implementation implements access to the standard library by importing some variant of these files, or through any other means (for example, by providing access to built-in definitions) is left to the implementation.

#### 7.7.5.2.1 Complete import of standard library

The full standard library, including all sub-modules thereof, can be imported with the following import statement:

Code 53. Import statement for use of the complete standard library

```
import osc.standard.all
```

This ensures that all the definitions of the standard library are accessible in their respective namespaces (meaning `std` and `stdtypes`).

If those namespaces are to be used, they need to be placed on the use list of the current namespace, via use clauses.

Note that in future releases more modules of the standard library might be defined, and all of them will be imported when using the import statement above.

#### 7.7.5.2.2 Partial import of standard library

If only one or more of the sub-modules of the standard library is needed, then they can be imported with one of the following import statements:

Code 54. Import statements for partial use of the standard library

```
import osc.standard.types # Imports the physical types and units and related structs
import osc.standard.domain # Imports the rest of the domain model
```

This ensures that all the definitions of the relevant standard library sub-module are accessible in their respective namespaces (meaning `stdtypes` or `std`).

If those namespaces are to be used, they need to be placed on the use list of the current namespace, via use clauses.

#### 7.7.5.2.3 Legacy import with auto-use of standard library

For backward-compatibility with ASAM OpenSCENARIO 2.0, the following import statement imports the full standard library and adds both the `std` and `stdtypes` namespaces to the use list of the `null` namespace:

Code 55. Import statement for legacy use of standard library

```
import osc.standard
```

This ensures that all the definitions of the standard library are accessible in unprefixed form from the `null` namespace, as long as no namespace statement is encountered.
Once a namespace statement is encountered, its namespace and use list specifications will take effect normally.

This facility is only intended for backward-compatibility with ASAM OpenSCENARIO 2.0, where this was the mandated way to import the standard library, and no namespaces existed.
Once a scenario is properly migrated to this or later releases, it should use one of the non-legacy mechanisms to import the standard library.