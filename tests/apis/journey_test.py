"""Tests for the journey API."""

from journey_data import all_endpoints
from tubeulator import fetch

tested_eps = set()
untested_eps = {"forward_requests", "journey_results", "modes"}


def test_journey_endpoints():
    assert list(vars(fetch.journey)) == all_endpoints
    assert set(vars(fetch.journey)) == tested_eps.union(untested_eps)
