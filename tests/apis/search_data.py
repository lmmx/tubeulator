from inline_snapshot import snapshot

all_endpoints = snapshot(
    [
        "search",
        "bus_schedules",
        "meta_categories",
        "meta_search_providers",
        "meta_sorts",
    ],
)
