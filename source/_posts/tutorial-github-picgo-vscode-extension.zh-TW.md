---
title: '[教學] GitHub + PicGo + VSCode Extension'
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
source_sha: db04f9fa41318ae7174ee1f3e9322ebbbc731831d6c3b9cc3f0881fd2ae3f829
origin_lang: en
permalink: zh-TW/tutorial-github-picgo-vscode-extension/
translations:
  en: /tutorial-github-picgo-vscode-extension.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
本文說明如何設定 GitHub、PicGo 與 VSCode 延伸功能，以方便將圖片上傳到 GitHub 儲存庫。說明必要的前置條件、產生 GitHub Token 的流程，以及在 VSCode 中設定 PicGo 延伸功能的重點步驟。
<!-- more -->

# 🚀 快速開始
## 開始之前

請確認您已具備以下項目：

- A Github Token with access to your repo
- A repo to store images

## GitHUb

### Generate GitHub Token

1. Go to `Settings/Developer settings/Personal access tokens/Token (classic)`
1. Click ***Generate new token (classic)***
1. Set a name for the token to identify it easily and choose **No expiration**
1. Select the required scopes for the token
<!-- 1. Setup token's name for better recognize and select no expiration date. Finally, select the scope that this access token can do. -->

<details>

![image](https://hackmd.io/_uploads/SJkewdvukl.png)
![image](https://hackmd.io/_uploads/rkmvPOvu1l.png)
![image](https://hackmd.io/_uploads/HyU5wdvO1x.png)
![image](https://hackmd.io/_uploads/rkvCwuw_ke.png)
![image](https://hackmd.io/_uploads/r1HEddvdJl.png)    
    
</details>


### Set Up Repo
為確保您的圖片可被存取，請將儲存庫設定為 ***public***。

## VScode Extension

1. Install **PicGo** extension in VScode
1. Set **`Pic Bed: Current`** to **github**
1. Set **`Pic Bed > Github: Repo`** to your previously created public repo. Format is `{username}/{repo_name}`
1. Set **`Pic Bed: Uploader`** to **github**
1. Set **`Pic Bed > Github: Branch`** to the branch of your public repo
1. Set **`Pic Bed > Github: Token`** to the Github token you created earlier

<details>

![image](https://hackmd.io/_uploads/r1Yv0Pvu1g.png)
![image](https://hackmd.io/_uploads/SJHrBdwuyg.png)
<!-- ![image](https://hackmd.io/_uploads/rkkYiuP_1l.png) -->
![20260219175145](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260219175145.png)

</details>


### Troubleshooting

If you see the following error, it means `xclip` is not installed:

```shell
PicGo: xclip not found! Please install xclip before run picgo.
```
To fix this, install `xclip` using the following command:

```shell
sudo apt install xclip
```

# 🔁 重點回顧
- You need a Github token and a public repository for image storage.
- Install the PicGo extension in VSCode for image uploading.
- Follow specific configuration steps in the PicGo extension to link it with GitHub.
- Potential troubleshooting includes ensuring `xclip` is installed on your system.
