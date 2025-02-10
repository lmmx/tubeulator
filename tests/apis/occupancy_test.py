"""Tests for the occupancy API."""

from occupancy_data import all_endpoints
from pytest import mark

from tubeulator import fetch

tested_eps = {
    "bike_points",
    "charge_connector",
    "charge_connector_ids",
}
untested_eps = {
    "car_park",
    "car_park_id",
}


def test_occupancy_endpoints():
    assert list(vars(fetch.occupancy)) == all_endpoints
    assert set(vars(fetch.occupancy)) == tested_eps.union(untested_eps)


def test_bike_points():
    bike_points = fetch.occupancy.bike_points(ids="BikePoints_100")
    assert bike_points


@mark.skip(reason="500: Internal server error")
def test_car_park():
    car_park = fetch.occupancy.car_park()
    assert car_park


@mark.skip(reason="500: Internal server error")
def test_car_park_id():
    car_park_id = fetch.occupancy.car_park_id(id="CarParks_800503")
    assert car_park_id


def test_charge_connector():
    charge_connector = fetch.occupancy.charge_connector()
    assert charge_connector


def test_charge_connector_ids():
    charge_connector_ids = fetch.occupancy.charge_connector_ids(
        ids="ChargePointCM-BPT62200886-143260",
    )
    assert charge_connector_ids
