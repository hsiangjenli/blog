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
slug: note-installation-of-golang-path
---

# 📌 Introduction

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
