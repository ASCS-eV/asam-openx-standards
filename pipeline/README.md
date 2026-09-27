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

Three scripts produce no artifact at all:

- [`scripts/check_model_equivalence.py`](../scripts/check_model_equivalence.py) proves the SCXML
  is ASAM's EA project;
- [`scripts/check_xsd_transformation.py`](../scripts/check_xsd_transformation.py) derives the
  normative XSD from the model;
- [`scripts/check_xsd_structural_parity.py`](../scripts/check_xsd_structural_parity.py) checks
  what ShapeChange generates from the model against the published XSD.

See the "Checking it" sections below.

## The rule that shapes everything here

**Nothing is post-processed.** Both stages are off-the-shelf tools driven by the
configuration in this directory; the script only resolves paths and runs them in order. If a
generated artifact is wrong, exactly one of three things is wrong — the **model**, the
**configuration**, or the **tool** — and the fix belongs there.

Every fix the pipeline depends on was written as a self-contained upstream contribution rather
than a local patch, so a tool is only forked for as long as its contributions are unmerged. SHACL
Play! is plain upstream; owl2shacl and ShapeChange carry contributions that are still open
upstream, as commits on the `feature/asam-pipeline` branch of their `ASCS-eV` forks:

- **owl2shacl** — ⏳ carries an enumeration written as an OWL 2 datatype definition mapped to
  `sh:in` ([#10]). Upstream already has the `owl:onDataRange` cardinality rules as the
  data-property counterpart of `owl:onClass` ([#7]), datatype ranges decided structurally and
  `owl:oneOf` mapped to `sh:in` ([#8]), and `owl:unionOf` of class expressions translated to
  `sh:or` ([#9]).
- **SHACL Play!** — ✅ **upstream.** Conversion rules supplied explicitly via `--rules` ([#344]),
  failing on an input that cannot be read instead of producing an empty result ([#345]),
  `sh:ignoredProperties` gathered into an RDF list so closed shapes are honoured outside the web
  UI ([#346]), and every *other* list-valued constraint gathered too, so the `sh:or` above is a
  well-formed SHACL list rather than repeated bare values ([#347]).
- **ShapeChange** — ⏳ carries three contributions:
  - the Flattener keeping a union excluded by `flattenUnionTypesExcludeRegex` ([#798]);
  - junit 3.8.1 kept off the test classpath, so the fork's tests run under `mvn test` ([#799]);
  - the target parameter `iso191502EnumerationAsDatatypeDefinition`, which encodes an
    enumeration as an OWL 2 datatype definition ([#800]).

  Upstream already has `ModelExport` honouring the `sortedOutput` parameter ([#764]) and the OWL
  target declaring a data property when a property's value type is an enumeration ([#766]). A
  `«union»`'s alternatives being its association ends ([#768]) was declined: the defect it
  addressed belongs in ASAM's model (request 10 in
  [`asam-change-requests.md`](asam-change-requests.md)).

[#7]: https://github.com/sparna-git/owl2shacl/pull/7
[#8]: https://github.com/sparna-git/owl2shacl/pull/8
[#9]: https://github.com/sparna-git/owl2shacl/pull/9
[#10]: https://github.com/sparna-git/owl2shacl/pull/10
[#344]: https://github.com/sparna-git/shacl-play/pull/344
[#345]: https://github.com/sparna-git/shacl-play/pull/345
[#346]: https://github.com/sparna-git/shacl-play/pull/346
[#347]: https://github.com/sparna-git/shacl-play/pull/347
[#764]: https://github.com/ShapeChange/ShapeChange/pull/764
[#766]: https://github.com/ShapeChange/ShapeChange/pull/766
[#768]: https://github.com/ShapeChange/ShapeChange/pull/768
[#798]: https://github.com/ShapeChange/ShapeChange/pull/798
[#799]: https://github.com/ShapeChange/ShapeChange/pull/799
[#800]: https://github.com/ShapeChange/ShapeChange/pull/800

A tool that carries nothing is still pinned to an exact commit — being upstream is not the same as
being unpinned, and the `ASCS-eV` forks remain the checkouts the pipeline reads, whether they carry
commits or sit at plain upstream. [`pipeline/toolchain-lock.json`](toolchain-lock.json) records that exact commit for
each tool and, for anything still carried, the upstream contribution it implements. Moving a tool to
a released upstream commit is a lock update, described under
[The toolchain lock](#the-toolchain-lock) — never a silent branch drift.

## The toolchain lock

[`pipeline/toolchain-lock.json`](toolchain-lock.json) pins every input that determines the output
bytes: for each fork, its exact commit, the upstream development branch and base commit it was
rebased on, and the ordered list of commits it carries on top (each mapped to the upstream PR it
implements); the exact Python serialization versions from
[`scripts/requirements.txt`](../scripts/requirements.txt); and the exact JDK/Maven build
environment plus content-based fingerprints of the built ShapeChange runtime and the built SHACL
Play jar.

`carried_commits` and the `commit`/`upstream_base` pair state the same thing twice, and both
checks below hold them to agreeing: the carried list is exactly the path from the base to the
locked commit. An **empty** carried list is therefore not a defect but the goal — it says upstream
has merged everything this fork was carrying, so the fork is pinned at plain upstream and `commit`
equals `upstream_base`. Every carried commit is working towards being deleted from this file.

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

**For first-time machine setup — exact JDK and Maven versions, portable install, the
tool checkouts, and the failure modes that cost the most time — see
[`pipeline/SETUP.md`](SETUP.md).** This section assumes that is already done.

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
`targetNamespace` tagged value on any package, so the schema package is named once in the
configuration and exactly one
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
| → `rdfs:Datatype` defined as an enumeration of literals | 55 | 39 |
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

## Checking it: equivalence with ASAM's EA project

Everything above starts from `standards/<std>/uml/<std>.scxml`. That file comes from ASAM's
Enterprise Architect project, `standards/<std>/uml/source/*.qeax`, through the one step that
needs an EA licence, and the XSD parity check below compares what the pipeline *generates*,
not what it *reads*. [`scripts/check_model_equivalence.py`](../scripts/check_model_equivalence.py)
closes that gap. It decides, fact by fact, whether each committed SCXML is the model in the EA
project, and names every way it is not. The only exceptions are the normalizations and the
out-of-scope content it declares.

It needs neither EA nor ShapeChange. A `.qeax` is an SQLite database, so both sides are read
with the Python standard library:

- **The EA side is read with UML semantics, not ShapeChange's.** Where EA records a fact in
  two places, both are read. For example, a connector's stereotype is in
  `t_connector.Stereotype` *or* in `t_xref`, and ShapeChange consults only `t_xref`. A
  classifier owned by another classifier is part of the model, although ShapeChange never
  visits it. Reading the model the exporter's way would only prove that the exporter agrees
  with itself.
- **The SCXML side is read the way ShapeChange's own SCXML reader reads it, and totally**,
  but not through that reader, which re-normalizes stereotypes and tags on the way in:
  - a table of what each SCXML element may contain decides that every element and attribute
    of the file is either compared or reported;
  - a repeated single-valued child is reported, and the last one wins, as in ShapeChange;
  - a list item under a non-canonical tag is reported, and still read as an item;
  - an association end ShapeChange's reader would drop from its class is reported.

Elements are joined by identifier, which ShapeChange carries over from EA:

| Element | SCXML id | From EA |
|---|---|---|
| package | `P<n>` | `t_package.Package_ID` |
| classifier | `<n>` | `t_object.Object_ID` |
| attribute | `<class>_<n>` | `t_attribute.ID` |
| association | `as<n>` | `t_connector.Connector_ID` |
| association end | `S…` / `T…` | the source or target end of that connector |

A difference is `MISSING` (the model states it, the SCXML does not carry it), `EXTRA` (the
SCXML states something the model does not) or `DIFFERENT` (both state it, with contradicting
values). Each difference also names the rule that found it.

Three kinds of difference are declared rather than reported. The module docstring of
[`scripts/model_equivalence.py`](../scripts/model_equivalence.py) is the complete list, with the
ShapeChange source line behind each entry. The main ones:

- **Values ShapeChange derives** where the model is blank. The check computes the value the
  export must then hold and reports anything else:
  - association names `<source>_<target>`;
  - role names `role_S…` / `role_T…`;
  - the `enumeration` stereotype on EA enumerations;
  - composition on attributes;
  - navigability of an end EA leaves `Unspecified`;
  - `definition` as the trimmed documentation.
- **Notation that carries no information:**
  - UML's default multiplicity 1;
  - EA's plain-text rendering of rich-text notes. Hyperlink targets, which that rendering
    drops, *are* reported;
  - the case of ShapeChange's well-known stereotypes;
  - a tagged value declared with no value. These are still counted per tag, so a statement
    such as "declared 106 times, never given a value" is measured, not asserted.
- **What is not UML model content:** diagrams and their `Boundary`/`Text`/`Note` elements,
  `NoteLink` connectors, EA's documents and profile definitions, and EA's bookkeeping
  columns. Every such table is counted and printed as out of scope, and every such column is
  named in the module docstring. The counts are reported rather than gated, because the
  `.qeax` bytes are already pinned by the checksum `verify-models.yml` enforces.

### What it found

| Verdict | Rule | OpenDRIVE | OpenSCENARIO |
|---|---|---:|---:|
| `DIFFERENT` | `end-navigability` | 1 | 1 |
| `MISSING` | `association` | 8 | – |
| `MISSING` | `association-stereotype` | – | 3 |
| `MISSING` | `association-tag` | – | 127 |
| `MISSING` | `attribute-documentation-link` | 1 | 2 |
| `MISSING` | `attribute-tag` | 121 | 125 |
| `MISSING` | `attribute-unrepresentable` | 18 | – |
| `MISSING` | `attribute-visibility` | 29 | 420 |
| `MISSING` | `classifier-kind` | – | 5 |
| `MISSING` | `classifier-tag` | 34 | 44 |
| `MISSING` | `constraint` | 25 | – |
| `MISSING` | `element-type` | – | 11 |
| `MISSING` | `generalization-by-name` | 25 | – |
| `MISSING` | `generalization-stereotype` | 2 | – |
| `MISSING` | `nested-classifier` | 1 | – |
| `MISSING` | `package-documentation-link` | – | 1 |
| `MISSING` | `package-tag` | 22 | – |
| `MISSING` | `realization` | – | 25 |
| | **total** | **287** | **764** |

Every package, classifier name, attribute type, multiplicity, initial value, documentation
text, role tag and attribute order that the SCXML *does* carry matches the EA project. What
differs is information the export does not carry:

- **A classifier owned by a classifier is not exported.** OpenDRIVE's root content model
  belongs to `t_OpenDRIVE` (`t_object` 11), owned by the class `OpenDRIVE`. ShapeChange's EA
  reader loads only the elements of a package, so the classifier and its 8 associations to
  `header`, `road`, `controller`, `junction`, `junctionGroup`, `station`, `g_additionalData` and
  `vmsGroup` are absent.
- **A connector stereotype held only in `t_connector.Stereotype` is not exported.**
  OpenSCENARIO marks three associations `«transient»` ("not mapped to the schema") there:
  `CatalogReference.ref` and the two `phaseRef`. EA's `Connector.StereotypeEx`, which
  ShapeChange reads, does not return them. `CatalogReference.ref` is consequently required by
  the SHACL, which then rejects every conforming document containing a `<CatalogReference>`.
- **The SCXML has no place for:** realizations (OpenSCENARIO 25, all to its `«transient»`
  interfaces), generalization stereotypes (OpenDRIVE 2 `XSDextension`), classifier kind
  (`Interface`), visibility, the `isID` custom property (OpenDRIVE 18), and elements other than
  classes, interfaces, data types and enumerations (OpenSCENARIO 7 `PrimitiveType`,
  2 `Object`, 2 `Association` elements).
- **Generalizations EA records by name are not read.** `t_object.GenLinks` holds
  `Parent=<name>;` for 22 OpenDRIVE classifiers:
  - the union members the export has no other trace of: all four of `e_unit`,
    `e_maxSpeedString` of `t_maxSpeed`, and `e_countryCode_deprecated` of `e_countryCode`;
  - the restriction bases of the XSD simple types.
- **Constraints are not loaded:** `checkingConstraints=disabled` drops OpenDRIVE's
  24 invariants and 1 attribute constraint.
- **Valued tags outside `representTaggedValues` are dropped.** Examples: OpenDRIVE's XSD
  identity constraints `key`/`keyref`/`refer`/`selector`, and OpenSCENARIO's
  `xsdElementName`/`xsdType`/`anonymousRole`. The export configuration's own comment lists
  only the tags that are declared without a value.
- **Navigability EA states is contradicted in 2 ends:**
  - OpenDRIVE `t_road_link → g_additionalData` is navigable but unnamed, and ShapeChange never
    makes an unnamed end navigable.
  - OpenSCENARIO `ControllerAction → ActivateControllerAction` is explicitly non-navigable on a
    connector whose direction is `Unspecified`.

#### Gating, and why by baseline

Each standard records its accepted differences in
`pipeline/<artifact>-model-equivalence-baseline.json`, grouped by verdict:

- A difference outside the baseline fails the run.
- With `--strict-baseline`, as CI runs it, so does a baseline entry that no longer occurs.

The baseline is a list of known export defects, keyed by rule, not a tolerance. The target
for every rule is zero. Reaching it for the losses above means an export-configuration change
or a ShapeChange contribution, followed by one EA re-export.

#### Testing the oracle

[`scripts/test_model_equivalence.py`](../scripts/test_model_equivalence.py) builds a minimal EA
project (an SQLite database with EA's column names) and the SCXML ShapeChange writes for it.

- **Faithful pairs must produce zero findings.** There is the base pair, plus one faithful
  pair for each value ShapeChange derives rather than copies. These keep the declared derived
  values honest.
- **Every other case changes one model fact and states the complete list of findings it
  produces.** Where the case needs it, the case also changes the export's rendering of that
  fact. A case passes only on exactly that list.
- **Every rule has at least one such case.** `RULES` in `model_equivalence.py` lists them, and
  the run fails if one has none. Among the cases are all the losses the committed exports
  have.
- **The reader's totality is tested too.** The following are findings:
  - a repeated id or child element;
  - a list item under a non-canonical tag;
  - a role property no association end uses;
  - an end ShapeChange's reader would drop from its class;
  - an end whose id, association or owner is not the one its connector implies;
  - a descriptor or element the check does not compare;
  - a value that is not an `xs:boolean`;
  - a missing `sequenceNumber`.
- **The guards are tested too:**
  - an export with no classes, and two models that share no id, raise `VacuousComparison`;
  - a Git LFS pointer in place of the `.qeax` is rejected with the fix named.

Both steps run in the `model-equivalence` job of
[`verify-models.yml`](../.github/workflows/verify-models.yml), which checks out Git LFS.

## Checking it: the normative XSD, derived from the model

The equivalence check above proves that the SCXML is ASAM's model. It does not say that the
model is a model *of the normative schema*. ASAM states that it is: "The XSD schemas are derived
from the UML model" (OpenDRIVE V1.9.0, clause 1). [`scripts/check_xsd_transformation.py`](../scripts/check_xsd_transformation.py)
tests that claim. It derives each XSD from ASAM's EA project, and again from the committed
SCXML, and compares both results with the published schema in `standards/<std>/schema/`.

```bash
python scripts/check_xsd_transformation.py --strict-baseline
```

Like the equivalence check, it needs neither EA nor ShapeChange.
[`scripts/ea_api.py`](../scripts/ea_api.py) offers the part of EA's object model that a schema
generator walks: `Package.Elements`, `Element.Attributes`, `Element.Connectors`,
`TaggedValues`, `Stereotype` and `StereotypeEx`. It does so over the `.qeax`, in the order EA's
own API returns each collection, and over the SCXML, stating what it assumes where the export
has no counterpart. `Name` compares as EA's schema declares the column, `COLLATE NOCASE`, so
`Controller` sorts before `ControlPoint`.

### OpenSCENARIO: ASAM's own generator, byte for byte

The OpenSCENARIO project contains the JScript ASAM generates its schema with, in `t_script`,
named "OSC 2 XSD Transformation". It is extracted byte for byte to
[`standards/asam-openscenario-xml/uml/source/osc-2-xsd-transformation.js`](../standards/asam-openscenario-xml/uml/source/osc-2-xsd-transformation.js),
and the check fails unless that file is still the project's script.
[`scripts/osc_xsd_transformation.py`](../scripts/osc_xsd_transformation.py) ports it function by
function, including the behaviour the V1.4.0 model never reaches. Run on the EA project, the
port writes a file **byte-identical to `OpenSCENARIO.xsd`**, and the check asserts that on every
run. The published schema is therefore exactly what ASAM's model and ASAM's generator produce,
with no manual step between them.

Run on the SCXML, the same port shows what the export is missing: 127 differences, every one of
them an export loss.

| From the SCXML | Count | Cause |
|---|---:|---|
| a name reference without its `xsdType` | 32 | connector tag outside `representTaggedValues` |
| a complex type that differs | 81 | the connector tags `xsdElementName` and `xsdType`, and the three `«transient»` connectors whose stereotype is only in `t_connector.Stereotype` |
| a component not generated | 13 | the 5 wrapper types and the root element name are class tags outside `representTaggedValues`; the 7 `Boolean`…`UnsignedShort` unions come from EA `PrimitiveType` elements, which the export skips |
| a component generated in excess | 1 | the root element, unnamed without its `elementName` tag |

### OpenDRIVE: EA's XML Schema profile

The OpenDRIVE project contains no generator. It applies Enterprise Architect's *UML profile for
XML Schema*:

- classes stereotyped `XSDschema`, `XSDcomplexType`, `XSDsimpleType`, `XSDunion`, `XSDgroup`,
  `XSDchoice`, `XSDany` and `XSDtopLevelElement`;
- attributes stereotyped `XSDattribute`;
- the profile's tagged values;
- ASAM's own tagged values for what XSD 1.1 adds: identity constraints (`key`, `keyref`,
  `refer`, `selector`, `targetElement`) and type alternatives (`XSDAlternative_*`), with the
  assertions as EA invariants.

[`scripts/odr_xsd_transformation.py`](../scripts/odr_xsd_transformation.py) derives the seven
documents from those constructs. It has one rule per construct and names no class; its module
docstring states each rule. [`scripts/xsd_equivalence.py`](../scripts/xsd_equivalence.py)
compares the result with the published files, component by component, and distinguishes:

- `component`: the declared content differs;
- `particle-order`: a sequence has the same particles in another order;
- `alternative-order`: an element has the same type alternatives in another order;
- `documentation`: the text differs;
- `schema`: an attribute of `xs:schema` differs.

It does not compare what XML Schema gives no meaning: attribute order, the order of choice
alternatives and of facets, comments, and the lexical form of the file.

From the EA project, **every other declaration matches**: every type, element, attribute, use,
default, fixed value, facet, union, list, group, wildcard, key, keyref, assertion and type
alternative. So does all the documentation, in 724 `xs:documentation` elements. 50 differences
remain:

| Rule | Count | What the normative schema has that the model does not say |
|---|---:|---|
| `particle-order` | 33 | The element order of 33 sequences. The model records order only in 20 sparse `position` tags, some of which contradict the schema: in `t_road_signals_staticBoard`, `sign` is `position` 5 and `g_additionalData` 6, and the schema puts `g_additionalData` first. |
| `component` | 2 | Content the schema comments out "to comply with the sequence order of earlier OpenDRIVE versions": `_OpenDriveElement`'s `g_additionalData`, and `t_junction`'s `priority`, `controller`, `surface` and `g_additionalData`. Every subtype declares these itself, so the UML model has each of them twice. |
| `alternative-order` | 1 | The order of `junction`'s type alternatives. The model numbers them `crossing` 1, `direct` 2, `virtual` 3, `common` 4, and the schema lists `virtual`, `direct`, `crossing`, `common`. The tests are mutually exclusive, so the language is the same. |
| `schema` | 14 | Each package's `targetNamespace` tag, which no published document declares, and `vc:minVersion="1.1"`, which the XSD 1.1 constructs need and the model does not state. |

The derivation also exposes three places where model and schema agree, and **both are
wrong**:

- **The model contradicts itself on attribute use.** An `XSDattribute`'s `use` is its tag, and
  `optional` when the tag is unset. Its UML multiplicity is not read, and it disagrees with the
  schema for 80 attributes: 76 are `1..1` but optional, and 4 are `0..1` but required. Anything
  that reads the model as UML, as the OWL target does, sees the opposite.
- **Four classes can never be valid.** `t_header_defaultRegulations`,
  `t_header_roadRegulation`, `t_header_signalRegulation` and `t_signalGroup_vmsGroup` each
  have an unnamed `1..1` association to the abstract `_OpenDriveElement`. So each requires a
  child `<_OpenDriveElement>`, which no document can supply without `xsi:type`.
- **8 attributes are `xs:string` in the schema.** Their type names a class, such as
  `t_grEqZero`, but the attribute's classifier reference in EA is missing, so nothing resolves
  it.

From the SCXML, 127 differences show what the export is missing:

- the `schemaLocation`, `elementFormDefault`, facet, `derivation`, identity-constraint and
  `XSDAlternative_*` tags;
- the invariants;
- the `GenLinks` restriction bases and union members;
- the nested root class `t_OpenDRIVE`.

#### Gating, and why by baseline

`pipeline/<artifact>-xsd-transformation-baseline.json` records the accepted differences, per
source. A difference outside it fails the run; with `--strict-baseline` so does an entry that no
longer occurs.

- For the EA project, the baseline lists every difference between ASAM's model and ASAM's
  schema. OpenSCENARIO's is empty, and the check also demands byte identity.
- For the SCXML, the baseline lists what the export loses of what the schema depends on. Its
  target is the EA project's own list.

#### Testing the oracle

[`scripts/test_xsd_transformation.py`](../scripts/test_xsd_transformation.py) builds small models
in memory and tests each rule of both derivations. That covers every behaviour of ASAM's script
that the real model never reaches, including the ones the code does not seem to intend: a
finite upper bound other than 1 writes `maxOccurs` with the lower bound's value, and `*` on a
compositor becomes `unbound`.

It tests the comparison in both directions: a difference that carries meaning is reported,
under the right rule, and one that does not is not. It also loads a small `.qeax` and a small
SCXML through both of `ea_api.py`'s loaders, to test EA's collection order, the
`Stereotype`/`StereotypeEx` split, and the facade's stated assumptions.

Both steps run in the `xsd-transformation` job of
[`verify-models.yml`](../.github/workflows/verify-models.yml).

## Checking it: the SHACL against the model's schema

[`scripts/check_shacl_equivalence.py`](../scripts/check_shacl_equivalence.py) compares the
generated SHACL with what the model means in schema terms. It uses the derivation above, which
records the UML property each declaration stands for. For each class it computes what a
node may carry:

- each property, with its least and greatest number of values and its value type;
- each choice, a set of alternatives that exclude each other.

Inheritance, group references, nested compositors and XML list wrappers are resolved on the way.
It then reads the same from the node shapes: `sh:property`, `sh:closed` with
`sh:ignoredProperties`, and the `sh:or` the OWL union encoding produces.
[`scripts/shacl_equivalence.py`](../scripts/shacl_equivalence.py) states the reading of both
sides; `pipeline/<artifact>-shacl-equivalence-baseline.json` records the accepted findings.

Against the committed release shapes it finds 1,032 differences for OpenDRIVE and 187 for
OpenSCENARIO:

- OpenDRIVE's closed shapes reject the additional data every element may carry, because the
  model's links to `g_additionalData` are unnamed, so no UML reader sees them;
- choices are encoded as conjunctions;
- attribute use disagrees with multiplicity;
- simple-type unions and lists are classes;
- OpenSCENARIO's unions fold properties outside the choice into it.

The candidate models below address these. An experimental run of the pipeline on the OpenDRIVE
candidate, with the flattening and union-set rules it is written for, leaves 24.

## Candidate models

A change to the modelling is published as a candidate for a future version, never in the release
model (AGENTS.md, rule 7): `standards/<std>/candidates/<version>/`. `changes.json` lists the
changes, each with its reason, its effect on the normative schema and its operations.
[`scripts/candidate_model.py`](../scripts/candidate_model.py) applies them to the release SCXML,
writing it as ShapeChange writes a model, and renders `CHANGELOG.md`; CI checks both are up to
date. The same operations applied to a copy of ASAM's EA project let a candidate be checked like
the release:

| | OpenDRIVE 1.10 candidate | OpenSCENARIO XML 1.5 candidate |
|---|---|---|
| Changes | 10 (425 operations) | 4 (84 operations) |
| Project copy vs candidate SCXML (`model_equivalence`) | no difference the release lacks | no difference the release lacks |
| Schema derived from the candidate | the schema-invariant changes alone derive all 7 normative documents with **zero** differences; the two corrections change exactly 8 types | ASAM's generator writes `OpenSCENARIO.xsd` **byte for byte** |

The corrections are:

- ODR-8: 4 types required a child of the abstract `_OpenDriveElement`, so no valid file could
  contain them;
- ODR-9: 8 attributes were `xs:string` because their classifier link was broken.

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

### It runs in CI, and the number is the point

This check is the answer to *"how far is the open pipeline from reproducing the normative
artifacts?"*, so it runs on every pull request that can move it, on every push to `main`, and
weekly — because the gap can also move without this repository changing, if ASAM re-releases a
schema. See [`measure-gap.yml`](../.github/workflows/measure-gap.yml).

Each run writes a table to the job summary, per standard:

| Verdict | Meaning |
|---|---|
| `CONTRADICTS` | the generated schema **rejects documents the normative schema accepts** — unsound |
| `EXTRA` | the generated schema accepts documents the normative schema rejects — unsound |
| `MISSING` | present in the normative schema, absent from ours — incomplete |
| `TYPE_MISMATCH` | same particle, different type — incomplete |

`CONTRADICTS` and `EXTRA` are the ones that make generated artifacts *wrong* rather than merely
partial, and the release plan gates on `CONTRADICTS` reaching zero.

CI runs with `--strict-baseline`, which differs from a local run in one way: a baseline finding
that no longer occurs **fails** the build instead of merely being reported. That sounds perverse
— it makes an improvement fail — but a baseline nobody tightens stops describing the gap that
exists, and then the recorded figure is fiction. Failing forces the improvement and the
re-recorded baseline into the same change:

```bash
python scripts/check_xsd_structural_parity.py \
    --standard asam-opendrive --shapechange ../ShapeChange \
    --write-content-baseline
```

The workflow needs a JDK, Maven and a ShapeChange build, which is the dependency argument that
keeps the *generation* stages out of CI. That argument does not apply here: regenerating
artifacts must be byte-reproducible and therefore needs the exact locked JDK, whereas a
structural comparison of two schemas does not, so a stock Temurin 21 is enough. The ShapeChange
fork and commit are read out of `toolchain-lock.json` rather than hardcoded, so the workflow
cannot drift from what actually generates the artifacts.

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

This assertion, like the rest of the check, now runs on every pull request that can move it —
see [It runs in CI, and the number is the point](#it-runs-in-ci-and-the-number-is-the-point)
above. Run it locally too whenever the XSD encoding rule or a committed model changes, so the
result is known before the push.

### The content-model level

The counts above are blind to two things a schema says: which compositor groups a set of
particles, and how many times each may occur. So they can all match, or differ only by the
documented attribute-encoding style, while the generated schema accepts a **different
language** than the official one. `scripts/xsd_content_model.py` adds the comparison that
sees it, per `complexType`, with `xs:extension` bases and `xs:group` references resolved
first:

| Verdict | Meaning | OpenDRIVE | OpenSCENARIO |
|---|---|---:|---:|
| `MISSING` | the official schema declares a particle the model cannot express | **465** | 48 |
| `EXTRA` | the generated schema invents a particle | **5** | 24 |
| `CONTRADICTS` | the generated schema *demands* what the official schema makes optional, makes mandatory what it offers as one alternative of a choice, or *permits fewer occurrences* than it allows — **a conforming document is rejected** | **91** | 20 |
| `TYPE_MISMATCH` | same particle, different declared type | 8 | 32 |

`CONTRADICTS` is the only verdict that is unsound rather than incomplete, and it is not
zero: OpenDRIVE's `t_road_planView_geometry` requires all five geometry primitives at once
where ASAM declares an `xs:choice`, so the generated schema — and the SHACL derived from
the same model — reject every conforming `.xodr`. That was invisible to the counts, which
see five element declarations on both sides.

Three normalizations keep this from reporting the encoding style as a defect. Each is
derived from a published artifact, never written out by hand:

- **element vs attribute** — compared as one particle set, because ASAM's schema favours
  XML attributes and the model carries no `xsdEncodingRule` tagged value selecting them.
  An attribute's `use="required"` reads as `minOccurs="1"`.
- **type substitutions** — the XSD target's own `XsdMapEntry` entries are applied to the
  official side, plus the official schema's own `xs:simpleType` unions, so
  OpenSCENARIO's `Double` (a union of `expression parameter xs:double`, the parameter
  mechanism) pairs with the model's `double`. Without the latter, 366 of OpenSCENARIO's
  findings were that one difference.
- **particle names** — ASAM names an XML element, ShapeChange names the UML role. In
  OpenDRIVE they coincide; in OpenSCENARIO the element is UpperCamelCase and singular
  (`<ManeuverGroup>`) while the role is lowerCamelCase and plural (`maneuverGroups`).
  Pairing is conservative — a candidate must be unique, and anything unpaired stays
  reported — because a wrong pairing hides a real difference. Without it one particle was
  reported as both `MISSING` and `EXTRA`, 400 times over.

#### Gating, and why by baseline

Each standard has a committed baseline of accepted findings
(`pipeline/<artifact>-xsd-content-baseline.json`). A finding outside it fails the run; a
baseline entry that no longer occurs is reported so the baseline is tightened in the same
change that resolved it (`--write-content-baseline`).

Absolute zero is the target for `CONTRADICTS` and `EXTRA`, not the current state, so a
baseline is the only gate that can be enforced today. It is also the only gate that reads
correctly when a fix lands: content the model currently cannot express will, once it can,
*raise* the generated element count further above ASAM's total — because ASAM's total is
low for the unrelated attribute-encoding reason. A count-based check would read that
improvement as a regression.

#### Testing the oracle

`scripts/test_xsd_content_model.py` runs on every pull request — stdlib only, no JDK. Every
case in it exists because an earlier version of the comparison produced a confident wrong
answer: stripping ShapeChange's `Type` suffix from official names that genuinely end in
`Type` (`e_roadType`) invented 141 mismatches; pairing against the empty `PropertyType`
wrapper instead of the content type reported all 1222 particles as `MISSING`; defaulting an
attribute's `minOccurs` to 1 invented 174 contradictions; and one wiring loaded no schemas
at all, reported zero findings for all four verdicts, wrote an empty baseline and printed
PASS. A `VacuousComparison` error now makes that last one impossible.

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
- The `asam-owl` encoding rule selects the OWL constructs the ASAM models actually use; the two
  rules that fail quietly when wrong are named below.
- `{SHAPECHANGE_RESOURCES}`, `{PIPELINE}` and `{OUT}` are substituted by the script. Only the
  first depends on where the tool lives; the model and output paths are repository-relative so
  the configuration reads the same for everyone.

Two rules deserve naming, because getting them wrong fails quietly:

- `rule-owl-prop-multiplicityAsQualifiedCardinalityRestriction` turns a UML multiplicity
  into a cardinality restriction. It needs a ShapeChange that emits `owl:onDataRange`, not
  `owl:onClass`, when the restricted value type is a datatype.
- `rule-owl-cls-iso191502Enumeration` encodes each enumeration as an `rdfs:Datatype` whose
  value space is its literals. With `iso191502EnumerationAsDatatypeDefinition` ([#800]) it writes
  that as the OWL 2 datatype definition `DatatypeDefinition( DT DataOneOf( ... ) )` (OWL 2
  Structural Specification, Sec. 9.4): the named datatype is `owl:equivalentClass` to an
  anonymous `rdfs:Datatype` carrying the `owl:oneOf` list (Mapping to RDF Graphs, Sec. 2.1,
  Table 1). OWL 2 DL requires such a definition for every datatype that is neither
  `rdfs:Literal` nor in the OWL 2 datatype map (Sec. 11.2). Without the parameter, `owl:oneOf`
  sits on the named datatype, and the OWL API's OWL 2 DL profile check reads each enumeration
  as an empty enumeration of individuals: 55 and 39 `EmptyOneOfAxiom` violations, 0 with it.
  The alternative, `rule-owl-cls-enumerationAsCodelist`, is
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

The XSD-target counterpart of `mapentries-asam.xml`, and it splits the ASAM base types the same
way, for two different reasons.

`t_grEqZero`, `t_grZero` and `t_zeroOne` carry no stereotype that ShapeChange's category
dispatch recognises, so it cannot classify them without a map entry and would render them as
empty, content-less `complexType`s instead. Since the re-export set `addStereotypes="*"` they do
carry `XSDsimpleType` from ASAM's EA XML Schema profile, but `establishCategory()` has no branch
for it, so the map entries remain necessary.

`t_bool` is a different case: it **is** categorised, as an `enumeration` over `true` and
`false`. Its map entry is a deliberate choice to collapse that two-literal enumeration into
`xs:boolean`, not a workaround for a missing category.

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

Several of the gaps below are not ours to close: they are properties of ASAM's models rather
than of this pipeline. Those are collected, with reproducible evidence, in
[`asam-change-requests.md`](asam-change-requests.md) — the authoritative list of what we intend
to raise with ASAM, and of two requests already withdrawn after they turned out to be our own
bugs.

- **Numeric facets in the SHACL.** `t_grEqZero`'s `minInclusive=0` and its siblings are mapped
  to plain `xsd:double`: `mapentries-asam.xml` maps types, not facets, so the shapes constrain
  those attributes' datatype but not their range. Enumerated value sets are covered: the
  `owl:oneOf` → `sh:in` rule applies, also to an enumeration written as a datatype definition
  ([#10]), and the counts are in the coverage table above.
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
  scratch reproduces what is committed. `check_xsd_structural_parity.py` had no such blocker —
  it needs a plain ShapeChange checkout and nothing else — and now runs in CI via
  [`measure-gap.yml`](../.github/workflows/measure-gap.yml), so the gap to the normative
  schemas is measured on every change. What remains missing here is the OWL/SHACL half.

  For the OWL/SHACL side access is no longer the blocker. Every tool is pinned to a public commit
  that a workflow can clone, as `measure-gap.yml` already does for ShapeChange: SHACL Play! at
  plain upstream, owl2shacl and ShapeChange at their `ASCS-eV` feature branches. What is left is
  CI cost — a JDK, Maven and two tool builds — and, for running from upstream sources only, the
  open contributions [#10], [#798], [#799] and [#800].
- **The remaining ASAM standards.** OpenDRIVE and OpenSCENARIO XML both run end to end.
  `standards/` holds directories for OpenCRG, OpenLABEL, OpenMATERIAL 3D, OpenODD,
  OpenSCENARIO DSL, OSI, traffic participants and ISO 345xx; none of those has a committed UML
  model yet, which is the prerequisite for a configuration.
