# 掘金(Juejin) Python SDK

## 项目简介

`occrq-juejin-python-sdk` 是一个收集公开的掘金API并封装的Python封装库，部分参数可选值未知，需要自行在外部公开的页面，当前仅提供了部分掘金平台功能接口，包括用户管理、文章操作等功能。

## 主要特性

- 完整的掘金文档/用户API封装
- 简洁易用的Python接口
- 支持用户签到
- 支持文章创建、编辑、删除管理

## 安装方式

```bash
pip install occrq-juejin-python-sdk
```

## 快速开始

### 浏览器获取cookie，a_bogus，ms_token
登录后，进入掘金用户签到页面：
<img width="1565" alt="Clipboard_Screenshot_1744198424" src="https://github.com/user-attachments/assets/8be2f82f-a83e-47e1-8437-ecc3961d9f0e" />


F12打开浏览器开发者工具，选择Network，刷新页面，搜索check_in_rulers接口：
<img width="1601" alt="Clipboard_Screenshot_1744198137" src="https://github.com/user-attachments/assets/8c9ce5ec-35e1-40ab-8dd6-38be318df4e5" />


#### 获取cookie
<img width="1571" alt="Clipboard_Screenshot_1744198219" src="https://github.com/user-attachments/assets/e6a509c1-25fc-4000-a1d0-31a7a44f62c7" />

#### 获取a_bogus，ms_token
<img width="1575" alt="Clipboard_Screenshot_1744198345" src="https://github.com/user-attachments/assets/143da920-e812-4587-8d03-c44afeb8d397" />


### 初始化客户端

```python
# UserClient初始化
from juejin.user import UserClient
import os
# 初始化客户端(需要从浏览器获取认证信息) 需要使用签到功能时需要设置ms_token/a_bogus，默认为空
cookies = os.environ["JUEJIN_COOKIE"] 
ms_token = os.environ["JUEJIN_MS_TOKEN"]
a_bogus = os.environ["JUEJIN_A_BOGUS"]
user_client = UserClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
```


### 用户相关操作
#### 获取用户信息
```python
# 获取用户信息
import os
from juejin.user import UserClient
# 初始化客户端(预先从浏览器获取登录信息) 使用签到功能时需要设置ms_token/a_bogus，默认为空
cookies = os.environ["JUEJIN_COOKIE"] 
ms_token = os.environ["JUEJIN_MS_TOKEN"]
a_bogus = os.environ["JUEJIN_A_BOGUS"]
user_client = UserClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
# 打印用户信息
result = user_client.get_info_package()
print(result)
```

### 文章管理
#### 创建一篇草稿
```python
import os

from juejin.article import ArticleClient
from juejin.models import ArticleRequest

# 初始化客户端(需要从浏览器获取认证信息) 需要使用签到功能时需要设置ms_token/a_bogus，默认为空
cookies = os.environ["JUEJIN_COOKIE"]
ms_token = os.environ["JUEJIN_MS_TOKEN"]
a_bogus = os.environ["JUEJIN_A_BOGUS"]
article_client = ArticleClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
result = article_client.create_draft(ArticleRequest().from_dict(
    {"title": "这是我的第一篇博客"})
)
# 创建草稿
print(f"result")
```


## 贡献指南

欢迎提交Pull Request或Issue报告问题。

## 许可证

MIT License
