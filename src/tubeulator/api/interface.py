from .endpoint.names import EndpointNames
from .endpoint.routes import EndpointRoute
from .endpoint.routes.types import AnyEndpointRouteEnum
from .request import Path, Request

__all__ = ["EndpointInfo", "AllEndpointInterface", "fetch"]


class EndpointInfo:
    def __init__(self, endpoint: AnyEndpointRouteEnum):
        for route in endpoint.value:
            endpoint_name = EndpointNames[endpoint.name]
            request = Request(path=Path(endpoint=endpoint_name, route=route))
            setattr(self, route.name.lower(), request)


class AllEndpointInterface:
    def __init__(self):
        for endpoint in EndpointRoute:
            interface = EndpointInfo(endpoint=endpoint)
            setattr(self, endpoint.name.lower(), interface)


fetch = AllEndpointInterface()
