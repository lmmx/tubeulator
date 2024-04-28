import polars as pl

from .load import load_platform_services, load_platforms, load_stations

__all__ = [
    "load_platforms_with_stations_and_services",
    "load_lines_by_station",
    "load_stations_by_line",
]


def load_platforms_with_stations_and_services():
    """Annotate platform services with their platform and station info."""
    # TODO move all of these renamings into the data model instead (alias).
    #      This prevents having to rename multiple times (at sites of use)
    #      giving in effect a 'global column namespace'

    # There are about 1400 platforms
    platform_renamings = {k: f"Platform{k}" for k in ["UniqueId", "FriendlyName"]}
    platforms = load_platforms().rename(platform_renamings)
    # There are around 500 stations
    station_renamings = {k: f"Station{k}" for k in ["UniqueId", "Name"]}
    stations = load_stations().rename(station_renamings)
    # There are around 1600 platform services.
    # There are more than the number of physical platforms because multiple services use
    # the same platform (stopping at different times, e.g. Hammersmith & City/District)
    platform_service_renamings = {k: f"Platform{k}" for k in ["GroupName"]}
    platform_svcs = load_platform_services().rename(platform_service_renamings)
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
        station2lines.explode("Lines").group_by("Lines").agg(pl.col("StationName"))
    )
    return line2stations
