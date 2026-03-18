---
title: '[tutorial] 讓在 VScode 開發 Java 跟 Intellij 一樣好用的 Extension'
date: '2026-03-18'
updated: '2026-03-18'
author:
- 'Hsiang-Jen Li'
tags:
- java
toc: true
lang: zh-TW
---

# 📌 簡介

讓在 VScode 開發 Java 跟 Intellij 一樣好用 ~~

<!-- more -->

# 🚀 介紹 Extension

## Indention Setup

![image](https://hackmd.io/_uploads/r1akTW6t-e.png)

![image](https://hackmd.io/_uploads/ByA53ZatWg.png)


## Project Manager for Java

![image](https://hackmd.io/_uploads/HJ7xkCvqWe.png)


![image](https://hackmd.io/_uploads/HkPqktUtZe.png)

## Java Formatter

![image](https://hackmd.io/_uploads/rJe0oOnPtZg.png)

![image](https://hackmd.io/_uploads/HkmxF3DtWg.png)

```json
"java.format.settings.url": "https://raw.githubusercontent.com/google/styleguide/gh-pages/eclipse-java-google-style.xml",
```

```json
"java.format.settings.profile": "GoogleStyle",
```

## IntelliJ IDEA Keybindings

![image](https://hackmd.io/_uploads/HkX6tO8F-x.png)

- https://marketplace.visualstudio.com/items?itemName=k--kato.intellij-idea-keybindings

### After

#### 建立新的 Method

1. <kbd>Option</kbd> + <kbd>Enter</kbd>
2. 選 `Create method xxx`

![image](https://hackmd.io/_uploads/HJrUid8YZe.png)

## Javadoc Tools

![image](https://hackmd.io/_uploads/SyaZOd8Ybe.png)

### Before

![image](https://hackmd.io/_uploads/BJ-2a_IF-g.png)

漂浮視窗

### After

![image](https://hackmd.io/_uploads/SyM9Ou8t-x.png)

點選 Java Class 可以直接 preview Java Doc

# 🔗 參考資料

- [Improve readability of javadoc #3773](https://github.com/redhat-developer/vscode-java/issues/3773)
- [Java formatting and linting](https://code.visualstudio.com/docs/java/java-linting)
- [vscode-java](https://github.com/redhat-developer/vscode-java)
