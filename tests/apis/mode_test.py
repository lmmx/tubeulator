"""Tests for the mode API."""

from mode_data import all_endpoints
from tubeulator import fetch

tested_eps = set()
untested_eps = {"active_service_types", "mode_arrivals"}


def test_mode_endpoints():
    assert list(vars(fetch.mode)) == all_endpoints
    assert set(vars(fetch.mode)) == tested_eps.union(untested_eps)
