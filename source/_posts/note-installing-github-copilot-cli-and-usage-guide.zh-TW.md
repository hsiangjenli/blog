---
title: '[note] 安裝 GitHub Copilot CLI 與使用指南'
date: '2023-07-10'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags: []
toc: true
slug: note-installing-github-copilot-cli-and-usage-guide
lang: zh-TW
source_sha: 563d3557713146fb79e6f7abd3555a948b129c94781c4974095ef2e1fe5b7ff8
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 Introduction
本文說明如何安裝與使用 GitHub Copilot CLI。內容包括使用 npm 的安裝流程、在 Windows 上設定執行原則，並示範如何使用 CLI 取得某些 git 指令的說明。
<!-- more -->

# 🚀 Quick Start
1. Install GitHub Copilot CLI:
   ```shell
   npm install -g @githubnext/github-copilot-cli
   ```
2. Set execution policy for PowerShell:
   ```shell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Authenticate with GitHub Copilot CLI:
   ```shell
   github-copilot-cli auth
   ```
4. Test the CLI:
   ```shell
   github-copilot-cli what-the-shell how to delete branch
   ```
   **Output:**
   ──────────────────── Command ────────────────────
   
git branch -d <branch>
   
   ────────────────── Explanation ──────────────────
   
   ○ git branch 用來列出分支。
     ◆ -d <branch> 會刪除分支 <branch>。
   
     ✅ 執行此指令
     📝 修改查詢
   > ❌ 取消

# 🔁 Recap
- 可透過 npm 輕鬆安裝 GitHub Copilot CLI。
- Windows 使用者需設定執行原則以允許執行腳本。
- 該 CLI 可協助 git 指令，並輸出指令與其說明。
