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


tube_line_snapshot = snapshot(
    [
        {
            "Id": "bakerloo",
            "Name": "Bakerloo",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.647000Z",
            "Modified": "2024-05-14T14:35:06.647000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Bakerloo&serviceTypes=Regular",
                }
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "central",
            "Name": "Central",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.630000Z",
            "Modified": "2024-05-14T14:35:06.630000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Central&serviceTypes=Regular",
                },
                {"Name": "Night", "Uri": "/Line/Route?ids=Central&serviceTypes=Night"},
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "circle",
            "Name": "Circle",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.647000Z",
            "Modified": "2024-05-14T14:35:06.647000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Circle&serviceTypes=Regular",
                }
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "district",
            "Name": "District",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.630000Z",
            "Modified": "2024-05-14T14:35:06.630000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=District&serviceTypes=Regular",
                }
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "hammersmith-city",
            "Name": "Hammersmith & City",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.647000Z",
            "Modified": "2024-05-14T14:35:06.647000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Hammersmith & City&serviceTypes=Regular",
                }
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "jubilee",
            "Name": "Jubilee",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.630000Z",
            "Modified": "2024-05-14T14:35:06.630000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Jubilee&serviceTypes=Regular",
                },
                {"Name": "Night", "Uri": "/Line/Route?ids=Jubilee&serviceTypes=Night"},
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "metropolitan",
            "Name": "Metropolitan",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.647000Z",
            "Modified": "2024-05-14T14:35:06.647000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Metropolitan&serviceTypes=Regular",
                }
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "northern",
            "Name": "Northern",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.647000Z",
            "Modified": "2024-05-14T14:35:06.647000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Northern&serviceTypes=Regular",
                },
                {"Name": "Night", "Uri": "/Line/Route?ids=Northern&serviceTypes=Night"},
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "piccadilly",
            "Name": "Piccadilly",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.630000Z",
            "Modified": "2024-05-14T14:35:06.630000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Piccadilly&serviceTypes=Regular",
                },
                {
                    "Name": "Night",
                    "Uri": "/Line/Route?ids=Piccadilly&serviceTypes=Night",
                },
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
        {
            "Id": "victoria",
            "Name": "Victoria",
            "ModeName": "tube",
            "Disruptions": [],
            "Created": "2024-05-14T14:35:06.617000Z",
            "Modified": "2024-05-14T14:35:06.617000Z",
            "LineStatuses": [],
            "RouteSections": [],
            "ServiceTypes": [
                {
                    "Name": "Regular",
                    "Uri": "/Line/Route?ids=Victoria&serviceTypes=Regular",
                },
                {"Name": "Night", "Uri": "/Line/Route?ids=Victoria&serviceTypes=Night"},
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
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
                }
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
    ]
)


@mark.parametrize("mode_id,expected", [("tube", tube_line_snapshot)])
def test_lines_by_modes(mode_id, expected):
    lines = tubeulator.fetch.line.lines_by_modes(mode_id)
    assert [l.model_dump(mode="json") for l in lines] == expected
