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
    ACCIDENT_STATS = AccidentStatsEndpointRoutes
    AIR_QUALITY = AirQualityEndpointRoutes
    BIKE_POINT = BikePointEndpointRoutes
    CROWDING = CrowdingEndpointRoutes
    DISRUPTIONS_LIFTS_V2 = DisruptionsLiftsEndpointRoutes
    JOURNEY = JourneyEndpointRoutes
    LINE = LineEndpointRoutes
    MODE = ModeEndpointRoutes
    OCCUPANCY = OccupancyEndpointRoutes
    PLACE = PlaceEndpointRoutes
    ROAD = RoadEndpointRoutes
    SEARCH = SearchEndpointRoutes
    STOP_POINT = StopPointEndpointRoutes
    VEHICLE = VehicleEndpointRoutes
