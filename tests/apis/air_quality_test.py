"""Tests for the air_quality API."""

from air_quality_data import all_endpoints
from tubeulator import fetch

tested_eps = {}
untested_eps = {}


def test_air_quality_endpoints():
    assert list(vars(fetch.air_quality)) == all_endpoints
    assert set(vars(fetch.air_quality)) == tested_eps.union(untested_eps)
