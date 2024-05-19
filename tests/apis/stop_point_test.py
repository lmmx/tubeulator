"""Tests for the stop_point API."""

from stop_point_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_stop_point_endpoints():
    assert list(vars(fetch.stop_point)) == all_endpoints
    assert set(vars(fetch.stop_point)) == tested_eps.union(untested_eps)
