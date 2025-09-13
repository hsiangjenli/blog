---
title: '[tutorial] 使用 commitollama 強化提交訊息：VSCode 與本地 LLM 整合指南'
date: '2024-09-04'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- ollama
toc: true
translation_key: tutorial-enhancing-commit-messages-with-commitollama-a-guide-for-vscode-and-local-llm-integration
slug: tutorial-enhancing-commit-messages-with-commitollama-a-guide-for-vscode-and-local-llm-integration
source_sha: a9a1d22cbcf7ab9a8998bdd34a355a4d4adb1113753395fa376f5f7debb904a0
origin_lang: en
---

# 📌 介紹
This article introduces commitollama, an alternative to GitHub Copilot designed for generating commit messages using local LLMs, ensuring privacy for confidential projects. It outlines the installation process for the commitollama extension in VSCode and necessary setup steps to start using it effectively.
<!-- more -->

# 🚀 快速開始

![](https://commitollama.gallerycdn.vsassets.io/extensions/commitollama/commitollama/1.7.2/1723710671949/Microsoft.VisualStudio.Services.Icons.Default)

## 使用方式

1. 在 VSCode 安裝此擴充套件。  
1. 安裝 Ollama 以整合 LLM。

![來自 2024-09-04 22-35-57 的截圖](https://hackmd.io/_uploads/r1Vdxl8nR.png)

![來自 2024-09-04 22-37-24 的截圖](https://hackmd.io/_uploads/Bk-6gx830.png)
### 安裝 Ollama

執行以下命令以安裝 Ollama：
```shell
curl -fsSL https://ollama.com/install.sh | sh
```

![來自 2024-09-04 23-01-51 的截圖](https://hackmd.io/_uploads/rJwuUxIn0.png)

安裝後，您可以使用以下指令執行 Ollama：
```python
ollama
```
這會顯示可用指令的列表：
```python
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information

Use "ollama [command] --help" for more information about a command.
```

<!-- In this case, we will use `tavernari/git-commit-message` as our LLM model. This model is trained on Mistral0.3 . -->

透過執行以下命令下載 Phi3 模型 (3.8b)：

```shell
ollama pull phi3:3.8b
```

使用以下指令啟動 Ollama 服務：
```shell
ollama serve
```

<!-- If there a error message `Error: listen tcp 127.0.0.1:11434: bind: address already in use`. Which can be found at [there](https://github.com/ollama/ollama/issues/707) . You need to shutdown the ollama and restart it. -->

如果遇到錯誤訊息 `Error: listen tcp 127.0.0.1:11434: bind: address already in use`，可以在 [此處](https://github.com/ollama/ollama/issues/707) 找到解決方案。

要重新啟動 Ollama，請停止目前的服務並重新啟動：

```shell
systemctl stop ollama.service
ollama serve
```

要避免下載後模型被刪除，請參閱 [此討論](https://github.com/ollama/ollama/issues/1493)。



### 設定 VSCode

- 安裝擴充套件後，使用自訂模型來產生提交訊息。
- 在介面中按下按鈕以自動產生提交訊息。

![圖像](https://hackmd.io/_uploads/HklK2W82C.png)


# 🔁 重點回顧
- commitollama 是一個以隱私為重點的提交訊息產生器，可作為 GitHub Copilot 的替代方案。
- 該工具利用開源 LLM，例如 Llama、Mistral 與 Phi3。
- 透過簡單的擴充安裝程序可輕鬆整合到 VSCode。
- 使用者可以輕鬆取得模型、執行服務，並有效率地產生提交訊息。

# 🔗 參考資料
- https://github.com/ollama/ollama/issues/707
- https://github.com/ollama/ollama/issues/1493
