---
title: '[tutorial] 使用 AWS SAM 建立與執行 Lambda 函數'
date: '2025-06-20'
updated: '2025-06-20'
author:
- Hsiang-Jen Li
tags:
- aws
- lambda
toc: true
slug: tutorial-aws-sam-lambda
lang: zh-TW
permalink: zh-TW/tutorial-aws-sam-lambda/
translations:
  en: /tutorial-aws-sam-lambda.en/
---

# 📌 Introduction

主要介紹如何使用 AWS SAM 建立與執行 Lambda 函數，包含基本安裝、專案結構說明，以及在本地端執行 Lambda 的操作流程

<!-- more -->

# 🚀 Quick Start

## AWS CLI

```shell
brew install awscli
```

## AWS SAM (Serverless Application Model) CLI

```shell
brew install aws-sam-cli
```

### 初始化 SAM project
```shell
sam init
```

### 介紹專案架構

```shell
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

- `events/` - 放置模擬事件（Event Payload）的 Json 檔，用來測試 Lambda 函數
- `hello_world/` - Application 的放置處，與 Lambda 有關的函數，包含 handler 函式（例如 app.py）以及依賴（例如 requirements.txt）
- `tests/` - 單元測試的資料夾
- `samconfig.toml` - 儲存 SAM CLI 執行參數（如部署區域、Stack 名稱、S3 bucket 等），用來簡化 `sam deploy` 時的設定流程
- `template.yaml` - 定義所有 Lambda 函數，IaC 的主要核心檔案（主要會用到哪些服務，互相的相依關係），是基於 AWS CloudFormation 的擴充語法

#### `template.yaml`

> 可使用 CloudFormation Linter 工具 [`cfn-lint`](https://github.com/aws-cloudformation/cfn-lint) 對檔案偵測格式、屬性錯誤

**Header**

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  TODO....
```
1. **AWSTemplateFormatVersion** - AWS CloudFormation 的版本號
1. **Transform** - 告訴 CloudFormation 這個模板要額外使用 SAM 來擴充語法
1. **Description** - 專案介紹

**Content**

1. **Globals** - 預設設定，提供給 Resources 使用
2. **Resources** - 建立的 AWS 資源，可參考 [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html)、[AWS SAM resources and properties](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-resources-and-properties.html)
3. **Outputs** - 在部署完後預期印出的結果（你需要知道哪些資訊）

#### `samconfig.toml`

> 可參考 [AWS SAM CLI configuration file](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html)、[Configuring the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-configure.html)、[AWS SAM CLI command reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)

目的是為了簡化使用 sam 指令時的複雜度

| Original                                                                 | Optimized with `samconfig`         |
|--------------------------------------------------------------------------|------------------------------------|
| `sam build --cached --parallel --use-containers`                        | `sam build`                        |
| `sam local invoke --env-vars locals.json`                               | `sam local invoke`                 |
| `sam local start-api --env-vars locals.json --warm-containers EAGER`   | `sam local start-api`              |

### Local Invoke

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

# 🔁 Recap

- 安裝指令
- 理解 AWS SAM 的專案架構
- 知道特定檔案 `template.yaml`、`samconfig.toml` 檔案用途以及欄位的官方相關文件
- 在地端 Invoke 一個簡單的 `Hello World` Lambda Function

# 🔗 References
- [Day02-環境準備(一)安裝AWS CLI、Docker、AWS SAM CLI](https://ithelp.ithome.com.tw/articles/10214954)
