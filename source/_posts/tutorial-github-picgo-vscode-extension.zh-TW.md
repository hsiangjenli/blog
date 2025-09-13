---
title: '[教學] GitHub + PicGo + VSCode 擴充套件'
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

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> # 📌 介紹
本文提供設定 GitHub、PicGo 與 VSCode 擴充套件的教學，以方便將圖片上傳至 GitHub 儲存庫。說明必要的前置準備、產生 GitHub 權杖的流程，及在 VSCode 配置 PicGo 擴充套件的要點。
<!-- more -->

# 🚀 快速開始
## 開始之前

請確認你具備：

- 可存取你的儲存庫的 GitHub 權杖
- 用來存放圖片的儲存庫

## GitHub

### 產生 GitHub 權杖

1. 前往 `Settings/Developer settings/Personal access tokens/Token (classic)`
1. 點選 ***Generate new token (classic)***
1. 為權杖設定易於辨識的名稱，並選擇 **No expiration**
1. 選取該權杖所需的權限範圍
<!-- 1. Setup token's name for better recognize and select no expiration date. Finally, select the scope that this access token can do. -->

<details>

![image](https://hackmd.io/_uploads/SJkewdvukl.png)
![image](https://hackmd.io/_uploads/rkmvPOvu1l.png)
![image](https://hackmd.io/_uploads/HyU5wdvO1x.png)
![image](https://hackmd.io/_uploads/rkvCwuw_ke.png)
![image](https://hackmd.io/_uploads/r1HEddvdJl.png)    
    
</details>


### 設定儲存庫
為確保你的圖片能被存取，將儲存庫設定為 ***public***。

## VSCode 擴充套件

1. 在 VSCode 安裝 **PicGo** 擴充套件
1. 將 **`Pic Bed: Current`** 設為 **github**
1. 將 **`Pic Bed > Github: Repo`** 設為你先前建立的公開儲存庫。格式為 `{username}/{repo_name}`
1. 將 **`Pic Bed: Uploader`** 設為 **github**
1. 將 **`Pic Bed > Github: Branch`** 設為你公開儲存庫的分支
1. 設定 **`Pic Bed > Github: Path`**（選用）。若你希望將圖片存放於特定資料夾（例如 `images`），請確保包含尾端斜線（`/`），否則該值會被當作圖片名稱的前綴。
1. 將 **`Pic Bed > Github: Token`** 設為你先前建立的 GitHub 權杖

<details>

![image](https://hackmd.io/_uploads/r1Yv0Pvu1g.png)
![image](https://hackmd.io/_uploads/SJHrBdwuyg.png)
![image](https://hackmd.io/_uploads/rkkYiuP_1l.png)

</details>


### 疑難排解

若你看到下列錯誤，表示系統尚未安裝 `xclip`：

```shell
PicGo: xclip not found! Please install xclip before run picgo.
```
要修復此問題，請使用下列指令安裝 `xclip`：

```shell
sudo apt install xclip
```

# 🔁 重點回顧
- 你需要一個 GitHub 權杖與一個公開儲存庫來存放圖片。
- 在 VSCode 安裝 PicGo 擴充套件以便上傳圖片。
- 依照 PicGo 擴充套件中的設定步驟將其與 GitHub 連結。
- 可能遇到的問題包含確認系統是否已安裝 `xclip`。
