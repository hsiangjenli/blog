---
title: '[tutorial] GitHub + PicGo + VSCode Extension'
date: '2025-01-29'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- picgo
toc: true
slug: tutorial-github-picgo-vscode-extension
lang: en
permalink: tutorial-github-picgo-vscode-extension.en/
translations:
  zh-TW: /zh-TW/tutorial-github-picgo-vscode-extension/
---

# 📌 Introduction
This article provides a tutorial on setting up GitHub, PicGo, and a VSCode extension to facilitate image uploading to GitHub repositories. It outlines the necessary prerequisites, the procedure to generate a GitHub token, and essential steps for configuring the PicGo extension in VSCode.
<!-- more -->

# 🚀 Quick Start
## Before You Start

Make sure you have following:

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
To ensure your images are accessible, set your repo to ***public***.

## VScode Extension

1. Install **PicGo** extension in VScode
1. Set **`Pic Bed: Current`** to **github**
1. Set **`Pic Bed > Github: Repo`** to your previously created public repo. Format is `{username}/{repo_name}`
1. Set **`Pic Bed: Uploader`** to **github**
1. Set **`Pic Bed > Github: Branch`** to the branch of your public repo
1. Set **`Pic Bed > Github: Path`** (Optional). If you want to store images in specific folder (e.g. `images`). Make sure to include a trailing slash (`/`), otherwise, it will be used as a prefix for image names
1. Set **`Pic Bed > Github: Token`** to the Github token you created earlier

<details>

![image](https://hackmd.io/_uploads/r1Yv0Pvu1g.png)
![image](https://hackmd.io/_uploads/SJHrBdwuyg.png)
![image](https://hackmd.io/_uploads/rkkYiuP_1l.png)

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

# 🔁 Recap
- You need a Github token and a public repository for image storage.
- Install the PicGo extension in VSCode for image uploading.
- Follow specific configuration steps in the PicGo extension to link it with GitHub.
- Potential troubleshooting includes ensuring `xclip` is installed on your system.
