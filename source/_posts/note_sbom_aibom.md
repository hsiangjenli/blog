---
title: '[note] 介紹 SBOM、AIBOM 及其工具'
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
lang: zh-TW
slug: note-sbom-aibom
permalink: zh-TW/note-sbom-aibom/
translations:
  en: /note-sbom-aibom.en/
---

# 📌 簡介

本篇文章介紹了軟體物料清單（SBOM）及其在 AI 領域的應用 AIBOM。簡單介紹三種常見的 SBOM 標準格式：SPDX、CycloneDX 和 SWID。在介紹 AIBOM 的同時，解釋 AIBOM 與 Model Card 的差異，並介紹開源工具 `aetheris-ai/aibom-generator`，該工具可用來萃取在 Hugging Face 上的模型資訊並進行評分

<!-- more -->

# 🚀 介紹 BOM 及其工具

## BOM 表是什麼？

首先，先介紹何謂 BOM 表（Bill of Materials，物料清單）。此概念源自於製造業，是記載產品所使用的所有組件、零件、原料及其相關資訊（如數量、規格、編號）的文件，是產品結構、生產管理與成本核算的核心來源

### 有哪些 BOM 表？


![CycloneDX Capabilities](https://hackmd.io/_uploads/r1l0tkD1bl.png)

> 可參考 [CycloneDX 的網站](https://cyclonedx.org/capabilities/sbom/)

### SBOM

軟體物料清單（Software Bill of Materials，SBOM），一份詳細列出軟體中所有元件（包括開源、第三方和專屬軟體）的清單，目的是希望可以完整的查看軟體的組成份，追蹤軟體元件、版本、授權資訊、潛在漏洞。可以使用 SBOM 來加強軟體供應鏈的安全，並在發生安全事件的時候可以快速定位、修復問題

#### 常見的 SBOM 格式

- SPDX（Software Package Data Exchange）--> 推薦 👍
- CycloneDX（Cyclone Data Exchange）--> 推薦 👍
- SWID（Software Identification）

|   |SPDX|CycloneDX|SWID|
|---|----|---------|----|
|維護組織|Linux Foundation|OWASP|ISO/IEC|
|國際標準|ISO/IEC 5962:2021|列入 NTIA 最小要素互通支援格式之一|ISO/IEC 19770‑2:2015|
|優點|授權透明度最高，可深入到檔案層級，生態系統最成熟、文件最豐富|輕量、簡潔、快速，且可以與安全工具整合緊密（VEX）|擁有產品唯一識別功能，可在資產管理系統（ITAM）進行精確的軟體盤點與授權比對|
|缺點|格式較龐大、複雜度高，需要額外的工具來處理其複雜結構|快速，但在處理複雜的專有/客製化授權條款時，可能不如 SPDX 全面|識別粒度較粗，主要提供「這是什麼版本」，而不提供「它包含哪些子組件」的詳細清單|

#### SBOM 的好朋友 VEX

VEX 全名為 Vulnerability Exploitability eXchange，過往的掃描工具會告訴有什麼漏洞，但是不會告訴你這個漏洞在這組程式中是否會發生/利用（降低誤報並提高漏洞通報的效率）。

- OpenVEX
- CSAF VEX
- CycloneDX VEX

## AIBOM

> Model Card？ML-BOM？AI-BOM？差在哪裡？

- **Model Card**：AI/ML 模型的說明文件，強調性能、用途與限制（偏向模型說明書）
- **AI‑BOM/ML‑BOM**：把 AI/ML 系統的「**材料清單**」（資料集、模型、第三方元件、開源套件、硬體等），強調可追蹤性與供應鏈（偏向統構成清單）

## `aetheris-ai/aibom-generator`

### 核心功能

- 支援 Web 與 API 介面
- 自動從 Hugging Face 提取各種元數據
- 標準 SBOM 格式（使用 CycloneDX 1.6）
- 同時支援 Model Card、Dataset、Evaluation Metrics

### 支援欄位

| 策略 | 核心描述 | 信心等級 | 抽取欄位範例 |
| :--- | :--- | :--- | :--- |
| **Hugging Face API 抽取（HuggingFace API Extraction）** | 直接從 API 回應中進行欄位映射。 | 高，結構化資料 | `name`、`author`、`license`、`tags` 等等 |
| **模型卡抽取（Model Card Extraction）** | 解析結構化的模型卡 YAML | 中高 | `limitation`、`metrics`、`datasets` 等等 |
| **設定檔抽取（Configuration File Extraction）** | 從設定檔案中挖掘模型細節 | 高 | `typeOfModel`、`hyperparameter` 等等 |
| **文字模式抽取（Text Pattern Extraction）** | 使用 Regex 從 README 內容中進行提取 | 中（需要驗證） | `safetyRiskAssessment`、`informationAboutTraining` 等等 |
| **智慧推論（Intelligent Inference）** | 根據模型特性使用預設值 | 中（依賴上下文） | `primaryPurpose`、`domain` 等等 |
| **預留值（Fallback Values）** | 沒有可用資料時，使用預留值以維持結構完整性 | 低、無 | 確保 SBOM 結構完整性 |

### 評分方式

#### 評分類別

| 類別                                  | 欄位數 | 最高分數 | 權重 | 說明                      |
|:------------------------------------- | ------ | -------- | ---- | ------------------------- |
| **必要欄位 (Required Fields)**        | 4      | 20       | 20%  | CycloneDX 必要欄位        |
| **中繼資料 (Metadata)**               | 5      | 20       | 20%  | AI 的 metadata 與溯源資訊 |
| **組件基礎 (Component Basic)**        | 5      | 20       | 20%  | 核心元件的識別資訊        |
| **組件模型卡 (Component Model Card)** | 14     | 30       | 30%  | AI 模型文件               |
| **外部參考 (External References)**    | 1      | 10       | 10%  | 模型版本與外部連結        |


#### 欄位分級

- 關鍵欄位 (Critical fields)
- 重要欄位 (Important fields)
- 補充欄位 (Supplementary fields)

每個欄位有不同的分級、權重以及分數，詳細資訊可以在 [`HF_files/aibom-generator/src/aibom-generator/field_registry.json`](https://github.com/aetheris-ai/aibom-generator/blob/7e13fbd5e0d169c9b16e7a26b9e9d5db3eb1e0ce/HF_files/aibom-generator/src/aibom-generator/field_registry.json) 找到每個欄位對應的分級、權重、分數，像是下面的 json 檔案：

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

# 🔁 重點回顧

- 介紹 BOM 表的概念，以及軟體產業中常用的 SBOM 及其延伸應用 AIBOM
- 了解目前主流的三種 SBOM 標準格式：SPDX、CycloneDX 與 SWID
- 除了 SBOM，還介紹了 VEX 格式，能有效降低漏洞誤報率，提升漏洞管理效率
- 說明 AIBOM 的概念，並區分 AIBOM 與 Model Card 之間的差異與定位
- 簡介 AIBOM 工具 `aetheris-ai/aibom-generator` 的特色、抽取欄位與評分機制

# 🔗 參考資料

- [從模型卡到ML-BOM](https://www.ithome.com.tw/article/171180)
- [CycloneDX - Machine Learning Bill of Materials (ML-BOM)](https://cyclonedx.org/capabilities/mlbom/)
- [AI學習之旅系列 - Day 12 漏洞管理與修補大作戰 × SBOM 與供應鏈安全](https://ithelp.ithome.com.tw/articles/10388012)
- [企業導入SBOM軟體物料清單有六大常見迷思的考驗](https://www.ithome.com.tw/news/164109)
- [軟體供應鏈真的安全嗎？瞭解如何利用OPSWAT強大的 SBOM 解決方案保護軟體供應鏈安全](https://traditional-chinese.opswat.com/blog/sbom-formats)
