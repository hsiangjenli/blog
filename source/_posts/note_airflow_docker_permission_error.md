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
slug: note-fixing-git-installation-issues-in-apache-airflow-2-10-2-docker-image
---

# 📌 Introduction

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
