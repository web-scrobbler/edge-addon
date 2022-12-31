#!/usr/bin/env python

import os
import sys

from edge_addons_api.client import Client, Options

if len(sys.argv) != 7:
    print("Incorrect number of arguments given. Please check action parameters")
    sys.exit(1)

product_id = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]
access_token_url = sys.argv[4]
file_path = sys.argv[5]
notes = sys.argv[6]

options = Options(
    product_id=product_id,
    client_id=client_id,
    client_secret=client_secret,
    access_token_url=access_token_url,
)

client = Client(options)

print("Submitting addon")

client.submit(file_path=file_path, notes=notes)

print("Successfully uploaded addon")
