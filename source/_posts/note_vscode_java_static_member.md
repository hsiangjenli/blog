---
title: '[note] 在 VScode 內設定常用的 Static Members'
date: '2026-02-26'
updated: '2026-02-26'
author:
- Hsiang-Jen Li
tags:
- java
toc: true
lang: zh-TW
slug: note-vscode-static-members
permalink: zh-TW/note-vscode-static-members/
translations:
  en: /note-vscode-static-members.en/
---

# 📌 簡介

在 VSCode 內設定常用的 Staic Member

<!-- more -->

# 🚀 如何在 VScode 內設定

開啟設定並搜尋 `Java Completion`，找到 `Favoriate Static Members` 點選`Edit in setting.json`，把自己常用的 Member 加入，像下面這樣。

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

# 🔗 參考資料

- [Code action: add static import #796](https://github.com/redhat-developer/vscode-java/issues/796)
- [浅谈 Java 中的 import static 使用方式](https://blog.csdn.net/weixin_43844521/article/details/150965843)
