import os
import unittest
from unittest.mock import patch, MagicMock
from juejin.client import JuejinClient
from juejin.user import UserAPI

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        cookies = os.environ["JUEJIN_COOKIE"]
        ms_token = os.environ["JUEJIN_MS_TOKEN"]
        a_bogus = os.environ["JUEJIN_A_BOGUS"]

        self.client = JuejinClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)

        self.user_api = UserAPI(self.client)
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {
            "err_no": 0,
            "err_msg": "success",
            "data": {}
        }

    # @patch('juejin.client.JuejinClient._request')
    def test_get_signin_info(self):
        # mock_request.return_value = {"count": 1}
        # result = self.user_api.get_signin_info()
        # print(result)
        # self.assertEqual(result, {"count": 1})
        # mock_request.assert_called_once_with(
        #     "GET", "/growth_api/v1/get_counts"
        # )

    # @patch('juejin.client.JuejinClient._request')
    # def test_get_today_status(self, mock_request):
    #     mock_request.return_value = {"signed": True}
        result = self.user_api.get_growth_level()
        # self.assertEqual(result, {"signed": True})
        # mock_request.assert_called_once_with(
        #     "GET", "/growth_api/v1/get_today_status"
        # )
        print(result)

    def test_get_user_info(self):
        result = self.user_api.get_info_package()
        print(result)

    def test_get_user_rank(self):
        result = self.user_api.get_rank_user_info()
        print(result)

    def test_check_in(self):
        result = self.user_api.check_in()
        print(result)

    def test_dynamic(self):
        result = self.user_api.dynamic()
        print(result)


if __name__ == '__main__':
    unittest.main()
