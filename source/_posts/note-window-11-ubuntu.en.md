---
title: '[note] Windows 11 + Ubuntu dual-boot installation record'
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

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> <!-- # 🤯 Start with some reflection

> Finally understood why most people who need Ubuntu either use a virtual machine or install WSL, and why Windows remains necessary.

This time I proceeded with the mindset of "even if the computer system breaks, I can always spend a few thousand to buy a Windows 11 license and ask someone at Guanghua to reinstall" and documented the entire installation process. :)
-->

# 🎒 Preparations

## 💻 Computer info

- **Model**: VivoBook 14 X1405VA-0041K
- **OS**: Windows 11
- **CPU**: i5-13500H
- **SSD**: NVMe SAMSUNG MZVL4512HBLU-00BTW
- **BIOS access key**: <kbd>F2</kbd>
- **Boot device selection key**: <kbd>F12</kbd>

<!-- more -->

## 🎯 Goal

The current SSD already has Windows 11 installed. The goal is to partition the 1 TB SSD and install Ubuntu 20.04 LTS.

- ![](https://img.shields.io/badge/Windows_11-0078d4?style=for-the-badge&logo=windows-11&logoColor=white) - 350 GB
- ![Ubuntu](https://img.shields.io/badge/Ubuntu%2020.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) - 650 GB

<!-- - BIOS latest version
- Secure Boot disabled
- Fast Boot disabled
- CSM disabled
- Use UEFI
- In BIOS SATA Configuration confirm AHCI format -->

# 💻 Procedure

## 🚨 Notes / Precautions

> - According to online tutorials, most changes are made in the BIOS menu
> - However, some manufacturers disable these options (to prevent users from damaging the computer)
> - That makes changes more troublesome and may end up requiring a Windows reset, so back up your PC

1. Turn off BitLocker
2. Ensure BIOS is updated to the latest version
   - The latest BIOS usually includes bug fixes and improved hardware compatibility, which helps avoid unnecessary installation issues
3. Set the BIOS Boot Mode to UEFI
   - UEFI is the modern standard boot mode with better disk partition support, faster booting, and security features. Both Ubuntu and Windows recommend UEFI rather than legacy BIOS (CSM)
4. Disable Secure Boot
   - Secure Boot prevents unauthorized operating systems from booting, but some Ubuntu releases or custom drivers may fail verification and cause installation to fail
   - In the BIOS find the Secure Boot setting and set it to Disabled
5. Disable Fast Boot (BIOS & Windows Control Panel)
   - Fast Boot skips some hardware initialization and may prevent the USB installer from being detected, affecting the Ubuntu installation
   - In the BIOS find Fast Boot and set it to Disabled
   - In Windows Control Panel under Hardware and Sound → Power Options, turn off Fast Startup
6. Ensure SATA Configuration is set to AHCI mode (this is the most likely place for problems; some BIOS may not allow changing this)
   - It must not be RAID
7. Disable CSM (Compatibility Support Module)
   - CSM provides compatibility for legacy BIOS; disabling it makes the system focus on UEFI booting and reduces potential compatibility issues
   - In the BIOS find CSM and set it to Disabled

## Step 1 Disk partitioning

- First, partition the disk in Windows to separate Windows and Ubuntu
- Search on the PC for **`Create and format hard disk partitions`**

![image](https://hackmd.io/_uploads/Bytew2Ovke.png)

## Step 2 Turn off fast startup

1. Windows - Fast Startup
2. BIOS - Fast Boot

### Windows

- In Windows Control Panel, find the power management options and turn off Fast Startup

![image](https://hackmd.io/_uploads/SkOjV2_vkl.png)

![image](https://hackmd.io/_uploads/H19EHbqDyl.png)

![image](https://hackmd.io/_uploads/S1bSHZ9w1x.png)

![image](https://hackmd.io/_uploads/ry4Er2_Dkx.png)

## Step 3 Remove drivers related to Intel RST [^ubuntu_rst]

> - This step can cause the computer to fail to boot, requiring a full system reset (you need a strong heart 💔💔💔...)
> - However, only after resetting can you turn off RST (change the disk from RAID to AHCI); otherwise Ubuntu won't detect this SSD during installation

### Press <kbd>Win</kbd> + <kbd>X</kbd> and open Device Manager

- Go to Storage Controllers, where you'll see the Intel RST driver
   ![image](https://hackmd.io/_uploads/HyamMTuvyl.png)
- This is the culprit that prevents the SSD from being detected during Ubuntu installation!!!!
- Please follow the steps in [Ubuntu Documentation - RST & Ubuntu installation](https://help.ubuntu.com/rst/) to uninstall the Intel RST driver step by step


### Press <kbd>Win</kbd> + <kbd>R</kbd>, search for `regedit`

1. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\iaStorV\`
   - Find **Start** and change its value to 0
   - Find **StartOverride** and change its value to 0
2. `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\storahci\`
   - Find **Start** and change its value to 0
   - Find **StartOverride** and change its value to 0

### Uninstall the Intel RST driver

- Completely uninstall the Intel RST driver, then reboot
- During the reboot you may see a blue screen showing `INACCESSIBLE_BOOT_DEVICE`; the fix is to reset the entire computer

### After resetting

- Press <kbd>Win</kbd> + <kbd>X</kbd> again, open Device Manager and check Storage Controllers to confirm whether Intel RST is still present

    ![image](https://hackmd.io/_uploads/r1qe9f5DJx.png)

## Step 4 Install Ubuntu

### Install Ubuntu using a USB drive

- Press <kbd>F12</kbd> to choose the USB drive as the boot device
- Since the partitions were pre-created, choose Installation Type → Something else
    ![image](https://hackmd.io/_uploads/rJstz95P1e.png)
- Proceed through the installer; there should be no major issues afterwards

### Driver issues

- In past desktop and older laptop installs I didn't encounter Wi-Fi driver issues
- But this VivoBook had a problem; the fastest solution was to buy a Linux-compatible USB Wi-Fi adapter
- TP-Link TL-WN725N22
![image](https://hackmd.io/_uploads/SJfbN55PJe.png)


## Glossary
- CSM - Compatibility Support Module
- Intel RST - Intel Rapid Storage Technology

[^ubuntu_rst]: Ubuntu Documentation - RST & Ubuntu installation
https://help.ubuntu.com/rst/
