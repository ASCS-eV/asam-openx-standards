# ASAM OpenSCENARIO® DSL v2.2.0 — 8.13 Primitive types and structs

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/domain-model/primitive_types.html
> **Standard**: ASAM OpenSCENARIO® DSL v2.2.0, 2026-03-19
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 8.13 Primitive types and structs

The following definitions constitute the types sub-module of the standard library.
They are reflected in `types.osc`, and are made available via either `import osc.standard.types`, `import osc.standard.all`, or `import osc.standard` statements, as defined in [Importing the standard library](../language-reference/Libraries.html#code-lc-libraries-file-import-standard-library).
They reside in the `stdtypes` namespace.

### 1 String Methods

The standard library provides the following methods on strings in the `std` namespace:

| Method | Method declaration fragment | Description | Example |
| --- | --- | --- | --- |
| `<string>.length()` | def length() → int | Returns the length of a string. | `"Hello".length() #Returns 5` |
| `<string>.contains(<string>)` | def contains(substring: string) → bool | Returns true if a string contains a substring. | `"Hello".contains("ell") #Returns true` |
| `<string>.substring(<integer>[, <integer>])` | def substring(start: int, end: int) → string | Returns a substring of a string. Indexing is zero-based. The start index, is inclusive, the end index, which defaults to the end of the string, is exclusive. Negative indices index from the end of the string, with -1 being the last character of the string. Indices that are out of bounds are silently truncated to be in bounds. | `"Hello".substring(1, 3) #Returns "el"` |
| `<string>.split(<string>)` | def split(separator: string) → list of string | Splits a string into a list of substrings using the argument as the separator, empty strings are retained. | `"Hello".split("el") #Returns ["H", "lo"]` |
| `<string>.join(<list of string>)` | def join(parts: list of string) → string | Concatenates a list of strings connected by a separator. | `"_".join(["We","were","four","once"]) #Returns "We_were_four_once"` |
| `<string>.replace(<string>, <string>)` | def replace(old: string, new: string) → string | Replaces all occurrences of a substring in the string with another substring. | `"Hello".replace("l", "LL") #Returns "HeLLLLo"` |
| `<string>.trim()` | def trim() → string | Removes leading and trailing whitespace from a string. | `" Hello ".trim() #Returns "Hello"` |