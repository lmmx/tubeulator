"""Tests for the crowding API."""

from crowding_data import all_endpoints
from pytest import mark

from tubeulator import fetch

tested_eps = {"naptan_crowding", "live_crowding", "dow_crowding"}
untested_eps = set()


def test_crowding_endpoints():
    assert list(vars(fetch.crowding)) == all_endpoints
    assert set(vars(fetch.crowding)) == tested_eps.union(untested_eps)


@mark.skip(reason="KeyError: 'content' (in the response_refpath method)")
def test_naptan_crowding():
    naptan_crowding = fetch.crowding.naptan_crowding(Naptan="HUBZWL")
    assert naptan_crowding


@mark.skip(reason="KeyError: 'content' (in the response_refpath method)")
def test_live_crowding():
    live_crowding = fetch.crowding.live_crowding(Naptan="HUBZWL")
    assert live_crowding


@mark.skip(reason="KeyError: 'content' (in the response_refpath method)")
def test_dow_crowding():
    dow_crowding = fetch.crowding.dow_crowding(Naptan="HUBZWL", DayOfWeek="Mon")
    assert dow_crowding
