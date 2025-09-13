---
title: '[note] ngrok - static domain for free'
date: '2025-07-22'
lang: en
updated: '2025-07-22'
author:
- Hsiang-Jen Li
tags:
- ngrok
toc: true
translation_key: note-ngrok-static-domain-for-free
slug: note-ngrok-static-domain-for-free
---

# 📌 Introduction

ngrok provides users with free static domains!

<!-- more -->

# 🚀 Quick Start

## Install ngrok

```shell
sudo snap install ngrok
```

## Create Domain

> Login to [ngrok](https://dashboard.ngrok.com/login) and create your personal domain (random)

![image](https://hackmd.io/_uploads/BJj8LzTLge.png)

## Setup Token

![image](https://hackmd.io/_uploads/BklCszTUlx.png)


```shell
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

## Create Tunnel

```shell
ngrok http --url=$URL $PORT
```

# 🔗 References

- [Static domains for all ngrok users](https://ngrok.com/blog-post/free-static-domains-ngrok-users)
