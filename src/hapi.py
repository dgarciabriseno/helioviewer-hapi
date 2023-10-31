"""
This module queries the helioviewer database and returns rows in a csv format
to be served by the generic HAPI server.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from datetime import datetime

if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("dataset", type=str, help="Dataset to query")
    parser.add_argument("parameters", type=str, help="Dataset specific parameters to return")
    parser.add_argument("start", type=datetime.fromisoformat, help="Start of query range")
    parser.add_argument("stop", type=datetime.fromisoformat, help="Stop of query range")
    parser.add_argument("format", type=datetime.fromisoformat, help="Output format")

