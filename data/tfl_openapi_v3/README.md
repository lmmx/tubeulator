# TfL Open API (v3) JSON

Files for all of the APIs except 
the Unified API (which was legacy)
and the separate API listed for v1 of the Lifts API.

Obtained manually (download on each API page by clicking the _API definition_ dropdown menu).
Notably these differ from the v1 Swagger JSON file, containing fewer errors. Below these errors are
listed.

The errors are all the same:

> Schemas with 'type: array', require a sibling 'items: ' field`.

Except for `crowding` which has "structural" errors (descriptions of the responses are `null` rather
than a `string`).

## AccidentStats

- No errors

## AirQuality

- No errors

## BikePoint

- No errors

## crowding

- 3 errors
  - Line 32: Structural error at `paths./{Naptan}.get.responses.200.description`
  - Line 64: Structural error at `paths./{Naptan}/{DayOfWeek}.get.responses.200.description`
  - Line 87: Structural error at `paths./{Naptan}/Live.get.responses.200.description`

## Disruptions-Lifts-v2

- No errors

## Journey

- 1 error
  - Line 156: Semantic error at `paths./JourneyResults/{from}/to/{to}.get.parameters.8.schema`

## Line

- 1 error
  - Line 1002: Semantic error at `paths./Search/{query}.get.parameters.1.schema`

## Mode

- No errors

## occupancy

- No errors

## Place

- 3 errors
  - Line 274: Semantic error at `paths./.get.parameters.3.schema`
  - Line 290: Semantic error at `paths./.get.parameters.5.schema`
  - Line 430: Semantic error at `paths./Search.get.parameters.1.schema`

## Road

- 2 errors
  - Line 282: Semantic error at `paths./{ids}/Disruption.get.parameters.2.schema`
  - Line 290: Semantic error at `paths./{ids}/Disruption.get.parameters.3.schema`

## Search

- No errors

## StopPoint

- 8 errors
  - Line 479: Semantic error at `paths./ServiceTypes.get.parameters.1.schema`
  - Line 487: Semantic error at `paths./ServiceTypes.get.parameters.2.schema`
  - Line 1248: Semantic error at `paths./.get.parameters.5.schema`
  - Line 1256: Semantic error at `paths./.get.parameters.6.schema`
  - Line 1376: Semantic error at `paths./Search/{query}.get.parameters.1.schema`
  - Line 1400: Semantic error at `paths./Search/{query}.get.parameters.4.schema`
  - Line 1510: Semantic error at `paths./Search.get.parameters.1.schema`
  - Line 1534: Semantic error at `paths./Search.get.parameters.4.schema`

## Vehicle

- No errors
