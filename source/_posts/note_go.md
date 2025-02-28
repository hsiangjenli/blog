---
title: '[note] Installation of Golang (PATH)'
date: '2024-08-27'
updated: '2025-02-28 (Refactored by ChatGPT-4o Mini)'
author:
  - 'Hsiang-Jen Li'
  - ' & ChatGPT-4o Mini'
tags:
- go
toc: true
---

# 📌 Introduction
This article provides a step-by-step guide on how to install Go on macOS and configure the system's PATH variable to include Go binaries.
<!-- more -->

# 🚀 Quick Start
1. **Install Go using Homebrew:**
   ```shell
   brew install go
   ```

2. **Verify the Installation:**
   ```shell
   ls ~/go/bin/
   ```

3. **Update PATH Temporarily:**
   ```shell
   export PATH=$PATH:~/go/bin
   ```

4. **Update PATH Permanently:**
   ```shell
   echo 'export PATH=$PATH:~/go/bin' >> ~/.zshrc
   source ~/.zshrc
   ```

# 🔁 Recap
- The guide covers how to install Go programming language on macOS.
- It includes verification steps to check the installation.
- Instructions are provided for temporarily and permanently updating the PATH environment variable.
