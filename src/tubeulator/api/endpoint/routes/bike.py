"""Accessed via dynamic method resolution under `tubeulator.fetch.bike`."""

from .types import RouteEnum


class BikePointEndpointRoutes(RouteEnum):
    all_locations = "/"
    """Gets all bike point locations. The Place object has an addtionalProperties array
    which contains the nbBikes, nbDocks and nbSpaces numbers which give the status of
    the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) != 0
    indicates broken docks."""
    search_stations = "/Search"
    """Search for bike stations by their name, a bike point's name often contains
    information about the name of the street or nearby landmarks, for example. Note that the
    search result does not contain the PlaceProperties i.e. the status or occupancy of the
    BikePoint, to get that information you should retrieve the BikePoint by its id on
    '/BikePoint/id."""
    bike_point_by_id = "/{id}"
    """Gets the bike point with the given id."""
