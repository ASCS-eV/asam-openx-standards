#!/usr/bin/env python3
"""
Validate ``pipeline/toolchain-lock.json`` against itself and against the committed
``provenance.json`` files, without needing a JDK, Maven, network access, or any tool
checkout.

This is the fast, static half of toolchain verification: it proves the lock is
internally consistent (full 40-character SHAs, no duplicate carried commits, each
carried-commit chain actually ending at the locked commit, every carried commit mapped
to an upstream PR) and that what was actually generated
(``standards/<standard>/generated/provenance.json``) matches what the lock claims
produced it. It does not rebuild anything and does not prove the fork commits are still
checked out correctly on disk - reproducing the fork commits and the ``build_inputs``
fingerprints from a live checkout is ``scripts/generate_semantic_artifacts.py``'s job,
run wherever the sibling ``../ShapeChange``, ``../shacl-play`` and ``../owl2shacl``
checkouts are available. Both checks matter; this one is the one CI can always run.

Usage
-----
::

    python scripts/check_toolchain_lock.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = REPO_ROOT / "pipeline" / "toolchain-lock.json"
REQUIREMENTS_PATH = REPO_ROOT / "scripts" / "requirements.txt"

_SHA_LENGTH = 40
_FINGERPRINT_LENGTH = 64
_HEX_DIGITS = set("0123456789abcdef")


def _is_hex(value: str, length: int) -> bool:
    return len(value) == length and set(value.lower()) <= _HEX_DIGITS


def check_lock_schema(lock: dict) -> list[str]:
    """Validate the lock is internally consistent, independent of any live checkout."""
    problems: list[str] = []
    tools = lock.get("tools", {})
    for tool_name in ("shapechange", "owl2shacl", "shacl_play"):
        entry = tools.get(tool_name)
        if entry is None:
            problems.append(f"tools.{tool_name} is missing")
            continue
        for field in (
            "fork", "branch", "commit", "upstream", "upstream_branch",
            "upstream_base", "carried_commits",
        ):
            if field not in entry:
                problems.append(f"tools.{tool_name}.{field} is missing")

        commit = entry.get("commit", "")
        if commit and not _is_hex(commit, _SHA_LENGTH):
            problems.append(f"tools.{tool_name}.commit is not a full 40-char SHA: {commit!r}")
        base = entry.get("upstream_base", "")
        if base and not _is_hex(base, _SHA_LENGTH):
            problems.append(f"tools.{tool_name}.upstream_base is not a full 40-char SHA: {base!r}")
        if commit and base and commit == base:
            problems.append(f"tools.{tool_name}.commit equals upstream_base; the fork carries nothing")

        carried = entry.get("carried_commits", [])
        if not carried:
            problems.append(f"tools.{tool_name}.carried_commits is empty")
        carried_shas = [carried_commit.get("commit", "") for carried_commit in carried]
        for sha in carried_shas:
            if not _is_hex(sha, _SHA_LENGTH):
                problems.append(
                    f"tools.{tool_name} carries a commit that is not a full 40-char SHA: {sha!r}"
                )
        if len(carried_shas) != len(set(carried_shas)):
            problems.append(f"tools.{tool_name}.carried_commits has duplicate entries")
        # The chain of carried commits is the ordered path from upstream_base to the
        # locked commit; if its last entry is not the locked commit, either the lock
        # was hand-edited inconsistently or a later rebase was only half-applied.
        if carried_shas and commit and carried_shas[-1] != commit:
            problems.append(
                f"tools.{tool_name}.carried_commits does not end at the locked commit "
                f"({carried_shas[-1]!r} != {commit!r})"
            )
        # Every carried commit must say why the fork carries it. Normally that is the
        # upstream contribution it implements; a fork may also legitimately carry a change
        # that has not been submitted yet, and refusing to record one would only push it
        # out of the lock and out of sight. Either is accepted, neither may be absent - an
        # unexplained commit on a fork branch is exactly what this file exists to prevent.
        for carried_commit in carried:
            if not (carried_commit.get("upstream_pr") or carried_commit.get("note")):
                problems.append(
                    f"tools.{tool_name} carries {carried_commit.get('commit')} with neither "
                    "an upstream_pr mapping nor a note explaining why the fork carries it"
                )

    build_inputs = lock.get("build_inputs")
    if build_inputs is None:
        problems.append("build_inputs is missing")
    else:
        for field in ("shapechange_runtime_fingerprint", "shacl_play_jar_fingerprint"):
            value = build_inputs.get(field, "")
            if not _is_hex(value, _FINGERPRINT_LENGTH):
                problems.append(
                    f"build_inputs.{field} is not a {_FINGERPRINT_LENGTH}-hex-digit "
                    f"fingerprint: {value!r}"
                )

    build_environment = lock.get("build_environment")
    if build_environment is None:
        problems.append("build_environment is missing")
    else:
        for field in ("jdk_version", "maven_version"):
            if not build_environment.get(field):
                problems.append(f"build_environment.{field} is missing")

    if "serialization" not in lock:
        problems.append("serialization is missing")

    return problems


def check_serialization_matches_requirements(lock: dict) -> list[str]:
    """The lock's pinned Python versions must be exactly what requirements.txt installs."""
    problems: list[str] = []
    if not REQUIREMENTS_PATH.exists():
        problems.append(f"{REQUIREMENTS_PATH.relative_to(REPO_ROOT)} not found")
        return problems
    requirements_text = REQUIREMENTS_PATH.read_text()
    for dist, dist_version in lock.get("serialization", {}).items():
        if dist.startswith("_"):
            continue
        if f"{dist}=={dist_version}" not in requirements_text:
            problems.append(
                f"serialization.{dist} ({dist_version}) is not pinned as "
                f"'{dist}=={dist_version}' in {REQUIREMENTS_PATH.relative_to(REPO_ROOT)}"
            )
    return problems


def check_provenance_matches_lock(lock: dict, provenance_path: Path) -> list[str]:
    """A committed provenance.json must name exactly the tools the lock pins."""
    problems: list[str] = []
    label = provenance_path.relative_to(REPO_ROOT)
    provenance = json.loads(provenance_path.read_text())
    tools_recorded = provenance.get("tools", {})

    shapechange_recorded = tools_recorded.get("shapechange", {})
    expected_shapechange_commit = lock["tools"]["shapechange"]["commit"]
    recorded_commit = (shapechange_recorded.get("commit") or "").split("-dirty")[0]
    if recorded_commit != expected_shapechange_commit:
        problems.append(
            f"{label}: tools.shapechange.commit {shapechange_recorded.get('commit')!r} "
            f"!= locked {expected_shapechange_commit!r}"
        )
    expected_sc_fingerprint = lock["build_inputs"]["shapechange_runtime_fingerprint"]
    if shapechange_recorded.get("runtime_fingerprint") != expected_sc_fingerprint:
        problems.append(
            f"{label}: tools.shapechange.runtime_fingerprint does not match "
            "build_inputs.shapechange_runtime_fingerprint"
        )

    owl2shacl_recorded = tools_recorded.get("owl2shacl_rules", {})
    expected_owl2shacl_commit = lock["tools"]["owl2shacl"]["commit"]
    recorded_rules_commit = (owl2shacl_recorded.get("commit") or "").split("-dirty")[0]
    if recorded_rules_commit != expected_owl2shacl_commit:
        problems.append(
            f"{label}: tools.owl2shacl_rules.commit {owl2shacl_recorded.get('commit')!r} "
            f"!= locked {expected_owl2shacl_commit!r}"
        )

    shacl_play_recorded = tools_recorded.get("shacl_play", {})
    expected_shacl_play_commit = lock["tools"]["shacl_play"]["commit"]
    if shacl_play_recorded.get("commit") != expected_shacl_play_commit:
        problems.append(
            f"{label}: tools.shacl_play.commit {shacl_play_recorded.get('commit')!r} "
            f"!= locked {expected_shacl_play_commit!r}"
        )
    recorded_jar_fingerprint = shacl_play_recorded.get("jar_fingerprint", "")
    if not _is_hex(recorded_jar_fingerprint, _FINGERPRINT_LENGTH):
        problems.append(
            f"{label}: tools.shacl_play.jar_fingerprint is not a "
            f"{_FINGERPRINT_LENGTH}-hex-digit fingerprint"
        )
    expected_sp_fingerprint = lock["build_inputs"]["shacl_play_jar_fingerprint"]
    if recorded_jar_fingerprint != expected_sp_fingerprint:
        problems.append(
            f"{label}: tools.shacl_play.jar_fingerprint does not match "
            "build_inputs.shacl_play_jar_fingerprint"
        )

    build_environment_recorded = provenance.get("build_environment", {})
    for field in ("jdk_version", "maven_version"):
        if build_environment_recorded.get(field) != lock["build_environment"].get(field):
            problems.append(
                f"{label}: build_environment.{field} "
                f"{build_environment_recorded.get(field)!r} != "
                f"locked {lock['build_environment'].get(field)!r}"
            )

    serialization_recorded = tools_recorded.get("serialization", {})
    for dist, dist_version in lock.get("serialization", {}).items():
        if dist.startswith("_"):
            continue
        if serialization_recorded.get(dist) != dist_version:
            problems.append(
                f"{label}: tools.serialization.{dist} "
                f"{serialization_recorded.get(dist)!r} != locked {dist_version!r}"
            )

    return problems


def main() -> int:
    if not LOCK_PATH.exists():
        sys.stderr.write(f"{LOCK_PATH.relative_to(REPO_ROOT)} not found\n")
        return 1
    lock = json.loads(LOCK_PATH.read_text())

    problems: list[str] = []
    problems += check_lock_schema(lock)
    problems += check_serialization_matches_requirements(lock)

    provenance_paths = sorted((REPO_ROOT / "standards").glob("*/generated/provenance.json"))
    if not provenance_paths:
        problems.append("no standards/*/generated/provenance.json found to check")
    for provenance_path in provenance_paths:
        problems += check_provenance_matches_lock(lock, provenance_path)

    if problems:
        for problem in problems:
            sys.stderr.write(f"  {problem}\n")
        sys.stderr.write(f"\n{len(problems)} toolchain lock problem(s) found.\n")
        return 1

    print(
        "pipeline/toolchain-lock.json is internally consistent and matches every "
        f"committed provenance.json ({len(provenance_paths)} checked)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
