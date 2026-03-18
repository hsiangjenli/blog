---
title: '[tutorial] Extensions that make developing Java in VScode as convenient as
  in Intellij'
date: '2026-03-18'
updated: '2026-03-18'
author:
- Hsiang-Jen Li
tags:
- java
toc: true
lang: en
slug: tutorial-vscode-java-intellij-extension
source_sha: 0e189118d66a6f409213a1a51a4fa6f57314945d70f688565fbb708699c7a525
origin_lang: zh-TW
permalink: tutorial-vscode-java-intellij-extension.en/
translations:
  zh-TW: /zh-TW/tutorial-vscode-java-intellij-extension/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

Make developing Java in VScode as convenient as in Intellij ~~

<!-- more -->

# 🚀 Introducing Extensions

## Indentation Setup

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

#### Create a new Method

1. <kbd>Option</kbd> + <kbd>Enter</kbd>
2. Select `Create method xxx`

![image](https://hackmd.io/_uploads/HJrUid8YZe.png)

## Javadoc Tools

![image](https://hackmd.io/_uploads/SyaZOd8Ybe.png)

### Before

![image](https://hackmd.io/_uploads/BJ-2a_IF-g.png)

Floating window

### After

![image](https://hackmd.io/_uploads/SyM9Ou8t-x.png)

Clicking a Java Class lets you directly preview Java Doc

# 🔗 References

- [Improve readability of javadoc #3773](https://github.com/redhat-developer/vscode-java/issues/3773)
- [Java formatting and linting](https://code.visualstudio.com/docs/java/java-linting)
- [vscode-java](https://github.com/redhat-developer/vscode-java)
