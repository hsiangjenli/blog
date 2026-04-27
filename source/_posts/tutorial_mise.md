---
title: '[tutorial] 使用 mise 管理多程式語言環境'
date: '2026-03-29'
updated: '2026-04-27'
author:
- 'Hsiang-Jen Li'
tags:
- devops
toc: true
lang: zh-TW
---

# 🚀 實際安裝 mise

```shell
curl https://mise.run | sh
```

```shell
mise --version
```

<!-- more -->


![image](https://hackmd.io/_uploads/SyLek5IoZg.png)


## Java

```shell
mise use -g java@openjdk-21
source ~/.bashrc 

java --version

>>> openjdk 21.0.2 2024-01-16
>>> OpenJDK Runtime Environment (build 21.0.2+13-58)
>>> OpenJDK 64-Bit Server VM (build 21.0.2+13-58, mixed mode, sharing)

which java
>>> /home/xxx/.local/share/mise/installs/java/openjdk-21.0.2/bin/java
```

## Rust

```shell
mise use -g rust@latest
source ~/.bashrc 

which rustc
>>> /home/xxx/.cargo/bin/rustc

which cargo
>>> /home/xxx/.cargo/bin/cargo
```

- Rust 的安裝路徑跟其它的不同，即使是透過 mise 也是安裝在 `.cargo` 底下

## Bun

```shell
mise latest bun # 搜尋最新的版本
mise use -g bun@1.3.13
source ~/.bashrc 

bun --version
>>> 1.3.13
which bun
>>> /home/xxx/.local/share/mise/installs/bun/1.3.13/bin/bun
```

## Node

```shell
mise use -g node@22
source ~/.bashrc 

which npm
>>> /home/xxx/.local/share/mise/installs/node/22.22.2/bin/npm
which node
>>> /home/xxx/.local/share/mise/installs/node/22.22.2/bin/node
```

# 🔗 參考資料

- [mise- java](https://mise.jdx.dev/lang/java.html)
