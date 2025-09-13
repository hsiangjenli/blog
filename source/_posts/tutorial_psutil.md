---
title: '[tutorial] How to use psutil to monitor CPU and memory usage in python'
date: '2024-01-26'
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
This article introduces psutil, an open-source Python package that provides system information about CPU, memory, disks, and networks. It covers the installation of psutil and demonstrates useful functions for monitoring CPU and memory usage, as well as how to integrate it into Python code using decorators.
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

## How to integrate psutil into our code?

We can use psutil to monitor each function cpu and memory usage by using decorator.
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
- It provides useful functions to get CPU and memory usage information.
- You can use decorators to monitor CPU and memory usage of Python functions easily.

# 🔗 References
- [Python常用库之psutil使用指南](https://zhuanlan.zhihu.com/p/380842937)
- [简单介绍psutil库（virtual_memory()、cpu_percent()](https://blog.csdn.net/qq_43391414/article/details/124431187)
- [Python System Monitoring and Profiling with the psutil Module](https://www.askpython.com/python-modules/psutil-module)
- [Psutil module in Python](https://www.geeksforgeeks.org/psutil-module-in-python/)
- [Administrative Tasks for Oracle Machine Learning for Python](https://docs.oracle.com/en/database/oracle/machine-learning/oml4py/2/mlpug/administrative-tasks-oracle-machine-learning-python1.html#GUID-0A8BF865-13EA-4A20-BAA9-7066066C45CB)
