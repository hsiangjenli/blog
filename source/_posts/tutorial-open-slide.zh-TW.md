---
title: '[教學] open-slide 使用教學'
date: '2026-07-03'
updated: '2026-07-03'
author:
- Hsiang-Jen Li
tags:
- ai
- skill
toc: true
slug: tutorial-open-slide
lang: zh-TW
source_sha: 876e33331124f9748ef4855a4dd8df57cbe769a21e25d8605ae516d0314b87b8
origin_lang: en
permalink: zh-TW/tutorial-open-slide/
translations:
  en: /tutorial-open-slide.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹

使用 open-slide 技能讓 AI 幫你快速生出一份簡報

<!-- more -->

# 🚀 實際操作

## Init Demo 簡報

```shell
npx @open-slide/cli init my-demo-slide
```

![20260703192900](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703192900.png)

![20260703193024](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703193024.png)

> 產生一份完整的 repo，包含啟動簡報的工具、Agent Skill、範例簡報等等

## 啟動簡報

- http://localhost:5173/

```shell
cd my-demo-slide
npm run dev
```

![20260703193221](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703193221.png)

![20260703193256](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703193256.png)

## 經常使用到的 Skill

- `/create-slide`: 用來新建或草擬 slide deck
- `/apply-comments`: 用來處理 @slide-comment 標記

## 實際操作截圖

### 使用 `/create-slide` 產生簡報

![20260703201640](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703201640.png)

### 需求問答（風格、頁數、效果等等）

![20260703201711](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703201711.png)

![20260703201906](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703201906.png)
![20260703201821](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703201821.png)

![20260703202157](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703202157.png)

### 第一版產出的簡報

![20260703211455](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703211455.png)

### 在簡報上留下建議

![20260703212008](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703212008.png)

1. 在簡報上留下 Comment
2. 在 terminal 上執行 `/apply-comments`，就會把根據 Comment 進行的修改

### 第二版產出的簡報

![20260703220930](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703220930.png)

# 🔁 重點回顧

1. 使用 `npx @open-slide/cli init my-demo-slide` 產生一份完整的簡報專案
2. 使用 `npm run dev` 啟動簡報
3. 使用 `/create-slide` 產生簡報
4. 使用 `/apply-comments` 依據簡報上的 Comment 進行修改
5. 目前 open-slide 仍在開發中，僅支援匯出成 pdf、html 以及圖片

# 🔗 參考資料

- [Open Slide GitHub](https://github.com/1weiho/open-slide)
