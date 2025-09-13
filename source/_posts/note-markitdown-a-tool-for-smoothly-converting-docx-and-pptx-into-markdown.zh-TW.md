---
title: '[note] MarkItDown：一個用於將 docx 與 pptx 順利轉換為 markdown 的工具'
date: '2024-12-13'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- python
- markdown
toc: true
translation_key: note-markitdown-a-tool-for-smoothly-converting-docx-and-pptx-into-markdown
slug: note-markitdown-a-tool-for-smoothly-converting-docx-and-pptx-into-markdown
source_sha: 397aa5750799648f289e395e4f5dca8443ea015721442d7493885bc0b35dcbb8
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> # 📌 介紹
本文討論 MarkItDown，一個專門設計用於將 docx 與 pptx 檔案輕鬆轉換成 Markdown 格式的工具。文章介紹了用於此轉換流程的各種 Python 套件，讓使用者能有效處理文件與多媒體內容。
<!-- more -->

# 🚀 快速開始

## MarkItDown 如何運作？
以下是 MarkItDown 所使用的模組

```python
dependencies = [
  "beautifulsoup4",
  "requests",
  "mammoth",
  "markdownify",
  "numpy",
  "python-pptx",
  "pandas",
  "openpyxl",
  "pdfminer.six",
  "puremagic",
  "pydub",
  "youtube-transcript-api",
  "SpeechRecognition",
  "pathvalidate",
]
```

## mammoth
- https://pypi.org/project/mammoth/
Mammoth 是一個用於將像 MS Word、Google Docs 與 LibreOffice 等文件轉換為 HTML 的工具

## python-pptx
- https://github.com/scanny/python-pptx
  一個可以建立/讀取/更新 `.pptx` 檔案的 Python 函式庫
  
## openpyxl
- https://openpyxl.readthedocs.io/en/stable/
  一個用於讀寫 Excel 2010 `xlsx`、`xlsm`、`xltx`、`xltm` 檔案的 Python 函式庫

## pdfminer
- https://github.com/pdfminer/pdfminer.six
Pdfminer.six 是一個由社群維護、從原始 PDFMiner 分支出來的版本。此模組可協助使用者從 PDF 檔案中擷取資訊。

## pydub
- https://github.com/jiaaro/pydub
  以簡單的方式讓你輕鬆操作音訊

## youtube-transcript-api
- https://github.com/jdepoix/youtube-transcript-api
  一個 Python API，可取得指定 YouTube 影片的逐字稿

## SpeechRecognition
- https://github.com/Uberi/speech_recognition/tree/master
  支援像 Google Cloud Speech API、Wit.ai、Whisper 等語音轉文字引擎

## markdownify
- https://github.com/matthewwithanm/python-markdownify
  將 HTML 轉換為 Markdown

## pathvalidate
- https://github.com/thombashi/pathvalidate
  一個用於清理與驗證字串（例如檔名、檔案路徑等）的 Python 函式庫

## puremagic
- https://github.com/cdgriffith/puremagic/tree/master
- **Puremagic 是一個檔案類型檢測工具**，可以在不依賴副檔名的情況下辨識輸入檔案的類型。由於副檔名很容易被更改，單靠它們來識別檔案類型可能有風險。該模組定義了一組規則，以讀取檔案內容並判定其類型。

```python
# puremagic/magic_data.json
{
  "extension_only": [
    ["", 0, ".txt", "text/plain", "Text File"],
    ["", 0, ".log", "text/plain", "Logger File"],
    ["", 0, ".yaml", "application/x-yaml", "YAML File"],
    ["", 0, ".yml", "application/x-yaml", "YAML File"],
    ["", 0, ".toml", "application/toml", "TOML File"],
    ["", 0, ".py", "text/x-python", "Python File"],
    ["", 0, ".pyc", "application/x-python", "Python Complied File"],
    ["", 0, ".pyd", "application/x-python", "Python Complied File"],
    ["", 0, ".python_history", "text/plain", "Python History File"],
    ["", 0, ".bat", "application/x-script", "Windows BAT file"],
    ["", 0, ".gitconfig", "text/plain", "Git Ignore File"],
...
```

# 🔁 重點回顧
- MarkItDown 允許將 docx 與 pptx 檔案順利轉換為 Markdown 格式。
- 此轉換需要各種相依套件，包括用於處理文件、音訊與資料的函式庫。
- 每個提到的函式庫都有其特定功能，例如將 Word 文件轉為 HTML 或讀取 Excel 檔案。

# 🔗 參考資料
- https://pypi.org/project/mammoth/
- https://github.com/scanny/python-pptx
- https://openpyxl.readthedocs.io/en/stable/
- https://github.com/pdfminer/pdfminer.six
- https://github.com/jiaaro/pydub
- https://github.com/jdepoix/youtube-transcript-api
- https://github.com/Uberi/speech_recognition/tree/master
- https://github.com/matthewwithanm/python-markdownify
- https://github.com/thombashi/pathvalidate
- https://github.com/cdgriffith/puremagic/tree/master
