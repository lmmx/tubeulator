# Naming the arbitrary identifiers

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
      for j in ../../../openapi_unified/ReleasedUnifiedAPIProd/schemas/*.json; do
        diff $j $jj >/dev/null 2>&1
        if [ $? -eq 0 ]; then
          echo "$jj = $(basename $j)" | grep -v "tfl-api-presentation-entities"
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
tfl-11.json = jpelevation.json
tfl-14.json = linegroup.json
tfl-15.json = linemodegroup.json
tfl-16.json = additionalproperties.json
tfl-22.json = plannedwork.json
tfl-24.json = faretapdetails.json
tfl-27.json = farecaveat.json
tfl-2.json = pathattribute.json
tfl-30.json = validityperiod.json
tfl-32.json = matchedroute.json
tfl-33.json = lineservicetypeinfo.json
tfl-35.json = journeyplannercyclehiredockingstationdata.json
tfl-36.json = timeadjustment.json
tfl-39.json = journeyvector.json
tfl-5.json = obstacle.json
tfl-6.json = point.json
tfl-7.json = passengerflow.json
tfl-8.json = trainloading.json
tfl.json = mode.json

Line/schemas
tfl-15.json = validityperiod.json
tfl-17.json = matchedroute.json
tfl-18.json = lineservicetypeinfo.json
tfl-22.json = orderedroute.json
tfl-24.json = lineroutesection.json
tfl-25.json = matchedroutesections.json
tfl-28.json = interval.json
tfl-2.json = statusseverity.json
tfl-30.json = knownjourney.json
tfl-31.json = twentyfourhourclocktime.json
tfl-32.json = servicefrequency.json
tfl-37.json = disambiguationoption.json
tfl-3.json = passengerflow.json
tfl-40.json = predictiontiming.json
tfl-4.json = trainloading.json
tfl-7.json = linegroup.json
tfl-8.json = linemodegroup.json
tfl-9.json = additionalproperties.json
tfl.json = mode.json

Mode/schemas

occupancy/schemas
tfl-3.json = chargeconnectoroccupancy.json
tfl-4.json = bikepointoccupancy.json
tfl.json = bay.json

Place/schemas
tfl-2.json = additionalproperties.json
tfl-4.json = passengerflow.json
tfl-5.json = trainloading.json
tfl-8.json = linegroup.json
tfl-9.json = linemodegroup.json
tfl.json = placecategory.json
tfl.json = stoppointcategory.json

Road/schemas
tfl-2.json = streetsegment.json
tfl-4.json = roadproject.json
tfl-7.json = roaddisruptionschedule.json
tfl-9.json = statusseverity.json
tfl.json = roadcorridor.json

Search/schemas
tfl.json = searchmatch.json

StopPoint/schemas
tfl-12.json = lineservicetypeinfo.json
tfl-15.json = predictiontiming.json
tfl-18.json = stoppointroutesection.json
tfl-19.json = disruptedpoint.json
tfl-21.json = searchmatch.json
tfl-2.json = mode.json
tfl-3.json = passengerflow.json
tfl-4.json = trainloading.json
tfl-7.json = linegroup.json
tfl-8.json = linemodegroup.json
tfl-9.json = additionalproperties.json
tfl.json = placecategory.json
tfl.json = stoppointcategory.json

Vehicle/schemas
tfl-3.json = vehiclematch.json
tfl.json = predictiontiming.json
```

Comparing this against the number of files in each of those directories:

```sh
for s in */schemas; do
  pushd $s >/dev/null
  echo $s
  ls tfl*.json 2>/dev/null | grep -v "tfl-api-presentation-entities" | wc -l
  popd >/dev/null
  echo
done
```
⇣
```
AccidentStats/schemas
0

AirQuality/schemas
0

BikePoint/schemas
0

crowding/schemas
0

Disruptions-Lifts-v2/schemas
0

Journey/schemas
40

Line/schemas
41

Mode/schemas
0

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

- Journey: 19 of 40
- Line: 19 of 41
- occupancy: 3 of 4
- Place: 6 of 10 (one duplicate match: `tfl.json` matched `placecategory` and `stoppointcategory`)
- Road: 5 of 9
- Search: 1 of 2
- StopPoint: 12 of 22 (one duplicate match: `tfl.json` matched `placecategory` and `stoppointcategory`)
- Vehicle: 2 of 3

While the following didn't have any to find:

- AccidentStats: 0 of 0
- AirQuality: 0 of 0
- BikePoint: 0 of 0
- crowding: 0 of 0
- Disruptions-Lifts-v2: 0 of 0
- Mode: 0 of 0

## Matching the remaining entities and understanding what changed about them

The easiest win here is the 4th entity in the `occupancy` API (`tfl-2.json`).
Its keys include `carParkDetailsUrl`, which matches a key in
`Tfl.Api.Presentation.Entities.CarParkOccupancy`. The diff between these files is:

```sh
diff occupancy/schemas/tfl-2.json ../openapi_unified/ReleasedUnifiedAPIProd/schemas/carparkoccupancy.json 
```
⇣
```
10c10
<         "$ref": "Tfl.json"
---
>         "$ref": "Tfl.Api.Presentation.Entities.Bay.json"
```

This appears to indicate that where a definition is recursive (i.e. refers to another definition),
the change in referent name makes the match inexact. However by substituting a known match, we
should be able to replace the name: indeed here we already found that `tfl.json = bay.json`,
which is the lowercased leaf of `Tfl.Api.Presentation.Entities.Bay` as a JSON file.

This means a program could be written to substitute the names and (presumably) achieve the full
correspondence for every entity in each API.

## Reference chasing

To get the following output, run:

```
tubeulator count
```

**Update**: after 'reference chasing', the figures are:

```py
{#'AccidentStats': '3 of 3',
 #'AirQuality': '1 of 1',
 #'BikePoint': '2 of 2',
 #'Disruptions-Lifts-v2': '0 of 1',
 'Journey': '23 of 40',
 'Line': '24 of 41',
 #'Mode': '3 of 3',
 'Place': '8 of 11',
 'Road': '9 of 12',
 'Search': '2 of 2',
 'StopPoint': '18 of 23',
 'Vehicle': '3 of 3',
 #'crowding': '0 of 0',
 'occupancy': '4 of 4'}
```

- Ignore those we ruled out above: AccidentStats, AirQuality, BikePoint, crowding, Disruptions-Lifts-v2, Mode
- Journey: +4, Line: +5, Place: +2 (?), Road: +4 (?), Search: +1, StopPoint: +6 (?), Vehicle: +1,
  occupancy: +1
  - Those where the underlying total changed are marked "(?)"

**Update**: all references chased, the properties were then sufficient to match the remaining and
make a full inventory, which can be output by the `names` subcommand. See the issue
[#1](https://github.com/lmmx/tubeulator/issues/1) for further details.
