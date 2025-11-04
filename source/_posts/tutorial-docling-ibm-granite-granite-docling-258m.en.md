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
lang: en
slug: tutorial-docling-ibm-granite-granite-docling-258m
source_sha: b2fa4b93f76d5f7df384c8790f7d9f96416b8cb670bc554b5fb55fd26146b996
origin_lang: zh-TW
permalink: tutorial-docling-ibm-granite-granite-docling-258m.en/
translations:
  zh-TW: /zh-TW/tutorial-docling-ibm-granite-granite-docling-258m/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

This demonstrates how to use the Docling document conversion tool with IBM's newly released VLM `ibm-granite/granite-docling-258M` to convert PDFs, images, and other files into structured Markdown or HTML formats for easier downstream use with LLMs.

<!-- more -->

# 🚀 Introducing the document conversion tool + Vision Language Model

## Docling

![](https://docling-project.github.io/docling/assets/docling_processing.png)

- Input: PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, VTT, images (PNG, TIFF, JPEG, ...)
- Output: a unified [DoclingDocument](https://docling-project.github.io/docling/concepts/docling_document/)
- Purpose: provide a unified and simple tool to convert various documents into a structured (LLM-Ready) format

## Vision Language Model (VLM)

This test uses IBM's newly released VLM model `ibm-granite/granite-docling-258M`. Compared to the older `ds4sd/SmolDocling-256M-preview`, with nearly the same number of parameters, the model size was reduced from 3.55 GB to 530 MB.

### VLM used by the older Docling
![image](https://hackmd.io/_uploads/rk4ayQ-hlx.png)

### VLM used by the new Docling
![image](https://hackmd.io/_uploads/HJU0JQb2xg.png)

## Practical steps

- Docling + `ibm-granite/granite-docling-258M`

```shell
uv add docling 
uv add mlx-vlm # I use a Mac; install only if you need acceleration with M-series chips
```

### Supported VLM models

- Old: `vlm_model_specs.SMOLDOCLING_MLX`
- New: `vlm_model_specs.GRANITEDOCLING_MLX`

### Module overview

- `VlmPipelineOptions`: configuration for using a VLM for document conversion (e.g., model name, saving images, etc.)
- `DocumentConverter`: configures processing methods for different input formats

### Image handling modes

```python
class ImageRefMode(str, Enum):
    """ImageRefMode."""

    PLACEHOLDER = "placeholder"  # just a place-holder
    EMBEDDED = "embedded"  # embed the image as a base64
    REFERENCED = "referenced"  # reference the image via uri
```

- `PLACEHOLDER`: use `<!-- IMAGE -->` to represent images (does not save the image)
- `EMBEDDED`: convert the image to base64 and store it directly in the converted document
- `REFERENCED`: reference the image via a URI

### Full code

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

# 🔁 Key takeaways

- Install docling and use the latest model `ibm-granite/granite-docling-258M` for recognition
- On Macs with M-series chips you can additionally install `mlx-vlm` and choose models that support acceleration
- Two output modes: export directly to Markdown or HTML

# 🔗 References

- [Docling/Vision models](https://docling-project.github.io/docling/usage/vision_models/)
- [Docling/Usage/Basic-usage](https://docling-project.github.io/docling/usage/)
