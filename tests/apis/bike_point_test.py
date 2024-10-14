"""Tests for the bike_point API."""

from bike_point_data import all_endpoints
from pytest import mark

from tubeulator import fetch

tested_eps = {"all_locations", "bike_point_by_id"}
untested_eps = {"search_stations"}


def test_bike_point_endpoints():
    assert list(vars(fetch.bike_point)) == all_endpoints
    assert set(vars(fetch.bike_point)) == tested_eps.union(untested_eps)


def test_all_locations():
    all_locations = fetch.bike_point.all_locations()
    assert all_locations


@mark.skip(reason="404 (endpoint not found)?")
def test_search_stations():
    search_stations = fetch.bike_point.search_stations()
    assert search_stations


def test_bike_point_by_id():
    bike_point_by_id = fetch.bike_point.bike_point_by_id(id="BikePoints_100")
    assert bike_point_by_id
