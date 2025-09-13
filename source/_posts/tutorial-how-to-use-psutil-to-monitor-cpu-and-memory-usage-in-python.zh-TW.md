---
title: '[tutorial] 如何使用 psutil 在 Python 中監控 CPU 和記憶體 使用情況'
date: '2024-01-26'
lang: zh-TW
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- python
toc: true
translation_key: tutorial-how-to-use-psutil-to-monitor-cpu-and-memory-usage-in-python
slug: tutorial-how-to-use-psutil-to-monitor-cpu-and-memory-usage-in-python
source_sha: a52e60395798375f85fdbcb36e583fc0fc48cfc6263e2fe8a73e4303ac150ae5
origin_lang: en
---

# 📌 介紹
本篇文章介紹 psutil，一個開源的 Python 套件，提供有關 CPU、記憶體、磁碟與網路的系統資訊。內容涵蓋 psutil 的安裝並示範監控 CPU 與記憶體 使用的常用函式，以及如何使用裝飾器整合到 Python 程式碼中。
<!-- more -->

# 🚀 快速開始
```python
pip install psutil
```

## psutil 中的實用函式

### CPU
```python
psutil.cpu_count() # get the number of CPU
psutil.cpu_percent() # get the usage of all CPU
psutil.cpu_percent(percpu=True) # get the usage of per CPU
psutil.cpu_percent(interval=1) # get the usage of all CPU in 1 second, using interval will get more robust result
```

### 記憶體
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

## 如何在程式中整合 psutil？

我們可以透過裝飾器使用 psutil 來監控每個函式的 CPU 與記憶體 使用情況。
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

### 範例
```python
@monitor
def example_code():
    import numpy as np

    for i in range(100):
        np.random.rand(100, 100, 100)

example_code()
```

# 🔁 重點回顧
- psutil 是一個用於系統監控的開源 Python 套件。
- 它提供取得 CPU 與記憶體 使用資訊的實用函式。
- 你可以使用裝飾器來輕鬆監控 Python 函式的 CPU 與記憶體 使用情況。

# 🔗 參考資料
- [Python 常用庫之 psutil 使用指南](https://zhuanlan.zhihu.com/p/380842937)
- [簡單介紹psutil庫（virtual_memory()、cpu_percent()](https://blog.csdn.net/qq_43391414/article/details/124431187)
- [Python 使用 psutil 模組進行系統監控與分析](https://www.askpython.com/python-modules/psutil-module)
- [Python 中的 psutil 模組](https://www.geeksforgeeks.org/psutil-module-in-python/)
- [Oracle Machine Learning for Python 的管理工作](https://docs.oracle.com/en/database/oracle/machine-learning/oml4py/2/mlpug/administrative-tasks-oracle-machine-learning-python1.html#GUID-0A8BF865-13EA-4A20-BAA9-7066066C45CB)
