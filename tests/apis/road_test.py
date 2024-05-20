"""Tests for the road API."""

from road_data import all_endpoints
from tubeulator import fetch

tested_eps = set()
untested_eps = {
    "all_roads",
    "meta_categories",
    "meta_severities",
    "disruption_by_ids",
    "street_disruption",
    "road_by_ids",
    "road_disruption",
    "road_status",
}


def test_road_endpoints():
    assert list(vars(fetch.road)) == all_endpoints
    assert set(vars(fetch.road)) == tested_eps.union(untested_eps)
