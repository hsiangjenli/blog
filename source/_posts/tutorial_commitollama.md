---
title: '[tutorial] Using commitollama to improve commit messages: VSCode and local
  LLM integration guide'
date: '2024-09-04'
lang: en
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- ollama
toc: true
translation_key: tutorial-enhancing-commit-messages-with-commitollama-a-guide-for-vscode-and-local-llm-integration
slug: tutorial-enhancing-commit-messages-with-commitollama-a-guide-for-vscode-and-local-llm-integration
source_sha: 616ece52a38bfab5290866615254fa5fa7a5c7405c2edbab3f4b49006bd04ff8
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 Introduction
This article introduces commitollama, a local-LLM-based alternative for generating commit messages, suitable for situations where project privacy must be protected. It explains the process of installing the commitollama extension in VSCode and the necessary setup before getting started.
<!-- more -->

# 🚀 Quick Start

![](https://commitollama.gallerycdn.vsassets.io/extensions/commitollama/commitollama/1.7.2/1723710671949/Microsoft.VisualStudio.Services.Icons.Default)

## How to use

1. Install the extension in VSCode.  
1. Install Ollama to integrate LLMs.

![Screenshot from 2024-09-04 22-35-57](https://hackmd.io/_uploads/r1Vdxl8nR.png)

![Screenshot from 2024-09-04 22-37-24](https://hackmd.io/_uploads/Bk-6gx830.png)
### Install Ollama

Run the following command to install Ollama:
```shell
curl -fsSL https://ollama.com/install.sh | sh
```

![Screenshot from 2024-09-04 23-01-51](https://hackmd.io/_uploads/rJwuUxIn0.png)

After installation, you can run Ollama:
```python
ollama
```
This will show a list of available commands:
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

<!-- In this example, we will use `tavernari/git-commit-message` as the LLM model. That model is trained on Mistral0.3. -->

Download the Phi3 model (3.8b) by running:

```shell
ollama pull phi3:3.8b
```

Start the Ollama service:
```shell
ollama serve
```

<!-- If you encounter the error `Error: listen tcp 127.0.0.1:11434: bind: address already in use`, refer to this discussion: https://github.com/ollama/ollama/issues/707. You may need to stop ollama and restart it. -->

If you encounter the error `Error: listen tcp 127.0.0.1:11434: bind: address already in use`, you can find a solution here: [https://github.com/ollama/ollama/issues/707](https://github.com/ollama/ollama/issues/707).

To restart Ollama, stop the current service and then restart:

```shell
systemctl stop ollama.service
ollama serve
```

To avoid models being deleted after download, see this discussion: [https://github.com/ollama/ollama/issues/1493](https://github.com/ollama/ollama/issues/1493).



### Configuring in VSCode

- After installing the extension, you can use a custom model to generate commit messages.
- Press the button in the UI to automatically generate a commit message.

![image](https://hackmd.io/_uploads/HklK2W82C.png)


# 🔁 Summary
- commitollama is a privacy-focused alternative for generating commit messages, serving as a replacement for GitHub Copilot in this use case.
- The tool can use open-source LLMs like Llama, Mistral, and Phi3.
- It integrates easily into VSCode through a simple extension installation process.
- Users can obtain models, run the service, and effectively generate commit messages with minimal effort.

# 🔗 References
- https://github.com/ollama/ollama/issues/707
- https://github.com/ollama/ollama/issues/1493
