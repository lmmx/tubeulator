import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard, LoadMeta
from dataclass_wizard.loaders import fromdict
import jsonschema

@dataclass
class PlaceCategoryDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.PlaceCategory
    """
    Category: str = None
    AvailableKeys: list[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PlaceCategoryDeserialiser)


@dataclass
class AdditionalPropertiesDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.AdditionalProperties
    """
    Category: str = None
    Key: str = None
    SourceSystemKey: str = None
    Value: str = None
    Modified: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(AdditionalPropertiesDeserialiser)


@dataclass
class PlaceDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.Place
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
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PlaceDeserialiser)


@dataclass
class PassengerFlowDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.PassengerFlow
    """
    TimeSlice: str = None
    Value: int = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PassengerFlowDeserialiser)


@dataclass
class TrainLoadingDeserialiser(JSONWizard):
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
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TrainLoadingDeserialiser)


@dataclass
class CrowdingDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.Crowding
    """
    PassengerFlows: list[dict] = field(default_factory=list)
    TrainLoadings: list[dict] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(CrowdingDeserialiser)


@dataclass
class IdentifierDeserialiser(JSONWizard):
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
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(IdentifierDeserialiser)


@dataclass
class LineGroupDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.LineGroup
    """
    NaptanIdReference: str = None
    StationAtcoCode: str = None
    LineIdentifier: list[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(LineGroupDeserialiser)


@dataclass
class LineModeGroupDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.LineModeGroup
    """
    ModeName: str = None
    LineIdentifier: list[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(LineModeGroupDeserialiser)


@dataclass
class StopPointDeserialiser(JSONWizard):
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
    Distance: Any = None
    PlaceType: str = None
    AdditionalProperties: list[dict] = field(default_factory=list)
    Children: list[dict] = field(default_factory=list)
    ChildrenUrls: list[str] = field(default_factory=list)
    Lat: Any = None
    Lon: Any = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(StopPointDeserialiser)


@dataclass
class ObjectDeserialiser(JSONWizard):
    """
    Autogenerated from Place::System.Object
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ObjectDeserialiser)


@dataclass
class MetaCategoriesGet200_or_MetaPlaceTypesGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Place::MetaCategoriesGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(MetaCategoriesGet200_or_MetaPlaceTypesGet200ApplicationJsonResponseDeserialiser)


@dataclass
class Get200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(Get200ApplicationJsonResponseDeserialiser)


@dataclass
class MetaCategoriesGet200_or_MetaPlaceTypesGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Place::MetaPlaceTypesGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(MetaCategoriesGet200_or_MetaPlaceTypesGet200ApplicationJsonResponseDeserialiser)


@dataclass
class TypetypesGet200_or_idGet200_or_SearchGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Type-types-Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TypetypesGet200_or_idGet200_or_SearchGet200ApplicationJsonResponseDeserialiser)


@dataclass
class TypetypesGet200_or_idGet200_or_SearchGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Place::id-Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TypetypesGet200_or_idGet200_or_SearchGet200ApplicationJsonResponseDeserialiser)


@dataclass
class ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Place::Get200ApplicationJsonResponse-1
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ApplicationJsonResponseDeserialiser)


@dataclass
class TypetypesGet200_or_idGet200_or_SearchGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from Place::SearchGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TypetypesGet200_or_idGet200_or_SearchGet200ApplicationJsonResponseDeserialiser)
