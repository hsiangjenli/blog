# Enhanced Hexo Info API

這個擴展為您的 Hexo blog 提供了包含 `lang` 和其他自定義欄位的增強版 API。

## 新增的 API 端點

### 1. 增強版文章列表
```
GET /api/enhanced/getPosts/
```

返回所有文章，包含語言資訊：
```json
{
  "type": "getPostsEnhanced",
  "data": {
    "posts": [
      {
        "title": "[教學] 掃描模型的簡單範例",
        "date": "2025-06-14T00:00:00.000Z",
        "updated": "2025-06-14T00:00:00.000Z",
        "description": "",
        "categories": [],
        "tags": ["mlsecops"],
        "lang": "zh-TW",
        "slug": "tutorial-a-toy-example-of-scanning-models",
        "source_sha": "c71699f8d0ad067977a553f06e68c9509578fe87abcefa4f28d09ea89fc263ae",
        "origin_lang": "en",
        "_path": "tutorial-a-toy-example-of-scanning-models/",
        "_link": "https://hsiangjenli.github.io/blog/tutorial-a-toy-example-of-scanning-models/",
        "_id": "..."
      }
    ],
    "count": 1
  }
}
```

### 2. 增強版最新文章
```
GET /api/enhanced/getLatestPost/
```

返回最新文章，包含完整內容和語言資訊。

### 3. 增強版最新 5 篇文章
```
GET /api/enhanced/getLatest5Posts/
```

返回最新 5 篇文章，包含語言資訊。

### 4. 依語言篩選文章
```
GET /api/enhanced/getPostsByLang/{lang}/
```

例如：
- `/api/enhanced/getPostsByLang/zh-TW/` - 取得所有中文文章
- `/api/enhanced/getPostsByLang/en/` - 取得所有英文文章

注意：系統會自動為每個可用的語言創建對應的端點。

### 5. 取得可用語言列表
```
GET /api/enhanced/getLanguages/
```

返回所有可用的語言和每種語言的文章數量：
```json
{
  "type": "getLanguagesEnhanced",
  "data": {
    "languages": [
      { "lang": "zh-TW", "count": 25 },
      { "lang": "en", "count": 18 }
    ],
    "default": "en"
  }
}
```

## 包含的額外欄位

除了原本的欄位，增強版 API 還包含：

- `lang`: 文章的語言 (從 front-matter 的 `lang` 或 `language` 欄位讀取)
- `slug`: 文章的 slug
- `updated`: 更新時間
- `source_sha`: 如果有的話，來源 SHA (用於翻譯追蹤)
- `origin_lang`: 原始語言 (用於翻譯文章)
- `author`: 作者資訊
- `toc`: 目錄設定

## 使用方式

1. 確保 `_config.yml` 中已啟用 `hexo_info_api`
2. 部署或啟動開發服務器：`hexo server`
3. 訪問新的 API 端點：`http://localhost:4000/api/enhanced/getPosts/`

## 範例用法

### JavaScript
```javascript
// 取得所有文章
fetch('/api/enhanced/getPosts/')
  .then(response => response.json())
  .then(data => {
    data.data.posts.forEach(post => {
      console.log(`${post.title} (${post.lang})`);
    });
  });

// 取得中文文章
fetch('/api/enhanced/getPostsByLang/zh-TW/')
  .then(response => response.json())
  .then(data => {
    console.log(`找到 ${data.data.count} 篇中文文章`);
  });
```

### Python
```python
import requests

# 取得語言統計
response = requests.get('http://localhost:4000/api/enhanced/getLanguages/')
data = response.json()

for lang_info in data['data']['languages']:
    print(f"{lang_info['lang']}: {lang_info['count']} 篇文章")
```