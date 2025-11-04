---
title: '[備註] Gatsby 用法'
date: '2022-09-02'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- static-site
- gatsby
toc: false
slug: note-gatsby-usage
lang: zh-TW
source_sha: 64e4d8c57e0f1fb316670e085c653d27f5c7a6c41cac8c5f798761b3f368fbb4
origin_lang: en
permalink: zh-TW/note-gatsby-usage/
translations:
  en: /note-gatsby-usage.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
本文提供如何安裝 Gatsby 並使用啟始佈景主題（starter themes）建立新的 Gatsby 網站的指南。內容涵蓋安裝步驟、建立 Gatsby 網站的指令，以及用於排解常見錯誤的相關連結。
<!-- more -->

# 🚀 快速開始
## 安裝 Gatsby
```shell=
npm install -g gatsby-cli
gatsby --version
```

![](https://i.imgur.com/GqF5btJ.png)

## gatsby-starter-blog
```shell=
gatsby new hjl https://github.com/gatsbyjs/gatsby-starter-blog
cd hjl
gatsby develop
```

## gatsby-starter-julia
```shell
gatsby new RN https://github.com/niklasmtj/gatsby-starter-julia
cd rn
```

## 使用舊版 peer 依賴
```shell
--legacy-peer-deps
```

# 🔁 重點回顧
- 使用 npm 安裝 Gatsby CLI 非常簡單，指令為 `npm install -g gatsby-cli`。
- 安裝完成後，可檢查已安裝的 Gatsby 版本。
- 要建立新的 Gatsby 網站，可使用多個 starter 主題，例如 `gatsby-starter-blog` 與 `gatsby-starter-julia`。
- 與 npm 與 Gatsby 相關的常見錯誤已透過本文提供的各個連結詳盡記錄。

# 🔗 參考資料
- [指令（Gatsby CLI）](https://www.gatsbyjs.com/docs/reference/gatsby-cli/)
- [npm WARN old lockfile The package-lock.json file was created with an old version of npm](https://stackoverflow.com/questions/68260784/npm-warn-old-lockfile-the-package-lock-json-file-was-created-with-an-old-version)
- [錯誤：Command failed with exit code 1: npm install #27548](https://github.com/gatsbyjs/gatsby/issues/27548)
- [npm-upgrade](https://www.npmjs.com/package/npm-upgrade)
