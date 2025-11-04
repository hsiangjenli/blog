---
title: '[教學] 在 Ubuntu 上設定 Miniconda'
date: '2023-02-13'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- ubuntu
- python
toc: true
slug: tutorial-setting-up-miniconda-on-ubuntu
lang: zh-TW
source_sha: a5ff16c87656c99fc6dda7dda8e5b38ed6101997e1daeeecffed6541516fb9ee
origin_lang: en
permalink: zh-TW/tutorial-setting-up-miniconda-on-ubuntu/
translations:
  en: /tutorial-setting-up-miniconda-on-ubuntu.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
本文詳細說明在 Ubuntu 上安裝 Miniconda 所需的步驟，包含下載安裝程式並建立初始環境。
<!-- more -->

# 🚀 快速開始
```shell!
sudo wget -c https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

```shell!
sudo chmod +x Miniconda3-latest-Linux-x86_64.sh
```

```shell!
./Miniconda3-latest-Linux-x86_64.sh
```

```shell
conda activate
conda env list
```

# 🔁 回顧
- Miniconda 是 conda 的精簡安裝程式，適合用來管理 Python 的環境與套件。
- 安裝過程包括下載安裝程式、將其設為可執行，並執行以設定 Miniconda。
- 安裝完成後，你可以使用 conda 指令輕鬆建立與管理 Python 環境。

# 🔗 參考資料
- https://medium.com/featurepreneur/setting-up-miniconda-on-ubuntu-4bf6bece6f9b
