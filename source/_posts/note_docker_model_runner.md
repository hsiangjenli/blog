---
title: '[note] Docker Model Runner Installation'
date: '2025-07-25'
updated: '2025-08-19'
author:
- ChatGPT-5
- ' & Hsiang-Jen Li'
tags:
- llm
- docker
toc: true
slug: note-docker-model-runner-installation
lang: en
permalink: note-docker-model-runner-installation.en/
translations:
  zh-TW: /zh-TW/note-docker-model-runner-installation/
---

# 📌 Introduction

While installing the Docker Model Plugin on Ubuntu 24.04, I ran into an issue where apt couldn’t locate the package. It turned out that the Docker repository was pointing to the wrong release (focal instead of noble).

> **⭐ Note** 
> This article was initially drafted with the help of ChatGPT based on a real issue I encountered. I verified the solution and revised the content to ensure accuracy and clarity for others facing similar problems.

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

When I following the tuorial from [How to Run Docker Model Runner on Ubuntu 24.04](https://mrcloudbook.com/how-to-run-docker-model-runner-on-ubuntu-24-04/). I found an issue that apt install cannot find docker-model-plugin. The solution is 

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

# 🔁 Recap

- The error occurred because the Docker APT repository was pointing to the wrong release (focal instead of noble)
- Fixing the issue required adding the correct Docker GPG key and configuring the proper repository for Ubuntu 24.04
- After updating the APT sources, the docker-model-plugin package became available for installation

# 🔗 References

- [How to Run Docker Model Runner on Ubuntu 24.04](https://mrcloudbook.com/how-to-run-docker-model-runner-on-ubuntu-24-04/)
