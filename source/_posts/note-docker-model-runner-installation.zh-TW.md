---
title: '[注意] Docker Model Runner 安裝'
date: '2025-07-25'
lang: zh-TW
updated: '2025-08-19'
author:
- ChatGPT-5
- ' & Hsiang-Jen Li'
tags:
- llm
- docker
toc: true
translation_key: note-docker-model-runner-installation
slug: note-docker-model-runner-installation
source_sha: 4baaff6e38f03d3da69fc6face5bf553fb13934c5597744ae76aa21a6a80b4d2
origin_lang: en
---

# 📌 介紹

在 Ubuntu 24.04 上安裝 Docker Model Plugin 時，我遇到 apt 找不到該套件的問題。結果發現 Docker 的套件庫指向了錯誤的發行版本（指向 focal 而非 noble）。

> **⭐ 注意** 
> 這篇文章最初是由 ChatGPT 協助草擬，基於我實際遇到的問題。我已驗證解決方法並修訂內容，以確保其他遇到類似問題的人能夠準確且清楚地參考。

<!-- more -->

# 🚀 快速開始

```shell
sudo apt-get update
sudo apt-get install docker-model-plugin -y

Hit:1 http://tw.archive.ubuntu.com/ubuntu noble InRelease                                 
Hit:2 http://tw.archive.ubuntu.com/ubuntu noble-updates InRelease                         
Hit:3 http://tw.archive.ubuntu.com/ubuntu noble-backports InRelease                       
Hit:4 https://packages.microsoft.com/repos/edge stable InRelease                          
Hit:5 https://brave-browser-apt-release.s3.brave.com stable InRelease                     
Hit:6 https://packages.microsoft.com/repos/code stable InRelease                          
Hit:7 http://security.ubuntu.com/ubuntu noble-security InRelease                          
Get:8 https://download.docker.com/linux/ubuntu focal InRelease [57.7 kB]                  
Hit:9 https://ppa.launchpadcontent.net/mozillateam/ppa/ubuntu jammy InRelease             
Fetched 57.7 kB in 7s (8650 B/s)
Reading package lists... Done
N: Skipping acquire of configured file 'main/binary-i386/Packages' as repository 'https://brave-browser-apt-release.s3.brave.com stable InRelease' doesn't support architecture 'i386'
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package docker-model-plugin
```

當我按照 [How to Run Docker Model Runner on Ubuntu 24.04](https://mrcloudbook.com/how-to-run-docker-model-runner-on-ubuntu-24-04/) 的教學時，我發現 apt install 找不到 docker-model-plugin。解決方法是

```shell
sudo apt-get update
sudo apt-get install \
  ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) \
    signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

# 🔁 回顧

- 錯誤發生的原因是 Docker APT 套件庫指向了錯誤的發行版本（focal 而非 noble）
- 修正此問題需要新增正確的 Docker GPG 金鑰並為 Ubuntu 24.04 設定正確的套件庫
- 更新 APT 來源後，docker-model-plugin 套件即可安裝

# 🔗 參考資料

- [How to Run Docker Model Runner on Ubuntu 24.04](https://mrcloudbook.com/how-to-run-docker-model-runner-on-ubuntu-24-04/)
