import os
import unittest
from unittest.mock import MagicMock

import juejin
from juejin.client import AuthConfig


class TestUserClient(unittest.TestCase):
    def setUp(self):
        # 使用签到功能时需要初始化auth_config
        auth_config = AuthConfig()
        auth_config.ms_token = '-='
        auth_config.a_bogus = ''
        auth_config.aid = '2608'
        auth_config.uuid = '7491181683644925450'
        cookie = ''
        self.client = juejin.JuejinClient(auth_config=auth_config, cookie=cookie)

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
        result = self.client.create_user_sign_in()
        print(result)

    def test_dynamic(self):
        result = self.client.describe_user_dynamic()
        print(result)


if __name__ == '__main__':
    unittest.main()
