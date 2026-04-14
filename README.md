# tubeulator

[![PyPI](https://img.shields.io/pypi/v/tubeulator.svg)](https://pypi.org/project/tubeulator)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/tubeulator.svg)](https://pypi.org/project/tubeulator)
[![License](https://img.shields.io/pypi/l/tubeulator.svg)](https://pypi.python.org/pypi/tubeulator)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/lmmx/tubeulator/master.svg)](https://results.pre-commit.ci/latest/github/lmmx/tubeulator/master)

Typed Python client for the TfL open data APIs. Covers 14 APIs and roughly 100
endpoints, with Pydantic models generated from TfL's OpenAPI schemas and a handful of
Polars DataFrame-backed views of common enumerations of the London station network.

Responses from the APIs are Pydantic models, endpoints can be explored by tab completion
of the `fetch.{api}.{endpoint}(...)` enums, and the entire DTO
layer can be reproducibly regenerated from upstream schemas.

## Install

```sh
pip install tubeulator
```

Requires Python 3.10+.

## Quickstart

```python
>>> from tubeulator import fetch
>>> lines = fetch.line.lines_by_modes("tube")
>>> [(l.Name, [s.Name for s in l.ServiceTypes]) for l in lines[:3]]
[('Bakerloo', ['Regular']),
 ('Central', ['Regular', 'Night']),
 ('Piccadilly', ['Regular', 'Night'])]
```

## Related projects

tubeulator is the data layer to the API and only handles authentication and transformation.
There are related projects built on top of it which add further functionality:

- **[tubeulator-models](https://github.com/lmmx/tubeulator-models)** —
  GNN route planning and travel-time prediction trained on TfL timetable
  data. Models and datasets published to Hugging Face.
- **[tb8](https://github.com/lmmx/tb8)** — FastAPI server and React
  frontend, deployed on Render/Railway.
- **[tb8-rs](https://github.com/lmmx/tb8-rs)** — Rust reimplementation of
  the tb8 server.

## Walkthrough

For full docs [see the MkDocs site](https://tubeulator.vercel.app/).
A brief overview of the package:

- **Typed fetch interface.** A `fetch` object with a sub-module per TfL API
  (Journey, Line, Mode, Place, Road, StopPoint, Search, Vehicle, BikePoint,
  AirQuality, AccidentStats, Occupancy, Crowding, Disruptions-Lifts). Each
  endpoint is a method that builds a validated URL from a typed path template,
  sends the request, and parses the response into the Pydantic model declared
  for that route's 200 response.
  
- **Generated pydantic DTOs.** One module per API under `tubeulator.generated`,
  containing every response model TfL's schemas describe. Models use Pydantic's
  `AliasGenerator` to handle TfL's PascalCase / camelCase mix transparently.
  Regenerable via `tubeulator populate`.
  
- **Codegen pipeline.** `tubeulator.openapi` and `tubeulator.codegen` implement
  the route from upstream OpenAPI to emitted Python: schemas are fetched and
  vendored under `src/tubeulator/data/openapi/`; entity names in the
  per-API schemas are matched against the unified TfL schema and resolved to
  canonical names; JSON references are chased across schema boundaries; and
  Pydantic classes are emitted via `ast`. A longest-common-prefix trie is used
  to disambiguate array and back-reference names during emission.
  
- **Endpoint discoverability.** Every endpoint is registered as a `RouteEnum`
  member (one enum per API, composed into a top-level `EndpointRoute`). This
  is what makes `fetch.line.<tab>` show you every valid route at the REPL, and
  what `api/request.py` uses to validate path variables before sending.
  
- **Station network as DataFrames.** The NaPTAN detailed station dataset and
  TfL's GTFS feed are shipped with the package and loaded as polars DataFrames
  validated with patito — useful for structural queries that don't map cleanly
  onto the JSON API:
  
```python
from tubeulator.topology.combine import load_stations_by_line
df = load_stations_by_line()
```
 
- **Reproducible schema refresh.** `tubeulator refresh-schemas` pulls current
  schemas from TfL for a given API version; `tubeulator populate` regenerates
  the entire `generated/` subpackage from them. The vendored schemas mean the
  package is offline-installable and the DTO layer is deterministic at a given
  version.

## Usage

```python
from tubeulator import fetch

# Live arrivals for a line at a specific stop
arrivals = fetch.line.arrivals_by_ids_stop(
    ids="waterloo-city",
    stopPointId="940GZZLUASL",
)

# Journey planning (wraps TfL's own planner)
journey = fetch.journey.journey_results(
    **{"from": "Tooting Bec Underground", "to": "Tooting Broadway Underground"}
)
for leg in journey.Journeys[0].Legs:
    print(leg.Instruction.Summary)

# Stop point search
result = fetch.stop_point.search_query(query="Euston")
result.Total  # 6
```

Each test file under `tests/apis/` is a working example of every endpoint in
that API: see there for demos covering the full surface.

## Regenerating the DTO layer

```sh
tubeulator refresh-schemas --api-version 2022-04-01-preview  # pull upstream
tubeulator populate                                           # regenerate models
tubeulator list-schemas                                       # inspect inventory
```

See [`docs/code_generation.md`](docs/code_generation.md) for details on the
pipeline — schema scanning, alias resolution, reference chasing, and AST
emission.

## Development

```sh
pdm install
pdm run pytest
```

Tests hit the live TfL API, skipped tests (`@mark.skip` in `tests/apis/`)
document known upstream issues with specific endpoints which are also
recorded in the docs site.

## License

MIT — see [LICENSE.txt](LICENSE.txt).
