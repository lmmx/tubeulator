"""Accessed via dynamic method resolution under `tubeulator.fetch.air_quality_data`.

!!! example "Example: `tubeulator.fetch.air_quality.air_quality_data()`"

    This API doesn't seem to be working...

    ```py
    >>> data = fetch.air_quality.air_quality_data()
    >>> data
    Object()
    ```
"""

from .types import RouteEnum


class AirQualityEndpointRoutes(RouteEnum):
    air_quality_data = "/"
    """Gets air quality data feed"""
