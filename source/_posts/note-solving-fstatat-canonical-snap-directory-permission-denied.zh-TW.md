---
title: '[note] 解決 fstatat canonical snap 目錄：權限被拒'
date: '2025-03-27'
updated: '2025-03-31'
author:
- ChatGPT-4o
- ' & Hsiang-Jen Li'
tags:
- snap
- permission denied
toc: true
slug: note-solving-fstatat-canonical-snap-directory-permission-denied
lang: zh-TW
source_sha: 72ef3016c3bfd2ef96662235006426b66d7e4a12aa03cdca64aa2f9c22892a02
origin_lang: en
permalink: zh-TW/note-solving-fstatat-canonical-snap-directory-permission-denied/
translations:
  en: /note-solving-fstatat-canonical-snap-directory-permission-denied.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹

在 Ubuntu 上使用 Snap 應用程式時，您可能會遇到與 fstatat 有關的令人困惑的權限錯誤。這篇筆記記錄了一個真實的問題，探討可能的原因，並分享實際有效的簡單解法。

> **⭐ 注意**
> 本文最初在遇到實際問題時，並在 ChatGPT 協助下草擬。我已驗證解決方案並修訂內容，以確保對遇到相似問題的人來說準確且清楚。


<!-- more -->

# 📚 前置條件

- AppArmor
- LDAP (Lightweight Directory Access Protocol)
- fstatat
- snap

以下是本文提及的一些關鍵概念：

| 術語 | 中文說明 | 英文說明 |
|------|----------|---------------------|
| **AppArmor** | Ubuntu 的一種安全模組，用來限制應用程式能存取的資源，例如檔案、網路。 | Ubuntu 的安全模組，用來限制應用程式可以存取的資源。 |
| **LDAP (Lightweight Directory Access Protocol)** | 一種常見的用戶驗證協定，常用於企業環境集中管理帳號。 | 一種常見的用戶驗證協定，常用於企業環境中的集中式帳號管理。 |
| **fstatat** | 一個 Linux 系統呼叫，用來查詢檔案資訊。這個錯誤就是因為它失敗了。 | 一個用於取得檔案資訊的 Linux 系統呼叫。當此呼叫失敗時會產生錯誤。 |
| **Snap** | Ubuntu 推出的套件系統，讓應用程式更容易安裝、升級與隔離管理。 | Ubuntu 的套件系統，讓應用程式更容易安裝、更新，並在沙盒中執行。 |

- **非標準家目錄**：使用者的家目錄位於預設 `/home/username` 路徑之外，通常位於不同的磁碟或掛載點上
- **家目錄為符號連結**：家目錄看起來在 `/home/username`，但實際上是指向其他位置的符號連結

# 🧭 問題解決框架

## 問題

```
cannot fstatat canonical snap directory: Permission denied
```

## 根本原因分析

一般而言，此問題常見有兩個原因：

1. 系統安裝在 NTFS 分割區。
1. 家目錄被符號連結到非標準位置。

### 檢查檔案系統類型

```shell
df -T /

Filesystem     Type 1K-blocks     Used Available Use% Mounted on
/dev/nvme0n1p4 ext4 669754920 44435324 591224492   7% /
```

系統安裝在 ext4 分割區


### 檢查是否有符號連結

```shell
ls -l /home/hsiangjenli/Documents/github

drwxrwxr-x 10 hsiangjenli hsiangjenli 4096  一  27 17:05 blog
drwxrwxr-x 11 hsiangjenli hsiangjenli 4096  三  28 17:03 default-of-credit-card-clients-mlops
drwxrwxr-x  8 hsiangjenli hsiangjenli 4096  一  29 16:40 hsiangjenli.github.io
drwxrwxr-x  5 hsiangjenli hsiangjenli 4096  三  27 14:28 java-from-python
drwxrwxr-x  4 hsiangjenli hsiangjenli 4096  一  29 17:19 pic-bed
drwxrwxr-x 11 hsiangjenli hsiangjenli 4096  二  16 08:44 python-package-template
drwxrwxr-x  6 hsiangjenli hsiangjenli 4096  一  27 17:25 star-to-review
```

這些資料夾都不是符號連結

## 為什麼會發生

我也不知道 ...

## 解決方案

令人驚訝的是，執行下列指令解決了問題：

```
sudo dpkg-reconfigure apparmor
```

輸入您想使用的目標目錄路徑

![image](https://hackmd.io/_uploads/Bk5RTUG6Jg.png)

重新啟動電腦~~

# 🔁 重點回顧

- ✅ 錯誤 `cannot fstatat canonical snap directory: Permission denied` 通常與 AppArmor 的限制有關
- ✅ 常見原因包括：
  - 系統或家目錄使用 NTFS 分割區
  - 家目錄為符號連結或位於非標準位置
- 🔍 在本例中：
  - 系統在 ext4 分割區 — ✅ 不是 NTFS。
  - 家目錄不是符號連結 — ✅ 不是符號連結。
- ⚠️ 根本原因仍不明
- 🛠 問題透過下列方式解決：
  1. 執行 `sudo dpkg-reconfigure apparmor`
  1. 在設定過程中輸入家目錄的實際路徑
  1. 重新啟動系統


# 🔗 參考資料
- [在 Ubuntu 16.04 以 LDAP 使用者執行 snap 應用程式時出現 'Permission denied'](https://askubuntu.com/questions/1108780/permission-denied-when-running-snap-applications-on-ubuntu-16-04-as-a-ldap-use)
- [執行以 snap 套件安裝的應用程式時出現 Permission denied 錯誤 - Ubuntu 17.04](https://askubuntu.com/a/1156839/912790)
