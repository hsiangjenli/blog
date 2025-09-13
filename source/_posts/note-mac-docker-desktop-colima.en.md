---
title: '[note] Mac not installing Docker Desktop, switching to Colima - FAQ'
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

# 📌 Introduction

On Mac, to use Docker you don't necessarily have to install the official Docker Desktop; you can use a lighter alternative like Colima. However, if you previously installed Docker Desktop and then installed the Docker CLI via Homebrew without cleaning up some old settings, you may encounter some errors.

<!-- more -->

# 🚀 Operations

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

Because Docker Desktop was initially installed then later removed and replaced with Colima, some original settings continued to be used, causing the errors.

## Solution

### `Error 1`

Installing `docker` via `brew install docker` only installs the Docker CLI, not the Docker Engine. The Docker Engine must run on a Linux-based system, and macOS is not Linux, so an extra VM is required. Docker Desktop used to create a VM in the background, so you might not have noticed. After removing Docker Desktop, you need to provide a VM for Docker to run.

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
If Docker Desktop was installed originally, some settings may be reused and cause this error.

1. Edit `config.json`
    ```shell
    nano ~/.docker/config.json
    ```
1. Remove this section inside
    ```shell
    {
      "credsStore": "desktop"
    }
    ```

# 🔁 Recap

This note summarizes two common errors:
1. Docker cannot connect to the daemon
1. Missing `docker-credential-desktop` causing credential errors

# 🔗 References
- [Day 07: Developing for Kubernetes with KinD - macOS](https://ithelp.ithome.com.tw/articles/10355740)
- [Using Colima to quickly build a Kubernetes development environment](https://blog.wu-boy.com/2023/06/how-to-create-kubernetes-cluster-in-local/)
