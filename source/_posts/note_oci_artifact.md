---
title: '[note] OCI Artifact?'
date: '2025-05-13'
lang: en
updated: '2025-05-13'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags: null
toc: true
translation_key: note-oci-artifact
slug: note-oci-artifact
source_sha: 94abfe8913c31ecbb82f4acd0b50186fef86014e91b547b15b1631403b47f3cb
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 What is an OCI Artifact?

"**OCI Artifact**" stands for "**Open Container Initiative Artifact**." It is a unified format that can be used to store anything — whether Docker images, Helm charts, WASM modules, machine learning models, SBOMs, policies, or scan reports.

Most importantly, any item that follows the OCI format can be uploaded to or downloaded from registries (for example Harbor, DockerHub, Artifact Hub).

<!-- more -->

# 🚀 OCI Artifact Structure

- **Tag** – A human-readable name (for example `nginx:1.0`) that points to a manifest or index. A tag is a version label.
- **Index** – A list of manifests, commonly used for multi-platform artifacts.
- **Manifest** – Describes an artifact (e.g., Docker image, Helm chart) and references blobs.
- **Blobs** – The actual content, such as .tar.gz, binaries, or configuration files used by the artifact.


# 🔗 References
- [OCI Image Layout Specification](https://github.com/opencontainers/image-spec/blob/v1.1.1/image-layout.md)
- [ORAS - Learn about OCI artifacts](https://oras.land/docs/concepts/artifact/)
