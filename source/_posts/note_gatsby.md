---
title: '[Notes] Using Gatsby'
date: '2022-09-02'
lang: en
updated: 2025-02-28 (Refactored by ChatGPT-4o Mini)
author:
- Hsiang-Jen Li
- ' & ChatGPT-4o Mini'
tags:
- static-site
- gatsby
toc: false
translation_key: note-gatsby-usage
slug: note-gatsby-usage
source_sha: f6dcef86ea7da8af922ffb3705223e07b2fc0bd72a3e94139236995226990bdf
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> > Note: This page was automatically translated from the original English by an AI (gpt-5-mini-2025-08-07) and may contain minor inaccuracies.
> 
> # 📌 Introduction
This article provides a guide on how to install Gatsby and create a new Gatsby site using starter themes. It covers installation steps, commands to create a Gatsby site, and links for troubleshooting common errors.
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

## Using legacy peer dependencies
```shell
--legacy-peer-deps
```

# 🔁 Recap
- Installing the Gatsby CLI with npm is very simple; you can use the command `npm install -g gatsby-cli`.
- After installation, you can check the installed Gatsby version.
- To create a new Gatsby site, you can use various starter themes, such as `gatsby-starter-blog` and `gatsby-starter-julia`.
- Common npm and Gatsby-related errors are detailed via multiple links provided in the article.

# 🔗 References
- [Commands (Gatsby CLI)](https://www.gatsbyjs.com/docs/reference/gatsby-cli/)
- [npm WARN old lockfile: the package-lock.json file was created with an old version of npm](https://stackoverflow.com/questions/68260784/npm-warn-old-lockfile-the-package-lock-json-file-was-created-with-an-old-version)
- [Error: command failed with exit code 1: npm install #27548](https://github.com/gatsbyjs/gatsby/issues/27548)
- [npm-upgrade](https://www.npmjs.com/package/npm-upgrade)
