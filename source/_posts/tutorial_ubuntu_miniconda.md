---
title: '[tutorial] Setting up Miniconda on Ubuntu'
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
lang: en
permalink: tutorial-setting-up-miniconda-on-ubuntu.en/
translations:
  zh-TW: /zh-TW/tutorial-setting-up-miniconda-on-ubuntu/
---

# 📌 Introduction
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
- Miniconda is a minimal installer for conda, useful for managing environments and packages in Python.
- The installation process includes downloading the installer, making it executable, and running it to set up Miniconda.
- After installation, you can easily create and manage Python environments using conda commands.

# 🔗 References
- https://medium.com/featurepreneur/setting-up-miniconda-on-ubuntu-4bf6bece6f9b
