#!/usr/bin/env python3
"""
Derive OWL and SHACL from the committed ASAM UML models.

Turns the tool-neutral UML in ``standards/<standard>/uml/`` into machine-readable
artifacts, without Enterprise Architect and without hand editing::

    ASAM UML  ──ShapeChange──▶  OWL 2 ontology  ──owl2shacl rules──▶  SHACL shapes
    (SCXML)                     (.owl.ttl)                            (.shacl.ttl)

Both stages are off-the-shelf tools driven by committed configuration; this script only
resolves paths, runs them in order and records what produced what. Neither stage's output is
edited: if an artifact is wrong, the fix belongs in the model, the configuration or the tool.
The one transformation applied is a deterministic re-serialization of the RDF (RDFC-1.0
canonical form), which preserves every triple and exists so that regenerating an unchanged
model produces byte-identical files.

Usage
-----
::

    python scripts/generate_semantic_artifacts.py \\
        --standard asam-opendrive \\
        --shapechange ../ShapeChange \\
        --shaclplay ../shacl-play/shacl-play-app/target/shacl-play-app-0.12.2-onejar.jar \\
        --rules ../owl2shacl/owl2sh-closed.ttl

Run ``--help`` for the full argument list. See ``pipeline/README.md`` for how to obtain the
two tools, which versions are pinned, and why each stage is configured the way it is.

Outputs
-------
``standards/<standard>/generated/``

- ``<name>.owl.ttl``          the OWL 2 ontology
- ``<name>.shacl.ttl``        the SHACL shapes
- ``provenance.json``         inputs, tool versions and checksums of everything involved

The provenance file is what makes a generated artifact traceable: it names the model it came
from, the tool commit that produced it and the rules that shaped it, so a reviewer can tell
whether a difference comes from the model or from the toolchain.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from xml.etree import ElementTree

REPO_ROOT = Path(__file__).resolve().parents[1]

#: Per-standard pipeline description. Adding a standard means adding an entry plus its
#: ShapeChange configuration under pipeline/ — no code change.
STANDARDS = {
    "asam-opendrive": {
        "model": "standards/asam-opendrive/uml/opendrive.scxml",
        "config": "pipeline/opendrive-owl.config.xml",
        "artifact": "opendrive",
        # Used by scripts/check_xsd_structural_parity.py only; the OWL/SHACL stages
        # above never read these three keys.
        "xsd_config": "pipeline/opendrive-xsd.config.xml",
        "xsd_schema_dir": "standards/asam-opendrive/schema",
        "xsd_prefix": "OpenDRIVE",
        # The XSD target does not apply the OWL packaging rule, so its run is clean.
        "tolerated_errors": {"owl": ("single-ontology-per-schema",)},
        "union_defects": frozenset({"e_countryCode", "t_grEqZeroOrContactPoint"}),
    },
    "asam-openscenario-xml": {
        "model": "standards/asam-openscenario-xml/uml/openscenario.scxml",
        "config": "pipeline/openscenario-owl.config.xml",
        "artifact": "openscenario",
        "xsd_config": "pipeline/openscenario-xsd.config.xml",
        "xsd_schema_dir": "standards/asam-openscenario-xml/schema",
        "xsd_prefix": "OpenSCENARIO",
        # The OWL stage tolerates nothing, and needs to tolerate nothing. Unlike OpenDRIVE,
        # the OpenSCENARIO model carries no targetNamespace tagged values at all, so the schema
        # package is named once in the configuration and ShapeChange resolves exactly one
        # schema — the condition producing OpenDRIVE's 227 singleOntologyPerSchema errors does
        # not arise, and neither do any union-encoding defects. Should either appear, that is a
        # change in the model and this pipeline will stop. Only the XSD verification stage has
        # a documented exception, for one property ASAM models as a reference to a union.
        "tolerated_errors": {"xsd": ("union-valued-reference",)},
        "union_defects": frozenset(),
    },
}


#: Distributions whose versions determine the bytes of a canonicalized artifact. rdflib does
#: the final serialization, so a minor bump there can reintroduce exactly the churn that
#: canonicalizing removes — which is why all three are pinned in scripts/requirements.txt and
#: recorded in provenance.json.
SERIALIZATION_DISTS = ("diffable-rdf", "rdflib", "pyoxigraph")

#: ShapeChange log messages that are understood and deliberately do not fail the build, keyed
#: by the name a standard opts into through its ``tolerated_errors``. Each entry pairs a matcher
#: with the reason it is tolerated. Anything else logged at Error level stops the pipeline, so a
#: genuine error cannot hide among these.
#:
#: Tolerations are opted into per standard *and per stage* rather than applied globally: a
#: condition explained by one model's encoding says nothing about another's, and one explained
#: for the XML Schema target says nothing about the OWL target. Extending OpenDRIVE's
#: explanation to a second standard, or OpenSCENARIO's XSD exception to its OWL run, would
#: suppress exactly the signal each one documents.
TOLERATED_ERRORS = {
    "single-ontology-per-schema": (
        re.compile(
            r"Rule 'rule-owl-pkg-singleOntologyPerSchema' is in effect, "
            r"but no schema package was found for class"
        ),
        "the OpenDRIVE EA model tags all seven sub-packages with the same targetNamespace, "
        "so ShapeChange sees eight schemas resolving to one ontology name and reports every "
        "class outside the schema it is currently processing. The emitted ontology is "
        "complete regardless; see the pipeline README",
    ),
    "union-valued-reference": (
        re.compile(
            r"Property '[^']+' of class '[^']+' is not a composition, but has a data type as "
            r"its value"
        ),
        "OpenSCENARIO models ActivateControllerAction.objectControllerRef as an association to "
        "ObjectController, a <<union>>, while ASAM's normative XSD declares it type=\"String\" "
        "- a reference by name. A union has no identity, so the XML Schema target is right to "
        "refuse to encode a reference to one. The generated XSD therefore omits this one "
        "property, which is why the structural comparison shows one fewer attribute; the "
        "enumeration-value invariant this check enforces is unaffected. Tracked as an ASAM "
        "change request; see the pipeline README",
    ),
}

_UNION_WARNING = re.compile(
    r"The class '([^']+)' is modelled as a feature type, object type, data type, mixin, or "
    r"union, but has (?:more than one supertype of the same kind|a supertype of a different "
    r"category)"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def serialization_versions() -> dict[str, str]:
    """Versions of the canonicalization stack, for the provenance record."""
    versions = {}
    for dist in SERIALIZATION_DISTS:
        try:
            versions[dist] = version(dist)
        except PackageNotFoundError:
            versions[dist] = "unknown"
    return versions


def check_shapechange_log(log: Path, spec: dict, stage: str) -> None:
    """Fail on anything in the ShapeChange log that is not a known, explained condition.

    ShapeChange exits 0 while logging Error-level messages, so its exit code says nothing
    about whether the run was clean. What counts as explained is declared by the standard's
    own entry in ``STANDARDS``, per *stage*: the OpenDRIVE model produces two categories of
    noise in its OWL run, both rooted in the EA model rather than in this pipeline, and both
    are counted here rather than silently ignored, so a new message of either kind is a build
    failure instead of something a reader has to notice in a 900-line log.

    Tolerations are keyed by stage because the two ShapeChange targets diagnose different
    things about the same model, and a condition explained for one is not explained for the
    other. OpenSCENARIO is the case in point: its OWL run is completely clean, while its XML
    Schema run reports one property the target cannot encode. Declaring that per standard
    would have suppressed the OWL run's zero-tolerance guarantee to buy a toleration the XSD
    verification needs. A stage that declares no tolerations - the default - requires a
    completely clean log.

    Args:
        log: The log file the resolved configuration wrote.
        spec: The standard's ``STANDARDS`` entry.
        stage: Which target produced the log, ``"owl"`` or ``"xsd"``.
    """
    if not log.exists():
        raise SystemExit(f"ShapeChange wrote no log at {log}; cannot verify the run was clean")

    by_stage = spec.get("tolerated_errors", {})
    unknown = set(by_stage) - {"owl", "xsd"}
    if unknown:
        raise SystemExit(
            f"unknown stage(s) {sorted(unknown)} in tolerated_errors; expected 'owl' or 'xsd'"
        )
    tolerations = tuple(TOLERATED_ERRORS[name] for name in by_stage.get(stage, ()))
    union_defects = spec.get("union_defects", frozenset())

    try:
        root = ElementTree.parse(log).getroot()
    except ElementTree.ParseError as exc:
        # A truncated log usually means the JVM died mid-run, which is exactly the case where
        # silently continuing would publish an artifact from a half-finished generation.
        raise SystemExit(
            f"{log.name} is not parseable XML ({exc}); the ShapeChange run cannot be verified, "
            "so its output is not trustworthy"
        ) from exc
    tolerated: dict[str, int] = {}
    unexpected: list[str] = []
    for element in root.iter():
        if not element.tag.endswith("Error"):
            continue
        message = element.get("message", "")
        for matcher, reason in tolerations:
            if matcher.search(message):
                tolerated[reason] = tolerated.get(reason, 0) + 1
                break
        else:
            unexpected.append(message)

    for reason, count in tolerated.items():
        print(f"  tolerated {count} ShapeChange error(s): {reason}")

    if unexpected:
        for message in unexpected[:20]:
            sys.stderr.write(f"  ShapeChange error: {message}\n")
        raise SystemExit(
            f"{len(unexpected)} unexpected ShapeChange error(s) in {log.name}; "
            "the pipeline refuses to publish an artifact from a run it cannot vouch for"
        )

    reported = {
        match.group(1)
        for element in root.iter()
        if element.tag.endswith("Warning")
        for match in [_UNION_WARNING.search(element.get("message", ""))]
        if match
    }
    if reported - union_defects:
        raise SystemExit(
            "ShapeChange rejects the supertype structure of "
            f"{', '.join(sorted(reported - union_defects))}, which is not in the documented "
            "set of union-encoding defects for this standard. Either the EA model changed or "
            "a new defect appeared: investigate before publishing, then update the standard's "
            "'union_defects' entry and the 'Known encoding gaps' section of the model's "
            "README together."
        )
    if reported:
        print(
            f"  {len(reported)} known union-encoding defect(s) unchanged: "
            f"{', '.join(sorted(reported))}"
        )


def model_class_names(model: Path) -> set[str]:
    """Every class name in an SCXML model, lower-cased.

    Raises:
        SystemExit: if two classes differ only by case. Coverage below is compared
            case-insensitively, because ShapeChange normalises a class name by upper-casing
            its first character; that comparison is only exact while no two names collide
            under it, so the condition is asserted rather than assumed.
    """
    names: dict[str, str] = {}
    for element in ElementTree.parse(model).getroot().iter():
        if not element.tag.endswith("}Class") and element.tag != "Class":
            continue
        for child in element:
            if child.tag.endswith("}name") or child.tag == "name":
                name = (child.text or "").strip()
                if name:
                    previous = names.setdefault(name.lower(), name)
                    if previous != name:
                        raise SystemExit(
                            f"{model.name} contains classes '{previous}' and '{name}', which "
                            "differ only by case; the coverage check below cannot tell them "
                            "apart and would pass while one was missing"
                        )
                break
    return set(names)


def check_model_coverage(spec: dict, owl: Path, config: Path) -> None:
    """Fail unless every class in the source model reached the ontology.

    This is the guard for the regression that motivated the whole pipeline: all 55 unmapped
    OpenDRIVE enumerations were once silently dropped, and the result was 530 KB of
    plausible-looking OWL. ShapeChange logged a warning 55 times and exited 0.

    A class is accounted for when it is emitted as a named ``owl:Class`` or ``rdfs:Datatype``,
    or when a map entry deliberately replaces it with an RDF datatype - OpenDRIVE's ``t_bool``
    becomes ``xsd:boolean``, so its absence from the ontology is correct. Anything else is a
    class the model declares and the ontology does not have.

    The map entries are read from the resolved configuration rather than assumed, for the same
    reason ``shapechange_log`` reads the log path from it: a configuration that maps types from
    a different file would otherwise make this check quietly wrong.
    """
    from rdflib import BNode, Graph, RDF, RDFS
    from rdflib.namespace import OWL as OWL_NS

    mapped: set[str] = set()
    for include in ElementTree.parse(config).getroot().iter():
        href = include.get("href", "") if include.tag.endswith("include") else ""
        if not href.endswith("mapentries-asam.xml"):
            continue
        entries = ElementTree.parse(href.removeprefix("file:///")).getroot()
        for entry in entries.iter():
            if entry.tag.endswith("RdfTypeMapEntry") and entry.get("type"):
                mapped.add(entry.get("type", "").lower())

    graph = Graph().parse(owl, format="turtle")
    emitted = {
        str(subject).rsplit("#", 1)[-1].rsplit("/", 1)[-1].lower()
        for class_type in (OWL_NS.Class, RDFS.Datatype)
        for subject in graph.subjects(RDF.type, class_type)
        if not isinstance(subject, BNode)
    }

    declared = model_class_names(REPO_ROOT / spec["model"])
    missing = sorted(declared - emitted - mapped)
    if missing:
        raise SystemExit(
            f"{len(missing)} of {len(declared)} classes in {Path(spec['model']).name} reached "
            f"neither the ontology nor a map entry: {', '.join(missing[:15])}"
            + (" …" if len(missing) > 15 else "")
            + ". Check the ShapeChange log for 'Unsupported class category' - an encoding rule "
            "is probably missing for that category."
        )
    print(
        f"  all {len(declared)} model classes accounted for "
        f"({len(declared & mapped)} mapped to RDF datatypes by configuration)"
    )


def canonicalize_turtle(path: Path) -> None:
    """Rewrite a Turtle file in RDFC-1.0 canonical form, in place.

    Both generators assign blank-node identifiers from process-dependent ordering, so an
    unchanged model can produce a diff of hundreds of lines that carries no meaning: the
    previous regeneration in this branch's history changed 1,428 lines while the triple set
    stayed identical. Canonicalizing makes regeneration byte-stable, so a diff in a generated
    artifact means the model or the toolchain changed and is worth reading.

    Only the serialization changes. That the output says the same thing as the input is
    guaranteed by diffable-rdf itself from 0.0.2 on: it re-parses its own output, requires the
    result to be isomorphic to the input, and raises otherwise (ASCS-eV/diffable-rdf#1, where
    shared rdf:List tails were silently dropped or duplicated). The triple count is still
    asserted here as a cheap tripwire against a regression in that guarantee - a full
    isomorphism check would repeat, at ninety seconds per artifact, work the library has
    already done. The file is written as bytes with LF endings so a Windows run cannot
    introduce CRLF.
    """
    try:
        from diffable_rdf import deterministic_turtle
        from rdflib import Graph
    except ImportError as exc:  # pragma: no cover - environment, not logic
        raise SystemExit(
            "diffable-rdf is required to serialize the generated artifacts deterministically; "
            "install it with 'pip install -r scripts/requirements.txt'"
        ) from exc

    graph = Graph().parse(path, format="turtle")
    expected = len(graph)
    text = deterministic_turtle(graph)
    actual = len(Graph().parse(data=text, format="turtle"))
    if actual != expected:
        raise SystemExit(
            f"canonicalizing {path.name} changed the triple count ({expected} -> {actual}); "
            "refusing to write a lossy artifact"
        )
    path.write_bytes(text.encode("utf-8"))
    print(f"  canonicalized {path.name} ({expected:,} triples)")


def run(command: list[str], cwd: Path, what: str) -> None:
    """Run a stage, failing loudly with its output when it does not succeed."""
    # Elide long arguments: a resolved Java classpath is thousands of characters and makes
    # the log unreadable for the person trying to see what ran.
    shown = [c if len(str(c)) < 80 else f"{str(c)[:60]}…({len(str(c))} chars)" for c in command]
    print(f"  $ {' '.join(str(c) for c in shown)}")
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.stderr.write(result.stdout[-4000:] + result.stderr[-4000:])
        raise SystemExit(f"{what} failed with exit code {result.returncode}")


def git_describe(repo: Path) -> str:
    """Identify a tool checkout precisely enough to reproduce a run."""
    try:
        rev = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        dirty = subprocess.run(
            ["git", "-C", str(repo), "status", "--porcelain"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        return f"{rev}{'-dirty' if dirty else ''}"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def build_shapechange(home: Path, mvn: str) -> Path:
    """Build ShapeChange without Enterprise Architect and return its resource directory.

    ``-DskipEa`` leaves out the shapechange-ea module, which compiles against the
    proprietary org.sparx:eaapi artifact that ships inside an EA installation. The OWL
    target and the SCXML reader both live in shapechange-core, and EA model readers are
    resolved by class name at runtime, so nothing needed here depends on EA.

    Requires ShapeChange/ShapeChange#757 (merged upstream into `next`); without it the
    reactor stops at shapechange-ea.
    """
    print("• building ShapeChange (-DskipEa)")
    run([mvn, "-q", "-DskipEa", "install", "-DskipTests"], cwd=home, what="ShapeChange build")
    return home / "shapechange-core" / "src" / "main" / "resources"


def shapechange_classpath(home: Path, mvn: str, work: Path) -> str:
    """Classpath for running the OWL target: shapechange-core plus its dependencies.

    The runnable entry point lives in shapechange-app, whose single source file is compiled
    here rather than taken from the assembled distribution, so that a build without EA needs
    no distribution assembly step.
    """
    cp_file = work / "shapechange-cp.txt"
    run([mvn, "-q", "-pl", "shapechange-core", "dependency:build-classpath",
         f"-Dmdep.outputFile={cp_file}"], cwd=home, what="ShapeChange classpath export")
    core_classes = home / "shapechange-core" / "target" / "classes"
    app_classes = work / "shapechange-app-classes"
    app_classes.mkdir(parents=True, exist_ok=True)
    app_source = home / "shapechange-app/src/main/java/de/interactive_instruments/shapechange/app/Main.java"
    run(["javac", "-nowarn", "-cp", os.pathsep.join([cp_file.read_text(), str(core_classes)]),
         "-d", str(app_classes), str(app_source)], cwd=home, what="ShapeChange app compile")
    return os.pathsep.join([cp_file.read_text(), str(core_classes), str(app_classes)])


def shapechange_log(config: Path) -> Path:
    """Where the resolved configuration told ShapeChange to write its log.

    Read from the configuration rather than assumed, so that changing logFile there cannot
    leave this script checking a stale file and reporting a clean run.
    """
    for parameter in ElementTree.parse(config).getroot().iter():
        if parameter.tag.endswith("parameter") and parameter.get("name") == "logFile":
            return Path(parameter.get("value", ""))
    raise SystemExit(
        f"{config.name} sets no logFile parameter, so the run cannot be verified; "
        "add one to the pipeline configuration"
    )


def generate_owl(spec: dict, classpath: str, resources: Path, out_dir: Path, work: Path) -> Path:
    """Stage 1: ASAM UML (SCXML) → OWL 2, via the ShapeChange OWL target."""
    print("• generating OWL from the committed SCXML model")
    template = (REPO_ROOT / spec["config"]).read_text()
    config = work / "shapechange.config.xml"
    owl_out = work / "owl"
    # Emptied first, so that the "exactly one Turtle output" check below is a statement about
    # this run. The work directory is reused across invocations, and generating a second
    # standard into a directory still holding the first one's ontology made that check fail on
    # a file ShapeChange had not just produced.
    shutil.rmtree(owl_out, ignore_errors=True)
    config.write_text(
        template.replace("{SHAPECHANGE_RESOURCES}", str(resources))
        .replace("{PIPELINE}", str(REPO_ROOT / "pipeline"))
        .replace("{OUT}", str(owl_out))
    )
    run(["java", "-cp", classpath,
         "de.interactive_instruments.shapechange.app.Main", "-c", str(config)],
        cwd=REPO_ROOT, what="ShapeChange OWL generation")
    check_shapechange_log(shapechange_log(config), spec, stage="owl")

    produced = sorted(owl_out.rglob("*.ttl"))
    if not produced:
        raise SystemExit("ShapeChange produced no Turtle output; see the log in the work directory")
    if len(produced) > 1:
        raise SystemExit(
            "ShapeChange produced more than one Turtle output "
            f"({', '.join(str(p) for p in produced)}); refusing to silently pick one. "
            "Picking the wrong file is exactly the class of bug this pipeline exists to "
            "catch (see the enumeration-dropping fix earlier in this branch's history) - "
            "fix the ShapeChange target configuration to emit exactly one file, or make "
            "the selection explicit here."
        )
    target = out_dir / f"{spec['artifact']}.owl.ttl"
    shutil.copyfile(produced[0], target)
    # Checked before stage 2 rather than after: shapes derived from an incomplete ontology are
    # themselves incomplete, and the missing classes are far harder to spot there.
    check_model_coverage(spec, target, config)
    # Before stage 2, so the SHACL is derived from a deterministic input too.
    canonicalize_turtle(target)
    return target


def generate_shacl(owl: Path, shaclplay_jar: Path, rules: Path, out_dir: Path, artifact: str, work: Path) -> Path:
    """Stage 2: OWL 2 → SHACL, via the SHACL Play! owl2shacl rules.

    ``--rules`` pins the ruleset to a known file. Without it the tool fetches the rules from
    the main branch of the owl2shacl repository at run time, which makes the output depend on
    what that branch happened to contain (see sparna-git/shacl-play#344).
    """
    print("• converting OWL to SHACL with the pinned owl2shacl rules")
    target = out_dir / f"{artifact}.shacl.ttl"
    # Runs in the work directory, not the repository root: the shacl-play application
    # writes shacl-play-app.log into its working directory, and that log is build
    # output, not a repository file. All paths passed to it are absolute.
    run(["java", "-jar", str(shaclplay_jar), "owl2shacl",
         "-i", str(owl), "-o", str(target), "--rules", str(rules)],
        cwd=work, what="owl2shacl conversion")
    canonicalize_turtle(target)
    return target


def write_provenance(spec: dict, standard: str, shapechange: Path, shaclplay: Path,
                     rules: Path, owl: Path, shacl: Path, out_dir: Path) -> Path:
    """Record what produced these artifacts, so a diff in them can be attributed.

    Tools are identified by name and content, never by the path they happened to live at:
    an absolute path is specific to whoever ran the pipeline and says nothing about what
    was used.

    The ruleset is recorded by checksum *and* by the commit of the repository it came from.
    A checksum alone proves two runs used the same bytes but not that anyone else can obtain
    them: the previously committed provenance in this branch recorded a rules checksum that
    matches no commit in the owl2shacl repository, because the run had picked up an
    unversioned working copy. The commit is what makes the stage reproducible by a third
    party, and "unknown" here means the ruleset was not under version control.
    """
    provenance = {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "standard": standard,
        "source_model": {"path": spec["model"], "sha256": sha256(REPO_ROOT / spec["model"])},
        "configuration": {"path": spec["config"], "sha256": sha256(REPO_ROOT / spec["config"])},
        "tools": {
            "shapechange": {"commit": git_describe(shapechange), "profile": "-DskipEa"},
            "shacl_play": {"jar": shaclplay.name},
            "owl2shacl_rules": {
                "name": rules.name,
                "sha256": sha256(rules),
                "commit": git_describe(rules.parent),
            },
            "serialization": serialization_versions(),
        },
        "outputs": {p.name: sha256(p) for p in (owl, shacl)},
    }
    target = out_dir / "provenance.json"
    target.write_text(json.dumps(provenance, indent=2) + "\n")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--standard", choices=sorted(STANDARDS), default="asam-opendrive")
    parser.add_argument("--shapechange", type=Path, required=True,
                        help="ShapeChange checkout, built here with -DskipEa")
    parser.add_argument("--shaclplay", type=Path, required=True,
                        help="shacl-play-app onejar providing the owl2shacl command")
    parser.add_argument("--rules", type=Path, required=True,
                        help="owl2shacl ruleset to pin, e.g. owl2sh-closed.ttl")
    parser.add_argument("--mvn", default="mvn", help="Maven executable (default: mvn)")
    parser.add_argument("--work", type=Path, default=Path(".pipeline-work"),
                        help="scratch directory for build output (default: .pipeline-work)")
    args = parser.parse_args()

    for path, what in ((args.shapechange, "--shapechange"), (args.shaclplay, "--shaclplay"), (args.rules, "--rules")):
        if not path.exists():
            raise SystemExit(f"{what} does not exist: {path}")

    spec = STANDARDS[args.standard]
    work = (REPO_ROOT / args.work).resolve()
    work.mkdir(parents=True, exist_ok=True)
    out_dir = REPO_ROOT / "standards" / args.standard / "generated"
    out_dir.mkdir(parents=True, exist_ok=True)

    resources = build_shapechange(args.shapechange.resolve(), args.mvn)
    classpath = shapechange_classpath(args.shapechange.resolve(), args.mvn, work)
    owl = generate_owl(spec, classpath, resources, out_dir, work)
    shacl = generate_shacl(owl, args.shaclplay.resolve(), args.rules.resolve(), out_dir, spec["artifact"], work)

    provenance = write_provenance(spec, args.standard, args.shapechange.resolve(),
                                  args.shaclplay.resolve(), args.rules.resolve(),
                                  owl, shacl, out_dir)

    print(f"\n{owl.relative_to(REPO_ROOT)}   {owl.stat().st_size:,} bytes")
    print(f"{shacl.relative_to(REPO_ROOT)}   {shacl.stat().st_size:,} bytes")
    print(f"{provenance.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
