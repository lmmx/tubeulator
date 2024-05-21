"""Accessed via dynamic method resolution under `tubeulator.fetch.disruption_lifts`.

!!! example "Example: `fetch.disruptions_lifts_v2.all()`"

    Somewhat ironically, the lift disruptions API is out of order (eturns a 404 when called).

    ```py
    >>> disruptions = fetch.disruptions_lifts_v2.all()
    ```
"""

from .types import RouteEnum


class DisruptionsLiftsEndpointRoutes(RouteEnum):
    all = "/"
    """List of all currently disrupted lift routes"""
