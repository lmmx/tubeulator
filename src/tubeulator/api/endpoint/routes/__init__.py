"""All API endpoints are accessed via dispatch method under `tubeulator.fetch`."""

from enum import Enum

from .accident import AccidentStatsEndpointRoutes
from .air import AirQualityEndpointRoutes
from .bike import BikePointEndpointRoutes
from .crowding import CrowdingEndpointRoutes
from .disruption_lifts import DisruptionsLiftsEndpointRoutes
from .journey import JourneyEndpointRoutes
from .line import LineEndpointRoutes
from .mode import ModeEndpointRoutes
from .occupancy import OccupancyEndpointRoutes
from .place import PlaceEndpointRoutes
from .road import RoadEndpointRoutes
from .search import SearchEndpointRoutes
from .stop import StopPointEndpointRoutes
from .vehicle import VehicleEndpointRoutes

__all__ = ["EndpointRoute"]


class EndpointRoute(Enum):
    accident_stats = AccidentStatsEndpointRoutes
    air_quality = AirQualityEndpointRoutes
    bike_point = BikePointEndpointRoutes
    crowding = CrowdingEndpointRoutes
    disruptions_lifts_v2 = DisruptionsLiftsEndpointRoutes
    journey = JourneyEndpointRoutes
    line = LineEndpointRoutes
    mode = ModeEndpointRoutes
    occupancy = OccupancyEndpointRoutes
    place = PlaceEndpointRoutes
    road = RoadEndpointRoutes
    search = SearchEndpointRoutes
    stop_point = StopPointEndpointRoutes
    vehicle = VehicleEndpointRoutes
