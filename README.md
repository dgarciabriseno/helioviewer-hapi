# Helioviewer HAPI

Helioviewer's HAPI configuration and CLI

# Usage

Clone [server-nodejs](https://github.com/hapi-server/server-nodejs).

Run with the following environment variables and parameters:

```bash
HAPISERVERPATH=path/to/this/repo PYTHONEXE=path/to/python/venv DB_USER=db_username DB_PASSWORD=db_password DB_NAME=db_name node server.js --file path/to/meta.json
```

| parameter      | description                                          |
| -------------- | ---------------------------------------------------- |
| HAPISERVERPATH | Path to this repository's directory                  |
| PYTHONEXE      | Path to python executable with required dependencies |
| DB_USER        | Database username                                    |
| DB_PASSWORD    | Database password                                    |
| DB_NAME        | Name of helioviewer database                         |
| DB_HOST        | Optional database host. Defaults to localhost        |

## Running tests
Run pytest as a module in the src directory with environment variables set.
```bash
cd src
DB_USER= DB_PASSWORD= DB_HOST= DB_NAME= python -m pytest
```
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
