import json


class BaseRequest(object):

    def _serialize(self):
        return json.dumps({k: v for k, v in self.__dict__.items() if v is not None})

    def from_dict(self, data: dict):
        """
        从字典自动创建ArticleRequest对象
        通过类型注解自动获取有效属性名
        """
        attrs = self.__dict__
        for k, v in data.items():
            if k in attrs:
                setattr(self, k, v)
        return self

class ArticleRequest(BaseRequest):
    """
    文章请求
    """

    def __init__(self,
                 category_id: str = "0",
                 tag_ids: list = None,
                 link_url: str = "",
                 cover_image: str = "",
                 title: str = "未命名文章",
                 author: str = "",
                 brief_content: str = "",
                 edit_type: int = 10,
                 html_content: str = "deprecated",
                 mark_content: str = "",
                 theme_ids: list = None,
                 pics: list = None):
        """
        初始化文章请求参数

        参数:
            category_id (str): 文章分类ID，默认"0"
            tag_ids (list): 标签ID列表，默认空列表
            link_url (str): 外链URL，默认空字符串
            cover_image (str): 封面图片URL，默认空字符串
            title (str): 文章标题，默认"未命名文章"
            author (str): 作者名称，默认空字符串
            brief_content (str): 文章摘要，默认空字符串
            edit_type (int): 编辑类型(10=Markdown)，默认10
            html_content (str): HTML内容(已弃用)，默认"deprecated"
            mark_content (str): Markdown内容，默认空字符串
            theme_ids (list): 主题ID列表，默认空列表
            pics (list): 图片列表，默认空列表
        """
        self.category_id = category_id
        self.tag_ids = tag_ids if tag_ids is not None else []
        self.link_url = link_url
        self.cover_image = cover_image
        self.title = title
        self.author = author
        self.brief_content = brief_content
        self.edit_type = edit_type
        self.html_content = html_content
        self.mark_content = mark_content
        self.theme_ids = theme_ids if theme_ids is not None else []
        self.pics = pics if pics is not None else []


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
