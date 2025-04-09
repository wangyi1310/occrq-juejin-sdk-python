import os
import unittest
from unittest.mock import MagicMock

from juejin.client import JuejinClient


class TestClient(unittest.TestCase):
    def setUp(self):
        cookies = os.environ["JUEJIN_COOKIE"]
        ms_token = os.environ["JUEJIN_MS_TOKEN"]
        a_bogus = os.environ["JUEJIN_A_BOGUS"]

        self.client = JuejinClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {
            "err_no": 0,
            "err_msg": "success",
            "data": {}
        }


if __name__ == '__main__':
    unittest.main()
