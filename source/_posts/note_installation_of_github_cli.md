---
title: '[note] Install GitHub Copilot CLI and Usage Guide'
date: '2023-07-10'
lang: en
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags: []
toc: true
translation_key: note-installing-github-copilot-cli-and-usage-guide
slug: note-installing-github-copilot-cli-and-usage-guide
source_sha: a36cff513c0b3ae452f077b8427bf7e28ae6488964579dd991d77c48329e1581
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> 
# 📌 Introduction
This article explains how to install and use the GitHub Copilot CLI. It includes the installation process using npm, setting the execution policy on Windows, and demonstrates how to use the CLI to get help for specific git commands.
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
   
   ○ git branch is used to list branches.
     ◆ -d <branch> will delete the branch <branch>.
   
     ✅ Run this command
     📝 Modify query
   > ❌ Cancel

# 🔁 Key Takeaways
- The GitHub Copilot CLI can be easily installed via npm.
- Windows users need to set the execution policy to allow running scripts.
- The CLI can assist with git commands and outputs the command along with explanations.
