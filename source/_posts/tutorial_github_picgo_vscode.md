---
title: '[Tutorial] GitHub + PicGo + VSCode Extension'
date: '2025-01-29'
lang: en
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- picgo
toc: true
translation_key: tutorial-github-picgo-vscode-extension
slug: tutorial-github-picgo-vscode-extension
source_sha: 22cf90991752465758d33f5aff62141f584c34d1b478656d546ae8f35d539f7c
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
>
# 📌 Introduction
This article provides a tutorial for setting up GitHub, PicGo, and the VSCode extension to easily upload images to a GitHub repository. It explains the necessary prerequisites, the process to generate a GitHub token, and key points for configuring the PicGo extension in VSCode.
<!-- more -->

# 🚀 Quick Start
## Before you begin

Make sure you have:

- A GitHub token with access to your repository
- A repository to store images

## GitHub

### Generating a GitHub token

1. Go to `Settings/Developer settings/Personal access tokens/Token (classic)`
1. Click ***Generate new token (classic)***
1. Set a recognizable name for the token and choose **No expiration**
1. Select the scopes/permissions required for the token
<!-- 1. Setup token's name for better recognize and select no expiration date. Finally, select the scope that this access token can do. -->

<details>

![image](https://hackmd.io/_uploads/SJkewdvukl.png)
![image](https://hackmd.io/_uploads/rkmvPOvu1l.png)
![image](https://hackmd.io/_uploads/HyU5wdvO1x.png)
![image](https://hackmd.io/_uploads/rkvCwuw_ke.png)
![image](https://hackmd.io/_uploads/r1HEddvdJl.png)    
    
</details>


### Configure the repository
Set the repository to ***public*** to ensure your images can be accessed.

## VSCode Extension

1. Install the **PicGo** extension in VSCode
1. Set **`Pic Bed: Current`** to **github**
1. Set **`Pic Bed > Github: Repo`** to the public repository you created. Format: `{username}/{repo_name}`
1. Set **`Pic Bed: Uploader`** to **github**
1. Set **`Pic Bed > Github: Branch`** to the branch of your public repository
1. Configure **`Pic Bed > Github: Path`** (optional). If you want images stored in a specific folder (e.g., `images`), make sure to include a trailing slash (`/`); otherwise the value will be treated as a prefix of the image name.
1. Set **`Pic Bed > Github: Token`** to the GitHub token you created earlier

<details>

![image](https://hackmd.io/_uploads/r1Yv0Pvu1g.png)
![image](https://hackmd.io/_uploads/SJHrBdwuyg.png)
![image](https://hackmd.io/_uploads/rkkYiuP_1l.png)

</details>


### Troubleshooting

If you see the following error, it means `xclip` is not installed on your system:

```shell
PicGo: xclip not found! Please install xclip before run picgo.
```
To fix this, install `xclip` using the following command:

```shell
sudo apt install xclip
```

# 🔁 Key takeaways
- You need a GitHub token and a public repository to store images.
- Install the PicGo extension in VSCode to upload images.
- Link PicGo with GitHub by following the settings in the PicGo extension.
- A possible issue is ensuring `xclip` is installed on your system.
