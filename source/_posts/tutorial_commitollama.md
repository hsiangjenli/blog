---
title: "[tutorial] Enhancing Commit Messages with commitollama: A Guide for VSCode and Local LLM Integration"
date: 2024-09-04
created_at: 2024-09-04
tags: ollama
toc: true
---

## commitollama

<!-- more -->

![](https://commitollama.gallerycdn.vsassets.io/extensions/commitollama/commitollama/1.7.2/1723710671949/Microsoft.VisualStudio.Services.Icons.Default)

<!-- The commitollama is an alternative of github copilot commit generator which based on open source llama (llama3, gemma, mistral, phi3 etc). If your project is confidential, you can use local LLM to ensure privacy issue. -->

**commitollama** is an alternative to GitHub Copilot’s commit message generator, powered by open-source models such as Llama (Llama3, Gemma, Mistral, Phi3, etc. For projects where confidentiality is a concern, commitollama allows you to use a local Large Language Model (LLM), ensuring privacy.

## How to use

<!-- Thanks to the contributors, commitollama can be directly used by simply install the extension in vscode and ollama -->

Thanks to its contributors, commitollama can be directly integrated into VSCode by installing the extension and setting up Ollama.

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

