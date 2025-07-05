#!/usr/bin/env python

import sys

from edge_addons_api.client import Client
from edge_addons_api.exceptions import UploadException

from edge_addon.config import create_options
from edge_addon.logging_utils import setup_logging

options = create_options()
setup_logging(options.debug)

client = Client(options.to_edge_options())

print("Submitting addon")

try:
    operation_id = client.submit(file_path=options.file_path, notes=options.notes)
    client.fetch_publish_status(operation_id)

    print("Successfully uploaded addon")
except UploadException as e:
    print(f"Failed to upload: {e.status} - {e.error_code} - {e.message}")
    print("Errors:")
    for error in e.errors:
        print(f"- {error['message']}")

    sys.exit(1)
except BaseException as e:
    print(f"failed to upload: {e}")
    sys.exit(1)
