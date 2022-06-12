# TfL Open API (v3) JSON

Files for all of the APIs except 
the Unified API (which was legacy)
and the separate API listed for v1 of the Lifts API.

Obtained manually (download on each API page by clicking the _API definition_ dropdown menu).
Notably these differ from the v1 Swagger JSON file, containing fewer errors. Below these errors are
listed.

The following 8 APIs had no errors
(as validated by the [Swagger Editor](https://editor.swagger.io/) web tool):

- AccidentStats
- AirQuality
- BikePoint
- Disruptions-Lifts-v2
- Mode
- occupancy
- Search
- Vehicle

The following 5 files had one or more Semantic errors...

- Journey (1)
- Line (1)
- Place (3)
- Road (2)
- StopPoint (8)

...specifically this identical error:

> Schemas with 'type: array', require a sibling 'items: ' field`.

These errors in more detail were:

- Journey
  - Line 156: Semantic error at `paths./JourneyResults/{from}/to/{to}.get.parameters.8.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  
- Line
  - Line 1002: Semantic error at `paths./Search/{query}.get.parameters.1.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  
- Place
  - Line 274: Semantic error at `paths./.get.parameters.3.schema`
    - The name of the parameter is `categories` and the description is comma-separated string
      of property categories (corresponding to `/Place/Meta/categories` endpoint)
      which can be passed as null or empty to return all properties,
      or as the keyword "none" to return no properties.
  - Line 290: Semantic error at `paths./.get.parameters.5.schema`
    - The name of the parameter is `type` and the description is
      _"Place types to filter on, or null to return all types"_,
      presumably a comma-separated string.
  - Line 430: Semantic error at `paths./Search.get.parameters.1.schema`
    - The name of the parameter is `types` and the description is
      _"A comma-separated list of the types to return. Max. approx 12 types"_.
      Corresponds to `/Meta/PlaceTypes`
  
- Road
  - Line 282: Semantic error at `paths./{ids}/Disruption.get.parameters.2.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  - Line 290: Semantic error at `paths./{ids}/Disruption.get.parameters.3.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  
- StopPoint
  - Line 479: Semantic error at `paths./ServiceTypes.get.parameters.1.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  - Line 487: Semantic error at `paths./ServiceTypes.get.parameters.2.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  - Line 1248: Semantic error at `paths./.get.parameters.5.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  - Line 1256: Semantic error at `paths./.get.parameters.6.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  - Line 1376: Semantic error at `paths./Search/{query}.get.parameters.1.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  - Line 1400: Semantic error at `paths./Search/{query}.get.parameters.4.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  - Line 1510: Semantic error at `paths./Search.get.parameters.1.schema`
    - The name of the parameter is `modes` and the description is comma-separated string
  - Line 1534: Semantic error at `paths./Search.get.parameters.4.schema`
    - The name of the parameter is `modes` and the description is comma-separated string

The `crowding` API was the only one with "structural" errors
(descriptions of the responses are `null` rather than a `string`).

- crowding
  - Line 32: Structural error at `paths./{Naptan}.get.responses.200.description`
  - Line 64: Structural error at `paths./{Naptan}/{DayOfWeek}.get.responses.200.description`
  - Line 87: Structural error at `paths./{Naptan}/Live.get.responses.200.description` 

## Naming the arbitrary identifiers

To name the arbitary incremented identifiers (`tfl`, `tfl-2`, `tfl-3`, etc.) it helps to note how
these are the refs for the responses for various endpoints, which gives a hint at what they are.

They are now numbered in a non-unified way, presumably just by order of appearance. So the `Place`
API has renamed the `Tfl.Api.Presentation.Entities.PlaceCategory` entity to `Tfl`,
`Tfl.Api.Presentation.Entities.Mode` to `Tfl-2`, etc.

Importantly, these entity identifiers are **inconsistent across APIs**.
In the `Line` API for example, what was `Tfl.Api.Presentation.Entities.Mode` becomes `Tfl`.

One simple way of 'expanding out' these and matching them up would be to use the `openai2jsonschema`
package, putting the results for each API into a subdirectory and then finding matching files
(presuming no entities have identical schemas).

This is not just an exercise in obtaining consistent identifiers for its own sake:
it makes it more concrete to say that for example the type of the array giving the semantic error at
line 430 of the `Places` API schema does not just 'correspond' to the `/Meta/PlaceTypes` result
type, but is in fact the same entity, with a name.

The following command finds exact matches between v1 and v3 of the Open API schemas, by:

- Iterating over the different APIs (each of which has its own directory) as `s`
- Iterating over the JSON schemas with arbitrary names in said API as `jj`
- Iterating over the JSON schemas with known names in the legacy 'unified' API as `j`

```sh
for s in */schemas; do
  pushd $s >/dev/null
  echo $s
    for jj in tfl*.json; do
      for j in ../../../tfl_openapi_v1/schemas/*.json; do
        diff $j $jj >/dev/null 2>&1
        if [ $? -eq 0 ]; then
          echo "$jj = $(basename $j)"
        fi
        done
   done
   popd >/dev/null
   echo
done
```
⇣
```
AccidentStats/schemas

AirQuality/schemas

BikePoint/schemas

crowding/schemas

Disruptions-Lifts-v2/schemas

Journey/schemas
tfl-14.json = linegroup.json
tfl-15.json = linemodegroup.json
tfl-27.json = farecaveat.json
tfl-2.json = pathattribute.json
tfl-33.json = lineservicetypeinfo.json
tfl-36.json = timeadjustment.json
tfl-39.json = journeyvector.json
tfl.json = mode.json

Line/schemas
tfl-18.json = lineservicetypeinfo.json
tfl-22.json = orderedroute.json
tfl-31.json = twentyfourhourclocktime.json
tfl-37.json = disambiguationoption.json
tfl-7.json = linegroup.json
tfl-8.json = linemodegroup.json
tfl.json = mode.json

Mode/schemas

occupancy/schemas

Place/schemas
tfl-8.json = linegroup.json
tfl-9.json = linemodegroup.json
tfl.json = placecategory.json
tfl.json = stoppointcategory.json

Road/schemas

Search/schemas

StopPoint/schemas
tfl-12.json = lineservicetypeinfo.json
tfl-2.json = mode.json
tfl-7.json = linegroup.json
tfl-8.json = linemodegroup.json
tfl.json = placecategory.json
tfl.json = stoppointcategory.json

Vehicle/schemas
```

Comparing this against the number of files in each of those directories:

```sh
for s in */schemas; do
  pushd $s >/dev/null
  echo $s
  ls tfl*.json 2>/dev/null | wc -l
  popd >/dev/null
  echo
done
```
⇣
```
AccidentStats/schemas
4

AirQuality/schemas
0

BikePoint/schemas
8

crowding/schemas
0

Disruptions-Lifts-v2/schemas
0

Journey/schemas
40

Line/schemas
41

Mode/schemas
8

occupancy/schemas
4

Place/schemas
10

Road/schemas
9

Search/schemas
2

StopPoint/schemas
22

Vehicle/schemas
3
```

This means this rudimentary matching is only able to name the following proportions of each file:

- AccidentStats: 0 of 4
- AirQuality: 0 of 0
- BikePoint: 0 of 8
- crowding: 0 of 0
- Disruptions-Lifts-v2: 0 of 0
- Journey: 8 of 40
- Line: 7 of 41
- Mode: 0 of 8
- occupancy: 0 of 4
- Place: 4 of 10
- Road: 0 of 9
- Search: 0 of 2
- StopPoint: 6 of 22
- Vehicle: 0 of 3
