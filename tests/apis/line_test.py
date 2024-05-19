"""Tests for the line API."""

import tubeulator
from line_data import all_endpoints, snapshot_album
from pytest import mark

tested_eps = {
    "lines_by_ids",
    "lines_by_modes",
    "meta_modes",
}
untested_eps = {
    "all_routes",
    "arrivals_by_ids",
    "arrivals_by_ids_stop",
    "disruption_by_ids",
    "disruption_by_modes",
    "forward_requests",
    "meta_disruption_categories",
    "meta_service_types",
    "meta_severity",
    "route_by_ids",
    "route_by_modes",
    "route_sequence_by_id_direction",
    "search_lines_routes",
    "status_by_ids",
    "status_by_ids_dates",
    "status_by_modes",
    "status_by_severity",
    "stop_points_by_id",
    "timetable_by_id_from_stop",
    "timetable_by_id_from_to_stop",
}


def test_line_endpoints():
    assert list(vars(tubeulator.fetch.line)) == all_endpoints
    assert set(vars(tubeulator.fetch.line)) == tested_eps.union(untested_eps)


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
