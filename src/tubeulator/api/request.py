from __future__ import annotations

from urllib.parse import urlencode

import httpx

__all__ = ["handle_request"]

def handle_request(url: str, credentials: dict[str,str]) -> httpx.Response:
    params = urlencode({"app_id": creds["app_id"], "app_key": creds["primary_key"]})
    response = httpx.get(url, params=params)
    return response
