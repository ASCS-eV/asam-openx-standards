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
| Origin | [`source/OpenSCENARIO.qeax`](source/README.md) (Enterprise Architect project, committed) |
| Exported by | ShapeChange built from source at commit [`f4ee27b5`](https://github.com/ASCS-eV/ShapeChange/commit/f4ee27b5) (`ASCS-eV/ShapeChange`, branch `feature/asam-pipeline` = upstream `next` `7a44ce20` plus one carried commit that touches only the OWL target), `ModelExport` target, `inputModelType=EA7`, `zipOutput=true` |
| Producer header | `scxmlProducer="ShapeChange"`, `scxmlProducerVersion="4.1.0-SNAPSHOT"` |
| Classes | 343 |
| Stereotypes | 1,582 — the EA XML Schema profile, carried via `addStereotypes` |
| Tagged values | 1,073 — a curated set, carried via `representTaggedValues` |

### Why a commit, not a numbered ShapeChange release

The `4.0.0` release cannot build the EA/`eaapi` module from source at all — that only
became possible once the EA module upstream became an optional Maven profile (`ea`,
active unless `-DskipEa` is passed). That change is on `next` but not yet in a numbered
release, so we cite the exact commit above instead. We verified
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

### `.scxml` and `.scxml.zip` hold identical bytes

The zip's `openscenario.xml` entry is **byte-identical** to `openscenario.scxml`. Earlier
exports differed by line endings — the export ran on Windows and produced CRLF, which had to be
normalised before committing — but the exporter now writes LF on every platform, so the two
agree without conversion:

| Artifact | Bytes | CR bytes | SHA-256 (truncated) |
|---|---:|---:|---|
| `openscenario.scxml` | 2,358,883 | 0 | `5a0831d306b7bc91…` |
| `openscenario.xml` inside the zip | 2,358,883 | 0 | `5a0831d306b7bc91…` |
| `openscenario.scxml.zip` | 129,272 | — | `bee4ab9514366fd4…` |

Use `openscenario.scxml` unless a tool requires the zip. The zip entry is named for the
standard rather than the exporter because the configuration sets `outputFilename`; it used to
be `ModelExport.xml`, which said nothing about what it contained.

### Why the export is diff-friendly

Two properties, both of which the exporter now provides by default.

**Element order is a function of the model's names, not of Enterprise Architect's ids.**
Packages and classes are emitted in name order. This matters because EA's internal element ids
shift whenever the project is edited, and an id-ordered file would reshuffle for reasons that
have nothing to do with the model. A diff against an export made before ShapeChange `7a44ce20`
therefore shows a wholesale reordering that carries no meaning.

The `sortedOutput` parameter is deliberately **not** set: it was verified byte-for-byte inert
against this model, because the order it requests is the order already produced.

**`ModelExport` is deterministic.** The committed `.scxml` is a fixed point of the exporter:
re-running `ModelExport` over it, using the committed `export-model-to-scxml.config.xml` with
only `inputModelType` switched from `EA7` to `SCXML`, reproduces the committed bytes. Any diff
here therefore reflects a real change in the Enterprise Architect project or in the exporter,
and the project itself is now committed under [`source/`](source/README.md) so the two can be
told apart.

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

This writes `scxml-out/INPUT/openscenario.zip`; unzip to obtain the SCXML. The exporter writes
LF on every platform, so no line-ending normalisation is needed before committing. The
configuration needs no editing: it runs as committed, and carries no absolute paths.

### What the export carries, and what it deliberately does not

The configuration sets `addStereotypes="*"` and a named `representTaggedValues` list. Without
them the export drops 1,495 of 1,582 stereotypes and every tagged value bar two.

Carried because the model populates them:

| | Count with a value | What it is |
|---|---:|---|
| `XSDelement` / `XSDattribute` (stereotypes) | 419 / 448 | the element-vs-attribute distinction, which nothing downstream previously had any basis for |
| `xor` (stereotype, on connectors) | 171 | explicit exclusive-choice constraints between associations |
| `union` (stereotype) | 48 | already well-known; encoded as `owl:unionOf` |
| `position` | 450 | element order within a content model |
| `modelGroup` | 295 | XSD content-model kind: `sequence`, `all`, `choice` |
| `mixed` | 282 | mixed content |
| `withVersion` | 39 | this standard's spelling of OpenDRIVE's `introducedAtVersion` |

Left out because the model declares them but leaves them empty:

`use` (165 present, **0** with a value), `memberNames` (72 present, 0), and `form`, `fixed`,
`default` (106 present each, 0).

That `use` is empty here is worth noting on its own: OpenDRIVE populates 365 of its 444 with
`required` / `optional`, so this standard cannot express attribute requiredness at all. Along
with the `XSDunion` / `«union»` divergence, it is one of the cross-standard inconsistencies
raised with ASAM in
[#6](https://github.com/ASCS-eV/asam-openx-standards/issues/6).

### Exclusive choice is carried but not yet honoured

The model marks **55 classes `modelGroup = choice`** and 56 `all`, and applies 171 `xor`
stereotypes to connectors. The export now carries all of this, but the OWL, SHACL and XSD
targets still generate a sequence requiring **all** members, so a generated artifact rejects
documents the normative schema accepts. Tracked in
[#37](https://github.com/ASCS-eV/asam-openx-standards/issues/37).
