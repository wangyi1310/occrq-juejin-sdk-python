import os
import unittest
from unittest.mock import MagicMock

import juejin
from juejin.models import ArticleRequest, UpdateArticleRequest, DescribeArticleDetailRequest, DescribeArticleListRequest

print(print(os.environ))


class TestArticleAPI(unittest.TestCase):
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

    def test_create_article(self):
        result = self.client.create_article_draft(ArticleRequest().from_dict(
            {"title": "这是我的第一篇博客"})
        )
        print(result)

    def test_update_article(self):
        update = UpdateArticleRequest(id="")
        result = self.client.update_article_draft(update)
        print(result)

    def test_delete_draft(self):
        result = self.client.delete_article_draft(draft_id="")
        print(result)

    def test_push_article(self):
        result = self.client.publish_article_draft(draft_id="")
        print(result)

    def test_delete_article(self):
        result = self.client.delete_article(article_id="")
        print(result)

    def test_list(self):
        result = self.client.describe_article_list(DescribeArticleListRequest())
        print(result)

    def test_list_for_draft(self):
        result = self.client.describe_article_draft_list(DescribeArticleListRequest())
        print(result)

    def test_get_draft_detail(self):
        result = self.client.describe_article_draft_detail(draft_id="")
        print(result)

    def test_get_detail(self):
        req = DescribeArticleDetailRequest()
        req.article_id = "7429626822868336649"
        resp = self.client.describe_article_detail(req)
        print(resp.to_json())


if __name__ == '__main__':
    unittest.main()
