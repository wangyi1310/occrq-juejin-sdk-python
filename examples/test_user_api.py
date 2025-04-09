import os
import unittest
from unittest.mock import MagicMock

from juejin.user import UserClient


class TestUserAPI(unittest.TestCase):
    def setUp(self):
        cookies = os.environ["JUEJIN_COOKIE"]
        ms_token = os.environ["JUEJIN_MS_TOKEN"]
        a_bogus = os.environ["JUEJIN_A_BOGUS"]
        self.user_client = UserClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {
            "err_no": 0,
            "err_msg": "success",
            "data": {}
        }

    def test_get_user_info(self):
        result = self.user_client.get_info_package()
        print(result)

    def test_get_user_rank(self):
        result = self.user_client.get_rank_user_info()
        print(result)

    def test_check_in(self):
        result = self.user_client.check_in()
        print(result)

    def test_dynamic(self):
        result = self.user_client.dynamic()
        print(result)


if __name__ == '__main__':
    unittest.main()
