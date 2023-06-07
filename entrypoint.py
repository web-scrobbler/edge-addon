#!/usr/bin/env python

import logging
import sys

from edge_addons_api.client import Client, Options
from edge_addons_api.exceptions import UploadException

if len(sys.argv) < 6:
    print("Incorrect number of arguments given. Please check action parameters")
    sys.exit(1)

product_id = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]
access_token_url = sys.argv[4]
file_path = sys.argv[5]
notes = sys.argv[6]
debug = sys.argv[7].lower() in ["true", "1"]

if debug:
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

options = Options(
    product_id=product_id,
    client_id=client_id,
    client_secret=client_secret,
    access_token_url=access_token_url,
)

client = Client(options)

print("Submitting addon")

try:
    operation_id = client.submit(file_path=file_path, notes=notes)
    client.fetch_publish_status(operation_id)

    print("Successfully uploaded addon")
except UploadException as e:
    print(f"Failed to upload: {e.status} - {e.error_code} - {e.message}")
    print(f"Errors:")
    for error in e.errors:
        print(f"- {error['message']}")

    sys.exit(1)
except BaseException as e:
    print(f"failed to upload: {e}")
    sys.exit(1)
