# tubeulator

> It's time for the tubeulator

TfL open data interface library

## Key features

- Route planning (underground, overground, bus, walking)
- Time estimation taking into account mixed modes of travel in one journey

## Requires

- Python 3.9+
- MongoDB

## Installation

> _tubeulator_ is available from [PyPI](https://pypi.org/project/tubeulator), and
> the code is on [GitHub](https://github.com/lmmx/tubeulator)

Install using `pip`:

```sh
pip install tubeulator
```

The suggested local environment installation is stored in `CONDA_SETUP.md`:

```
conda create -n tubeulator "python=3.9"
conda activate tubeulator
pip install -r requirements.txt
```

## Usage

Outline of expected usage:

```py
>>> import tubeulator
>>> j = tubeulator.Journey(A="Shoreditch High Street", B="Tooting Bec")
[INFO] Found 3 routes [1: (Tube,Tube,Walk) 2: (Tube,Tube,Bus), 3: (Overground,Tube)].
[INFO] Selected 1 as best route (fastest).
...
```

Possible features to customise the `Journey`:

- `via` (routes, locations)
- `avoid` (e.g. busy areas, or a particular interconnection)
- `prefer` (fastest, least walking)

## Storage

A good option for storage would be to use MongoDB
([PyMongo](https://pymongo.readthedocs.io/en/stable/tutorial.html))
as done in [this project](https://github.com/milh0use/tfl/blob/master/monitor_buses.py).
This would require the user to set up and run a MongoDB client with `mongod`,
then the program would connect to it on localhost.

For simplicity, I store the data in the package itself (under `src/tubeulator` in this repo,
which would be retained when distributed as an installed package in `site-packages`),
rather than the default `/data/db` at the root of my file system.

The program will not create this directory within its package directory if there is already an
instance of MongoDB running (`mongod`) to connect to. To supply a different database path, run
the following and substitute your path of choice:

```
mkdir -p data/db
mongod --dbpath data/db
```

Data is stored in JSON-style documents (represented as dictionaries in PyMongo),
converted from Python types to BSON types under the hood.

## Data collection approach

The available network is a configuration, liable to change (stations may open/close temporarily/permanently).

However the network is also fairly static: it can be expected to remain fixed in the short-term.

This situation motivates an incremental method of collection that builds from dynamically downloaded
components (rather than hard-coding aspects liable to change),
and can therefore be regenerated in response to change.

Most of these can be found by looking for `Meta` API names in
[the main Swagger doc](https://api.tfl.gov.uk/swagger/docs/v1). For `Line` these are `Modes`,
`Severity`, `DisruptionCategories` and `ServiceTypes`. For `StopPoint` these are `Categories`,
`StopTypes` and `Modes`.

- Enumerate valid modes
  ([`Line/Meta/Modes`](https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_MetaModes) or equivalently `StopPoint/Meta/Modes`)
  - For a 'tube' network I would include `tube`, `elizabeth-line`, `dlr`, `overground`, `tflrail`, `national-rail`, and at a push `bus`
    and `replacement-bus`.
  - For representing interchange I might include: `walking`, `interchange-keep-sitting`, and `interchange-secure`.
  - I would not include: taxis, river boats, trams, bikes, coaches, cable cars.

- Enumerate lines that serve the selected modes
  ([`Line/Mode/{modes}`](https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_GetByModeByPathModes))
  - For example:
    - The `elizabeth-line` mode has a single `Line` entity, id = "elizabeth", name = "Elizabeth line".
    - The `dlr` mode has a single `Line` entity, id = "dlr", name = "DLR"
    - The `tube` mode has 11 `Line` entities, the first has id "bakerloo" and name "Bakerloo" (etc).
      Some tube lines have both "Regular" and "Night" `serviceTypes`.

- Enumerate the types of `StopPoint` that are applicable to the selected modes
  ([`StopPoint/Meta/StopTypes`](https://api-portal.tfl.gov.uk/api-details#api=StopPoint&operation=StopPoint_MetaStopTypes))
  - For a 'tube' network I would include "NaptanMetroAccessArea", "NaptanMetroEntrance", "NaptanMetroPlatform",
    "NaptanMetroStation", "NaptanRailAccessArea", "NaptanRailEntrance", "NaptanRailPlatform", "NaptanRailStation",
    "TransportInterchange", "NaptanFlexibleZone", "NaptanUnmarkedPoint".
    - Unfortunately `NaptanMetroStation` describes both tube stations and cable car 'stations' (at Greenwich),
      as seen when obtaining all stop points of a given type
  - At a push I would include "NaptanBusCoachStation", "NaptanBusWayPoint", "NaptanMarkedPoint",
    "NaptanOnstreetBusCoachStopCluster", "NaptanOnstreetBusCoachStopPair", "NaptanPrivateBusCoachTram", "NaptanPublicBusCoachTram".
  - I would exclude "CarPickupSetDownArea", "NaptanAirAccessArea", "NaptanAirEntrance", "NaptanAirportBuilding",
    "NaptanCoachAccessArea", "NaptanCoachBay", "NaptanCoachEntrance", "NaptanCoachServiceCoverage",
    "NaptanCoachVariableBay", "NaptanFerryAccessArea", "NaptanFerryBerth", "NaptanFerryEntrance",
    "NaptanFerryPort", "NaptanHailAndRideSection", "NaptanLiftCableCarAccessArea",
    "NaptanLiftCableCarEntrance", "NaptanLiftCableCarStop", "NaptanLiftCableCarStopArea",
    "NaptanSharedTaxi", "NaptanTaxiRank"

- List the stations for the given line IDs
  ([`Line/{id}/StopPoints[?tflOperatedNationalRailStationsOnly]`](https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StopPointsByPathIdQueryTflOperatedNationalRailStationsOnly))
  - Each entry returned (alphabetically) has
    - a `commonName` (readable title)
    - `lat` and `lon` floating points
    - `modes` e.g. `['bus', 'tube']`
    - `lines`, a list of dicts of each line, for all modes, with an `id` (e.g. `district`), proper `name` (e.g. `District`),
      `uri` (which seems to just be `/Line/{id}`. The mode is not indicated for each line.
    - `lineGroup` is again a list of dicts, whose purpose seems to be to indicate the side of the road for a bus, for each line
    - `lineModeGroups` is again a list of dicts, which indicates the mode for each line (grouped by mode).
    - `children` list with the same `commonName` but distinct `naptanId` (presumably these are for each platform/direction.
  - Note that the child nodes do not have populated `modes` (`[]`), `lat` or `lon` (`0.0`).

(TBC)
