"""Helpers courtesy of the dataclass_wizard package's `utils.string_conv` module.

These are used to convert the keys from Pydantic model field names to TfL Data Transfer
Object (DTO) JSON keys.

Pydantic uses 'alias generators' for this, the same as DCW just in the opposite
direction (DCW consider conversions going from JSON key to model field). Unfortunately
Pydantic's string conversion helpers do not actually do the job required here,
so I copied over these helper functions rather than enforce a dependency for them.
"""

import re

__all__ = ["to_camel_case", "to_pascal_case", "to_snake_case"]


def replace_multi_with_single(string: str, char="_") -> str:
    """
    Replace multiple consecutive occurrences of `char` with a single one.
    """
    rep = char + char
    while rep in string:
        string = string.replace(rep, char)

    return string


def to_camel_case(string: str) -> str:
    """
    Convert a string to Camel Case.

    Examples::

        >>> to_camel_case("ModeName")
        'modeName'
        >>> to_camel_case("a_b_c")
        'aBC'

    """
    string = replace_multi_with_single(string.replace("-", "_").replace(" ", "_"))

    return string[0].lower() + re.sub(
        r"(?:_)(.)",
        lambda m: m.group(1).upper(),
        string[1:],
    )


def to_pascal_case(string):
    """
    Converts a string to Pascal Case (also known as "Upper Camel Case")

    Examples::

        >>> to_pascal_case("device_type")
        'DeviceType'

    """
    string = replace_multi_with_single(string.replace("-", "_").replace(" ", "_"))

    return string[0].upper() + re.sub(
        r"(?:_)(.)",
        lambda m: m.group(1).upper(),
        string[1:],
    )


def to_snake_case(string: str) -> str:
    """
    Make an underscored, lowercase form from the expression in the string.


    Example::


        >>> to_snake_case("DeviceType")
        'device_type'


    """
    string = string.replace("-", "_").replace(" ", "_")
    # Short path: the field is already
    # lower-cased, so we don't need to handle
    # for camel or title case.
    if string.islower():
        return replace_multi_with_single(string)

    result = re.sub(r"((?!^)(?<!_)[A-Z][a-z]+|(?<=[a-z0-9])[A-Z])", r"_\1", string)

    return replace_multi_with_single(result.lower())
