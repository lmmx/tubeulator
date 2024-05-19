import random

from .combine import load_station_points_with_lines

__all__ = ["show_station_points_map"]


def get_line_colour(line):
    line2colour = {
        "london-cable-car": "#D799AF",  # Light purple
        "dlr": "#00AFAD",  # Turquoise
        "thameslink": "#0019A8",  # Dark blue
        "national-rail": "#A0A5A9",  # Silver
        "london-overground": "#E86A10",  # Orange
        "elizabeth": "#5A4799",  # Purple
        "tram": "#00BD19",  # Green
        "bakerloo": "#B36305",  # Brown
        "central": "#E32017",  # Red
        "circle": "#FFD300",  # Yellow
        "district": "#00782A",  # Green
        "hammersmith-city": "#F3A9BB",  # Pink
        "jubilee": "#868F98",  # Grey
        "metropolitan": "#9B0056",  # Magenta
        "northern": "#000000",  # Black
        "piccadilly": "#003688",  # Dark blue
        "victoria": "#0098D4",  # Light blue
        "waterloo-city": "#93CEBA",  # Pale turquoise
    }
    return line2colour[line]


def show_station_points_map(zoom: int = 12) -> None:
    """Create a map centered on London and plot all station points."""
    # TODO: ideally handle this using a Pydantic model `ImportPath`
    try:
        import folium as fl
    except ImportError:
        raise ImportError(
            "Please install the folium package: `pip install tubeulator[folium]`.",
        )
    centre_of_london = [51.5074, -0.1278]
    map_style = "cartodbpositron"
    london_map = fl.Map(location=centre_of_london, zoom_start=zoom, tiles=map_style)
    stn_points = load_station_points_with_lines()
    for stp in stn_points.to_dicts():
        coord = [stp["Lat"], stp["Lon"]]
        pt_name = stp["FriendlyName"]
        stn_name = stp["StationName"]
        lines = ", ".join([l.title() for l in stp["Lines"]])
        popup_text = f"{pt_name} at {stn_name} ({lines})"
        marker_colour = get_line_colour(random.choice(stp["Lines"]))
        styled_icon = fl.Icon(color="white", icon_color=marker_colour)
        fl.Marker(location=coord, popup=popup_text, icon=styled_icon).add_to(london_map)
    london_map.show_in_browser()
    return
