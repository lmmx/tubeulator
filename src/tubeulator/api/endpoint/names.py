from enum import Enum

__all__ = ["EndpointNames"]


class EndpointNames(Enum):
    """Standardised enum of names used in JSON schema filenames for each endpoint."""

    accident_stats = "AccidentStats"
    air_quality = "AirQuality"
    bike_point = "BikePoint"
    crowding = "crowding"
    disruptions_lifts_v2 = "Disruptions-Lifts-v2"
    journey = "Journey"
    line = "Line"
    mode = "Mode"
    occupancy = "occupancy"
    place = "Place"
    road = "Road"
    search = "Search"
    stop_point = "StopPoint"
    vehicle = "Vehicle"
