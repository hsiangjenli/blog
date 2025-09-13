---
title: '[note] 想使用 pip 從 GitHub 倉庫安裝最新版本'
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

# 📌 介紹
本文說明如何使用 pip 安裝 GitHub 倉庫的特定分支，特別著重於 'devel' 分支——通常用於開發用途，而非穩定釋出。
<!-- more -->

# 🚀 快速開始
要使用 pip 從 GitHub 安裝開發版本，請執行以下指令：

```bash
pip install git+https://github.com/username/repository.git@devel
```

# 🔁 重點回顧
- 你可以使用 pip 從 GitHub 安裝指定的分支。
- 'devel' 分支通常包含不穩定的開發版本。
- 要安裝，使用指令格式：`pip install git+{repo_url}@{branch_name}`。
- 將 `{repo_url}` 替換為你的倉庫 URL，將 `{branch_name}` 替換為 'devel'。
- 確保你的系統已安裝 pip 才能使用此指令。
