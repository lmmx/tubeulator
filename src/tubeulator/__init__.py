"""`tubeulator` is an interface to TfL open data."""

__all__ = ["fetch"]

from .api import fetch
from .network.load import (
    load_lines,
    load_platform_services,
    load_platforms,
    load_station_points,
    load_stations,
)

__all__ = [
    "load_lines",
    "load_platforms",
    "load_platform_services",
    "load_stations",
    "load_station_points",
]
