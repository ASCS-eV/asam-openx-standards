# From ASAM UML to OWL and SHACL

This directory holds the configuration that turns the committed ASAM UML models into
machine-readable artifacts:

```
standards/<std>/uml/<std>.scxml          the ASAM model, exported from Enterprise Architect
        │                                 once and committed, so nobody else needs EA
        ▼  ShapeChange, OWL target
standards/<std>/generated/<std>.owl.ttl   an OWL 2 ontology
        │
        ▼  SHACL Play!, owl2shacl rules
standards/<std>/generated/<std>.shacl.ttl SHACL shapes
```

Run it with [`scripts/generate_semantic_artifacts.py`](../scripts/generate_semantic_artifacts.py).

## The rule that shapes everything here

**Nothing is post-processed.** Both stages are off-the-shelf tools driven by the
configuration in this directory; the script only resolves paths and runs them in order. If a
generated artifact is wrong, exactly one of three things is wrong — the **model**, the
**configuration**, or the **tool** — and the fix belongs there.

That is why the pipeline currently depends on four upstream contributions rather than a patch
directory. Every one of them is a general improvement, filed upstream, with the reasoning in
the pull request:

| Upstream PR | What it fixes | Why the pipeline needs it |
|---|---|---|
| [ShapeChange#756](https://github.com/ShapeChange/ShapeChange/pull/756) ✅ merged | Datatype qualified cardinality restrictions emitted `owl:onClass xsd:double`, which is not valid OWL 2 DL | Every typed attribute with a multiplicity |
| [ShapeChange#757](https://github.com/ShapeChange/ShapeChange/pull/757) | `shapechange-app` could not be built without a proprietary Enterprise Architect artifact | Building the tool in CI at all |
| [owl2shacl#7](https://github.com/sparna-git/owl2shacl/pull/7) | Data-property cardinality was dropped when converting OWL to SHACL | See the numbers below |
| [shacl-play#344](https://github.com/sparna-git/shacl-play/pull/344) | Conversion rules were fetched from a moving branch at run time | Reproducibility, and offline runs |

Until they land, each tool is used from a `feature/asam-pipeline` branch that carries exactly
those commits, one per open pull request, on top of upstream. When a pull request merges, its
commit disappears from the branch on the next rebase.

### What owl2shacl#7 is worth here

Converting the same generated OpenDRIVE ontology twice, changing only the rules:

| Rules | `sh:minCount` / `sh:maxCount` constraints |
|---|---|
| Pinned, with owl2shacl#7 | **908** |
| Upstream `main` | 278 |

630 constraints — every required or optional typed attribute in OpenDRIVE — are silently lost
without the fix. The shapes still look plausible, which is what makes it worth pinning the
rules rather than fetching whatever the branch holds today.

## Running it

You need JDK 21, Maven, and checkouts of the two tools:

```bash
git clone https://github.com/ASCS-eV/ShapeChange.git   && git -C ShapeChange switch feature/asam-pipeline
git clone https://github.com/ASCS-eV/shacl-play.git    && git -C shacl-play  switch feature/asam-pipeline
git clone https://github.com/ASCS-eV/owl2shacl.git     && git -C owl2shacl   switch feature/asam-pipeline

# build the SHACL converter once
mvn -f shacl-play/pom.xml -pl shacl-validator,shacl-play-app -am install -DskipTests

python scripts/generate_semantic_artifacts.py \
    --standard asam-opendrive \
    --shapechange ../ShapeChange \
    --shaclplay ../shacl-play/shacl-play-app/target/shacl-play-app-0.12.2-onejar.jar \
    --rules ../owl2shacl/owl2sh-closed.ttl
```

ShapeChange is built by the script itself, with `-DskipEa`, so no Enterprise Architect licence
is involved. EA is needed only to re-export a `.scxml` model, and those exports are committed.

## What comes out, and how to trust it

`standards/<std>/generated/` holds the two artifacts plus `provenance.json`, which records the
SHA-256 of the source model, the configuration, and the rules, along with the ShapeChange
commit. That is what makes a difference in the output diagnosable: it tells a reviewer whether
the model changed, the configuration changed, or the toolchain did.

## The configuration, stage by stage

### `opendrive-owl.config.xml` — ShapeChange, OWL target

- `inputModelType=SCXML` reads the committed model. `EA7` would read a `.qea` repository and
  require Enterprise Architect; the SCXML export exists precisely to avoid that.
- The `asam-owl` encoding rule selects the OWL constructs the ASAM models actually use.
  `rule-owl-prop-multiplicityAsQualifiedCardinalityRestriction` is the one that turns a UML
  multiplicity into a cardinality restriction, and is what ShapeChange#756 corrected.
- `{SHAPECHANGE_RESOURCES}`, `{PIPELINE}` and `{OUT}` are substituted by the script. Only the
  first depends on where the tool lives; the model and output paths are repository-relative so
  the configuration reads the same for everyone.

### `mapentries-asam.xml` — type mapping

Maps the ASAM primitive types onto XSD datatypes. Without it, ShapeChange treats them as
unknown classes and the cardinality restrictions land on `owl:Class` rather than a data range.

### owl2shacl rules — the SHACL stage

`owl2sh-closed.ttl` is used: it closes the shapes, so an instance may not carry properties the
ontology does not declare. `owl2sh-open.ttl` and `owl2sh-semi-closed.ttl` are the looser
alternatives; the choice belongs in this file, not in the script.

## Adding a standard

Add an entry to `STANDARDS` in the script and a ShapeChange configuration here. No code
changes are required — the script is a path resolver and a runner.

## Not here yet

- **The XSD equivalence oracle.** ASAM ships normative XSDs alongside the UML; validating the
  generated SHACL against instance data that the XSD also accepts is the independent check
  that the derivation is faithful. That belongs in this pipeline as a third stage.
- **CI.** Blocked on ShapeChange#757: until a build without Enterprise Architect is possible
  upstream, a runner cannot build the tool. The generated artifacts are committed, so a CI job
  can eventually assert that regenerating them changes nothing — the same guarantee the
  ontology-management-base repository already applies to its own generated files.
- **OpenSCENARIO XML.** The model is committed; the configuration is not written yet.
