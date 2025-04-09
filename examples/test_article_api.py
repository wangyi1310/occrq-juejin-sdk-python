import os
import unittest
from unittest.mock import MagicMock

from juejin.article import ArticleAPI, ArticleRequest, UpdateArticleRequest, DescribeArticleListRequest, \
    DescribeArticleDetailRequest
from juejin.client import JuejinClient


class TestArticleAPI(unittest.TestCase):
    def setUp(self):
        cookies = os.environ["JUEJIN_COOKIE"]
        ms_token = os.environ["JUEJIN_MS_TOKEN"]
        a_bogus = os.environ["JUEJIN_A_BOGUS"]

        self.client = JuejinClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
        self.article_api = ArticleAPI(self.client)
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {
            "err_no": 0,
            "err_msg": "success",
            "data": {}
        }

    def test_create_article(self):
        result = self.article_api.create_draft(ArticleRequest())
        print(result)

    def test_update_article(self):
        update = UpdateArticleRequest(id="")
        result = self.article_api.update_draft(update)
        print(result)

    def test_delete_draft(self):
        result = self.article_api.delete_draft(draft_id="")
        print(result)

    def test_push_article(self):
        result = self.article_api.publish(draft_id="")
        print(result)

    def test_delete_article(self):
        result = self.article_api.delete(id="")
        print(result)

    def test_list(self):
        result = self.article_api.describe_list(DescribeArticleListRequest())
        print(result)

    def test_list_for_draft(self):
        result = self.article_api.describe_draft_list(DescribeArticleListRequest())
        print(result)

    def test_get_draft_detail(self):
        result = self.article_api.describe_draft_detail(draft_id="")
        print(result)

    def test_get_detail(self):
        req = DescribeArticleDetailRequest()
        req.article_id = ""
        req.client_type=0
        result = self.article_api.describe_detail(req)
        print(result)



if __name__ == '__main__':
    unittest.main()
