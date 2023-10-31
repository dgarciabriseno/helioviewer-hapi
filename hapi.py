"""
This module queries the helioviewer database and returns rows in a csv format
to be served by the generic HAPI server.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter

if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument
