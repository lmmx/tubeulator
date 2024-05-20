"""Tests for the search API."""

from search_data import all_endpoints
from tubeulator import fetch

tested_eps = set()
untested_eps = {
    "search",
    "bus_schedules",
    "meta_categories",
    "meta_search_providers",
    "meta_sorts",
}


def test_search_endpoints():
    assert list(vars(fetch.search)) == all_endpoints
    assert set(vars(fetch.search)) == tested_eps.union(untested_eps)
