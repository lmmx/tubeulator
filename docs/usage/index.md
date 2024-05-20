The `Minder` context manager keeps failure modes **contained** with minimal **legibility** cost:

???+ success

    ```py
    from tubeulator import fetch

    response = fetch.stop_point.meta_modes()
    coords = Matches[0].model_dump(include=["Lat","Lon"])
    ```

    ```py
    {'Lat': 51.52918, 'Lon': -0.132944}
    ```

When an error is encountered, we get the same interface.

???+ failure

    ```py
    from minder import Minder


    def main() -> dict:
        with Minder() as guard:
            with guard.duty("greet"):
                print("Hello world")
            with guard.duty("division"):
                guard.result = 1 / 0
        return guard.report()


    response = main()
    print(f"Got {response=}")
    ```

    ```py
    Hello world
    Got response={'result': {'error': 'division by zero', 'where': 'division'}, 'success': False}
    ```

In this example we expose a reliable interface of a `result` and `success` boolean.
