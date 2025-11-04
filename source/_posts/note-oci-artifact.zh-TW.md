---
title: '[注意] OCI 工件？'
date: '2025-05-13'
updated: '2025-05-13'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags: null
toc: true
slug: note-oci-artifact
lang: zh-TW
source_sha: 501aea97ab1076b7e73176c5432347bea4da5496cc7e0bcf112a545fa049c9f8
origin_lang: en
permalink: zh-TW/note-oci-artifact/
translations:
  en: /note-oci-artifact.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 什麼是 OCI Artifact?

**OCI Artifact** 的全名是 **Open Container Initiative Artifact**。它是一種統一的格式，可用來儲存任何內容——無論是 Docker image、Helm chart、WASM module、ML 模型、SBOM、政策或掃描報告。

<!-- more -->

# 🚀 OCI Artifact 結構

- **Tag** – 一個可讀的人類名稱（例如 `nginx:1.0`），用來指向 manifest 或 index。Tag 是版本標籤。
- **Index** – 一個 manifest 的清單，常用於多平台工件。
- **Manifest** – 描述一個工件（例如 Docker image、Helm chart）並參考 blobs。
- **Blobs** – 實際內容，例如 .tar.gz、二進位檔或工件使用的設定檔。

# 🔗 參考資料
- [OCI Image Layout Specification](https://github.com/opencontainers/image-spec/blob/v1.1.1/image-layout.md)
- [ORAS - Understanding OCI artifacts](https://oras.land/docs/concepts/artifact/)
