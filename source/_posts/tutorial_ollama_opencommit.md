---
title: '[tutorial] Using Ollama with OpenCommit for Local Commit Message Generation'
date: '2024-08-29'
updated: '2025-02-28 (Refactored by ChatGPT-4o Mini)'
author:
  - 'Hsiang-Jen Li'
  - ' & ChatGPT-4o Mini'
tags:
- ollama
toc: true
---

# 📌 Introduction
This article covers using Ollama with OpenCommit for generating commit messages locally. It includes an overview of running Ollama in a Docker container, instructions for using the Ollama CLI, and how to combine Ollama with OpenCommit for generating commit messages.
<!-- more -->

# 🚀 Quick Start
### Start a container
```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama-commit ollama/ollama:0.3.6
```

### Enter the Docker container
```shell
docker exec -it ollama-commit bash
```

### Pull model
```shell
ollama run gemma2:2b
```

### Start a chat
```shell
>>> Send a message (/? for help)
```

### Exit the chat
Type `/bye` to exit the chat.

### Install opencommit
```shell
npm install -g opencommit
```

### Generate commit messages with local ollama server
```shell
OCO_AI_PROVIDER='ollama/gemma2:2b' opencommit
```

output:

```shell
┌  open-commit
│
◇  1 staged files:
  README.md
│
◇  📝 Commit message generated
│
└  Generated commit message:
——————————————————
feat(README.md): add link to Ollama website and examples of running models


——————————————————

│
◇  Confirm the commit message?
│  No
│
◇  Do you want to regenerate the message ?
│  Yes
│
◇  📝 Commit message generated
│
└  Generated commit message:
——————————————————
feat(README.md): add link to Ollama website and examples of model usage in README.md 
```



## Error code 127

```shell
Error: llama runner process has terminated: exit status 127

>>> [GIN] 2024/08/28 - 18:43:24 | 200 |      68.455µs |       127.0.0.1 | HEAD     "/"
>>> [GIN] 2024/08/28 - 18:43:24 | 200 |    7.845273ms |       127.0.0.1 | POST     "/api/show"
>>> time=2024-08-28T18:43:24.392Z level=INFO source=memory.go:309 msg="offload to cpu" layers.requested=-1 layers.model=33 layers.offload=0 layers.split="" memory.available="[7.3 GiB]" memory.required.full="5.5 GiB" memory.required.partial="0 B" memory.required.kv="1.0 GiB" memory.required.allocations="[5.5 GiB]" memory.weights.total="4.7 GiB" memory.weights.repeating="4.6 GiB" memory.weights.nonrepeating="105.0 MiB" memory.graph.full="560.0 MiB" memory.graph.partial="585.0 MiB"
>>> time=2024-08-28T18:43:24.392Z level=INFO source=server.go:391 msg="starting llama server" cmd="/tmp/ollama731275887/runners/cpu/ollama_llama_server --model /root/.ollama/models/blobs/sha256-ff82381e2bea77d91c1b824c7afb83f6fb73e9f7de9dda631bcdbca564aa5435 --ctx-size 8192 --batch-size 512 --embedding --log-disable --no-mmap --parallel 4 --port 33357"
>>> time=2024-08-28T18:43:24.392Z level=INFO source=sched.go:450 msg="loaded runners" count=1
>>> time=2024-08-28T18:43:24.393Z level=INFO source=server.go:591 msg="waiting for llama runner to start responding"
>>> time=2024-08-28T18:43:24.393Z level=INFO source=server.go:625 msg="waiting for server to become available" status="llm server error"
>>> /tmp/ollama731275887/runners/cpu/ollama_llama_server: error while loading shared libraries: libllama.so: cannot open shared object file: No such file or directory
>>> time=2024-08-28T18:43:24.644Z level=ERROR source=sched.go:456 msg="error loading llama server" error="llama runner process has terminated: exit status 127"
[GIN] 2024/08/28 - 18:43:24 | 500 |  266.021797ms |       127.0.0.1 | POST     "/api/chat"
```

The error code occurs when the Docker image version is greater than `0.3.6`. Therefore, you need to pull the ollama image with version `0.3.6` and run the container. Click [here](https://github.com/ollama/ollama/issues/6541) to view the discussion.


# 🔁 Recap
- Ollama allows for the generation of commit messages using AI models.
- The article details setting up Ollama in a Docker environment.
- OpenCommit is integrated to simplify the process of generating commit messages using an AI model.
- Users can interact with the AI model through a chat interface.

# 🔗 References
- https://ollama.com/models
- https://github.com/ollama/ollama/issues/6541
