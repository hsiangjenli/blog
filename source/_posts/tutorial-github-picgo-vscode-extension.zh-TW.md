---
title: '[教學] GitHub + PicGo + VSCode 擴充套件'
date: '2025-01-29'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- picgo
toc: true
slug: tutorial-github-picgo-vscode-extension
lang: zh-TW
source_sha: edc5a93bc6a74c5fe14587131bd69e9c9614876d7be1cda97841a832af453a59
origin_lang: en
permalink: zh-TW/tutorial-github-picgo-vscode-extension/
translations:
  en: /tutorial-github-picgo-vscode-extension.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
本文提供如何設定 GitHub、PicGo 與 VSCode 擴充套件的教學，以便將圖片上傳到 GitHub 儲存庫。說明必要的先決條件、產生 GitHub 權杖的步驟，以及在 VSCode 中設定 PicGo 擴充套件的重點步驟。
<!-- more -->

# 🚀 快速開始
## 開始前準備

請確認你已具備下列項目：

- 具有存取你儲存庫權限的 GitHub 權杖
- 一個用於存放圖片的儲存庫

## GitHub

### 產生 GitHub 權杖

1. 前往 `Settings/Developer settings/Personal access tokens/Token (classic)`
1. 點選 ***Generate new token (classic)***
1. 為權杖設定名稱以便識別，並選擇 **No expiration**
1. 選取該權杖所需的權限範圍（scopes）

<details>

![image](https://hackmd.io/_uploads/SJkewdvukl.png)
![image](https://hackmd.io/_uploads/rkmvPOvu1l.png)
![image](https://hackmd.io/_uploads/HyU5wdvO1x.png)
![image](https://hackmd.io/_uploads/rkvCwuw_ke.png)
![image](https://hackmd.io/_uploads/r1HEddvdJl.png)    
    
</details>


### 設定儲存庫
為確保圖片可被存取，請將你的儲存庫設為 ***public***。

## VSCode 擴充套件

1. 在 VSCode 中安裝 **PicGo** 擴充套件
1. 將 **`Pic Bed: Current`** 設為 **github**
1. 將 **`Pic Bed > Github: Repo`** 設為你先前建立的公開儲存庫。格式為 `{username}/{repo_name}`
1. 將 **`Pic Bed: Uploader`** 設為 **github**
1. 將 **`Pic Bed > Github: Branch`** 設為公開儲存庫的分支
1. 設定 **`Pic Bed > Github: Path`**（可選）。若要將圖片儲存在特定資料夾（例如 `images`），請確保包含結尾的斜線（`/`），否則會被當作圖片名稱的前綴。
1. 將 **`Pic Bed > Github: Token`** 設為你先前建立的 GitHub 權杖

<details>

![image](https://hackmd.io/_uploads/r1Yv0Pvu1g.png)
![image](https://hackmd.io/_uploads/SJHrBdwuyg.png)
![image](https://hackmd.io/_uploads/rkkYiuP_1l.png)

</details>


### 疑難排解

若出現以下錯誤，表示系統未安裝 `xclip`：

```shell
PicGo: xclip not found! Please install xclip before run picgo.
```
可使用下列指令安裝 `xclip`：

```shell
sudo apt install xclip
```

# 🔁 總結
- 你需要一個 GitHub 權杖與一個用於儲存圖片的公開儲存庫。
- 在 VSCode 中安裝 PicGo 擴充套件以進行圖片上傳。
- 在 PicGo 擴充套件中按照特定設定步驟將其與 GitHub 連結。
- 可能的疑難排解包含確認系統已安裝 `xclip`。
