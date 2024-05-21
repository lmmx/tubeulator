"""Accessed via dynamic method resolution under `tubeulator.fetch.journey`."""

from .types import RouteEnum


class JourneyEndpointRoutes(RouteEnum):
    forward_requests = "/*"
    """Forwards any remaining requests to the back-end"""
    journey_results = "/JourneyResults/{from}/to/{to}"
    """Perform a Journey Planner search from the parameters specified in simple types"""
    modes = "/Meta/Modes"
    """Gets a list of all of the available journey planner modes"""
