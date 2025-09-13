---
title: '[note] Mac: Don''t install Docker Desktop, switch to Colima — FAQ'
date: '2025-04-28'
lang: en
updated: '2025-04-28'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags:
- docker
toc: true
translation_key: note-mac-docker-desktop-colima
slug: note-mac-docker-desktop-colima
source_sha: 45ea7578fa0b317eae3876ad81bba7b7dea3ee23cac359f58b963ff2af4078c9
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> # 📌 Introduction

On Mac, you don't have to install the official Docker Desktop to use Docker; you can use lighter alternatives like Colima. However, if you previously installed Docker Desktop and later installed the Docker CLI via Homebrew without fully cleaning old settings, you may encounter some errors.

<!-- more -->

# 🚀 Actions

## Error messages

```shell
# Error 1
docker: Cannot connect to the Docker daemon at unix:///Users/XXXXXXXX/.docker/run/docker.sock. Is the docker daemon running?
```

```shell
# Error 2
docker: error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH, out: ``
```

## Cause

Because Docker Desktop was initially used for installation, and then removed in favor of Colima, some original settings continued to be used, causing these errors.

## Solution

### `Error 1`

Installing with `brew install docker` installs the Docker CLI, not the Docker Engine. The Docker Engine must run on a Linux-based system, and macOS is not Linux, so an additional VM is required. Docker Desktop used to start a VM in the background, so you might not have noticed; after removing Docker Desktop, you need to provide a VM for Docker to run.

1. Install `colima`
    ```shell
    brew install colima
    ```
1. Start `colima`
    ```shell
    colima start
    ```
1. Use Docker commands as usual

### `Error 2`
If Docker Desktop was installed initially, some settings may have been reused, causing this error.

1. Edit `config.json`
    ```shell
    nano ~/.docker/config.json
    ```
1. Remove this section
    ```shell
    {
      "credsStore": "desktop"
    }
    ```

# 🔁 Recap

This note summarizes two common errors:
1. Docker cannot connect to the daemon
1. Missing docker-credential-desktop causing credential errors

# 🔗 References
- [Day 07：Developing for Kubernetes with KinD - MacOS](https://ithelp.ithome.com.tw/articles/10355740)
- [使用 Colima 快速打造 Kubernetes 開發環境](https://blog.wu-boy.com/2023/06/how-to-create-kubernetes-cluster-in-local/)
