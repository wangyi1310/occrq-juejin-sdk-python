import json
import logging
from typing import Optional, Dict, Any, Union

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from juejin.error import JuejinAPIError
from juejin.models import BaseRequest

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

    BASE_URL = "https://api.juejin.cn"
    DEFAULT_USER_AGENT = "juejin-python-sdk/1.0.0"

    def __init__(self, cookie: str, a_bogus: str = None, ms_token: str = None):
        """
        Initialize the Juejin client

        Parameters:
            cookie: Juejin authentication cookie
            a_bogus: Authentication parameter
            ms_token: Authentication token
        """
        self._config = RequestConfig()
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
            data: Optional[Union[Dict[str, Any], BaseRequest]] = None,
            headers: Optional[Dict[str, str]] = None,
            extra_auth: bool = False
    ) -> tuple[str, Optional[str], Dict[str, str]]:
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
                "a_bogus": self._a_bogus,
                "spider": "0",
                "msToken": self._ms_token
            })

        # Serialize the request body
        request_data = None
        if data:
            if isinstance(data, BaseRequest):
                request_data = data._serialize()
            elif isinstance(data, dict):
                request_data = json.dumps(data, ensure_ascii=False)

        return url, request_data, headers

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
            data: Optional[Union[Dict[str, Any], BaseRequest]] = None,
            headers: Optional[Dict[str, str]] = None,
            extra_auth: bool = False
    ) -> Dict[str, Any]:
        try:
            # Prepare request parameters
            url, request_data, headers = self._prepare_request(
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

