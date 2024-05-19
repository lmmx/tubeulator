"""Tests for the accident_stats API."""

from accident_stats_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_accident_stats_endpoints():
    assert list(vars(fetch.accident_stats)) == all_endpoints
    assert set(vars(fetch.accident_stats)) == tested_eps.union(untested_eps)
