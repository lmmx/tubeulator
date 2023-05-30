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
class PlaceArray(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl-Api-Presentation-Entities-PlaceArray
    """
    _source_schema_name: str = 'BikePoint'
    _component_schema_name: str = 'Tfl-Api-Presentation-Entities-PlaceArray'
    
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
class Place(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl.Api.Presentation.Entities.Place
    """
    Id: str = None
    Url: str = None
    CommonName: str = None
    Distance: float = None
    PlaceType: str = None
    AdditionalProperties: list[AdditionalProperties] = field(default_factory=list)
    Children: list[Place] = field(default_factory=list)
    ChildrenUrls: list[str] = field(default_factory=list)
    Lat: float = None
    Lon: float = None
    _source_schema_name: str = 'BikePoint'
    _component_schema_name: str = 'Tfl.Api.Presentation.Entities.Place'
    
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
class AdditionalProperties(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl.Api.Presentation.Entities.AdditionalProperties
    """
    Category: str = None
    Key: str = None
    SourceSystemKey: str = None
    Value: str = None
    Modified: datetime = None
    _source_schema_name: str = 'BikePoint'
    _component_schema_name: str = 'Tfl.Api.Presentation.Entities.AdditionalProperties'
    
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
    Tfl_Api_Presentation_Entities_PlaceArray = PlaceArray
    Tfl__Api__Presentation__Entities__Place = Place
    Tfl__Api__Presentation__Entities__AdditionalProperties = AdditionalProperties