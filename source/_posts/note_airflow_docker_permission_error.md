---
title: "[note] Fixing Git Installation Issues in `apache/airflow:2.10.2` Docker Image"
date: 2024-09-26
tags: docker
toc: true
---

<!-- When I using `apache/airflow:2.10.2` Image to install the package from github will raise permission error. The solutoion is to install `git` by using root. Then switch the user back to airflow to install the package. -->

When using the apache/airflow:2.10.2 image to install packages from GitHub, a permission error may occur. The solution is to install git using the root user, then switch back to the airflow user to install the package.

```dockerfile
FROM apache/airflow:slim-2.10.2

USER root
RUN apt-get update && apt-get install -y git

USER airflow
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
```