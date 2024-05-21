"""Accessed via dynamic method resolution under `tubeulator.fetch.place`.

!!! example "Example: `tubeulator.fetch.place.meta_categories()`"

    Unfortunately most of these methods don't work. This one isn't much use on its own:

    ```py
    >>> categories = fetch.place.meta_categories()
    >>> print(categories[11].model_dump_json(indent=2))
    {
      "Category": "Load",
      "AvailableKeys": [
        "Pallets/bagged",
        "Liquids/gas",
        "Containers",
        "Bulks",
        "General Cargo",
        "Can accommodate a crane"
      ]
    }
    ```
"""

from .types import RouteEnum


class PlaceEndpointRoutes(RouteEnum):
    places_by_geo_region = "/"
    """Gets the places that lie within a geographic region. The geographic region of interest can either
    be specified by using a lat/lon geo-point and a radius in metres to return places within the locus
    defined by the lat/lon of its centre or alternatively, by the use of a bounding box defined by the
    lat/lon of its north-west and south-east corners. Optionally filters on type and can strip
    properties for a smaller payload."""
    forward_requests = "/*"
    """Forwards any remaining requests to the back-end"""
    meta_categories = "/Meta/Categories"
    """Gets a list of all of the available place property categories and keys."""
    meta_place_types = "/Meta/PlaceTypes"
    """Gets a list of the available types of Place."""
    search_places = "/Search"
    """Gets all places that matches the given query"""
    places_by_type = "/Type/{types}"
    """Gets all places of a given type"""
    place_by_id = "/{id}"
    """Gets the place with the given id."""
    place_by_type_at_coordinates = "/{type}/At/{lat}/{lon}"
    """Gets any places of the given type whose geography intersects the given latitude and longitude. In
    practice this means the Place must be polygonal e.g. a BoroughBoundary."""
