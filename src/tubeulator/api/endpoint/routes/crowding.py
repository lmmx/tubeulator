"""Accessed via dynamic method resolution under `tubeulator.fetch.crowding`.

!!! example "Example: `tubeulator.fetch.crowding.dow_crowding()`"

    This method isn't working right now, but it's called like this:

    ```py
    >>> dow_crowding = fetch.crowding.dow_crowding(Naptan="HUBZWL", DayOfWeek="Mon")
    ```
"""

from .types import RouteEnum


class CrowdingEndpointRoutes(RouteEnum):
    naptan_crowding = "/{Naptan}"
    """Returns crowding information for Naptan"""
    live_crowding = "/{Naptan}/Live"
    """Returns live crowding information for Naptan"""
    dow_crowding = "/{Naptan}/{DayOfWeek}"
    """Returns crowding information for Naptan for Day of Week"""
