---
title: "[tutorial] Build your own python package"
date: 2024-01-15
toc: true
tags:
    - python
---

## Why Build Your Own Python Package?
As projects grow in size, maintaing code scattered across different directories becomes increasingly challenges for programmers.

<!-- more -->

## How to build your own Python Package?

https://github.com/NTUST-SiMS-Lab/tutorial-simple-pypkg

- `setup.py`
- `pyproject.toml`

```python
# setup.py, the old way
from setuptools import setup, find_packages

setup(name="ntust_simslab", version="0.13", packages=find_packages())
```

```toml
# pyproject.toml, the new way
[tool.poetry]
name = "ntust_simslab"
version = "0.13"
description = "A simple example for building a Python package."
authors = ["Hsiang-Jen Li <hsiangjenli@gmail.com>"]
readme = "README.md"
packages = [{include = "ntust_simslab"}]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### Publish to pypi
You need to have an account - https://pypi.org/
