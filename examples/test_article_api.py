import os
import unittest
from unittest.mock import MagicMock

from juejin.article import ArticleRequest, UpdateArticleRequest, DescribeArticleListRequest, \
    DescribeArticleDetailRequest, ArticleClient


class TestArticleAPI(unittest.TestCase):
    def setUp(self):
        cookies = os.getenv("JUEJIN_COOKIE")
        ms_token = os.getenv("JUEJIN_MS_TOKEN")
        a_bogus = os.getenv("JUEJIN_A_BOGUS")

        self.article_client = ArticleClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {
            "err_no": 0,
            "err_msg": "success",
            "data": {}
        }

    def test_create_article(self):
        result = self.article_client.create_draft(ArticleRequest().from_dict(
            {"title": "这是我的第一篇博客"})
        )
        print(result)

    def test_update_article(self):
        update = UpdateArticleRequest(id="")
        result = self.article_client.update_draft(update)
        print(result)

    def test_delete_draft(self):
        result = self.article_client.delete_draft(draft_id="")
        print(result)

    def test_push_article(self):
        result = self.article_client.publish(draft_id="")
        print(result)

    def test_delete_article(self):
        result = self.article_client.delete(id="")
        print(result)

    def test_list(self):
        result = self.article_client.describe_list(DescribeArticleListRequest())
        print(result)

    def test_list_for_draft(self):
        result = self.article_client.describe_draft_list(DescribeArticleListRequest())
        print(result)

    def test_get_draft_detail(self):
        result = self.article_client.describe_draft_detail(draft_id="")
        print(result)

    def test_get_detail(self):
        req = DescribeArticleDetailRequest()
        req.article_id = ""
        req.client_type = 0
        result = self.article_client.describe_detail(req)
        print(result)


if __name__ == '__main__':
    unittest.main()
