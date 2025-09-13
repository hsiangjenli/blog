---
title: '[note] Fix Git installation issue in apache/airflow:2.10.2 Docker image'
date: '2024-09-26'
lang: en
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- docker
toc: true
translation_key: note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image
slug: note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image
source_sha: 3fcf9ea5c47f6fc08d4f895b6c471200c3974376d1787bc93b5ef10eff85e637
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 Introduction
> This article discusses an issue where attempting to install packages from GitHub using the apache/airflow:2.10.2 Docker image encounters permission errors. The proposed solution is to temporarily switch to the root user to install 'git', then switch back to the airflow user for subsequent installations.
<!-- more -->

# 🚀 Quick Start
```dockerfile
FROM apache/airflow:slim-2.10.2

USER root
RUN apt-get update && apt-get install -y git

USER airflow
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
```

# 🔁 Recap
- Permission errors may occur when installing packages from GitHub using the apache/airflow:2.10.2 image.
- To resolve this, install git as root before switching back to the airflow user.
- The provided Dockerfile demonstrates how to perform these steps.
