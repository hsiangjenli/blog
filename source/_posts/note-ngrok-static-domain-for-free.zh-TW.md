---
title: '[note] ngrok - 免費靜態網域'
date: '2025-07-22'
updated: '2025-07-22'
author:
- Hsiang-Jen Li
tags:
- ngrok
toc: true
slug: note-ngrok-static-domain-for-free
lang: zh-TW
source_sha: e6e099a928463dd6a030d1b9a556f125c7865d623bd5683db6b460351a5e12b5
origin_lang: en
permalink: zh-TW/note-ngrok-static-domain-for-free/
translations:
  en: /note-ngrok-static-domain-for-free.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 簡介

ngrok 為使用者提供免費的靜態網域！

<!-- more -->

# 🚀 快速開始

## 安裝 ngrok

```shell
sudo snap install ngrok
```

## 建立網域

> 登入 [ngrok](https://dashboard.ngrok.com/login) 並建立你的個人網域（隨機）

![圖片](https://hackmd.io/_uploads/BJj8LzTLge.png)

## 設定 Token

![圖片](https://hackmd.io/_uploads/BklCszTUlx.png)


```shell
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

## 建立隧道

```shell
ngrok http --url=$URL $PORT
```

# 🔗 參考資料

- [適用於所有 ngrok 使用者的靜態網域](https://ngrok.com/blog-post/free-static-domains-ngrok-users)
