from __future__ import annotations

from urllib.parse import urlencode

import httpx

__all__ = ["tfl_request"]


def tfl_request(endpoint: str, credentials: dict[str, str]) -> httpx.Response:
    url = f"https://api.tfl.gov.uk/{endpoint}"
    params = urlencode(
        {"app_id": credentials["app_id"], "app_key": credentials["primary_key"]}
    )
    response = httpx.get(url, params=params)
    return response
