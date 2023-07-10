---
title: The installation of GitHub Copilot CLI
date: 2023-07-10
toc: true
cover:
thumbnail:
---

```shell
npm install -g @githubnext/github-copilot-cli
```

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