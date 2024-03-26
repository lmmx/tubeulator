from pprint import pprint

import defopt

from .codegen.gen import emit_deserialisers
from .codegen.populate import generate_schema_coverage
from .openapi.fetch import refresh_schema
from .openapi.scan import count_namespace, scan_namespace


def deserialise(schema_name: str) -> None:
    """Map each API schema to a corresponding dataclass which deserialises its JSON."""
    deserialised = emit_deserialisers(schema_name=schema_name)
    print(deserialised)
    return


def populate() -> None:
    """Map all API schemas to corresponding dataclasses that deserialise their JSON.
    Write all generated Python to module files in the `tubeulator.generated` directory.
    """
    generate_schema_coverage()
    return


def list_schemas() -> None:
    """Print each schema name on a line (for processing in scripts etc over STDIN)."""
    for schema in sorted(count_namespace(ignore_responses=True), key=str.lower):
        print(schema)
    return


def refresh_schemas(api_version: str = "2022-04-01-preview") -> None:
    """Redownload each schema source JSON (in-place) at `data/openapi/*/*.json`."""
    for schema in sorted(count_namespace(ignore_responses=True), key=str.lower):
        refresh_schema(schema_name=schema, api_version=api_version)
    return


def namespace() -> None:
    """Make a namespace inventory"""
    ns = scan_namespace(ignore_responses=True)
    pprint(ns)
    return


def ns_count() -> None:
    """Count empty/non-empty in namespace inventory"""
    ns = count_namespace(ignore_responses=True)
    pprint(ns)
    return


def main():
    defopt.run(
        {
            "names": namespace,
            "count": ns_count,
            "deserialise": deserialise,
            "populate": populate,
            "schemas": list_schemas,
            "refresh": refresh_schemas,
        },
        no_negated_flags=True,
        strict_kwonly=False,
        short={},
    )
    return
