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

That is why the pipeline currently depends on five upstream contributions rather than a patch
directory. Every one of them is a general improvement, filed upstream, with the reasoning in
the pull request:

| Upstream PR | What it fixes | Why the pipeline needs it |
|---|---|---|
| [ShapeChange#756](https://github.com/ShapeChange/ShapeChange/pull/756) ✅ merged | Datatype qualified cardinality restrictions emitted `owl:onClass xsd:double`, which is not valid OWL 2 DL | Every typed attribute with a multiplicity |
| [ShapeChange#757](https://github.com/ShapeChange/ShapeChange/pull/757) ✅ merged | `shapechange-app` could not be built without a proprietary Enterprise Architect artifact | Building the tool in CI at all |
| [owl2shacl#7](https://github.com/sparna-git/owl2shacl/pull/7) | Data-property cardinality was dropped when converting OWL to SHACL | See the numbers below |
| [shacl-play#344](https://github.com/sparna-git/shacl-play/pull/344) | Conversion rules were fetched from a moving branch at run time | Reproducibility, and offline runs |
| [shacl-play#345](https://github.com/sparna-git/shacl-play/pull/345) | An input that could not be read produced an empty, plausible-looking output instead of failing | Trusting that a run with no errors actually converted something |

Both ShapeChange fixes are merged upstream, into `next`, its default branch — plain upstream
ShapeChange needs no fork and no branch switch any more (see [Running it](#running-it)).
owl2shacl#7 and shacl-play#344/#345 are still open, so those two tools are still built from a
`feature/asam-pipeline` branch on the `ASCS-eV` fork that carries exactly those commits on top
of upstream. When a pull request merges, its commit disappears from the branch on the next
rebase.

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
git clone https://github.com/ShapeChange/ShapeChange.git  # #756 and #757 both merged upstream
git clone https://github.com/ASCS-eV/shacl-play.git    && git -C shacl-play  switch feature/asam-pipeline
git clone https://github.com/ASCS-eV/owl2shacl.git     && git -C owl2shacl   switch feature/asam-pipeline

# build the SHACL converter once
mvn -f shacl-play/pom.xml -pl shacl-validator,shacl-play-app -am install -DskipTests

# the serialization stack, pinned — see "Why the output is byte-stable" below
pip install -r scripts/requirements.txt

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
SHA-256 of the source model, the configuration, and the rules, along with the ShapeChange and
owl2shacl commits and the versions of the serialization stack. That is what makes a difference
in the output diagnosable: it tells a reviewer whether the model changed, the configuration
changed, or the toolchain did.

The ruleset is recorded by commit as well as by checksum, because a checksum alone proves two
runs used the same bytes but not that a third party can obtain them. An earlier provenance
record in this branch's history carried a rules checksum that matched no commit in the
owl2shacl repository — the run had picked up an unversioned working copy. `"commit": "unknown"`
in that field means the same thing and should be treated as a reproducibility gap.

### Why the output is byte-stable

ShapeChange and shacl-play both label blank nodes from process-dependent ordering, so
regenerating an unchanged model used to produce a large diff that meant nothing: the earlier
regeneration in this branch changed 1,428 lines of `opendrive.owl.ttl` while the triple set
stayed identical, and confirming that took a graph-isomorphism comparison by hand.

Both artifacts are therefore written in RDFC-1.0 canonical form, via
[`diffable-rdf`](https://github.com/ASCS-eV/diffable-rdf) — canonicalization plus
Weisfeiler-Lehman blank-node hashing, so a changed triple only touches the blank nodes it
actually involves. Every triple is preserved and the triple count is asserted before the file
is written; only the syntactic form changes. The OWL is canonicalized *before* the SHACL stage
reads it, so stage 2 gets a deterministic input too.

This is why `scripts/requirements.txt` pins exact versions rather than ranges: rdflib performs
the final serialization, so a minor bump there can reintroduce the churn, arriving in review
looking like a semantic change. `provenance.json` records the resolved versions, and
`scripts/check_canonical.py` (run in CI) fails if a committed artifact is not in canonical form.

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

Reading the log is no longer left to whoever remembers. `check_shapechange_log()` parses it on
every run and stops the pipeline unless everything in it is a condition this repository has
already explained:

- **227 tolerated errors.** `rule-owl-pkg-singleOntologyPerSchema` reports *"no schema package
  was found for class X"* for 227 of the 238 classes. The OpenDRIVE EA model tags all seven
  sub-packages with the same `targetNamespace`, so ShapeChange sees eight schemas resolving to
  one ontology name and complains about every class outside the schema it is processing. The
  emitted ontology is complete regardless — verified class by class — so these are counted and
  reported rather than hidden, and **any other error fails the build**.
- **2 known union-encoding defects.** ShapeChange rejects the supertype structure of
  `e_countryCode` and `t_grEqZeroOrContactPoint`, because the EA model encodes XSD unions as
  generalizations. This is the model-side gap documented under "Known encoding gaps" in
  `standards/asam-opendrive/uml/README.md`. If the warning names a class outside the documented
  set, the build fails: that is either a change in the EA model or a new defect, and both
  deserve a decision rather than a silent artifact.

Widening either allowlist means editing `TOLERATED_ERRORS` or `KNOWN_UNION_DEFECTS` in
`scripts/generate_semantic_artifacts.py` *and* saying why in the model's README, in the same
change.

### Coverage of the current encoding

| Model construct | Count | In the OWL | In the SHACL |
|---|---:|---|---|
| Classes | 238 | yes | yes |
| Enumerations | 56 | 55, each an `rdfs:Datatype` with `owl:oneOf`. The 56th, `t_bool`, is mapped to `xsd:boolean` by `mapentries-asam.xml` | **no** — see below |
| Enumeration literals | 292 | 290. The two absent are `t_bool`'s `true` and `false`, which the mapping turns into `xsd:boolean` | **no** |
| Cardinality constraints | — | 585 `owl:Restriction` nodes (324 exact, 33 minimum-only, 228 maximum-only) | 908 `sh:minCount`/`sh:maxCount` triples |

The OWL and SHACL numbers count different things, not the same restrictions twice: an exact
cardinality (`owl:qualifiedCardinality`) is **one** OWL restriction node but becomes **two**
SHACL triples, `sh:minCount` and `sh:maxCount` with the same value. That accounts for most of
the gap between 585 and 908 — read "908" as a SHACL triple count, not an OWL restriction count.

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
- **CI.** No longer blocked on ShapeChange: #757 merged upstream, so a runner can build it
  today with a plain clone of `ShapeChange/ShapeChange` and no Enterprise Architect
  installation. owl2shacl#7 and shacl-play#344/#345 are still open, so a CI job would have to
  build those two tools from the `ASCS-eV` fork's `feature/asam-pipeline` branch rather than a
  released version — workable, but not what a CI job should depend on long-term. The generated
  artifacts are committed, so a CI job can assert that regenerating them changes nothing — the
  same guarantee the ontology-management-base repository already applies to its own generated
  files.
- **OpenSCENARIO XML.** The model is committed; the configuration is not written yet.
