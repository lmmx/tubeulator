"""Tests for the search API."""

from search_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_search_endpoints():
    assert list(vars(fetch.search)) == all_endpoints
    assert set(vars(fetch.search)) == tested_eps.union(untested_eps)
