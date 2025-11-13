---
title: '[note] Introduction to SBOM, AIBOM and Their Tools'
date: '2025-11-05'
updated: '2025-11-05'
author:
- Hsiang-Jen Li
- ' & DeepWiki'
- ' & GPT-5 Search'
tags:
- ai
- security
toc: true
lang: en
slug: note-sbom-aibom
source_sha: 2e41988de2f49f4497c47e962607dd49b54e8af14f24266a5810c1b193e79510
origin_lang: zh-TW
permalink: note-sbom-aibom.en/
translations:
  zh-TW: /zh-TW/note-sbom-aibom/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

This article introduces the Software Bill of Materials (SBOM) and its application in the AI domain, AIBOM. It briefly presents three common SBOM standard formats: SPDX, CycloneDX, and SWID. While introducing AIBOM, it explains the differences between AIBOM and Model Cards, and presents the open-source tool `aetheris-ai/aibom-generator`, which can extract model information from Hugging Face and perform scoring.

<!-- more -->

# 🚀 Introducing BOMs and Their Tools

## What is a BOM?

First, let's introduce what a BOM (Bill of Materials) is. The concept originates from manufacturing and is a document that records all components, parts, raw materials used in a product and related information (such as quantity, specifications, and identifiers). It is a core source for product structure, production management, and cost accounting.

### What kinds of BOMs exist?


![CycloneDX Capabilities](https://hackmd.io/_uploads/r1l0tkD1bl.png)

> See [CycloneDX's website](https://cyclonedx.org/capabilities/sbom/)

### SBOM

A Software Bill of Materials (SBOM) is a detailed list of all components in software (including open source, third-party, and proprietary software). Its purpose is to provide a complete view of software composition, track software components, versions, licensing information, and potential vulnerabilities. SBOMs can be used to strengthen software supply chain security and to quickly locate and remediate issues when security incidents occur.

#### Common SBOM formats

- SPDX (Software Package Data Exchange) --> Recommended 👍
- CycloneDX (Cyclone Data Exchange) --> Recommended 👍
- SWID (Software Identification)

|   |SPDX|CycloneDX|SWID|
|---|----|---------|----|
|Maintainer|Linux Foundation|OWASP|ISO/IEC|
|International Standard|ISO/IEC 5962:2021|Included as one of NTIA's minimal elements interoperability supported formats|ISO/IEC 19770‑2:2015|
|Advantages|Highest license transparency, can go down to file-level, most mature ecosystem and most documentation|Lightweight, concise, fast, and can integrate tightly with security tools (VEX)|Provides unique product identification, enabling precise software inventory and license reconciliation in asset management systems (ITAM)|
|Disadvantages|Format can be large and complex; requires additional tools to handle its complex structure|Fast, but when handling complex proprietary/custom licensing terms it may not be as comprehensive as SPDX|Coarser identification granularity; mainly provides "what version this is" rather than detailed listing of "which subcomponents it contains"|

#### SBOM's friend: VEX

VEX stands for Vulnerability Exploitability eXchange. Traditional scanning tools tell you what vulnerabilities exist, but not whether that vulnerability is exploitable in this particular codebase (reducing false positives and improving vulnerability reporting efficiency).

- OpenVEX
- CSAF VEX
- CycloneDX VEX

## AIBOM

> Model Card? ML-BOM? AI-BOM? What's the difference?

- **Model Card**: A documentation for AI/ML models emphasizing performance, intended use, and limitations (more like a model manual).
- **AI‑BOM/ML‑BOM**: A "bill of materials" for AI/ML systems listing materials (datasets, models, third-party components, open-source packages, hardware, etc.), emphasizing traceability and supply chain (more like a composition inventory).

## `aetheris-ai/aibom-generator`

### Core Features

- Supports Web and API interfaces
- Automatically extracts various metadata from Hugging Face
- Standard SBOM format (uses CycloneDX 1.6)
- Supports Model Card, Dataset, Evaluation Metrics

### Supported Fields

| Strategy | Core Description | Confidence Level | Example Extracted Fields |
| :--- | :--- | :--- | :--- |
| **Hugging Face API Extraction (HuggingFace API Extraction)** | Maps fields directly from API responses. | High, structured data | `name`, `author`, `license`, `tags`, etc. |
| **Model Card Extraction (Model Card Extraction)** | Parses structured model card YAML | Medium-high | `limitation`, `metrics`, `datasets`, etc. |
| **Configuration File Extraction (Configuration File Extraction)** | Extracts model details from configuration files | High | `typeOfModel`, `hyperparameter`, etc. |
| **Text Pattern Extraction (Text Pattern Extraction)** | Uses Regex to extract from README content | Medium (requires validation) | `safetyRiskAssessment`, `informationAboutTraining`, etc. |
| **Intelligent Inference (Intelligent Inference)** | Uses defaults based on model characteristics | Medium (context-dependent) | `primaryPurpose`, `domain`, etc. |
| **Fallback Values (Fallback Values)** | Uses fallback values when no data is available to maintain structural integrity | Low/None | Ensures SBOM structure integrity |

### Scoring Method

#### Scoring Categories

| Category                                  | Number of Fields | Max Points | Weight | Description                      |
|:------------------------------------- | ------ | -------- | ---- | ------------------------- |
| **Required Fields**        | 4      | 20       | 20%  | CycloneDX required fields        |
| **Metadata**               | 5      | 20       | 20%  | AI metadata and provenance info |
| **Component Basic**        | 5      | 20       | 20%  | Core component identification info        |
| **Component Model Card** | 14     | 30       | 30%  | AI model documentation               |
| **External References**    | 1      | 10       | 10%  | Model version and external links        |


#### Field Tiers

- Critical fields
- Important fields
- Supplementary fields

Each field has different tiers, weights, and points. Detailed information can be found in [`HF_files/aibom-generator/src/aibom-generator/field_registry.json`](https://github.com/aetheris-ai/aibom-generator/blob/7e13fbd5e0d169c9b16e7a26b9e9d5db3eb1e0ce/HF_files/aibom-generator/src/aibom-generator/field_registry.json), which maps each field's tier, weight, and points. For example, the JSON file below:

```json
  "fields": {
    "bomFormat": {
      "tier": "critical",
      "weight": 4.0,
      "category": "required_fields",
      "description": "Format identifier for the SBOM",
      "jsonpath": "$.bomFormat",
      "aibom_generation": {
        "location": "$.bomFormat",
        "rule": "always_include",
        "source_fields": ["bomFormat"],
        "validation": "required",
        "data_type": "string"
      },
      "scoring": {
        "points": 4.0,
        "required_for_profiles": ["basic", "standard", "advanced"],
        "category_contribution": 0.2
      },
      "validation_message": {
        "missing": "Missing critical field: bomFormat - essential for SBOM identification",
        "recommendation": "Ensure bomFormat is set to 'CycloneDX'"
      }
    },
    "modelExplainability": {
      "tier": "supplementary",
      "weight": 1.0,
      "category": "component_model_card",
      "description": "Information about model explainability",
      "jsonpath": "$.metadata.properties[?(@.name=='modelExplainability')].value",
      "aibom_generation": {
        "location": "$.metadata.properties",
        "rule": "include_if_available",
        "source_fields": ["modelExplainability", "explainability", "interpretability"],
        "validation": "optional",
        "data_type": "string"
      },
      "scoring": {
        "points": 1.0,
        "required_for_profiles": ["advanced"],
        "category_contribution": 0.033
      },
      "validation_message": {
        "missing": "Missing supplementary field: modelExplainability - explainability information helpful for transparency",
        "recommendation": "Add information about model explainability or interpretability features"
      }
    },
```

# 🔁 Key Takeaways

- Introduced the concept of BOMs, the commonly used SBOM in the software industry, and its extended application AIBOM
- Reviewed the three mainstream SBOM standard formats: SPDX, CycloneDX, and SWID
- In addition to SBOM, introduced VEX formats that can effectively reduce vulnerability false positives and improve vulnerability management efficiency
- Explained the concept of AIBOM and distinguished the differences and positioning between AIBOM and Model Cards
- Introduced features, extracted fields, and scoring mechanisms of the AIBOM tool `aetheris-ai/aibom-generator`

# 🔗 References

- [From Model Cards to ML-BOM](https://www.ithome.com.tw/article/171180)
- [CycloneDX - Machine Learning Bill of Materials (ML-BOM)](https://cyclonedx.org/capabilities/mlbom/)
- [AI Learning Journey Series - Day 12 Vulnerability Management and Patching × SBOM and Supply Chain Security](https://ithelp.ithome.com.tw/articles/10388012)
- [Six common myths when enterprises adopt SBOM software bills of materials](https://www.ithome.com.tw/news/164109)
- [Is the software supply chain really secure? Learn how to use OPSWAT's powerful SBOM solution to protect software supply chain security](https://traditional-chinese.opswat.com/blog/sbom-formats)
