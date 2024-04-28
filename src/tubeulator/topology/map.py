from .load import load_station_points

__all__ = ["show_station_points_map"]


def show_station_points_map(zoom: int = 12) -> None:
    """Create a map centered on London and plot all station points."""
    # TODO: ideally handle this using a Pydantic model `ImportPath`
    try:
        import folium
    except ImportError:
        raise ImportError(
            "Please install the folium package: `pip install tubeulator[folium]`.",
        )
    centre_of_london = [51.5074, -0.1278]
    map_style = "cartodbpositron"
    london_map = folium.Map(location=centre_of_london, zoom_start=zoom, tiles=map_style)
    coordinates = load_station_points()[["Lat", "Lon"]].to_numpy().tolist()
    for coord in coordinates:
        folium.Marker(location=coord).add_to(london_map)
    london_map.show_in_browser()
    return
