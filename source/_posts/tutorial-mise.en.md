---
title: '[tutorial] Using mise to manage multiple programming language environments'
date: '2026-03-29'
updated: '2026-04-27'
author:
- Hsiang-Jen Li
tags:
- devops
toc: true
lang: en
slug: tutorial-mise
source_sha: 73b5d81c261a6932c0db07c8bb311e92c22fa4ffc1242747b6a55fff3eda43a0
origin_lang: zh-TW
permalink: tutorial-mise.en/
translations:
  zh-TW: /zh-TW/tutorial-mise/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 🚀 Installing mise

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

- The installation path for Rust is different from the others; even when installed via mise, it is installed under `.cargo`

## Bun

```shell
mise latest bun # search for the latest version
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

# 🔗 References

- [mise- java](https://mise.jdx.dev/lang/java.html)
