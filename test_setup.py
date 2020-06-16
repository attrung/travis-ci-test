import requests
import unittest

class TestRepositories(unittest.TestCase):
    def testing(self):
        url = "https://google.com"

        res = requests.get(url).text

        assert res != None

    def test_always_passes(self):
        assert True

if __name__ == '__main__':
    unittest.main()
