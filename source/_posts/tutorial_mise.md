---
title: '[tutorial] 使用 mise 管理多程式語言環境'
date: '2026-03-29'
updated: '2026-10-24'
author:
- Hsiang-Jen Li
tags:
- devops
toc: true
lang: zh-TW
slug: tutorial-mise
permalink: zh-TW/tutorial-mise/
translations:
  en: /tutorial-mise.en/
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

## 更新 mise

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
# 查看支援哪些 Project Type 或是 Dependencies
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
