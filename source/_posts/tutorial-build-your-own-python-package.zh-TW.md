---
title: '[tutorial] 建立你自己的 Python 套件'
date: '2024-01-15'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- python
toc: true
slug: tutorial-build-your-own-python-package
lang: zh-TW
source_sha: 325081210978c69e6bb37a726d02a95c3743b20ede58ea0cae5a4f1cfc8a696d
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
建立自己的 Python 套件有助於維護大型專案，因為它可以管理那些散落在各個目錄中的程式碼。
<!-- more -->

# 🚀 快速開始
- 建立一個 `setup.py` 檔案：
```python
from setuptools import setup, find_packages

setup(name="ntust_simslab", version="0.13", packages=find_packages())
```
- 建立一個 `pyproject.toml` 檔案：
```toml
[tool.poetry]
name = "ntust_simslab"
version = "0.13"
description = "A simple example for building a Python package."
authors = ["Hsiang-Jen Li <hsiangjenli@gmail.com>"]
readme = "README.md"
packages = [{include = "ntust_simslab"}]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
- 在 https://pypi.org/ 註冊一個 PyPI 帳號以發佈你的套件。

# 🔁 重點回顧
- 建立 Python 套件有助於在大型專案中維持程式碼的組織。
- 使用 `setup.py` 是傳統方法，而 `pyproject.toml` 則是使用 Poetry 的現代作法。
- 在 PyPI 擁有帳號是發佈套件的必要條件。

# 🔗 參考
- https://github.com/NTUST-SiMS-Lab/tutorial-simple-pypkg
- https://pypi.org/
