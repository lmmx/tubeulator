"""Tests for the road API."""

from road_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_road_endpoints():
    assert list(vars(fetch.road)) == all_endpoints
    assert set(vars(fetch.road)) == tested_eps.union(untested_eps)
