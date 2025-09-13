---
title: '[note] Mac：不要安裝 Docker Desktop，改用 Colima — 常見問答'
date: '2025-04-28'
lang: zh-TW
updated: '2025-04-28'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags:
- docker
toc: true
translation_key: note-mac-docker-desktop-colima
slug: note-mac-docker-desktop-colima
source_sha: 1a33a82bafd194034fc1478b0dc0a86adf29f60116ed879444569151a0c56e76
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> > 注意：本頁面為由 AI 生成的翻譯（gpt-5-mini-2025-08-07），自繁體中文翻譯而來，可能包含些許不準確之處。
> 
> # 📌 介紹

在 Mac 上，使用 Docker 並不必安裝官方的 Docker Desktop；可以使用像 Colima 這種更輕量的替代方案。不過，如果你先前安裝過 Docker Desktop，之後又透過 Homebrew 安裝 Docker CLI，卻沒有完全清除舊的設定，就可能會遇到一些錯誤。

<!-- more -->

# 🚀 操作

## 錯誤訊息

```shell
# Error 1
docker: Cannot connect to the Docker daemon at unix:///Users/XXXXXXXX/.docker/run/docker.sock. Is the docker daemon running?
```

```shell
# Error 2
docker: error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH, out: ``
```

## 原因

因為最初使用 Docker Desktop 進行安裝，之後改用 Colima 並移除 Docker Desktop，導致部分原有的設定仍被使用，進而引發這些錯誤。

## 解決方法

### `Error 1`

以 `brew install docker` 安裝的是 Docker CLI，而不是 Docker Engine。Docker Engine 必須在 Linux 系統上執行，而 macOS 並非 Linux，因此需要額外的 VM。Docker Desktop 會在背景啟動一個 VM，可能讓你沒有注意到；移除 Docker Desktop 後，就需要自行提供一個 VM 讓 Docker 運行。

1. 安裝 `colima`
    ```shell
    brew install colima
    ```
1. 啟動 `colima`
    ```shell
    colima start
    ```
1. 照常使用 Docker 指令

### `Error 2`
如果最初安裝過 Docker Desktop，有些設定可能被重複使用，導致出現此錯誤。

1. 編輯 `config.json`
    ```shell
    nano ~/.docker/config.json
    ```
1. 移除此段設定
    ```shell
    {
      "credsStore": "desktop"
    }
    ```

# 🔁 重點回顧

本篇摘要兩個常見錯誤：
1. Docker 無法連接到 daemon
1. 缺少 docker-credential-desktop，導致認證錯誤

# 🔗 參考資料
- [第 07 天：使用 KinD 為 Kubernetes 開發 - MacOS](https://ithelp.ithome.com.tw/articles/10355740)
- [使用 Colima 快速打造 Kubernetes 開發環境](https://blog.wu-boy.com/2023/06/how-to-create-kubernetes-cluster-in-local/)
