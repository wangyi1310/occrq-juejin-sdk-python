# 掘金(Juejin) Python SDK

## 项目简介

`occrq-juejin-sdk` 是一个收集公开的掘金API并封装的Python封装库，部分参数可选值未知，需要自行查找，当前仅提供了部分掘金平台功能接口，包括用户管理、文章操作等功能。

## 主要特性

- 完整的掘金文档/用户API封装
- 简洁易用的Python接口
- 支持文章创建、编辑、删除管理

## 安装方式

```bash
pip install occrq-juejin-sdk
```

## 快速开始

### 初始化客户端

```python
from juejin.client import JuejinClient

# 初始化客户端(需要从浏览器获取认证信息)
client = JuejinClient(
    cookie="your_cookie",
    a_bogus="your_a_bogus",
    ms_token="your_ms_token"
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

欢迎提交Pull Request或Issue报告问题。提交代码前请确保：
1. 通过所有单元测试
2. 更新相关文档
3. 遵循PEP8代码风格

## 许可证

MIT License
