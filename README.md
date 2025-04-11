# 掘金(Juejin) Python SDK

## 项目简介

`occrq-juejin-python-sdk` 是一个收集公开的掘金API并封装的Python封装库，部分参数可选值未知，需要自行获取，当前仅提供了部分掘金平台功能接口，包括用户管理、文章操作等功能。

## 主要特性

- 完整的掘金文档/用户API封装
- 简洁易用的Python接口
- 支持用户签到
- 支持文章创建、编辑、删除管理

## 安装方式

```bash
pip install occrq-juejin-python-sdk
```

## 依赖版本
Python >= 3.8

## 快速开始

### 浏览器获取cookie，a_bogus，ms_token
登录后，进入掘金用户签到页面：https://juejin.cn/user/center/signin?from=sign_in_menu_bar
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
from juejin.client import JuejinClient
import os
# 初始化客户端(需要从浏览器获取认证信息) 需要使用签到功能时需必须设置ms_token/a_bogus，默认为空
cookies = os.getenv("JUEJIN_COOKIE")
ms_token = os.getenv("JUEJIN_MS_TOKEN")
a_bogus = os.getenv("JUEJIN_A_BOGUS")]

client = JuejinClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)

```


### 用户相关操作
#### 获取用户信息

```python
# 获取用户信息
import juejin
import os

# 初始化客户端(预先从浏览器获取登录信息) 使用签到功能时需要设置ms_token/a_bogus，默认为空
cookies = os.getenv("JUEJIN_COOKIE")
ms_token = os.getenv("JUEJIN_MS_TOKEN")
a_bogus = os.getenv("JUEJIN_A_BOGUS")

client = juejin.JuejinClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
# 打印用户信息
result = client.describe_user_info_package()
print(result)

```

### 文章管理
#### 创建一篇草稿
```python
import os
import juejin

from juejin.models import ArticleRequest

# 初始化客户端(需要从浏览器获取认证信息) 需要使用签到功能时需要设置ms_token/a_bogus，默认为空
cookies = os.environ["JUEJIN_COOKIE"]
ms_token = os.environ["JUEJIN_MS_TOKEN"]
a_bogus = os.environ["JUEJIN_A_BOGUS"]

client = juejin.JuejinClient(cookie=cookies, ms_token=ms_token, a_bogus=a_bogus)
result = client.create_article_draft(ArticleRequest().from_dict(
    {"title": "这是我的第一篇博客"})
)
# 创建草稿
print(f"result")

```
## API 文档

##### `describe_user_info_package()`
- **描述**：获取用户的信息包，包含用户的基本信息、计数信息等。
- **返回**：包含用户信息的字典，具体格式取决于掘金 API 的响应。
##### `describe_user_rank_info()`
- **描述**：获取用户的排行榜信息。
- **返回**：包含用户排行榜信息的字典，具体格式取决于掘金 API 的响应。
##### `create_user_check_in()`
- **描述**：执行用户签到操作。
- **返回**：：包含签到结果的字典，具体格式取决于掘金 API 的响应。
##### `describe_user_dynamic()`
- **描述**：：获取用户的动态信息。
- **返回**：包含用户动态信息的字典，具体格式取决于掘金 API 的响应。
#####  `create_article_draft(article_request)`
- **描述**：创建一篇新的文章草稿。
- **参数**：
  - `article_request` (ArticleRequest): 包含文章标题、内容等信息的请求对象。可以使用 ArticleRequest().from_dict({"title": "文章标题"}) 这样的方式构建。
- **返回**：包含创建结果的字典，具体格式取决于掘金 API 的响应。
##### `update_article_draft(ArticleRequest)`
- **描述**：更新一篇已有的文章草稿。
- **参数**：
`req (ArticleRequest):` 包含需要更新的文章信息的请求对象。
- **返回**：包含更新结果的字典，具体格式取决于掘金 API 的响应。
##### `delete_article_draft(draft_id)`
- **描述**：删除一篇文章草稿。
- **参数**：
draft_id (str): 要删除的文章草稿的 ID。
- **返回**：包含删除结果的字典，具体格式取决于掘金 API 的响应。
##### `delete_article(id)`
- **描述**：删除一篇文章。
- **参数**：
id (str): 要删除的文章的 ID。
- **返回**：包含删除结果的字典，具体格式取决于掘金 API 的响应。
  
#####  `publish_article_draft(draft_id)`
- **描述**：发布一篇文章草稿。
- **参数**：
draft_id (str): 要发布的文章草稿的 ID。
- **返回**：包含发布结果的字典，具体格式取决于掘金 API 的响应。
##### `describe_article_detail(draft_id)`
- **描述**：获取一篇文章的详细信息。
- **参数**：
draft_id (str): 要获取详情的文章草稿的 ID。
- **返回**：包含文章草稿详细信息的字典，具体格式取决于掘金 API 的响应。
##### `describe_article_detail(req)`
- **描述**：获取一篇文章的详细信息。
- **参数**：
req (DescribeArticleDetailRequest): 要获取详情的文章草稿的 ID。
- **返回**：包含文章草稿详细信息的字典，具体格式取决于掘金 API 的响应。
  
##### `describe_article_list(req)`
- **描述**：获取文章列表。
- **参数**：
req (DescribeArticleListRequest): 查询参数，例如分页信息、筛选条件等。
- **返回**：包含文章列表的字典，具体格式取决于掘金 API 的响应。

##### `describe_article_draft_list(req)`
- **描述**：获取草稿箱列表。
- **参数**：
req (DescribeArticleListRequest): 查询参数，例如分页信息、筛选条件等。
- **返回**：包含文章列表的字典，具体格式取决于掘金 API 的响应。


## 贡献指南

欢迎提交Pull Request或Issue报告问题。

## 许可证

MIT License
