# From ASAM UML to OWL and SHACL — Operational Runbook

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

A second script, [`scripts/check_xsd_structural_parity.py`](../scripts/check_xsd_structural_parity.py),
does not produce an artifact at all: it checks the same model against ASAM's independently
published XSD. See [Checking it](#checking-it-the-xsd-structural-parity-check) below.

## The rule that shapes everything here

**Nothing is post-processed.** Both stages are off-the-shelf tools driven by the
configuration in this directory; the script only resolves paths and runs them in order. If a
generated artifact is wrong, exactly one of three things is wrong — the **model**, the
**configuration**, or the **tool** — and the fix belongs there.

ShapeChange and the SHACL Play! owl2shacl converter are both consumed from `feature/asam-pipeline`
branches on the `ASCS-eV` forks of each tool, rebased on the fork's stated upstream development
branch with only the pending upstream-contribution commits cherry-picked on top. Those branches
carry the fixes the pipeline depends on, applied as self-contained upstream contributions:
[ShapeChange#764](https://github.com/ShapeChange/ShapeChange/pull/764) and
[#766](https://github.com/ShapeChange/ShapeChange/pull/766);
[owl2shacl#7](https://github.com/sparna-git/owl2shacl/pull/7) and
[#8](https://github.com/sparna-git/owl2shacl/pull/8);
[shacl-play#344](https://github.com/sparna-git/shacl-play/pull/344),
[#345](https://github.com/sparna-git/shacl-play/pull/345) and
[#346](https://github.com/sparna-git/shacl-play/pull/346). Tracked in
[ASCS-eV/asam-openx-standards#7](https://github.com/ASCS-eV/asam-openx-standards/issues/7)
(ShapeChange) and
[#9](https://github.com/ASCS-eV/asam-openx-standards/issues/9) (owl2shacl, SHACL Play): when an
upstream PR merges, that issue is where the transition to a released upstream commit is decided
and recorded — never a silent branch drift.

## The toolchain lock

[`pipeline/toolchain-lock.json`](toolchain-lock.json) pins every input that determines the output
bytes: for each fork, its exact commit, the upstream development branch and base commit it was
rebased on, and the ordered list of commits it carries on top (each mapped to the upstream PR it
implements); the exact Python serialization versions from
[`scripts/requirements.txt`](../scripts/requirements.txt); and the exact JDK/Maven build
environment plus content-based fingerprints of the built ShapeChange runtime and the built SHACL
Play jar.

`scripts/generate_semantic_artifacts.py` validates every tool checkout against this lock before
building anything: the checkout must be clean, at the exact locked commit, with the locked
upstream base an ancestor and the actual carried-commit list matching exactly. `--shaclplay` is
therefore a checkout root, not a pre-built jar — the jar is always rebuilt here from that locked
source, so the binary that runs is provably the one the lock describes, never a stale artifact
left over from an earlier build.

**Two independent checks, not one:**

- `scripts/check_toolchain_lock.py` is static — no JDK, no Maven, no network, no tool checkout.
  It proves the lock is internally consistent and that every committed `provenance.json` matches
  what the lock claims produced it. This is the one CI can always run, and it is wired into
  [`.github/workflows/verify-generated.yml`](../.github/workflows/verify-generated.yml).
- `scripts/generate_semantic_artifacts.py` itself proves the *live* checkouts still match the
  lock and reproduce the same `build_inputs` fingerprints — this needs the sibling tool
  checkouts and a JDK/Maven, so it runs wherever a maintainer regenerates, not in ordinary CI.

**Updating the lock is a release-like action, never a routine edit:**

```bash
# 1. Rebase the fork on its current upstream development branch, re-cherry-pick the
#    pending contributions (see the issue for which PRs are still open)
git -C ../ShapeChange fetch upstream next
git -C ../ShapeChange rebase upstream/next   # or re-apply the cherry-picks after a reset

# 2. Update pipeline/toolchain-lock.json: the new commit, the new upstream_base if it
#    moved, and the exact carried_commits (compare with `git rev-list --reverse
#    <upstream_base>..HEAD`)

# 3. Regenerate both standards TWICE with a clean build each time, and confirm the
#    build_inputs fingerprints and the generated OWL/SHACL bytes are identical between
#    the two runs before trusting either value
just  # or invoke scripts/generate_semantic_artifacts.py directly, see below

# 4. Commit the lock update, the regenerated artifacts, and the provenance together,
#    with the reasoning in the commit message
```

Never lock a raw file hash for a built jar: SHACL Play's onejar embeds per-entry ZIP timestamps,
so its raw file SHA-256 differs on every clean build even from identical source — verified across
three independent builds. `build_inputs.shacl_play_jar_fingerprint` is a **content** fingerprint
(every entry's decompressed bytes, hashed, sorted by name, concatenated, hashed again), which is
stable because it ignores the timestamps. The same reasoning applies to
`shapechange_runtime_fingerprint`, computed from the compiled classes plus the resolved dependency
classpath, identified by relative path / filename rather than absolute local path so it does not
depend on where the checkout happens to sit.

## Running it

You need JDK 21, Maven, and the three tool checkouts as *siblings* of this repository (`../*`,
never nested inside it) — this matches the layout `pipeline/toolchain-lock.json` and
`scripts/generate_semantic_artifacts.py` assume:

```bash
git clone https://github.com/ASCS-eV/ShapeChange.git   && git -C ShapeChange checkout <locked commit>
git clone https://github.com/ASCS-eV/shacl-play.git    && git -C shacl-play  checkout <locked commit>
git clone https://github.com/ASCS-eV/owl2shacl.git     && git -C owl2shacl   checkout <locked commit>
```

Read the locked commits from `pipeline/toolchain-lock.json`'s `tools.*.commit` fields rather than
switching to the moving `feature/asam-pipeline` branch tip — the branch name is where the fork's
work happens, the lock is what a run is actually validated against.

```bash
# the serialization stack, pinned — see "Why the output is byte-stable" below
pip install -r scripts/requirements.txt

for standard in asam-opendrive asam-openscenario-xml; do
  python scripts/generate_semantic_artifacts.py \
      --standard "$standard" \
      --shapechange ../ShapeChange \
      --shaclplay ../shacl-play \
      --rules ../owl2shacl/owl2sh-closed.ttl
done
```

Both standards run the same two stages with the same encoding rule and the same map entries.
They differ only in what the models make necessary, and each difference is commented in the
configuration that causes it.

ShapeChange is built by the script itself, with `-DskipEa`, so no Enterprise Architect licence
is involved. EA is needed only to re-export a `.scxml` model, and those exports are committed.
SHACL Play is built by the script too, from the `--shaclplay` checkout — never point it at a
pre-built jar.

## What comes out, and how to trust it

`standards/<std>/generated/` holds the two artifacts plus `provenance.json`, which records the
SHA-256 of the source model and the configuration; the ShapeChange commit and its content-based
runtime fingerprint; the SHACL Play commit and its content-based jar fingerprint; the owl2shacl
rules' checksum and commit; the resolved serialization versions; and the JDK/Maven build
environment. That is what makes a difference in the output diagnosable: it tells a reviewer
whether the model changed, the configuration changed, or the toolchain did — and
`scripts/check_toolchain_lock.py` asserts every one of those fields against
`pipeline/toolchain-lock.json` on every CI run.

The ruleset is recorded by commit as well as by checksum, because a checksum alone proves two
runs used the same bytes but not that a third party can obtain them. `"commit": "unknown"` in
that field means the run picked up an unversioned working copy and should be treated as a
reproducibility gap.

### Why the output is byte-stable

ShapeChange and shacl-play both label blank nodes from process-dependent ordering, so
regenerating an unchanged model can produce a large diff that means nothing. Both artifacts are
therefore written in RDFC-1.0 canonical form, via
[`diffable-rdf`](https://github.com/ASCS-eV/diffable-rdf) — canonicalization plus
Weisfeiler-Lehman blank-node hashing, so a changed triple only touches the blank nodes it
actually involves. Only the syntactic form changes. The OWL is canonicalized *before* the SHACL
stage reads it, so stage 2 gets a deterministic input too.

That the canonical form says the same thing as its input is guaranteed by the library rather
than hoped for: `deterministic_turtle` re-parses its own output, requires the result to be
isomorphic to the input, and raises otherwise. The pipeline asserts the triple count as a cheap
additional tripwire.

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

When changing the encoding rule, check the log for warnings before trusting the artifact:

```bash
grep -c 'Unsupported class category' .pipeline-work/owl/opendrive-owl-log.xml
```

`check_shapechange_log()` parses the log on every run and stops the pipeline unless everything in
it is a condition this repository has already explained. What counts as explained is declared
**per standard and per stage**, because the two ShapeChange targets diagnose different things
about the same model and a condition explained for one is not explained for the other.

**OpenDRIVE, OWL stage:**

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

**OpenSCENARIO, OWL stage: nothing is tolerated, and nothing needs to be.** The model carries no
tagged values at all, so the schema package is named once in the configuration and exactly one
schema resolves — the collision behind OpenDRIVE's 227 errors cannot arise. Its 48 `<<union>>`
classes also encode without supertype defects. The log is empty of errors and warnings, and any
that appear will stop the build.

**OpenSCENARIO, XSD stage: one tolerated error**, for `ActivateControllerAction.objectControllerRef` —
see [the parity check](#what-it-checks-and-what-it-found). **OpenDRIVE, XSD stage: nothing**; the
OWL packaging rule does not apply to that target.

Widening any of these means editing `TOLERATED_ERRORS`, or the standard's `tolerated_errors` /
`union_defects` entry, in `scripts/generate_semantic_artifacts.py` *and* saying why — here or in
the model's README — in the same change.

### Coverage of the current encoding

**Every class in both models reaches the ontology.** That is asserted on every run:
`check_model_coverage()` compares the class names in the SCXML against the named
`owl:Class` and `rdfs:Datatype` declarations in the output, allowing only the classes a map
entry deliberately replaces with an RDF datatype.

| | OpenDRIVE | OpenSCENARIO |
|---|---:|---:|
| Classes in the model | 238 | 343 |
| → named `owl:Class` | 178 | 304 |
| → `rdfs:Datatype` with `owl:oneOf` | 55 | 39 |
| → replaced by an RDF datatype via `mapentries-asam.xml` | 5 | 0 |
| **unaccounted for** | **0** | **0** |
| Enumeration literals in the OWL | 290 | 251 |
| `owl:DatatypeProperty` / `owl:ObjectProperty` | 460 / 208 | 420 / 454 |
| `owl:Restriction` nodes | 585 | 1664 |
| SHACL node shapes | 159 | 293 |
| SHACL `sh:minCount` + `sh:maxCount` triples | 908 | 1036 |
| SHACL `sh:in` constraints (properties / permitted values) | 81 / 452 | 80 / 481 |

Reading the numbers:

- **OpenDRIVE's 5 mapped classes** are `t_bool`, `t_grEqZero`, `t_grZero`, `t_zeroOne` and
  `userDataContent`. Their absence from the ontology is correct: `mapentries-asam.xml` turns
  them into `xsd:boolean`, `xsd:double` and `xsd:string`. That also explains the 290 enumeration
  literals against the model's 292 — the two missing are `t_bool`'s `true` and `false`.
  OpenSCENARIO maps none: it refers to XSD primitives by name rather than declaring classes for
  them, so all 343 of its classes are emitted.
- **`sh:in` counts properties, not enumerations.** Each of OpenDRIVE's 81 enumeration-typed
  properties receives the full value list of its enumeration, so the 452 permitted values count
  an enumeration's members once per property that uses it.
- **Cardinality is not double-counted.** An exact cardinality is **one** OWL restriction node
  but **two** SHACL triples, `sh:minCount` and `sh:maxCount` with the same value. Read the SHACL
  figure as a triple count.
- **OpenSCENARIO's 1664 restrictions** are dominated by its 48 `<<union>>` classes. A union of
  *n* options is encoded as a disjunction of *n* alternatives, each asserting
  `owl:qualifiedCardinality 1` on its own property and `owl:cardinality 0` on the other *n-1* —
  the standard "exactly one of these" encoding, and 840 of the restrictions are those zeros.
- **Names are normalised by ShapeChange**, so the model's `e_laneType` appears as
  `odr:E_laneType`. Checking for a model name verbatim will report a false absence.

What is still **not** carried into the SHACL is the numeric facets: `t_grEqZero`'s
`minInclusive=0` and its siblings are mapped to plain `xsd:double`, deliberately, because
`mapentries-asam.xml` maps types and not facets. A consumer needing those bounds must still
read them from the normative XSD in `standards/<std>/schema/`.

## Checking it: the XSD structural parity check

ASAM does not just publish the UML model — it separately publishes a normative XSD
(`standards/<std>/schema/`). That is something the OWL/SHACL stages alone cannot give this
pipeline: an independently produced description of the same standard to check against.
[`scripts/check_xsd_structural_parity.py`](../scripts/check_xsd_structural_parity.py)
regenerates an XSD from the same committed SCXML, using
[`opendrive-xsd.config.xml`](opendrive-xsd.config.xml) — a third ShapeChange target
configuration — and compares its structural inventory against ASAM's official schema, file
by file:

```bash
python scripts/check_xsd_structural_parity.py \
    --standard asam-opendrive \
    --shapechange ../ShapeChange
```

It builds ShapeChange the same way `generate_semantic_artifacts.py` does and needs nothing
else — no owl2shacl, no shacl-play, no fork, since the XSD target rules it uses need no
patch beyond what plain upstream ShapeChange already has. Its output goes to
`.pipeline-work/xsd/`, never to `standards/<std>/generated/`: the XSD it produces is
evidence, not a deliverable, and is not committed.

### What it checks, and what it found

The comparison is a structural inventory — elements, attributes, complexTypes, simpleTypes,
enumeration values and `complexContent` extensions, each counted at any nesting depth — not a
byte diff: the two schemas use different naming and structuring conventions by design (see the
config file for why). The current result, regenerated from the committed model:

| Metric | OpenDRIVE gen. | official | OpenSCENARIO gen. | official | Reading it |
|---|---:|---:|---:|---:|---|
| **Enumeration values** | **292** | **292** | **251** | **251** | Exact match — for OpenDRIVE, file by file across all 7. This is the strongest signal the check produces: the count is asserted directly on every run. |
| **Extensions** (`complexContent`) | **153** | **152** | 1 | 0 | The encoded class hierarchy. For OpenDRIVE it matches ASAM per file — Core 6/6, Junction 24/24, Lane 26/26, Object 23/23, Railroad 8/8, Signal 36/36 — with Road 30/29; the one extra is `e_countryCode`, which extends one of its own alternatives because the model gives that `«XSDunion»` class its alternatives as supertypes, where ASAM declares a `simpleType` union. OpenSCENARIO's model yields one extension (`SpawnedObject` → `Entity`) where ASAM's schema has none; ASAM's four `xs:extension` uses there are `simpleContent`, which is not inheritance. |
| Elements | 1018 | 209 | 1829 | 410 | ASAM's XSD encodes most properties as XML **attributes**, not elements; see the next row. |
| Attributes | 0 | 468 | 0 | 448 | Neither committed UML model has an `xsdEncodingRule=xsdAsAttribute` tagged value on any property (confirmed: zero occurrences), so ShapeChange has no basis to choose attribute encoding for any of them. Closing this needs modelling effort in Enterprise Architect, not a configuration change — see [Not here yet](#not-here-yet). |
| complexTypes | 366 | 166 | 955 | 291 | Follows from the element/attribute difference: content modelled as child elements needs more complexType machinery than the same content modelled as attributes. |
| simpleTypes | 58 | 66 | 39 | 126 | The residual gap after mapping ASAM's stereotype-less base types in `xsdmapentries-asam.xml`; both official schemas additionally factor out inline restrictions as named simpleTypes that the models do not represent as separate UML classes. |

The check fails on two conditions: a file's enumeration-value count not matching exactly, and
the official schema encoding a class hierarchy that the generated schema does not encode at all. Those are the two invariants meaningful to assert automatically today. The
element, attribute, complexType and simpleType differences are reported for visibility but do
not fail the run: they reflect a known, current limitation of the models, not evidence that a
run derived the wrong content. Extension counts are reported rather than asserted exactly, for
the `e_countryCode` reason above — only a collapse to zero is unambiguously a defect.

The extension row is there because the other metrics cannot see inheritance at all. Adding
`rule-xsd-cls-no-base-class` to the XSD encoding rule discards every class's base class, so the
generated schema emits **no** `xs:extension` against ASAM's 152 — while the element, attribute,
complexType, simpleType and enumeration-value counts stay **identical to the numbers above**,
because ShapeChange emits each property exactly once either way. A whole class hierarchy can
therefore disappear without a single one of those counts moving, which is why that rule must not
be added and why this row is asserted, if loosely.

Note that no workflow runs this check: like the generation stages it needs a JDK, Maven and a
ShapeChange build, which is the same dependency argument that keeps those out of this
repository's cheap workflows. The assertion above therefore fires for whoever runs the script,
not on a pull request — run it whenever the XSD encoding rule or a committed model changes.

#### One property ASAM models as a reference to a union

OpenSCENARIO's XSD run reports exactly one error, and it is a finding rather than noise:

> Property `objectControllerRef` of class `ActivateControllerAction` is not a composition, but
> has a data type as its value: `ObjectController`.

ASAM's normative schema declares `objectControllerRef` as `type="String"` — a reference **by
name**. The UML instead models it as a non-composition association to `ObjectController`, which
is stereotyped `<<union>>`. A union has no identity, so there is nothing for a reference to point
at, and the XML Schema target is right to refuse. The generated schema therefore omits this one
property, which is one of the 448 attributes in the difference above.

The same modelling choice is invisible in the OWL, where it is *worse*: `objectControllerRef`
becomes an object property whose range is the union class, asserting that the action **contains**
an ObjectController where the standard says it **names** one. 34 `*Ref` properties across the
model are non-composition associations to a class; this one fails loudly only because its target
is a union. Filed as an ASAM change request; the toleration is scoped to the XSD stage alone, so
the OWL stage's zero-tolerance guarantee is untouched.

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

### `opendrive-xsd.config.xml` — ShapeChange, XML Schema target

- Same `inputModelType=SCXML` input as the OWL config, but one `PackageInfo` per
  sub-package (`Core`, `Junction`, `Lane`, `Object`, `Railroad`, `Road`, `Signal`), each with
  its own `xsdDocument`. This matches ASAM's official 7-file split, rather than the OWL
  target's single merged ontology (`rule-owl-pkg-singleOntologyPerSchema`) — the two targets
  are configured differently on purpose, each to match what it is compared against.
- `rule-xsd-cls-standard-gml-property-types` is the rule that matters most, and the one most
  likely to be dropped by accident when trimming an encoding rule down: it gates the branch in
  ShapeChange's XSD target that renders enumeration, codelist and basictype property
  references at all. Without it, every enumeration- or basictype-valued property fails with
  "No type can be provided for the property", regardless of which enumeration- or
  basictype-specific rules are also present — those are only consulted once this rule has
  let the branch run.
- `rule-xsd-cls-global-enumeration` emits each enumeration as one named, shared `simpleType`.
  The alternative, `rule-xsd-cls-local-enumeration`, renders an anonymous inline `simpleType`
  at every use site instead; it inflates the enumeration-value count through duplication rather
  than changing the content, so it is not used here.
- `rule-xsd-cls-no-base-class` is **deliberately absent**, and the config comment says so in the
  same words, because an encoding rule reads as a list of choices and an absence is easy to
  mistake for an oversight. Adding it discards every base class, removing all 152 of OpenDRIVE's
  `xs:extension` declarations while leaving every other reported count unchanged; see the
  extension row of the table above.

### `xsdmapentries-asam.xml` — type mapping

The XSD-target counterpart of `mapentries-asam.xml`, mapping the same ASAM primitive and
stereotype-less base types to XSD built-ins, for the same reason: `t_grEqZero`, `t_grZero`,
`t_zeroOne` and `t_bool` carry no UML stereotype at all in the committed model, so
ShapeChange's category dispatch cannot recognise them without a map entry and would render
them as empty, content-less `complexType`s instead.

### `openscenario-owl.config.xml` and `openscenario-xsd.config.xml`

Both are the OpenDRIVE configurations with the differences the model forces, and nothing else —
the same encoding rule, the same map entries, the same descriptor targets, so that the two
ontologies differ because the models differ rather than because they were generated differently.
Each difference is commented where it occurs; in summary:

- **The schema package is declared, not read from the model.** OpenSCENARIO carries no tagged
  values at all, so `<PackageInfo>` is what makes `OpenSCENARIO` a schema package
  (`PackageInfoImpl.isSchema` falls back to the namespace configured for a package name). The
  welcome consequence is that exactly one schema resolves, so
  `rule-owl-pkg-singleOntologyPerSchema` is satisfied cleanly.
- **The namespace follows OpenDRIVE's convention, not the XSD.** Neither standard's XSD declares
  a `targetNamespace` — both are unqualified — so `.../openscenario_schema` mirrors the
  `.../opendrive_schema` value the OpenDRIVE model carries in its tagged values.
- **One XSD document, not seven.** ASAM publishes OpenSCENARIO XML as a single schema file, so
  the XSD configuration declares one `PackageInfo` whose `xsdDocument` names the file the
  comparison pairs against.
- **No `sortedSchemaOutput`** in the OWL configuration: it orders classes for the XML Schema
  target and has no effect on the OWL target, which sorts by IRI.

## Adding a standard

Add an entry to `STANDARDS` in the script and a ShapeChange configuration here. No code
changes are required — the script is a path resolver and a runner.

| Key | Required | Meaning |
|---|---|---|
| `model`, `config`, `artifact` | yes | The SCXML model, its OWL configuration, and the base name of the generated files |
| `xsd_config`, `xsd_schema_dir`, `xsd_prefix` | no | Used by `check_xsd_structural_parity.py` only. A standard with no official XSD to compare against, or no XSD target configuration yet, omits them and is left out of that script's `--standard` choices |
| `tolerated_errors` | no | `{"owl": (...), "xsd": (...)}` — names from `TOLERATED_ERRORS` this standard's stages may log. Omitting it, or a stage, requires that stage's log to be free of errors |
| `union_defects` | no | Class names whose supertype structure ShapeChange is known to reject for this model. A class reported outside the set fails the build |

Start with no tolerations. OpenSCENARIO needed none for its OWL stage, and finding that out took
one run — whereas inheriting OpenDRIVE's would have hidden whatever its own model does.

## Not here yet

- **Numeric facets in the SHACL.** `t_grEqZero`'s `minInclusive=0` and its siblings are mapped
  to plain `xsd:double`: `mapentries-asam.xml` maps types, not facets, so the shapes constrain
  those attributes' datatype but not their range. Enumerated value sets are covered: the
  `owl:oneOf` → `sh:in` rule applies, and the counts are in the coverage table above.
- **Reference semantics.** 34 `*Ref` properties in OpenSCENARIO are non-composition
  associations to a class, while ASAM's XSD declares them `type="String"` — references by name.
  The OWL encodes them as containment. This is a modelling question for ASAM, filed as a change
  request; see [the parity check](#one-property-asam-models-as-a-reference-to-a-union).
- **Data-instance validation against both schemas.** [`check_xsd_structural_parity.py`](#checking-it-the-xsd-structural-parity-check)
  checks *structure* — element, attribute and enumeration-value counts — between a regenerated
  XSD and ASAM's official one. What it does not do is take real instance data and confirm the
  *same document* validates against the generated SHACL and against ASAM's XSD. That would be a
  stronger check — it would catch a value that satisfies the SHACL's datatype but violates a
  facet the XSD encodes and the SHACL does not (see the `t_grEqZero`-family gap in
  `xsdmapentries-asam.xml`) — but it needs a corpus of representative instance documents,
  which this pipeline does not have.
- **CI beyond the cheap checks.** [`verify-generated.yml`](../.github/workflows/verify-generated.yml)
  and [`verify-models.yml`](../.github/workflows/verify-models.yml) catch drift cheaply —
  canonical form, recorded serialization versions, and the committed models against their zips
  and published checksums — without needing Maven or a JVM. Neither actually re-runs
  ShapeChange or shacl-play, so a change cannot assert that regenerating the OWL/SHACL from
  scratch reproduces what is committed. `check_xsd_structural_parity.py` has no such blocker —
  it needs a plain ShapeChange checkout and nothing else — so it could run in CI today; the
  OWL/SHACL side still cannot, until the open upstream contributions land and the pipeline no
  longer depends on the `ASCS-eV` forks' `feature/asam-pipeline` branches.
- **The remaining ASAM standards.** OpenDRIVE and OpenSCENARIO XML both run end to end.
  `standards/` holds directories for OpenCRG, OpenLABEL, OpenMATERIAL 3D, OpenODD,
  OpenSCENARIO DSL, OSI, traffic participants and ISO 345xx; none of those has a committed UML
  model yet, which is the prerequisite for a configuration.
