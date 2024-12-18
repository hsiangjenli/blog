---
title: "[note] Want to install the latest version from a GitHub repo using pip"
date: 2024-12-18
tags:
  - python
  - git
  - pip
toc: true
---

- `devel` - stands for **development**

<!-- more -->

If you want to install a specific branch from GitHub, instead of the stable version from PyPI:

- **Repo URL :** `https://github.com/username/repository.git`
- **Repo Branch :** `devel`

The command to pip install this repo:

```python
pip install git+{repo_url}@{branch_name}
```

```python
pip install git+https://github.com/username/repository.git@devel
```

<!-- 「Installing devel from GitHub with pip」指的是使用 `pip` 來安裝 GitHub 上某個專案的開發版（development version），通常這個版本位於 GitHub 專案的 `devel` 或 `development` 分支。這些分支一般是專案的開發者用來進行功能測試和改進的地方，並不一定像正式釋出的版本那樣穩定。

`devel` 是「development」的縮寫，通常代表專案的開發過程中進行中的版本，而不是一個穩定、經過完整測試的版本。開發版會包含最新的功能和修復，但可能也會有一些尚未解決的問題。

以下是使用 `pip` 從 GitHub 安裝 `devel` 分支的方法：

```bash
pip install git+https://github.com/username/repository.git@devel
```

這個指令中：
- `git+https://github.com/username/repository.git` 是 GitHub 上專案的 URL。
- `@devel` 指的是你要從 `devel` 分支安裝專案。

這樣可以讓你安裝某個專案的開發版，而不是安裝從 PyPI 發佈的穩定版本。 -->
