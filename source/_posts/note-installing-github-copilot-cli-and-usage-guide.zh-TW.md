---
title: '[note] 安裝 GitHub Copilot CLI 與使用指南'
date: '2023-07-10'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags: []
toc: true
translation_key: note-installing-github-copilot-cli-and-usage-guide
slug: note-installing-github-copilot-cli-and-usage-guide
source_sha: 563d3557713146fb79e6f7abd3555a948b129c94781c4974095ef2e1fe5b7ff8
origin_lang: en
---

# 📌 介紹
這篇文章說明如何安裝並使用 GitHub Copilot CLI。內容涵蓋使用 npm 的安裝流程、在 Windows 上設定執行原則，並示範如何使用 CLI 取得某些 git 指令的說明。
<!-- more -->

# 🚀 快速開始
1. 安裝 GitHub Copilot CLI：
   ```shell
   npm install -g @githubnext/github-copilot-cli
   ```
2. 為 PowerShell 設定執行原則：
   ```shell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. 使用 GitHub Copilot CLI 進行驗證：
   ```shell
   github-copilot-cli auth
   ```
4. 測試 CLI：
   ```shell
   github-copilot-cli what-the-shell how to delete branch
   ```
   **輸出：**
   ──────────────────── Command ────────────────────
   
git branch -d <branch>
   
   ────────────────── Explanation ──────────────────
   
   ○ git branch 用於列出分支。
     ◆ -d <branch> 刪除分支 <branch>。
   
     ✅ 執行此命令
     📝 修改查詢
   > ❌ 取消

# 🔁 回顧
- GitHub Copilot CLI 可透過 npm 輕鬆安裝。
- Windows 使用者需設定執行原則以允許執行腳本。
- CLI 可協助 git 指令，並輸出指令與說明。
