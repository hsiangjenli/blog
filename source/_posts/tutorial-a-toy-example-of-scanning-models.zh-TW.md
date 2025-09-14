---
title: '[教學] 掃描模型的簡單範例'
date: '2025-06-14'
updated: '2025-06-14'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags:
- mlsecops
toc: true
slug: tutorial-a-toy-example-of-scanning-models
lang: zh-TW
source_sha: c71699f8d0ad067977a553f06e68c9509578fe87abcefa4f28d09ea89fc263ae
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹

本文示範如何使用一個簡單的範例與 `modelscan` 工具來偵測不安全的 PyTorch 模型。

<!-- more -->

# 🚀 快速開始

> 開始之前，您需要安裝以下套件

```shell
pip install numpy torch modelscan
```

## 準備安全模型

```python
from torch import nn
import torch

class SafeModel(nn.Module):

    def __init__(self):
        super(SafeModel, self).__init__()
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)
    
if __name__ == "__main__":
    model = SafeModel()

    # save the model
    torch.save(model.state_dict(), "safe_model.pth")
```

## 準備惡意模型

這是一個在載入時會產生輸出的惡意模型。

```python
from torch import nn
import torch
import os

class MaliciousModel:

    def __reduce__(self):
        print("Reduce called!")  # 應該會印出
        return (os.system, ("echo 'This is a malicious model!' > malicious_output.txt",))
    
if __name__ == "__main__":
    model = MaliciousModel()

    # save the model
    torch.save(model, "malicious_model.pth")
```

## 載入模型

Torch 已經有基本保護，因此我們需要暫時關閉 `weights_only` 選項。當你載入該模型後，你會看到名為 `malicious_output.txt` 的檔案。這表示惡意行為已經在載入時發生。

```python
import torch

safe_model_path = "safe_model.pth"
malicious_model_path = "malicious_model.pth"

s_model = torch.load(safe_model_path)
m_model = torch.load(malicious_model_path, weights_only=False)
```

## 使用 `modelscan` 掃描模型

### 安全模型

```shell
modelscan -p safe_model.pth
```

```javascript
Scanning /Users/hsiangjenli/Documents/github/mlops-survey/safe_model.pth:safe_model/data.pkl using modelscan.scanners.PickleUnsafeOpScan model scan

--- Summary ---

 No issues found! 🎉

--- Skipped --- 

Total skipped: 7 - run with --show-skipped to see the full list.
```

### 惡意模型

```shell
modelscan -p malicious_model.pth
```

```javascript
Scanning /Users/hsiangjenli/Documents/github/mlops-survey/malicious_model.pth:malicious_model/data.pkl using modelscan.scanners.PickleUnsafeOpScan model scan

--- Summary ---

Total Issues: 1

Total Issues By Severity:

    - LOW: 0
    - MEDIUM: 0
    - HIGH: 0
    - CRITICAL: 1

--- Issues by Severity ---

--- CRITICAL ---

Unsafe operator found:
  - Severity: CRITICAL
  - Description: Use of unsafe operator 'system' from module 'posix'
  - Source: /Users/hsiangjenli/Documents/github/mlops-survey/malicious_model.pth:malicious_model/data.pkl

--- Skipped --- 

Total skipped: 5 - run with --show-skipped to see the full list.
```

# 🔁 重點回顧

1. 建立了一個安全模型與一個惡意模型（在載入時會產生輸出）
1. 使用 `modelscan` 掃描了兩個模型

# 🔗 參考資料

- https://github.com/protectai/modelscan
