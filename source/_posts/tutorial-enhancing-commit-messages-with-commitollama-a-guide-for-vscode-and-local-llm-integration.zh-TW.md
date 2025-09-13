---
title: '[tutorial] 使用 commitollama 改善提交訊息：VSCode 與本地 LLM 整合指南'
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

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> # 📌 介紹
本篇文章介紹 commitollama，一個用於生成提交訊息且以本地 LLM 為基礎的替代方案，適合需保護專案隱私的情境。本文說明在 VSCode 中安裝 commitollama 延伸功能的流程以及開始使用前的必要設定。
<!-- more -->

# 🚀 快速開始

![](https://commitollama.gallerycdn.vsassets.io/extensions/commitollama/commitollama/1.7.2/1723710671949/Microsoft.VisualStudio.Services.Icons.Default)

## 使用方式

1. 在 VSCode 中安裝此延伸功能。  
1. 安裝 Ollama，以整合 LLM。

![Screenshot from 2024-09-04 22-35-57](https://hackmd.io/_uploads/r1Vdxl8nR.png)

![Screenshot from 2024-09-04 22-37-24](https://hackmd.io/_uploads/Bk-6gx830.png)
### 安裝 Ollama

執行以下指令以安裝 Ollama：
```shell
curl -fsSL https://ollama.com/install.sh | sh
```

![Screenshot from 2024-09-04 23-01-51](https://hackmd.io/_uploads/rJwuUxIn0.png)

安裝完成後，可執行 Ollama：
```python
ollama
```
這會顯示可用的指令列表：
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

<!-- 在此範例中，我們將使用 `tavernari/git-commit-message` 作為 LLM 模型。該模型以 Mistral0.3 訓練。 -->

下載 Phi3 模型（3.8b），執行：

```shell
ollama pull phi3:3.8b
```

啟動 Ollama 服務：
```shell
ollama serve
```

<!-- 若遇到錯誤訊息 `Error: listen tcp 127.0.0.1:11434: bind: address already in use`，可參考此處的討論：https://github.com/ollama/ollama/issues/707。你需要關閉 ollama 並重新啟動。 -->

如果你遇到錯誤訊息 `Error: listen tcp 127.0.0.1:11434: bind: address already in use`，可以在此處找到解法 [here](https://github.com/ollama/ollama/issues/707) 。

要重新啟動 Ollama，先停止目前的服務再重新啟動：

```shell
systemctl stop ollama.service
ollama serve
```

為避免模型在下載後被刪除，請參考此討論 [here](https://github.com/ollama/ollama/issues/1493) 。



### 在 VSCode 中設定

- 安裝延伸功能後，可使用自訂模型來生成提交訊息。
- 在介面中按下按鈕即可自動生成提交訊息。

![image](https://hackmd.io/_uploads/HklK2W82C.png)


# 🔁 小結
- commitollama 是一個以隱私為重點、可替代 GitHub Copilot 的提交訊息生成工具。
- 該工具可使用 Llama、Mistral 和 Phi3 等開源 LLM。
- 可透過簡單的延伸功能安裝流程，輕鬆整合到 VSCode。
- 使用者可以輕鬆取得模型、執行服務並有效生成提交訊息。

# 🔗 參考資料
- https://github.com/ollama/ollama/issues/707
- https://github.com/ollama/ollama/issues/1493
