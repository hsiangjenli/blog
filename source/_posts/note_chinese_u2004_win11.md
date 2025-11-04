---
title: '[note] Window 11 + Ubuntu 雙系統安裝紀錄'
date: 2025-01-17
tags:
- ubuntu
- windows
- intel rst
toc: true
slug: note-window-11-ubuntu
lang: zh-TW
permalink: zh-TW/note-window-11-ubuntu/
translations:
  en: /note-window-11-ubuntu.en/
---

<!-- # 🤯 先從反省開始

> 終於理解為什麼大部分的人若是有使用 Ubuntu 的需求，都是使用虛擬機或是安裝 WSL，以及 Windows 存在的必要性。

這次是抱著「***就算電腦系統掛掉，大不了就在花個幾千重買 Windows 11 授權，去光華請人重灌***」的決心，也要順出整個安裝的流程 ：） -->


# 🎒 預先準備

## 💻 電腦資訊

- **型號**：VivoBook 14 X1405VA-0041K
- **系統**：Windows 11
- **CPU**：i5-13500H
- **SSD**：NVMe SAMSUNG MZVL4512HBLU-00BTW
- **進入 BIOS 快捷鍵**：<kbd>F2</kbd>
- **選擇開機碟快捷鍵**：<kbd>F12</kbd>

<!-- more -->

## 🎯 目標

目前的 SSD 已經安裝上 win 11，目標是將 1 TB 的 SSD 做磁碟分割後安裝上 Ubuntu 20.04 LTS

- ![](https://img.shields.io/badge/Windows_11-0078d4?style=for-the-badge&logo=windows-11&logoColor=white) - 350 GB
- ![Ubuntu](https://img.shields.io/badge/Ubuntu%2020.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) - 650 GB

<!-- - BIOS 最新版
- Secure Boot 關閉
- Fast Boot 關閉
- CSM 關閉
- 使用 UEFI
- 在 BIOS 的 SATA Configuration 中確認格式是 AHCI -->


# 💻 操作流程

## 🚨 注意事項

> - 根據網路上的教學文章，大部分的修改都是在 BIOS 選單內
> - 但是，現在有些電腦的廠商會把這些選項關掉（避免使用者把電腦弄壞）
> - 這也讓更改變得麻煩，最後可能會搞到需要重設 windows，需把電腦備份好

1. 關掉 Bitlocker
2. 確認 BIOS 已更新至最新版本
   - 最新版本的 BIOS 通常包含修復錯誤和改進硬體相容性的功能，有助於避免安裝過程中的不必要問題
2. 將 BIOS 的 Boot Mode 設定為 UEFI
   - UEFI 是現代系統的標準開機模式，具有更好的硬碟分割支援、快速啟動和安全功能。Ubuntu 和 Windows 都建議使用 UEFI 而非傳統的 BIOS（CSM）
3. 關閉 Secure Boot
   - Secure Boot 的作用是防止未授權的操作系統啟動，但某些 Ubuntu 發行版本或自訂驅動程式可能無法正確通過驗證，導致安裝失敗
   - 在 BIOS 中找到 Secure Boot 設定，將其設為 Disabled
4. 關閉 Fast Boot（BIOS & Windows Control Panel）
   - Fast Boot 會跳過部分硬體初始化過程，可能導致 USB 開機盤無法被檢測到，從而影響 Ubuntu 的安裝
   - 進入 BIOS，找到 Fast Boot 設定，將其設為 Disabled
   - 在 Windows 中的 Control Panel 找到 Hardware and Sound 底下的 Power Option，把 Fast Starup 關閉 
5. 確認 SATA Configuration 設定為 AHCI 模式（這邊最有可能出現問題，BIOS 有些會沒有這些選項可以更改）
   - 不能是 Raid
6. 關閉 CSM（Compatibility Support Module）
   - CSM 是用於支援傳統 BIOS 的相容性模式，關閉後系統會專注於使用 UEFI 啟動，減少可能的相容性問題
   - 在 BIOS 中找到 CSM 設定，將其設為 Disabled

## Step 1 磁碟分割

- 首先會在 windows 上做磁碟分割，分成 windows 跟 ubuntu 兩個系統
- 在電腦上搜尋 **`Create and format hard disk partitions`**

![image](https://hackmd.io/_uploads/Bytew2Ovke.png)

## Step 2 關閉快速啟動

1. Windows - Fast Startup
1. BIOS - Fast Boot

### Windows

- 在 windows 中 的 control panel 找到管理電源的選項，把 fast startup 關掉

![image](https://hackmd.io/_uploads/SkOjV2_vkl.png)

![image](https://hackmd.io/_uploads/H19EHbqDyl.png)

![image](https://hackmd.io/_uploads/S1bSHZ9w1x.png)

![image](https://hackmd.io/_uploads/ry4Er2_Dkx.png)

## Step 3 跟 Intel RST 有關的 driver 刪除 [^ubuntu_rst]

> - 這個步驟會讓之後電腦開機的時候失敗，會需要整台電腦重設（需要有一顆強壯的心臟 💔💔💔...）
> - 但是重設完之後才可以順利把 RST 關掉（把硬碟從 Raid 改成 AHCI），否則 ubuntu 在安裝的時候會讀取不到這個 SSD

### 按 <kbd>Win</kbd> + <kbd>X</kbd> 快捷鍵後找到 Device Manager 

- 進去裡面找到 Storage Controllers，在裡面會看到 Intel RST 的 driver
   ![image](https://hackmd.io/_uploads/HyamMTuvyl.png)
- 這個就是安裝 ubuntu 過程中導致無法偵測到 SSD 的罪魁禍首！！！！
- 請按照 [Ubuntu Documentation - RST & Ubuntu installation](https://help.ubuntu.com/rst/) 裡面的步驟一步一步的卸載 Intel RST driver


### 按 <kbd>Win</kbd> + <kbd>R</kbd>，搜尋 `regedit`

1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\iaStorV\`
   - 找到 **Start** 選項，把值改成 0
   - 找到 **StartOverride** 把值改成 0
1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\storahci\`
   - 找到 **Start** 選項，把值改成 0
   - 找到 **StartOverride** 把值改成 0

### 把 Intel RST driver 卸載

- 把 Intel RST driver 完全 uninstall，然後重新開機
- 重新開機的過程會藍屏，上面是顯示 `INACCESSIBLE_BOOT_DEVICE`，解決方式就是重新設定整台電腦

### 重設完之後

- 一樣按 <kbd>Win</kbd> + <kbd>X</kbd> 進入 Device Manager 看 Storage Controllers 裡面確認 Intel RST 是否還在

    ![image](https://hackmd.io/_uploads/r1qe9f5DJx.png)

## Step 4 安裝 Ubuntu

### 使用隨身碟安裝 Ubuntu

- 按 <kbd>F12</kbd> 選擇隨身碟當作開機碟
- 因為已經預先切好磁碟區，Installation Type 就選 Something else
    ![image](https://hackmd.io/_uploads/rJstz95P1e.png)
- 一路按確認即可，後續安裝不太會有問題

### 驅動問題

- 過往安裝桌機跟自己舊筆電的時候都沒遇到 wifi 驅動問題
- 但是這台 vivobook 遇到了，最快的解法是直接買一個支援 linux 的無線連接器 
- TP-Link TL-WN725N22  
![image](https://hackmd.io/_uploads/SJfbN55PJe.png)


## 專有名詞
- CSM - Compatibility Support Module
- Intel RST - Intel Rapid Storage Technology

[^ubuntu_rst]: Ubuntu Documentation - RST & Ubuntu installation
https://help.ubuntu.com/rst/
