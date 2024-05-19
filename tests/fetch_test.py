import datetime

import tubeulator
from inline_snapshot import snapshot
from pydantic_core import TzInfo


def test_first_mode_is_bus():
    modes = tubeulator.fetch.line.meta_modes()
    first_mode_name = modes[0].ModeName
    assert first_mode_name == "bus"


def test_lines_by_ids():
    """Relies on correct codegen of arrays (previously had a bug).

    Note: the `TzInfo(0)` snapshots as `TzInfo(UTC)` for unclear reasons.
    """
    lines = tubeulator.fetch.line.lines_by_ids("waterloo-city")
    assert [l.model_dump() for l in lines] == snapshot(
        [
            {
                "Id": "waterloo-city",
                "Name": "Waterloo & City",
                "ModeName": "tube",
                "Disruptions": [],
                "Created": datetime.datetime(
                    2024,
                    5,
                    14,
                    14,
                    35,
                    6,
                    617000,
                    tzinfo=TzInfo(0),
                ),
                "Modified": datetime.datetime(
                    2024,
                    5,
                    14,
                    14,
                    35,
                    6,
                    617000,
                    tzinfo=TzInfo(0),
                ),
                "LineStatuses": [],
                "RouteSections": [],
                "ServiceTypes": [
                    {
                        "Name": "Regular",
                        "Uri": "/Line/Route?ids=Waterloo & City&serviceTypes=Regular",
                    },
                ],
                "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
            },
        ],
    )
