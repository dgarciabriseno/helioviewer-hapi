"""
Returns metadata info for the given dataset
"""

from argparse import ArgumentParser
import json

from common import DATE_FORMAT
from db import HAPIDataset

def get_info(id: str) -> dict:
    """
    Gets database info for the given dataset id

    Parameters
    ----------
    id: `str`
        Dataset id to query information for
    """
    with open("../info_template.json", "r") as fp:
        template = json.load(fp)
    dataset = HAPIDataset(id)
    template["startDate"] = dataset.GetStartDate().strftime(DATE_FORMAT)
    template["stopDate"] = dataset.GetStopDate().strftime(DATE_FORMAT)
    return template

def print_info(id: str):
    """
    Prints dataset information to stdout

    Parameters
    ----------
    id: `str`
        Dataset id to query information for
    """
    info = get_info(id)
    print(json.dumps(info))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--id", type=str, help="Dataset ID")
    args = parser.parse_args()
    print_info(args.id)