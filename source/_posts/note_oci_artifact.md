---
title: '[note] OCI Artifact?'
date: '2025-05-13'
updated: '2025-05-13'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags: null
toc: true
slug: note-oci-artifact
lang: en
---

# 📌 What is an OCI Artifact?

The full name of **OCI Artifact** is **Open Container Initiative Artifact**. It is a unified format that can be used to store anything — whether it's a Docker image, Helm chart, WASM module, ML model, SBOM, policy, or scan report.

Most importantly, anything that follows the OCI format can be uploaded to or downloaded from a registry (e.g., Harbor, DockerHub, Artifact Hub).

<!-- more -->

# 🚀 OCI Artifact Structure

- **Tag** – A human-readable name (e.g., `nginx:1.0`) that points to a manifest or index. Tags are version labels.
- **Index** – A list of manifests, often used for multi-platform artifacts.
- **Manifest** – Describes an artifact (e.g., Docker image, Helm chart) and references blobs.
- **Blobs** – Actual content like .tar.gz, binaries, or configs used by the artifact.


# 🔗 References
- [OCI Image Layout Specification](https://github.com/opencontainers/image-spec/blob/v1.1.1/image-layout.md)
- [ORAS - Understanding OCI artifacts](https://oras.land/docs/concepts/artifact/)
