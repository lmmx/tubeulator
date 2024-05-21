"""Accessed via dispatch method under `tubeulator.fetch.road`."""
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
