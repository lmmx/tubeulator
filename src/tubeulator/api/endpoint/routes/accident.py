from .types import RouteEnum


class AccidentStatsEndpointRoutes(RouteEnum):
    year_accidents = "/{year}"
    """Gets all accident details for accidents occuring in the specified year"""
