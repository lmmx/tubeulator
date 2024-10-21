"""Tests for the air_quality API."""

from air_quality_data import all_endpoints
from pytest import mark

from tubeulator import fetch

tested_eps = {"air_quality_data"}
untested_eps = set()


def test_air_quality_endpoints():
    assert list(vars(fetch.air_quality)) == all_endpoints
    assert set(vars(fetch.air_quality)) == tested_eps.union(untested_eps)


@mark.skip(reason="Returns an empty Object")
def test_air_quality_data():
    air_quality_data = fetch.air_quality.air_quality_data()
    assert air_quality_data.model_dump()
