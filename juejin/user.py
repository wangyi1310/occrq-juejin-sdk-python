from typing import Dict, Any

from .client import JuejinClient


class UserAPI:
    """User related APIs"""

    def __init__(self, client: JuejinClient):
        self._client = client

    def get_counts(self) -> Dict[str, Any]:
        """Get user sign-in information"""
        return self._client.request("GET", "/growth_api/v1/get_counts")

    def get_today_status(self) -> Dict[str, Any]:
        """Get today's sign-in status"""
        return self._client.request("GET", "/growth_api/v2/get_today_status")

    def get_info_package(
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
        return self._client.request("POST", "/user_api/v1/user/get_info_pack", data=data)

    def get_rank_user_info(self, fro: int = 1, item_rank_type: int = 3, item_sub_rank_type: str = "0") \
            -> Dict[str, Any]:
        """获取用户排行榜信息"""
        data = {
            "from": fro,
            "item_rank_type": item_rank_type,
            "item_sub_rank_type": item_sub_rank_type,
        }
        return self._client.request("POST", "/user_api/v1/quality_user/rank", data=data)

    def check_in(self) -> Dict[str, Any]:
        """签到"""
        data = {}
        return self._client.request("POST", "/growth_api/v1/check_in", data=data, extra_auth=True)

    def dynamic(self) -> Dict[str, Any]:
        """获取动态"""
        return self._client.request("GET", "/user_api/v1/user/dynamic")


