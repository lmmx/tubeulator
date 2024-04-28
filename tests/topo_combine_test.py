import polars as pl
from tubeulator.topology.combine import load_lines_by_station, load_stations_by_line

__all__ = ["test_load_stations_by_line", "test_load_lines_by_station"]


def test_load_stations_by_line():
    line2stns = load_stations_by_line()
    stn_counts = line2stns.with_columns(
        pl.col("StationName").list.len().alias("Count"),
    ).sort("Count")
    assert stn_counts["Count"].min() == 2
    assert stn_counts["Count"].max() == 112


def test_load_lines_by_station():
    stn2lines = load_lines_by_station()
    line_counts = stn2lines.with_columns(
        pl.col("Lines").list.len().alias("Count"),
    ).sort("Count")
    assert line_counts["Count"].min() == 1
    assert line_counts["Count"].max() == 7
