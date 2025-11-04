---
title: '[note] Run Ubuntu VMs on Your Mac Using Multipass'
date: '2023-10-23'
updated: '2025-05-14'
author:
- Hsiang-Jen Li
tags: null
toc: true
slug: note-run-ubuntu-vms-on-your-mac-using-multipass
lang: en
permalink: note-run-ubuntu-vms-on-your-mac-using-multipass.en/
translations:
  zh-TW: /zh-TW/note-run-ubuntu-vms-on-your-mac-using-multipass/
---

# 📌 Introduction

Multipass is a simple tool by Canonical for running Ubuntu VMs easily. 

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

## Download Desktop
```
sudo apt install ubuntu-desktop xrdp
```

# 🔁 Recap

- Learned how to quickly launch and manage Ubuntu VMs using Multipass on macOS
- Understood how to allocate resources and access the VM via shell

# 🔗 References
- [canonical/multipass](https://github.com/canonical/multipass)
- [Multipass — 如 Docker 般的虛擬機](https://jackkuo-tw.medium.com/multipass-%E5%A6%82-docker-%E8%88%AC%E7%9A%84%E8%99%9B%E6%93%AC%E6%A9%9F-e19e3e36aec3)
- [How To Install & RUN Ubuntu W/ GUI On M1 or M2 Mac Using MULTI PASS](https://www.youtube.com/watch?v=oi8f6hVI2P4)
- [久違的在 Mac M2 上使用 Ubuntu](https://vocus.cc/article/63d11eddfd89780001f3daf4)
