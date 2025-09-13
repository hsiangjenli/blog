---
title: '[備註] OCI Artifact？'
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

# 📌 什麼是 OCI Artifact？

OCI Artifact 的全名是 **Open Container Initiative Artifact**。它是一種統一的格式，可用來儲存任何東西 — 無論是 Docker 映像、Helm chart、WASM 模組、機器學習模型 (ML model)、SBOM、政策或掃描報告。

最重要的是，任何遵循 OCI 格式的項目都可以上傳到或從註冊中心（例如 Harbor、DockerHub、Artifact Hub）下載。

<!-- more -->

# 🚀 OCI Artifact 結構

- **Tag** – 一個人可讀的名稱（例如 `nginx:1.0`），指向一個 manifest 或 index。Tag 是版本標籤。
- **Index** – 一個 manifest 的列表，通常用於跨平台的 artifact。
- **Manifest** – 描述一個 artifact（例如 Docker 映像、Helm chart），並參考 blobs。
- **Blobs** – 實際內容，如 .tar.gz、二進位檔或 artifact 使用的設定檔。


# 🔗 參考資料
- [OCI 映像佈局規範](https://github.com/opencontainers/image-spec/blob/v1.1.1/image-layout.md)
- [ORAS — 了解 OCI 產物](https://oras.land/docs/concepts/artifact/)
