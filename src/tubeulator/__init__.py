"""`tubeulator` is an interface to TfL open data."""

__all__ = ["fetch"]

from .api import fetch
from .network import (
    load_lines,
    load_lines_by_station,
    load_platform_services,
    load_platforms,
    load_platforms_with_stations_and_services,
    load_station_points,
    load_stations,
    load_stations_by_line,
)

__all__ = [
    "load_lines",
    "load_lines_by_station",
    "load_platform_services",
    "load_platforms",
    "load_platforms_with_stations_and_services",
    "load_station_points",
    "load_stations",
    "load_stations_by_line",
]
