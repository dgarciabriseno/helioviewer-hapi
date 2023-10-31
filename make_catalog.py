"""
Hacky script to read datasources from hvpy and generate catalog json for each source.
"""
import json

import hvpy.datasource as datasource

catalogs = []
# Read in the datasource source file
with open(datasource.__file__) as fp:
    # Enumerate the lines in the file
    lines = list(enumerate(fp.readlines()))
    for idx, line in lines:
        # Look for enum value assignments
        if "=" in line and not line.startswith("__all__"):
            assignment = line.split("=")
            # Get the enum variable name
            varname = assignment[0].strip()
            # Get the docstring from 2 lines ahead.
            docstring = lines[idx + 2][1].strip()
            # Add this enum to the catalog.
            catalogs.append({
                "id": varname,
                "title": docstring,
                "info": f"$PYTHONEXE $HAPISERVERPATH/src/id.py --id {varname}"
            })

# Dump the result.
# Manually copy/paste this into meta.json and use prettier to make it readable.
print(json.dumps(catalogs))