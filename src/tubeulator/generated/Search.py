from __future__ import annotations
import json
from datetime import datetime
from dataclasses import dataclass, field
from dataclass_wizard.utils.string_conv import to_camel_case
from pydantic import AliasGenerator, BaseModel, ConfigDict, PrivateAttr
from ..utils.paths import DtoEnum

class SearchMatch(BaseModel):
    """
    Autogenerated from Search::Tfl.Api.Presentation.Entities.SearchMatch
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case)
    )

    Id: str = None
    Url: str = None
    Name: str = None
    Lat: float = None
    Lon: float = None
    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='Tfl')



class SearchResponse(BaseModel):
    """
    Autogenerated from Search::Tfl.Api.Presentation.Entities.SearchResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case)
    )

    Query: str = None
    From: int = None
    Page: int = None
    PageSize: int = None
    Provider: str = None
    Total: int = None
    Matches: list["SearchMatch"] = field(default_factory=list)
    MaxScore: float = None
    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='Tfl-2')



class MetaSearchProviders(BaseModel):
    """
    Autogenerated from Search::MetaSearchProvidersGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case)
    )

    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='MetaSearchProvidersGet200ApplicationJsonResponse')



class MetaCategories(BaseModel):
    """
    Autogenerated from Search::MetaCategoriesGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case)
    )

    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='MetaCategoriesGet200ApplicationJsonResponse')



class MetaSorts(BaseModel):
    """
    Autogenerated from Search::MetaSortsGet200ApplicationJsonResponse
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case)
    )

    _source_schema_name: str = PrivateAttr(default='Search')
    _component_schema_name: str = PrivateAttr(default='MetaSortsGet200ApplicationJsonResponse')



class Deserialisers(DtoEnum):
    Tfl = SearchMatch
    Tfl_2 = SearchResponse
    MetaSearchProvidersGet200ApplicationJsonResponse = MetaSearchProviders
    MetaCategoriesGet200ApplicationJsonResponse = MetaCategories
    MetaSortsGet200ApplicationJsonResponse = MetaSorts