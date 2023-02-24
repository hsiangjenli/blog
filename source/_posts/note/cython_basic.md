---
title: 'note: Cython 基礎知識' 
date: 2023-02-23
tags: Python
toc: true
cover: https://i.imgur.com/65dETIz.jpg
thumbnail: https://i.imgur.com/65dETIz.jpg
chatgpt: true
---

## Cython
### 什麼是Cython？

<!-- more -->

> **Chat GPT:**
> Cython是一種基於Python的靜態編譯器，可以將Python代碼轉換成C語言代碼，進而編譯成機器碼，從而提高Python代碼的運行速度和效率。Cython既保留了Python的簡單易用和動態特性，同時也支持C語言的靜態類型聲明和高效內存管理，是一種非常強大的Python優化工具。Cython還可以用於編寫Python擴展、簡化C/C++代碼、加速數值計算、並行運算等方面的應用。

### Cython的優點
1. 執行速度快
1. 語法簡單
1. 靜態聲明
1. 兼容性高

### 應用場景
1. 讓 Python 執行更快
1. 簡化繁雜的 C 語法，改用 Python 的寫法，增加維護、可讀性

### 安裝和配置
```python
pip install cython
```
```shell
sudo apt install gcc
```

### Python和Cython的區別
| 特性            | Python                 | Cython   |
|:--------------- |:---------------------- |:-------- |
| 靜態類型聲明    | 不支持                 | 支持     |
| 靜態編譯        | 不支持                 | 支持     |
| 運行速度        | 較慢                   | 較快     |
| 內存使用        | 較高                   | 較低     |
| 與C/C++代碼集成 | 需要使用Cython或其他庫 | 直接支持 |
| 優化效果        | 較弱                   | 較強     |

### Cython中的靜態型別
| Python                  | Cython                                  |
|:----------------------- |:--------------------------------------- |
| `bool`                  | `bint`                                  |
| `int` `long`            | `char` `short` `int` `long` `long long` |
| `float`                 | `float` `double` `long double`          |
| `complex`               | `float complex` `double complex`        |
| `bytes` `str` `unicode` | `char *` `std::string`                  |

> **Reference**
> 1. [What are all the types available in Cython?](https://stackoverflow.com/questions/55451545/what-are-all-the-types-available-in-cython)

### 常用的Cython指令
|             |                                            |
|:----------- |:------------------------------------------ |
| `pyximport` | 直接從Cython代碼中引入模塊或函數           |
| `cdef`      | 聲明Cython中的C變量和函數                  |
| `cpdef`     | 定義既可被Python調用又可被Cython調用的函數 |
| `cimport`   | import `.pyx` `.pxd` `.pxi` 的檔案         |

> **Reference**
> 1. [Cython中def,cdef,cpdef的区别](https://www.cnblogs.com/lidyan/p/7474244.html)
> 1. [第13篇：Cython封装C++类接口](https://zhuanlan.zhihu.com/p/273570750)