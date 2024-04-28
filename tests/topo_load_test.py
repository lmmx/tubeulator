from tubeulator.topology.load import (
    load_lines,
    load_platform_services,
    load_platforms,
    load_station_points,
    load_stations,
)

__all__ = [
    "test_load_lines",
    "test_load_platforms",
    "test_load_platform_services",
    "load_stations",
    "load_station_points",
]


def test_load_lines():
    lines = load_lines()


def test_load_platforms():
    platforms = load_platforms()


def test_load_platform_services():
    platform_services = load_platform_services()


def test_load_stations():
    stations = load_stations()


def test_load_station_points():
    station_points = load_station_points()
