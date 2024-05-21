"""Accessed via dynamic method resolution under `tubeulator.fetch.air_quality_data`."""
from .types import RouteEnum


class AirQualityEndpointRoutes(RouteEnum):
    air_quality_data = "/"
    """Gets air quality data feed"""
