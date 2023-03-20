from .types import RouteEnum


class CrowdingEndpointRoutes(RouteEnum):
    NAPTAN_CROWDING = "/{Naptan}"
    """Returns crowding information for Naptan"""
    LIVE_CROWDING = "/{Naptan}/Live"
    """Returns live crowding information for Naptan"""
    DOW_CROWDING = "/{Naptan}/{DayOfWeek}"
    """Returns crowding information for Naptan for Day of Week"""
