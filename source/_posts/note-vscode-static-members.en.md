---
title: '[note] Setting commonly used Static Members in VScode'
date: '2026-02-26'
updated: '2026-02-26'
author:
- Hsiang-Jen Li
tags:
- java
toc: true
lang: en
slug: note-vscode-static-members
source_sha: 3540e5fe070901bec14c2d94f76c48889d211456c53f2f956fd206f7ac73442c
origin_lang: zh-TW
permalink: note-vscode-static-members.en/
translations:
  zh-TW: /zh-TW/note-vscode-static-members/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

在 VSCode 內設定常用的 Staic Member

<!-- more -->

# 🚀 How to configure in VScode

Open settings and search `Java Completion`, find `Favoriate Static Members` and click `Edit in setting.json`. Add your commonly used Member entries, like the following.

```jsonld
"java.completion.favoriteStaticMembers": [
    "org.junit.Assert.*",
    "org.junit.Assume.*",
    "org.junit.jupiter.api.Assertions.*",
    "org.junit.jupiter.api.Assumptions.*",
    "org.junit.jupiter.api.DynamicContainer.*",
    "org.junit.jupiter.api.DynamicTest.*",
    "org.mockito.Mockito.*",
    "org.mockito.ArgumentMatchers.*",
    "org.mockito.Answers.*"
]
```

![image](https://hackmd.io/_uploads/HJkBgY6dWl.png)


<!-- # 🔁 重點回顧 -->

# 🔗 References

- [Code action: add static import #796](https://github.com/redhat-developer/vscode-java/issues/796)
- [A brief discussion on using import static in Java](https://blog.csdn.net/weixin_43844521/article/details/150965843)
