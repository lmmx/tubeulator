## Error inventory

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

## Solving the errors

The errors should be soluble once the names have been mapped back to the legacy ("unified") API
namespace, as documented in the [naming.md](naming.md) document, and issue
[1](https://github.com/lmmx/tubeulator/issues/1). The resulting mapping is obtainable by running
`tubeulator names`, and the output has been saved within the library as 
[`src/tubeulator/data/openapi/namespace.json`](namespace.json).

The way you can solve for instance `Line`'s semantic error, is to find any other `Array` property with name
`"modes"` and get the type of the fields of that array, and presume that sharing a name elsewhere in
the API is sufficient to assign the same type.

- **Q:** Where else has Array properties named `"modes"` and how can we find them?
- **A:** We just figured out the namespace for all the individual APIs, and some of those have
  properties, and some of those properties are arrays, and we can check if there are one or more
  such properties which share the same name.

```py
import json
from pathlib import Path

from tubeulator.data.openapi import __path__ as openapi_data_dir
namespace_json = Path(next(iter(openapi_data_dir))) / "namespace.json"
ns = json.loads(namespace_json.read_text())
```

This is equivalent to recalculating it:

```py
from tubeulator.openapi.scan import scan_namespace
ns_calculated = scan_namespace()
```

The result is identical:

```py
>>> ns == ns_calculated
True
```

We can then find the Array properties named `modes` and their types like so:

```py

```

TODO
