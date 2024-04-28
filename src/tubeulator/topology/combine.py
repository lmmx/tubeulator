import polars as pl

from .load import (
    load_platform_services,
    load_platforms,
    load_station_points,
    load_stations,
)

__all__ = [
    "load_platforms_with_stations_and_services",
    "load_lines_by_station",
    "load_stations_by_line",
]


def load_platforms_with_stations_and_services():
    """Annotate platform services with their platform and station info."""
    # There are about 1400 platforms
    platforms = load_platforms()
    # There are around 500 stations
    stations = load_stations()
    # There are around 1600 platform services.
    # There are more than the number of physical platforms because multiple services use
    # the same platform (stopping at different times, e.g. Hammersmith & City/District)
    platform_svcs = load_platform_services()
    # There are the same number of platforms with stations as platforms
    platforms_with_stns = platforms.join(stations, on="StationUniqueId")
    # There are the same number of platforms with stations and services as platform services
    plts_stns_svcs = platforms_with_stns.join(platform_svcs, on="PlatformUniqueId")
    return plts_stns_svcs


def load_lines_by_station():
    pss = load_platforms_with_stations_and_services()
    station2lines = pss.group_by("StationUniqueId").agg(
        [pl.col("Line").unique().alias("Lines")],
    )
    station2lines = station2lines.join(
        pss.select(["StationUniqueId", "StationName"]).unique(),
        on="StationUniqueId",
        how="left",
    )
    return station2lines


def load_stations_by_line():
    station2lines = load_lines_by_station()
    line2stations = (
        station2lines.rename({"Lines": "Line"})
        .explode("Line")
        .group_by("Line")
        .agg(pl.col("StationName"))
    )
    return line2stations


def load_station_points_with_lines():
    stn_points = load_station_points()
    stn2lines = load_lines_by_station()
    stn_points_with_lines = stn_points.join(stn2lines, on="StationUniqueId")
    return stn_points_with_lines
