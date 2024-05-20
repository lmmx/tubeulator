from inline_snapshot import snapshot

all_endpoints = snapshot(
    [
        "all_roads",
        "meta_categories",
        "meta_severities",
        "disruption_by_ids",
        "street_disruption",
        "road_by_ids",
        "road_disruption",
        "road_status",
    ],
)
