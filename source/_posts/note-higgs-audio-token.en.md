---
title: '[note] Higgs-Audio Common Token Summary'
date: '2025-09-24'
updated: '2025-09-24'
author:
- Hsiang-Jen Li
- ' & ChatGPT-5'
tags:
- higgs-audio
- audiollm
toc: true
lang: en
slug: note-higgs-audio-token
source_sha: 4fefd9a05ba88a84c5046a38523c4a3dde90f7737e12bd94d3f77d090b43bd3c
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

When encountering errors while working with Higgs-Audio, I plan to carefully study the entire operation of Higgs-Audio from start to finish, so I'll start by understanding tokens. Because Higgs-Audio needs to handle both "text" and "audio" tokens simultaneously, it looks rather complicated at first, so I plan to thoroughly organize how many tokens there are.

<!-- more -->

# 🚀 Introduction to Tokens Used in Higgs-Audio

- Lowercase tokens: boundary control (start / end)
- Uppercase tokens: content replacement (replaced with actual data during preprocessing)

## Text

### Text markers
- `<|begin_of_text|>`: start of text sequence
- `<|end_of_text|>`: end of text sequence

<!--  -->
- `<|eom_id|>`: end of message
- `<|eot_id|>`: end of turn

### Message roles (System, User, Assistant)
<!--  -->
- `<|start_header_id|>`: marks the start of a message role
- `<|end_header_id|>`: marks the end of a message role

## Audio

<!--  -->
- `<|audio_bos|>`: marks the start of an input audio segment
- `<|audio_eos|>`: marks the end of an input audio segment
- `<|audio_out_bos|>`: marks the starting point of output audio tokens

<!--  -->
- `<|scene_desc_start|>`: start of recording environment/scene description
- `<|scene_desc_end|>`: end of recording environment/scene description

<!--  -->
- `<|AUDIO|>`: audio input
- `<|AUDIO_OUT|>`: discrete audio tokens

## Others

### Tools
<!--  -->
- `<|recipient|>`: tool call

### Reserved words
- `<|reserved_special_token_*|>`

### Generation style guidelines
<!--  -->
- `<|generation_instruction_start|>`: start of generation rules/style instructions
- `<|generation_instruction_end|>`: end of generation rules/style instructions

### Event-type sound effects
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

# 🔁 Recap

- Learned there are two main token categories: boundary control and content replacement
- Compiled the tokens appearing in Higgs-Audio and their uses

# 🔗 References

- [`boson-ai/higgs-audio`](https://github.com/boson-ai/higgs-audio)
