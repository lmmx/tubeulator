from .types import RouteEnum


class SearchEndpointRoutes(RouteEnum):
    SEARCH = "/"
    """Search the site for occurrences of the query string. The maximum number of
    results returned is equal to the maximum page size of 100. To return subsequent
    pages, use the paginated overload."""
    BUS_SCHEDULES = "/BusSchedules"
    """Searches the bus schedules folder on S3 for a given bus number."""
    META_CATEGORIES = "/Meta/Categories"
    """Gets the available search categories."""
    META_SEARCH_PROVIDERS = "/Meta/SearchProviders"
    """Gets the available searchProvider names."""
    META_SORTS = "/Meta/Sorts"
    """Gets the available sorting options."""
