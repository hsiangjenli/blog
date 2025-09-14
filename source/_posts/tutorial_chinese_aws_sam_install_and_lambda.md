---
title: '[教學] 使用 AWS SAM 建立與執行 Lambda 函數'
date: '2025-06-20'
lang: zh-TW
updated: '2025-06-20'
author:
- Hsiang-Jen Li
tags:
- aws
- lambda
toc: true
slug: tutorial-aws-sam-lambda
---

# 📌 介紹

本指南介紹如何使用 AWS SAM 建立與執行 Lambda 函數，包含基本安裝、專案結構說明，以及在本機執行 Lambda 的流程。

<!-- more -->

# 🚀 快速開始

## AWS CLI

```shell
brew install awscli
```

## AWS SAM（Serverless Application Model）CLI

```shell
brew install aws-sam-cli
```

### 初始化 SAM 專案
```shell
sam init
```

### 專案結構總覽

```text
.
├── __init__.py
├── events
│   └── event.json
├── hello_world
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
├── README.md
├── samconfig.toml
├── template.yaml
└── tests
    ├── __init__.py
    ├── integration
    │   ├── __init__.py
    │   └── test_api_gateway.py
    ├── requirements.txt
    └── unit
        ├── __init__.py
        └── test_handler.py
```

- `events/` - 包含用來測試 Lambda 函數的模擬事件有效載荷 JSON 檔案
- `hello_world/` - 應用程式所在；Lambda 相關函數（例如 handler，例如 app.py）與相依套件（例如 requirements.txt）
- `tests/` - 單元測試資料夾
- `samconfig.toml` - 儲存 SAM CLI 執行參數（例如部署區域、stack 名稱、S3 桶等），以便在執行 `sam deploy` 時簡化設定
- `template.yaml` - 定義所有 Lambda 函數；主要的基礎設施即程式碼（IaC）檔案（哪些服務被使用以及它們的相依性）。它是 AWS CloudFormation 語法的擴充。

#### `template.yaml`

> 您可以使用 CloudFormation Linter 工具 [`cfn-lint`](https://github.com/aws-cloudformation/cfn-lint) 來偵測檔案中的格式與屬性錯誤

**標頭**

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  TODO....
```
1. **AWSTemplateFormatVersion** - AWS CloudFormation 的版本
1. **Transform** - 指示 CloudFormation 使用 SAM 擴充模板語法
1. **Description** - 專案描述

**內容**

1. **Globals** - 提供給資源的預設設定
2. **Resources** - 要建立的 AWS 資源。請參閱 [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html) 與 [AWS SAM resources and properties](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-resources-and-properties.html)
3. **Outputs** - 部署後的預期輸出（您需要的資訊）

#### `samconfig.toml`

> 參見 [AWS SAM CLI configuration file](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html)、[Configuring the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-configure.html)、[AWS SAM CLI command reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)

目的在於簡化使用 sam 指令時的複雜度

| 原本                                                                 | 使用 `samconfig` 後                  |
|---------------------------------------------------------------------|------------------------------------|
| `sam build --cached --parallel --use-containers`                    | `sam build`                        |
| `sam local invoke --env-vars locals.json`                           | `sam local invoke`                 |
| `sam local start-api --env-vars locals.json --warm-containers EAGER`| `sam local start-api`              |

### 本機呼叫

```shell
sam local invoke
```

```shell
No current session found, using default AWS::AccountId                                                       
Invoking app.lambda_handler (python3.13)                                                                    
Local image is up-to-date                                                                                  
Using local image: public.ecr.aws/lambda/python:3.13-rapid-x86_64.                                           
                                                                                                           
Mounting /Users/XXXXXX/Documents/TEST/hello_world as 
/var/task:ro,delegated, inside runtime container                                                            
START RequestId: f6a6ec50-58b2-432c-9381-ec45ca43b130 Version: $LATEST
END RequestId: e883464b-1216-43ae-b0fe-f7f803a73057
REPORT RequestId: e883464b-1216-43ae-b0fe-f7f803a73057  Init Duration: 1.26 ms  Duration: 381.91 ms     Billed Duration: 382 ms     Memory Size: 128 MB     Max Memory Used: 128 MB
{"statusCode": 200, "body": "{\"message\": \"hello world\"}"}
```

# 🔁 重點回顧

- 安裝指令
- 了解 AWS SAM 專案結構
- 了解 `template.yaml` 與 `samconfig.toml` 這些檔案的用途及其相關官方文件
- 在本機呼叫一個簡單的「Hello World」Lambda 函數

# 🔗 參考資料
- [Day02-環境準備(一)安裝AWS CLI、Docker、AWS SAM CLI](https://ithelp.ithome.com.tw/articles/10214954)
