from .types import RouteEnum


class BikePointEndpointRoutes(RouteEnum):
    ALL_LOCATIONS = "/"
    """Gets all bike point locations. The Place object has an addtionalProperties array
    which contains the nbBikes, nbDocks and nbSpaces numbers which give the status of
    the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) != 0
    indicates broken docks."""
    SEARCH_STATIONS = "/Search"
    """Search for bike stations by their name, a bike point's name often contains
    information about the name of the street or nearby landmarks, for example. Note that the
    search result does not contain the PlaceProperties i.e. the status or occupancy of the
    BikePoint, to get that information you should retrieve the BikePoint by its id on
    '/BikePoint/id."""
    BIKE_POINT_BY_ID = "/{id}"
    """Gets the bike point with the given id."""
