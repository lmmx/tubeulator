import json
from dataclasses import dataclass, field
from pathlib import Path
from dataclass_wizard import JSONWizard, LoadMeta
from dataclass_wizard.loaders import fromdict
import jsonschema

@dataclass
class PlaceCategoryDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.PlaceCategory
    """
    category: str = None
    availableKeys: list[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PlaceCategoryDeserialiser)


@dataclass
class ModeDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.Mode
    """
    isTflService: bool = None
    isFarePaying: bool = None
    isScheduledService: bool = None
    modeName: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ModeDeserialiser)


@dataclass
class PassengerFlowDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.PassengerFlow
    """
    timeSlice: str = None
    value: int = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PassengerFlowDeserialiser)


@dataclass
class TrainLoadingDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.TrainLoading
    """
    line: str = None
    lineDirection: str = None
    platformDirection: str = None
    direction: str = None
    naptanTo: str = None
    timeSlice: str = None
    value: int = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(TrainLoadingDeserialiser)


@dataclass
class CrowdingDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.Crowding
    """
    passengerFlows: list[dict] = field(default_factory=list)
    trainLoadings: list[dict] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(CrowdingDeserialiser)


@dataclass
class IdentifierDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.Identifier
    """
    id: str = None
    name: str = None
    uri: str = None
    fullName: str = None
    type: str = None
    crowding: dict = None
    routeType: str = None
    status: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(IdentifierDeserialiser)


@dataclass
class LineGroupDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.LineGroup
    """
    naptanIdReference: str = None
    stationAtcoCode: str = None
    lineIdentifier: list[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(LineGroupDeserialiser)


@dataclass
class LineModeGroupDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.LineModeGroup
    """
    modeName: str = None
    lineIdentifier: list[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(LineModeGroupDeserialiser)


@dataclass
class AdditionalPropertiesDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.AdditionalProperties
    """
    category: str = None
    key: str = None
    sourceSystemKey: str = None
    value: str = None
    modified: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(AdditionalPropertiesDeserialiser)


@dataclass
class PlaceDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.Place
    """
    id: str = None
    url: str = None
    commonName: str = None
    distance: Any = None
    placeType: str = None
    additionalProperties: list[dict] = field(default_factory=list)
    children: list[dict] = field(default_factory=list)
    childrenUrls: list[str] = field(default_factory=list)
    lat: Any = None
    lon: Any = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PlaceDeserialiser)


@dataclass
class StopPointDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.StopPoint
    """
    naptanId: str = None
    platformName: str = None
    indicator: str = None
    stopLetter: str = None
    modes: list[str] = field(default_factory=list)
    icsCode: str = None
    smsCode: str = None
    stopType: str = None
    stationNaptan: str = None
    accessibilitySummary: str = None
    hubNaptanCode: str = None
    lines: list[dict] = field(default_factory=list)
    lineGroup: list[dict] = field(default_factory=list)
    lineModeGroups: list[dict] = field(default_factory=list)
    fullName: str = None
    naptanMode: str = None
    status: bool = None
    id: str = None
    url: str = None
    commonName: str = None
    distance: Any = None
    placeType: str = None
    additionalProperties: list[dict] = field(default_factory=list)
    children: list[dict] = field(default_factory=list)
    childrenUrls: list[str] = field(default_factory=list)
    lat: Any = None
    lon: Any = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(StopPointDeserialiser)


@dataclass
class LineServiceTypeInfoDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.LineServiceTypeInfo
    """
    name: str = None
    uri: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(LineServiceTypeInfoDeserialiser)


@dataclass
class LineSpecificServiceTypeDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.LineSpecificServiceType
    """
    serviceType: dict = None
    stopServesServiceType: bool = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(LineSpecificServiceTypeDeserialiser)


@dataclass
class LineServiceTypeDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.LineServiceType
    """
    lineName: str = None
    lineSpecificServiceTypes: list[dict] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(LineServiceTypeDeserialiser)


@dataclass
class PredictionTimingDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.PredictionTiming
    """
    countdownServerAdjustment: str = None
    source: str = None
    insert: str = None
    read: str = None
    sent: str = None
    received: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PredictionTimingDeserialiser)


@dataclass
class PredictionDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.Prediction
    """
    id: str = None
    operationType: int = None
    vehicleId: str = None
    naptanId: str = None
    stationName: str = None
    lineId: str = None
    lineName: str = None
    platformName: str = None
    direction: str = None
    bearing: str = None
    destinationNaptanId: str = None
    destinationName: str = None
    timestamp: str = None
    timeToStation: int = None
    currentLocation: str = None
    towards: str = None
    expectedArrival: str = None
    timeToLive: str = None
    modeName: str = None
    timing: dict = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(PredictionDeserialiser)


@dataclass
class ArrivalDepartureDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.ArrivalDeparture
    """
    platformName: str = None
    destinationNaptanId: str = None
    destinationName: str = None
    naptanId: str = None
    stationName: str = None
    estimatedTimeOfArrival: str = None
    scheduledTimeOfArrival: str = None
    estimatedTimeOfDeparture: str = None
    scheduledTimeOfDeparture: str = None
    minutesAndSecondsToArrival: str = None
    minutesAndSecondsToDeparture: str = None
    cause: str = None
    departureStatus: str = None
    timing: dict = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ArrivalDepartureDeserialiser)


@dataclass
class StopPointRouteSectionDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.StopPointRouteSection
    """
    naptanId: str = None
    lineId: str = None
    mode: str = None
    validFrom: str = None
    validTo: str = None
    direction: str = None
    routeSectionName: str = None
    lineString: str = None
    isActive: bool = None
    serviceType: str = None
    vehicleDestinationText: str = None
    destinationName: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(StopPointRouteSectionDeserialiser)


@dataclass
class DisruptedPointDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.DisruptedPoint
    """
    atcoCode: str = None
    fromDate: str = None
    toDate: str = None
    description: str = None
    commonName: str = None
    type: str = None
    mode: str = None
    stationAtcoCode: str = None
    appearance: str = None
    additionalInformation: str = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(DisruptedPointDeserialiser)


@dataclass
class StopPointsResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.StopPointsResponse
    """
    centrePoint: list[Any] = field(default_factory=list)
    stopPoints: list[dict] = field(default_factory=list)
    pageSize: int = None
    total: int = None
    page: int = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(StopPointsResponseDeserialiser)


@dataclass
class SearchMatchDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.SearchMatch
    """
    id: str = None
    url: str = None
    name: str = None
    lat: Any = None
    lon: Any = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(SearchMatchDeserialiser)


@dataclass
class SearchResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Tfl.Api.Presentation.Entities.SearchResponse
    """
    query: str = None
    from: int = None
    page: int = None
    pageSize: int = None
    provider: str = None
    total: int = None
    matches: list[dict] = field(default_factory=list)
    maxScore: Any = None
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(SearchResponseDeserialiser)


@dataclass
class ObjectDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::System.Object
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ObjectDeserialiser)


@dataclass
class Get200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(Get200ApplicationJsonResponseDeserialiser)


@dataclass
class MetaCategoriesGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::MetaCategoriesGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(MetaCategoriesGet200ApplicationJsonResponseDeserialiser)


@dataclass
class MetaStopTypesDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::MetaStopTypesGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(MetaStopTypesDeserialiser)


@dataclass
class MetaModesGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::MetaModesGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(MetaModesGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::ids-Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idPlaceTypesGet200_or_stopPointIdTaxiRanksGet200_or_stopPointIdCarParksGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::id-PlaceTypesGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idPlaceTypesGet200_or_stopPointIdTaxiRanksGet200_or_stopPointIdCarParksGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::id-Crowding-line-Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Type-types-Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Type-types-Page-page-Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser)


@dataclass
class ServiceTypesGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::ServiceTypesGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ServiceTypesGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idArrivalsGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::id-ArrivalsGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idArrivalsGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idArrivalDeparturesGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::id-ArrivalDeparturesGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idArrivalDeparturesGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::id-CanReachOnLine-lineId-Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idsGet200_or_idCrowdinglineGet200_or_TypetypesGet200_or_TypetypesPagepageGet200_or_idCanReachOnLinelineIdGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idRouteGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::id-RouteGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idRouteGet200ApplicationJsonResponseDeserialiser)


@dataclass
class ModemodesDisruptionGet200_or_idsDisruptionGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::Mode-modes-DisruptionGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ModemodesDisruptionGet200_or_idsDisruptionGet200ApplicationJsonResponseDeserialiser)


@dataclass
class ModemodesDisruptionGet200_or_idsDisruptionGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::ids-DisruptionGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(ModemodesDisruptionGet200_or_idsDisruptionGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idDirectionTotoStopPointIdGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::id-DirectionTo-toStopPointId-Get200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idDirectionTotoStopPointIdGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idPlaceTypesGet200_or_stopPointIdTaxiRanksGet200_or_stopPointIdCarParksGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::stopPointId-TaxiRanksGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idPlaceTypesGet200_or_stopPointIdTaxiRanksGet200_or_stopPointIdCarParksGet200ApplicationJsonResponseDeserialiser)


@dataclass
class idPlaceTypesGet200_or_stopPointIdTaxiRanksGet200_or_stopPointIdCarParksGet200ApplicationJsonResponseDeserialiser(JSONWizard):
    """
    Autogenerated from StopPoint::stopPointId-CarParksGet200ApplicationJsonResponse
    """
    
    @classmethod
    def from_dict(cls, o):
        jsonschema.validate(o, schema)
        return fromdict(cls, o)


LoadMeta(raise_on_unknown_json_key=True).bind_to(idPlaceTypesGet200_or_stopPointIdTaxiRanksGet200_or_stopPointIdCarParksGet200ApplicationJsonResponseDeserialiser)
