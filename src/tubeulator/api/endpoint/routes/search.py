from .types import RouteEnum


class SearchEndpointRoutes(RouteEnum):
    search = "/"
    """Search the site for occurrences of the query string. The maximum number of
    results returned is equal to the maximum page size of 100. To return subsequent
    pages, use the paginated overload."""
    bus_schedules = "/BusSchedules"
    """Searches the bus schedules folder on S3 for a given bus number."""
    meta_categories = "/Meta/Categories"
    """Gets the available search categories."""
    meta_search_providers = "/Meta/SearchProviders"
    """Gets the available searchProvider names."""
    meta_sorts = "/Meta/Sorts"
    """Gets the available sorting options."""
