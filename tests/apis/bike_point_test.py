"""Tests for the bike_point API."""

from bike_point_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_bike_point_endpoints():
    assert list(vars(fetch.bike_point)) == all_endpoints
    assert set(vars(fetch.bike_point)) == tested_eps.union(untested_eps)
