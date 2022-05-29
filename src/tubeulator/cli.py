from time import sleep

from .db.store_creds import check_creds
from .db.check_mongod import get_mongod_process
from .utils.logging import set_up_logging

logger = set_up_logging(__name__)

def main():
    # First set up the mongod daemon
    mongod_proc = get_mongod_process()
    try:
        print("Hello")
        client = check_creds()
        print("zzz...")
        sleep(3)
    except (KeyboardInterrupt, SystemExit):
        mongod_proc.clean_up()
        raise
    except Exception:
        mongod_proc.clean_up()
        raise
    else:
        mongod_proc.clean_up()
