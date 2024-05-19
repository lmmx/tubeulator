"""Tests for the occupancy API."""

from occupancy_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_occupancy_endpoints():
    assert list(vars(fetch.occupancy)) == all_endpoints
    assert set(vars(fetch.occupancy)) == tested_eps.union(untested_eps)
