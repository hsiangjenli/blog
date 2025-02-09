---
title: "[note] Installing GitHub Copilot CLI and Usage Guide"
date: 2023-07-10
toc: true
---

```shell
npm install -g @githubnext/github-copilot-cli
```
<!-- more -->
```shell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

```shell
github-copilot-cli auth
```


```shell
# test for cli
github-copilot-cli what-the-shell how to delete branch
```
```shell
 # output
 ──────────────────── Command ────────────────────

git branch -d <branch>

 ────────────────── Explanation ──────────────────

○ git branch is used to list branches.
  ◆ -d <branch> deletes the branch <branch>.

  ✅ Run this command
  📝 Revise query
> ❌ Cancel
```
