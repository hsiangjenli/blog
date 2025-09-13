---
title: '[Notice] Docker Model Runner Installation'
date: '2025-07-25'
lang: en
updated: '2025-08-19'
author:
- ChatGPT-5
- ' & Hsiang-Jen Li'
tags:
- llm
- docker
toc: true
translation_key: note-docker-model-runner-installation
slug: note-docker-model-runner-installation
source_sha: 7cc496b70fe2349caa0e90a01090d581b7ba25420fe2cd719aec8d487644e943
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 Introduction

On Ubuntu 24.04 while installing the Docker Model Plugin, I encountered an issue where apt could not find the package. It turned out the Docker repository was pointing to the wrong release (pointing to focal instead of noble).

> **⭐ Note**
> This article was initially drafted based on the real issue I encountered, with assistance from ChatGPT. I have verified the fix and revised the content to ensure it is accurate and clear for others facing a similar problem.

<!-- more -->

# 🚀 Quick Start

```shell
sudo apt-get update
sudo apt-get install docker-model-plugin -y

Hit:1 http://tw.archive.ubuntu.com/ubuntu noble InRelease                                 
Hit:2 http://tw.archive.ubuntu.com/ubuntu noble-updates InRelease                         
Hit:3 http://tw.archive.ubuntu.com/ubuntu noble-backports InRelease                       
Hit:4 https://packages.microsoft.com/repos/edge stable InRelease                          
Hit:5 https://brave-browser-apt-release.s3.brave.com stable InRelease                     
Hit:6 https://packages.microsoft.com/repos/code stable InRelease                          
Hit:7 http://security.ubuntu.com/ubuntu noble-security InRelease                          
Get:8 https://download.docker.com/linux/ubuntu focal InRelease [57.7 kB]                  
Hit:9 https://ppa.launchpadcontent.net/mozillateam/ppa/ubuntu jammy InRelease             
Fetched 57.7 kB in 7s (8650 B/s)
Reading package lists... Done
N: Skipping acquire of configured file 'main/binary-i386/Packages' as repository 'https://brave-browser-apt-release.s3.brave.com stable InRelease' doesn't support architecture 'i386'
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package docker-model-plugin
```

When I followed the tutorial [How to Run Docker Model Runner on Ubuntu 24.04](https://mrcloudbook.com/how-to-run-docker-model-runner-on-ubuntu-24-04/) I found that apt install could not find docker-model-plugin. The solution is

```shell
sudo apt-get update
sudo apt-get install \
  ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) \
    signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

# 🔁 Key Takeaways

- The cause was that Docker's APT repository pointed to the wrong release (focal instead of noble)
- Fixing this requires adding the correct Docker GPG key and configuring the proper repository for Ubuntu 24.04
- After updating the APT sources, the docker-model-plugin package can be installed

# 🔗 References

- [How to Run Docker Model Runner on Ubuntu 24.04](https://mrcloudbook.com/how-to-run-docker-model-runner-on-ubuntu-24-04/)
