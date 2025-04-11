import json
import logging
from typing import Optional, Dict, Any, Union

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from juejin.const import DRAFT_ID, ARTICLE_ID
from juejin.error import JuejinAPIError
from juejin.models import BaseModule, ArticleRequest, UpdateArticleRequest, DescribeArticleDetailRequest, \
    DescribeArticleListRequest, DescribeArticleDetailResponse

# Configure logging
logger = logging.getLogger(__name__)


class RequestConfig:
    """Request configuration class"""
    timeout: int = 10
    max_retries: int = 3
    retry_backoff_factor: float = 0.5
    retry_status_codes: tuple = (500, 502, 503, 504)


class JuejinClient:
    """Juejin API client"""

    BASE_URL = "http://api.juejin.cn"
    DEFAULT_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"

    def __init__(self, cookie: str, a_bogus: str = None, ms_token: str = None, config: RequestConfig = RequestConfig()):
        """
        Initialize the Juejin client

        Parameters:
            cookie: Juejin authentication cookie
            a_bogus: Authentication parameter
            ms_token: Authentication token
        """
        self._config = config
        self.session = requests.Session()
        self._set_session(cookie)
        self._a_bogus = a_bogus
        self._ms_token = ms_token

    def _set_session(self, cookie: str) -> None:
        # Set retry strategy
        retry_strategy = Retry(
            total=self._config.max_retries,
            backoff_factor=self._config.retry_backoff_factor,
            status_forcelist=self._config.retry_status_codes
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)

        # Set default request headers
        self.session.headers.update({
            "cookie": cookie,
            "user-agent": self.DEFAULT_USER_AGENT,
            "accept": "application/json"
        })

    def _prepare_request(
            self,
            method: str,
            endpoint: str,
            params: Optional[Dict[str, Any]] = None,
            data: Optional[Union[Dict[str, Any], BaseModule]] = None,
            headers: Optional[Dict[str, str]] = None,
            extra_auth: bool = False
    ) -> tuple[str, Optional[str], Dict[str, str],  Dict[str, str]]:
        """Prepare request parameters"""
        url = f"{self.BASE_URL}{endpoint}"
        headers = headers or {}

        # Set POST request headers
        if method.upper() == "POST":
            headers.setdefault("content-type", "application/json")

        # Add additional authentication parameters
        if extra_auth:
            params = params or {}
            params.update({
                "aid": "2608",
                "uuid": "7491181683644925450",
                "spider": "0",
                "msToken": self._ms_token,
                "a_bogus": self._a_bogus,
            })

        # Serialize the request body
        request_data = None
        if data is not None:
            if isinstance(data, BaseModule):
                request_data = data._serialize()
            elif isinstance(data, dict):
                request_data = json.dumps(data, ensure_ascii=False)

        return url, request_data, headers, params

    def _parse_response(self, response: requests.Response) -> Dict[str, Any]:
        """Parse the response data"""
        try:
            rsp = response.json()
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {e}\nResponse content: {response.text[:200]}")
            raise JuejinAPIError(f"JSON parsing failed: {str(e)}", -1)

        # Check the API error code
        if rsp.get("err_no") != 0:
            error_msg = rsp.get("err_msg", "Unknown error")
            error_code = rsp.get("err_no", -1)
            logger.error(f"API error: {error_code} - {error_msg}")
            raise JuejinAPIError(error_msg, error_code)

        return rsp.get("data", {})

    def request(
            self,
            method: str,
            endpoint: str,
            params: Optional[Dict[str, Any]] = None,
            data: Optional[Union[Dict[str, Any], BaseModule]] = None,
            headers: Optional[Dict[str, str]] = None,
            extra_auth: bool = False
    ) -> Dict[str, Any]:
        try:
            # Prepare request parameters
            url, request_data, headers, params = self._prepare_request(
                method, endpoint, params, data, headers, extra_auth
            )

            logger.debug(f"Sending request: {method} {url}")

            # Send the request
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=request_data,
                headers=headers,
                timeout=self._config.timeout
            )

            # Check the HTTP status code
            response.raise_for_status()

            # Parse the response
            return self._parse_response(response)

        except requests.exceptions.RequestException as e:
            logger.error(f"Network request failed: {str(e)}")
            raise JuejinAPIError(f"Network request failed: {str(e)}", -2)
        except Exception as e:
            logger.error(f"Unknown error: {str(e)}", exc_info=True)
            raise JuejinAPIError(f"Unknown error: {str(e)}", -3)

    def create_article_draft(self, req: ArticleRequest) -> Dict[str, Any]:
        """
        Create a new article draft.

        Args:
            req (ArticleRequest): Request object containing article draft details.

        Returns:
            Dict[str, Any]: API response.
        """
        return self.request("POST", "/content_api/v1/article_draft/create", data=req)

    def update_article_draft(self, req: UpdateArticleRequest) -> Dict[str, Any]:
        """
        Update an existing article draft.

        Args:
            req (UpdateArticleRequest): Request object containing updated article draft details.

        Returns:
            Dict[str, Any]: API response.
        """
        return self.request("POST", "/content_api/v1/article_draft/update", data=req)

    def describe_article_draft_detail(self, draft_id: str) -> Dict[str, Any]:
        """
        Get details of an article draft.

        Args:
            draft_id (str): ID of the article draft.

        Returns:
            Dict[str, Any]: API response containing draft details.
        """
        return self.request("POST", "/content_api/v1/article_draft/detail", data={DRAFT_ID: draft_id})

    def describe_article_detail(self, req: DescribeArticleDetailRequest) -> DescribeArticleDetailResponse:
        """
        Get details of an article.

        Args:
            req (DescribeArticleDetailRequest): Request object containing article ID.

        Returns:
            Dict[str, Any]: API response containing article details.
        """
        data = self.request("POST", "/content_api/v1/article/detail", data=req)
        resp = DescribeArticleDetailResponse(data)
        return resp

    def delete_article_draft(self, draft_id: str) -> Dict[str, Any]:
        """
        Delete an article draft.

        Args:
            draft_id (str): ID of the article draft to delete.

        Returns:
            Dict[str, Any]: API response indicating the result of the delete operation.
        """
        return self.request("POST", "/content_api/v1/article_draft/delete", data={DRAFT_ID: draft_id})

    def delete_article(self, article_id: str) -> Dict[str, Any]:
        """
        Delete an article.

        Args:
            article_id (str): ID of the article to delete.

        Returns:
            Dict[str, Any]: API response indicating the result of the delete operation.
        """
        return self.request("POST", "/content_api/v1/article/delete", data={ARTICLE_ID: article_id})

    def publish_article_draft(self, draft_id: str) -> Dict[str, Any]:
        """
        Publish an article draft.

        Args:
            draft_id (str): ID of the article draft to publish.

        Returns:
            Dict[str, Any]: API response indicating the result of the publish operation.
        """
        return self.request("POST", "/content_api/v1/article/publish", data={DRAFT_ID: draft_id})

    def describe_article_list(self, req: DescribeArticleListRequest) -> Dict[str, Any]:
        """
        Get a list of articles.

        Args:
            req (DescribeArticleListRequest): Request object containing filters and pagination details.

        Returns:
            Dict[str, Any]: API response containing a list of articles.
        """
        return self.request("POST", "/content_api/v1/article/list_by_user", data=req)

    def describe_article_draft_list(self, req: DescribeArticleListRequest) -> Dict[str, Any]:
        """
        Get a list of article drafts.

        Args:
            req (DescribeArticleListRequest): Request object containing filters and pagination details.

        Returns:
            Dict[str, Any]: API response containing a list of article drafts.
        """
        return self.request("POST", "/content_api/v1/article_draft/list_by_user", data=req)

    def describe_user_counts(self) -> Dict[str, Any]:
        """Get user sign-in information"""
        return self.request("GET", "/growth_api/v1/get_counts")

    def describe_user_today_status(self) -> Dict[str, Any]:
        """Get today's sign-in status"""
        return self.request("GET", "/growth_api/v2/get_today_status")

    def describe_user_info_package(
            self,
            user: bool = True,
            user_counter: bool = True,
            user_growth_info: bool = True
    ) -> Dict[str, Any]:
        """获取用户信息包

        参数:
            user: 是否包含用户基本信息
            user_counter: 是否包含用户计数信息
            user_growth_info: 是否包含用户成长信息

        返回:
            包含请求信息的字典
        """
        data = {
            "pack_req": {
                "user": user,
                "user_counter": user_counter,
                "user_growth_info": user_growth_info,
            }
        }
        return self.request("POST", "/user_api/v1/user/get_info_pack", data=data)

    def describe_user_rank_info(self, fro: int = 1, item_rank_type: int = 3, item_sub_rank_type: str = "0") \
            -> Dict[str, Any]:
        """获取用户排行榜信息"""
        data = {
            "from": fro,
            "item_rank_type": item_rank_type,
            "item_sub_rank_type": item_sub_rank_type,
        }
        return self.request("POST", "/user_api/v1/quality_user/rank", data=data)

    def create_user_sign_in(self) -> Dict[str, Any]:
        """签到"""
        data = {}
        return self.request("POST", "/growth_api/v1/check_in", data=data, extra_auth=True)

    def describe_user_dynamic(self) -> Dict[str, Any]:
        """获取动态"""
        return self.request("GET", "/user_api/v1/user/dynamic")
