from pathlib import Path

from httpx import Response

__all__ = ["RequestError"]


class RequestError(Exception):
    def __init__(self, response: Response, path: Path, *args, **kwargs):
        path_repr = f"{path.endpoint.name}:{path.route.value}"
        reason = f"{response.status_code} {response.reason_phrase}"
        message = f"HTTP error at {path_repr} ({list(args)}, {kwargs})\n  {reason}"
        try:
            message += f": {response.json()['message']}"
        except:
            pass
        self.message = message
        self.response = response
        super().__init__(self.message)
