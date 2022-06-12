from pymongo import MongoClient

from .db.store_creds import check_creds
from .db.mongod import MongodExceptionGuard
from .api.line import line_data


def main():
    with MongodExceptionGuard():
        client = MongoClient()
        creds = check_creds(client=client, interactive=True)
        line_data(creds)
