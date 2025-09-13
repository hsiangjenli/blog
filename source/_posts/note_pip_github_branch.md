---
title: '[note] Want to install the latest version from a GitHub repo using pip'
date: '2024-12-18'
lang: en
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- python
- git
- pip
toc: true
translation_key: note-want-to-install-the-latest-version-from-a-github-repo-using-pip
slug: note-want-to-install-the-latest-version-from-a-github-repo-using-pip
---

# 📌 Introduction
This article explains how to install a specific branch of a GitHub repository using pip, particularly focusing on the 'devel' branch, which is typically used for development purposes rather than stable releases.
<!-- more -->

# 🚀 Quick Start
To install the development version from GitHub using pip, execute the following command:

```bash
pip install git+https://github.com/username/repository.git@devel
```

# 🔁 Recap
- You can install a specific branch from GitHub using pip.
- The 'devel' branch typically contains unstable development versions.
- To install, use the command format: `pip install git+{repo_url}@{branch_name}`.
- Replace `{repo_url}` with your repository URL and `{branch_name}` with 'devel'.
- Ensure you have pip installed to use this command.
