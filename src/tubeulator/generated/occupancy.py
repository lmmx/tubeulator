import json
from typing import Any
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard
from dataclass_wizard.loaders import fromdict
import jsonschema
from ..utils.paths import load_endpoint_component_schemas

@dataclass
class BayDeserialiser(JSONWizard):
    """
    Autogenerated from occupancy::Tfl.Api.Presentation.Entities.Bay
    """
    BayType: str = None
    BayCount: int = None
    Free: int = None
    Occupied: int = None
    __source_schema_name: str = 'occupancy'
    __component_schema_name: str = 'Tfl'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class CarParkOccupancyDeserialiser(JSONWizard):
    """
    Autogenerated from occupancy::Tfl.Api.Presentation.Entities.CarParkOccupancy
    """
    Id: str = None
    Bays: list[dict] = field(default_factory=list)
    Name: str = None
    CarParkDetailsUrl: str = None
    __source_schema_name: str = 'occupancy'
    __component_schema_name: str = 'Tfl-2'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class ChargeConnectorOccupancyDeserialiser(JSONWizard):
    """
    Autogenerated from occupancy::Tfl.Api.Presentation.Entities.ChargeConnectorOccupancy
    """
    Id: int = None
    SourceSystemPlaceId: str = None
    Status: str = None
    __source_schema_name: str = 'occupancy'
    __component_schema_name: str = 'Tfl-3'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class BikePointOccupancyDeserialiser(JSONWizard):
    """
    Autogenerated from occupancy::Tfl.Api.Presentation.Entities.BikePointOccupancy
    """
    Id: str = None
    Name: str = None
    BikesCount: int = None
    EmptyDocks: int = None
    TotalDocks: int = None
    __source_schema_name: str = 'occupancy'
    __component_schema_name: str = 'Tfl-4'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class CarParkGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from occupancy::CarParkGet200ApplicationJsonResponse
    """
    __source_schema_name: str = 'occupancy'
    __component_schema_name: str = 'CarParkGet200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class ChargeConnectoridsGet200_or_ChargeConnectorGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from occupancy::ChargeConnector-ids-Get200ApplicationJsonResponse
    """
    __source_schema_name: str = 'occupancy'
    __component_schema_name: str = 'ChargeConnector-ids-Get200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class ChargeConnectoridsGet200_or_ChargeConnectorGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from occupancy::ChargeConnectorGet200ApplicationJsonResponse
    """
    __source_schema_name: str = 'occupancy'
    __component_schema_name: str = 'ChargeConnectorGet200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class BikePointsidsGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from occupancy::BikePoints-ids-Get200ApplicationJsonResponse
    """
    __source_schema_name: str = 'occupancy'
    __component_schema_name: str = 'BikePoints-ids-Get200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True