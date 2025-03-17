"""Tests for the stop_point API."""

from inline_snapshot import snapshot
from pytest import mark, raises
from stop_point_data import all_endpoints

from tubeulator import fetch
from tubeulator.exc import RequestError

tested_eps = {
    "search_query",
    "sms_id",
}
untested_eps = {
    "mode",
    "mode_disruption",
    "type",
    "type_page",
    "stop_point_ids",
    "stop_point_disruption",
    "arrival_departures",
    "arrivals",
    "can_reach_on_line",
    "crowding",
    "direction_to",
    "route",
    "place_types",
    "forward_requests",
    "search",
    "service_types",
    "within_radius",
    "meta_categories",
    "meta_modes",
    "meta_stop_types",
    "car_parks",
    "taxi_ranks",
}


def test_stop_point_endpoints():
    assert list(vars(fetch.stop_point)) == all_endpoints
    assert set(vars(fetch.stop_point)) == tested_eps.union(untested_eps)


@mark.skip(reason="404 (endpoint not found)?")
def test_within_radius():
    within_radius = fetch.stop_point.within_radius()
    assert within_radius


@mark.skip(reason="404 (endpoint not found)?")
def test_forward_requests():
    forward_requests = fetch.stop_point.forward_requests()
    assert forward_requests


def test_meta_categories():
    meta_categories = fetch.stop_point.meta_categories()
    assert meta_categories


def test_meta_modes():
    meta_modes = fetch.stop_point.meta_modes()
    assert meta_modes


def test_meta_stop_types():
    meta_stop_types = fetch.stop_point.meta_stop_types()
    assert meta_stop_types


@mark.skip(
    reason="Times out (big and slow?), 'bus' mode is rejected without pagination",
)
def test_mode():
    mode = fetch.stop_point.mode(modes="tube")
    assert mode


def test_mode_disruption():
    mode_disruption = fetch.stop_point.mode_disruption(modes="overground")
    assert mode_disruption


@mark.skip(reason="404 (endpoint not found)?")
def test_search():
    search = fetch.stop_point.search()
    assert search


@mark.parametrize(
    "query_input,result_size",
    [("Bromley-By-Bow", 1), ("Euston", snapshot(6))],
)
def test_search_query(query_input, result_size):
    search_query = fetch.stop_point.search_query(query=query_input)
    assert search_query.Total == result_size


@mark.skip(reason="Returns a HTTP error")
def test_service_types():
    service_types = fetch.stop_point.service_types()
    assert service_types


def test_sms_id():
    """Returns a 302 (redirect)"""
    with raises(RequestError):
        fetch.stop_point.sms_id(id=73241)


def test_type():
    type = fetch.stop_point.type(types="TransportInterchange")
    assert type


def test_type_page():
    type_page = fetch.stop_point.type_page(types="TransportInterchange", page=1)
    assert type_page


def test_stop_point_ids():
    stop_point_ids = fetch.stop_point.stop_point_ids(ids="HUBWAT")
    assert stop_point_ids


def test_stop_point_disruption():
    stop_point_disruption = fetch.stop_point.stop_point_disruption(ids="HUBWAT")
    for disruption in stop_point_disruption:
        assert disruption


@mark.skip(reason="Says lineIds is not in endpoint signature but schema shows it is")
def test_arrival_departures():
    arrival_departures = fetch.stop_point.arrival_departures(
        id="HUBWAT",
        lineIds="tfl-rail",
    )
    assert arrival_departures


def test_arrivals():
    arrivals = fetch.stop_point.arrivals(id="HUBWAT")
    for arrival in arrivals:
        assert arrival


@mark.skip(
    reason="Non-bool status: 'Unknown'. Should be enum not bool? Schema line 2214",
)
def test_can_reach_on_line():
    can_reach_on_line = fetch.stop_point.can_reach_on_line(
        id="940GZZLUASL",
        lineId="Piccadilly",
    )
    assert can_reach_on_line


@mark.skip(reason="404 (endpoint not found)?")
def test_crowding():
    crowding = fetch.stop_point.crowding(id="940GZZLUASL", line="Piccadilly")
    assert crowding


def test_direction_to():
    direction_to = fetch.stop_point.direction_to(
        id="940GZZLUASL",
        toStopPointId="940GZZLUHWY",
    )
    assert direction_to


def test_route():
    route = fetch.stop_point.route(id="940GZZLUASL")
    assert route


@mark.skip(reason="404 (endpoint not found)?")
def test_place_types():
    place_types = fetch.stop_point.place_types(id="940GZZLUASL")
    assert place_types


def test_car_parks():
    car_parks = fetch.stop_point.car_parks(stopPointId="HUBWAT")
    for parking in car_parks:
        assert parking


def test_taxi_ranks():
    taxi_ranks = fetch.stop_point.taxi_ranks(stopPointId="HUBWAT")
    for taxis in taxi_ranks:
        assert taxis
