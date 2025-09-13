---
title: '[tutorial] Build your own python package'
date: '2024-01-15'
lang: en
updated: '2025-02-28 (Refactored by ChatGPT-4o Mini)'
author:
  - 'Hsiang-Jen Li'
  - ' & ChatGPT-4o Mini'
tags:
- python
toc: true
---

# 📌 Introduction
Building your own Python package is beneficial for maintaining large projects, as it helps manage code that is otherwise scattered across directories.
<!-- more -->

# 🚀 Quick Start
- Create a `setup.py` file:
```python
from setuptools import setup, find_packages

setup(name="ntust_simslab", version="0.13", packages=find_packages())
```
- Create a `pyproject.toml` file:
```toml
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
- Sign up for a PyPI account at https://pypi.org/ to publish your package.

# 🔁 Recap
- Building a Python package helps maintain code organization in larger projects.
- Using `setup.py` is the traditional method, while `pyproject.toml` is the modern approach with Poetry.
- It's essential to have an account on PyPI to publish your package.

# 🔗 References
- https://github.com/NTUST-SiMS-Lab/tutorial-simple-pypkg
- https://pypi.org/
