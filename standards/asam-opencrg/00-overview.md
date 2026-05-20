# ASAM OpenCRG® — Overview

- **Source**: https://github.com/ASAM-ev/OpenCRG
- **Version**: v1.2.0
- **License**: Apache-2.0
- **Date retrieved**: 2025-05-19

## Summary

ASAM OpenCRG defines a file format for the description of road surfaces. It was
originally developed to store high-precision elevation data from road surface scans.
The primary use for this data is in tire, vibration or driving simulation.

## Key Concepts

### Curved Regular Grid (CRG)

The standard describes a method to store data in a specific layout called "curved
regular grid". The advantages are:

- High memory efficiency
- Low computation time for file generation and data processing
- High accuracy of positioning data onto road networks

### Basic Principle

The basic principle for describing the road surface is to place data into a grid
along a road reference line:

- Line segments described by start position and heading angle
- Grid produced by longitudinal cuts (columns) and lateral cuts (rows)
- Each cell has a value (typically elevation)
- Road center line includes end position for drift detection/correction

### File Format

ASAM OpenCRG defines ASCII and binary file formats with clear-text headers containing:

- Road parameters for the reference line
- Overall configuration of longitudinal sections
- Data format definition (ASCII and binary)
- Sequence of data expected in the trailing data block
- Modifier and option parameters
- References to other files for handling different parameters

## Integration with Other Standards

- **OpenDRIVE**: CRG data can be included in OpenDRIVE road network descriptions
- **OpenSCENARIO**: Dynamic content (vehicle maneuvers) described with OpenSCENARIO
- Together they cover static and dynamic content of in-the-loop vehicle simulation

## Software Libraries

The standard is delivered with software libraries in:

- **ANSI-C**: Reading CRG files, modifying and evaluating imported data
- **MATLAB**: Reading, generating, analyzing, and visualizing data

## Relevance to ENVITED-X

| ENVITED-X Domain | Relationship |
|-----------------|--------------|
| `surface-model` | Direct — OpenCRG defines the road surface file format |
| `hdmap` | Complementary — CRG referenced from OpenDRIVE road networks |
| `scenario` | Complementary — surface properties affect simulation fidelity |
