#!/usr/bin/env python3
"""Regression tests for how the pipeline pins ShapeChange's SNAPSHOT dependencies.

ShapeChange's pom declares ``de.interactive_instruments:ldproxy-cfg:4.9.0-SNAPSHOT``. Maven
resolves a SNAPSHOT to whatever build its repository serves, so the lock records the build
and the sha256 of its jar (``build_inputs.snapshot_dependencies``), and
``check_snapshot_dependencies`` refuses a classpath that does not match.

The sha256 is what has to match. The ii-maven repository republishes byte-identical jars
under new build numbers: 4.9.0-20260926.073424-39 has the sha256 of the locked
4.9.0-20260925.085606-38. A check that also compared the build number stopped the pipeline
on every republication, although nothing in the runtime had changed. What these tests pin:
a republication with the same content passes; different content, a SNAPSHOT the lock does
not record, and a recorded one that is gone all fail; and ``snapshot_dependencies`` reads
the build number from the local repository's metadata.

No JDK, no Maven, no network: the local repository is built inline.

Run:  python scripts/test_snapshot_dependencies.py
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import os
import sys
import tempfile
from pathlib import Path

from generate_semantic_artifacts import check_snapshot_dependencies, snapshot_dependencies

COORDINATES = "de.interactive_instruments:ldproxy-cfg:4.9.0-SNAPSHOT"
LOCKED_BUILD = "4.9.0-20260925.085606-38"
REPUBLISHED_BUILD = "4.9.0-20260926.073424-39"
CONTENT = b"ldproxy-cfg classes"
CONTENT_SHA256 = hashlib.sha256(CONTENT).hexdigest()

FAILURES: list[str] = []


def check(condition: bool, what: str) -> None:
    if condition:
        print(f"  ok   {what}")
    else:
        print(f"  FAIL {what}")
        FAILURES.append(what)


def lock(resolved: str = LOCKED_BUILD, sha: str = CONTENT_SHA256) -> dict:
    return {"build_inputs": {"snapshot_dependencies": {
        COORDINATES: {"resolved": resolved, "sha256": sha}}}}


def outcome(found: dict, locked: dict) -> tuple[str | None, str]:
    """Run the check; return its SystemExit message (None if it passed) and what it printed."""
    printed = io.StringIO()
    try:
        with contextlib.redirect_stdout(printed):
            check_snapshot_dependencies(found, locked)
    except SystemExit as stop:
        return str(stop), printed.getvalue()
    return None, printed.getvalue()


def local_repository(root: Path, build: str) -> Path:
    """A local Maven repository holding ldproxy-cfg, resolved to *build*, and its classpath file."""
    directory = root / "repository" / "de" / "interactive_instruments" / "ldproxy-cfg" / "4.9.0-SNAPSHOT"
    directory.mkdir(parents=True)
    jar = directory / "ldproxy-cfg-4.9.0-SNAPSHOT.jar"
    jar.write_bytes(CONTENT)
    (directory / "maven-metadata-ii-maven.xml").write_text(
        "<metadata><versioning><snapshotVersions>"
        f"<snapshotVersion><extension>pom</extension><value>{build}</value></snapshotVersion>"
        f"<snapshotVersion><extension>jar</extension><value>{build}</value></snapshotVersion>"
        "<snapshotVersion><classifier>sources</classifier><extension>jar</extension>"
        "<value>4.9.0-19990101.000000-1</value></snapshotVersion>"
        "</snapshotVersions></versioning></metadata>")
    released = root / "repository" / "org" / "example" / "released" / "1.0" / "released-1.0.jar"
    released.parent.mkdir(parents=True)
    released.write_bytes(b"released")
    classpath = root / "classpath.txt"
    classpath.write_text(os.pathsep.join([str(jar), str(released)]))
    return classpath


def main() -> int:
    print("reading the classpath")
    with tempfile.TemporaryDirectory() as directory:
        found = snapshot_dependencies(local_repository(Path(directory), REPUBLISHED_BUILD))
    check(found == {COORDINATES: {"resolved": REPUBLISHED_BUILD, "sha256": CONTENT_SHA256}},
          "the build number comes from the plain jar's snapshotVersion, released jars are skipped")

    print("a republication of the same content - the reason the sha256 decides")
    stop, printed = outcome({COORDINATES: {"resolved": REPUBLISHED_BUILD, "sha256": CONTENT_SHA256}},
                            lock())
    check(stop is None, "the same sha256 under a new build number passes")
    check(REPUBLISHED_BUILD in printed and LOCKED_BUILD in printed,
          "and names both build numbers")
    stop, printed = outcome({COORDINATES: {"resolved": LOCKED_BUILD, "sha256": CONTENT_SHA256}},
                            lock())
    check(stop is None and printed == "", "the locked build passes silently")

    print("what must still be refused")
    stop, _ = outcome({COORDINATES: {"resolved": REPUBLISHED_BUILD, "sha256": "0" * 64}}, lock())
    check(stop is not None and "content changed" in stop,
          "a different sha256 under a new build number fails")
    stop, _ = outcome({COORDINATES: {"resolved": LOCKED_BUILD, "sha256": "0" * 64}}, lock())
    check(stop is not None, "a different sha256 under the locked build number fails")
    stop, _ = outcome({"org.example:other:1.0-SNAPSHOT": {"resolved": "1.0-1", "sha256": "0" * 64},
                       COORDINATES: {"resolved": LOCKED_BUILD, "sha256": CONTENT_SHA256}}, lock())
    check(stop is not None and "does not record" in stop, "a SNAPSHOT the lock does not record fails")
    stop, _ = outcome({}, lock())
    check(stop is not None and "not on ShapeChange's classpath" in stop,
          "a recorded SNAPSHOT that is no longer on the classpath fails")

    print()
    if FAILURES:
        print(f"{len(FAILURES)} check(s) failed")
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
