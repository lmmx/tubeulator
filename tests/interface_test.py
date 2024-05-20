import tubeulator
from inline_snapshot import snapshot


def test_interface():
    """This list was used to generate the `tests/apis/` test files.

    If the snapshot changes (a new interface is generated) then add test coverage.
    """
    interfaces = snapshot(
        [
            "accident_stats",
            "air_quality",
            "bike_point",
            "crowding",
            "disruptions_lifts_v2",
            "journey",
            "line",
            "mode",
            "occupancy",
            "place",
            "road",
            "search",
            "stop_point",
            "vehicle",
        ],
    )
    list(vars(tubeulator.fetch)) == interfaces
