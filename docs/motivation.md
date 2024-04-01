---
title: Motivation
---

The motivations behind this pattern are explained by the following observations:

Consider this trivially sequential operation:

``` py
a = 1
b = 2
c = 3
response = {"result": c}
```

- Maybe we'll send `a` and `b` to files or STDOUT along the way. Here just keep it simple.

### 1) Repeated `try`/`except`/`else` blocks eliminate risk of crashes

- In many situations it's important that the service doesn't crash.
- Error handling coordination should go at call sites (top level) not mixed in with operations
  themselves (internal functions etc.)
- A single exception catcher at the top level means error origins are opaque.


``` py
try:
    a = 1
    b = 2
    c = 3
except Exception as exc:
    response = {"error": str(exc)}
else:
    response = {"result": c}
finally:
    return response
```

### 2) Attaching specific locations to error messages aids debugging

- Tracebacks are too fine-grained: we typically want to see something more equivalent to a "stage"
  of the program rather than the precise line.
- Tracebacks can often point into dependencies, and obscure the relevant part of our program to
  investigate. I.e. they don't provide practical situational awareness.


### 3) Nesting from `else` to `try` blocks harms legibility

- Sequential operations are made to look nested, which is counterintuitive.


!!! example

    ``` py
    try:
        a = 1
    except Exception as exc:
        response = {"error": str(exc), "where": "A"}
    else:
        try:
            b = 2
        except Exception as exc:
            response = {"error": str(exc), "where": "B"}
        else:
            try:
                c = 3
            except Exception as exc:
                response = {"error": str(exc), "where": "C"}
            else:
                response = {"result": c}
    finally:
        return response
    ```

- It's impossible to say if this `response` has a `result` key or `error` key.
- Visually checking if the logic was sound is strenuous due to the boilerplate bloat.
- The error handling takes 3x more lines than the actual business logic.
