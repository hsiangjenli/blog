---
title: '[note] 安裝 Golang (PATH)'
date: '2024-08-27'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- go
toc: true
translation_key: note-installation-of-golang-path
slug: note-installation-of-golang-path
source_sha: 9d3c141b7370a556c233b0c443c662d12ebe171694cfbb684859a502273b15a6
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> # 📌 介紹
這篇文章提供在 macOS 上安裝 Go 並將系統的 PATH 變數配置為包含 Go 可執行檔的逐步指南。
<!-- more -->

# 🚀 快速開始
1. **使用 Homebrew 安裝 Go：**
   ```shell
   brew install go
   ```

2. **驗證安裝：**
   ```shell
   ls ~/go/bin/
   ```

3. **暫時更新 PATH：**
   ```shell
   export PATH=$PATH:~/go/bin
   ```

4. **永久更新 PATH：**
   ```shell
   echo 'export PATH=$PATH:~/go/bin' >> ~/.zshrc
   source ~/.zshrc
   ```

# 🔁 回顧
- 本指南說明如何在 macOS 上安裝 Go 程式語言。
- 包含驗證步驟以檢查安裝是否成功。
- 提供了暫時與永久更新 PATH 環境變數的指示。
