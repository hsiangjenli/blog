---
title: '[教學] 使用 Mailgun + Python 發送電子郵件'
date: '2025-03-08'
lang: zh-TW
updated: '2025-03-08'
author:
- Hsiang-Jen Li
tags:
- python
- mailgun
toc: true
translation_key: tutorial-using-mailgun-python-to-send-email
slug: tutorial-using-mailgun-python-to-send-email
source_sha: 75ff5ddac1d08195c10e921707badf0fc4a21d5e521cadacceb8b9227666d6e1
origin_lang: en
---

# 📌 介紹
本教學涵蓋如何使用 Mailgun 和 Python 發送電子郵件。你將學會如何設定 Mailgun、產生 API 金鑰，以及撰寫 Python 程式碼來發送有或沒有附件的電子郵件。

<!-- more -->

# 🚀 快速上手

## Mailgun
- Mailgun 提供免費方案，每天最多可發送 100 封電子郵件。

以下是你需要做的三件事
1. 生成 Mailgun API 金鑰
1. 記住你的 Mailgun 網域名稱（用於發送電子郵件）
1. 將你的電子郵件加入 Mailgun（Mailgun 僅允許發送電子郵件給已授權的收件者）

![圖片](https://hackmd.io/_uploads/Hk6SuIujkg.png)
<!-- ![image](https://hackmd.io/_uploads/HkFMY8_syx.png) -->

### 建立 API 金鑰

![圖片](https://hackmd.io/_uploads/ByhJkmFj1g.png)
![圖片](https://hackmd.io/_uploads/ry8XkmFikl.png)
![圖片](https://hackmd.io/_uploads/BJOHy7Fjkg.png)

### 從 Mailgun 取得你的網域

![圖片](https://hackmd.io/_uploads/SkoMbQtsyg.png)

### 設定並驗證你的電子郵件

1. 在 Mailgun 新增你的電子郵件
1. 檢查你的郵箱以完成驗證

![圖片](https://hackmd.io/_uploads/S14QdQtoke.png)
![圖片](https://hackmd.io/_uploads/HkU8_Qtj1g.png)
![圖片](https://hackmd.io/_uploads/Sko__7tjkg.png)
![圖片](https://hackmd.io/_uploads/Hkggi7Kikx.png)

## Python

完整程式碼見： [mailgun/demo.py](https://github.com/hsiangjenli/tiny-colab/blob/f62b74143bc029935914b28652b314bfa9512e5d/mailgun/demo.py)

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
從 Mailgun 發送電子郵件後，你可以檢查收件匣。郵件可能會被標示為垃圾郵件，請檢查垃圾郵件資料夾是否有該郵件。

![圖片](https://hackmd.io/_uploads/BJtOYQtoyl.png)

# 🔁 回顧
- Mailgun 設定：產生 API 金鑰、取得你的網域名稱，並驗證你的電子郵件
- Python 整合：使用 Mailgun API 與 Python 程式化地發送電子郵件
- 傳送附件：學習如何使用 Mailgun API 發送帶有附件的電子郵件

# 🔗 參考資料
- https://www.mailgun.com/blog/it-and-engineering/send-email-using-python/
- https://stackoverflow.com/questions/53861582/sent-email-via-python-using-mailgun-api
