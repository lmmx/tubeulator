"""Tests for the road API."""

from datetime import datetime, timedelta

from pytest import mark
from road_data import all_endpoints

from tubeulator import fetch

tested_eps = {
    "all_roads",
    "meta_categories",
    "meta_severities",
    "disruption_by_ids",
    "street_disruption",
    "road_by_ids",
    "road_disruption",
    "road_status",
}
untested_eps = set()


def test_road_endpoints():
    assert list(vars(fetch.road)) == all_endpoints
    assert set(vars(fetch.road)) == tested_eps.union(untested_eps)


def test_all_roads():
    all_roads = fetch.road.all_roads()
    assert all_roads


def test_meta_categories():
    meta_categories = fetch.road.meta_categories()
    assert meta_categories


def test_meta_severities():
    meta_severities = fetch.road.meta_severities()
    assert meta_severities


def test_disruption_by_ids():
    """Incident from website, may not be able to keep it?

    20th May 2024: https://tfl.gov.uk/traffic/status/?disruptionIds=TIMS-198697
    """
    disruption_by_ids = fetch.road.disruption_by_ids(disruptionIds="TIMS-198697")
    assert disruption_by_ids


@mark.skip(
    reason="404",
)
def test_street_disruption():
    street_disruption = fetch.road.street_disruption()
    assert street_disruption


@mark.skip(
    reason="Prevented from sending by self.invalidate call (optional parameters)",
)
def test_street_disruption_date_range():
    now = datetime.now()
    start = (now + timedelta(days=-7)).strftime("%Y-%m-%dT%H:%M:%S-00:00")
    end = (now + timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%S-00:00")
    street_disruption = fetch.road.street_disruption(
        startDate=start,
        endDate=end,
    )
    assert street_disruption


def test_road_by_ids():
    road_by_ids = fetch.road.road_by_ids(ids="A1")
    assert road_by_ids


def test_road_disruption():
    road_disruption = fetch.road.road_disruption(ids="A1")
    for disruption in road_disruption:
        assert disruption


def test_road_status():
    road_status = fetch.road.road_status(ids="A1")
    assert road_status
