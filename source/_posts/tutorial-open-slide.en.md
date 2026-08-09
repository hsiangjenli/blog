---
title: '[tutorial] open-slide Usage Tutorial'
date: '2026-07-03'
updated: '2026-07-03'
author:
- Hsiang-Jen Li
tags:
- ai
- skill
toc: true
slug: tutorial-open-slide
lang: en
permalink: tutorial-open-slide.en/
source_sha: 876e33331124f9748ef4855a4dd8df57cbe769a21e25d8605ae516d0314b87b8
origin_lang: zh-TW
translations:
  zh-TW: /zh-TW/tutorial-open-slide/
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

Use the open-slide skill to have AI quickly generate a presentation for you.

<!-- more -->

# 🚀 Hands-on

## Init Demo Slide

```shell
npx @open-slide/cli init my-demo-slide
```

![20260703192900](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703192900.png)

![20260703193024](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703193024.png)

> Generates a complete repo, including tools to start the presentation, Agent Skills, example slides, and more

## Start the presentation

- http://localhost:5173/

```shell
cd my-demo-slide
npm run dev
```

![20260703193221](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703193221.png)

![20260703193256](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703193256.png)

## Frequently used Skills

- `/create-slide`: used to create or draft a slide deck
- `/apply-comments`: used to handle `@slide-comment` tags

## Screenshots

### Using `/create-slide` to generate slides

![20260703201640](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703201640.png)

### Requirements Q&A (style, page count, effects, etc.)

![20260703201711](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703201711.png)

![20260703201906](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703201906.png)
![20260703201821](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703201821.png)

![20260703202157](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703202157.png)

### First version of the generated slides

![20260703211455](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703211455.png)

### Leaving comments on the slides

![20260703212008](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703212008.png)

1. Leave comments on the slides
2. Run `/apply-comments` in the terminal to apply changes based on the comments

### Second version of the generated slides

![20260703220930](https://raw.githubusercontent.com/hsiangjenli/pic-bed/main/images/20260703220930.png)

# 🔁 Key takeaways

1. Use `npx @open-slide/cli init my-demo-slide` to generate a complete slide project
2. Use `npm run dev` to start the presentation
3. Use `/create-slide` to generate slides
4. Use `/apply-comments` to modify slides based on comments
5. Currently open-slide is still under development; it only supports exporting to PDF, HTML, and images

# 🔗 References

- [Open Slide GitHub](https://github.com/1weiho/open-slide)
