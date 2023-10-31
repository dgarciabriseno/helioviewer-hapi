from id import get_info

def test_get_info():
    info = get_info("AIA_304")
    assert isinstance(info, dict)
    assert info["startDate"].strip() != ""
    assert info["stopDate"].strip() != ""