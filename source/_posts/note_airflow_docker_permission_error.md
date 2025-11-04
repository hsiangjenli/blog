---
title: '[note] Fixing Git Installation Issues in apache/airflow:2.10.2 Docker Image'
date: '2024-09-26'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- docker
toc: true
slug: note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image
lang: en
permalink: note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image.en/
translations:
  zh-TW: /zh-TW/note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image/
---

# 📌 Introduction
The article discusses the issue of permission errors when attempting to install packages from GitHub while using the apache/airflow:2.10.2 Docker image. It presents a solution that involves temporarily switching to the root user to install 'git' and then reverting to the airflow user for further installations.
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
- Permission errors can occur with the apache/airflow:2.10.2 image when installing packages from GitHub.
- To resolve this issue, install git as the root user before switching back to the airflow user.
- The Dockerfile provided demonstrates the steps to perform these actions.
