---
title: "[note] MarkItDown: A tool for smoothly converting docx and pptx into markdown"
date: 2024-12-13
tags: python, markdown
toc: true
---

## How MarkItDown works?

- Down below are the module use for MarkItDown

<!-- more -->

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
Mammoth is a tool designed for converting documents like MS Word, Google Docs, and LibreOffice files into HTML

## python-pptx
- https://github.com/scanny/python-pptx
  A Python library that can create/read/update `.pptx` file
  
## openpyxl
- https://openpyxl.readthedocs.io/en/stable/
  A Python library to read/write Excel 2010 `xlsx` `xlsm` `xltx` `xltm` file

## pdfminer
- https://github.com/pdfminer/pdfminer.six
Pdfminer.six is a community-maintained version that was forked from original PDFMiner. This module helps users extract information from PDF files.

## pydub
- https://github.com/jiaaro/pydub
  Make it easy for you to manipulate audio in a simple way

## youtube-transcript-api
- https://github.com/jdepoix/youtube-transcript-api
  A Python API allows you to get the transcript for a given YouTube video

## SpeechRecognition
- https://github.com/Uberi/speech_recognition/tree/master
  Support for speech-to-text engines like Google Cloud Speech API, Wit.ai, Whisper, etc

## markdownify
- https://github.com/matthewwithanm/python-markdownify
  Convert HTML file into Markdown

## pathvalidate
- https://github.com/thombashi/pathvalidate
  A Python library to sanitize and validate strings such as filenames, file paths, etc

## puremagic
- https://github.com/cdgriffith/puremagic/tree/master
- Puremagic is a **file type detection tool** that can identify the type of an input file without relying on its extension. Since file extensions can be easily changed, using them alone to identify file type can be risky. This module defines a set of rules to read the file content and determine its type.

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



