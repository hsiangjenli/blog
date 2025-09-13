---
title: '[note] 解決 fstatat canonical snap 目錄：權限被拒絕'
date: '2025-03-27'
lang: zh-TW
updated: '2025-03-31'
author:
- ChatGPT-4o
- ' & Hsiang-Jen Li'
tags:
- snap
- permission denied
toc: true
translation_key: note-solving-fstatat-canonical-snap-directory-permission-denied
slug: note-solving-fstatat-canonical-snap-directory-permission-denied
source_sha: 72ef3016c3bfd2ef96662235006426b66d7e4a12aa03cdca64aa2f9c22892a02
origin_lang: en
---

# 📌 介紹

在 Ubuntu 上使用 Snap 應用程式時，你可能會遇到與 fstatat 相關的令人困惑的權限錯誤。這篇筆記記錄了一個實際遇到的問題、探討可能的原因，並分享了有效的簡單解法。

> **⭐ 注意**
> 這篇文章最初是在我遇到的一個真實問題上，透過 ChatGPT 協助草擬。我已驗證了解法並修訂內容，以確保面臨類似問題的讀者能夠清楚、正確地參考。

<!-- more -->

# 📚 先決條件

- AppArmor
- LDAP (Lightweight Directory Access Protocol)
- fstatat
- snap

以下是本文提及的一些關鍵概念：

| Term | 中文說明 | 英文說明 |
|------|----------|----------|
| **AppArmor** | Ubuntu 的一種安全模組，用來限制應用程式能存取的資源，例如檔案、網路。 | Ubuntu 的安全模組，限制應用程式可以存取的資源。 |
| **LDAP (Lightweight Directory Access Protocol)** | 一種常見的用戶驗證協定，常用於企業環境集中管理帳號。 | 一種常見的用戶驗證協定，常用於企業環境中的集中式帳號管理。 |
| **fstatat** | 一個 Linux 系統呼叫，用來查詢檔案資訊。這個錯誤就是因為它失敗了。 | 一個用來取得檔案資訊的 Linux 系統呼叫。當這個呼叫失敗時會發生錯誤。 |
| **Snap** | Ubuntu 推出的套件系統，讓應用程式更容易安裝、升級與隔離管理。 | Ubuntu 的套件系統，讓應用程式易於安裝、更新和沙箱隔離。 |

- **非標準的主目錄**：使用者的主目錄位於預設 `/home/username` 路徑之外，通常在不同的磁碟或掛載點上
- **主目錄為符號連結**：看起來主目錄位於 `/home/username`，但實際上它是指向其他位置的符號連結

# 🧭 解決問題框架

## 問題

```
cannot fstatat canonical snap directory: Permission denied
```

## 根因分析

一般而言，這個問題有兩個常見原因：

1. 系統安裝在 NTFS 分割區上。
1. 主目錄被符號連結到非標準位置。

### 檢查檔案系統類型

```shell
df -T /

Filesystem     Type 1K-blocks     Used Available Use% Mounted on
/dev/nvme0n1p4 ext4 669754920 44435324 591224492   7% /
```

系統安裝在 ext4 分割區上


### 檢查符號連結

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

上述資料夾都不是符號連結

## 為什麼會這樣

我不知道……

## 解決方法

出乎意料地，執行下列指令解決了問題：

```
sudo dpkg-reconfigure apparmor
```

輸入你想使用的目的目錄

![圖片](https://hackmd.io/_uploads/Bk5RTUG6Jg.png)

重新啟動電腦~~

# 🔁 回顧

- ✅ 錯誤 `cannot fstatat canonical snap directory: Permission denied` 通常與 AppArmor 的限制有關
- ✅ 常見原因包括：
  - 將系統或主目錄放在 NTFS 分割區上
  - 主目錄為符號連結或位於非標準位置
- 🔍 在這個案例中：
  - 系統位於 ext4 分割區 — ✅ 不是 NTFS。
  - 主目錄不是符號連結 — ✅ 不是符號連結。
- ⚠️ 根本原因仍不明
- 🛠 問題透過以下步驟解決：
  1. 執行 `sudo dpkg-reconfigure apparmor`
  1. 在設定過程中輸入實際的主目錄路徑
  1. 重新啟動系統


# 🔗 參考資料
- [「在 Ubuntu 16.04 作為 LDAP 使用者執行 snap 應用程式時出現 'Permission denied'」](https://askubuntu.com/questions/1108780/permission-denied-when-running-snap-applications-on-ubuntu-16-04-as-a-ldap-use)
- [執行以 snap 套件安裝的應用程式時的 Permission denied 錯誤 - Ubuntu 17.04](https://askubuntu.com/a/1156839/912790)
