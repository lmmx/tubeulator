from __future__ import annotations
import json
from datetime import datetime
from dataclasses import dataclass, field
from tubeulator.utils.string_conv import to_camel_case
from pydantic import AliasGenerator, BaseModel, ConfigDict, PrivateAttr
from ..utils.paths import DtoEnum

class PlaceCategory(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.PlaceCategory
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    Category: str = None
    AvailableKeys: list[str] = []
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl')


PlaceCategoryModel = PlaceCategory


class AdditionalProperties(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.AdditionalProperties
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    Category: str = None
    Key: str = None
    SourceSystemKey: str = None
    Value: str = None
    Modified: datetime = None
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-2')


AdditionalPropertiesModel = AdditionalProperties


class Place(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.Place
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    Id: str = None
    Url: str = None
    CommonName: str = None
    Distance: float = None
    PlaceType: str = None
    AdditionalProperties: list["AdditionalPropertiesModel"] = []
    Children: list["PlaceModel"] = []
    ChildrenUrls: list[str] = []
    Lat: float = None
    Lon: float = None
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-3')


PlaceModel = Place


class PassengerFlow(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.PassengerFlow
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    TimeSlice: str = None
    Value: int = None
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-4')


PassengerFlowModel = PassengerFlow


class TrainLoading(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.TrainLoading
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    Line: str = None
    LineDirection: str = None
    PlatformDirection: str = None
    Direction: str = None
    NaptanTo: str = None
    TimeSlice: str = None
    Value: int = None
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-5')


TrainLoadingModel = TrainLoading


class Crowding(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.Crowding
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    PassengerFlows: list["PassengerFlowModel"] = []
    TrainLoadings: list["TrainLoadingModel"] = []
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-6')


CrowdingModel = Crowding


class Identifier(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.Identifier
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    Id: str = None
    Name: str = None
    Uri: str = None
    FullName: str = None
    Type: str = None
    Crowding: CrowdingModel = None
    RouteType: str = None
    Status: str = None
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-7')


IdentifierModel = Identifier


class LineGroup(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.LineGroup
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    NaptanIdReference: str = None
    StationAtcoCode: str = None
    LineIdentifier: list[str] = []
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-8')


LineGroupModel = LineGroup


class LineModeGroup(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.LineModeGroup
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    ModeName: str = None
    LineIdentifier: list[str] = []
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-9')


LineModeGroupModel = LineModeGroup


class StopPoint(BaseModel):
    """
    Autogenerated from Place::Tfl.Api.Presentation.Entities.StopPoint
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    NaptanId: str = None
    PlatformName: str = None
    Indicator: str = None
    StopLetter: str = None
    Modes: list[str] = []
    IcsCode: str = None
    SmsCode: str = None
    StopType: str = None
    StationNaptan: str = None
    AccessibilitySummary: str = None
    HubNaptanCode: str = None
    Lines: list["IdentifierModel"] = []
    LineGroup: list["LineGroupModel"] = []
    LineModeGroups: list["LineModeGroupModel"] = []
    FullName: str = None
    NaptanMode: str = None
    Status: bool = None
    Id: str = None
    Url: str = None
    CommonName: str = None
    Distance: float = None
    PlaceType: str = None
    AdditionalProperties: list["AdditionalPropertiesModel"] = []
    Children: list["PlaceModel"] = []
    ChildrenUrls: list[str] = []
    Lat: float = None
    Lon: float = None
    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Tfl-10')


StopPointModel = StopPoint


class Object(BaseModel):
    """
    Autogenerated from Place::System.Object
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='System')


ObjectModel = Object


class MetaCategoriesGet200ApplicationJsonResponse(BaseModel):
    """
    Autogenerated from Place::MetaCategoriesGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='MetaCategoriesGet200ApplicationJsonResponse')


MetaCategoriesGet200ApplicationJsonResponseModel = MetaCategoriesGet200ApplicationJsonResponse


class Get200ApplicationJsonResponse(BaseModel):
    """
    Autogenerated from Place::Get200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Get200ApplicationJsonResponse')


Get200ApplicationJsonResponseModel = Get200ApplicationJsonResponse


class MetaPlaceTypesGet200ApplicationJsonResponse(BaseModel):
    """
    Autogenerated from Place::MetaPlaceTypesGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='MetaPlaceTypesGet200ApplicationJsonResponse')


MetaPlaceTypesGet200ApplicationJsonResponseModel = MetaPlaceTypesGet200ApplicationJsonResponse


class TypetypesGet200ApplicationJsonResponse(BaseModel):
    """
    Autogenerated from Place::Type-types-Get200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Type-types-Get200ApplicationJsonResponse')


TypetypesGet200ApplicationJsonResponseModel = TypetypesGet200ApplicationJsonResponse


class idGet200ApplicationJsonResponse(BaseModel):
    """
    Autogenerated from Place::id-Get200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='id-Get200ApplicationJsonResponse')


idGet200ApplicationJsonResponseModel = idGet200ApplicationJsonResponse


class ApplicationJsonResponse(BaseModel):
    """
    Autogenerated from Place::Get200ApplicationJsonResponse-1
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='Get200ApplicationJsonResponse-1')


ApplicationJsonResponseModel = ApplicationJsonResponse


class SearchGet200ApplicationJsonResponse(BaseModel):
    """
    Autogenerated from Place::SearchGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Place')
    _component_schema_name: str = PrivateAttr(default='SearchGet200ApplicationJsonResponse')


SearchGet200ApplicationJsonResponseModel = SearchGet200ApplicationJsonResponse


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