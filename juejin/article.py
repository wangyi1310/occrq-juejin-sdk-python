from typing import Dict, Any

from .client import JuejinClient
from .const import ARTICLE_ID, DRAFT_ID
from .models import ArticleRequest, UpdateArticleRequest, DescribeArticleDetailRequest, DescribeArticleListRequest


class ArticleClient(JuejinClient):
    """Article related APIs"""

    def __init__(self, cookie: str, a_bogus: str = None, ms_token: str = None):
        super().__init__(cookie, a_bogus, ms_token)

    def create_draft(self, req: ArticleRequest) -> Dict[str, Any]:
        """
        Create a new article draft.

        Args:
            req (ArticleRequest): Request object containing article draft details.

        Returns:
            Dict[str, Any]: API response.
        """
        return self.request("POST", "/content_api/v1/article_draft/create", data=req)

    def update_draft(self, req: UpdateArticleRequest) -> Dict[str, Any]:
        """
        Update an existing article draft.

        Args:
            req (UpdateArticleRequest): Request object containing updated article draft details.

        Returns:
            Dict[str, Any]: API response.
        """
        return self.request("POST", "/content_api/v1/article_draft/update", data=req)

    def describe_draft_detail(self, draft_id: str) -> Dict[str, Any]:
        """
        Get details of an article draft.

        Args:
            draft_id (str): ID of the article draft.

        Returns:
            Dict[str, Any]: API response containing draft details.
        """
        return self.request("POST", "/content_api/v1/article_draft/detail", data={DRAFT_ID: draft_id})

    def describe_detail(self, req: DescribeArticleDetailRequest) -> Dict[str, Any]:
        """
        Get details of an article.

        Args:
            req (DescribeArticleDetailRequest): Request object containing article ID.

        Returns:
            Dict[str, Any]: API response containing article details.
        """
        return self.request("POST", "/content_api/v1/article/detail", data=req)

    def delete_draft(self, draft_id: str) -> Dict[str, Any]:
        """
        Delete an article draft.

        Args:
            draft_id (str): ID of the article draft to delete.

        Returns:
            Dict[str, Any]: API response indicating the result of the delete operation.
        """
        return self.request("POST", "/content_api/v1/article_draft/delete", data={DRAFT_ID: draft_id})

    def delete(self, id: str) -> Dict[str, Any]:
        """
        Delete an article.

        Args:
            id (str): ID of the article to delete.

        Returns:
            Dict[str, Any]: API response indicating the result of the delete operation.
        """
        return self.request("POST", "/content_api/v1/article/delete", data={ARTICLE_ID: id})

    def publish(self, draft_id: str) -> Dict[str, Any]:
        """
        Publish an article draft.

        Args:
            draft_id (str): ID of the article draft to publish.

        Returns:
            Dict[str, Any]: API response indicating the result of the publish operation.
        """
        return self.request("POST", "/content_api/v1/article/publish", data={DRAFT_ID: draft_id})

    def describe_list(self, req: DescribeArticleListRequest) -> Dict[str, Any]:
        """
        Get a list of articles.

        Args:
            req (DescribeArticleListRequest): Request object containing filters and pagination details.

        Returns:
            Dict[str, Any]: API response containing a list of articles.
        """
        return self.request("POST", "/content_api/v1/article/list_by_user", data=req)

    def describe_draft_list(self, req: DescribeArticleListRequest) -> Dict[str, Any]:
        """
        Get a list of article drafts.

        Args:
            req (DescribeArticleListRequest): Request object containing filters and pagination details.

        Returns:
            Dict[str, Any]: API response containing a list of article drafts.
        """
        return self.request("POST", "/content_api/v1/article_draft/list_by_user", data=req)

    def describe_article_detail(self, article_id: str) -> Dict[str, Any]:
        """
        Get article details.

        Args:
            article_id (str): Article ID to retrieve.

        Returns:
            Dict[str, Any]: Article detail data.
        """
        return self.request("GET", "/content_api/v1/article/detail", params={ARTICLE_ID: article_id})
