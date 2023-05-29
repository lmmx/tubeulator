import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard
from dataclass_wizard.loaders import fromdict
import jsonschema
from ..utils.paths import load_endpoint_component_schemas, DtoEnum

@dataclass
class PlaceCategory(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.PlaceCategory
    """
    Category: str = None
    AvailableKeys: list[str] = field(default_factory=list)
    _source_schema_name: str = 'Place'
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
class AdditionalProperties(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.AdditionalProperties
    """
    Category: str = None
    Key: str = None
    SourceSystemKey: str = None
    Value: str = None
    Modified: str = None
    _source_schema_name: str = 'Place'
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
class Place(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.Place
    """
    Id: str = None
    Url: str = None
    CommonName: str = None
    Distance: float = None
    PlaceType: str = None
    AdditionalProperties: list[dict] = field(default_factory=list)
    Children: list[dict] = field(default_factory=list)
    ChildrenUrls: list[str] = field(default_factory=list)
    Lat: float = None
    Lon: float = None
    _source_schema_name: str = 'Place'
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
class PassengerFlow(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.PassengerFlow
    """
    TimeSlice: str = None
    Value: int = None
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Tfl-4'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class TrainLoading(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.TrainLoading
    """
    Line: str = None
    LineDirection: str = None
    PlatformDirection: str = None
    Direction: str = None
    NaptanTo: str = None
    TimeSlice: str = None
    Value: int = None
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Tfl-5'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class Crowding(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.Crowding
    """
    PassengerFlows: list[dict] = field(default_factory=list)
    TrainLoadings: list[dict] = field(default_factory=list)
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Tfl-6'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class Identifier(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.Identifier
    """
    Id: str = None
    Name: str = None
    Uri: str = None
    FullName: str = None
    Type: str = None
    Crowding: dict = None
    RouteType: str = None
    Status: str = None
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Tfl-7'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class LineGroup(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.LineGroup
    """
    NaptanIdReference: str = None
    StationAtcoCode: str = None
    LineIdentifier: list[str] = field(default_factory=list)
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Tfl-8'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class LineModeGroup(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.LineModeGroup
    """
    ModeName: str = None
    LineIdentifier: list[str] = field(default_factory=list)
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Tfl-9'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class StopPoint(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.StopPoint
    """
    NaptanId: str = None
    PlatformName: str = None
    Indicator: str = None
    StopLetter: str = None
    Modes: list[str] = field(default_factory=list)
    IcsCode: str = None
    SmsCode: str = None
    StopType: str = None
    StationNaptan: str = None
    AccessibilitySummary: str = None
    HubNaptanCode: str = None
    Lines: list[dict] = field(default_factory=list)
    LineGroup: list[dict] = field(default_factory=list)
    LineModeGroups: list[dict] = field(default_factory=list)
    FullName: str = None
    NaptanMode: str = None
    Status: bool = None
    Id: str = None
    Url: str = None
    CommonName: str = None
    Distance: float = None
    PlaceType: str = None
    AdditionalProperties: list[dict] = field(default_factory=list)
    Children: list[dict] = field(default_factory=list)
    ChildrenUrls: list[str] = field(default_factory=list)
    Lat: float = None
    Lon: float = None
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Tfl-10'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class Object(JSONWizard):
    """
    Autogenerated from Place::System.Object
    """
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'System'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class MetaCategoriesGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Place::MetaCategoriesGet200ApplicationJsonResponse
    """
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'MetaCategoriesGet200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class Get200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Place::Get200ApplicationJsonResponse
    """
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Get200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class MetaPlaceTypesGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Place::MetaPlaceTypesGet200ApplicationJsonResponse
    """
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'MetaPlaceTypesGet200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class TypetypesGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Place::Type-types-Get200ApplicationJsonResponse
    """
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Type-types-Get200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class idGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Place::id-Get200ApplicationJsonResponse
    """
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'id-Get200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Place::Get200ApplicationJsonResponse-1
    """
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'Get200ApplicationJsonResponse-1'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


@dataclass
class SearchGet200ApplicationJsonResponse(JSONWizard):
    """
    Autogenerated from Place::SearchGet200ApplicationJsonResponse
    """
    _source_schema_name: str = 'Place'
    _component_schema_name: str = 'SearchGet200ApplicationJsonResponse'
    
    @classmethod
    def from_dict(cls, o):
        parent_schema = load_endpoint_component_schemas(cls._source_schema_name)
        schema = parent_schema[cls._component_schema_name]
        jsonschema.validate(o, schema)
        return fromdict(cls, o)
    
    class Meta(JSONWizard.Meta):
        key_transform_with_load = 'PASCAL'


class Deserialisers(DtoEnum):
    Tfl = PlaceCategory
    Tfl_2 = AdditionalProperties
    Tfl_3 = Place
    Tfl_4 = PassengerFlow
    Tfl_5 = TrainLoading
    Tfl_6 = Crowding
    Tfl_7 = Identifier
    Tfl_8 = LineGroup
    Tfl_9 = LineModeGroup
    Tfl_10 = StopPoint
    System = Object
    MetaCategoriesGet200ApplicationJsonResponse = MetaCategoriesGet200ApplicationJsonResponse
    Get200ApplicationJsonResponse = Get200ApplicationJsonResponse
    MetaPlaceTypesGet200ApplicationJsonResponse = MetaPlaceTypesGet200ApplicationJsonResponse
    Type_types_Get200ApplicationJsonResponse = TypetypesGet200ApplicationJsonResponse
    id_Get200ApplicationJsonResponse = idGet200ApplicationJsonResponse
    Get200ApplicationJsonResponse_1 = ApplicationJsonResponse
    SearchGet200ApplicationJsonResponse = SearchGet200ApplicationJsonResponse