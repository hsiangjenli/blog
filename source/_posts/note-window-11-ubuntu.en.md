---
title: '[note] Windows 11 + Ubuntu Dual-Boot Installation Record'
date: 2025-01-17
tags:
- ubuntu
- windows
- intel rst
toc: true
slug: note-window-11-ubuntu
lang: en
source_sha: 40503ee224d8c3d9be87999dc3ac804987d73021292b590b606ed23082325869
origin_lang: zh-TW
permalink: note-window-11-ubuntu.en/
translations:
  zh-TW: /zh-TW/note-window-11-ubuntu/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

<!-- # 🤯 Start with some reflection

> Finally understand why most people who need to use Ubuntu either use a virtual machine or install WSL, and why Windows remains necessary.

This time I went in with the attitude of "even if the computer system dies, at worst I'll just spend a few thousand to buy a Windows 11 license and pay someone at Guanghua to reinstall" and wanted to document the entire installation process :)

-->

# 🎒 Preparations

## 💻 Computer information

- **Model**: VivoBook 14 X1405VA-0041K
- **OS**: Windows 11
- **CPU**: i5-13500H
- **SSD**: NVMe SAMSUNG MZVL4512HBLU-00BTW
- **BIOS access key**: <kbd>F2</kbd>
- **Boot device selection key**: <kbd>F12</kbd>

<!-- more -->

## 🎯 Goal

The current SSD already has Win 11 installed. The goal is to partition the 1 TB SSD and install Ubuntu 20.04 LTS

- ![](https://img.shields.io/badge/Windows_11-0078d4?style=for-the-badge&logo=windows-11&logoColor=white) - 350 GB
- ![Ubuntu](https://img.shields.io/badge/Ubuntu%2020.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) - 650 GB

<!-- - BIOS up to date
- Secure Boot disabled
- Fast Boot disabled
- CSM disabled
- Using UEFI
- In BIOS SATA Configuration confirm AHCI -->


# 💻 Procedure

## 🚨 Notes

> - According to online tutorials, most changes are made in the BIOS menu
> - However, some manufacturers disable these options (to prevent users from damaging the computer)
> - That also makes changes troublesome, and in the end you may need to reset Windows, so back up your computer

1. Turn off BitLocker
2. Ensure BIOS is updated to the latest version
   - The latest BIOS typically includes bug fixes and improved hardware compatibility, which helps avoid unnecessary issues during installation
2. Set the BIOS Boot Mode to UEFI
   - UEFI is the modern standard boot mode, offering better disk partition support, faster startup, and security features. Both Ubuntu and Windows are recommended to use UEFI rather than legacy BIOS (CSM)
3. Disable Secure Boot
   - Secure Boot prevents unauthorized operating systems from booting, but some Ubuntu releases or custom drivers may not pass verification, causing installation failures
   - Find the Secure Boot setting in BIOS and set it to Disabled
4. Disable Fast Boot (BIOS & Windows Control Panel)
   - Fast Boot skips some hardware initialization and may cause the USB boot drive to not be detected, affecting Ubuntu installation
   - In BIOS, find Fast Boot and set it to Disabled
   - In Windows Control Panel under Hardware and Sound -> Power Options, turn off Fast Startup
5. Confirm SATA Configuration is set to AHCI mode (this is the most likely place to encounter issues; some BIOSes don't expose these options)
   - It must not be RAID
6. Disable CSM (Compatibility Support Module)
   - CSM provides compatibility for legacy BIOS; disabling it makes the system focus on UEFI booting and reduces potential compatibility problems
   - In BIOS, find CSM and set it to Disabled

## Step 1 Partition the disk

- First, partition the disk in Windows into Windows and Ubuntu systems
- Search on the computer for **`Create and format hard disk partitions`**

![image](https://hackmd.io/_uploads/Bytew2Ovke.png)

## Step 2 Turn off fast startup

1. Windows - Fast Startup
1. BIOS - Fast Boot

### Windows

- In Windows Control Panel, find the power management options and turn off fast startup

![image](https://hackmd.io/_uploads/SkOjV2_vkl.png)

![image](https://hackmd.io/_uploads/H19EHbqDyl.png)

![image](https://hackmd.io/_uploads/S1bSHZ9w1x.png)

![image](https://hackmd.io/_uploads/ry4Er2_Dkx.png)

## Step 3 Remove drivers related to Intel RST [^ubuntu_rst]

> - This step will cause the computer to fail to boot afterward and will require resetting the entire computer (you need a strong heart 💔💔💔...)
> - But only after resetting can you successfully turn off RST (change the disk from RAID to AHCI); otherwise Ubuntu cannot detect the SSD during installation

### Press <kbd>Win</kbd> + <kbd>X</kbd> and open Device Manager

- Inside, find Storage Controllers, where you will see the Intel RST driver
   ![image](https://hackmd.io/_uploads/HyamMTuvyl.png)
- This is the main culprit that causes the SSD to not be detected during the Ubuntu installation!!!!
- Please follow the steps in [Ubuntu Documentation - RST & Ubuntu installation](https://help.ubuntu.com/rst/) to uninstall the Intel RST driver step by step


### Press <kbd>Win</kbd> + <kbd>R</kbd>, search `regedit`

1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\iaStorV\`
   - Find the **Start** entry and change its value to 0
   - Find **StartOverride** and change its value to 0
1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\storahci\`
   - Find the **Start** entry and change its value to 0
   - Find **StartOverride** and change its value to 0

### Uninstall the Intel RST driver

- Completely uninstall the Intel RST driver, then reboot
- During reboot you will get a blue screen showing `INACCESSIBLE_BOOT_DEVICE`; the solution is to reset the entire computer

### After resetting

- Again press <kbd>Win</kbd> + <kbd>X</kbd> to open Device Manager and check Storage Controllers to confirm whether Intel RST is still present

    ![image](https://hackmd.io/_uploads/r1qe9f5DJx.png)

## Step 4 Install Ubuntu

### Install Ubuntu using a USB drive

- Press <kbd>F12</kbd> to select the USB drive as the boot device
- Since partitions were pre-created, choose Installation Type -> Something else
    ![image](https://hackmd.io/_uploads/rJstz95P1e.png)
- Keep confirming through the prompts; the subsequent installation should not have many problems

### Driver issues

- In the past, installing on a desktop and my old laptop I didn't encounter Wi-Fi driver issues
- But this Vivobook had issues; the quickest fix was to buy a Linux-compatible USB wireless adapter
- TP-Link TL-WN725N22  
![image](https://hackmd.io/_uploads/SJfbN55PJe.png)


## Glossary
- CSM - Compatibility Support Module
- Intel RST - Intel Rapid Storage Technology

[^ubuntu_rst]: Ubuntu Documentation - RST & Ubuntu installation
https://help.ubuntu.com/rst/
