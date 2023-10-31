from datetime import datetime

from db import HAPIDataset, DataRow

def test_get_start_date():
    ds = HAPIDataset("AIA_304")
    date = ds.GetStartDate()
    assert isinstance(date, datetime)

def test_get_stop_date():
    ds = HAPIDataset("AIA_304")
    date = ds.GetStopDate()
    assert isinstance(date, datetime)

def test_DataRow_to_csv():
    ds = HAPIDataset("AIA_304")
    result = ds.Get(datetime(2023, 1, 1), datetime(2023,1,2))
    for row in result:
        split = row.to_csv(["url"]).split(",")
        assert split[0].startswith("2023")
        assert split[1].startswith("http")
        assert len(split) == 2

def test_get_data():
    ds = HAPIDataset("AIA_304")
    result = ds.Get(datetime(2023, 1, 1), datetime(2023,1,2))
    for item in result:
        assert isinstance(item, DataRow)
