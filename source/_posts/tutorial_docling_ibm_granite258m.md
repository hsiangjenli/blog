---
title: '[tutorial] Docling + ibm-granite/granite-docling-258M'
date: '2025-09-23'
updated: '2025-09-23'
author:
- Hsiang-Jen Li
tags:
- vlm
- python
toc: true
lang: zh-TW
slug: tutorial-docling-ibm-granite-granite-docling-258m
permalink: zh-TW/tutorial-docling-ibm-granite-granite-docling-258m/
translations:
  en: /tutorial-docling-ibm-granite-granite-docling-258m.en/
---

# 📌 簡介

示範如何使用 Docling 文件轉換工具與 IBM 最新推出的 `ibm-granite/granite-docling-258M` VLM，將 PDF、Image 等檔案轉換成結構化的 Markdown 或 HTML 格式，方便後續搭配 LLM 使用

<!-- more -->

# 🚀 介紹文件轉換工具 + 視覺語言模型

## Docling

![](https://docling-project.github.io/docling/assets/docling_processing.png)

- 輸入：PDF、DOCX、PPTX、XLSX、HTML、WAV、MP3、VTT、images（PNG, TIFF, JPEG, ...）
- 輸出：統一的 [DoclingDocument](https://docling-project.github.io/docling/concepts/docling_document/)
- 目的：提供一個統一且簡單的工具，把各種文件轉換成結構化格式（LLM-Ready Format）

## 視覺語言模型（Vision Language Model, VLM）

本次實測 IBM 最新推出的 VLM 模型 `ibm-granite/granite-docling-258M`，相較於舊版的 `ds4sd/SmolDocling-256M-preview`，兩者參數量幾乎一樣的情況下，模型體積從 3.55 GB 降到 530 MB

### 舊版 Docling 使用的 VLM
![image](https://hackmd.io/_uploads/rk4ayQ-hlx.png)

### 新版 Docling 使用的 VLM
![image](https://hackmd.io/_uploads/HJU0JQb2xg.png)

## 實際操作 

- Docling + `ibm-granite/granite-docling-258M`

```shell
uv add docling 
uv add mlx-vlm # 筆者使用 Mac，要使用 M 系列晶片加速才需要裝
```

### 支援的 VLM 模型

- 舊版：`vlm_model_specs.SMOLDOCLING_MLX`
- 新版：`vlm_model_specs.GRANITEDOCLING_MLX`

### 模組介紹

- `VlmPipelineOptions`：使用 VLM 進行文件轉換的設定檔（例如：模型名稱、保存圖片等等...）
- `DocumentConverter`：設定不同 Input Format 的處理方式

### 圖片處理方式

```python
class ImageRefMode(str, Enum):
    """ImageRefMode."""

    PLACEHOLDER = "placeholder"  # just a place-holder
    EMBEDDED = "embedded"  # embed the image as a base64
    REFERENCED = "referenced"  # reference the image via uri
```

- `PLACEHOLDER`：使用 `<!-- IMAGE -->` 來代表圖片（不保存圖片的意思）
- `EMBEDDED`：把圖片轉換成 base64，直接保存在轉換後的文件內 
- `REFERENCED`：使用 URI 引用圖片

### 完整程式碼

```python
from pathlib import Path
from docling.datamodel.base_models import InputFormat
from docling.document_converter import (
    DocumentConverter,
    ImageFormatOption,
    PdfFormatOption,
)
from docling.pipeline.vlm_pipeline import VlmPipeline
from docling.datamodel.pipeline_options import VlmPipelineOptions
from docling.datamodel import vlm_model_specs
from docling_core.types.doc import ImageRefMode

import os

model = vlm_model_specs.GRANITEDOCLING_MLX

vlm_pipeline_options = VlmPipelineOptions(
    vlm_options=model,
    generate_page_images=True,
    generate_picture_images=False,
    images_scale=2.0,
    do_picture_description=True,
)

converter = DocumentConverter(
    format_options={
        InputFormat.IMAGE: ImageFormatOption(
            pipeline_cls=VlmPipeline,
            pipeline_options=vlm_pipeline_options,
        ),
        InputFormat.PDF: PdfFormatOption(
            pipeline_cls=VlmPipeline,
            pipeline_options=vlm_pipeline_options,
        ),
    }
)

FILE_PATHS = os.listdir("data/raw/")

output_dir = Path(f"data/output/{model.repo_id.replace('/', '_')}")
output_dir.mkdir(parents=True, exist_ok=True)

for file_path in FILE_PATHS:
    input_file_path = Path(f"data/raw/{file_path}")
    output_file_path = output_dir / f"{input_file_path.stem}.md"
    
    doc = converter.convert(source=input_file_path, raises_on_error=True).document
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(doc.export_to_markdown(image_mode=ImageRefMode.EMBEDDED))

    with open(output_file_path.with_suffix(".html"), "w", encoding="utf-8") as f:
        f.write(
            doc.export_to_html(image_mode=ImageRefMode.EMBEDDED, split_page_view=True)
        )
```

# 🔁 重點回顧

- 安裝 docling 以及使用最新的模型 `ibm-granite/granite-docling-258M` 進行辨識
- 使用 Mac 的 M 系列晶片可額外安裝 `mlx-vlm`，並挑選可以加速的模型
- 兩種輸出模式（直接匯出成 Markdown 或是 HTML）

# 🔗 參考資料

- [Docling/Vision models](https://docling-project.github.io/docling/usage/vision_models/)
- [Docling/Usage/Basic-usage](https://docling-project.github.io/docling/usage/)
