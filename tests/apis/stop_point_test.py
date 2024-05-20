"""Tests for the stop_point API."""

from stop_point_data import all_endpoints
from tubeulator import fetch

tested_eps = set()
untested_eps = {
    "within_radius",
    "forward_requests",
    "meta_categories",
    "meta_modes",
    "meta_stop_types",
    "mode",
    "mode_disruption",
    "search",
    "search_query",
    "service_types",
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
    "car_parks",
    "taxi_ranks",
}


def test_stop_point_endpoints():
    assert list(vars(fetch.stop_point)) == all_endpoints
    assert set(vars(fetch.stop_point)) == tested_eps.union(untested_eps)
