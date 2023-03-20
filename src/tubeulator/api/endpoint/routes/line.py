from .types import RouteEnum


class LineEndpointRoutes(RouteEnum):
    FORWARD_REQUESTS = "/*"
    """Forwards any remaining requests to the back-end"""
    META_DISRUPTION_CATEGORIES = "/Meta/DisruptionCategories"
    """Gets a list of valid disruption categories"""
    META_MODES = "/Meta/Modes"
    """Gets a list of valid modes"""
    META_SERVICE_TYPES = "/Meta/ServiceTypes"
    """Gets a list of valid ServiceTypes to filter on"""
    META_SEVERITY = "/Meta/Severity"
    """Gets a list of valid severity codes"""
    LINES_BY_MODES = "/Mode/{modes}"
    """Gets lines that serve the given modes."""
    DISRUPTION_BY_MODES = "/Mode/{modes}/Disruption"
    """Get disruptions for all lines of the given modes."""
    ROUTE_BY_MODES = "/Mode/{modes}/Route"
    """Gets all lines and their valid routes for given modes, including the name and id of
    the originating and terminating stops for each route"""
    STATUS_BY_MODES = "/Mode/{modes}/Status"
    """Gets the line status of for all lines for the given modes"""
    ALL_ROUTES = "/Route"
    """Get all valid routes for all lines, including the name and id of the originating and
    terminating stops for each route."""
    SEARCH_LINES_ROUTES = "/Search/{query}"
    """Search for lines or routes matching the query string"""
    STATUS_BY_SEVERITY = "/Status/{severity}"
    """Gets the line status for all lines with a given severity. A list of valid severity
    codes can be obtained from a call to Line/Meta/Severity"""
    LINES_BY_IDS = "/{ids}"
    """Gets lines that match the specified line ids."""
    ARRIVALS_BY_IDS = "/{ids}/Arrivals"
    """Get the list of arrival predictions for given line ids based at the given stop"""
    ARRIVALS_BY_IDS_STOP = "/{ids}/Arrivals/{stopPointId}"
    """Get the list of arrival predictions for given line ids based at the given stop"""
    DISRUPTION_BY_IDS = "/{ids}/Disruption"
    """Get disruptions for the given line ids"""
    ROUTE_BY_IDS = "/{ids}/Route"
    """Get all valid routes for given line ids, including the name and id of the
    originating and terminating stops for each route."""
    STATUS_BY_IDS = "/{ids}/Status"
    """Gets the line status of for given line ids e.g Minor Delays"""
    STATUS_BY_IDS_DATES = "/{ids}/Status/{startDate}/to/{endDate}"
    """Gets the line status for given line ids during the provided dates e.g Minor Delays"""
    ROUTE_SEQUENCE_BY_ID_DIRECTION = "/{id}/Route/Sequence/{direction}"
    """Gets all valid routes for given line id, including the sequence of stops on each
    route."""
    STOP_POINTS_BY_ID = "/{id}/StopPoints"
    """Gets a list of the stations that serve the given line id"""
    TIMETABLE_BY_ID_FROM_STOP = "/{id}/Timetable/{fromStopPointId}"
    """Gets the timetable for a specified station on the give line"""
    TIMETABLE_BY_ID_FROM_TO_STOP = (
        "/{id}/Timetable/{fromStopPointId}/to/{toStopPointId}"
    )
    """Gets the timetable for a specified station on the give line with specified
    destination"""
