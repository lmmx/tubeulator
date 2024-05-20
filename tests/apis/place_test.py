"""Tests for the place API."""

from place_data import all_endpoints
from tubeulator import fetch

tested_eps = set()
untested_eps = {
    "places_by_geo_region",
    "forward_requests",
    "meta_categories",
    "meta_place_types",
    "search_places",
    "places_by_type",
    "place_by_id",
    "place_by_type_at_coordinates",
}


def test_place_endpoints():
    assert list(vars(fetch.place)) == all_endpoints
    assert set(vars(fetch.place)) == tested_eps.union(untested_eps)
