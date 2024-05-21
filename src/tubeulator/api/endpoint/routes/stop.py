"""Accessed via dynamic method resolution under `tubeulator.fetch.stop_point`.

!!! example "Example: `tubeulator.fetch.stop_point.direction_to()`"

    ```py
    >>> direction_to = fetch.stop_point.direction_to(
    ...         id="940GZZLUASL",
    ...         toStopPointId="940GZZLUHWY",
    ... )
    >>> direction_to
    'inbound'
    ```
"""

from .types import RouteEnum


class StopPointEndpointRoutes(RouteEnum):
    within_radius = "/"
    """Gets a list of StopPoints within {radius} by the specified criteria"""
    forward_requests = "/*"
    """Forwards any remaining requests to the back-end"""
    meta_categories = "/Meta/Categories"
    """Gets the list of available StopPoint additional information categories"""
    meta_modes = "/Meta/Modes"
    """Gets the list of available StopPoint modes"""
    meta_stop_types = "/Meta/StopTypes"
    """Gets the list of available StopPoint types"""
    mode = "/Mode/{modes}"
    """Gets a list of StopPoints filtered by the modes available at that StopPoint."""
    mode_disruption = "/Mode/{modes}/Disruption"
    """Gets a distinct list of disrupted stop points for the given modes"""
    search = "/Search"
    """Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code."""
    search_query = "/Search/{query}"
    """Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code."""
    service_types = "/ServiceTypes"
    """Gets the service types for a given stoppoint"""
    sms_id = "/Sms/{id}"
    """Gets a StopPoint for a given sms code."""
    type = "/Type/{types}"
    """Gets all stop points of a given type"""
    type_page = "/Type/{types}/page/{page}"
    """Gets all the stop points of given type(s) with a page number"""
    stop_point_ids = "/{ids}"
    """Gets a list of StopPoints corresponding to the given list of stop ids."""
    stop_point_disruption = "/{ids}/Disruption"
    """Gets all disruptions for the specified StopPointId, plus disruptions for any
    child Naptan records it may have."""
    arrival_departures = "/{id}/ArrivalDepartures"
    """Gets the list of arrival and departure predictions for the given stop point id
    (overground and tfl rail only)"""
    arrivals = "/{id}/Arrivals"
    """Gets the list of arrival predictions for the given stop point id"""
    can_reach_on_line = "/{id}/CanReachOnLine/{lineId}"
    """Gets Stopoints that are reachable from a station/line combination."""
    crowding = "/{id}/Crowding/{line}"
    """Gets all the Crowding data (static) for the StopPointId, plus crowding data
    for a given line and optionally a particular direction."""
    direction_to = "/{id}/DirectionTo/{toStopPointId}"
    """Returns the canonical direction, "inbound" or "outbound", for a given pair of
    stop point Ids in the direction from -&gt; to."""
    route = "/{id}/Route"
    """Returns the route sections for all the lines that service the given stop point
    ids"""
    place_types = "/{id}/placeTypes"
    """Get a list of places corresponding to a given id and place types."""
    car_parks = "/{stopPointId}/CarParks"
    """Get car parks corresponding to the given stop point id."""
    taxi_ranks = "/{stopPointId}/TaxiRanks"
    """Gets a list of taxi ranks corresponding to the given stop point id."""
