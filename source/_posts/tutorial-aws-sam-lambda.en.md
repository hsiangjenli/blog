---
title: '[tutorial] Creating and Running Lambda Functions with AWS SAM'
date: '2025-06-20'
lang: en
updated: '2025-06-20'
author:
- Hsiang-Jen Li
tags:
- aws
- lambda
toc: true
translation_key: tutorial-aws-sam-lambda
slug: tutorial-aws-sam-lambda
source_sha: d2ef9bc3013711be7c831a3d1f7cf31e394ba009c28e7c3697a4759e2bf308e7
origin_lang: zh-TW
---

> Note: This page is an AI-generated (gpt-5-mini-2025-08-07) translation from Traditional Chinese and may contain minor inaccuracies.
> 
> # 📌 Introduction

This guide introduces how to use AWS SAM to create and run Lambda functions, including basic installation, an explanation of project structure, and the workflow for running Lambda locally.

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

### Initialize a SAM project
```shell
sam init
```

### Project structure overview

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

- `events/` - Contains mock event payload JSON files used to test the Lambda function
- `hello_world/` - Where the application lives; Lambda-related functions including the handler (e.g., app.py) and dependencies (e.g., requirements.txt)
- `tests/` - Unit test folder
- `samconfig.toml` - Stores SAM CLI execution parameters (such as deployment region, stack name, S3 bucket, etc.) to simplify settings when running `sam deploy`
- `template.yaml` - Defines all Lambda functions; the main IaC file (which services are used and their dependencies). It is an extension of AWS CloudFormation syntax.

#### `template.yaml`

> You can use the CloudFormation Linter tool [`cfn-lint`](https://github.com/aws-cloudformation/cfn-lint) to detect format and property errors in the file

**Header**

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  TODO....
```
1. **AWSTemplateFormatVersion** - The AWS CloudFormation version
1. **Transform** - Tells CloudFormation to use SAM to extend the template syntax
1. **Description** - Project description

**Content**

1. **Globals** - Default settings provided to Resources
2. **Resources** - The AWS resources to create. See [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html) and [AWS SAM resources and properties](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-resources-and-properties.html)
3. **Outputs** - Expected outputs after deployment (the information you need to know)

#### `samconfig.toml`

> See [AWS SAM CLI configuration file](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html), [Configuring the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-configure.html), [AWS SAM CLI command reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)

The purpose is to simplify the complexity of using sam commands

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

- Installation commands
- Understand the AWS SAM project structure
- Know the purposes of the specific files `template.yaml` and `samconfig.toml` and their related official documentation
- Invoke a simple "Hello World" Lambda function locally

# 🔗 References
- [Day02-環境準備(一)安裝AWS CLI、Docker、AWS SAM CLI](https://ithelp.ithome.com.tw/articles/10214954)
