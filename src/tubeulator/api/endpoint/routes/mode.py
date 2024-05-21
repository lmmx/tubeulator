from .types import RouteEnum


class ModeEndpointRoutes(RouteEnum):
    active_service_types = "/ActiveServiceTypes"
    """Returns the service type active for a mode. Currently only supports tube"""
    mode_arrivals = "/{mode}/Arrivals"
    """Gets the next arrival predictions for all stops of a given mode"""
