---
title: '[note] Mac — Using Colima instead of Docker Desktop: FAQ'
date: '2025-04-28'
updated: '2025-04-28'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags:
- docker
toc: true
slug: note-mac-docker-desktop-colima
lang: en
source_sha: 45ea7578fa0b317eae3876ad81bba7b7dea3ee23cac359f58b963ff2af4078c9
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

To use Docker on a Mac, you don't have to install the official Docker Desktop; you can use lighter alternatives like Colima. However, if you previously installed Docker Desktop and later installed the Docker CLI via Homebrew, leftover settings may cause some errors.

<!-- more -->

# 🚀 Steps

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

These errors occur when Docker Desktop was initially used and then removed in favor of Colima, but some original settings remained in use.

## Solution

### `Error 1`

Installing with `brew install docker` installs the Docker CLI only, not the Docker Engine. Because the Docker Engine must run on a Linux-based system and macOS isn't Linux, you need to provide a VM. Docker Desktop used to run a VM in the background, so this wasn't noticeable; after removing Docker Desktop you must provide a VM for Docker to run.

1. Install `colima`
    ```shell
    brew install colima
    ```
1. Start `colima`
    ```shell
    colima start
    ```
1. Use Docker commands normally

### `Error 2`

If Docker Desktop was previously installed, some settings may persist and cause this error.

1. Edit `config.json`
    ```shell
    nano ~/.docker/config.json
    ```
1. Remove the following section
    ```json
    {
      "credsStore": "desktop"
    }
    ```

# 🔁 Recap

This note summarizes two common errors:
1. Docker cannot connect to the daemon
1. `docker-credential-desktop` not found causing credential errors

# 🔗 References
- [Day 07：Developing for Kubernetes with KinD - MacOS](https://ithelp.ithome.com.tw/articles/10355740)
- [Using Colima to quickly build a Kubernetes development environment](https://blog.wu-boy.com/2023/06/how-to-create-kubernetes-cluster-in-local/)
