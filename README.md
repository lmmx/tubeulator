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
