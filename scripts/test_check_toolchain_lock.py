#!/usr/bin/env python3
"""Regression tests for ``check_toolchain_lock.py``'s internal-consistency check.

The lock says the same thing twice on purpose: ``carried_commits`` lists the path from
``upstream_base`` to ``commit``, and ``commit``/``upstream_base`` bound that path. Saying it
twice is only worth anything if the two are checked against each other, so what is pinned
here is that agreement - in both directions, including the direction where a fork carries
nothing at all because upstream merged everything it was carrying.

That last case is the one these tests were written for. An earlier version rejected it
outright, on the assumption that a fork always carries something; the only way to satisfy
it after an upstream merge would have been to keep an already-merged commit listed as
pending, which is precisely the drift the lock exists to prevent.

No JDK, no Maven, no network, no tool checkout: the lock is built inline.

Run:  python scripts/test_check_toolchain_lock.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from check_toolchain_lock import LOCK_PATH, check_lock_schema

BASE = "a" * 40
CARRIED = "b" * 40
OTHER = "c" * 40
FINGERPRINT = "d" * 64

FAILURES: list[str] = []


def check(condition: bool, what: str) -> None:
    if condition:
        print(f"  ok   {what}")
    else:
        print(f"  FAIL {what}")
        FAILURES.append(what)


def tool(commit: str, base: str, carried: list[dict]) -> dict:
    return {
        "fork": "ASCS-eV/Example",
        "branch": "feature/asam-pipeline",
        "commit": commit,
        "upstream": "example/Example",
        "upstream_branch": "main",
        "upstream_base": base,
        "carried_commits": carried,
    }


#: A fork carrying one documented commit on top of its upstream base - the ordinary case.
CARRIES_ONE = tool(CARRIED, BASE, [{"commit": CARRIED, "upstream_pr": "https://example/pull/1"}])

#: A fork pinned exactly at upstream, carrying nothing.
CARRIES_NOTHING = tool(BASE, BASE, [])


def problems_for(entry: dict) -> list[str]:
    """Run the schema check with ``owl2shacl`` replaced by ``entry``.

    Returns only the problems naming ``owl2shacl``, so that the requirements the other
    two tools and the surrounding lock sections carry cannot be mistaken for a verdict
    on the entry under test.
    """
    lock = {
        "tools": {
            "shapechange": CARRIES_ONE,
            "owl2shacl": entry,
            "shacl_play": CARRIES_ONE,
        },
        "build_inputs": {
            "shapechange_runtime_fingerprint": FINGERPRINT,
            "shacl_play_jar_fingerprint": FINGERPRINT,
        },
        "build_environment": {"jdk_version": "21.0.12+8", "maven_version": "3.9.9"},
        "serialization": {},
    }
    return [problem for problem in check_lock_schema(lock) if "owl2shacl" in problem]


# --- the two states the lock may describe ----------------------------------------------
print("a fork's carried list and its commit/base pair must agree, in both directions")

check(problems_for(CARRIES_ONE) == [],
      "a fork carrying one documented commit is accepted")

# Before the fix this reported two problems: "carried_commits is empty" and "commit equals
# upstream_base; the fork carries nothing". Both described the healthy end state.
check(problems_for(CARRIES_NOTHING) == [],
      "a fork pinned at upstream carrying nothing is accepted")

# --- ways the two can disagree ---------------------------------------------------------
print("\nand a disagreement between them is reported")

problems = problems_for(tool(CARRIED, BASE, []))
check(any("empty" in problem and BASE in problem for problem in problems),
      "an empty carried list with commit != upstream_base is rejected")

problems = problems_for(tool(BASE, BASE, [{"commit": CARRIED, "upstream_pr": "https://e/1"}]))
check(any("carries nothing" in problem for problem in problems),
      "commit == upstream_base while carrying a commit is rejected")

problems = problems_for(tool(
    OTHER, BASE, [{"commit": CARRIED, "upstream_pr": "https://e/1"}]))
check(any("does not end at the locked commit" in problem for problem in problems),
      "a carried chain whose last entry is not the locked commit is rejected")

# --- the checks that must survive the refactor -----------------------------------------
print("\nthe rest of the entry is still checked")

problems = problems_for(tool(CARRIED, BASE, [
    {"commit": CARRIED, "upstream_pr": "https://e/1"},
    {"commit": CARRIED, "upstream_pr": "https://e/1"},
]))
check(any("duplicate" in problem for problem in problems),
      "a duplicated carried commit is rejected")

problems = problems_for(tool(CARRIED, BASE, [{"commit": CARRIED}]))
check(any("neither" in problem for problem in problems),
      "a carried commit with neither an upstream_pr nor a note is rejected")

problems = problems_for(tool("b" * 7, BASE, [{"commit": "b" * 7, "upstream_pr": "https://e/1"}]))
check(any("not a full 40-char SHA" in problem for problem in problems),
      "an abbreviated commit is rejected")

problems = problems_for(tool(CARRIED, "z" * 40, [{"commit": CARRIED, "upstream_pr": "https://e/1"}]))
check(any("upstream_base is not a full 40-char SHA" in problem for problem in problems),
      "a non-hexadecimal upstream_base is rejected")

entry = dict(CARRIES_ONE)
del entry["carried_commits"]
check(any("carried_commits is missing" in problem for problem in problems_for(entry)),
      "an absent carried_commits is still reported as missing, not read as empty")

# --- and the committed lock itself -----------------------------------------------------
print("\nthe committed lock satisfies the check")

committed = json.loads(Path(LOCK_PATH).read_text())
check(check_lock_schema(committed) == [],
      "pipeline/toolchain-lock.json is internally consistent")

# ---------------------------------------------------------------------------------------
print()
if FAILURES:
    print(f"{len(FAILURES)} FAILED:")
    for name in FAILURES:
        print(f"  - {name}")
    sys.exit(1)
print("all toolchain-lock consistency tests pass")
