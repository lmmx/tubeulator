from .types import RouteEnum


class RoadEndpointRoutes(RouteEnum):
    ALL_ROADS = "/"
    """Gets all roads managed by TfL"""
    META_CATEGORIES = "/Meta/Categories"
    """Gets a list of valid RoadDisruption categories"""
    META_SEVERITIES = "/Meta/Severities"
    """Gets a list of valid RoadDisruption severity codes"""
    DISRUPTION_BY_IDS = "/all/Disruption/{disruptionIds}"
    """Gets a list of active disruptions filtered by disruption Ids."""
    STREET_DISRUPTION = "/all/Street/Disruption"
    """Gets a list of disrupted streets. If no date filters are provided, current
    disruptions are returned."""
    ROAD_BY_IDS = "/{ids}"
    """Gets the road with the specified id (e.g. A1)"""
    ROAD_DISRUPTION = "/{ids}/Disruption"
    """Get active disruptions, filtered by road ids"""
    ROAD_STATUS = "/{ids}/Status"
    """Gets the specified roads with the status aggregated over the date range
    specified, or now until the end of today if no dates are passed."""
