from __future__ import annotations
import json
from datetime import datetime
from dataclasses import dataclass, field
from tubeulator.utils.string_conv import to_camel_case
from pydantic import AliasGenerator, BaseModel, ConfigDict, PrivateAttr
from ..utils.paths import DtoEnum

class ActiveServiceTypeArray(BaseModel):
    """
    Autogenerated from Mode::Tfl-Api-Presentation-Entities-ActiveServiceTypeArray
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Mode')
    _component_schema_name: str = PrivateAttr(default='Tfl-Api-Presentation-Entities-ActiveServiceTypeArray')



class ActiveServiceType(BaseModel):
    """
    Autogenerated from Mode::Tfl.Api.Presentation.Entities.ActiveServiceType
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    Mode: str = None
    ServiceType: str = None
    _source_schema_name: str = PrivateAttr(default='Mode')
    _component_schema_name: str = PrivateAttr(default='Tfl.Api.Presentation.Entities.ActiveServiceType')



class PredictionArray(BaseModel):
    """
    Autogenerated from Mode::Tfl-Api-Presentation-Entities-PredictionArray-4
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    _source_schema_name: str = PrivateAttr(default='Mode')
    _component_schema_name: str = PrivateAttr(default='Tfl-Api-Presentation-Entities-PredictionArray-4')



class Prediction(BaseModel):
    """
    Autogenerated from Mode::Tfl.Api.Presentation.Entities.Prediction
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

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
    Timestamp: datetime = None
    TimeToStation: int = None
    CurrentLocation: str = None
    Towards: str = None
    ExpectedArrival: datetime = None
    TimeToLive: datetime = None
    ModeName: str = None
    Timing: PredictionTiming = None
    _source_schema_name: str = PrivateAttr(default='Mode')
    _component_schema_name: str = PrivateAttr(default='Tfl.Api.Presentation.Entities.Prediction')



class PredictionTiming(BaseModel):
    """
    Autogenerated from Mode::Tfl.Api.Presentation.Entities.PredictionTiming
    """

    model_config = ConfigDict(
        alias_generator=AliasGenerator(validation_alias=to_camel_case),
    )

    CountdownServerAdjustment: str = None
    Source: datetime = None
    Insert: datetime = None
    Read: datetime = None
    Sent: datetime = None
    Received: datetime = None
    _source_schema_name: str = PrivateAttr(default='Mode')
    _component_schema_name: str = PrivateAttr(default='Tfl.Api.Presentation.Entities.PredictionTiming')



class Deserialisers(DtoEnum):
    Tfl_Api_Presentation_Entities_ActiveServiceTypeArray = ActiveServiceTypeArray
    Tfl__Api__Presentation__Entities__ActiveServiceType = ActiveServiceType
    Tfl_Api_Presentation_Entities_PredictionArray_4 = PredictionArray
    Tfl__Api__Presentation__Entities__Prediction = Prediction
    Tfl__Api__Presentation__Entities__PredictionTiming = PredictionTiming