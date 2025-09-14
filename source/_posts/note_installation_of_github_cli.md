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
slug: note-installing-github-copilot-cli-and-usage-guide
---

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
