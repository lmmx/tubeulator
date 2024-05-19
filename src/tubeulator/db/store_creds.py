import os
from functools import lru_cache

from pydantic import BaseModel, Field, ValidationError
from pymongo import MongoClient

from .mongod import MongodExceptionGuard


class EnvCredentials(BaseModel):
    app_id: str = Field(validation_alias="TFL_API_KEY_ID")
    primary_key: str = Field(validation_alias="TFL_API_PRIMARY_ACCESS_KEY")
    secondary_key: str = Field(validation_alias="TFL_API_SECONDARY_ACCESS_KEY")


@lru_cache
def check_creds() -> dict[str, str]:
    """Store the API credentials in a simple singleton collection "tfl_cred" in the "creds"
    database if none has been stored there before. Interactive only.
    """
    try:
        env_creds = EnvCredentials.parse_obj(os.environ)
        credential = env_creds.model_dump()
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
                credential = dict(
                    app_id=app_id,
                    primary_key=primary_key,
                    secondary_key=secondary_key,
                )
                creds_collection.insert_one(credential)
            elif n_docs > 1:
                raise ValueError(
                    f"Multiple credentials {n_docs=} found: database has been corrupted",
                )
            else:
                credential = creds_collection.find_one()
    return credential
