---
title: '[note] Running Ubuntu VM on Mac with Multipass'
date: '2023-10-23'
lang: en
updated: '2025-05-14'
author:
- Hsiang-Jen Li
tags: null
toc: true
slug: note-run-ubuntu-vms-on-your-mac-using-multipass
---

# 📌 Introduction

Multipass is a simple tool provided by Canonical for easily running Ubuntu virtual machines.

<!-- more -->

# 🚀 Quick Start

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

## Install Desktop Environment
```
sudo apt install ubuntu-desktop xrdp
```

# 🔁 Recap

- Learn how to quickly launch and manage Ubuntu VMs on macOS using Multipass
- Understand how to allocate resources and access the VM via shell

# 🔗 References
- [canonical/multipass](https://github.com/canonical/multipass)
- [Multipass — 如 Docker 般的虛擬機](https://jackkuo-tw.medium.com/multipass-%E5%A6%82-docker-%E8%88%AC%E7%9A%84%E8%99%9B%E6%93%AC%E6%A9%9F-e19e3e36aec3)
- [在 M1 或 M2 Mac 上使用 MULTI PASS 安裝並執行帶 GUI 的 Ubuntu](https://www.youtube.com/watch?v=oi8f6hVI2P4)
- [久違的在 Mac M2 上使用 Ubuntu](https://vocus.cc/article/63d11eddfd89780001f3daf4)
