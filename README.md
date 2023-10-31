# Helioviewer HAPI

Helioviewer's HAPI configuration and CLI

# Listing

## meta.json

HAPI server metadata. See [server-nodejs](https://github.com/hapi-server/server-nodejs#5-metadata) for formatting details.

## hapi.py

Program to read from database and output to HAPI.

## info_template.json

Template info response for all datasets.
hapi.py fills in dataset specific details

## requirements.txt

Dependencies for `hapi.py`.
Install with `pip install -r requirements.txt`
