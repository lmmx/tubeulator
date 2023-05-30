from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard
from dataclass_wizard.loaders import fromdict
import jsonschema
from ..utils.paths import load_endpoint_component_schemas, DtoEnum

@dataclass
class PredictionTiming(JSONWizard):
    """
    Autogenerated from Vehicle::Tfl.Api.Presentation.Entities.PredictionTiming
    """
    CountdownServerAdjustment: str = None
    Source: str = None
    Insert: str = None
    Read: str = None
    Sent: str = None
    Received: str = None
    _source_schema_name: str = 'Vehicle'
    _component_schema_name: str = 'Tfl'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class Prediction(JSONWizard):
    """
    Autogenerated from Vehicle::Tfl.Api.Presentation.Entities.Prediction
    """
    Id: str = None
    OperationType: int = None
    VehicleId: str = None
    NaptanId: str = None
    StationName: str = None
    LineId: str = None
    LineName: str = None
    PlatformName: str = None
    Direction: str = None
    Bearing: str = None
    DestinationNaptanId: str = None
    DestinationName: str = None
    Timestamp: str = None
    TimeToStation: int = None
    CurrentLocation: str = None
    Towards: str = None
    ExpectedArrival: str = None
    TimeToLive: str = None
    ModeName: str = None
    Timing: dict = None
    _source_schema_name: str = 'Vehicle'
    _component_schema_name: str = 'Tfl-2'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class VehicleMatch(JSONWizard):
    """
    Autogenerated from Vehicle::Tfl.Api.Presentation.Entities.VehicleMatch
    """
    Vrm: str = None
    Type: str = None
    Make: str = None
    Model: str = None
    Colour: str = None
    Compliance: str = None
    _source_schema_name: str = 'Vehicle'
    _component_schema_name: str = 'Tfl-3'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class idsArrivalsGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Vehicle::ids-ArrivalsGet200ApplicationJsonResponse
    """
    _source_schema_name: str = 'Vehicle'
    _component_schema_name: str = 'ids-ArrivalsGet200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


class Deserialisers(DtoEnum):
    Tfl = PredictionTiming
    Tfl_2 = Prediction
    Tfl_3 = VehicleMatch
    ids_ArrivalsGet200ApplicationJsonResponse = idsArrivalsGet200ApplicationJsonResponse