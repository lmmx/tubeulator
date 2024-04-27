from .load import load_platforms, load_stations

__all__ = ["load_station_services"]


def load_station_services():
    """Annotate platforms with their station info"""
    platform2station_kwargs = dict(left_on="StationUniqueId", right_on="UniqueId")
    platforms = load_platforms().join(load_stations(), **platform2station_kwargs)
    # platform_services = load_platform_services()
    return platforms
