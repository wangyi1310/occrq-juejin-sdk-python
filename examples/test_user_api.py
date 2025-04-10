import os
import unittest
from unittest.mock import MagicMock

import juejin


class TestUserClient(unittest.TestCase):
    def setUp(self):
        cookies = os.getenv("JUEJIN_COOKIE")
        ms_token = os.getenv("JUEJIN_MS_TOKEN")
        a_bogus = os.getenv("JUEJIN_A_BOGUS")
        self.client = juejin.JuejinClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {
            "err_no": 0,
            "err_msg": "success",
            "data": {}
        }

    def test_get_user_info(self):
        result = self.client.describe_user_info_package()
        print(result)

    def test_get_user_rank(self):
        result = self.client.describe_user_rank_info()
        print(result)

    def test_check_in(self):
        result = self.client.create_user_check_in()
        print(result)

    def test_dynamic(self):
        result = self.client.describe_user_dynamic()
        print(result)


if __name__ == '__main__':
    unittest.main()
