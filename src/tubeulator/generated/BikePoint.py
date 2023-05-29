import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard
from dataclass_wizard.loaders import fromdict
import jsonschema
from ..utils.paths import load_endpoint_component_schemas

@dataclass
class PlaceArrayDeserialiser(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl-Api-Presentation-Entities-PlaceArray
    """
    __source_schema_name: str = 'BikePoint'
    __component_schema_name: str = 'Tfl-Api-Presentation-Entities-PlaceArray'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    @classmethod
    def Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class PlaceDeserialiser(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl.Api.Presentation.Entities.Place
    """
    Id: str = None
    Url: str = None
    CommonName: str = None
    Distance: Any = None
    PlaceType: str = None
    AdditionalProperties: list[dict] = field(default_factory=list)
    Children: list[dict] = field(default_factory=list)
    ChildrenUrls: list[str] = field(default_factory=list)
    Lat: Any = None
    Lon: Any = None
    __source_schema_name: str = 'BikePoint'
    __component_schema_name: str = 'Tfl.Api.Presentation.Entities.Place'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    @classmethod
    def Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True


@dataclass
class AdditionalPropertiesDeserialiser(JSONWizard):
    """
    Autogenerated from BikePoint::Tfl.Api.Presentation.Entities.AdditionalProperties
    """
    Category: str = None
    Key: str = None
    SourceSystemKey: str = None
    Value: str = None
    Modified: str = None
    __source_schema_name: str = 'BikePoint'
    __component_schema_name: str = 'Tfl.Api.Presentation.Entities.AdditionalProperties'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls.__source_schema_name)
        schema = parent_schema[cls.__component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    @classmethod
    def Meta(JSONWizard.Meta):
        key_transform_with_load = "PASCAL"
        raise_on_unknown_json_key = True