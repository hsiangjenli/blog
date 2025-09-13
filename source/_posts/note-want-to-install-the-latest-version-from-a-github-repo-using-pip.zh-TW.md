---
title: '[注意] 想要使用 pip 從 GitHub 倉庫安裝最新版本'
date: '2024-12-18'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- python
- git
- pip
toc: true
translation_key: note-want-to-install-the-latest-version-from-a-github-repo-using-pip
slug: note-want-to-install-the-latest-version-from-a-github-repo-using-pip
source_sha: a3da3844eeb21038c7894882c100679346cc65d47883df69c011296cbaedfe7e
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> # 📌 介紹
本文說明如何使用 pip 安裝 GitHub 倉庫的特定分支，特別著重於通常用於開發而非穩定發行的 'devel' 分支。
<!-- more -->

# 🚀 快速開始
要使用 pip 從 GitHub 安裝開發版本，執行下列命令：

```bash
pip install git+https://github.com/username/repository.git@devel
```

# 🔁 總結
- 可以使用 pip 從 GitHub 安裝特定分支。
- 'devel' 分支通常包含不穩定的開發版本。
- 要安裝，使用命令格式：`pip install git+{repo_url}@{branch_name}`。
- 將 `{repo_url}` 替換為你的倉庫 URL，將 `{branch_name}` 替換為 'devel'。
- 確保已安裝 pip 以使用此命令。
