---
title: '[Tutorial] Toy Example for Scanning Models'
date: '2025-06-14'
lang: en
updated: '2025-06-14'
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o'
tags:
- mlsecops
toc: true
slug: tutorial-a-toy-example-of-scanning-models
---

# 📌 Introduction

This article demonstrates how to use a simple example and the `modelscan` tool to detect unsafe PyTorch models.

<!-- more -->

# 🚀 Quick Start

> Before getting started you need to install the following packages

```shell
pip install numpy torch modelscan
```

## Prepare a safe model

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

## Prepare a malicious model

This is a malicious model that produces output when you load it.

```python
from torch import nn
import torch
import os

class MaliciousModel:

    def __reduce__(self):
        print("Reduce called!")  # Should print
        return (os.system, ("echo 'This is a malicious model!' > malicious_output.txt",))
    
if __name__ == "__main__":
    model = MaliciousModel()

    # save the model
    torch.save(model, "malicious_model.pth")
```

## Loading models

Torch has basic protections, so we need to temporarily disable the `weights_only` option. After loading the model, you'll see a file named `malicious_output.txt`. This indicates the malicious action occurred during loading.

```python
import torch

safe_model_path = "safe_model.pth"
malicious_model_path = "malicious_model.pth"

s_model = torch.load(safe_model_path)
m_model = torch.load(malicious_model_path, weights_only=False)
```

## Using `modelscan` to scan models

### Safe model

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

### Malicious model

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

# 🔁 Review

1. Created a safe model and a malicious model (which produces output when loaded)
1. Scanned both models with `modelscan`

# 🔗 References

- https://github.com/protectai/modelscan
