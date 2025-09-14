---
title: '[tutorial] 使用 Ollama 與 OpenCommit 在本地生成提交訊息'
date: '2024-08-29'
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- ollama
toc: true
slug: tutorial-using-ollama-with-opencommit-for-local-commit-message-generation
lang: zh-TW
source_sha: 7b5ad48eaf49f87b2f8799479740c20362eb6281e183bb6b64b1822bf79b5008
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
本文說明如何使用 Ollama 與 OpenCommit 在本地生成提交訊息。內容包含在 Docker 容器中執行 Ollama 的概覽、使用 Ollama CLI 的指示，以及如何將 Ollama 與 OpenCommit 結合以生成提交訊息。
<!-- more -->

# 🚀 快速開始
### 啟動容器
```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama-commit ollama/ollama:0.3.6
```

### 進入 Docker 容器
```shell
docker exec -it ollama-commit bash
```

### 拉取模型
```shell
ollama run gemma2:2b
```

### 開始聊天
```shell
>>> Send a message (/? for help)
```

### 離開聊天
輸入 `/bye` 以離開聊天。

### 安裝 opencommit
```shell
npm install -g opencommit
```

### 使用本地 ollama 伺服器生成提交訊息
```shell
OCO_AI_PROVIDER='ollama/gemma2:2b' opencommit
```

輸出：

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



## 錯誤碼 127

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

當 Docker 映像版本大於 `0.3.6` 時會發生此錯誤碼。因此，您需要拉取版本為 `0.3.6` 的 ollama 映像並執行該容器。請點擊 [here](https://github.com/ollama/ollama/issues/6541) 查看討論。


# 🔁 重點回顧
- Ollama 允許使用 AI 模型生成提交訊息。
- 本文詳述在 Docker 環境中設置 Ollama 的步驟。
- OpenCommit 被整合以簡化使用 AI 模型生成提交訊息的流程。
- 使用者可以透過聊天介面與 AI 模型互動。

# 🔗 參考資料
- https://ollama.com/models
- https://github.com/ollama/ollama/issues/6541
