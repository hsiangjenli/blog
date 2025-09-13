---
title: '[tutorial] Using Mailgun + Python to send email'
date: '2025-03-08'
lang: en
updated: '2025-03-08'
author:
  - 'Hsiang-Jen Li'
tags:
  - python
  - mailgun
toc: true
---

# 📌 Introduction
This tutorial covers how to send emails using Mailgun and Python. You’ll learn how to set up Mailgun, generate an API key, and write Python code to send emails with or without attachments.

<!-- more -->

# 🚀 Quick Start

## Mailgun
- Mailgun provides a free plan allows sending up to 100 emails per day.

Here are three things you need to do
1. Generate a Mailgun API key
1. Remember your Mailgun domain name (used for sending email)
1. Add your email to Mailgun (Mailgun only allows sending an email to authorized recipients)

![image](https://hackmd.io/_uploads/Hk6SuIujkg.png)
<!-- ![image](https://hackmd.io/_uploads/HkFMY8_syx.png) -->

### Create an API key

![image](https://hackmd.io/_uploads/ByhJkmFj1g.png)
![image](https://hackmd.io/_uploads/ry8XkmFikl.png)
![image](https://hackmd.io/_uploads/BJOHy7Fjkg.png)

### Get your domain from Mailgun

![image](https://hackmd.io/_uploads/SkoMbQtsyg.png)

### Set up your email & verify it

1. Add your email to mailgun
1. Check your mailbox to verify it

![image](https://hackmd.io/_uploads/S14QdQtoke.png)
![image](https://hackmd.io/_uploads/HkU8_Qtj1g.png)
![image](https://hackmd.io/_uploads/Sko__7tjkg.png)
![image](https://hackmd.io/_uploads/Hkggi7Kikx.png)

## Python

To see the entire code : [mailgun/demo.py](https://github.com/hsiangjenli/tiny-colab/blob/f62b74143bc029935914b28652b314bfa9512e5d/mailgun/demo.py)

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
After sending the email from Mailgun, you can check your inbox. It might be marked as spam, so you can check your spam folder to see if the email is there.

![image](https://hackmd.io/_uploads/BJtOYQtoyl.png)

# 🔁 Recap
- Mailgun Setup: Generate an API key, retrieve your domain name, and verify your email
- Python Integration: Use the Mailgun API with Python to send emails programmatically
- Sending Attachments: Learn how to send emails with attachments using the Mailgun API

# 🔗 References
- https://www.mailgun.com/blog/it-and-engineering/send-email-using-python/
- https://stackoverflow.com/questions/53861582/sent-email-via-python-using-mailgun-api
