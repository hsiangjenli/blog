---
title: '[note] ngrok - Free Static Domains'
date: '2025-07-22'
lang: en
updated: '2025-07-22'
author:
- Hsiang-Jen Li
tags:
- ngrok
toc: true
slug: note-ngrok-static-domain-for-free
---

# 📌 Introduction

ngrok offers users free static domains!

<!-- more -->

# 🚀 Quick Start

## Install ngrok

```shell
sudo snap install ngrok
```

## Create a domain

> Log in to [ngrok](https://dashboard.ngrok.com/login) and create your personal domain (random)

![Image](https://hackmd.io/_uploads/BJj8LzTLge.png)

## Set up Token

![Image](https://hackmd.io/_uploads/BklCszTUlx.png)

```shell
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

## Create a tunnel

```shell
ngrok http --url=$URL $PORT
```

# 🔗 References

- [Free static domains for all ngrok users](https://ngrok.com/blog-post/free-static-domains-ngrok-users)
