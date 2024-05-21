"""Accessed via dynamic method resolution under `tubeulator.fetch.line`.

!!! example "Example: `tubeulator.fetch.line.meta_modes()`"

    ```py
    >>> modes = fetch.line.meta_modes()
    >>> modes[0]
    Mode(IsTflService=True, IsFarePaying=True, IsScheduledService=True, ModeName='bus')
    ```
"""

from .types import RouteEnum


class LineEndpointRoutes(RouteEnum):
    forward_requests = "/*"
    """Forwards any remaining requests to the back-end"""
    meta_disruption_categories = "/Meta/DisruptionCategories"
    """Gets a list of valid disruption categories"""
    meta_modes = "/Meta/Modes"
    """Gets a list of valid modes"""
    meta_service_types = "/Meta/ServiceTypes"
    """Gets a list of valid ServiceTypes to filter on"""
    meta_severity = "/Meta/Severity"
    """Gets a list of valid severity codes"""
    lines_by_modes = "/Mode/{modes}"
    """Gets lines that serve the given modes."""
    disruption_by_modes = "/Mode/{modes}/Disruption"
    """Get disruptions for all lines of the given modes."""
    route_by_modes = "/Mode/{modes}/Route"
    """Gets all lines and their valid routes for given modes, including the name and id of
    the originating and terminating stops for each route"""
    status_by_modes = "/Mode/{modes}/Status"
    """Gets the line status of for all lines for the given modes"""
    all_routes = "/Route"
    """Get all valid routes for all lines, including the name and id of the originating and
    terminating stops for each route."""
    search_lines_routes = "/Search/{query}"
    """Search for lines or routes matching the query string"""
    status_by_severity = "/Status/{severity}"
    """Gets the line status for all lines with a given severity. A list of valid severity
    codes can be obtained from a call to Line/Meta/Severity"""
    lines_by_ids = "/{ids}"
    """Gets lines that match the specified line ids."""
    arrivals_by_ids = "/{ids}/Arrivals"
    """Get the list of arrival predictions for given line ids based at the given stop"""
    arrivals_by_ids_stop = "/{ids}/Arrivals/{stopPointId}"
    """Get the list of arrival predictions for given line ids based at the given stop"""
    disruption_by_ids = "/{ids}/Disruption"
    """Get disruptions for the given line ids"""
    route_by_ids = "/{ids}/Route"
    """Get all valid routes for given line ids, including the name and id of the
    originating and terminating stops for each route."""
    status_by_ids = "/{ids}/Status"
    """Gets the line status of for given line ids e.g Minor Delays"""
    status_by_ids_dates = "/{ids}/Status/{startDate}/to/{endDate}"
    """Gets the line status for given line ids during the provided dates e.g Minor Delays"""
    route_sequence_by_id_direction = "/{id}/Route/Sequence/{direction}"
    """Gets all valid routes for given line id, including the sequence of stops on each
    route."""
    stop_points_by_id = "/{id}/StopPoints"
    """Gets a list of the stations that serve the given line id"""
    timetable_by_id_from_stop = "/{id}/Timetable/{fromStopPointId}"
    """Gets the timetable for a specified station on the give line"""
    timetable_by_id_from_to_stop = (
        "/{id}/Timetable/{fromStopPointId}/to/{toStopPointId}"
    )
    """Gets the timetable for a specified station on the give line with specified
    destination"""
