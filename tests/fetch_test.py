import tubeulator
from inline_snapshot import snapshot
from pytest import mark


def test_first_mode_is_bus():
    modes = tubeulator.fetch.line.meta_modes()
    first_mode_name = modes[0].ModeName
    assert first_mode_name == "bus"


wc_line_snapshot = snapshot(
    [
        {
            "Id": "waterloo-city",
            "Name": "Waterloo & City",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.617000Z",
            "Modified": "2024-05-14T14:35:06.617000Z",
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


@mark.parametrize("line_id,expected", [("waterloo-city", wc_line_snapshot)])
def test_lines_by_ids(line_id, expected):
    """Relies on correct codegen of arrays (previously had a bug)."""
    lines = tubeulator.fetch.line.lines_by_ids(line_id)
    assert [l.model_dump(mode="json") for l in lines] == expected
