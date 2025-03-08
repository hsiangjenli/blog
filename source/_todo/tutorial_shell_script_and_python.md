---
title: '[tutorial] Combining Shell Script and Python for Efficient Automation'
date: '2023-04-05'
updated: '2025-02-28 (Refactored by ChatGPT-4o Mini)'
author:
  - 'Hsiang-Jen Li'
  - ' & ChatGPT-4o Mini'
tags:
- python
toc: true
---

# 📌 Introduction
This article discusses how to combine shell scripting and Python for automation, providing examples and practical steps for creating and executing scripts.
<!-- more -->

# 🚀 Quick Start
1. Write a shell script similar to the example below and save it as `run.sh`
    ```shell
    # run.sh
    python demo-1.py
    ```
2. Open Git Bash in the Terminal
3. `bash run.sh`

For Example-2:
1. Write a shell script similar to the example below and save it as `run.sh`
   ```shell
   echo "hello world - 1" | python demo-2.py
   echo "hello cat - 2" | python demo-2.py
   ```

> **💡Error** `run.sh: line 1: python: command not found`
> 1. Configure the path to your Python executable
>    - To find the path of your Python exe, you can use the command `where python`
> ```shell
> # run.sh
> PYTHON=/mnt/c/Miniconda3/python.exe
> "$PYTHON" demo-1.py
> ```

# 🔁 Recap
- Combining shell scripts with Python can enhance automation tasks.
- The article provides clear examples for writing and running scripts in both shell and Python.
- Users are guided to handle errors related to Python executable paths.

# 🔗 References
- https://i.imgur.com/VeXN5GO.png
