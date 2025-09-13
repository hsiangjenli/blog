---
title: '[note] Gatsby Usage'
date: '2022-09-02'
lang: en
updated: '2025-02-28 (Refactored by ChatGPT-4o Mini)'
author:
  - 'Hsiang-Jen Li'
  - ' & ChatGPT-4o Mini'
tags:
- static-site
- gatsby
toc: false
---

# 📌 Introduction
This article provides a guide on how to install Gatsby and create a new Gatsby site using starter themes. It covers the installation steps, commands to set up a Gatsby site, and links to troubleshoot common errors.
<!-- more -->

# 🚀 Quick Start
## Install Gatsby
```shell=
npm install -g gatsby-cli
gatsby --version
```

![](https://i.imgur.com/GqF5btJ.png)

## gatsby-starter-blog
```shell=
gatsby new hjl https://github.com/gatsbyjs/gatsby-starter-blog
cd hjl
gatsby develop
```

## gatsby-starter-julia
```shell
gatsby new RN https://github.com/niklasmtj/gatsby-starter-julia
cd rn
```

## Use Legacy Peer Dependencies
```shell
--legacy-peer-deps
```

# 🔁 Recap
- Installation of Gatsby CLI using npm is straightforward with the command `npm install -g gatsby-cli`.
- After installation, you can check the version of Gatsby installed.
- To create a new Gatsby site, several starter themes can be used, such as `gatsby-starter-blog` and `gatsby-starter-julia`.
- Common errors related to npm and Gatsby are well documented through various links provided in the article.

# 🔗 References
- [Commands (Gatsby CLI)](https://www.gatsbyjs.com/docs/reference/gatsby-cli/)
- [npm WARN old lockfile The package-lock.json file was created with an old version of npm](https://stackoverflow.com/questions/68260784/npm-warn-old-lockfile-the-package-lock-json-file-was-created-with-an-old-version)
- [Error: Command failed with exit code 1: npm install #27548](https://github.com/gatsbyjs/gatsby/issues/27548)
- [npm-upgrade](https://www.npmjs.com/package/npm-upgrade)
