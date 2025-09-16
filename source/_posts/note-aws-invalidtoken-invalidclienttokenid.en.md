---
title: '[note] AWS encounters InvalidToken or InvalidClientTokenId'
date: '2025-07-11'
updated: '2025-09-16'
author:
- Hsiang-Jen Li
tags:
- aws
toc: true
lang: en
slug: note-aws-invalidtoken-invalidclienttokenid
source_sha: 58323dc76cfca29dd7dbdb4c49f1d34778130ce6394d9ccd27ebd4bd4225bf9e
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.

# 📌 Introduction

When using the AWS CLI, if the MFA-generated `AWS_SESSION_TOKEN` expires, it can cause `InvalidToken` or `InvalidClientTokenId` errors

<!-- more -->

# 🚀 Quick Start

## Issue description

The Token ID and Secret are correct, but operations fail to authenticate (InvalidToken)

### Running `aws s3 ls` shows the following error

```shell
An error occurred (InvalidToken) when calling the ListBuckets operation: The provided token is malformed or otherwise invalid.
```

### Running `aws sts get-session-token` to generate a token shows the following error
```shell
An error occurred (InvalidClientTokenId) when calling the GetSessionToken operation: The security token included in the request is invalid
```

## Solution

This issue occurs when an `AWS_SESSION_TOKEN` was previously used and has likely expired, causing authentication to fail. You should first unset the following environment variables

<!-- `~/.aws/credentials` -->

```shell
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
```

# 🔁 Recap

- Session tokens obtained via AWS MFA become unusable after expiration
- You need to remove `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` from environment variables
<!-- - Because a one-time token once overwrote the login credentials, verify whether the current `aws_access_key_id` and `aws_secret_access_key` are the Access Keys originally generated in AWS IAM -->

# 🔗 References

- [An error occurred (InvalidToken) when calling the ListBuckets operation: The provided token is malformed or otherwise invalid. aws s3 ls](https://stackoverflow.com/questions/54837248/an-error-occurred-invalidtoken-when-calling-the-listbuckets-operation-the-pr)
- [aws cli get error "The security token included in the request is invalid"](https://stackoverflow.com/questions/40198127/aws-cli-get-error-the-security-token-included-in-the-request-is-invalid)
