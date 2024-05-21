The `tubeulator` interface to the TfL APIs always returns results in Pydantic data models:

???+ success

    ```py
    from tubeulator import fetch

    response = fetch.stop_point.meta_modes()
    coords = Matches[0].model_dump(include=["Lat","Lon"])
    ```

    ```py
    {'Lat': 51.52918, 'Lon': -0.132944}
    ```

As shown here, you can retrieve regular Python dicts with the `model_dump()` method,
but data models do a lot more besides. Here their primary role is to ensure we always
have valid data. Definitions for all data models in `tubeulator` are generated from the official TfL schemas.
