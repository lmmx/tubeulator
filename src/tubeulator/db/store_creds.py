from pymongo import MongoClient

from .check_mongod import get_mongod_process

def check_creds():
    no_creds = True # TODO
    client = MongoClient()
    return client
