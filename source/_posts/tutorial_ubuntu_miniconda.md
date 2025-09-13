---
title: '[Tutorial] Installing Miniconda on Ubuntu'
date: '2023-02-13'
lang: en
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
source_sha: 6699c747e01ec6fdb2a928b32c2f1ed598e88ac5011638b75027d9a567244a22
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 Introduction
This article details the steps required to install Miniconda on Ubuntu, including downloading the installer and setting up the initial environment.
<!-- more -->

# 🚀 Quick Start
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

# 🔁 Recap
- Miniconda is a minimal installer for conda, suitable for managing Python environments and packages.
- The installation process includes downloading the installer, making it executable, and running it to set up Miniconda.
- After installation, you can easily create and manage Python environments using conda commands.

# 🔗 References
- https://medium.com/featurepreneur/setting-up-miniconda-on-ubuntu-4bf6bece6f9b
