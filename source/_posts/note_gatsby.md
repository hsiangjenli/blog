---
title: "[note] Gatsby Usage"
date: 2022-09-02
tags: 
  - static-site
  - gatsby
---

## 安裝 gatsby
```shell=
npm install -g gatsby-cli
gatsby --version
```

![](https://i.imgur.com/GqF5btJ.png)

> [Commands (Gatsby CLI)](https://www.gatsbyjs.com/docs/reference/gatsby-cli/)


## Theme
### gatsby-starter-blog
```shell=
gatsby new hjl https://github.com/gatsbyjs/gatsby-starter-blog
cd hjl
gatsby develop
```
> http://localhost:8000/

![](https://i.imgur.com/Nkld8Pe.png)

---

### gatsby-starter-julia
```shell=
gatsby new RN https://github.com/niklasmtj/gatsby-starter-julia
cd rn
```

## Error
1. [npm WARN old lockfile The package-lock.json file was created with an old version of npm](https://stackoverflow.com/questions/68260784/npm-warn-old-lockfile-the-package-lock-json-file-was-created-with-an-old-version)
1. [Error: Command failed with exit code 1: npm install #27548](https://github.com/gatsbyjs/gatsby/issues/27548)
1. [npm-upgrade](https://www.npmjs.com/package/npm-upgrade)

```shell=
--legacy-peer-deps
```