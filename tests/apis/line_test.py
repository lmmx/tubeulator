"""Tests for the line API."""

import tubeulator
from line_data import line_snapshot_album as snapshot_album
from pytest import mark


@mark.parametrize("expected", [snapshot_album["meta_modes"]])
def test_meta_modes(expected):
    modes = tubeulator.fetch.line.meta_modes()
    assert [m.model_dump(mode="json") for m in modes] == expected


@mark.parametrize("line_id", ["waterloo-city"])
def test_lines_by_ids(line_id):
    """Relies on correct codegen of arrays (previously had a bug)."""
    expected = snapshot_album["lines_by_ids"][line_id]
    lines = tubeulator.fetch.line.lines_by_ids(line_id)
    assert [l.model_dump(mode="json") for l in lines] == expected


@mark.parametrize("mode_id,expected", [("tube", snapshot_album["lines_by_modes"])])
def test_lines_by_modes(mode_id, expected):
    lines = tubeulator.fetch.line.lines_by_modes(mode_id)
    assert [l.model_dump(mode="json") for l in lines] == expected
