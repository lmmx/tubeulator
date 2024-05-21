"""Accessed via dynamic method resolution under `tubeulator.fetch.search`.

!!! example "Example: `tubeulator.fetch.search`"

    A few of these are unclear on how to call them, but they have meta methods:

    ```py
    >>> categories = fetch.search.meta_categories()
    >>> fetch.search.meta_search_providers()
    ['content', 'stopPoints', 'extraPlaces', 'extraPlacesAutocomplete', 'addressPlaces']
    >>> fetch.search.meta_sorts()
    ['lastModified,asc', 'lastModified,desc', 'date,asc', 'date,desc', 'score,asc', 'score,desc', 'timestamp,asc', 'timestamp,desc']
    ```
"""

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
