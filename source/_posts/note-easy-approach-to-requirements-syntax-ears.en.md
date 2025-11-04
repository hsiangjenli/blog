---
title: '[note] Introduction to the Easy Approach to Requirements Syntax (EARS)'
date: '2025-09-19'
updated: '2025-09-19'
author:
- Hsiang-Jen Li
- ' & ChatGPT-5'
tags: null
toc: true
lang: en
slug: note-easy-approach-to-requirements-syntax-ears
source_sha: a55227dcc8cdbedd593e06f0db720d5b88da79ae3624f1981ddcda411418f397
origin_lang: zh-TW
permalink: note-easy-approach-to-requirements-syntax-ears.en/
translations:
  zh-TW: /zh-TW/note-easy-approach-to-requirements-syntax-ears/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

With the rise of AI Code Assist, many have found that pure "vibe coding" is hard to maintain, and Context Engineering along with traditional development processes (BDD, TDD, SDD) are being re-emphasized. This article introduces two simple and useful requirement writing templates: **EARS** and **GWT**.

<!-- more -->

# 🚀 Introduction to EARS

## Differences between EARS and BDD's GWT statements

|   | EARS | GWT |
| --------: | :-------- | :-------- |
| Used for  | writing requirements  | describing behavior |
| Focuses on | stating clear requirements | verifying requirements |
| Characteristics | emphasizes single-sentence, verifiable requirement statements | uses "scenarios" for acceptance testing |
| Sentence template | ***When*** an error occurs, the system ***Shall*** record the error | ***Given*** the system is operating normally, ***When*** an error occurs, ***Then*** it should record the error |

- **EARS**: use sentence templates to 'write' requirements
- **GWT**: use scenarios to 'verify' requirements

## Common EARS sentence types

- **Ubiquitous**: the requirement must always hold (no trigger or condition needed)
- **State-driven (While)**: the requirement must hold while a certain state is true
- **Event-driven (When)**: the system must respond when an event occurs
- **Complex**: a combination of the above patterns (e.g., event + state together)
- **Option (Where)**: handles variant requirements of the product or system (e.g., different configurations, regions)

# 🔁 Key takeaways

- Highlights the difference in use cases between EARS and GWT

# 🔗 References

- [Introduction to Requirements Engineering](https://www.mropengate.com/2015/11/software-engineering-introduction-to.html)
- [Using the EARS method to improve requirements engineering](https://zhuanlan.zhihu.com/p/652649744)
- [Introduction to EARS (Easy Approach to Requirements Syntax)](https://www.incose.org/docs/default-source/working-groups/requirements-wg/rwg_iw2022/mav_ears_incoserwg_jan22.pdf)
