"""Tests for the occupancy API."""

from occupancy_data import all_endpoints
from tubeulator import fetch

tested_eps = set()
untested_eps = {
    "bike_points",
    "car_park",
    "car_park_id",
    "charge_connector",
    "charge_connector_ids",
}


def test_occupancy_endpoints():
    assert list(vars(fetch.occupancy)) == all_endpoints
    assert set(vars(fetch.occupancy)) == tested_eps.union(untested_eps)
