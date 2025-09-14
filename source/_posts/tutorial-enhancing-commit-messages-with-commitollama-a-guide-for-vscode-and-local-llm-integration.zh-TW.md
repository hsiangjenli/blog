---
title: '[tutorial] 使用 commitollama 強化提交訊息：VSCode 與本地 LLM 整合指南'
date: '2024-09-04'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- ollama
toc: true
slug: tutorial-enhancing-commit-messages-with-commitollama-a-guide-for-vscode-and-local-llm-integration
lang: zh-TW
source_sha: a9a1d22cbcf7ab9a8998bdd34a355a4d4adb1113753395fa376f5f7debb904a0
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
本文介紹 commitollama，這是一個用於產生提交訊息（commit messages）的工具，作為 GitHub Copilot 的替代方案，採用本地 LLM 以確保機密專案的隱私。本文說明在 VSCode 中安裝 commitollama 擴充套件的流程以及開始使用所需的設定步驟。
<!-- more -->

# 🚀 快速開始

![](https://commitollama.gallerycdn.vsassets.io/extensions/commitollama/commitollama/1.7.2/1723710671949/Microsoft.VisualStudio.Services.Icons.Default)

## 使用方式

1. 在 VSCode 中安裝該擴充套件。  
1. 安裝 Ollama 以整合 LLM。

![截圖：2024-09-04 22-35-57](https://hackmd.io/_uploads/r1Vdxl8nR.png)

![截圖：2024-09-04 22-37-24](https://hackmd.io/_uploads/Bk-6gx830.png)
### 安裝 Ollama

執行以下指令以安裝 Ollama：
```shell
curl -fsSL https://ollama.com/install.sh | sh
```

![截圖：2024-09-04 23-01-51](https://hackmd.io/_uploads/rJwuUxIn0.png)

安裝完成後，可透過下列方式執行 Ollama：
```python
ollama
```
這會顯示可用指令清單：
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

下載 Phi3 模型 (3.8b)，執行：

```shell
ollama pull phi3:3.8b
```

啟動 Ollama 服務：
```shell
ollama serve
```

<!-- If there a error message `Error: listen tcp 127.0.0.1:11434: bind: address already in use`. Which can be found at [there](https://github.com/ollama/ollama/issues/707) . You need to shutdown the ollama and restart it. -->

如果遇到錯誤訊息 `Error: listen tcp 127.0.0.1:11434: bind: address already in use`，可在 [這裡](https://github.com/ollama/ollama/issues/707) 找到解法。

要重新啟動 Ollama，先停止目前服務再重新啟動：

```shell
systemctl stop ollama.service
ollama serve
```

若要避免下載後模型被刪除，請參閱此討論 [這裡](https://github.com/ollama/ollama/issues/1493) 。



### 在 VSCode 中設定

- 安裝擴充套件後，可使用自訂模型來產生提交訊息。
- 在介面中按下按鈕即可自動產生提交訊息。

![圖片](https://hackmd.io/_uploads/HklK2W82C.png)


# 🔁 回顧
- commitollama 是一個重視隱私的提交訊息產生器，作為 GitHub Copilot 的替代方案。
- 該工具利用開放原始碼 LLM，例如 Llama、Mistral 與 Phi3。
- 透過簡單的擴充套件安裝程序即可與 VSCode 輕鬆整合。
- 使用者可以輕鬆取得模型、啟動服務並有效率地生成提交訊息。

# 🔗 參考資料
- https://github.com/ollama/ollama/issues/707
- https://github.com/ollama/ollama/issues/1493
