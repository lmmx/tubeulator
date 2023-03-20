from .types import RouteEnum


class AccidentStatsEndpointRoutes(RouteEnum):
    YEAR_ACCIDENTS = "/{year}"
    """Gets all accident details for accidents occuring in the specified year"""
