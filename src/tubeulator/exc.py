from contextlib import suppress
from pathlib import Path

from httpx import Response

__all__ = ["RequestError"]


class RequestError(Exception):
    def __init__(
        self,
        response: Response,
        path: Path,
        _args: tuple[str],
        _kwargs: dict[str, str],
    ):
        path_repr = f"{path.endpoint.name}.{path.route.name}:{path.route.value}"
        reason = f"{response.status_code} {response.reason_phrase}"
        message = f"HTTP error at {path_repr} ({list(_args)}, {_kwargs})\n  {reason}"
        with suppress(Exception):
            message += f": {response.json()['message']}"
        self.message = message
        self.response = response
        super().__init__(self.message)
