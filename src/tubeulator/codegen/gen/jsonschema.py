"""Helpers to process the JSONSchema format (a.k.a. Swagger)."""

__all__ = ["python_type"]


def python_type(json_type: str, format: str = None) -> str:
    """Map property types in the JSON schema to Python types for type annotation.

    The `format` can be "email" if it's a string but it doesn't change the result.
    """
    type_lookup = {
        "string": "str",
        "integer": "int",
        "boolean": "bool",
        "array": "list",
        "object": "dict",
    }
    if json_type == "number" and format == "double":
        python_type = "float"
    elif json_type == "string" and format == "date-time":
        python_type = "datetime"
    else:
        python_type = type_lookup[json_type]
    return python_type
