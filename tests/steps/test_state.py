"""Steps for state.feature: state.json read with pubfleet's own functions,
offline."""

from __future__ import annotations

import json
from pathlib import Path

from pubfleet.state import repos_file, shape
from pytest_bdd import given, parsers, scenarios, then, when

scenarios("state.feature")

STATE = Path(__file__).resolve().parents[2] / "state.json"


@given("the state file", target_fixture="state")
def state_file():
    return json.loads(STATE.read_text(encoding="utf-8"))


@then("pubfleet finds nothing wrong with its shape")
def no_shape_problems(state):
    assert shape(state) == []


@then("each repository is named once, under the state's owner")
def named_once(state):
    names = list(state["repos"])
    assert len(names) == len(set(names))
    assert all("/" not in name for name in names), names
    listed = [entry["repo"] for entry in repos_file(state, "board")["repositories"]]
    assert all(repo.startswith(f"{state['owner']}/") for repo in listed), listed


@when(parsers.parse("pubfleet writes the repos file for the {role}"), target_fixture="written")
def written(state, role):
    return repos_file(state, role)


@then(parsers.parse("it lists each repository with {role} on, and no other"))
def lists_exactly(state, written, role):
    want = [f"{state['owner']}/{name}" for name, roles in state["repos"].items() if roles.get(role, False)]
    assert [entry["repo"] for entry in written["repositories"]] == want
