---
title: '[教學] 使用 Mailgun + Python 發送電子郵件'
date: '2025-03-08'
updated: '2025-03-08'
author:
- Hsiang-Jen Li
tags:
- python
- mailgun
toc: true
slug: tutorial-using-mailgun-python-to-send-email
lang: zh-TW
source_sha: 75ff5ddac1d08195c10e921707badf0fc4a21d5e521cadacceb8b9227666d6e1
origin_lang: en
permalink: zh-TW/tutorial-using-mailgun-python-to-send-email/
translations:
  en: /tutorial-using-mailgun-python-to-send-email.en/
---

> 註記：此頁為由 AI（gpt-5-mini-2025-08-07）自動翻譯自英文原文，可能含有少量不準確之處。

# 📌 介紹
本教學說明如何使用 Mailgun 與 Python 發送電子郵件。你將學會如何設定 Mailgun、產生 API 金鑰，以及撰寫 Python 程式碼來發送有或無附件的電子郵件。

<!-- more -->

# 🚀 快速開始

## Mailgun
- Mailgun 提供免費方案，允許每天最多發送 100 封電子郵件。

以下是三件你需要做的事
1. 產生 Mailgun API 金鑰
1. 記住你的 Mailgun 網域名稱（用於發送電子郵件）
1. 將你的電子郵件加入 Mailgun（Mailgun 只允許發送郵件給已授權的收件人）

![image](https://hackmd.io/_uploads/Hk6SuIujkg.png)
<!-- ![image](https://hackmd.io/_uploads/HkFMY8_syx.png) -->

### 建立 API 金鑰

![image](https://hackmd.io/_uploads/ByhJkmFj1g.png)
![image](https://hackmd.io/_uploads/ry8XkmFikl.png)
![image](https://hackmd.io/_uploads/BJOHy7Fjkg.png)

### 從 Mailgun 取得你的網域

![image](https://hackmd.io/_uploads/SkoMbQtsyg.png)

### 設定你的電子郵件並進行驗證

1. 將你的電子郵件加入 Mailgun
1. 檢查信箱以完成驗證

![image](https://hackmd.io/_uploads/S14QdQtoke.png)
![image](https://hackmd.io/_uploads/HkU8_Qtj1g.png)
![image](https://hackmd.io/_uploads/Sko__7tjkg.png)
![image](https://hackmd.io/_uploads/Hkggi7Kikx.png)

## Python

完整程式碼請見： [mailgun/demo.py](https://github.com/hsiangjenli/tiny-colab/blob/f62b74143bc029935914b28652b314bfa9512e5d/mailgun/demo.py)

```python
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN_NAME = os.getenv("MAILGUN_DOMAIN_NAME")
MAILGUN_API_URL = (
    f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN_NAME}.mailgun.org/messages"
)
```

```python
@error_handler_for_send_email
def send_email(from_email: str, to_email: Union[str, list], subject: str, text: str):
    # Define the email parameters
    email_data = {"from": from_email, "to": to_email, "subject": subject, "text": text}

    # Send the email
    r = requests.post(
        url=MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY), data=email_data
    )

    return r
```

```python
@error_handler_for_send_email
def send_email_with_attachment(
    from_email: str,
    to_email: Union[str, list],
    subject: str,
    text: str,
    attachment_paths: list,
):
    # Define the email parameters
    email_data = {"from": from_email, "to": to_email, "subject": subject, "text": text}

    # Read the attachment
    files = [
        ("attachment", open(attachment_path, "rb"))
        for attachment_path in attachment_paths
    ]

    # Send the email
    r = requests.post(
        url=MAILGUN_API_URL, auth=("api", MAILGUN_API_KEY), data=email_data, files=files
    )

    return r
```

## Gmail
從 Mailgun 發送郵件後，你可以檢查收件匣。郵件可能會被標記為垃圾郵件，請檢查垃圾郵件資料夾是否有該郵件。

![image](https://hackmd.io/_uploads/BJtOYQtoyl.png)

# 🔁 小結
- Mailgun 設定：產生 API 金鑰、取得你的網域名稱，並驗證你的電子郵件
- Python 整合：使用 Mailgun API 與 Python 程式化發送電子郵件
- 附件發送：學習如何使用 Mailgun API 發送包含附件的郵件

# 🔗 參考資料
- https://www.mailgun.com/blog/it-and-engineering/send-email-using-python/
- https://stackoverflow.com/questions/53861582/sent-email-via-python-using-mailgun-api
