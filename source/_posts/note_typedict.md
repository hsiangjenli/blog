---
title: "[note] Enhancing Code Clarity with TypedDict"
date: 2024-09-07
created_at: 2024-09-07
tags: python
toc: true
---

## The reason why we meed to use `TypedDict`

<!-- more -->

In general, we use **dataclasses** and **Pydantic** to store data. However, using **dictionaries** to store complex data is often an easier approach. Nevertheless, without predefined fields, it becomes difficult for later developers to maintain the code effectively. Using `TypedDict` allows the IDE to provide developers with suggestions, enhancing their development efficiency. But, `TypedDict` have some limitations; it cannot enforce strict type checking.

```python
from typing import TypedDict
import datetime


class News(TypedDict):
    title: str 
    create_date: datetime.datetime
    content: str
```

![image](https://hackmd.io/_uploads/HkpDhsFhR.png)


## Reference
- [【一分钟快学】提高 Python 3 代码质量：掌握 TypedDict 实现精确的类型安全字典](https://juejin.cn/post/7342790243009363977)