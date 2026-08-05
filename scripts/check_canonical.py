#!/usr/bin/env python3
"""Check that every committed generated artifact is in RDFC-1.0 canonical form.

``generate_semantic_artifacts.py`` writes canonical Turtle, so a committed artifact that is
not canonical was hand-edited, produced by an older pipeline, or produced with a different
serialization stack. This check catches all three without needing Maven, ShapeChange or
shacl-play.

It deliberately does not re-run the generators: proving that the bytes are canonical is a
different claim from proving they are what the model implies, and the two belong in different
jobs.

Cheap in dependencies, not in time
----------------------------------
Canonicalizing is the only way to prove a file is canonical, so this costs what
canonicalization costs - and RDFC-1.0 is superlinear in the number of blank nodes. Measured
locally: about 6 seconds for ``opendrive.shacl.ttl`` (4,963 triples) and about 17 minutes for
``openscenario.owl.ttl`` (15,673 triples, dominated by the 1,664 restriction nodes its 48
unions produce). Pass explicit paths, or run one standard per CI job, rather than assuming the
whole set is quick.

Usage::

    python scripts/check_canonical.py [path ...]

With no arguments, checks ``standards/*/generated/*.ttl``.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def display(path: Path) -> str:
    """Repository-relative where possible, absolute otherwise.

    ``relative_to`` raises for anything outside the repository, and a path given on the command
    line need not be inside it, so this never lets formatting a message become the error.
    """
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def main(argv: list[str]) -> int:
    try:
        from diffable_rdf import deterministic_turtle
        from rdflib import Graph
    except ImportError:
        sys.stderr.write(
            "diffable-rdf is required; install it with "
            "'pip install -r scripts/requirements.txt'\n"
        )
        return 2

    if argv:
        # Resolved so that a relative path given on the command line behaves exactly
        # like the glob results below.
        artifacts = [Path(a).resolve() for a in argv]
    else:
        artifacts = sorted(REPO_ROOT.glob("standards/*/generated/*.ttl"))

    if not artifacts:
        sys.stderr.write("no generated Turtle artifacts found to check\n")
        return 2

    stale: list[Path] = []
    for path in artifacts:
        graph = Graph().parse(path, format="turtle")
        canonical = deterministic_turtle(graph).encode("utf-8")
        if path.read_bytes() == canonical:
            print(f"ok: {display(path)} ({len(graph):,} triples)")
        else:
            stale.append(path)
            sys.stderr.write(
                f"not in canonical form: {display(path)}\n"
                "  regenerate it, or run it through canonicalize_turtle(), before committing\n"
            )

    print(f"checked {len(artifacts)} artifact(s), {len(stale)} not canonical")
    return 1 if stale else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
