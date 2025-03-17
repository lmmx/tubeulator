"""Tests for the line API."""

from datetime import datetime, timedelta

from line_data import all_endpoints, snapshot_album
from pytest import mark

from tubeulator import fetch

tested_eps = {
    "all_routes",
    "arrivals_by_ids",
    "arrivals_by_ids_stop",
    "disruption_by_ids",
    "disruption_by_modes",
    "lines_by_ids",
    "lines_by_modes",
    "meta_disruption_categories",
    "meta_modes",
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
untested_eps = {
    "forward_requests",
}


def test_line_endpoints():
    assert list(vars(fetch.line)) == all_endpoints
    assert set(vars(fetch.line)) == tested_eps.union(untested_eps)


def test_arrivals_by_ids():
    arrivals_by_ids = fetch.line.arrivals_by_ids(ids="waterloo-city")
    for arrival in arrivals_by_ids:
        assert arrival


def test_all_routes():
    all_routes = fetch.line.all_routes()
    assert all_routes


def test_arrivals_by_ids_stop():
    arrivals_by_ids_stop = fetch.line.arrivals_by_ids_stop(
        ids="waterloo-city",
        stopPointId="940GZZLUASL",
    )
    for arrival in arrivals_by_ids_stop:
        assert arrival


def test_disruption_by_ids():
    disruption_by_ids = fetch.line.disruption_by_ids(ids="waterloo-city")
    for disruption in disruption_by_ids:
        assert disruption


def test_disruption_by_modes():
    disruption_by_modes = fetch.line.disruption_by_modes(modes="tube")
    assert disruption_by_modes


@mark.skip()
def test_forward_requests():
    forward_requests = fetch.line.forward_requests()
    assert forward_requests


def test_meta_disruption_categories():
    meta_disruption_categories = fetch.line.meta_disruption_categories()
    assert meta_disruption_categories


def test_meta_service_types():
    meta_service_types = fetch.line.meta_service_types()
    assert meta_service_types


def test_meta_severity():
    meta_severity = fetch.line.meta_severity()
    assert meta_severity


def test_route_by_ids():
    route_by_ids = fetch.line.route_by_ids(ids="waterloo-city")
    assert route_by_ids


def test_route_by_modes():
    route_by_modes = fetch.line.route_by_modes(modes="tube")
    assert route_by_modes


def test_route_sequence_by_id_direction():
    route_sequence_by_id_direction = fetch.line.route_sequence_by_id_direction(
        id="waterloo-city",
        direction="outbound",
    )
    assert route_sequence_by_id_direction


def test_search_lines_routes():
    search_lines_routes = fetch.line.search_lines_routes(query="Downing Street")
    assert search_lines_routes


def test_status_by_ids():
    status_by_ids = fetch.line.status_by_ids(ids="waterloo-city")
    assert status_by_ids


def test_status_by_ids_dates():
    now = datetime.now()
    start = (now + timedelta(days=6)).strftime("%Y-%m-%dT%H:%M:%S-00:00")
    end = (now + timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S-00:00")
    status_by_ids_dates = fetch.line.status_by_ids_dates(
        ids="waterloo-city",
        startDate=start,
        endDate=end,
    )
    assert status_by_ids_dates


def test_status_by_modes():
    status_by_modes = fetch.line.status_by_modes(modes="tube")
    assert status_by_modes


def test_status_by_severity():
    status_by_severity = fetch.line.status_by_severity(severity=0)
    assert status_by_severity


def test_stop_points_by_id():
    stop_points_by_id = fetch.line.stop_points_by_id(id="waterloo-city")
    assert stop_points_by_id


def test_timetable_by_id_from_stop():
    timetable_by_id_from_stop = fetch.line.timetable_by_id_from_stop(
        id="piccadilly",
        fromStopPointId="940GZZLUASL",
    )
    assert timetable_by_id_from_stop


def test_timetable_by_id_from_to_stop():
    """Arsenal to Piccadilly Circus, via Piccadilly line."""
    timetable_by_id_from_to_stop = fetch.line.timetable_by_id_from_to_stop(
        id="piccadilly",
        fromStopPointId="940GZZLUASL",
        toStopPointId="940GZZLUPCC",
    )
    assert timetable_by_id_from_to_stop


@mark.parametrize("expected", [snapshot_album["meta_modes"]])
def test_meta_modes(expected):
    modes = fetch.line.meta_modes()
    assert [m.model_dump(mode="json") for m in modes] == expected


@mark.parametrize("line_id", ["waterloo-city"])
def test_lines_by_ids(line_id):
    """Relies on correct codegen of arrays (previously had a bug)."""
    expected = snapshot_album["lines_by_ids"][line_id]
    lines = fetch.line.lines_by_ids(line_id)
    assert [l.model_dump(mode="json") for l in lines] == expected


@mark.parametrize("mode_id,expected", [("tube", snapshot_album["lines_by_modes"])])
def test_lines_by_modes(mode_id, expected):
    lines = fetch.line.lines_by_modes(mode_id)
    assert [l.model_dump(mode="json") for l in lines] == expected
