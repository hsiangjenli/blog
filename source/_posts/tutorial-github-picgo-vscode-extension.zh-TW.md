---
title: '[教學] GitHub + PicGo + VSCode 擴充功能'
date: '2025-01-29'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- picgo
toc: true
translation_key: tutorial-github-picgo-vscode-extension
slug: tutorial-github-picgo-vscode-extension
source_sha: edc5a93bc6a74c5fe14587131bd69e9c9614876d7be1cda97841a832af453a59
origin_lang: en
---

# 📌 介紹
這篇文章示範如何設定 GitHub、PicGo 與 VSCode 擴充功能，以便將圖片上傳到 GitHub 儲存庫。內容說明必要的前置條件、如何產生 GitHub 權杖，以及在 VSCode 中設定 PicGo 擴充功能的重點步驟。
<!-- more -->

# 🚀 快速開始
## 開始前

請確認您具備下列項目：

- 一個具有存取您儲存庫權限的 Github 權杖
- 一個用來儲存圖片的儲存庫

## GitHub

### 產生 GitHub 權杖

1. 前往 `Settings/Developer settings/Personal access tokens/Token (classic)`
1. 點選 ***Generate new token (classic)***
1. 設定一個容易辨識的名稱，並選擇 **永不過期**
1. 選取該權杖所需的權限範圍
<!-- 1. Setup token's name for better recognize and select no expiration date. Finally, select the scope that this access token can do. -->

<details>

![圖片](https://hackmd.io/_uploads/SJkewdvukl.png)
![圖片](https://hackmd.io/_uploads/rkmvPOvu1l.png)
![圖片](https://hackmd.io/_uploads/HyU5wdvO1x.png)
![圖片](https://hackmd.io/_uploads/rkvCwuw_ke.png)
![圖片](https://hackmd.io/_uploads/r1HEddvdJl.png)    
    
</details>


### 設定儲存庫
為確保圖片可被存取，請將您的儲存庫設為 ***public***。

## VSCode 擴充功能

1. 在 VSCode 安裝 **PicGo** 擴充功能
1. 將 **`Pic Bed: Current`** 設為 **github**
1. 將 **`Pic Bed > Github: Repo`** 設為您先前建立的公開儲存庫。格式為 `{username}/{repo_name}`
1. 將 **`Pic Bed: Uploader`** 設為 **github**
1. 將 **`Pic Bed > Github: Branch`** 設為您公開儲存庫的分支名稱
1. 將 **`Pic Bed > Github: Path`**（可選）。若您想將圖片儲存在特定資料夾（例如 `images`），請設定此項。務必包含結尾斜線 (`/`)，否則會被當作圖片名稱的前綴
1. 將 **`Pic Bed > Github: Token`** 設為您先前建立的 Github 權杖

<details>

![圖片](https://hackmd.io/_uploads/r1Yv0Pvu1g.png)
![圖片](https://hackmd.io/_uploads/SJHrBdwuyg.png)
![圖片](https://hackmd.io/_uploads/rkkYiuP_1l.png)

</details>


### 疑難排解

如果看到以下錯誤，表示系統未安裝 `xclip`：

```shell
PicGo: xclip not found! Please install xclip before run picgo.
```
要解決此問題，請使用下列指令安裝 `xclip`：

```shell
sudo apt install xclip
```

# 🔁 回顧
- 您需要一個 Github 權杖以及一個公開的儲存庫來儲存圖片。
- 在 VSCode 安裝 PicGo 擴充功能以進行圖片上傳。
- 按照 PicGo 擴充功能中的設定步驟將其連結到 GitHub。
- 常見的疑難排解包含確認系統已安裝 `xclip`。
