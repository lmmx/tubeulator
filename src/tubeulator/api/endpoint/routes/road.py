"""Accessed via dynamic method resolution under `tubeulator.fetch.road`.

!!! example "Example: `tubeulator.fetch.road.meta_modes()`"

    ```py
    >>> road_by_ids = fetch.road.road_by_ids(ids="A1")
    >>> print(road_by_ids[0].model_dump_json(indent=2))
    {
      "Id": "a1",
      "DisplayName": "A1",
      "Group": null,
      "StatusSeverity": "Good",
      "StatusSeverityDescription": "No Exceptional Delays",
      "Bounds": "[[-0.25616,51.5319],[-0.10234,51.6562]]",
      "Envelope": "[[-0.25616,51.5319],[-0.25616,51.6562],[-0.10234,51.6562],[-0.10234,51.5319],[-0.25616,51.5319]]",
      "StatusAggregationStartDate": null,
      "StatusAggregationEndDate": null,
      "Url": "/Road/a1"
    }
    ```
"""

from .types import RouteEnum


class RoadEndpointRoutes(RouteEnum):
    all_roads = "/"
    """Gets all roads managed by TfL"""
    meta_categories = "/Meta/Categories"
    """Gets a list of valid RoadDisruption categories"""
    meta_severities = "/Meta/Severities"
    """Gets a list of valid RoadDisruption severity codes"""
    disruption_by_ids = "/all/Disruption/{disruptionIds}"
    """Gets a list of active disruptions filtered by disruption Ids."""
    street_disruption = "/all/Street/Disruption"
    """Gets a list of disrupted streets. If no date filters are provided, current
    disruptions are returned."""
    road_by_ids = "/{ids}"
    """Gets the road with the specified id (e.g. A1)"""
    road_disruption = "/{ids}/Disruption"
    """Get active disruptions, filtered by road ids"""
    road_status = "/{ids}/Status"
    """Gets the specified roads with the status aggregated over the date range
    specified, or now until the end of today if no dates are passed."""
