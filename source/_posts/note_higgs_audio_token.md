---
title: '[note] Higgs-Audio 常用 token 彙整'
date: '2025-09-24'
updated: '2025-09-24'
author:
- Hsiang-Jen Li
- ' & ChatGPT-5'
tags:
- higgs-audio
- audiollm
toc: true
lang: zh-TW
slug: note-higgs-audio-token
permalink: zh-TW/note-higgs-audio-token/
translations:
  en: /note-higgs-audio-token.en/
---

# 📌 簡介

在操作 Higgs-Audio 的時候遇到錯誤，打算從頭到尾好好認真研究 Higgs-Audio 的整個運作過程，所以打算先從 token 開始了解，因為在 Higgs-Audio 內需要同時處理「文字」以及「音訊」兩種 token，初次看頗為複雜，打算好好整理裡面有多少 token。

<!-- more -->

# 🚀 介紹 Higgs-Audio 內使用到的 Token

- 小寫 token：邊界控制（開始 / 結束）
- 大寫 token：內容替換（前處理時會替換成實際資料）

## 文字

### 文字標記
- `<|begin_of_text|>`：文字序列開頭
- `<|end_of_text|>`：文字序列結束

<!--  -->
- `<|eom_id|>`：訊息結束
- `<|eot_id|>`：回合結束

### 訊息角色（System、User、Assistant）
<!--  -->
- `<|start_header_id|>`：界定一段訊息的角色開始
- `<|end_header_id|>`：界定一段訊息的角色結束

## 音訊

<!--  -->
- `<|audio_bos|>`：標示輸入音訊片段的開始
- `<|audio_eos|>`：標示輸入音訊片段的結束
- `<|audio_out_bos|>`：標示輸出音訊 token 的起點

<!--  -->
- `<|scene_desc_start|>`：錄音環境／場景描述開始
- `<|scene_desc_end|>`：錄音環境／場景描述節結束

<!--  -->
- `<|AUDIO|>`：音訊輸入
- `<|AUDIO_OUT|>`：離散音訊 token

## 其它

### 工具
<!--  -->
- `<|recipient|>`：工具呼叫

### 保留字
- `<|reserved_special_token_*|>`

### 生成風格規範
<!--  -->
- `<|generation_instruction_start|>`：生成規則／風格等指示開始
- `<|generation_instruction_end|>`：生成規則／風格等指示結束

### 事件類音效
<!--  -->
- `<SE>`
- `<SE_s>`
- `<SE_e>`

```python
for tag, replacement in [
    ("[laugh]", "<SE>[Laughter]</SE>"),
    ("[humming start]", "<SE_s>[Humming]</SE_s>"),
    ("[humming end]", "<SE_e>[Humming]</SE_e>"),
    ("[music start]", "<SE_s>[Music]</SE_s>"),
    ("[music end]", "<SE_e>[Music]</SE_e>"),
    ("[music]", "<SE>[Music]</SE>"),
    ("[sing start]", "<SE_s>[Singing]</SE_s>"),
    ("[sing end]", "<SE_e>[Singing]</SE_e>"),
    ("[applause]", "<SE>[Applause]</SE>"),
    ("[cheering]", "<SE>[Cheering]</SE>"),
    ("[cough]", "<SE>[Cough]</SE>"),
]:
```

# 🔁 重點回顧

- 了解到 Token 兩大分類：邊界控制、內容替換
- 整理在 Higgs-Audio 出現的 Token 以及其用處

# 🔗 參考資料

- [`boson-ai/higgs-audio`](https://github.com/boson-ai/higgs-audio)
