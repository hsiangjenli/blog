---
title: '[tutorial] Managing Multi-Language Environments with mise'
date: '2026-03-29'
updated: '2026-10-24'
author:
- Hsiang-Jen Li
tags:
- devops
toc: true
lang: en
slug: tutorial-mise
source_sha: db1ebd8d079c27eae1ae8bc7e4f211e2cef23e5dd56203b3852c98b6459dcd9f
origin_lang: zh-TW
permalink: tutorial-mise.en/
translations:
  zh-TW: /zh-TW/tutorial-mise/
---

> Note: This page is an AI-generated (openai/gpt-6-luna) translation from Traditional Chinese and may contain minor inaccuracies.

# 🚀 Installing mise in Practice

```shell
curl https://mise.run | sh
```

```shell
mise --version
```

<!-- more -->

![image](https://hackmd.io/_uploads/SyLek5IoZg.png)

## Update mise

```shell
mise self-update
```

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

## Java Spring Boot CLI (Spring Initializr)

```shell
mise registry spring-boot

>>> vfox:jdx/vfox-spring-boot asdf:mise-plugins/mise-spring-boot

mise use -g vfox:jdx/vfox-spring-boot@latest

>>> plugin:vfox-jdx-vfox-spring-boot clone https://github.com/jdx/vfox-spring-boot
>>> mise ~/.config/mise/config.toml tools: vfox:jdx/vfox-spring-boot@4.2.0-M2
```

```shell
# See which Project Types or Dependencies are supported
spring init --list
```

```shell
spring init --extract --build=maven --java-version=25 demo-spring-project
```

## Java Maven

```shell
mise use -g aqua:apache/maven@latest
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

- Rust has a different installation path from the others; even when installed through mise, it is installed under `.cargo`.

## Bun

```shell
mise latest bun # Search for the latest version
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
