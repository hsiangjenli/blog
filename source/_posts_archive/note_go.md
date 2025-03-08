---
title: "[note] Installation of Golang (PATH)"
date: 2024-08-27
created_at: 2024-08-27
tags: go
toc: true
---

## Install Go on macOS

<!-- more -->

1. **Install Go using Homebrew:**
   ```shell
   brew install go
   ```

2. **Verify the Installation:**
   After installation, check if Go binaries are located in `~/go/bin/`:

   ```shell
   ls ~/go/bin/
   ```

3. **Update PATH Temporarily:**
   If the Go binaries are present, temporarily add `~/go/bin` to your `PATH`:

   ```shell
   export PATH=$PATH:~/go/bin
   ```

4. **Update PATH Permanently:**
   To make this change permanent, add the following line to your `~/.zshrc` file:

   ```shell
   echo 'export PATH=$PATH:~/go/bin' >> ~/.zshrc
   source ~/.zshrc
   ```