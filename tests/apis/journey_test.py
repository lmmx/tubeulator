"""Tests for the journey API."""

from journey_data import all_endpoints

from tubeulator import fetch

tested_eps = {"journey_results", "modes"}
untested_eps = {"forward_requests"}


def test_journey_endpoints():
    assert list(vars(fetch.journey)) == all_endpoints
    assert set(vars(fetch.journey)) == tested_eps.union(untested_eps)


def test_journey_results():
    journey_results = fetch.journey.journey_results(
        **{"from": "Tooting Bec Underground", "to": "Tooting Broadway Underground"},
    )
    assert journey_results


def test_modes():
    modes = fetch.journey.modes()
    assert modes
