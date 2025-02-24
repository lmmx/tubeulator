"""Tests for the accident_stats API."""

from accident_stats_data import all_endpoints
from pytest import mark

from tubeulator import fetch

tested_eps = {"year_accidents"}
untested_eps = set()


def test_accident_stats_endpoints():
    assert list(vars(fetch.accident_stats)) == all_endpoints
    assert set(vars(fetch.accident_stats)) == tested_eps.union(untested_eps)


@mark.skip(reason="There are 50,626 results for 2019, then none for subsequent years")
def test_year_accidents():
    year_accidents = fetch.accident_stats.year_accidents(year=2019)
    assert year_accidents
