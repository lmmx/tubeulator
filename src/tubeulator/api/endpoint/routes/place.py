from .types import RouteEnum


class PlaceEndpointRoutes(RouteEnum):
    PLACES_BY_GEO_REGION = "/"
    """Gets the places that lie within a geographic region. The geographic region of interest can either
    be specified by using a lat/lon geo-point and a radius in metres to return places within the locus
    defined by the lat/lon of its centre or alternatively, by the use of a bounding box defined by the
    lat/lon of its north-west and south-east corners. Optionally filters on type and can strip
    properties for a smaller payload."""
    FORWARD_REQUESTS = "/*"
    """Forwards any remaining requests to the back-end"""
    META_CATEGORIES = "/Meta/Categories"
    """Gets a list of all of the available place property categories and keys."""
    META_PLACE_TYPES = "/Meta/PlaceTypes"
    """Gets a list of the available types of Place."""
    SEARCH_PLACES = "/Search"
    """Gets all places that matches the given query"""
    PLACES_BY_TYPE = "/Type/{types}"
    """Gets all places of a given type"""
    PLACE_BY_ID = "/{id}"
    """Gets the place with the given id."""
    PLACE_BY_TYPE_AT_COORDINATES = "/{type}/At/{lat}/{lon}"
    """Gets any places of the given type whose geography intersects the given latitude and longitude. In
    practice this means the Place must be polygonal e.g. a BoroughBoundary."""
