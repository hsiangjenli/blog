---
title: '[note] Install Golang (PATH)'
date: '2024-08-27'
lang: en
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- go
toc: true
translation_key: note-installation-of-golang-path
slug: note-installation-of-golang-path
source_sha: 4ac8890ddd25d5c5224bb7163e3a4e3864189786b96ed4fc8b80fb6590917648
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by an AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 Introduction
> This article provides a step-by-step guide to installing Go on macOS and configuring the system PATH variable to include Go executables.
<!-- more -->

# 🚀 Quick Start
1. **Install Go using Homebrew:**
   ```shell
   brew install go
   ```

2. **Verify the installation:**
   ```shell
   ls ~/go/bin/
   ```

3. **Temporarily update PATH:**
   ```shell
   export PATH=$PATH:~/go/bin
   ```

4. **Permanently update PATH:**
   ```shell
   echo 'export PATH=$PATH:~/go/bin' >> ~/.zshrc
   source ~/.zshrc
   ```

# 🔁 Recap
- This guide explains how to install the Go programming language on macOS.
- Includes verification steps to check if the installation succeeded.
- Provides instructions for temporarily and permanently updating the PATH environment variable.
