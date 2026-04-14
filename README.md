# tubeulator

[![PyPI](https://img.shields.io/pypi/v/tubeulator.svg)](https://pypi.org/project/tubeulator)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/tubeulator.svg)](https://pypi.org/project/tubeulator)
[![License](https://img.shields.io/pypi/l/tubeulator.svg)](https://pypi.python.org/pypi/tubeulator)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/lmmx/tubeulator/master.svg)](https://results.pre-commit.ci/latest/github/lmmx/tubeulator/master)

Typed Python client for the TfL Unified API. Pydantic models are generated from
the official OpenAPI schemas, and the station network is exposed as polars
DataFrames for structural queries.

## Install

```sh
pip install tubeulator
```

Requires Python 3.10+.

## Quickstart

```python
>>> from tubeulator.topology.combine import load_stations_by_line
>>> df = load_stations_by_line()
>>> df.sort("Line").head(3)
shape: (3, 2)
┌──────────┬─────────────────────────────────┐
│ Line     ┆ StationName                     │
│ ---      ┆ ---                             │
│ str      ┆ list[str]                       │
╞══════════╪═════════════════════════════════╡
│ bakerloo ┆ ["Kilburn Park", "Edgware Road… │
│ central  ┆ ["Wanstead", "Barkingside", … … │
│ circle   ┆ ["King's Cross St Pancras", "R… │
└──────────┴─────────────────────────────────┘
```

Every TfL API is available through a typed fetch interface:

```python
>>> from tubeulator import fetch
>>> result = fetch.stop_point.search_query(query="Euston")
>>> result.Total
14
```

Responses are Pydantic models, so autocomplete and static analysis work
end-to-end.

## Related projects

If you want the typed API client, you're in the right place. For the research
models or a running server, see the related projects built on top of this
library's data layer:

- **[tb8](https://github.com/lmmx/tb8)** — FastAPI server and React frontend.
- **[tb8-rs](https://github.com/lmmx/tb8-rs)** — Rust reimplementation of the
  tb8 server.
- **[tubeulator-models](https://github.com/lmmx/tubeulator-models)** — experimental
  GNN route planning and travel-time prediction trained on TfL timetable data.
  Models and datasets published to Hugging Face.
