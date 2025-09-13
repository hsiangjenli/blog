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
translation_key: note-ngrok-static-domain-for-free
slug: note-ngrok-static-domain-for-free
source_sha: 51b05bd4ae9294707a546d0a9907855893020f641012f3eee6b29b3977f6010d
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 Introduction

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
