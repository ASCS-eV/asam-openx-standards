# ASAM OpenSCENARIO® XML UML Model (SCXML) — V1.4.0

The **open, tool-neutral UML model** of ASAM OpenSCENARIO® XML V1.4.0 (the `.xosc`
format), exported once from Enterprise Architect and committed here so that every
downstream generation step — OWL, SHACL, XSD — runs **without an Enterprise Architect
licence**.

This is the **XML** standard, not OpenSCENARIO® **DSL** (see `../../asam-openscenario-dsl/`).

**These files are not original works of this project.** They are derived from ASAM's
`OpenSCENARIO.qeax` Enterprise Architect project. Copyright © ASAM e.V., 2026.
Redistributed under the ASAM Unrestricted Distribution Clause; see the repository
[LICENSE](../../../LICENSE).

## Provenance

| Field | Value |
|---|---|
| Standard | ASAM OpenSCENARIO® XML |
| Version | **V1.4.0** — matches the normative schema in [`../schema/`](../schema/) |
| Origin | `OpenSCENARIO.qeax` (Enterprise Architect project) |
| Exported by | ShapeChange built from source at commit [`1a16d4af3336`](https://github.com/ShapeChange/ShapeChange/commit/1a16d4af333627059d12d271f588e903e6ecb172) (`next` branch, 2026-07-30), `ModelExport` target, `inputModelType=EA7`, `zipOutput=true` |
| Producer header | `scxmlProducer="ShapeChange"`, `scxmlProducerVersion="4.1.0-SNAPSHOT"` |
| Classes | 343 |

### Why a commit, not a numbered ShapeChange release

The `4.0.0` release cannot build the EA/`eaapi` module from source at all — that only
became possible once [ShapeChange#756](https://github.com/ShapeChange/ShapeChange/pull/756)
and [#757](https://github.com/ShapeChange/ShapeChange/pull/757) merged, making the module
an optional Maven profile (`ea`, active unless `-DskipEa` is passed). Both are on `next`
but not yet in a numbered release, so we cite the exact commit above instead. We verified
it changes nothing in this export except the producer-version string in the header — see
[`export-model-to-scxml.config.xml`](export-model-to-scxml.config.xml) and
[Reproducing the export](#reproducing-the-export-requires-ea-once) below for the full
from-source build. The maintainer has indicated a `4.1.0` release is planned; we intend to
switch this citation to that release once it ships.

### Why the export config declares a `PackageInfo` override

Unlike OpenDRIVE, the OpenSCENARIO XML schema
([`../schema/OpenSCENARIO.xsd`](../schema/OpenSCENARIO.xsd)) declares no XML
`targetNamespace` at all, so its EA model has no package carrying that tagged value —
ShapeChange's schema detection has nothing to find and aborts with "None of the packages
... is a schema selected for processing". `export-model-to-scxml.config.xml` therefore
adds a `<PackageInfo packageName="OpenSCENARIO" ns="..."/>` override to select that
package regardless. The `ns` value is a ShapeChange bookkeeping placeholder only: it is not
written into the exported model, so it has no bearing on the standard itself. Verified three
ways — `openscenario.scxml` contains zero occurrences of `targetNamespace`, zero occurrences
of the `ns` URI itself, and zero occurrences of the `nsabr` abbreviation.

### How the version is established

The export carries no ASAM version stamp of its own — the producer version in the file
header identifies ShapeChange, not the standard. The revision is therefore determined
against the normative schema in `../schema/`, which is the version-pinned artifact:

- All **6** types V1.4.0 added over V1.3.1 are present in the model: `Interpolation`,
  `LaneLayerType`, `Motion`, `PreferredLaneLayerAction`,
  `TrafficDistributionEntryCatalogLocation` and `TrafficSignalSemantics`. The model is
  therefore V1.4.0 and not the previous revision.

Model and schema do not enumerate the same names, because UML and XML Schema encode the
same information differently. Neither direction indicates drift:

- **14 XSD types have no model class.** Nine are `xs:simpleType` primitives and
  parameterisable value types (`Boolean`, `Double`, `Int`, `String`, `UnsignedInt`,
  `UnsignedShort`, `DateTime`, `expression`, `parameter`), which map to UML primitives
  rather than classes. The other five — `MonitorDeclarations`, `ParameterDeclarations`,
  `VariableDeclarations`, `ParameterAssignments`, `TrafficSignals` — are XML list
  wrappers, each holding exactly one `maxOccurs="unbounded"` child; UML expresses that as
  a multiplicity on the owning class, so no wrapper class exists.
- **18 model classes have no named XSD type**, where "type" means a top-level
  `xs:complexType` or `xs:simpleType`. Thirteen of them do appear in the schema, as
  same-named top-level `xs:group` declarations — `EntityObject`, `ScenarioDefinition`,
  `CatalogDefinition`, `BrakeInput`, `Gear`, `SteadyState`, `OpenScenarioCategory`,
  `DistributionDefinition`, `ParameterValueDistributionDefinition` and the
  `*DistributionType` family — which is how the schema flattens a UML abstraction into a
  choice. Grepping the XSD for one of those names will find it; that is not drift. Only
  five have no counterpart in the schema at all: `Entity`, `StoryboardElement`,
  `CatalogElement`, `MotionControlAction` and `SpawnedObject`.

## Files

| File | What it is |
|------|------------|
| `openscenario.scxml` | The model in ShapeChange SCXML (plain XML, diff-friendly). **Source of truth** for all downstream generation. |
| `openscenario.scxml.zip` | The `ModelExport` artifact exactly as ShapeChange wrote it (`zipOutput=true`), directly consumable as a ShapeChange `inputFile`. |
| `export-model-to-scxml.config.xml` | The ShapeChange `ModelExport` configuration that produced both files **from EA**. |

### `.scxml` and `.scxml.zip` are the same model, in different line endings

The zip's `ModelExport.xml` entry is byte-identical to `openscenario.scxml` **after
converting CRLF to LF** — the export ran on Windows, and the committed `.scxml` is
normalised to LF for the repository. The two therefore have different checksums by
design, and comparing them byte-for-byte will report a difference that is not one:

| Artifact | Bytes | CRLF line endings | SHA-256 (truncated) |
|---|---:|---:|---|
| `openscenario.scxml` | 1,925,508 | 0 | `2fcea5c4a5fc91e8…` |
| `ModelExport.xml` inside the zip | 1,962,833 | 37,325 | `39339125d258399e…` |
| `openscenario.scxml.zip` | 118,375 | — | `2b6aa53090a3cf4b…` |

The 37,325-byte difference is exactly one `\r` per line. Use `openscenario.scxml` unless
a tool requires the zip.

### Why the export is diff-friendly

Not because of a sort parameter. ShapeChange's `sortedSchemaOutput` orders the *schemas* it
processes, not the classes within one; class order is `sortedOutput`, and `ModelExport` ignores
that parameter — verified against this model, as both an input and a target parameter, with the
output unchanged either way. Element order therefore follows the source model, and no package
in this export is alphabetical.

What makes the file reviewable is that `ModelExport` is **deterministic**: the committed
`.scxml` is a fixed point of the exporter. Re-running `ModelExport` over it, using the
committed `export-model-to-scxml.config.xml` with only `inputModelType` switched from `EA7` to
`SCXML`, reproduces the committed bytes exactly. Element order is a function of the model, not
of the run, so re-exporting an unchanged model yields an unchanged file and any diff here
reflects a real change in the Enterprise Architect project.

## Using the model without EA (the normal case)

This model drives the generation pipeline in this repository. No EA is required:

```bash
python scripts/generate_semantic_artifacts.py \
    --standard asam-openscenario-xml \
    --shapechange ../ShapeChange \
    --shaclplay ../shacl-play/shacl-play-app/target/shacl-play-app-0.12.2-onejar.jar \
    --rules ../owl2shacl/owl2sh-closed.ttl
```

It produces `../generated/openscenario.owl.ttl`, `../generated/openscenario.shacl.ttl` and a
`provenance.json` recording exactly what produced them. See [`pipeline/README.md`](../../../pipeline/README.md)
for the configuration, what is checked on every run, and the structural comparison against
ASAM's normative XSD.

Any other ShapeChange configuration can read the model the same way: point `inputFile` at
`openscenario.scxml` (or `openscenario.scxml.zip`) and set `inputModelType=SCXML`.

### What the generated artifacts cover

Every one of the model's 343 classes reaches the ontology — 304 as `owl:Class`, 39 as an
`rdfs:Datatype` with `owl:oneOf` — and that is asserted on every run, not assumed. The 48
`<<union>>` classes are encoded as OWL disjunctions, and the ShapeChange log is free of errors
and warnings, so the pipeline tolerates none for this standard. See the coverage table in
[`pipeline/README.md`](../../../pipeline/README.md).

One modelling issue is known, and it is visible only in the XSD comparison:
`ActivateControllerAction.objectControllerRef` is modelled as an association to
`ObjectController`, a `<<union>>`, while ASAM's normative schema declares it `type="String"` — a
reference by name. 34 `*Ref` properties share that shape; this one fails loudly because a union
has no identity for a reference to point at. Filed as an ASAM change request.

## Reproducing the export (requires EA once)

Only this step needs EA. Everything downstream consumes the committed `*.scxml`.

`eaapi.jar` (the EA Java API) is not published to Maven Central — it ships with your EA
installation and must be installed into your local Maven repository once, using the exact
coordinates the ShapeChange `ea` module expects:

```bash
mvn install:install-file \
    -Dfile="C:/Program Files/Sparx Systems/EA/Java API/eaapi.jar" \
    -DgroupId=org.sparx -DartifactId=eaapi -Dversion=17.0.1704 -Dpackaging=jar
```

Build ShapeChange from source at the commit in the provenance table above (the `ea`
Maven profile is active by default and bundles the EA module using the `eaapi` installed
above):

```bash
git clone https://github.com/ShapeChange/ShapeChange.git
cd ShapeChange
git checkout 1a16d4af333627059d12d271f588e903e6ecb172
mvn install
```

This produces `shapechange-app/target/ShapeChange-4.1.0-SNAPSHOT.zip`; unzip it, then run
the export. The native EA↔Java bridge DLL (`SSJavaCOM64.dll`) lives in the EA installation,
not in ShapeChange's own distribution, so `-Djava.library.path` must point there:

```bash
java -Djava.library.path="C:/Program Files/Sparx Systems/EA/Java API" \
     -jar ShapeChange-4.1.0-SNAPSHOT.jar -c export-model-to-scxml.config.xml \
     -x "$inputFile$" "C:/path/to/OpenSCENARIO.qeax"
```

This writes `scxml-out/INPUT/ModelExport.zip`; unzip to obtain the SCXML, and normalise its
line endings to LF before committing. The configuration needs no editing: it runs as
committed, and carries no absolute paths.

Two things to settle at the next re-export, deliberately left alone here because changing
them would mean the committed artifacts were no longer what this configuration produces:

- **`outputFilename`.** Unset, so `ModelExport` uses its default and the zip entry is called
  `ModelExport.xml` rather than something that identifies the standard. Setting it changes
  the zip's contents, so it belongs with a real re-export.
- **`representTaggedValues`.** Unset, so only tagged values ShapeChange already knows are
  carried; this export contains just `targetNamespace` and `xmlns`. Whether ASAM annotates
  the Enterprise Architect model further — deprecation, version-added — cannot be
  determined from the export itself. Run the export once with and once without the
  parameter and diff, then either set it or record that there was nothing to carry.
