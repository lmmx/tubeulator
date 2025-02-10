"""Tests for the search API."""

from pytest import mark
from search_data import all_endpoints

from tubeulator import fetch

tested_eps = {
    "search",
    "meta_categories",
    "meta_search_providers",
    "meta_sorts",
}
untested_eps = {
    "bus_schedules",
}


def test_search_endpoints():
    assert list(vars(fetch.search)) == all_endpoints
    assert set(vars(fetch.search)) == tested_eps.union(untested_eps)


@mark.skip(reason="Not sure how to call this one?")
def test_search():
    search = fetch.search.search()
    assert search


@mark.skip(reason="check_vars_supplied invalidates the optional argument 'query'.")
def test_bus_schedules():
    bus_schedules = fetch.search.bus_schedules(query="Canning Town")
    assert bus_schedules


def test_meta_categories():
    meta_categories = fetch.search.meta_categories()
    assert meta_categories


def test_meta_search_providers():
    meta_search_providers = fetch.search.meta_search_providers()
    assert meta_search_providers


def test_meta_sorts():
    meta_sorts = fetch.search.meta_sorts()
    assert meta_sorts
