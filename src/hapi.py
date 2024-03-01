"""
This module queries the helioviewer database and returns rows in a csv format
to be served by the generic HAPI server.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from datetime import datetime
from typing import Iterable
from sunpy.time import parse_time

from db import HAPIDataset, DataRow


class Result:
    def __init__(self, rows: Iterable[DataRow], parameters: list[str]) -> None:
        self.rows = rows
        self.parameters = parameters

    def print_csv(self):
        for row in self.rows:
            print(row.to_csv(self.parameters))


def get_data(
    dataset: str, start: datetime, stop: datetime, parameters: list[str]
) -> Result:
    ds = HAPIDataset(dataset)
    rows = ds.Get(start, stop)
    return Result(rows, parameters)

def parse_date(date: str) -> datetime:
    return parse_time(date).datetime

if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("--dataset", required=True, type=str, help="Dataset to query")
    parser.add_argument(
        "--parameters",
        required=True,
        type=str,
        help="Dataset specific parameters to return",
    )
    parser.add_argument(
        "--start",
        required=True,
        type=parse_date,
        help="Start of query range",
    )
    parser.add_argument(
        "--stop", required=True, type=parse_date, help="Stop of query range"
    )
    args = parser.parse_args()
    parameters = args.parameters.split(",")
    data = get_data(args.dataset, args.start, args.stop, parameters)
    data.print_csv()
