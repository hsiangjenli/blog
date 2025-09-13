---
title: '[note] Gatsby 用法'
date: '2022-09-02'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- static-site
- gatsby
toc: false
translation_key: note-gatsby-usage
slug: note-gatsby-usage
source_sha: 64e4d8c57e0f1fb316670e085c653d27f5c7a6c41cac8c5f798761b3f368fbb4
origin_lang: en
---

# 📌 介紹
本文提供如何安裝 Gatsby、以及使用 starter 主題建立新的 Gatsby 站點的指南。涵蓋安裝步驟、設定 Gatsby 站點的指令，以及排除常見錯誤的連結。
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
- 透過 npm 安裝 Gatsby CLI 很簡單，使用指令 `npm install -g gatsby-cli`。
- 安裝後可以檢查已安裝的 Gatsby 版本。
- 要建立新的 Gatsby 站點，可以使用多種 starter 主題，例如 `gatsby-starter-blog` 與 `gatsby-starter-julia`。
- 文章提供的各種連結中有詳細紀錄與 npm 和 Gatsby 相關的常見錯誤。

# 🔗 參考資料
- [指令（Gatsby CLI）](https://www.gatsbyjs.com/docs/reference/gatsby-cli/)
- [npm WARN old lockfile The package-lock.json file was created with an old version of npm](https://stackoverflow.com/questions/68260784/npm-warn-old-lockfile-the-package-lock-json-file-was-created-with-an-old-version)
- [錯誤：Command failed with exit code 1: npm install #27548](https://github.com/gatsbyjs/gatsby/issues/27548)
- [npm-upgrade](https://www.npmjs.com/package/npm-upgrade)
