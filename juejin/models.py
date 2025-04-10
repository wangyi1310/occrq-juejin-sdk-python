import json
from typing import Dict, Any


class DefaultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, object) and hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)


class BaseModule(object):

    def _serialize(self):
        return json.dumps({k: v for k, v in self.__dict__.items() if v is not None})

    def to_json(self):
        return json.dumps(self, cls=DefaultEncoder)

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


class ArticleRequest(BaseModule):
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


class DescribeArticleListRequest(BaseModule):
    def __init__(self):
        self.audit_status = None
        self.keyword = ""
        self.page_no = 1
        self.page_size = 10


class DescribeArticleDetailRequest(BaseModule):
    def __init__(self):
        self.article_id = None
        self.client_type = 2608
        self.forbid_count = False
        self.is_pre_load = False
        self.need_theme = True
        self.req_from = 1


class University:
    def __init__(self, university_id: str, name: str, logo: str):
        self.university_id = university_id
        self.name = name
        self.logo = logo


class Major:
    def __init__(self, major_id: str, parent_id: str, name: str):
        self.major_id = major_id
        self.parent_id = parent_id
        self.name = name


class UserGrowthInfo:
    def __init__(self, data: Dict[str, Any]):
        self.user_id = data.get("user_id")
        self.jpower = data.get("jpower")
        self.jscore = data.get("jscore")
        self.jpower_level = data.get("jpower_level")
        self.jscore_level = data.get("jscore_level")
        self.jscore_title = data.get("jscore_title")
        self.author_achievement_list = data.get("author_achievement_list", [])
        self.vip_level = data.get("vip_level")
        self.vip_title = data.get("vip_title")
        self.jscore_next_level_score = data.get("jscore_next_level_score")
        self.jscore_this_level_mini_score = data.get("jscore_this_level_mini_score")
        self.vip_score = data.get("vip_score")


class UserPrivInfo:
    def __init__(self, data: Dict[str, Any]):
        self.administrator = data.get("administrator", 0)
        self.builder = data.get("builder", 0)
        self.favorable_author = data.get("favorable_author", 0)
        self.book_author = data.get("book_author", 0)
        self.forbidden_words = data.get("forbidden_words", 0)
        self.can_tag_cnt = data.get("can_tag_cnt", 0)
        self.auto_recommend = data.get("auto_recommend", 0)
        self.signed_author = data.get("signed_author", 0)
        self.popular_author = data.get("popular_author", 0)
        self.can_add_video = data.get("can_add_video", 0)


class AuthorUserInfo:
    def __init__(self, data: Dict[str, Any]):
        self.user_id = data.get("user_id")
        self.user_name = data.get("user_name")
        self.company = data.get("company")
        self.job_title = data.get("job_title")
        self.avatar_large = data.get("avatar_large")
        self.level = data.get("level")
        self.description = data.get("description")
        self.followee_count = data.get("followee_count")
        self.follower_count = data.get("follower_count")
        self.post_article_count = data.get("post_article_count")
        self.digg_article_count = data.get("digg_article_count")
        self.got_digg_count = data.get("got_digg_count")
        self.got_view_count = data.get("got_view_count")
        self.post_shortmsg_count = data.get("post_shortmsg_count")
        self.digg_shortmsg_count = data.get("digg_shortmsg_count")
        self.isfollowed = data.get("isfollowed", False)
        self.favorable_author = data.get("favorable_author", 0)
        self.power = data.get("power")
        self.study_point = data.get("study_point")
        self.university = University(**data.get("university", {}))
        self.major = Major(**data.get("major", {}))
        self.student_status = data.get("student_status")
        self.select_event_count = data.get("select_event_count")
        self.select_online_course_count = data.get("select_online_course_count")
        self.identity = data.get("identity")
        self.is_select_annual = data.get("is_select_annual", False)
        self.select_annual_rank = data.get("select_annual_rank")
        self.annual_list_type = data.get("annual_list_type")
        self.extraMap = data.get("extraMap", {})
        self.is_logout = data.get("is_logout")
        self.annual_info = data.get("annual_info", [])
        self.account_amount = data.get("account_amount")
        self.user_growth_info = UserGrowthInfo(data.get("user_growth_info", {}))
        self.is_vip = data.get("is_vip", False)
        self.become_author_days = data.get("become_author_days")
        self.collection_set_article_count = data.get("collection_set_article_count")
        self.recommend_article_count_daily = data.get("recommend_article_count_daily")
        self.article_collect_count_daily = data.get("article_collect_count_daily")
        self.user_priv_info = UserPrivInfo(data.get("user_priv_info", {}))


class Tag:
    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.tag_id = data.get("tag_id")
        self.tag_name = data.get("tag_name")
        self.color = data.get("color")
        self.icon = data.get("icon")
        self.back_ground = data.get("back_ground")
        self.show_navi = data.get("show_navi")
        self.ctime = data.get("ctime")
        self.mtime = data.get("mtime")
        self.id_type = data.get("id_type")
        self.tag_alias = data.get("tag_alias")
        self.post_article_count = data.get("post_article_count")
        self.concern_user_count = data.get("concern_user_count")


class UserInteract:
    def __init__(self, data: Dict[str, Any]):
        self.id = data.get("id")
        self.omitempty = data.get("omitempty")
        self.user_id = data.get("user_id")
        self.is_digg = data.get("is_digg", False)
        self.is_follow = data.get("is_follow", False)
        self.is_collect = data.get("is_collect", False)
        self.collect_set_count = data.get("collect_set_count")


class Org:
    def __init__(self, data: Dict[str, Any]):
        self.is_followed = data.get("is_followed", False)


class Status:
    def __init__(self, data: Dict[str, Any]):
        self.push_status = data.get("push_status")


class Theme:
    def __init__(self, data: Dict[str, Any]):
        self.theme_id = data.get("theme_id")
        self.name = data.get("name")
        self.cover = data.get("cover")
        self.brief = data.get("brief")
        self.is_lottery = data.get("is_lottery", False)
        self.is_rec = data.get("is_rec", False)
        self.rec_rank = data.get("rec_rank")
        self.topic_ids = data.get("topic_ids", [])
        self.hot = data.get("hot")
        self.view_cnt = data.get("view_cnt")
        self.user_cnt = data.get("user_cnt")
        self.status = data.get("status")
        self.ctime = data.get("ctime")
        self.mtime = data.get("mtime")
        self.lottery_begin_time = data.get("lottery_begin_time")
        self.lottery_end_time = data.get("lottery_end_time")
        self.theme_type = data.get("theme_type")
        self.last_hot = data.get("last_hot")
        self.has_expiration = data.get("has_expiration", False)
        self.valid_begin_time = data.get("valid_begin_time")
        self.valid_end_time = data.get("valid_end_time")
        self.expired = data.get("expired")


class ThemeListItem:
    def __init__(self, data: Dict[str, Any]):
        self.theme = Theme(data.get("theme", {}))


class ArticleInfo:
    def __init__(self, data: Dict[str, Any]):
        self.article_id = data.get("article_id")
        self.user_id = data.get("user_id")
        self.category_id = data.get("category_id")
        self.tag_ids = data.get("tag_ids", [])
        self.visible_level = data.get("visible_level")
        self.link_url = data.get("link_url")
        self.cover_image = data.get("cover_image")
        self.is_gfw = data.get("is_gfw")
        self.title = data.get("title")
        self.brief_content = data.get("brief_content")
        self.is_english = data.get("is_english")
        self.is_original = data.get("is_original")
        self.user_index = data.get("user_index")
        self.original_type = data.get("original_type")
        self.original_author = data.get("original_author")
        self.content = data.get("content")
        self.ctime = data.get("ctime")
        self.mtime = data.get("mtime")
        self.rtime = data.get("rtime")
        self.draft_id = data.get("draft_id")
        self.view_count = data.get("view_count")
        self.collect_count = data.get("collect_count")
        self.digg_count = data.get("digg_count")
        self.comment_count = data.get("comment_count")
        self.hot_index = data.get("hot_index")
        self.is_hot = data.get("is_hot")
        self.rank_index = data.get("rank_index")
        self.status = data.get("status")
        self.verify_status = data.get("verify_status")
        self.audit_status = data.get("audit_status")
        self.mark_content = data.get("mark_content")
        self.display_count = data.get("display_count")
        self.is_markdown = data.get("is_markdown")
        self.app_html_content = data.get("app_html_content")
        self.version = data.get("version")
        self.web_html_content = data.get("web_html_content")
        self.meta_info = data.get("meta_info")
        self.catalog = data.get("catalog")
        self.homepage_top_time = data.get("homepage_top_time")
        self.homepage_top_status = data.get("homepage_top_status")
        self.content_count = data.get("content_count")
        self.read_time = data.get("read_time")
        self.pics_expire_time = data.get("pics_expire_time")


class DescribeArticleDetailResponse(BaseModule):
    def __init__(self, data: Dict[str, Any]):
        self.article_id = data.get("article_id")
        self.article_info = ArticleInfo(data.get("article_info", {}))
        self.author_user_info = AuthorUserInfo(data.get("author_user_info", {}))
        self.category = data.get("category")
        self.tags = [Tag(tag) for tag in data.get("tags", [])]
        self.user_interact = UserInteract(data.get("user_interact", {}))
        self.org = Org(data.get("org", {}))
        self.req_id = data.get("req_id")
        self.status = Status(data.get("status", {}))
        self.theme_list = [ThemeListItem(item) for item in data.get("theme_list", [])]
