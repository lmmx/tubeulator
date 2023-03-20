from .types import RouteEnum


class JourneyEndpointRoutes(RouteEnum):
    FORWARD_REQUESTS = "/*"
    """Forwards any remaining requests to the back-end"""
    JOURNEY_RESULTS = "/JourneyResults/{from}/to/{to}"
    """Perform a Journey Planner search from the parameters specified in simple types"""
    MODES = "/Meta/Modes"
    """Gets a list of all of the available journey planner modes"""
