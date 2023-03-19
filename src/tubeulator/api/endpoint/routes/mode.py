from enum import Enum


class ModeEndpointRoutes(Enum):
    ACTIVE_SERVICE_TYPES = "/ActiveServiceTypes"
    """Returns the service type active for a mode. Currently only supports tube"""
    MODE_ARRIVALS = "/{mode}/Arrivals"
    """Gets the next arrival predictions for all stops of a given mode"""
