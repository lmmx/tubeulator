"""Tests for the mode API."""

from mode_data import all_endpoints

from tubeulator import fetch

tested_eps = {"active_service_types", "mode_arrivals"}
untested_eps = set()


def test_mode_endpoints():
    assert list(vars(fetch.mode)) == all_endpoints
    assert set(vars(fetch.mode)) == tested_eps.union(untested_eps)


def test_active_service_types():
    active_service_types = fetch.mode.active_service_types()
    assert active_service_types


def test_mode_arrivals():
    mode_arrivals = fetch.mode.mode_arrivals(mode="tube")
    assert mode_arrivals
