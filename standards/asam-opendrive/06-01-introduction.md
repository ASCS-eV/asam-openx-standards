# ASAM Opendrive v1.9.0 — 6.1 Introduction to general architecture

> **Source**: https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/latest/specification/06_general_architecture/06_01_introduction.html
> **Standard**: ASAM Opendrive v1.9.0, 2026-05-08
> **License**: Unrestricted distribution (ASAM e.V.)
> **Downloaded**: 2026-05-19

---

# 6.1 Introduction to general architecture

ASAM OpenDRIVE data is stored in XML files with the extension `xodr`.
Compressed ASAM OpenDRIVE files have the extension `xodrz` (compression format: `gzip`).

The ASAM OpenDRIVE file structure conforms to XML rules; the associated schema file is referenced in the XML.
The schema files for the ASAM OpenDRIVE format can be retrieved from [Section "Deliverables"](../00_preface/00_introduction.html#sec-bbc4fe63-ed72-4092-8ae4-f1733fcff502).

Elements are organized into levels.
Elements with a level greater than zero (0) are children of the preceding level.
Elements with a level of one (1) are called primary elements.

Each element can be extended with user-defined data.
This data is stored in user data elements.

All floating-point numbers used in ASAM OpenDRIVE are IEEE 754 [[1](../bibliography.html#bib-ieee754_2019)] double precision floating-point numbers.
To ensure accurate representation of floating-point numbers in the XML representation, implementations should use a known correct accuracy preserving minimal floating-point printing algorithm (for example [[14](../bibliography.html#bib-Burger_Dybvig_1996)], [[15](../bibliography.html#bib-Adams_2018)]) or ensure that 17 significant decimal digits are always produced, for example using the "%.17g" ISO C printf modifier.
Importing implementations should use a known correct accuracy preserving floating-point reading algorithm (for example [[16](../bibliography.html#bib-Clinger_1990)]).