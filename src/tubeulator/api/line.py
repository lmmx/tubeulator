from __future__ import annotations

from .request import handle_request

__all__ = ["line_data"]

def line_data(creds: dict[str,str]):
    endpoint = "http://api.tfl.gov.uk/Line/"
    url = endpoint + "..."
    response = handle_request(url, creds)
