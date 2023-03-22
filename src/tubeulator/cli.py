from pprint import pprint

import defopt

from .openapi.scan import count_namespace, scan_namespace


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
            "lines": lines,
        },
        no_negated_flags=True,
        strict_kwonly=False,
        short={},
    )
