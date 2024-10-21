"""Tests for the vehicle API."""

from pytest import mark
from vehicle_data import all_endpoints

from tubeulator import fetch

tested_eps = {"vehicle_arrivals"}
untested_eps = {"emission_surcharge", "ulez_compliance"}


def test_vehicle_endpoints():
    assert list(vars(fetch.vehicle)) == all_endpoints
    assert set(vars(fetch.vehicle)) == tested_eps.union(untested_eps)


@mark.skip(reason="404 (endpoint not found)?")
def test_emission_surcharge():
    emission_surcharge = fetch.vehicle.emission_surcharge()
    assert emission_surcharge


@mark.skip(reason="404 (endpoint not found)?")
def test_ulez_compliance():
    ulez_compliance = fetch.vehicle.ulez_compliance()
    assert ulez_compliance


def test_vehicle_arrivals():
    vehicle_arrivals = fetch.vehicle.vehicle_arrivals(ids="100")
    assert vehicle_arrivals
