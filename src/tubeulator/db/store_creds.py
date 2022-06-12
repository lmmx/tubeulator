from pymongo import MongoClient


def check_creds(client: MongoClient, interactive: bool) -> dict[str, str]:
    """
    Store the API credentials in a simple singleton collection "tfl_cred" in the "creds"
    database if none has been stored there before.
    """
    creds_collection = client.creds.tfl_cred
    n_docs = creds_collection.count()
    if n_docs == 0:
        app_id = input("Enter your app ID (suggestion: 'tubeulator'): ")
        primary_key = input("Enter your primary key: ")
        secondary_key = input("Enter your secondary key: ")
        stored_credential = {
            "app_id": app_id,
            "primary_key": primary_key,
            "secondary_key": secondary_key,
        }
        creds_collection.insert_one(stored_credential)
    elif n_docs > 1:
        raise ValueError(
            f"Multiple credentials {n_docs=} found: database has been corrupted"
        )
    else:
        stored_credential = creds_collection.find_one()
    return stored_credential
