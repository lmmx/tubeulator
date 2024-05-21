from .types import RouteEnum


class CrowdingEndpointRoutes(RouteEnum):
    naptan_crowding = "/{Naptan}"
    """Returns crowding information for Naptan"""
    live_crowding = "/{Naptan}/Live"
    """Returns live crowding information for Naptan"""
    dow_crowding = "/{Naptan}/{DayOfWeek}"
    """Returns crowding information for Naptan for Day of Week"""
