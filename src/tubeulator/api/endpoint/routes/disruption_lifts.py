"""Accessed via dynamic method resolution under `tubeulator.fetch.disruption_lifts`."""

from .types import RouteEnum


class DisruptionsLiftsEndpointRoutes(RouteEnum):
    all = "/"
    """List of all currently disrupted lift routes"""
