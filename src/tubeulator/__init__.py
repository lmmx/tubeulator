"""`tubeulator` is an interface to TfL open data."""

__all__ = [
    "fetch",
    "load_lines",
    "load_lines_by_station",
    "load_platform_services",
    "load_platforms",
    "load_platforms_with_stations_and_services",
    "load_station_points",
    "load_stations",
    "load_stations_by_line",
    "show_station_points_map",
]

from .api import fetch
from .topology import (
    load_lines,
    load_lines_by_station,
    load_platform_services,
    load_platforms,
    load_platforms_with_stations_and_services,
    load_station_points,
    load_stations,
    load_stations_by_line,
    show_station_points_map,
)
