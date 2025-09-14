---
title: '[note] Mac 不裝 Docker Desktop，改用 Colima 常見問題整理'
date: '2025-04-28'
updated: '2025-04-28'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags:
- docker
toc: true
slug: note-mac-docker-desktop-colima
lang: zh-TW
source_sha: 45ea7578fa0b317eae3876ad81bba7b7dea3ee23cac359f58b963ff2af4078c9
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹

在 Mac 上要用 Docker，不一定要裝官方的 Docker Desktop，也可以改用像 Colima 這種比較輕量的選擇。不過，如果之前有裝過 Docker Desktop，後來又直接用 Homebrew 裝 Docker CLI，可能會因為一些舊設定沒清乾淨，遇到一些錯誤。

<!-- more -->

# 🚀 操作

## 錯誤訊息

```shell
# 錯誤 1
docker: Cannot connect to the Docker daemon at unix:///Users/XXXXXXXX/.docker/run/docker.sock. Is the docker daemon running?
```

```shell
# 錯誤 2
docker: error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH, out: ``
```

## 原因

因為剛開始使用 Docker Desktop 安裝，而後又將其刪除，改用 Colima，然原先的設定繼續沿用，故造成錯誤。

## 解法

### `錯誤 1`

直接使用 `brew install docker` 安裝的是 Docker 的 CLI，而非 Docker Engine。因為 Docker Engine 必須跑在 Linux-based 的系統上，但是 mac 並非使用 Linux，所以需要額外開 VM。過去 Docker Desktop 會在背後開 VM，所以沒注意到，這次將 Docker Desktop 移除就需要額外準備 VM 給 Docker 運作。

1. 安裝 `colima`
    ```shell
    brew install colima
    ```
1. 執行 `colima`
    ```shell
    colima start
    ```
1. 正常操作 Docker 指令

### `錯誤 2`
若一開始先安裝 Docker Desktop 有些設定會沿用，進而導致錯誤發生。

1. 至 `config.json` 中修改
    ```shell
    nano ~/.docker/config.json
    ```
1. 把裡面的這段刪除
    ```shell
    {
      "credsStore": "desktop"
    }
    ```

# 🔁 Recap

這篇筆記整理了兩個常見錯誤：
1. Docker 無法連線到 daemon
1. 找不到 docker-credential-desktop 導致憑證錯誤

# 🔗 參考資料
- [Day 07：Developing for Kubernetes with KinD - MacOS](https://ithelp.ithome.com.tw/articles/10355740)
- [使用 Colima 快速打造 Kubernetes 開發環境](https://blog.wu-boy.com/2023/06/how-to-create-kubernetes-cluster-in-local/)
