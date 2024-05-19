from inline_snapshot import snapshot

all_endpoints = snapshot(
    [
        "forward_requests",
        "meta_disruption_categories",
        "meta_modes",
        "meta_service_types",
        "meta_severity",
        "lines_by_modes",
        "disruption_by_modes",
        "route_by_modes",
        "status_by_modes",
        "all_routes",
        "search_lines_routes",
        "status_by_severity",
        "lines_by_ids",
        "arrivals_by_ids",
        "arrivals_by_ids_stop",
        "disruption_by_ids",
        "route_by_ids",
        "status_by_ids",
        "status_by_ids_dates",
        "route_sequence_by_id_direction",
        "stop_points_by_id",
        "timetable_by_id_from_stop",
        "timetable_by_id_from_to_stop",
    ],
)

meta_modes_snapshot = snapshot(
    [
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "bus",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "cable-car",
        },
        {
            "IsTflService": False,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "coach",
        },
        {
            "IsTflService": False,
            "IsFarePaying": False,
            "IsScheduledService": False,
            "ModeName": "cycle",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": False,
            "ModeName": "cycle-hire",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "dlr",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "elizabeth-line",
        },
        {
            "IsTflService": False,
            "IsFarePaying": False,
            "IsScheduledService": False,
            "ModeName": "interchange-keep-sitting",
        },
        {
            "IsTflService": False,
            "IsFarePaying": False,
            "IsScheduledService": False,
            "ModeName": "interchange-secure",
        },
        {
            "IsTflService": False,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "national-rail",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "overground",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "replacement-bus",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "river-bus",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "river-tour",
        },
        {
            "IsTflService": False,
            "IsFarePaying": False,
            "IsScheduledService": False,
            "ModeName": "taxi",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "tram",
        },
        {
            "IsTflService": True,
            "IsFarePaying": True,
            "IsScheduledService": True,
            "ModeName": "tube",
        },
        {
            "IsTflService": False,
            "IsFarePaying": False,
            "IsScheduledService": False,
            "ModeName": "walking",
        },
    ],
)
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
                },
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
                },
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
                },
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
                },
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
                },
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
                },
            ],
            "Crowding": {"PassengerFlows": [], "TrainLoadings": []},
        },
    ],
)


line_id_album = {
    "waterloo-city": wc_line_snapshot,
}

snapshot_album = {
    "meta_modes": meta_modes_snapshot,
    "lines_by_ids": line_id_album,
    "lines_by_modes": tube_line_snapshot,
}
