"""Tests for the vehicle API."""

from tubeulator import fetch
from vehicle_data import all_endpoints

tested_eps = set()
untested_eps = {"emission_surcharge", "ulez_compliance", "vehicle_arrivals"}


def test_vehicle_endpoints():
    assert list(vars(fetch.vehicle)) == all_endpoints
    assert set(vars(fetch.vehicle)) == tested_eps.union(untested_eps)
