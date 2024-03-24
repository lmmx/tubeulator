from enum import Enum

__all__ = ["EndpointNames"]


class EndpointNames(Enum):
    """Standardised enum of names used in JSON schema filenames for each endpoint."""

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
