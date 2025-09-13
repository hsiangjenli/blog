---
title: '[tutorial] How to monitor CPU and memory usage in Python with psutil'
date: '2024-01-26'
lang: en
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- python
toc: true
translation_key: tutorial-how-to-use-psutil-to-monitor-cpu-and-memory-usage-in-python
slug: tutorial-how-to-use-psutil-to-monitor-cpu-and-memory-usage-in-python
source_sha: 1e350db776c57cb086bb34bc8298aeb53ae71a40da947b76d77400d5be1b36d1
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 Introduction
This article introduces psutil, an open-source Python package that provides system information such as CPU, memory, disk, and network. It covers installing psutil, handy functions for monitoring CPU and memory usage, and how to use a decorator to integrate it into Python code.
<!-- more -->

# 🚀 Quick Start
```python
pip install psutil
```

## Useful functions in psutil

### CPU
```python
psutil.cpu_count() # get the number of CPU
psutil.cpu_percent() # get the usage of all CPU
psutil.cpu_percent(percpu=True) # get the usage of per CPU
psutil.cpu_percent(interval=1) # get the usage of all CPU in 1 second, using interval will get more robust result
```

### Memory
```python
info = psutil.virtual_memory()

# total memory
info.total / 1024 / 1024 / 1024 # bytes -> GB

# the usage of memory
info.percent
```

#### MacOS
```python
# svmem(total=25769803776, available=7726628864, percent=70.0, used=9045114880, free=791134208, active=6949453824, inactive=6915768320, wired=2095661056)
```

#### Ubuntu
```python
# will get more information like buffers, cached etc..
# svmem(total=33541988352, available=25899790336, percent=22.8, used=7087771648, free=2703233024, active=15287881728, inactive=14264188928, buffers=965103616, cached=22785880064, shared=8265728, slab=904495104)
```

## How to integrate psutil into your program?

We can use a decorator to monitor CPU and memory usage for each function.
```python
import psutil

def monitor(func):
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        cur_func_pid = process.pid
        process = psutil.Process(cur_func_pid)

        func(*args, **kwargs)

        cpu_usage = process.cpu_percent(interval=0.01)
        memory_usage = process.memory_info().rss / 1024 / 1024 / 1024 # bytes -> GB

        print(f"CPU usage: {cpu_usage}%")
        print(f"Memory usage: {memory_usage}GB")

    return wrapper
```

### Example
```python
@monitor
def example_code():
    import numpy as np

    for i in range(100):
        np.random.rand(100, 100, 100)

example_code()
```

# 🔁 Recap
- psutil is an open-source Python package for system monitoring.
- It provides handy functions to obtain CPU and memory usage information.
- You can easily monitor a Python function's CPU and memory usage using a decorator.

# 🔗 References
- [Python常用库之psutil使用指南](https://zhuanlan.zhihu.com/p/380842937)
- [简单介绍psutil库（virtual_memory()、cpu_percent()](https://blog.csdn.net/qq_43391414/article/details/124431187)
- [使用 psutil 模組進行 Python 系統監控與分析](https://www.askpython.com/python-modules/psutil-module)
- [Python 中的 Psutil 模組](https://www.geeksforgeeks.org/psutil-module-in-python/)
- [Oracle Machine Learning for Python 的管理任務](https://docs.oracle.com/en/database/oracle/machine-learning/oml4py/2/mlpug/administrative-tasks-oracle-machine-learning-python1.html#GUID-0A8BF865-13EA-4A20-BAA9-7066066C45CB)
