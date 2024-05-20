from inline_snapshot import snapshot

all_endpoints = snapshot(
    [
        "places_by_geo_region",
        "forward_requests",
        "meta_categories",
        "meta_place_types",
        "search_places",
        "places_by_type",
        "place_by_id",
        "place_by_type_at_coordinates",
    ],
)
