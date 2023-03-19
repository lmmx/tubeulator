from enum import Enum

from .line import Line

# class Endpoint(Enum):
#     OCCUPANCY = "occupancy"
#     DISRUPTIONS_LIFTS_V2 = "Disruptions-Lifts-v2"
#     STOP_POINT = "StopPoint"
#     SEARCH = "Search"
#     MODE = "Mode"
#     VEHICLE = "Vehicle"
#     ACCIDENT_STATS = "AccidentStats"
#     ROAD = "Road"
#     CROWDING = "crowding"
#     BIKE_POINT = "BikePoint"
#     AIR_QUALITY = "AirQuality"
#     JOURNEY = "Journey"
#     LINE = "Line"
#     PLACE = "Place"


class Endpoint(Enum):
    ACCIDENT_STATS = "AccidentStats"
    AIR_QUALITY = "AirQuality"
    BIKE_POINT = "BikePoint"
    CROWDING = "crowding"
    DISRUPTIONS_LIFTS_V2 = "Disruptions-Lifts-v2"
    JOURNEY = "Journey"
    LINE = "Line"
    MODE = "Mode"
    OCCUPANCY = "occupancy"
    PLACE = "Place"
    ROAD = "Road"
    SEARCH = "Search"
    STOP_POINT = "StopPoint"
    VEHICLE = "Vehicle"
