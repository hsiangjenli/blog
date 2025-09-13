---
title: '[note] Windows 11 + Ubuntu 雙重開機安裝紀錄'
date: 2025-01-17
lang: zh-TW
tags:
- ubuntu
- windows
- intel rst
toc: true
translation_key: note-window-11-ubuntu
slug: note-window-11-ubuntu
source_sha: 0a39397aca847caf4a58bc91228f4e57e1385d6c68cda099bd87bd48b185e679
origin_lang: en
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。
> 
> > 注意：此頁面為 AI 生成（gpt-5-mini-2025-08-07）之繁體中文翻譯，可能包含些微錯誤。
>
> <!-- # 🤯 從一些反思開始
>
> > 終於理解為何大多數需要 Ubuntu 的人要麼使用虛擬機，要麼安裝 WSL，以及為何仍然需要 Windows。
>
> 這次的心態是「即便電腦系統壞掉，我也可以花幾千塊買個 Windows 11 授權，然後請光華的某人幫我重灌」，並將整個安裝流程記錄下來。 :)
> -->

# 🎒 準備工作

## 💻 電腦資訊

- **型號**: VivoBook 14 X1405VA-0041K
- **作業系統**: Windows 11
- **處理器**: i5-13500H
- **SSD**: NVMe SAMSUNG MZVL4512HBLU-00BTW
- **BIOS 進入鍵**: <kbd>F2</kbd>
- **開機裝置選擇鍵**: <kbd>F12</kbd>

<!-- more -->

## 🎯 目標

目前 SSD 已安裝 Windows 11。目標是將 1 TB SSD 分割出分割區並安裝 Ubuntu 20.04 LTS。

- ![](https://img.shields.io/badge/Windows_11-0078d4?style=for-the-badge&logo=windows-11&logoColor=white) - 350 GB
- ![Ubuntu](https://img.shields.io/badge/Ubuntu%2020.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) - 650 GB

<!-- - BIOS latest version
- Secure Boot disabled
- Fast Boot disabled
- CSM disabled
- Use UEFI
- In BIOS SATA Configuration confirm AHCI format -->

# 💻 步驟

## 🚨 注意 / 預防事項

> - 根據線上教學，大多數更改是在 BIOS 選單中進行
> - 但有些廠商會禁用這些選項（以防使用者誤傷電腦）
> - 這會讓更改變得麻煩，並可能最終需要重置 Windows，所以請備份你的電腦

1. 關閉 BitLocker
2. 確保 BIOS 已更新到最新版本
   - 最新的 BIOS 通常包含錯誤修正與較佳的硬體相容性，有助避免不必要的安裝問題
3. 將 BIOS 開機模式設為 UEFI
   - UEFI 是現代標準的開機模式，具有更佳的磁碟分割支援、更快的開機與安全性功能。Ubuntu 與 Windows 都建議使用 UEFI 而非傳統 BIOS（CSM）。
4. 關閉 Secure Boot
   - Secure Boot 會防止未經授權的作業系統開機，但某些 Ubuntu 版本或自訂驅動可能無法通過驗證，導致安裝失敗
   - 在 BIOS 中找到 Secure Boot 設定並設為 Disabled（停用）
5. 關閉 Fast Boot（BIOS 與 Windows 控制台）
   - Fast Boot 會略過部分硬體初始化，可能導致 USB 安裝碟無法被偵測，影響 Ubuntu 安裝
   - 在 BIOS 中找到 Fast Boot 並設為 Disabled
   - 在 Windows 控制台的「硬體與音效 → 電源選項」中關閉 Fast Startup（快速啟動）
6. 確保 SATA 設定為 AHCI 模式（這是最可能出問題的地方；某些 BIOS 可能不允許更改）
   - 它不能是 RAID
7. 關閉 CSM（相容性支援模組）
   - CSM 提供傳統 BIOS 相容性；關閉它可讓系統專注於 UEFI 開機並降低潛在相容性問題
   - 在 BIOS 中找到 CSM 並設為 Disabled

## 第一步：磁碟分割

- 先在 Windows 中分割磁碟以區分 Windows 與 Ubuntu
- 在電腦上搜尋 **`Create and format hard disk partitions`**

![image](https://hackmd.io/_uploads/Bytew2Ovke.png)

## 步驟 2 關閉快速啟動

1. Windows — 關閉 Fast Startup
2. BIOS — 關閉 Fast Boot

### Windows

- 在 Windows 控制台中，找到電源管理選項並關閉快速啟動（Fast Startup）

![image](https://hackmd.io/_uploads/SkOjV2_vkl.png)

![image](https://hackmd.io/_uploads/H19EHbqDyl.png)

![image](https://hackmd.io/_uploads/S1bSHZ9w1x.png)

![image](https://hackmd.io/_uploads/ry4Er2_Dkx.png)

## 步驟 3 移除與 Intel RST 相關的驅動程式 [^ubuntu_rst]

> - 這個步驟可能會導致電腦無法啟動，需要重置整台系統（你要有心理準備 💔💔💔...）
> - 但只有在重置之後你才能關閉 RST（將磁碟從 RAID 改為 AHCI）；否則 Ubuntu 在安裝時無法偵測到這顆 SSD

### 按 <kbd>Win</kbd> + <kbd>X</kbd> 開啟 裝置管理員

- 到 Storage Controllers，在那裡你會看到 Intel RST 驅動程式
   ![image](https://hackmd.io/_uploads/HyamMTuvyl.png)
- 這就是導致 Ubuntu 安裝時無法偵測 SSD 的禍首!!!!
- 請依照 [Ubuntu Documentation - RST & Ubuntu installation](https://help.ubuntu.com/rst/) 的步驟逐步解除安裝 Intel RST 驅動程式


### 按 <kbd>Win</kbd> + <kbd>R</kbd>，搜尋 `regedit`

1. `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\iaStorV\\`
   - 找到 **Start** 並將其值改為 0
   - 找到 **StartOverride** 並將其值改為 0
2. `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\storahci\\`
   - 找到 **Start** 並將其值改為 0
   - 找到 **StartOverride** 並將其值改為 0

### 解除安裝 Intel RST 驅動程式

- 完全解除安裝 Intel RST 驅動，然後重新啟動
- 在重新啟動期間你可能會看到藍屏顯示 `INACCESSIBLE_BOOT_DEVICE`；解法是重置整台電腦

### 重置後

- 再次按 <kbd>Win</kbd> + <kbd>X</kbd>，開啟裝置管理員並檢查 Storage Controllers，確認 Intel RST 是否仍在

    ![image](https://hackmd.io/_uploads/r1qe9f5DJx.png)

## 步驟 4 安裝 Ubuntu

### 使用 USB 安裝 Ubuntu

- 按 <kbd>F12</kbd> 選擇 USB 隨身碟為開機裝置
- 由於分割區已預先建立，安裝類型選擇 → Something else（其他）
    ![image](https://hackmd.io/_uploads/rJstz95P1e.png)
- 照著安裝程式繼續安裝；之後應該不會有重大問題

### 驅動程式問題

- 以往在桌機與較舊筆電安裝時，我沒有遇到 Wi‑Fi 驅動問題
- 但這台 VivoBook 出了問題；最快的解法是買一個相容 Linux 的 USB 無線網卡
- TP-Link TL-WN725N22
![image](https://hackmd.io/_uploads/SJfbN55PJe.png)


## 術語表
- CSM - 相容性支援模組
- Intel RST - Intel 快速儲存技術

[^ubuntu_rst]: Ubuntu 文件 - RST 與 Ubuntu 安裝
https://help.ubuntu.com/rst/
