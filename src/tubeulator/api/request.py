from __future__ import annotations

from urllib.parse import urlencode

import httpx

__all__ = ["handle_request"]


def handle_request(url: str, credentials: dict[str, str]) -> httpx.Response:
    params = urlencode(
        {"app_id": credentials["app_id"], "app_key": credentials["primary_key"]}
    )
    response = httpx.get(url, params=params)
    return response
