from __future__ import annotations
import json
from datetime import datetime
from dataclasses import dataclass, field
from tubeulator.utils.string_conv import to_camel_case
from pydantic import AliasGenerator, BaseModel, ConfigDict, PrivateAttr
from ..utils.paths import DtoEnum

class SearchMatch(BaseModel):
    """
    Autogenerated from Search::Tfl.Api.Presentation.Entities.SearchMatch
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    Id: str = None
    Url: str = None
    Name: str = None
    Lat: float = None
    Lon: float = None
    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='Tfl')


SearchMatchModel = SearchMatch


class SearchResponse(BaseModel):
    """
    Autogenerated from Search::Tfl.Api.Presentation.Entities.SearchResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    Query: str = None
    From: int = None
    Page: int = None
    PageSize: int = None
    Provider: str = None
    Total: int = None
    Matches: list["SearchMatchModel"] = []
    MaxScore: float = None
    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='Tfl-2')


SearchResponseModel = SearchResponse


class MetaSearchProviders(BaseModel):
    """
    Autogenerated from Search::MetaSearchProvidersGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='MetaSearchProvidersGet200ApplicationJsonResponse')


MetaSearchProvidersModel = MetaSearchProviders


class MetaCategories(BaseModel):
    """
    Autogenerated from Search::MetaCategoriesGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='MetaCategoriesGet200ApplicationJsonResponse')


MetaCategoriesModel = MetaCategories


class MetaSorts(BaseModel):
    """
    Autogenerated from Search::MetaSortsGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='MetaSortsGet200ApplicationJsonResponse')


MetaSortsModel = MetaSorts


class Deserialisers(DtoEnum):
    Tfl = SearchMatch
    Tfl_2 = SearchResponse
    MetaSearchProvidersGet200ApplicationJsonResponse = MetaSearchProviders
    MetaCategoriesGet200ApplicationJsonResponse = MetaCategories
    MetaSortsGet200ApplicationJsonResponse = MetaSorts