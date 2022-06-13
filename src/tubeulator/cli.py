# from pprint import pprint

import defopt
from pymongo import MongoClient

from .api.line import line_data
from .db.mongod import MongodExceptionGuard
from .db.store_creds import check_creds
from .openapi.scan import scan_namespace


def lines():
    with MongodExceptionGuard():
        client = MongoClient()
        creds = check_creds(client=client, interactive=True)
        line_data(creds)


def namespace():
    """
    Make a namespace inventory
    """
    scan_namespace()
    # ns = scan_namespace()
    # pprint(ns)


def main():
    defopt.run(
        {
            "names": namespace,
            "lines": lines,
        },
        no_negated_flags=True,
        strict_kwonly=False,
        short={},
    )
