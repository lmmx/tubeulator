"""Tests for the crowding API."""

from crowding_data import all_endpoints
from tubeulator import fetch

tested_eps = set()
untested_eps = {"naptan_crowding", "live_crowding", "dow_crowding"}


def test_crowding_endpoints():
    assert list(vars(fetch.crowding)) == all_endpoints
    assert set(vars(fetch.crowding)) == tested_eps.union(untested_eps)
