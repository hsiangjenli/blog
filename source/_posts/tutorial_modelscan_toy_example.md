---
title: '[tutorial] A toy example of scanning models'
date: '2025-06-14'
updated: '2025-06-14'
author:
  - 'Hsiang-Jen Li'
  - ' & ChatGPT-4o'
tags:
  - mlsecops
toc: true
---

# 📌 Introduction

This article shows how to detect unsafe PyTorch models using a simple example and the `modelscan` tool.

<!-- more -->

# 🚀 Quick Start

> Before start you need to install following packages

```shell
pip install numpy torch modelscan
```

## Prepare Safe Model

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

## Prepare Malicious Model

This is a malicious model that will generate an output when you load it.

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

## Load model

Torch already has basic protection, so we need to temporarily turn off the `weights_only` option. After you load the model, you will see a file called `malicious_output.txt`. This means the malicious behavior has already happened suddenly.

```python
import torch

safe_model_path = "safe_model.pth"
malicious_model_path = "malicious_model.pth"

s_model = torch.load(safe_model_path)
m_model = torch.load(malicious_model_path, weights_only=False)
```

## Using `modelscan` to scan the model

### Safe Model

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

### Malicious Model

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

# 🔁 Recap

1. Created a safe model and a malicious model (which generates output on load)
1. Scanned both models using `modelscan`

# 🔗 References

- https://github.com/protectai/modelscan