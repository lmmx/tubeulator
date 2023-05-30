from __future__ import annotations
import json
from datetime import datetime
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard
from dataclass_wizard.loaders import fromdict
import jsonschema
from ..utils.paths import load_endpoint_component_schemas, DtoEnum

@dataclass
class Bay(JSONWizard):
    """
    Autogenerated from occupancy::Tfl.Api.Presentation.Entities.Bay
    """
    BayType: str = None
    BayCount: int = None
    Free: int = None
    Occupied: int = None
    _source_schema_name: str = 'occupancy'
    _component_schema_name: str = 'Tfl'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class CarParkOccupancy(JSONWizard):
    """
    Autogenerated from occupancy::Tfl.Api.Presentation.Entities.CarParkOccupancy
    """
    Id: str = None
    Bays: list[Bay] = field(default_factory=list)
    Name: str = None
    CarParkDetailsUrl: str = None
    _source_schema_name: str = 'occupancy'
    _component_schema_name: str = 'Tfl-2'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class ChargeConnectorOccupancy(JSONWizard):
    """
    Autogenerated from occupancy::Tfl.Api.Presentation.Entities.ChargeConnectorOccupancy
    """
    Id: int = None
    SourceSystemPlaceId: str = None
    Status: str = None
    _source_schema_name: str = 'occupancy'
    _component_schema_name: str = 'Tfl-3'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class BikePointOccupancy(JSONWizard):
    """
    Autogenerated from occupancy::Tfl.Api.Presentation.Entities.BikePointOccupancy
    """
    Id: str = None
    Name: str = None
    BikesCount: int = None
    EmptyDocks: int = None
    TotalDocks: int = None
    _source_schema_name: str = 'occupancy'
    _component_schema_name: str = 'Tfl-4'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class CarParkGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from occupancy::CarParkGet200ApplicationJsonResponse
    """
    _source_schema_name: str = 'occupancy'
    _component_schema_name: str = 'CarParkGet200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class ChargeConnectoridsGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from occupancy::ChargeConnector-ids-Get200ApplicationJsonResponse
    """
    _source_schema_name: str = 'occupancy'
    _component_schema_name: str = 'ChargeConnector-ids-Get200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class ChargeConnectorGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from occupancy::ChargeConnectorGet200ApplicationJsonResponse
    """
    _source_schema_name: str = 'occupancy'
    _component_schema_name: str = 'ChargeConnectorGet200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


@dataclass
class BikePointsidsGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from occupancy::BikePoints-ids-Get200ApplicationJsonResponse
    """
    _source_schema_name: str = 'occupancy'
    _component_schema_name: str = 'BikePoints-ids-Get200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'
        recursive_classes = True


class Deserialisers(DtoEnum):
    Tfl = Bay
    Tfl_2 = CarParkOccupancy
    Tfl_3 = ChargeConnectorOccupancy
    Tfl_4 = BikePointOccupancy
    CarParkGet200ApplicationJsonResponse = CarParkGet200ApplicationJsonResponse
    ChargeConnector_ids_Get200ApplicationJsonResponse = ChargeConnectoridsGet200ApplicationJsonResponse
    ChargeConnectorGet200ApplicationJsonResponse = ChargeConnectorGet200ApplicationJsonResponse
    BikePoints_ids_Get200ApplicationJsonResponse = BikePointsidsGet200ApplicationJsonResponse