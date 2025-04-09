import json


class BaseRequest(object):
    def _serialize(self):
        return json.dumps({k: v for k, v in self.__dict__.items() if v is not None})

class ArticleRequest(BaseRequest):
    """
    文章请求
    """

    def __init__(self):
        self.category_id = "0"
        self.tag_ids = []
        self.link_url = ""
        self.cover_image = ""
        self.title = "213123213"
        self.author = ""
        self.brief_content = ""
        self.edit_type = 10
        self.html_content = "deprecated"
        self.mark_content = ""
        self.theme_ids = []
        self.pics = []


class UpdateArticleRequest(ArticleRequest):
    def __init__(self, id):
        super().__init__()
        self.id = id


class DescribeArticleListRequest(BaseRequest):
    def __init__(self):
        self.audit_status = None
        self.keyword = ""
        self.page_no = 1
        self.page_size = 10


class DescribeArticleDetailRequest(BaseRequest):
    def __init__(self):
        self.article_id = None
        self.client_type = 0
        self.forbid_count = False
        self.is_pre_load = False
        self.need_theme = True
        self.req_from = 1
