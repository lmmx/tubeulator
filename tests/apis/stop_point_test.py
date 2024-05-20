"""Tests for the stop_point API."""

from pytest import mark, raises
from stop_point_data import all_endpoints
from tubeulator import fetch
from tubeulator.exc import RequestError

tested_eps = {
    "mode",
    "mode_disruption",
    "search",
    "search_query",
    "sms_id",
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
}
untested_eps = {
    "forward_requests",
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


@mark.skip(reason="KeyError: '$ref' in response_refpath")
def test_meta_categories():
    meta_categories = fetch.stop_point.meta_categories()
    assert meta_categories


@mark.skip(reason="KeyError: '$ref' in response_refpath")
def test_meta_modes():
    meta_modes = fetch.stop_point.meta_modes()
    assert meta_modes


@mark.skip(reason="KeyError: '$ref' in response_refpath")
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
    mode_disruption = fetch.stop_point.mode_disruption()
    assert mode_disruption


def test_search():
    search = fetch.stop_point.search()
    assert search


def test_search_query():
    search_query = fetch.stop_point.search_query()
    assert search_query


@mark.skip(reason="Returns a HTTP error")
def test_service_types():
    service_types = fetch.stop_point.service_types()
    assert service_types


def test_sms_id():
    """Returns a 302 (redirect)"""
    with raises(RequestError):
        fetch.stop_point.sms_id(id=73241)


def test_type():
    type = fetch.stop_point.type()
    assert type


def test_type_page():
    type_page = fetch.stop_point.type_page()
    assert type_page


def test_stop_point_ids():
    stop_point_ids = fetch.stop_point.stop_point_ids()
    assert stop_point_ids


def test_stop_point_disruption():
    stop_point_disruption = fetch.stop_point.stop_point_disruption()
    assert stop_point_disruption


def test_arrival_departures():
    arrival_departures = fetch.stop_point.arrival_departures()
    assert arrival_departures


def test_arrivals():
    arrivals = fetch.stop_point.arrivals()
    assert arrivals


def test_can_reach_on_line():
    can_reach_on_line = fetch.stop_point.can_reach_on_line()
    assert can_reach_on_line


def test_crowding():
    crowding = fetch.stop_point.crowding()
    assert crowding


def test_direction_to():
    direction_to = fetch.stop_point.direction_to()
    assert direction_to


def test_route():
    route = fetch.stop_point.route()
    assert route


def test_place_types():
    place_types = fetch.stop_point.place_types()
    assert place_types


@mark.skip(reason="KeyError: '$ref' in response_refpath")
def test_car_parks():
    car_parks = fetch.stop_point.car_parks(stopPointId="HUBWAT")
    assert car_parks


@mark.skip(reason="KeyError: '$ref' in response_refpath")
def test_taxi_ranks():
    taxi_ranks = fetch.stop_point.taxi_ranks(stopPointId="HUBWAT")
    assert taxi_ranks
