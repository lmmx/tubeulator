from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from urllib.parse import urlencode

import httpx
from pydantic import BaseModel, TypeAdapter

from ..codegen import load_test
from ..db.store_creds import check_creds
from ..exc import RequestError
from ..utils.paths import RefPath, SchemaPath
from ..utils.schemas import load_endpoint_component_schemas, load_endpoint_schema
from .endpoint.names import EndpointNames
from .endpoint.routes.types import AnyEndpointRouteEnum

__all__ = ["TflApiPath", "Path", "Request", "GET"]


class TflApiPath:
    root: str = "https://api.tfl.gov.uk/"


@dataclass
class Path(TflApiPath):
    endpoint: EndpointNames
    route: AnyEndpointRouteEnum
    vars: list = field(init=False)

    class Var(Enum):
        DAY_OF_WEEK = "DayOfWeek"
        NAPTAN = "Naptan"
        DIRECTION = "direction"
        DISRUPTION_IDS = "disruptionIds"
        END_DATE = "endDate"
        FROM = "from"
        FROM_STOP_POINT_ID = "fromStopPointId"
        ID = "id"
        IDS = "ids"
        LAT = "lat"
        LINE = "line"
        LINE_ID = "lineId"
        LON = "lon"
        MODE = "mode"
        MODES = "modes"
        PAGE = "page"
        QUERY = "query"
        SEVERITY = "severity"
        START_DATE = "startDate"
        STOP_POINT_ID = "stopPointId"
        TO = "to"
        TO_STOP_POINT_ID = "toStopPointId"
        TYPE = "type"
        TYPES = "types"
        YEAR = "year"

    def __post_init__(self):
        self.vars = [
            self.Var(var.strip("{}"))
            for var in self.route.parts
            if var.startswith("{") and var.endswith("}")
        ]

    @property
    def url(self) -> str:
        return f"{self.root}{self.endpoint.value}{self.route.value}"

    @property
    def vars_to_fill(self) -> list[str]:
        return [var.value for var in self.vars]

    def check_vars_supplied(self, *args, **kwargs) -> dict:
        """Basic input validation, not type validation."""
        if args and kwargs:
            self.invalidate(
                "You can't mix args and kwargs, pick one.",
                rcvd={"args": args, "kwargs": kwargs},
            )
        elif self.vars and not (args or kwargs):
            self.invalidate("No vars supplied.", rcvd={"args": args, "kwargs": kwargs})
        if args and len(args) < len(self.vars):
            self.invalidate("Missing arguments", rcvd=args)
        elif kwargs and set(self.vars_to_fill) != set(kwargs):
            self.invalidate("Missing parameters", rcvd=kwargs)

    def invalidate(self, reason: str, rcvd: list[str] | dict):
        raise ValueError(f"Bad request ({reason}): {self.vars_to_fill=}, got {rcvd}")

    def build_url(self, *args, **kwargs) -> str:
        self.check_vars_supplied(*args, **kwargs)
        params = dict(zip(self.vars_to_fill, args)) if args else kwargs
        return self.url.format(**params)


@dataclass
class Request:
    """`tubeulator` uses :cls:`Request` objects to handle the various Transport for London
    APIs. They all follow the same structure and are therefore handled by one class.

    For the documentation on each particular API, look up the capitalised method name
    in the collected documentation below (which is just a shortened version of the
    Enums found in the `tubeulator.api.endpoint.routes` modules). For example the
    `tubeulator.fetch.stop_point.meta_modes` API is under `STOP_POINT` > `META_MODES`.

    EndpointRoute
    =============

    ACCIDENT_STATS
    AIR_QUALITY
    BIKE_POINT
    CROWDING
    DISRUPTIONS_LIFTS_V2
    JOURNEY
    LINE
    MODE
    OCCUPANCY
    PLACE
    ROAD
    SEARCH
    STOP_POINT
    VEHICLE

    ACCIDENT_STATS
    ==============

    YEAR_ACCIDENTS = "/{year}"
    Gets all accident details for accidents occuring in the specified year

    AIR_QUALITY
    ===========

    AIR_QUALITY_DATA = "/"
    Gets air quality data feed

    BIKE_POINT
    ==========

    ALL_LOCATIONS = "/"
    Gets all bike point locations. The Place object has an addtionalProperties array
    which contains the nbBikes, nbDocks and nbSpaces numbers which give the status of
    the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) != 0
    indicates broken docks.

    SEARCH_STATIONS = "/Search"
    Search for bike stations by their name, a bike point's name often contains
    information about the name of the street or nearby landmarks, for example. Note that the
    search result does not contain the PlaceProperties i.e. the status or occupancy of the
    BikePoint, to get that information you should retrieve the BikePoint by its id on
    '/BikePoint/id.

    BIKE_POINT_BY_ID = "/{id}"
    Gets the bike point with the given id.

    CROWDING
    ========

    NAPTAN_CROWDING = "/{Naptan}"
    Returns crowding information for Naptan

    LIVE_CROWDING = "/{Naptan}/Live"
    Returns live crowding information for Naptan

    DOW_CROWDING = "/{Naptan}/{DayOfWeek}"
    Returns crowding information for Naptan for Day of Week

    DISRUPTIONS_LIFTS_V2
    ====================

    ALL = "/"
    List of all currently disrupted lift routes

    JOURNEY
    =======

    FORWARD_REQUESTS = "/*"
    Forwards any remaining requests to the back-end

    JOURNEY_RESULTS = "/JourneyResults/{from}/to/{to}"
    Perform a Journey Planner search from the parameters specified in simple types

    MODES = "/Meta/Modes"
    Gets a list of all of the available journey planner modes

    LINE
    ====

    FORWARD_REQUESTS = "/*"
    Forwards any remaining requests to the back-end

    META_DISRUPTION_CATEGORIES = "/Meta/DisruptionCategories"
    Gets a list of valid disruption categories

    META_MODES = "/Meta/Modes"
    Gets a list of valid modes

    META_SERVICE_TYPES = "/Meta/ServiceTypes"
    Gets a list of valid ServiceTypes to filter on

    META_SEVERITY = "/Meta/Severity"
    Gets a list of valid severity codes

    LINES_BY_MODES = "/Mode/{modes}"
    Gets lines that serve the given modes.

    DISRUPTION_BY_MODES = "/Mode/{modes}/Disruption"
    Get disruptions for all lines of the given modes.

    ROUTE_BY_MODES = "/Mode/{modes}/Route"
    Gets all lines and their valid routes for given modes, including the name and id of
    the originating and terminating stops for each route

    STATUS_BY_MODES = "/Mode/{modes}/Status"
    Gets the line status of for all lines for the given modes

    ALL_ROUTES = "/Route"
    Get all valid routes for all lines, including the name and id of the originating and
    terminating stops for each route.

    SEARCH_LINES_ROUTES = "/Search/{query}"
    Search for lines or routes matching the query string

    STATUS_BY_SEVERITY = "/Status/{severity}"
    Gets the line status for all lines with a given severity. A list of valid severity
    codes can be obtained from a call to Line/Meta/Severity

    LINES_BY_IDS = "/{ids}"
    Gets lines that match the specified line ids.

    ARRIVALS_BY_IDS = "/{ids}/Arrivals"
    Get the list of arrival predictions for given line ids based at the given stop

    ARRIVALS_BY_IDS_STOP = "/{ids}/Arrivals/{stopPointId}"
    Get the list of arrival predictions for given line ids based at the given stop

    DISRUPTION_BY_IDS = "/{ids}/Disruption"
    Get disruptions for the given line ids

    ROUTE_BY_IDS = "/{ids}/Route"
    Get all valid routes for given line ids, including the name and id of the
    originating and terminating stops for each route.

    STATUS_BY_IDS = "/{ids}/Status"
    Gets the line status of for given line ids e.g Minor Delays

    STATUS_BY_IDS_DATES = "/{ids}/Status/{startDate}/to/{endDate}"
    Gets the line status for given line ids during the provided dates e.g Minor Delays

    ROUTE_SEQUENCE_BY_ID_DIRECTION = "/{id}/Route/Sequence/{direction}"
    Gets all valid routes for given line id, including the sequence of stops on each
    route.

    STOP_POINTS_BY_ID = "/{id}/StopPoints"
    Gets a list of the stations that serve the given line id

    TIMETABLE_BY_ID_FROM_STOP = "/{id}/Timetable/{fromStopPointId}"
    Gets the timetable for a specified station on the give line

    TIMETABLE_BY_ID_FROM_TO_STOP = (
        "/{id}/Timetable/{fromStopPointId}/to/{toStopPointId}"
    )
    Gets the timetable for a specified station on the give line with specified
    destination


    MODE
    ====

    ACTIVE_SERVICE_TYPES = "/ActiveServiceTypes"
    Returns the service type active for a mode. Currently only supports tube

    MODE_ARRIVALS = "/{mode}/Arrivals"
    Gets the next arrival predictions for all stops of a given mode

    OCCUPANCY
    =========

    BIKE_POINTS = "/BikePoints/{ids}"
    Get the occupancy for bike points.

    CAR_PARK = "/CarPark"
    Gets the occupancy for all car parks that have occupancy data

    CAR_PARK_ID = "/CarPark/{id}"
    Gets the occupancy for a car park with a given id

    CHARGE_CONNECTOR = "/ChargeConnector"
    Gets the occupancy for all charge connectors

    CHARGE_CONNECTOR_IDS = "/ChargeConnector/{ids}"
    Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId)

    PLACE
    =====

    PLACES_BY_GEO_REGION = "/"
    Gets the places that lie within a geographic region. The geographic region of interest can either
    be specified by using a lat/lon geo-point and a radius in metres to return places within the locus
    defined by the lat/lon of its centre or alternatively, by the use of a bounding box defined by the
    lat/lon of its north-west and south-east corners. Optionally filters on type and can strip
    properties for a smaller payload.

    FORWARD_REQUESTS = "/*"
    Forwards any remaining requests to the back-end

    META_CATEGORIES = "/Meta/Categories"
    Gets a list of all of the available place property categories and keys.

    META_PLACE_TYPES = "/Meta/PlaceTypes"
    Gets a list of the available types of Place.

    SEARCH_PLACES = "/Search"
    Gets all places that matches the given query

    PLACES_BY_TYPE = "/Type/{types}"
    Gets all places of a given type

    PLACE_BY_ID = "/{id}"
    Gets the place with the given id.

    PLACE_BY_TYPE_AT_COORDINATES = "/{type}/At/{lat}/{lon}"
    Gets any places of the given type whose geography intersects the given latitude and longitude. In
    practice this means the Place must be polygonal e.g. a BoroughBoundary.

    ROAD
    ====

    ALL_ROADS = "/"
    Gets all roads managed by TfL

    META_CATEGORIES = "/Meta/Categories"
    Gets a list of valid RoadDisruption categories

    META_SEVERITIES = "/Meta/Severities"
    Gets a list of valid RoadDisruption severity codes

    DISRUPTION_BY_IDS = "/all/Disruption/{disruptionIds}"
    Gets a list of active disruptions filtered by disruption Ids.

    STREET_DISRUPTION = "/all/Street/Disruption"
    Gets a list of disrupted streets. If no date filters are provided, current
    disruptions are returned.

    ROAD_BY_IDS = "/{ids}"
    Gets the road with the specified id (e.g. A1)

    ROAD_DISRUPTION = "/{ids}/Disruption"
    Get active disruptions, filtered by road ids

    ROAD_STATUS = "/{ids}/Status"
    Gets the specified roads with the status aggregated over the date range
    specified, or now until the end of today if no dates are passed.

    SEARCH
    ======

    SEARCH = "/"
    Search the site for occurrences of the query string. The maximum number of
    results returned is equal to the maximum page size of 100. To return subsequent
    pages, use the paginated overload.

    BUS_SCHEDULES = "/BusSchedules"
    Searches the bus schedules folder on S3 for a given bus number.

    META_CATEGORIES = "/Meta/Categories"
    Gets the available search categories.

    META_SEARCH_PROVIDERS = "/Meta/SearchProviders"
    Gets the available searchProvider names.

    META_SORTS = "/Meta/Sorts"
    Gets the available sorting options.

    STOP_POINT
    ==========

    WITHIN_RADIUS = "/"
    Gets a list of StopPoints within {radius} by the specified criteria

    FORWARD_REQUESTS = "/*"
    Forwards any remaining requests to the back-end

    META_CATEGORIES = "/Meta/Categories"
    Gets the list of available StopPoint additional information categories

    META_MODES = "/Meta/Modes"
    Gets the list of available StopPoint modes

    META_STOP_TYPES = "/Meta/StopTypes"
    Gets the list of available StopPoint types

    MODE = "/Mode/{modes}"
    Gets a list of StopPoints filtered by the modes available at that StopPoint.

    MODE_DISRUPTION = "/Mode/{modes}/Disruption"
    Gets a distinct list of disrupted stop points for the given modes

    SEARCH = "/Search"
    Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.

    SEARCH_QUERY = "/Search/{query}"
    Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.

    SERVICE_TYPES = "/ServiceTypes"
    Gets the service types for a given stoppoint

    SMS_ID = "/Sms/{id}"
    Gets a StopPoint for a given sms code.

    TYPE = "/Type/{types}"
    Gets all stop points of a given type

    TYPE_PAGE = "/Type/{types}/page/{page}"
    Gets all the stop points of given type(s) with a page number

    STOP_POINT_IDS = "/{ids}"
    Gets a list of StopPoints corresponding to the given list of stop ids.

    STOP_POINT_DISRUPTION = "/{ids}/Disruption"
    Gets all disruptions for the specified StopPointId, plus disruptions for any
    child Naptan records it may have.

    ARRIVAL_DEPARTURES = "/{id}/ArrivalDepartures"
    Gets the list of arrival and departure predictions for the given stop point id
    (overground and tfl rail only)

    ARRIVALS = "/{id}/Arrivals"
    Gets the list of arrival predictions for the given stop point id

    CAN_REACH_ON_LINE = "/{id}/CanReachOnLine/{lineId}"
    Gets Stopoints that are reachable from a station/line combination.

    CROWDING = "/{id}/Crowding/{line}"
    Gets all the Crowding data (static) for the StopPointId, plus crowding data
    for a given line and optionally a particular direction.

    DIRECTION_TO = "/{id}/DirectionTo/{toStopPointId}"
    Returns the canonical direction, "inbound" or "outbound", for a given pair of
    stop point Ids in the direction from -&gt; to.

    ROUTE = "/{id}/Route"
    Returns the route sections for all the lines that service the given stop point
    ids

    PLACE_TYPES = "/{id}/placeTypes"
    Get a list of places corresponding to a given id and place types.

    CAR_PARKS = "/{stopPointId}/CarParks"
    Get car parks corresponding to the given stop point id.

    TAXI_RANKS = "/{stopPointId}/TaxiRanks"
    Gets a list of taxi ranks corresponding to the given stop point id.

    VEHICLE
    =======

    EMISSION_SURCHARGE = "/EmissionSurcharge"
    Gets the Emissions Surcharge compliance for the Vehicle

    ULEZ_COMPLIANCE = "/UlezCompliance"
    Gets the Ulez Surcharge compliance for the Vehicle

    VEHICLE_ARRIVALS = "/{ids}/Arrivals"
    Gets the predictions for a given list of vehicle Id's.
    """

    path: Path

    def __call__(self, *args, **kwargs):
        try:
            result = self.send(*args, **kwargs)
        except httpx.HTTPError as exc:
            resp = exc.response
            raise RequestError(
                response=resp,
                path=self.path,
                _args=args,
                _kwargs=kwargs,
            ) from None
        parsed = self.parse(result)
        return parsed

    def send(self, *args, **kwargs) -> httpx.Response:
        url = self.path.build_url(*args, **kwargs)
        response = GET(url=url)
        response.raise_for_status()
        return response

    def ep_name(self, dehyphenate: bool = False) -> str:
        endpoint_name = self.path.endpoint.value
        return endpoint_name.replace("-", "") if dehyphenate else endpoint_name

    def response_refpath(self) -> RefPath:
        """Go from the endpoint route info to the response type (its reference type)."""
        endpoint_schema = load_endpoint_schema(self.ep_name())
        route_info = endpoint_schema["paths"][self.path.route.value]
        response_schema = route_info["get"]["responses"]["200"]["content"][
            "application/json"
        ]["schema"]
        response_ref = response_schema["$ref"]
        return RefPath(response_ref)

    def parse(self, response: httpx.Response):
        response_refpath = self.response_refpath()
        component_schemas = load_endpoint_component_schemas(self.ep_name())
        response_component_schema = component_schemas[response_refpath.name]
        if response_component_schema.get("items", {}).get("type") == "string":
            parsed = response.json()
        else:
            try:
                # Take a 2nd order reference
                ref_type = SchemaPath(response_component_schema)
                ref_name = ref_type.ref.name
            except Exception:
                # Not a 2nd order reference
                ref_name = response_refpath.name
            try:
                marshals = getattr(
                    load_test,
                    self.ep_name(dehyphenate=True),
                ).Deserialisers
            except Exception as exc:
                hint = "(did the import from `generated` get removed by a linter?)"
                fail_msg = f"The API endpoint wasn't attached to `load_test` ({hint})"
                raise RuntimeError(f"{fail_msg} -- {exc}")
            dto = marshals.select_component(ref_name).value
            is_pydantic = issubclass(dto, BaseModel)
            try:
                if is_pydantic:
                    # Peek at the first character, let Pydantic deserialise the JSON
                    is_array = response.text[0] == "["
                    # data = response.json()
                    # is_array = isinstance(data, list)
                    if is_array:
                        validate = TypeAdapter(list[dto]).validate_json
                    else:
                        validate = dto.model_validate_json
                    parsed = validate(response.content)
                else:
                    # Assume JSONWizard
                    parsed = dto.from_json(response.content)
            except:
                raise
        return parsed


def GET(url: str) -> httpx.Response:
    credentials = check_creds()
    params = urlencode(
        {"app_id": credentials["app_id"], "app_key": credentials["primary_key"]},
    )
    return httpx.get(url, params=params)
