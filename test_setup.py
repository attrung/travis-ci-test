import requests

def testing():
    url = "https://google.com"

    res = requests.get(url).text

    assert res != None

def test_always_passes():
    assert True