---
title: '[note] OCI 工件？'
date: '2025-05-13'
lang: zh-TW
updated: '2025-05-13'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags: null
toc: true
translation_key: note-oci-artifact
slug: note-oci-artifact
source_sha: 501aea97ab1076b7e73176c5432347bea4da5496cc7e0bcf112a545fa049c9f8
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> # 📌 什麼是 OCI 工件？

「**OCI Artifact**」的全名是「**Open Container Initiative Artifact**」。它是一種統一格式，可用來儲存任何東西 — 無論是 Docker 映像、Helm 圖表、WASM 模組、機器學習模型、SBOM、政策，或掃描報告。

最重要的是，任何遵循 OCI 格式的項目都可以上傳到或從註冊中心下載（例如 Harbor、DockerHub、Artifact Hub）。

<!-- more -->

# 🚀 OCI 工件結構

- **Tag** – 可讀的人類名稱（例如 `nginx:1.0`），指向 manifest 或 index。Tag 是版本標籤。
- **Index** – manifest 的清單，常用於多平台工件。
- **Manifest** – 描述一個工件（例如 Docker 映像、Helm 圖表），並參考 blobs。
- **Blobs** – 實際內容，例如 .tar.gz、二進位檔或用於工件的設定檔。


# 🔗 參考資料
- [OCI 映像佈局規範](https://github.com/opencontainers/image-spec/blob/v1.1.1/image-layout.md)
- [ORAS - 了解 OCI 工件](https://oras.land/docs/concepts/artifact/)
