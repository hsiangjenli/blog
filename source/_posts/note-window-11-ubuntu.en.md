---
title: '[note] Windows 11 + Ubuntu dual-boot installation log'
date: 2025-01-17
lang: en
tags:
- ubuntu
- windows
- intel rst
toc: true
translation_key: note-window-11-ubuntu
slug: note-window-11-ubuntu
source_sha: 40503ee224d8c3d9be87999dc3ac804987d73021292b590b606ed23082325869
origin_lang: zh-TW
---

<!-- # 🤯 Start with reflection

> Finally understood why most people who need Ubuntu end up using a VM or installing WSL, and why Windows remains necessary.

This time I went in with the determination "***even if the computer system dies, at worst I'll spend a few thousand to buy a Windows 11 license and have someone at Guanghua re-install***", and I also want to document the entire installation process :) -->

# 🎒 Preparation

## 💻 Computer info

- **Model**: VivoBook 14 X1405VA-0041K
- **OS**: Windows 11
- **CPU**: i5-13500H
- **SSD**: NVMe SAMSUNG MZVL4512HBLU-00BTW
- **BIOS entry shortcut**: <kbd>F2</kbd>
- **Boot device selection shortcut**: <kbd>F12</kbd>

<!-- more -->

## 🎯 Goal

The current SSD already has Windows 11 installed. The goal is to partition the 1 TB SSD and install Ubuntu 20.04 LTS

- ![](https://img.shields.io/badge/Windows_11-0078d4?style=for-the-badge&logo=windows-11&logoColor=white) - 350 GB
- ![Ubuntu](https://img.shields.io/badge/Ubuntu%2020.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) - 650 GB

<!-- - Latest BIOS
- Secure Boot disabled
- Fast Boot disabled
- CSM disabled
- Use UEFI
- Verify SATA Configuration in BIOS is AHCI -->

# 💻 Procedure

## 🚨 Precautions

> - According to online guides, most changes are made inside the BIOS menu
> - However, some manufacturers hide these options (to prevent users from breaking the computer)
> - That makes changes troublesome, and you may end up needing to reset Windows, so back up your computer

1. Turn off Bitlocker
2. Ensure BIOS is updated to the latest version
   - The latest BIOS versions usually include bug fixes and improved hardware compatibility, which helps avoid unnecessary issues during installation
2. Set the BIOS Boot Mode to UEFI
   - UEFI is the modern standard boot mode with better disk partition support, faster booting, and security features. Both Ubuntu and Windows are recommended to use UEFI instead of legacy BIOS (CSM)
3. Disable Secure Boot
   - Secure Boot prevents unauthorized OS boots, but some Ubuntu releases or custom drivers may not pass verification and can cause installation failures
   - Find Secure Boot in the BIOS and set it to Disabled
4. Disable Fast Boot (BIOS & Windows Control Panel)
   - Fast Boot skips certain hardware initialization steps and may prevent USB boot media from being detected, affecting Ubuntu installation
   - In the BIOS, find Fast Boot and set it to Disabled
   - In Windows Control Panel under Hardware and Sound -> Power Options, turn off Fast Startup
5. Ensure SATA Configuration is set to AHCI (this is the most likely place to have issues; some BIOS won't expose these options)
   - It must not be RAID
6. Disable CSM (Compatibility Support Module)
   - CSM supports legacy BIOS compatibility. Disabling it makes the system rely on UEFI booting, reducing potential compatibility issues
   - Find CSM in the BIOS and set it to Disabled

## Step 1 Disk partitioning

- First, partition the disk in Windows to separate Windows and Ubuntu
- Search on the computer for **`Create and format hard disk partitions`**

![image](https://hackmd.io/_uploads/Bytew2Ovke.png)

## Step 2 Disable fast startup

1. Windows - Fast Startup
1. BIOS - Fast Boot

### Windows

- In Windows Control Panel find the power management options and turn off Fast Startup

![image](https://hackmd.io/_uploads/SkOjV2_vkl.png)

![image](https://hackmd.io/_uploads/H19EHbqDyl.png)

![image](https://hackmd.io/_uploads/S1bSHZ9w1x.png)

![image](https://hackmd.io/_uploads/ry4Er2_Dkx.png)

## Step 3 Remove drivers related to Intel RST [^ubuntu_rst]

> - This step may cause the computer to fail to boot and require a full reset (it takes a strong heart 💔💔💔...)
> - But after resetting you can successfully turn off RST (change the disk mode from RAID to AHCI); otherwise Ubuntu won't detect the SSD during installation

### Press <kbd>Win</kbd> + <kbd>X</kbd> and open Device Manager

- Inside, find Storage Controllers, where you'll see the Intel RST driver
   ![image](https://hackmd.io/_uploads/HyamMTuvyl.png)
- This is the culprit causing the SSD to be undetectable during the Ubuntu installation!!!!
- Follow the steps in [Ubuntu Documentation - RST & Ubuntu installation](https://help.ubuntu.com/rst/) to uninstall the Intel RST driver step by step

### Press <kbd>Win</kbd> + <kbd>R</kbd>, search for `regedit`

1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\iaStorV\`
   - Find **Start** and set its value to 0
   - Find **StartOverride** and set its value to 0
1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\storahci\`
   - Find **Start** and set its value to 0
   - Find **StartOverride** and set its value to 0

### Uninstall the Intel RST driver

- Fully uninstall the Intel RST driver, then reboot
- During reboot you may get a blue screen showing `INACCESSIBLE_BOOT_DEVICE`; the solution is to reset the whole computer

### After resetting

- Again press <kbd>Win</kbd> + <kbd>X</kbd>, enter Device Manager, and check Storage Controllers to confirm whether Intel RST is still present

    ![image](https://hackmd.io/_uploads/r1qe9f5DJx.png)

## Step 4 Install Ubuntu

### Install Ubuntu using USB flash drive

- Press <kbd>F12</kbd> and choose the USB drive as the boot device
- Since the partitions were pre-created, choose "Something else" for Installation Type
    ![image](https://hackmd.io/_uploads/rJstz95P1e.png)
- Keep confirming through the prompts; the rest of the installation should be fine

### Driver issues

- In previous desktop and my old laptop installs I didn't encounter Wi-Fi driver issues
- But this Vivobook had issues; the fastest solution was to buy a Linux-compatible wireless adapter
- TP-Link TL-WN725N22  
![image](https://hackmd.io/_uploads/SJfbN55PJe.png)


## Terminology
- CSM - Compatibility Support Module
- Intel RST - Intel Rapid Storage Technology

[^ubuntu_rst]: Ubuntu Documentation - RST & Ubuntu installation
https://help.ubuntu.com/rst/
