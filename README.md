# 掘金(Juejin) Python SDK

## 项目简介

`occrq-juejin-sdk` 是一个收集公开的掘金API并封装的Python封装库，部分参数可选值未知，需要自行在外部公开的页面，当前仅提供了部分掘金平台功能接口，包括用户管理、文章操作等功能。

## 主要特性

- 完整的掘金文档/用户API封装
- 简洁易用的Python接口
- 支持用户签到
- 支持文章创建、编辑、删除管理

## 安装方式

```bash
pip install occrq-juejin-sdk
```

## 快速开始

### 浏览器获取cookie，a_bogus，ms_token
登录后，进入掘金用户签到页面：
https://juejin.cn/user/center/signin?from=sign_in_menu_bar
<img width="1528" alt="Clipboard_Screenshot_1744196997" src="https://github.com/user-attachments/assets/d99a3ffd-6059-49bb-b838-1096535206bb" />

F12打开浏览器开发者工具，选择Network，刷新页面，搜索check_in_rulers接口：
<img width="1578" alt="Clipboard_Screenshot_1744197334" src="https://github.com/user-attachments/assets/8d156b9b-2df6-4819-82cb-d16445d9025c" />


#### 获取cookie
<img width="1578" alt="Clipboard_Screenshot_1744197334" src="https://github.com/user-attachments/assets/01c8b633-e0a8-4f33-a401-c19b4020b993" />

#### 获取a_bogus，ms_token
<img width="1449" alt="Clipboard_Screenshot_1744197521" src="https://github.com/user-attachments/assets/2c040196-3986-4f6c-82f8-6afa1d3b18ee" />


### 初始化客户端

```python
from juejin.client import JuejinClient

# 初始化客户端(需要从浏览器获取认证信息)
client = JuejinClient(
    cookie="your_cookie", // 用户cookie
    a_bogus="your_a_bogus", // 额外的用户校验参数，如使用签到功能时需要指定
    ms_token="your_ms_token" // 额外的用户校验参数，如使用签到功能时需要指定
)
```


### 用户相关操作

```python
# 获取用户信息
user_info = client.user.get_counts()
print(f"用户信息: {user_info}")

# 检查签到状态
sign_status = client.user.get_today_status()
print(f"今日签到状态: {'已签到' if sign_status['data']['check_in_done'] else '未签到'}")
```

### 文章管理

```python
# 获取首页文章列表
articles = client.article.get_home_articles()
print(f"获取到{len(articles['data'])}篇文章")

# 创建新文章
new_article = client.article.create_article(
    title="我的技术文章",
    content="这里是文章内容...",
    category_id="1",
    tags=["Python", "后端"]
)
print(f"新文章ID: {new_article['data']['article_id']}")
```

## API参考

### JuejinClient 类

```python
JuejinClient(cookie: str, a_bogus: str, ms_token: str)
```
- `cookie`: 掘金认证cookie
- `a_bogus`: 掘金API安全参数
- `ms_token`: 掘金API安全令牌

### 文章API (client.article)

- `get_home_categories()`: 获取首页分类
- `get_home_articles()`: 获取首页文章
- `create_article()`: 创建新文章
- `update_article()`: 更新文章
- `delete_article()`: 删除文章
- `get_article_detail()`: 获取文章详情

### 用户API (client.user)

- `get_counts()`: 获取用户统计信息
- `get_today_status()`: 获取今日签到状态
- `get_growth_level()`: 获取用户成长等级

## 贡献指南

欢迎提交Pull Request或Issue报告问题。

## 许可证

MIT License
