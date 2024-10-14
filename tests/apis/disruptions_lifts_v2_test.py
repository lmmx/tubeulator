"""Tests for the disruptions_lifts_v2 API."""

from disruptions_lifts_v2_data import all_endpoints
from pytest import mark

from tubeulator import fetch

tested_eps = set()
untested_eps = {"all"}


def test_disruptions_lifts_v2_endpoints():
    assert list(vars(fetch.disruptions_lifts_v2)) == all_endpoints
    assert set(vars(fetch.disruptions_lifts_v2)) == tested_eps.union(
        untested_eps,
    )


@mark.skip(reason="404")
def test_disruptions_lifts_v2():
    disruptions = fetch.disruptions_lifts_v2.all()
    assert disruptions
