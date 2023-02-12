---
title: Setting up Miniconda on Ubuntu
date: 2023-02-13
tags: Ubuntu, Python
toc: true
cover: https://i.imgur.com/Cn2JYj8.png
thumbnail: https://i.imgur.com/Cn2JYj8.png
---
```shell!
sudo wget -c https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
<!-- more -->
```shell!
sudo chmod +x Miniconda3-latest-Linux-x86_64.sh
```

```shell!
./Miniconda3-latest-Linux-x86_64.sh
```

```shell
conda activate
conda env list
```

> Reference
> 1. [Setting up Miniconda on Ubuntu](https://medium.com/featurepreneur/setting-up-miniconda-on-ubuntu-4bf6bece6f9b)