"""Tests for the mode API."""

from mode_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_mode_endpoints():
    assert list(vars(fetch.mode)) == all_endpoints
    assert set(vars(fetch.mode)) == tested_eps.union(untested_eps)
