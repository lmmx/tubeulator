# tubeulator

> It's time for the tubeulator

TfL open data interface library

## Key features

- Route planning (underground, overground, bus, walking)
- Time estimation taking into account mixed modes of travel in one journey

## Requires

- Python 3.9+

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
