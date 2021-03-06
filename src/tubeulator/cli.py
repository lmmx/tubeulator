from pprint import pprint

import defopt
from pymongo import MongoClient

from .api.line import line_data
from .db.mongod import MongodExceptionGuard
from .db.store_creds import check_creds
from .openapi.scan import count_namespace, scan_namespace


def lines():
    with MongodExceptionGuard():
        client = MongoClient()
        creds = check_creds(client=client, interactive=True)
        line_data(creds)


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
