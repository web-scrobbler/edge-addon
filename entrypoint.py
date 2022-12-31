#!/usr/bin/env python

import os
import sys

from edge_addons_api.client import Client, Options

product_id = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]
access_token_url = sys.argv[4]
file_path = sys.argv[5]
notes = sys.argv[6]

options = Options(
    product_id=os.environ["EDGE_PRODUCT_ID"],
    client_id=os.environ["EDGE_CLIENT_ID"],
    client_secret=os.environ["EDGE_CLIENT_SECRET"],
    access_token_url=os.environ["EDGE_ACCESS_TOKEN_URL"],
)

client = Client(options)

client.submit(file_path=file_path, notes=notes)
