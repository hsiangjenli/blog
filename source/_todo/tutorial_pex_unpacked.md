---
title: '[tutorial] PEX Unpacked: Building and Executing Python Executables with Ease'
date: '2024-08-15'
updated: '2025-02-28 (Refactored by ChatGPT-4o Mini)'
author:
  - 'Hsiang-Jen Li'
  - ' & ChatGPT-4o Mini'
tags:
- python
toc: true
---

# 📌 Introduction
This article introduces PEX (Python Executable), an open-source tool for creating virtual environments for executing Python code. It emphasizes the need for an existing Python environment on the user's computer and gives an overview of executing PEX files along with detailed instructions on installation and usage.
<!-- more -->

# 🚀 Quick Start
### Install PEX
```python
pip install pex
```

### Enter Interpretable pex environemt

Easy way

```python
pex 

# Enter an interpretable Pex environment specifying a specific Python version
pex --python=python3.12 # specific python version
```

Advanced

```python
# Specifying requirements
pex pandas
```

### Package `.py` into pex file

```python
# demo.py

import pandas as pd

def main():
    print(f"Hello, World! The pandas version is {pd.__version__}")

if __name__ == "__main__":
    main()
```

```python
pex -D . -e demo:main -o demo.pex -r requirements.txt
```

```python
# Execute PEX script
./demo.pex
```

# 🔁 Recap
- PEX stands for Python Executable and is used for creating isolated Python environments.
- It requires an existing Python interpreter as it does not include one when creating executables.
- PEX can be easily installed via pip, and it is capable of creating executable files from Python scripts.
- Users can specify Python versions and dependencies when entering a PEX environment.
- The article provides a step-by-step guide on packaging a `.py` script into a `.pex` executable.

# 🔗 References
- https://blog.csdn.net/gitblog_00001/article/details/138744439
- https://docs.pex-tool.org/buildingpex.html#specifying-entry-points
