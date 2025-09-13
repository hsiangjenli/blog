---
title: '[注意] 修復 apache/airflow:2.10.2 Docker 映像中 Git 安裝問題'
date: '2024-09-26'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- docker
toc: true
translation_key: note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image
slug: note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image
source_sha: 04c124bbd477d9e39cd8a1822c7760fc13c1c79f3be0e94917c89378d07bf84a
origin_lang: en
---

# 📌 簡介
本文討論在使用 apache/airflow:2.10.2 Docker 映像時，從 GitHub 安裝套件會遇到權限錯誤的問題。提出的解決方案是暫時切換到 root 使用者安裝 'git'，然後再切回 airflow 使用者繼續安裝。
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
- 要解決此問題，請先以 root 使用者安裝 git，然後再切回 airflow 使用者。
- 提供的 Dockerfile 示範了執行這些步驟。
