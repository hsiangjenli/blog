---
title: '[note] 在 Mac 上使用 Multipass 執行 Ubuntu VM'
date: '2023-10-23'
lang: zh-TW
updated: '2025-05-14'
author:
- Hsiang-Jen Li
tags: null
toc: true
translation_key: note-run-ubuntu-vms-on-your-mac-using-multipass
slug: note-run-ubuntu-vms-on-your-mac-using-multipass
source_sha: 55f33c5d185f25f426762cbb0063396d7172b23dd14f834fc5a1124ccf492788
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> # 📌 介紹

Multipass 是 Canonical 提供的一個簡單工具，用於輕鬆執行 Ubuntu 虛擬機。

<!-- more -->

# 🚀 快速開始

```
brew install qemu
```

```
multipass launch 20.04 -c 8 -m 8G -d 100G
multipass list
multipass shell your_vname
```

```
sudo apt update
sudo apt install neofetch
```

```
neofetch
```

![](https://hackmd.io/_uploads/S1Djr7RM6.png)

## 安裝桌面環境
```
sudo apt install ubuntu-desktop xrdp
```

# 🔁 回顧

- 學會如何在 macOS 上使用 Multipass 快速啟動與管理 Ubuntu 虛擬機
- 了解如何分配資源並透過 shell 存取虛擬機

# 🔗 參考資料
- [canonical/multipass](https://github.com/canonical/multipass)
- [Multipass — 如 Docker 般的虛擬機](https://jackkuo-tw.medium.com/multipass-%E5%A6%82-docker-%E8%88%AC%E7%9A%84%E8%99%9B%E6%93%AC%E6%A9%9F-e19e3e36aec3)
- [在 M1 或 M2 Mac 上使用 MULTI PASS 安裝並執行帶 GUI 的 Ubuntu](https://www.youtube.com/watch?v=oi8f6hVI2P4)
- [久違的在 Mac M2 上使用 Ubuntu](https://vocus.cc/article/63d11eddfd89780001f3daf4)
