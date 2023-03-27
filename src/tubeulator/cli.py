from pathlib import Path
from pprint import pprint

import defopt

from .codegen.codegen import emit_deserialisers
from .openapi.scan import count_namespace, scan_namespace


def deserialise(schema_name: str):
    """
    Map each API schema to a corresponding dataclass which deserialises its JSON.
    """
    emit_deserialisers(schema_name=schema_name)


def list_schemas():
    """
    Print each schema name on a line (for processing in scripts etc over STDIN).
    """
    for schema in sorted(count_namespace(ignore_responses=True), key=str.lower):
        print(schema)


def namespace():
    """
    Make a namespace inventory
    """
    ns = scan_namespace(ignore_responses=True)
    pprint(ns)


def ns_count():
    """
    Count empty/non-empty in namespace inventory
    """
    ns = count_namespace(ignore_responses=True)
    pprint(ns)


def main():
    defopt.run(
        {
            "names": namespace,
            "count": ns_count,
            "deserialise": deserialise,
            "schemas": list_schemas,
        },
        no_negated_flags=True,
        strict_kwonly=False,
        short={},
    )
