import os
from functools import lru_cache

from pydantic import BaseModel, ValidationError
from pymongo import MongoClient

from .mongod import MongodExceptionGuard


class Credentials(BaseModel):
    app_id: str
    primary_key: str
    secondary_key: str


@lru_cache
def check_creds() -> dict[str, str]:
    """Store the API credentials in a simple singleton collection "tfl_cred" in the "creds"
    database if none has been stored there before. Interactive only.
    """
    try:
        env_creds = Credentials.parse_obj(os.environ)
        stored_credential = env_creds.model_dump()
    except ValidationError:
        # No API keys in environment variables
        pass
    else:
        with MongodExceptionGuard():
            client = MongoClient()
            creds_collection = client.creds.tfl_cred
            n_docs = creds_collection.estimated_document_count()
            if n_docs == 0:
                default_app_id = "tubeulator"
                app_id = (
                    input(f"Enter your app ID (default: {default_app_id!r}): ")
                    or default_app_id
                )
                primary_key = input("Enter your primary key: ")
                secondary_key = input("Enter your secondary key: ")
                stored = Credentials(
                    app_id=app_id,
                    primary_key=primary_key,
                    secondary_key=secondary_key,
                )
                creds_collection.insert_one(stored.model_dump())
            elif n_docs > 1:
                raise ValueError(
                    f"Multiple credentials {n_docs=} found: database has been corrupted",
                )
            else:
                stored_credential = creds_collection.find_one()
    return stored_credential
