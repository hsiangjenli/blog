---
title: '[note] AWS 遇到 InvalidToken 或是 InvalidClientTokenId'
date: '2025-07-11'
updated: '2025-09-16'
author:
- Hsiang-Jen Li
tags:
- aws
toc: true
lang: zh-TW
slug: note-aws-invalidtoken-invalidclienttokenid
permalink: zh-TW/note-aws-invalidtoken-invalidclienttokenid/
translations:
  en: /note-aws-invalidtoken-invalidclienttokenid.en/
---

# 📌 Introduction

使用 AWS CLI 時，若 MFA 產生的 `AWS_SESSION_TOKEN` 過期，會導致 `InvalidToken` 或 `InvalidClientTokenId` 錯誤

<!-- more -->

# 🚀 Quick Start

## 問題描述

Token ID、Secret 都是正確，卻在操作時無法順利登入（InvalidToken）

### 使用 `aws s3 ls` 出現下面錯誤

```shell
An error occurred (InvalidToken) when calling the ListBuckets operation: The provided token is malformed or otherwise invalid.
```

### 使用 `aws sts get-session-token` 產生 Token 時出現下面錯誤
```shell
An error occurred (InvalidClientTokenId) when calling the GetSessionToken operation: The security token included in the request is invalid
```

## 解決方法

會發生這類型問題在於過去曾經使用過 `AWS_SESSION_TOKEN`，可能已經過期導致無法順利登入，要先 unset 以下參數

<!-- `~/.aws/credentials` -->

```shell
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
```

# 🔁 Recap

- 使用 AWS MFA 進行登入的 Session Token 會在過期後無法使用
- 需要先把 `AWS_ACCESS_KEY_ID`、`AWS_SECRET_ACCESS_KEY`、`AWS_SESSION_TOKEN` 從環境變數中去除
<!-- - 由於當初使用一次性 Token 覆蓋了登入憑證，所以需要確認目前的 `aws_access_key_id` 以及 `aws_secret_access_key` 是否為當初在 AWS IAM 產出的 Access Key -->

# 🔗 References

- [An error occurred (InvalidToken) when calling the ListBuckets operation: The provided token is malformed or otherwise invalid. aws s3 ls](https://stackoverflow.com/questions/54837248/an-error-occurred-invalidtoken-when-calling-the-listbuckets-operation-the-pr)
- [aws cli get error "The security token included in the request is invalid"](https://stackoverflow.com/questions/40198127/aws-cli-get-error-the-security-token-included-in-the-request-is-invalid)
