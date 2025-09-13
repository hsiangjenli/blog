---
title: '[教學] 在 Ubuntu 上設定 Miniconda'
date: '2023-02-13'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- ubuntu
- python
toc: true
translation_key: tutorial-setting-up-miniconda-on-ubuntu
slug: tutorial-setting-up-miniconda-on-ubuntu
source_sha: a5ff16c87656c99fc6dda7dda8e5b38ed6101997e1daeeecffed6541516fb9ee
origin_lang: en
---

# 📌 介紹
本文詳述在 Ubuntu 上安裝 Miniconda 所需的步驟，包括下載安裝程式並設定初始環境。
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

# 🔁 總結
- Miniconda 是 conda 的精簡安裝程式，方便管理 Python 的環境與套件。
- 安裝過程包含下載安裝程式、賦予執行權限，並執行它以設定 Miniconda。
- 安裝完成後，可使用 conda 指令輕鬆建立與管理 Python 環境。

# 🔗 參考資料
- https://medium.com/featurepreneur/setting-up-miniconda-on-ubuntu-4bf6bece6f9b
