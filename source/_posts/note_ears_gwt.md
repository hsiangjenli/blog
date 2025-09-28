---
title: '[note] 介紹簡易需求結構方法（Easy Approach to Requirements Syntax，EARS）'
date: '2025-09-19'
updated: '2025-09-19'
author:
- Hsiang-Jen Li
- ' & ChatGPT-5'
tags: null
toc: true
lang: zh-TW
slug: note-easy-approach-to-requirements-syntax-ears
---

# 📌 簡介

隨著 AI Code Assist 盛行，大家發現單純的「Vibe Coding」難以維護，Context Engineering 與傳統開發流程（BDD、TDD、SDD）開始被重新重視。本文將介紹 **EARS** 與 **GWT** 兩種簡單好用的需求撰寫模版。

<!-- more -->

# 🚀 介紹 EARS

## EARS 與 BDD 的 GWT 語句差別

|   | EARS | GWT |
| --------: | :-------- | :-------- |
| 用在  | 撰寫需求  | 描述行為 |
|著重在|講出清楚的需求|驗證需求|
|特色|強調「單句、可驗證」的需求條文|用「情境」來「驗收」測試|
|句型模板|***When*** 錯誤發生，系統 ***Shall*** 紀錄錯誤|***Given*** 系統正常運作，***When*** 錯誤發生，***Then*** 應紀錄錯誤|

- **EARS**：用句型「寫」需求
- **GWT**：用情境「驗證」需求

## EARS 常見句型

- **Ubiquitous**：需求永遠都要成立（不用加觸發或條件）
- **State-driven（While）**：在某個狀態成立時，需求必須成立
- **Event-driven（When）**：在某事件發生時，系統必須回應
- **Complex**：以上句型的組合（例如事件 + 狀態一起描述）
- **Option（Where）**：處理產品或系統的變體需求（例如不同配置、地區）

# 🔁 重點回顧

- 介紹 EARS 與 GWT 的使用場景差別

# 🔗 參考資料

- [需求工程簡介 Introduction to Requirements Engineering](https://www.mropengate.com/2015/11/software-engineering-introduction-to.html)
- [采用 EARS 方法来改进需求工程](https://zhuanlan.zhihu.com/p/652649744)
- [Introduction to EARS (Easy Approach to Requirements Syntax)](https://www.incose.org/docs/default-source/working-groups/requirements-wg/rwg_iw2022/mav_ears_incoserwg_jan22.pdf)
