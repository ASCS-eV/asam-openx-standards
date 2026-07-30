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

### Reading the ShapeChange log

`{OUT}/opendrive-owl-log.xml` is written on every run, and **a successful exit code does not
mean everything in the model was encoded**. ShapeChange reports a class it cannot encode as a
warning and carries on:

> `Unsupported class category (enumeration). Ensure that the encoding rule includes a rule
> that enables the conversion of this type of class – unless your intention is to exclude
> this class category.`

This repository shipped an OpenDRIVE ontology with **none** of the model's 56 enumerations in
it, because that warning appeared 55 times and nobody read it. The output was 530 KB of
plausible-looking OWL, so nothing else gave the omission away. When changing the encoding
rule, check the log for warnings before trusting the artifact:

```bash
grep -c 'Unsupported class category' .pipeline-work/owl/opendrive-owl-log.xml
```

### Coverage of the current encoding

| Model construct | Count | In the OWL | In the SHACL |
|---|---:|---|---|
| Classes | 238 | yes | yes |
| Enumerations | 56 | 55, each an `rdfs:Datatype` with `owl:oneOf`. The 56th, `t_bool`, is mapped to `xsd:boolean` by `mapentries-asam.xml` | **no** — see below |
| Enumeration literals | 292 | 290. The two absent are `t_bool`'s `true` and `false`, which the mapping turns into `xsd:boolean` | **no** |
| Cardinality constraints | — | 908 restrictions | 908 `sh:minCount`/`sh:maxCount` |

Names are normalised by ShapeChange, so the model's `e_laneType` appears as
`odr:E_laneType`. Checking for a model name verbatim will report a false absence.

The enumerations reach the OWL but not the SHACL: the owl2shacl rulesets contain no rule
mapping `owl:oneOf` to `sh:in`, so the generated shapes constrain an enumerated attribute's
datatype but not its value set. Closing that gap means contributing an `owl:oneOf` → `sh:in`
rule upstream to owl2shacl, not post-processing the output here.

Until then, consumers that need enumerated **value** constraints — such as the
`ontology-management-base` `sh:in` lists — must derive them from the normative XSD in
`standards/<std>/schema/` rather than from these shapes.

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

Two rules deserve naming, because getting them wrong fails quietly:

- `rule-owl-prop-multiplicityAsQualifiedCardinalityRestriction` turns a UML multiplicity
  into a cardinality restriction, and is what ShapeChange#756 corrected.
- `rule-owl-cls-iso191502Enumeration` encodes each enumeration as an `rdfs:Datatype` with
  `owl:oneOf` over its literals. The alternative, `rule-owl-cls-enumerationAsCodelist`, is
  deliberately **not** used: it makes an enumeration fall through to the code list
  encoding, which only applies when `rule-owl-cls-codelist-191502` or `-external` is also
  present. With neither, every enumeration reaches the default branch and is dropped — see
  [Reading the ShapeChange log](#reading-the-shapechange-log).

### `mapentries-asam.xml` — type mapping

Maps the ASAM primitive types onto XSD datatypes. Without it, ShapeChange treats them as
unknown classes and the cardinality restrictions land on `owl:Class` rather than a data range.

`t_bool` is mapped to `xsd:boolean` here rather than encoded as an enumeration, which is
why 55 of the model's 56 enumerations are encoded and one is not.

### owl2shacl rules — the SHACL stage

`owl2sh-closed.ttl` is used: it closes the shapes, so an instance may not carry properties the
ontology does not declare. `owl2sh-open.ttl` and `owl2sh-semi-closed.ttl` are the looser
alternatives; the choice belongs in this file, not in the script.

## Adding a standard

Add an entry to `STANDARDS` in the script and a ShapeChange configuration here. No code
changes are required — the script is a path resolver and a runner.

## Not here yet

- **Enumerated value constraints in the SHACL.** The OWL carries `owl:oneOf`; owl2shacl has
  no rule that turns it into `sh:in`. See the coverage table above.
- **The XSD equivalence oracle.** ASAM ships normative XSDs alongside the UML; validating the
  generated SHACL against instance data that the XSD also accepts is the independent check
  that the derivation is faithful. That belongs in this pipeline as a third stage. It is also
  what would have caught the missing enumerations without anyone reading a log.
- **CI.** Blocked on ShapeChange#757: until a build without Enterprise Architect is possible
  upstream, a runner cannot build the tool. The generated artifacts are committed, so a CI job
  can eventually assert that regenerating them changes nothing — the same guarantee the
  ontology-management-base repository already applies to its own generated files.
- **OpenSCENARIO XML.** The model is committed; the configuration is not written yet.
