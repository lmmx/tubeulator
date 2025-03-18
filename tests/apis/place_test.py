"""Tests for the place API."""

from place_data import all_endpoints
from pytest import mark

from tubeulator import fetch

tested_eps = {
    "meta_categories",
    "places_by_type",
    "place_by_id",
}
untested_eps = {
    "forward_requests",
    "places_by_geo_region",
    "meta_place_types",
    "place_by_type_at_coordinates",
    "search_places",
}


def test_place_endpoints():
    assert list(vars(fetch.place)) == all_endpoints
    assert set(vars(fetch.place)) == tested_eps.union(untested_eps)


@mark.skip(reason="404 (endpoint not found)?")
def test_places_by_geo_region():
    places_by_geo_region = fetch.place.places_by_geo_region()
    assert places_by_geo_region


def test_meta_categories():
    meta_categories = fetch.place.meta_categories()
    assert meta_categories


@mark.skip(reason="Receives list of strings but expects objects")
def test_meta_place_types():
    meta_place_types = fetch.place.meta_place_types()
    assert meta_place_types


@mark.skip(reason="404 (endpoint not found)?")
def test_search_places():
    search_places = fetch.place.search_places()
    assert search_places


@mark.parametrize("place_type", ["CarPark", "BikePoint", "ChargeConnector"])
def test_places_by_type(place_type):
    places_by_type = fetch.place.places_by_type(types=place_type)
    assert places_by_type


def test_place_by_id():
    place_by_id = fetch.place.place_by_id(id="CarParks_800503")
    assert place_by_id


@mark.skip(reason="Value is returned empty, despite coming from places_by_type result.")
def test_place_by_type_at_coordinates():
    """Car parks near Morden Station."""
    place = fetch.place.place_by_type_at_coordinates(
        type="CarPark",
        lat="51.404413",
        lon="-0.194517",
    )
    assert place
