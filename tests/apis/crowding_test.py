"""Tests for the crowding API."""

from crowding_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_crowding_endpoints():
    assert list(vars(fetch.crowding)) == all_endpoints
    assert set(vars(fetch.crowding)) == tested_eps.union(untested_eps)
