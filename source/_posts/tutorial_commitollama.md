---
title: '[tutorial] Enhancing Commit Messages with commitollama: A Guide for VSCode
  and Local LLM Integration'
date: '2024-09-04'
lang: en
updated: '2025-02-28 (Refactored by ChatGPT-4o Mini)'
author:
  - 'Hsiang-Jen Li'
  - ' & ChatGPT-4o Mini'
tags:
- ollama
toc: true
---

# 📌 Introduction
This article introduces commitollama, an alternative to GitHub Copilot designed for generating commit messages using local LLMs, ensuring privacy for confidential projects. It outlines the installation process for the commitollama extension in VSCode and necessary setup steps to start using it effectively.
<!-- more -->

# 🚀 Quick Start

![](https://commitollama.gallerycdn.vsassets.io/extensions/commitollama/commitollama/1.7.2/1723710671949/Microsoft.VisualStudio.Services.Icons.Default)

## How to use

1. Install the extension in VSCode.  
1. Install Ollama to integrate the LLM.

![Screenshot from 2024-09-04 22-35-57](https://hackmd.io/_uploads/r1Vdxl8nR.png)

![Screenshot from 2024-09-04 22-37-24](https://hackmd.io/_uploads/Bk-6gx830.png)
### Installing Ollama

Run the following command to install Ollama:
```shell
curl -fsSL https://ollama.com/install.sh | sh
```

![Screenshot from 2024-09-04 23-01-51](https://hackmd.io/_uploads/rJwuUxIn0.png)

After installation, you can run Ollama using:
```python
ollama
```
This will display a list of available commands:
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

Download the Phi3 model (3.8b) by running:

```shell
ollama pull phi3:3.8b
```

Start the Ollama service using:
```shell
ollama serve
```

<!-- If there a error message `Error: listen tcp 127.0.0.1:11434: bind: address already in use`. Which can be found at [there](https://github.com/ollama/ollama/issues/707) . You need to shutdown the ollama and restart it. -->


If you encounter the error message `Error: listen tcp 127.0.0.1:11434: bind: address already in use`, you can find a solution [here](https://github.com/ollama/ollama/issues/707) .

To restart Ollama, stop the current service and relaunch it:

```shell
systemctl stop ollama.service
ollama serve
```

To prevent the model from being deleted after downloading, refer to this discussion [here](https://github.com/ollama/ollama/issues/1493) .



### Setting Up VSCode

- After installing the extension, use a custom model for commit message generation.
- Press the button in the interface to automatically generate the commit message.

![image](https://hackmd.io/_uploads/HklK2W82C.png)


# 🔁 Recap
- commitollama is a privacy-focused commit message generator alternative to GitHub Copilot.
- The tool leverages open-source LLMs like Llama, Mistral, and Phi3.
- Easy integration with VSCode through a simple extension installation process.
- Users can easily retrieve models, run services, and generate commit messages efficiently.

# 🔗 References
- https://github.com/ollama/ollama/issues/707
- https://github.com/ollama/ollama/issues/1493
