from enum import Enum


class AccidentStatsEndpointRoutes(Enum):
    YEAR_ACCIDENTS = "/{year}"
    """Gets all accident details for accidents occuring in the specified year"""
