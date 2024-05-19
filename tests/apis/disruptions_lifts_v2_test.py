"""Tests for the disruptions_lifts_v2 API."""

from disruptions_lifts_v2_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_disruptions_lifts_v2_endpoints():
    assert list(vars(fetch.disruptions_lifts_v2)) == all_endpoints
    assert set(vars(fetch.disruptions_lifts_v2)) == tested_eps.union(
        untested_eps,
    )
