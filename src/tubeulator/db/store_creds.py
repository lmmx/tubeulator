"""TinyDB implementation for credential storage."""

import os
from functools import lru_cache

from pydantic import BaseModel, Field, ValidationError
from tinydb import TinyDB

from ..utils.logs import set_up_logging
from ..utils.paths import db_path

__all__ = ["check_creds"]

logger = set_up_logging(__name__)


class EnvCredentials(BaseModel):
    app_id: str = Field(validation_alias="TFL_API_KEY_ID")
    primary_key: str = Field(validation_alias="TFL_API_PRIMARY_ACCESS_KEY")
    secondary_key: str = Field(validation_alias="TFL_API_SECONDARY_ACCESS_KEY")


@lru_cache
def check_creds() -> dict[str, str]:
    """Either pick up API credentials from environment variables or retrieve from TinyDB.

    Store the API credentials in a simple TinyDB database if none has been stored before.
    This is used only in interactive sessions when environment variables are not set.
    """
    try:
        # Always try environment variables first
        env_creds = EnvCredentials.model_validate(os.environ)
        credential = env_creds.model_dump()
        logger.debug("Using credentials from environment variables")
        return credential
    except ValidationError:
        # No API keys in environment variables, get it from the TinyDB database
        logger.debug("No API keys in environment variables, checking TinyDB")

        # Ensure database directory exists
        db_path.mkdir(parents=True, exist_ok=True)

        # Open TinyDB file
        db_file = db_path / "credentials.json"
        with TinyDB(db_file) as db:
            credentials = db.all()

            if not credentials:
                # No stored credentials, prompt user to enter them
                logger.info(
                    "No stored credentials found. Please enter your TfL API credentials.",
                )
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

                # Store the credentials
                db.insert(credential)
                logger.debug("Credentials stored in TinyDB")
            elif len(credentials) > 1:
                # There should only be one credential entry
                logger.warning(
                    f"Multiple credentials found in database: {len(credentials)}",
                )
                # Use the first one
                credential = credentials[0]
            else:
                # Use the stored credentials
                credential = credentials[0]

    return credential
