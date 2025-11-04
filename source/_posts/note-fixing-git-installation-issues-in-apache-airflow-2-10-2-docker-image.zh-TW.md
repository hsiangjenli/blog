---
title: '[note] 修正 apache/airflow:2.10.2 Docker 映像中 Git 安裝問題'
date: '2024-09-26'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- docker
toc: true
slug: note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image
lang: zh-TW
source_sha: 04c124bbd477d9e39cd8a1822c7760fc13c1c79f3be0e94917c89378d07bf84a
origin_lang: en
permalink: zh-TW/note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image/
translations:
  en: /note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
The article discusses the issue of permission errors when attempting to install packages from GitHub while using the apache/airflow:2.10.2 Docker image. It presents a solution that involves temporarily switching to the root user to install 'git' and then reverting to the airflow user for further installations.
<!-- more -->

# 🚀 快速開始
```dockerfile
FROM apache/airflow:slim-2.10.2

USER root
RUN apt-get update && apt-get install -y git

USER airflow
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
```

# 🔁 重點回顧
- 使用 apache/airflow:2.10.2 映像從 GitHub 安裝套件時，可能會發生權限錯誤。
- 為了解決此問題，請在切回 airflow 使用者之前，以 root 使用者身分安裝 git。
- 範例 Dockerfile 示範了執行這些操作的步驟。
